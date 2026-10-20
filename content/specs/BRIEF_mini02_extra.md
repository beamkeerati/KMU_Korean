# Brief — two more full 복습시험② mock papers for the practice site (2026-10-19)

The real 복습시험② (mini exam 2, units 14–20) is TOMORROW, Tue 2026-10-20. The student already did paper 1
(content/mockweb/mini02.json). Write ONE more complete paper = 4 sets (writing · listening · reading · speaking)
as a new data file. Your paper number and file are given in your task message.

## Read first (in this order)
1. content/specs/SPEC_mockweb.md — the data schema. Your file MUST pass `python3 scripts/mockweb_validate.py <your file>`.
2. content/mockweb/mini02.json — paper 1: copy its exact structure, section headings, point values, minutes, the
   Thai `th` on every item, `why` notes. Do NOT reuse its items, passages or scripts (new questions only).
3. content/predictions/miniexam/exam02.md §1–§2 — what 복습시험 ① looked like and which 14–20과 grammar is most likely.
   content/exercises/miniexam/exam01.md — the real paper ① (format evidence).
4. Unit material for 14–20과: content/guide/01_units/unit14.md … unit20.md (vocab, grammar, 대화, 읽기 texts),
   content/guide/04_vocabulary/unit14.md … unit20.md, content/exercises/workbook/unit14.md … unit20.md,
   content/exercises/everyday/unit14.md … unit20.md (the teacher's daily tests — strongest signal of what she asks).
5. CLAUDE.md §6b — the student's recurring mistakes. Build items that test exactly those weak points
   (ㅈ/ㅊ words, ㅐ/ㅔ, 으 after 받침 before 시/러, -(으)ㄹ 거예요 spelling, 한테 vs 한테서 vs 에/에서, 께 + 드리다,
   부터~까지 attached, 에 after time words, 시월/유월, native counters 네 개/열네 명, 언제/며칠/몇 시 question words,
   noun past 이었어요, 어땠어요, ㄹ-drop 만드세요/삽니다, ㅡ-drop 바빠요/바쁩니다).

## Paper format (same as paper 1 = the real paper ①)
- 쓰기 100점, 30분: A [보기] particles 6×4 · B [보기] question words 6×4 · C [보기]처럼 쓰세요 (conjugation/transform) 4×4
  · D 문장을 만드세요 2×6 · E 그림을 보고 대답하세요 (picture = Thai `pic` description starting 🖼️) 4×6 · plus a reserve section with pts 0.
- 듣기 10점, 15분: MC 4×1 · O/X 4×0.5 · short written answers (blank/write) worth 4 in total. Each section has a `script`
  (speakers F/M, every number written in Hangul, natural level-1 Korean, 2–6 lines) and a `th` per line.
- 읽기 10점, 20분: three textbook-style passages (lift 읽기/대화 texts of 14–20과 nearly verbatim — the real paper ① did
  exactly this), each followed by 가/나 dialogue items where 나 must be written (type write, 1 point each, 10 total) + reserve.
- 말하기 10점, 10분: 10 interview questions (type speak) with model answers, `mth`, and `checks` regexes, as in paper 1.
- Set ids: mini02<letter>-writing / -listening / -reading / -speaking (letter given in your task). exam = "mini02".
  Titles: "쓰기 · 복습시험② ชุดที่ N" etc.

## Choosing content ("highest probability")
Rank grammar/topics by how often the teacher has tested them (daily tests 14–19, workbook, paper ①) and put the
most frequent ones in the scored items. Cover every unit 14–20 at least once across the paper. Prefer the textbook's own
sentences and vocabulary. Every item needs a Thai translation (`th`). Accepted-answer lists (`ans` for blanks, `model`
for write) should include the common valid variants (해요/합니다 both where natural, 뭐/무엇을, 한테/에게).

## Done =
- the file validates OK; run `python3 scripts/build_mockweb.py --no-audio` once to confirm it builds (do NOT run without
  --no-audio; the main session generates the voice clips).
- Final reply (≤150 words): the file path, the 4 set ids with item counts, which unit/grammar each 쓰기 section and each
  읽기 passage tests, and anything you were unsure of.
