# Extraction spec (shared by all agents)

Goal: turn scanned Korean exercise pages into a CLEAN, printable Thai-annotated practice set.
The pages contain the student's handwriting (pencil answers) and teacher's red marks.
**Ignore the handwriting when writing questions** — reproduce the blank exercise only.
Use handwriting/red marks only as hints for the answer key (the student is often WRONG — always give the truly correct answer).

## Output files
Write TWO files (paths given in your task):
1. `<name>_q.md` — questions only
2. `<name>_a.md` — answer key only

## Questions file format (follow exactly)

```
## 9과 · 매일 시험 (แบบทดสอบประจำวัน บทที่ 9)

### A. 그림을 보고 단어를 쓰세요.
*คำสั่ง: ดูภาพแล้วเขียนคำศัพท์*

> **보기 (ตัวอย่าง):** 🖼️ รูปร้านอาหาร → 식당 (ร้านอาหาร)

1. 🖼️ รูปธนาคาร (มีป้าย BANK) → (　　　　)
2. 🖼️ รูปสนามบิน มีเครื่องบินบินอยู่ → (　　　　)

### B. 그림을 보고 <보기>와 같이 대화를 완성하세요.
*คำสั่ง: ดูภาพแล้วแต่งบทสนทนาให้สมบูรณ์ตามตัวอย่าง*

> **보기:** 🖼️ กล่องดินสอวางอยู่บนโต๊ะ
> 가: 필통이 어디에 있어요? *(กล่องดินสออยู่ที่ไหน?)*
> 나: 책상 위에 있어요. *(อยู่บนโต๊ะ)*

5. 🖼️ กระเป๋าวางอยู่ใต้เก้าอี้
   가: 가방이 어디에 있어요? *(กระเป๋าอยู่ที่ไหน?)*
   나: (　　　　　　　　　　). *(อยู่ใต้เก้าอี้)*
```

Rules:
- Heading `##` = one unit/page-group: `<N>과 · <source label> (<Thai>)`. Keep units in ascending order (5→13) within your file.
- Heading `###` = one exercise block, letter A, B, C… restart per `##`. Korean instruction exactly as printed, then a line `*คำสั่ง: ...*` with Thai translation.
- EVERY question line must have a Thai translation in `*(...)*` — for Korean sentences, translate the sentence (with the blank's intended meaning, so the student knows what to write). For single-word items a Thai gloss is enough.
- Pictures → replace with `🖼️ ` + a short, precise Thai description of what the picture shows (include names/labels printed under the picture, flags → nationality, prices, quantities, positions, etc.). The description must contain enough info to answer.
- Blanks: use `(　　　　)` (full-width parentheses + ideographic spaces U+3000). NEVER use underscores `___` (breaks markdown).
- Multiple choice in brackets: keep as printed, e.g. `저(은, 는) 중국 사람입니다.`
- Keep the original question numbering.
- Listening/dictation items (듣고 쓰세요 / 받아쓰기, needs audio): convert to a writing exercise — give the Thai meaning and ask to write the Korean, e.g. `8. เขียนเป็นภาษาเกาหลี: "ข้างหลังตึกนักศึกษา" → (　　　　)`. Mark block instruction as `*(ดัดแปลงจากข้อฟัง)*`. If the transcript can't be determined, skip the item.
- Reading passages: reproduce the Korean text fully, then a Thai translation paragraph in italics, then the questions.
- Markdown hygiene (renderer is Python-Markdown): blank line before every list and every `>` block; one blank line between questions blocks; continuation lines of a numbered item indented 3 spaces; do not use HTML; do not use tables wider than 4 columns.
- Skip: cover pages, table of contents, purely blank pages, pages that are only answer keys.

## Answers file format

```
## 9과 · 매일 시험

**A.** 1) 은행 2) 공항 3) 약국 4) 우체국
**B.** 5) 의자 아래에 있어요. 6) 필통 안에 있어요. 7) 나무가 있어요. ⚠️
**C.** 8) 학생회관 뒤 9) 많이 있어요 10) 음식이 맛있어요
```

- One line per block. For open-ended items give a model answer.
- Put ⚠️ after an item when the teacher marked the student's answer wrong (red slash/X) — these are weak spots the student should review. Optionally add a very short Thai note why, e.g. `⚠️ (ถาม 무엇이 → ตอบสิ่งของ ไม่ใช่ตำแหน่ง)`.
- Blank line between lines (so each renders as its own paragraph).

When done, reply with: files written, units covered, number of exercise blocks, and anything skipped/uncertain.
