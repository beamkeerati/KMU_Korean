# BRIEF — practice-site UX/UI pass (written 2026-11-22, Opus, for a fresh session)

> **STATUS 2026-11-23: DONE (v72).** Answers to §5: computer first · full redesign · all phases then publish once; the user also asked for better
> transitions everywhere. All of §3 + a full restyle shipped in app.html v72 (log: docs/LAYOUT.md); run.sh all PASS. **Publish still pending** —
> the session had no Artifact tool; it is an app.html-only change (no `files`).

The user (Thai, reply in Thai, short) asked for a better user experience + UI on the practice site and approved seeing a plan first.
This file carries the audit, the plan and the rules so a new session does not redo them. **Nothing has been changed in app.html yet.**

## 0. Start here
1. Ask the user the three open decisions (§5) with AskUserQuestion — they were asked on 11/22 and not answered yet.
2. Model plan the user was given: **phases 1–2 = Sonnet 5.5** (CSS + page templates, low risk) · **phase 3 = Opus 5.5** (touches the exam
   paper and attempt state). Fable is not needed. Budget estimate given: phase 1 ≈ 90k · phase 2 ≈ 60k · phase 3 ≈ 130k tokens
   (lean variant ≈ 150k total: phone shots only, skip vocab + profile pages).
3. Exams: 말하기 기말 **Mon 11/23**, 기말 발표 Tue 11/24. Recommended (not yet confirmed): publish phases 1–2 any time; phase 3 only after 11/23.

