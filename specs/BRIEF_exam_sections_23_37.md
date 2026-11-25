# BRIEF — refresh the "exam" sections of the guide books with the real tests (units 23–37 · grammar topics 33–64)

Written 2026-11-17. The unit chapters 23–37 and grammar topics 33–64 were written around 10/27, before any 23–37 test, so their exam
sections still say "บทนี้ยังไม่มีข้อสอบจริง" / "ข้อนี้ยังไม่มีข้อสอบจริง". Since then the user sat 매일시험 23–36, got sheets 23–37, did the
workbook, and sat 복습시험③ (22–29과, 11/6). Rewrite ONLY those sections from the real records. Everything else in each file stays
byte-identical.

## Which section
- Unit chapter `content/guide/01_units/unitNN.md`: from the line `### 🧪 ออกสอบอย่างไร` up to (not including) the next `### ` heading
  (normally `### 🔗 เชื่อมโยง`).
- Grammar topic `content/guide/02_grammar/NN_slug.md`: from `### 🧪 ออกสอบแล้ว · ข้อผิดที่เคยเจอ` up to (not including) the next `### ` heading.

## Sources (read only what concerns your units)
| what | file | notes |
|:---|:---|:---|
| 매일시험 NN + 연습지 NN | content/exercises/everyday/unitNN.md | test section first (italic summary has date + score), then the sheet; `# 정답` keys: ⚠️ = marked wrong by the teacher (test) or self-checked (sheet). Unit 37 has the sheet only (its test, if any, is 11/19). |
| how the prediction scored | content/predictions/everyday/unitNN.md | the `✅ ผลจริงหลังสอบ` table at the top (units 22–36) |
| per-item score log | levels/1/docs/STATUS.md | search `NN과` |
| the user's slips, every sighting | docs/MISTAKES.md | search the unit number and the grammar |
| workbook | content/exercises/workbook/unitNN.md | publisher's printed keys; lines with ⚠️/✗ = the user's own slips |
| 복습시험③ (22–29과, 11/6) | content/exercises/miniexam/exam03.md | ⚠️ = deducted; §2 = how the mock matched. Units 23–29 only. |
| 기말 review handout (23–37과) | content/exercises/review/final02_part1.md, final02_part2.md | which handout items use this unit/grammar (cite as "ชุดทบทวนปลายภาค ข้อ 1-2") |
| what 기말 11/20 is likely to ask | content/predictions/final/final02.md §2.1 (unit → handout items + ★ slips) | |
| 낭독시험 | ⑤ 10/28 = 23과 · ⑦ 11/12 = 31과 · ⑧ 11/18 (unit not announced) | |

복습시험④ (30–37과) is on 11/18 and has **no result yet**: say "สอบ 18 พ.ย. — ผลยังไม่ออก" and point to KMU_Predict_miniexam04.pdf. Never invent
a score, a date or an item; if a source does not say it, leave it out.

## Unit section — template: the same section of content/guide/01_units/unit22.md (read it first)
1. A lead sentence saying what real material exists (test date + score, sheet, workbook, 복습시험③ part).
2. `#### 매일시험 NN과 (D พ.ย./ต.ค.) — ได้ X/10` + one lead sentence + a table `| ส่วน | รูปแบบ | ข้อที่ออก |` + "คะแนนที่เสีย" bullets:
   one per lost item, `เขียน ✗ form → **right form**` + the reason in a few words.
3. `#### 연습지 NN` — what it drilled (one line) + the ⚠️ slips.
4. `#### เวิร์กบุ๊ก NN과` — sections in one short list + the user's slips if recorded.
5. (23–29 only) `#### 복습시험③ (6 พ.ย.)` — the items from this unit and any deduction.
6. `#### ปลายภาค 20 พ.ย.` — 2–4 bullets: handout items for this unit and what final02 ranks highest for it.
7. Keep the old "ที่น่าจะพลาด" WARNING box if it has one, but update it: mark the slips that really happened with "(เกิดจริง: 매일시험 31)"
   and drop guesses that the real tests disproved.
Size: ≤ 6 KB per unit section (unit22's is 5.7 KB).

## Grammar-topic section — template: the same section of content/guide/02_grammar/29_ege-hante.md
A lead sentence, then bullets grouped by source (매일시험 NN · 연습지 NN · 워크북 NN · 복습시험③ · ชุดทบทวนปลายภาค), only items that use
THIS grammar, each `item ✓` or `เขียน ✗ → **✓**`. ≤ 3 KB. A topic whose grammar never appeared in a real paper says so in one sentence
and lists only where it is scheduled (handout items, 복습시험④).

## Writing rules (the renderer and the book style break otherwise)
- Thai prose, Korean examples; one Korean example per line with its gloss; no lines with more than 3 "·" outside a table (use a list).
- No bold-only line as a pseudo-heading (`**…**` alone on a line) — use `####`.
- Never write `~~`; write `✗`. Inside `*( … )*` never put a digit right before `)` (reword: `*(ข้อ 3 ผิด)*` ✗ → `*(ผิดในข้อ 3 ครับ)*` is still bad
  if it ends in a digit — end with a word).
- Leave a blank line before any heading that follows a table. No 4-space indent before ①②③④. Don't write `{c:` braces or `<보기>` (write [보기]).
- Consecutive `> ` lines merge: put a bare `>` line between dialogue lines in a quote box.
- Do not touch any other section or file. Do not run build.py, build_mockweb.py, or publish.

## Check before you finish
```bash
cd /home/beamkeerati/Documents/KMU_Korean && python3 scripts/book_style_check.py <every file you edited>
git diff --stat -- content/guide/   # only your files, only the exam sections
```
0 hard problems and no new soft ones in the lines you wrote. Report per file: the old section's first line → the new lead sentence,
and anything you could not verify.
