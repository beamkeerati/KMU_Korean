# BRIEF_daily_sets — every 매일시험 (daily test) as a practice-site set (2026-10-27)

Goal: the student wants to redo every daily test on the practice website. Convert `content/exercises/everyday/unitNN.md`
(the transcribed tests + practice sheets, questions first, then `# 정답`) into `content/mockweb/daily_a.json` (units 05–13) and
`daily_b.json` (units 14–23). Follow `content/specs/SPEC_mockweb.md` (set/section/item schema) and look at
`content/mockweb/mini02_real.json` for a finished example. Validate with `python3 scripts/mockweb_validate.py <file>`.
**Write your draft as `content/mockweb/_daily_a.json` (leading underscore = ignored by the build), validate, then rename it to
`daily_a.json`** — other agents are building the site while you work.

## Sets per unit
For unit NN (two-digit):
1. `daily-NN-writing` — every non-dictation part of the real test (A/B/… as sections; `h` = the Korean instruction as printed,
   `th` = its Thai line, `box` = the 보기 text if any). Item types: `blank` for fill-ins / conjugation rows / short answers,
   `write` for whole-sentence answers (model = the key's sentence(s), first = best), `mc` for choice items. Picture descriptions
   (the `🖼️ …` text) go into `pic`. `pts` = 1 (the tests are 10 × 1 point; keep 0.5 where the file says so).
2. `daily-NN-listening` — the dictation part (선생님 이야기를 듣고 쓰세요): **one section per dictated sentence**, each with
   `script: [{"s": "T", "ko": "<the sentence>", "th": "<Thai>"}]` and one item `{"type": "blank", "q": "___", "ans": [["<the sentence>"]]}`
   (`th` = Thai of the sentence; `why` = the student's mistake if the key has ⚠️). Sentences must contain no digits (write numbers
   in Hangul as read). Skip this set when the unit has no dictation.
3. `sheet-NN-writing` — the practice sheet (연습지) sections, when the unit file has one with gradeable items (conjugation tables → one
   `blank` item per row with several `___`; fill-in dialogues → `blank`; speaking prompts without a fixed answer → `write` with the
   key's example as `model` and `hint: "ตอบตามจริงได้"`). Skip pure speaking games.
All sets: `"exam": "daily"`, `"skill"` as above, `"minutes"`: 10 (sheet 15), `"title"`: `"매일시험 NN과 · 쓰기"` / `"… · 받아쓰기"` /
`"연습지 NN과"`, `"intro"`: one Thai line (date sat, score, what was lost — from the unit file's italic line).
Add one extra field on every set: `"group": "매일시험 NN과 · <date d MMM> · <score>/10"` (same string on the writing and listening sets of one test;
sheets: `"group": "연습지 NN과 · <date>"`). The site groups cards by that string.

## Content rules
- Korean exactly as in the source, colour tags stripped (`{n:학생}{p:이}` → `학생이`), no `*`/`**`/`~~`/HTML.
- Thai translation for every prompt (`th`), option, script line.
- `why`: where the key carries `⚠️` (the teacher deducted / the student erred), write what the student wrote and why it was wrong — these
  notes are the point of redoing the test. Also copy the key's short Thai reasons.
- Keep every item; keep the paper's numbering in `n` ("1", "2", … or "A1" when the file numbers per section).
- `unit00_classroom.md` is not a test — skip it. Units 21 has no test file; 22 and 23 do.

## Report
Files written, sets and item counts per unit, anything you could not convert (and why). No summaries of the content.
