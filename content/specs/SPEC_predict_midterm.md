# SPEC_predict_midterm — 중간시험 เก็งข้อสอบ (1–21과) · brief for the mock-paper agents

## 0. Facts
- 중간시험: **10/22 (Thu) 말하기** interview · **10/23 (Fri) 쓰기·듣기·읽기**. Scope 1–21과 (book 1-1: 자모 + 5–21과).
  Each skill's exam = 50 of that skill's 100 marks (the other 50 = 복습시험 20 + coursework 30).
- The teacher's own blueprint = 중간시험 복습문제 (`content/exercises/review/midterm01_part1.md`, `_part2.md`):
  쓰기 14 sections · 읽기 25 items (passages = textbook 읽기 of 5, 6, 7, 9, 10, 11, 13, 14, 15, 18, 19, 21과 nearly verbatim)
  · 듣기 12 (formats listed in part2) · 말하기 20 interview questions.
- 복습시험 ① (`content/exercises/miniexam/exam01.md`) shows how this teacher scores a paper: 쓰기 100 in 5 blocks,
  듣기 10, 읽기 10 (textbook readings turned into a 가/나 dialogue with 나 blank). Its 읽기 used 6-2, 9-2, 13-2.
- `content/predictions/miniexam/exam02.md` is the house-style exemplar of a prediction file (headings, glosses, key).
- Units the teacher has NOT drawn on in any paper yet: **8과, 12과, 16과, 17과, 20과** — only 17과 has a printed 읽기; 8, 12, 16, 20과
  have a 대화 and a 듣기 text instead (checked by the reading agent 2026-10-18) (OCR text in
  `extracted/textbook/unitNN.txt`; cleaner per-unit summaries in `content/guide/01_units/unitNN.md`). First candidates for
  fresh 읽기/듣기 material; the used ones can recur.
- Grammar checklist 1–21: `content/guide/06_quickref.md` (35 topics; only topics taught up to 21과 may appear — no -(으)ㄹ까요 /
  무슨 N / -고 sequencing from 22과, nothing from 23과+).

## 1. Output files (each agent writes exactly its two files, nothing else)
```
content/predictions/midterm/parts/
  02_writing.md     + 02_writing_key.md      (agent A — 쓰기)
  03_reading.md     + 03_reading_key.md      (agent B — 읽기)
  04_listening.md   + 04_listening_key.md    (agent C — 듣기)
  05_speaking.md    + 05_speaking_key.md     (agent D — 말하기)
```
Fable assembles them into `content/predictions/midterm/midterm01.md` (analysis + parts, then `# 정답` + keys) and builds
`output/predictions/midterm/KMU_Predict_midterm01.pdf`.

## 2. Markdown rules (make_pdf.py renders them)
- The part file starts with `### N. …` (N = 2 쓰기, 3 읽기, 4 듣기, 5 말하기); sub-sections are `#### A. …`, `#### [1~3] …`.
  Never `#` or `##` inside a part file. The key file starts with `## 쓰기` / `## 읽기` / `## 듣기` / `## 말하기`.
- **Every Korean item carries a Thai translation** in italics `*(…)*` right after it (passages: line by line, or one italic
  paragraph under the passage). Thai only — no English glosses.
- Word blanks: `(　　)` (two ideographic spaces). Sentence answers: the `####` heading must contain one of
  **문장을 만드세요 / 문장을 쓰세요 / 대화를 완성하세요 / 대답하세요 / 바꾸세요** (e.g. `#### D. [보기]와 같이 문장을 쓰세요.`) —
  the renderer then prints two ruled lines under every item line that starts with `N.`; a bare 쓰세요 in a `####` heading does
  NOT trigger lines (only `###` headings do), and **고르세요** / **단어** in the heading always switches them off.
- Pictures do not exist: describe them in Thai after `🖼️` (e.g. `🖼️ แมวอยู่ใต้โต๊ะ`) and let the student write the Korean.
- Never use `~~strikethrough~~` (prints literally) — use `✗`. No `{x:…}` braces (reserved for colour tags). No HTML.
- Items are numbered `1.` `2.` … inside each sub-section; options `① ② ③ ④` on one line separated by ` · `; O/X items end
  with `(　　)`; [보기] boxes as a blockquote `> [보기] …`.
- Dialogue lines: `가: …` / `나: …` each on its own line with a bare `>` line between them when inside a blockquote.
- Key file: one line per sub-section — `**A.** 1) … 2) … 3) …` (label up to 16 chars ending in a dot; items `1)`), with a
  short Thai reason in parentheses where the item is a trap. For 듣기 the key file also holds `## 듣기 스크립트` (see agent C).
- Korean must stay at textbook level 1–21과; names from the textbook (마키 · 투이 · 지훈 · 장핑 · 카오루 · 알렉세이 · 제프리 ·
  압둘라 · 윤아 · 바트 · 뚜언 · 이리나).

## 3. House style of a mock paper
- Mirror the teacher's instruction wording: 맞는 것을 고르세요 · [보기]에서 알맞은 단어를 골라 쓰세요 · 빈 칸에 알맞은 단어를
  쓰세요 · [보기]와 같이 쓰세요 · 다음 대화를 완성하세요 · 맞으면 O, 틀리면 X를 하세요 · 무엇이 맞아요? · (　　)에 무엇이 맞아요? ·
  순서를 쓰세요 · '㉠…'는 누구예요/어디예요? · 다음을 읽으세요. 그리고 대화로 만드세요.
- Points like the teacher: `(각 4점×6=24점)`; a 쓰기 paper totals 100.
- Each mock pre-empts the student's recurring mistakes (§4) with at least one item per bullet where the format allows.
- Each sub-section's Thai instruction line in italics right under the heading: `*คำสั่ง: …*`.

## 4. The student's recurring mistakes to target (from CLAUDE.md §6b)
ㅈ/ㅊ letter shape (책 · 청소 · 몇 · 차) · 생활→생할 · ㅐ/ㅔ (개/게) · 시월 · 유월 · destination takes 에 (not 하고) · 안 + N하다 word
order (아르바이트 안 해요) · 열심히 · 시/분 spacing (두 시 이십 분) · -(으)러 keeps its object (과일을 사러) · 으 after 받침
(받으십니다 · 씻으러 · 읽으세요) · 마십니다 · noun past 학생이었어요 · 어땠어요 · 에 vs 에서 · register swap keeps the tense
(안 했어요 → 안 했습니다) · time words with/without 에 (오늘 ✗에 · 토요일에) · 살아요/살았어요 · answering the wrong question
word (언제/며칠/몇 시/뭐) · 거예요 spelling + spacing (갈 거예요) · 부터/까지 attached (10시부터) · 한테/한테서/께 direction ·
position-word reference point (A가 B 앞에: B is the landmark; swapping flips 앞↔뒤) · 좋아하다 is not split by 안 · counter
answers need noun + number + counter (책 네 권 · 열네 명) · `(　　)에 무엇이 맞아요?` = fill the passage blank from the options ·
다니다 ≠ 가다 · 수업 ≠ 시험 · 여러 ≠ 우리 · 했어요 vs 하고 있어요 (answer in the tense of the question).
