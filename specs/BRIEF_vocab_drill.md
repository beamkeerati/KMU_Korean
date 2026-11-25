# BRIEF_vocab_drill — daily vocabulary drill + daily-test board on the practice site (v41, 2026-10-27)

The student failed today's daily test (4.5/10) because they could not recall vocabulary. They asked for the existing practice
website to give them **a vocabulary exercise for ALL words, every day**, plus the daily tests. Other agents are writing the daily-test
JSON sets (`content/mockweb/daily_*.json`, exam id `daily`, with a `group` string per paper); `scripts/build_mockweb.py` already
produces `vocab.js` (= `window.KMU_VOCAB`, 912 words) and `clips3.js` (one neural clip per word, key `"F|<ko>"`). Your job is the
front end in `scripts/mockweb/app.html` (Preact 10 + @preact/signals + htm, no build step, see the file's own header comments and
CLAUDE.md §2 "2_Practice_Web"). Keep every existing behaviour, id, CSS class and `kmuweb:` storage key working.

## Data
`window.KMU_VOCAB = [{u: 24, ko: "갈비탕", th: "คัลบีทัง (ซุปซี่โครง)", en: "galbitang…", cat: ""}, …]` — already sorted in drill
priority (units 24, 23, 25, 22, 26 … 37, then 21 … 5); `cat` = the centre's picture-theme name when the word is on a theme sheet.
Audio: `say(w.ko, 'F')` plays the clip (falls back to browser TTS). Load `vocab.js` and `clips3.js` with `<script>` tags after
`clips2.js` (both are also copied to output by the build; add them to the standalone list in the `size` print only if you touch
build_mockweb.py — you should not need to).

## Progress storage + sync
One record `kmuweb:vocab:srs` = `{ w: { [ko]: { b, d, n, x, l } }, days: { [YYYY-MM-DD]: { n, r } } }`
(b = Leitner box 0–5 · d = due day number (floor(localMidnight/86400000)) · n = times answered · x = times wrong · l = last day answered).
Make it sync like the sets: add `vocab` to the `SYNCED` regex and to the cloud module's `KEYS`, and let `pull()` handle the doc id
`srs` in addition to `SETS` ids (the doc then holds `{at, vocab: {...}}`; keep `stamp:srs` semantics identical to a set). Reads/writes
go through `store.get/set` like everything else. Never store names, only the word strings.

## Views (route `#vocab`, Strip button `🔤 ศัพท์`, Help section, home-board teaser card)
1. **วันนี้ (daily drill)** — the default tab. Builds today's session: all DUE words (d ≤ today, lowest box first, then latest unit
   first), then NEW words (never answered) in `KMU_VOCAB` order, up to the session size (chips 20 / 30 / 50, default 30, remembered in
   `kmuweb:vocab:size`). Two answer modes (chips, remembered): **พิมพ์** (default) shows the Thai (and English small) and the unit tag,
   the student types the Korean; grade with `judgeText(answer, [ko])` → 1 / 0.5 (near miss: show `diffText`) / 0; the ▶ button plays the
   word after grading. **การ์ด** shows the Korean big + ▶, tap to reveal Thai/English, then self-grade จำได้ / ไม่แน่ใจ / จำไม่ได้.
   Leitner: right → b+1 (max 5), due in [1, 2, 4, 7, 14, 30][b] days; half → same box, due tomorrow; wrong → b=0, due today and the
   word is re-queued at the end of the session until answered right. Show a progress bar (k / N), a running right/wrong count, and
   at the end a summary card: score, the wrong words with Thai (tap = ▶), buttons ทำอีกรอบเฉพาะที่ผิด / เริ่มชุดใหม่. Update `days[today]`.
   Enter submits; after an answer the next card appears on Enter or ถัดไป. Keyboard-friendly on iPad (focus the input).
2. **ตามบท (by unit)** — chips 5 … 37 and ทั้งหมด; a chip starts a session with ALL words of that unit (typed mode or card mode as chosen),
   same grading, same Leitner updates. The chip shows learned/total for that unit.
3. **สถิติ** — totals: words, seen (n>0), learned (b≥2), mastered (b≥4), due today, days practised (streak of consecutive days);
   per-unit bars (learned/total, mastered darker); the 20 most-missed words (x desc) as a list with Thai and ▶.
Design: reuse the existing CSS variables/classes (paper, card, btn, badge, grp, progress panel) so it looks like the rest of the site in
every tone and theme; works at phone width; no new libraries.

## Home board
- Add an `EXAMS` entry `{ id: 'daily', title: '매일시험 (ข้อสอบประจำวัน)', date: null, when: 'ทุกวันหลังเรียนบทใหม่ · 10 ข้อ · นับเป็นคะแนนเก็บ 쓰기 10', note: 'ข้อสอบจริงที่สอบไปแล้วทุกบท + เก็งข้อสอบของวันพรุ่งนี้ · ทำซ้ำได้ไม่จำกัด' }`
  — `dday()` must tolerate a null date (show nothing). Also `{ id: 'final', title: '기말시험 · 복습시험 ③④ (เล่ม 1-2)', date: '2026-11-06', when: 'ศ. 6 พ.ย. 복습시험 ③ 22~29과 · พ. 18 พ.ย. ④ 30~37과 · ศ. 20 / จ. 23 พ.ย. 기말', note: '' }` (no sets yet; an exam without sets is skipped already).
- `groupOf(st)`: a set's own `group` string wins over the `GROUPS` rules (sets sharing the string form one group; note = ''). Sort the
  daily groups newest unit first (parse `NN과` from the label; `🔮` prediction group first).
- Put a teaser card at the top of the home board: today's due count + new-word suggestion + a button → `#vocab`.
- Strip brand small text: `รวมแบบฝึกก่อนสอบ · 5~37과`.

## Regression (must do)
`python3 scripts/build_mockweb.py --no-audio` must succeed (it validates every JSON; if a `daily_*.json` written by another agent fails
validation at that moment, wait a minute and retry — do not edit those files). Then headless Chrome
(`chromium --headless=new --screenshot=… --window-size=1200,900 file://…/output/2_Practice_Web/index.html#vocab` or whatever
chromium/google-chrome exists; `which chromium chromium-browser google-chrome`) screenshots of: home, `#vocab` (daily drill with one
card answered — drive it via `window.__kmu` hooks you add: `__kmu.vocab.start(n)`, `.answer(text)`), `#profile`, and one set cover
(`#mid-writing-a`). Look at the PNGs. Also check in the browser console that no error is thrown on load and that `localStorage`
`kmuweb:vocab:srs` updates after an answer. Report the screenshot paths.

## Also
- Help section: a paragraph on the vocab drill (what the boxes mean, that progress syncs on the claude.ai link).
- Version comment at the top of the file: v41 — vocabulary drill + daily-test board.
- Do not touch other repo files except app.html (and CLAUDE.md is Fable's). Report: what you added (functions/ids), storage keys,
  anything unfinished.
