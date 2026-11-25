# Brief — port the practice site to Preact + Signals (2026-10-20)

Goal: `scripts/mockweb/app.html` (vanilla JS, 1,207 lines, "v24") becomes a Preact + Signals app with **the same look,
behaviour, storage and test hooks**. No build step, no npm: the libraries are vendored as UMD files so the site keeps
working offline (`output/2_Practice_Web/index.html` + start.sh) and as the claude.ai artifact (app.html + data.js + clips.js).
This is a port, not a redesign: no new features, no changed Thai strings, no changed CSS.

## Read first
1. `CLAUDE.md` §2 entry "2_Practice_Web" — what the site does, versions v9–v24, storage keys, cloud sync, AI grading, karaoke.
2. `scripts/mockweb/app.html` — the whole engine. Read all of it once; it is the spec.
3. `scripts/build_mockweb.py` (152 lines) and `specs/SPEC_mockweb.md` (data schema; data is NOT changing).
4. Test harness (not in the repo): `HARNESS=/tmp/claude-1000/-home-beamkeerati-Documents-KMU-Korean/326a74af-b56e-4897-a48e-4376c89b6423/scratchpad/harness`
   — `run.py` (header comment explains it: fake Audio, virtual time, localStorage seed, driver script, screenshot) and the
   `d_*.js` drivers (each starts with a comment naming its scenario). Work folder for everything else:
   `WORK=/tmp/claude-1000/-home-beamkeerati-Documents-KMU-Korean/326a74af-b56e-4897-a48e-4376c89b6423/scratchpad/port`.

## Step 0 — baseline BEFORE touching anything
- `cp -r output/2_Practice_Web $WORK/baseline_web`.
- Run every `d_*.js` driver against the baseline with run.py (pick `--hash`/`--seed` from the driver's comment and from
  the set ids in data.js; when unsure use `--hash mini02-listening`), save each report as `$WORK/base_<driver>.txt`, and
  take `--screenshot` for d_view / d_split / d_size / d_conj (and the home page with no hash). Keep the exact command lines
  in `$WORK/commands.sh` so the same runs can be repeated on the new build.

## Step 1 — vendor the libraries → `scripts/mockweb/vendor.js`
Concatenate, in this order, with a header comment listing each package, exact version and URL:
preact `dist/preact.umd.js` · preact `hooks/dist/hooks.umd.js` · @preact/signals-core `dist/signals-core.umd.js` ·
@preact/signals `dist/signals.umd.js` · htm `dist/htm.umd.js`. Use current stable versions (preact 10.x, @preact/signals 2.x,
htm 3.1.x) from cdn.jsdelivr.net/npm/ (`curl -sSfL`). Verify in headless Chrome with a tiny page that the globals
`preact`, `preactHooks`, `preactSignalsCore`, `preactSignals`, `htm` exist and that a signal-driven component re-renders.
If a UMD build is missing for a package, say so and use the smallest working alternative that still needs no build step.

## Step 2 — the new `scripts/mockweb/app.html`
Keep verbatim: `<title>`, metas, the whole `<style>` block (same class names — the CSS is the visual contract), the
`#scroller` fixed scroll container, sticky `.strip`/`.prog` with `--strip-h`, `data-theme` / `data-palette` / `data-layout`
on `<html>`, the `--ts` font-size factor (no CSS zoom), the transport bar `#tp`.
Script order: `vendor.js` → `data.js` → `clips.js` → the app in a plain `<script>` (not type=module):
`const { h, render } = preact; const { signal, computed, effect, batch } = preactSignals; const html = htm.bind(h);`.

Keep as plain functions (copy, do not rewrite the logic): judgeText + jamo distance, grade(), aiKeys/aiGradeAll + AI_ERR,
the cloud module (pull/push, 1.5 s debounce, `SYNCED` regex, `stamp:<id>`, pull on load/visibilitychange/every 20 s on
home+cover), the exam clock (attempt.left frozen on pause/close, saveLeft every 10 s + pagehide, time-up → submit('timeup')),
audio (playClip with word boundaries, say(), wrapWords, karaoke, transport bar with userPaused/curFin), paperOf() and the
home-board grouping, setSize/theme/palette/layout.

Replace all innerHTML / template-string rendering and manual DOM patching with components:
App → Home (board grouped by paper; card colours c-good ≥ 80 % / c-done / c-live) · Cover · Paper (sections → items:
mc / ox / blank / write / speak / conj grid; answered colouring; result classes g-ok/g-half/g-ng/g-pend; `.fix.corr` red vs
`.fix.tip` under correct items; split layout `.sec-l`/`.sec-r`) · Results card · Strip (clock, progress bar, dock incl.
`#dock-t`, `#dock-n`, `#dock-ai`, `#ai-line`) · Transport bar · Settings.

State = signals: everything in `cur` (st, mode cover|exam|practice|result, ans, self, ai, played, left, endAt, startedAt,
lastMode, used, reason), the settings, the home-board data; `computed` for scores/progress/answered counts; `effect`s for
localStorage persistence and the cloud push. **The `kmuweb:` keys and their JSON shapes must not change** — the user's saved
progress (local and in the artifact db subtree `data/users/<id>/<setId>`) must load unchanged. `claude.use('db'|'user'|'sample')`
calls stay as they are.

Rules that matter on a real device:
- Typing never loses focus or caret: per-item components, per-key signals (or a Map of signals), `batch()` for multi-key
  writes; never re-render the whole paper on a keystroke.
- Karaoke must survive re-renders: the `.w` spans and `.sung/.now` classes are added imperatively — keep the spoken element
  out of the reactive path while a clip plays (memo the item, or render the spans from a signal), so a tick of the clock does
  not wipe the highlight.
- Measure `--strip-h` after render with a ResizeObserver on `.strip`; `#scroller` stays the only scrolling element.
- Keep `window.__kmu = { get cur(), openSet, startSet, submit, grade, aiGradeAll }`; `cur` returns a plain snapshot with the
  same field names (the harness drivers and the main session use it).
- Keep app.html readable: a short section-header comment per module, ≤ ~1,300 lines.

## Step 3 — build
Teach `build_mockweb.py` to copy `vendor.js` into `output/2_Practice_Web/` (and count it in the size line; the artifact
publish will pass it as a third file). Then run `python3 scripts/build_mockweb.py --no-audio` — never without `--no-audio`
(the main session generates clips).

## Step 4 — regression (the deliverable is the evidence, not the claim)
- Re-run `$WORK/commands.sh` against `output/2_Practice_Web`, save as `$WORK/new_<driver>.txt`, `diff` each pair.
  Every difference must be explained; timing jitter is fine, behaviour is not. Compare the screenshots with the baseline ones
  (same scenario, same size) and look at them.
- Add `$WORK/d_port.js`: open a set in practice mode → type into a write input and a blank → let the clock tick → check the
  values and focus survive → submit → results card present → dump `Object.keys(localStorage)` and the JSON of the ans/score/
  hist keys; run it on both builds and diff the dumps (shapes must be identical).
- If something cannot be made to pass, leave the behaviour as in the baseline rather than "improving" it, and report it.

## Done =
No artifact publish, no git commit (the main session does both). Final reply ≤ 250 words: files changed · library versions ·
harness results (which drivers matched, which differ and why) · what could not be tested (cloud, AI, real audio, iPad) ·
anything you changed on purpose. Do not paste file contents into the reply.