## 1. Where things are (scripts/mockweb/app.html, 2,158 lines ≈ 70k tokens — never Read it whole; `grep -n "/\* -\{10,\}"` lists the sections)
| Lines (11/22) | Section |
|:---|:---|
| 16–491 | CSS (tokens on :root, dark mode, 6 palettes `data-palette`; breakpoints at 82 · 109 · 141 · 171 · 340 · 354 · 365 · 370 · 452 · 486–487) |
| 531 | helpers + storage — **the `kmuweb:` keys and their JSON shapes are the contract** (cloud sync merges them) |
| 750 / 758 | routing (home / set / help) · `dday()` |
| 942 | submit → grade → results |
| 1074–1222 | cloud sync — **do not touch** |
| 1223 | Strip (top bar) · Transport (audio bar) · Dock (floating time/progress pill) |
| 1279–1415 | Card · CATS (hub categories) · groupsOf/Group · Crumbs · Tile · ResumeBar · Home · CatHead · UnitGrid · UnitPage · Category |
| 1416 | Cover (set cover page, RULES text per skill) |
| 1450 | the paper (header, bars, sections, items) |
| 1625 / 1744 / 2088 | profile (#profile) · vocabulary drill (#vocab) · help page + routing shell |

Page scrolls inside fixed `#scroller` (iPad Safari grows an iframe to its content), so any new bottom bar lives inside that frame and pads
for `env(safe-area-inset-bottom)`.

## 2. Audit (screenshots 390×844 phone + 1024×768 tablet, empty profile)
1. **Home**: a how-to paragraph tops the page every visit · the 기말 hero tile says **"ผ่านแล้ว"** although 말하기 is 11/23 and 발표 11/24 —
   CATS `final` holds one `date` (11/20) and `dday()` prints ผ่านแล้ว after it · 10 tiles of equal height = 2–3 screens of scrolling ·
   vocabulary has three entrances (strip button 🔤, the VTeaser card, the ทดสอบศัพท์ tile).
2. **Top strip on phones**: four tiny unlabeled icon buttons (⚙ 🔤 👤 วิธีใช้).
3. **Category page (#x/final)**: 6 lines of note before the first set · 30 sets on one page, no filter · cards are 2 narrow columns on a phone,
   set titles wrap to 4 lines.
4. **Cover**: on a phone the rules push ▶ เริ่มสอบจริง / ✎ ฝึกทำ below the fold — scroll needed every time.
5. **Paper**: header + practice bar + progress box fill the first screen · progress shown twice (sticky box + Dock) · the Dock covers item
   text at the bottom right · the same 💡 hint (3 lines) repeats under every item of a section (24× in final-combine) · no way to jump to item N.
6. **Vocab (#vocab)**: settings fill the screen, the ▶ start button is at the bottom.
7. **Profile**: the score table overflows a phone — the 4th column is cut.
8. Results page **not audited yet** (submission did not trigger in the headless run) — look at it first in phase 3.

## 3. Plan
**Phase 1 — home + navigation**
- Phones (< 640 px): a bottom tab bar with labels — หน้าแรก · ศัพท์ · คะแนน · ตั้งค่า; wider screens keep the top strip.
- A "วันนี้" card at the top of home: countdown to the next exam not yet past (needs a list of dates per category, e.g. `dates: [...]`,
  pick the first ≥ today; fixes ผ่านแล้ว), the sets left half-done (absorbs ResumeBar), vocabulary due today (absorbs VTeaser).
- Category tiles become compact rows; the 🗂️ past-exams section is collapsed by default. The how-to text moves to the help page.
  One entrance for vocabulary.

**Phase 2 — category page + cover**
- Tap filters: skill (쓰기 · 듣기 · 읽기 · 말하기) and status (ยังไม่ทำ · ทำแล้ว · ต่ำกว่า 80%); category note collapsed to 1 line + "อ่านต่อ".
- Set cards on phones = one full-width row: title, items/minutes, last score as a coloured bar.
- Cover: start buttons first, rules in a collapsible block, back button top left.

**Phase 3 — paper, results, vocab, profile** (Opus; run the sync tests)
- Paper header shrinks to one line on phones; progress lives only in the bottom bar, which must not cover item text (pad the paper bottom).
- A hint repeated across a section's items shows once under the section heading.
- Tapping the bottom bar opens a grid of item numbers coloured by state (unanswered / answered / wrong after grading) → jump to the item.
- Results: summary on top, a "ดูเฉพาะข้อที่ผิด" toggle.
- Vocab: start button on top, settings collapsed. Profile on phones: one card per skill instead of the wide table.

**Everywhere**: secondary text ≥ 14 px, tap targets ≥ 44 px, clearer status colours; keep dark mode + the 6 palettes + font-size setting.

## 4. Do not touch
Set data (content/mockweb/*.json), grading, audio/clips, the AI teacher, cloud sync (1074–1222), the `kmuweb:` storage keys/shapes.
Any change to store / attempt / submit code → `bash scripts/mockweb/test/run.sh` must print no FAIL.

## 5. Open decisions (ask first)
1. Main device for practice: phone · iPad · computer → decides which layout is polished first and which shots to take.
2. Scope: **recommended** = restructure + clean up, keeping the "exam paper" look · alternative = a full visual redesign (costs more).
3. Timing: **recommended** = phases 1–2 published now, phase 3 after the 말하기 exam on 11/23.

## 6. Verify + publish
- Build after every app.html edit: `python3 scripts/build_mockweb.py` (copies app.html → output/2_Practice_Web/index.html; no new clips).
- Screens: `bash scripts/mockweb/test/shot.sh` (usage in its header; shots → extracted/web_shots/) then `--sheet` to view 4 at once.
  Before/after for: home · #x/final · #x/daily · a cover · a paper in ฝึกทำ (final-combine) · a listening paper (final-listening-a) ·
  results · #vocab · #profile; plus dark mode once (Settings → ธีม) and the device the user picks.
- Publish per CLAUDE.md §2.3: file_path scripts/mockweb/app.html, url https://claude.ai/artifact/14Xbi9kWyQgDryHzk7kuzm, `files` = only the
  output files that changed (an app.html-only change sends no `files`); omit `capabilities`. If a publish arms a watch, stop it
  (ArtifactComments watch on:false) — CLAUDE.md says not to keep one.
- After: a `<!-- v72 … -->` line at the top of app.html, the "Current" line in CLAUDE.md §2.3, the version log in docs/LAYOUT.md,
  a line in docs/HISTORY.md. Commit only when the user asks; never add a Co-Authored-By line (CLAUDE.md §8).
