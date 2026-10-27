# BRIEF_workbook_23_37 — transcribe the workbook (워크북) 23–37과 + the 22~37과 종합문제, and verify the 5–22 keys (2026-10-27)

Read this whole file, then only the sources named in your assignment. Write only the files your assignment names. Do not run build.py.

## Sources (all already rendered)
- `extracted/workbook/unitNN/wb-N.png` — the workbook pages of unit NN at 150 dpi (4–5 pages per unit). They carry the
  student's PENCIL answers and Thai margin notes; there are **no teacher marks**. The printed page number sits bottom right.
- `extracted/workbook/key/key-01.png … key-12.png` — the publisher's printed answer key 「워크북 정답」, book pages 184–195:
  key-01 = 5과 →, roughly two units per page, 23과 begins around key-06/07, 37과 ends on key-12, and the bottom of key-12 is the
  「22~41과 종합문제」 key (items 1–45; the heading says 41과 but the paper covers 22–37과). Find your units by their `NN과` rule lines.
- `extracted/workbook/review22-37/p-01.png … p-10.png` — the 22–37과 종합문제 (book pages 174–183, 45 items, blank, no pencil).
- `extracted/textbook/unitNN/page-N.png` — the textbook pages (300 dpi) if you need to check a word or a reading text.
- Existing files to copy the format from: `content/exercises/workbook/unit22.md` (a unit) and `unit21_review_5-21.md` (a 종합문제 file).
- Vocabulary with Thai glosses: `content/guide/04_vocabulary/unitNN.md`.

## Output format for a unit file `content/exercises/workbook/unitNN.md`
Copy unit22.md exactly:
```
## NN과 · 워크북 (ชื่อบทภาษาเกาหลี - คำแปลไทย)

### A. 어휘 1: <Korean instruction as printed>
*คำสั่ง: <Thai translation of the instruction>*

> **<보기>:** … (when the exercise has a 보기 box; Thai gloss in *(…)* after each word)

1. <item exactly as printed> *(Thai gloss)*
…
---
(next exercise: ### B. …, ### C. … — letter per exercise in page order; use the printed section names: 어휘, 문법 name
(e.g. -고 싶다), 듣기, 읽기, 쓰기, 말하기)

# [PART 2]

## NN과 · 워크북 (เฉลย)
**A.** 1) … 2) … 3) …
**B.** 1) …
```
Rules:
- **Every item of every page**, in order. Blanks are written `(　　　　)` (ideographic spaces). A whole-sentence answer is written
  `→ (　　　　　　　　)` or `나: (　　　　　　　　)` — the renderer turns these into ruled lines. Pictures become
  `🖼️ <Thai description of what the picture shows>` (never leave a picture out: the student must know what to answer).
  Conjugation tables stay tables (`| 동사 | -아/어요 | … |`). Reading passages are copied in full, one sentence per line with its
  Thai gloss `*(…)*`. Matching exercises list the left items numbered and the right items as `ⓐ ⓑ ⓒ`.
- Thai gloss `*(…)*` after every Korean prompt/sentence/option. Plain Markdown only: no `**` inside items (only the key labels
  `**A.**`), no `~~`, no HTML, no `{x:…}` colour braces (colours are automatic).
- **Keys come from the printed key pages, never from your own solving.** Where the key prints 〈예시 답안〉 write
  `*(ตัวอย่างตอบ)*` after it. Where the key has no entry (free writing, 말하기) write `ตอบตามจริง — ตัวอย่าง: …` and label it so.
  One line per exercise letter, items in number order: `**C.** 1) 매워요 2) 더워요 …`. A short Thai reason in `*(…)*` only where
  the answer is not obvious (particle choice, irregular form, trap).
- **The student's pencil:** compare each pencil answer with the printed key. Where it differs, append
  `⚠️ *(ผู้เรียนเขียน X — reason in Thai)*` to that key item. Where the pencil is unreadable write `(อ่านดินสอไม่ออก)`.
  Zoom in (crop the PNG with PIL at 2–3×) before deciding that a letter is wrong; ㅈ/ㅊ, ㅐ/ㅔ and ㅓ/ㅕ shapes are this
  student's known weak points. If a page has no pencil at all, say so in the unit's italic line under the `##` title.
- Under the `##` title put one italic line: pages covered (book page numbers), pencil present or not, number of exercises.
- Unreadable print: write `(อ่านไม่ออกจากสแกน)` — never guess.

## The 종합문제 file `content/exercises/workbook/unit37_review_22-37.md`
Copy unit21_review_5-21.md: `## 22~37과 · 종합문제 (ข้อสอบรวมบท 22–37 · 45 ข้อ)`, the item-range headings
`### [1–3] 밑줄 친 것과 의미가 같은 것을 고르세요.` + `*คำสั่ง: …*`, every item with its 4 options on one line
(`① … ② … ③ … ④ …`, Thai gloss for the stem and, when the options are not single words, for the options), passages copied in
full with Thai per sentence, pictures/tables as 🖼️ or Markdown tables. Then `# [PART 2]`, `## 22~37과 · 종합문제 (เฉลย)` and the
45 answers from key-12 (`1) ④ 주문했어요 = 시켰어요 *(สั่งอาหาร)*` — number, circled option, the option's text, a one-line Thai reason).
The key block on key-12 reads: 1.④ 2.③ 3.① 4.② 5.③ 6.② 7.① 8.① 9.② 10.④ 11.② 12.③ 13.④ 14.④ 15.② 16.① 17.② 18.① 19.③ 20.④
21.② 22.④ 23.③ 24.② 25.② 26.③ 27.② 28.③ 29.④ 30.④ 31.② 32.③ 33.③ 34.① 35.④ 36.① 37.① 38.③ 39.④ 40.① 41.③ 42.② 43.④ 44.③ 45.④
— re-read the page yourself and use what you see if it differs.

## The key-verification assignment (units 5–22 + 5~21과 종합문제)
The keys in `content/exercises/workbook/unit05.md … unit22.md` were written before the printed key existed: 5–13 from the
teacher-marked scans, 14 likewise, 15–22 and `unit21_review_5-21.md` solved by an AI. Compare every key item with key-01 … key-06
(5과 … 22과 and the 「5~21과 종합문제」 block). Fix the Markdown key where it differs from the print (keep existing `⚠️` teacher-mark
notes; when the printed key contradicts a ⚠️ note, keep the note and add `(เฉลยพิมพ์: …)`). Do not touch the question parts.
Report every change as `unitNN X.n: old → new`. If a printed key item is itself inconsistent with the question (it happens in this
book), keep the printed answer and add `*(เฉลยพิมพ์ — โจทย์ถามคนละอย่าง)*`.

## Report (short)
Files written + line counts · list of pencil ≠ key items (unit, exercise, pencil, key) · unreadable spots · anything odd in the
print (typos, key/question mismatch). No content summary.
