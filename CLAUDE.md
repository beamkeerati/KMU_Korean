# CLAUDE.md — KMU Korean 1 exam-prep workspace

Claude Code loads this file automatically when started in this folder.

## 1. User & goal
- Thai-speaking student at Kookmin University (KMU) Korean Language Center, level 1 (국민한국어 1).
- Course covers **자모 + Units 5–37** (midterm = 1–21과 per the teacher's board = book 1-1; 22과 opens book 1-2; final = 23–37). Study material covers **5–37** since 2026-10-26 (guides, vocab, mind maps; exercises/predictions still stop at 22). Exam schedule (from the 「2026 가을학기 1급 시험안내」 handout,
  including the teacher's red-pen correction): 복습시험1 2026-10-06, 복습시험2 2026-10-19,
  중간시험 2026-10-22 (말하기) / 10-23 (쓰기·듣기·읽기), 복습시험3 2026-11-06, 복습시험4 2026-11-18,
  기말시험 **2026-11-20** (쓰기·듣기·읽기) / **2026-11-23** (말하기).
  ⚠️ The handout prints the 기말 dates as 10/20 and 10/23; the teacher struck out the `10` and wrote
  `11` in red. 11/20/2026 is a Friday and 11/23/2026 a Monday, matching the printed weekdays —
  12/20/2026 is a Sunday, so the earlier note of "기말시험 2026-12-20/23" was wrong.
- **Pass rules (GKS orientation guide p.9 「Course Completion and Failure」, p.7 「Attendance」, 2026-10-21):** average per SUBJECT (each of the
  four skills, mean of 중간 1-1 and 기말 1-2) must be **≥ 70** to advance; **< 60 in any subject = fail**; 60–69 may re-test (attendance ≥ 80 %,
  at most 2 subjects in that band, 30,000원 per subject); cheating = 0. Scholars must attend 100 %: > 3 consecutive / > 5 days a month unexcused
  → NIIED warning, 3 tardiness warnings → scholarship lost; TOPIK 3 within the year. Stored in content/mockweb/scores.json `rules` and shown as
  profile section 2 (pass table + notes; colours now = ≥ 70 green · 60–69 yellow · < 60 red; the summary targets 70, not the old made-up 90). Site v33.
- Grading: every skill is out of 100 = 시험 50 + 복습시험 20 + coursework 30.
  말하기 발표 20 / 태도 10 · 듣기 워크북 숙제 20 / 태도 10 · 쓰기 글쓰기 10 + 매일시험 10 / 공책 숙제 10 ·
  읽기 낭독시험 20 / 개인 과제 (대화 외우기) 10. Half the marks are coursework, not the big exams.
- 복습시험 (the user says **"mini exam"**) = four papers in one morning: 말하기 10 (interview, no paper) · 쓰기 100
  (counts as /10; 5 questions: 보기 particles 6×4 · 보기 question words 6×4 · 보기처럼 쓰세요 4×4 · 문장을 만드세요 2×6 ·
  그림을 보고 대답하세요 4×6) · 듣기 10 (MC 1×4 · O/X 0.5×4 · short answers 4) · 읽기 10 (three textbook-style passages,
  each turned into a 가/나 dialogue with 나 blank, 1×10 — ①'s three passages were 읽기 6-2, 9-2 and 13-2 nearly
  verbatim, so ② will almost certainly lift 읽기 texts of 14–19). Transcribed in content/exercises/miniexam/exam01.md, analysed
  in content/predictions/miniexam/exam02.md §1. ① 10/6 = 5–13과 · ② **10/20 = 14–20과** (the syllabus said 10/19; the teacher's whiteboard on 10/15 moved it to Tue 10/20, same day as the 방학 계획 발표; Mon 10/19 = 21·22과) · ③ 11/6 = 22–29과 · ④ 11/18 = 30–37과.
  ② (sat 10/20, scan in source/miniexam/, transcription exercises/miniexam/exam02.md, scorecard at the top of predictions/miniexam/exam02.md) had a
  **7-section 쓰기** (반대말 · 해요→합니다 · 높임 · 조사 · answer-with-given-grammar -네요/-(으)시/-(으)러 · Q&A ×6 · picture timeline in 합니다체), 듣기 10×1 from the
  textbook 17–20과 listening texts, and 읽기 = the three passages of the teacher's 복습문제 verbatim. **Score slip 10/21: 말하기 10.0 · 쓰기 7.5 · 듣기 8.5 · 읽기 9.0** (the marked papers were not returned, so
  the per-item deductions are unknown. The scan in source/ is the QUESTION paper with the user's working; the answers were written on
  a separate answer sheet the user could not photograph — so section 5 was NOT left blank, the §6b note on it is withdrawn).
  복습시험 totals for the midterm term (①+②, /20 each skill): 말하기 20 · 쓰기 16.3 · 듣기 16.0 · 읽기 19.0 = 71.3/80.
  The handout's footnote 「중간(1-1) 100점, 기말(1-2) 100점」 means the 50/20/30 table applies once per term: ①+② feed the midterm
  term's 복습시험 20, ③+④ the final term's.
- **중간시험 facts from the teacher (10/20):** "not far from 복습시험①, ② and the 복습문제 — maybe only the words change"; Fri 10/23 쓰기 1 h · 듣기 40 min ·
  읽기 1 h; 말하기 Wed 10/22 slot 3, 09:45–10:00, 20–25 questions like the review set's 말하기 table. Mock v2 built from those formats
  (content/specs/BRIEF_midterm_v2.md, 4 Sonnet agents 10/20).
- **중간시험 result (score slip 2026-10-27, source/midterm/KMU midterm score unit 05 - 21.pdf, student no. 6):** 말하기 **41.2** · 듣기 **42.0** ·
  쓰기 **45.5** · 읽기 **49.0** (each /50) · 전체평균 44.4 (= 88.8 %). The teacher did not allow photographing the papers; the user remembers
  the exam "looked a lot like the book" (대화/읽기 texts and 연습 patterns) — the same lesson as 복습시험 ①②, so the 기말 prediction should
  again lift textbook texts of 23–37 nearly verbatim. Term totals so far (exam + 복습시험 ①②, coursework 30 still unknown): 말하기 61.2 ·
  듣기 58.0 · 쓰기 61.8 · 읽기 68.0 of 70 — even 50 % coursework keeps every skill above the 70 pass line. Weakest = 말하기 and 듣기.
- 낭독시험 (read-aloud, 20 marks of 읽기): ① 9/30 9과 · ② 10/6 · ③ 10/12 15과 · ④ **10/15** (announced 10/14, the 19과
  day — the plan names no unit; ① and ③ were the unit taught on the announcement day, so 19과 is the working assumption)
  · ⑤ 10/28 23과 · ⑥ 11/6 · ⑦ 11/12 31과 · ⑧ 11/18. The 19과 texts with pronunciation are in exam02.md §7.
- **Talk to the user in Thai, keep replies short.** Study material = Korean with Thai explanations.
- Stated preferences:
  - Deliverables as **PDF**. Fonts (user's choice 2026-10-27, replacing the earlier Noto-only rule): **Thai + Latin = TH Sarabun**
    (the installed `Laksaman` TTFs = TLWG's free clone of TH SarabunPSK), **Korean = Noto Serif CJK KR** (serif Hangul); symbols/emoji
    fall back to Noto. Mind maps (build_mindmaps.py) still use Noto Sans. The user compared five samples and picked "D + E".
  - **Book style (2026-10-27):** the two guides must read like a book, not dense notes — every chapter opens with an INTRO box, every
    section starts with a lead sentence, one Korean example per line with its gloss, no `·`-chains of examples, no bold lines as
    headings. Contract = `content/specs/SPEC_book_style.md`; exemplars = 01_units/unit23.md and 02_grammar/37_b-irregular.md;
    checker = `scripts/book_style_check.py`. The renderer does the rest (running heads, numbered sections, TOC with page numbers,
    Korean words never split mid-word).
  - Every exercise needs a **Thai translation**; pictures become **Thai text descriptions** (`🖼️ ...`).
  - Docs need a **table of contents**; each `##` starts on a new page (and now each `#` part too).
  - Answer keys ordered by question number, one item per line; sentence questions need **long blank lines** to write on.
  - Wants detail and full coverage of the exam content.
  - Likes the deep-dive explanatory style of the old `은는 vs 이가` doc (now **ส่วนที่ 2** of the guide).
  - **Colour by word function (since 2026-10-17):** every Korean sentence in every PDF is coloured by the function of
    each segment (n คำนาม blue · p 조사 orange on pale orange · v stem green · e ending/tense/이다 purple · q 의문사 teal ·
    x negation red · m numbers/counters brown · a adverbs/no-에 time words grey · dotted underline = honorific) and the
    Thai gloss after it uses the same colours, so 학생 and นักเรียน match. Implemented in `scripts/kotag.py`
    (Kiwi for Korean, PyThaiNLP + lexicons for Thai, applied at render time by make_pdf.py and build_mindmaps.py);
    scheme + review rules in `content/specs/SPEC_colors.md`; legend page = first `##` of ส่วนที่ 0 + a running strip in
    the top margin of every page. The user asked for this instead of bold-only emphasis.

## 2. Layout (reorganised 2026-10-07 — one folder per material type at every level)

```
source/        ต้นฉบับ — never modify the contents; file names follow §2.1
  textbook/    KMU student's book unit 05.pdf … unit 22.pdf
  workbook/    KMU workbook unit 05 - 13.pdf · KMU workbook unit 14 - 22.pdf · (2026-10-27) KMU workbook unit 23.pdf … unit 37.pdf (4–5 pp each,
               the user's pencil, no teacher marks) · KMU workbook key unit 05 - 37.pdf (the publisher's printed 워크북 정답 pp.184–195 — real keys
               for EVERY unit, incl. the 22~37과 종합문제; before it the 15–22 keys were AI-solved) · KMU workbook review unit 22 - 37.pdf
               (22~37과 종합문제, 45 items, pp.174–183)
  midterm/     KMU midterm score unit 05 - 21.pdf (the 중간시험 score slip, 2026-10-27 — the papers themselves may not be photographed)
  everyday/    KMU everyday test unit 05 - 13.pdf · KMU everyday sheet unit 05 - 13.pdf
               KMU everyday test unit 14.pdf · test unit 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28 · sheet unit 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29   ← daily hand-outs land HERE
               (the user dropped test 24 / sheet 25 in source/ itself on 10/28, test 25 / sheet 26 on 11/1, test 26 / sheet 27 on 11/2, test 27 / sheet 28 on 11/3, test 28 / sheet 29 on 11/4 — moved here; check source/ root after each drop)
               (the user dropped the 23과 sheet as "sheet unit 22" on 10/26 — its content is 23과 ㅂ불규칙/(으)ㄴ 형태 연습, renamed to unit 23)
  miniexam/    KMU mini exam 01 unit 05 - 13.pdf   (복습시험 ①: score sheet + 듣기/읽기/쓰기 papers in one PDF)
               KMU mini exam 02 unit 14 - 20.pdf   (복습시험 ②, sat 2026-10-20: 쓰기 4 pp + 듣기 + 읽기, the student's pencil, no marks yet)
               ← 복습시험 scans land HERE, never in everyday/ (the user wants the two kept apart at every level)
  review/      KMU midterm review 01 unit 05 - 22.pdf   (teacher's 「1급 중간시험 복습문제」, 16 pp: 쓰기 1–14 · 읽기 1–25 · 듣기 1–12 · 말하기 1–20;
               p.17 of the scan is the 19과 sheet again — ignored)
  vocabulary/  KMU vocabulary unit 05 - 22.pdf   (centre's own vocab book, 48 pp: 1–17 word lists per unit · 18–35 본문 듣기 sheets · 36–48 picture themes)
               KMU vocabulary unit 23 - 37.pdf   (2026-11-01, dropped as "vocabulary unit 23 - 37.pdf" in source/ root → renamed; 36 pp: 1–15 = book pp.20–34
               word lists 23–37 (the user's pencil glosses on 23–27) · 16–30 본문 듣기 23–37 (pencil on 23–26) · 31–34 irregular-verb pages ㅂ 23 · ㄹ 25 ·
               ㄷ 31 · 르 32 · 35 ◆동사 2 · 36 ◆형용사 2)
  lecture/     KMU lecture note unit 05 - 12.pdf   (18 pp of the user's PHOTOS of the teacher's slides + notebook; 366 MB; slides actually run 9–22과)
  syllabus/    KMU syllabus 2026 fall unit 05 - 37.pdf · KMU orientation guide 2026 fall GKS.pdf (2026-10-21, 33 pp English, was
               「KOOKMIN_KLC_Fall 2026 GKS Freshman Orientation Guide(노현서수정)」; pages → extracted/syllabus/orientation_2026fall/)
  audio/       (2026-10-21, git-ignored: 147 MB of publisher/teacher mp3s) textbook/KMU audio student's book unit 01 - 37/N-M.mp3
               (N = unit, M = track: 1 대화 · 2 읽어봅시다/듣기 text · 3 발음 drill; units 1–4 have more tracks = 자모) ·
               review/KMU audio midterm review 01 listening/*.mp3 (the teacher's audio for her 복습문제 듣기 1–12; file ids = the
               codes in the ฟัง headings of exercises/review/midterm01_part2.md, e.g. 1-1:01-06 ↔ 1-01…1-06.mp3)
  textbook/    + KMU student's book appendices unit 01 - 21.pdf (2026-10-21, 6 pp = 부록: 듣기 대본 of 8·12·16·20과 + 읽기/듣기 answer keys
               1–21 on pp.2–4, English 대화 translations 5–21 on pp.5–6) → extracted/textbook/appendices/page-N.png
               + (2026-10-25) KMU student's book unit 23.pdf … unit 37.pdf (book 1-2; unit 26 had only 3 pp until the user re-scanned it on
               2026-10-27 — now 8 pp = 262–269 complete, re-extracted the same day) · KMU student's book appendices unit 22 - 37.pdf (5 pp; its keys cover 22–37, the 1–21 file has no 22과 key)
               · KMU student's book table of contents.pdf (4 pp) → OCR'd 23–37 into extracted/textbook/unitNN/ + unitNN.txt;
               appendix → extracted/textbook/appendices_22-37/, contents → extracted/textbook/contents/ (200 dpi)
extracted/     intermediate extraction output (regenerable, ~300 MB) — same names as source/
  textbook/    unitNN/page-N.png (300 dpi) + unitNN.txt (tesseract)   ← written by scripts/ocr_extract.py
  workbook/    unit05-13/wb-01..41.png · unit14-22/wb-01..50.png       (graded scans, 150 dpi) · unit23…unit37/wb-N.png (150 dpi) ·
               key/key-01..12.png (printed key, 150 dpi) · review22-37/p-01..10.png (종합문제) · ../midterm/score-1.png
  everyday/    unit05-13/test-1..9.png + sheet-01..10.png · unit14/test-1.png · unit15/sheet-1..3.png + test-1.png · unit16/sheet-1..4.png + test-1.png · unit17/sheet-1..2.png + test-1.png · unit18/sheet-1..2.png + test-1.png · unit19/sheet-1..2.png + test-1.png · unit20/sheet-1.png · unit22/test-1.png · unit23/sheet-1..2.png + test-1.png · unit24/sheet-1..2.png + test-1.png · unit25/sheet-1..2.png + test-1.png · unit26/sheet-1..2.png + test-1.png · unit27/sheet-1..3.png + test-1.png · unit28/sheet-1.png + test-1.png · unit29/sheet-1..4.png
  miniexam/    exam01/page-1..5.png (110 dpi; page 1 = score sheet, 2 듣기, 3 읽기, 4–5 쓰기)
  review/      midterm01/page-01..17.png (80 dpi) · vocabulary/page-01..48.png (80 dpi) + vocabulary/unit23-37/page-01..36.png (100 dpi) · lecture/page-01..18.png (150 dpi — photos need it)
content/       ✍️ SOURCE OF TRUTH — edit here, never in output/
  guide/       00_exam_info.md = ส่วนที่ 0 (shared cover of both books; `{{today}}` / `{{days:YYYY-MM-DD}}` are filled at build time,
               so the countdown column never goes stale) · 01_units/unit05…37.md (ส่วนที่ 1 of the By_Unit book, unified template:
               หลังจบบท → 🗣️ vocab → 📝 grammar with 📽️ slide material inline + "ไวยากรณ์ข้อ NN" refs → 💬 대화 → 📖 읽기·듣기 → 🔊 발음
               → 🧪 tests → 🔗 links) · 02_grammar/NN_slug.md (ส่วนที่ 1 of the By_Topic book, topics 01–64 — 36–64 = 23–37과, numbering fixed in content/specs/SPEC_23_37.md, unified template:
               📌 รูปแบบและเงื่อนไข → 📖 ตัวอย่าง (slides merged) → ⚠️ จุดสับสน → 🧪 ออกสอบแล้ว → 🔗 เชื่อมโยง)
               03_particles.md (ส่วนที่ 2) · 03b_question_words.md (ส่วนที่ 3, 5–37과; §3.3 = every answer pattern: 5 rules · yes/no questions by ending · each 의문사 · checklist) · 05_selftest.md (ส่วนที่ 5) ·
               06_quickref.md (ส่วนที่ 6 — ASSEMBLED from per-topic snippets the rewrite agents wrote; 36–64 appended 2026-10-26 from
               06_quickref_parts/NN.md (kept; re-append if a snippet changes); keep 64 entries in topic order)
               04_vocabulary/unit05…22.md (centre's word lists, `###` heading, Thai+English) · unit23…37.md (since 2026-11-01 = the centre's sheet for 23–37
               in sheet order + `#### ∞ 읽기/듣기 ∞` blocks + `#### ศัพท์เพิ่มเติมจากตำรา` = the textbook-margin words of the 10/26 version the sheet lacks;
               glosses are Sonnet's, the user's pencil ignored) · 90_themes.md (picture themes; 11/1 gained ◆ ㅂ 불규칙 23 · ㄹ 탈락 25 · ㄷ 불규칙 31 · 르 불규칙 32 ·
               동사 2 · 형용사 2, the last two headed "(23과)" only for the loader; ◆ 문제 지시어 — คำในคำสั่งโจทย์ (5과) = 29 instruction words) · 91_categories.md (old AI list)
               **Since 2026-11-01 evening every unit file 5–37 ends with `#### ศัพท์เพิ่มเติมจากตำราและเวิร์กบุ๊ก (ไม่อยู่ในชีตของศูนย์)`** (the 23–37 margin sections were
               renamed into it): 416 words of the textbook and workbook the centre's sheets lack (있다/없다, numerals 영…만 / 하나…아흔, months 일월…십이월, 선물, 계획,
               중국집, 분위기 …), each in the FIRST unit it appears. Found by scratchpad Kiwi lemmatiser diff (textbook OCR ∩ guide chapter, + workbook) minus the site
               words, judged and glossed by 3 Sonnet agents (content/specs/BRIEF_vocab_gapfill.md); duplicates across units removed by hand. 1,366 words on the site.
               07_lecture/unitNN.md = ARCHIVE of the slide transcription (`#### 📽️ [topic:NN] …` blocks). Since 2026-10-16 evening
               its content lives inside 01_units and 02_grammar; build.py no longer assembles it.
               (a part = one .md OR a directory joined in name order; dirs start with 00_header.md) · part banners say "ส่วนที่ N", never "ภาค"
  exercises/   workbook/unit05…22.md (+ unit21_review_5-21.md = 5~21과 종합문제)
               everyday/unit00_classroom.md, unit05…20.md, unit22.md (test 22, 8.5/10), unit23.md (sheet 23, user's pencil)  (매일시험 + 연습지 merged per unit)
               miniexam/exam01.md  (복습시험 ① as sat: one `##` per paper — score sheet · 듣기 · 읽기 · 쓰기 — then `# 정답`)
               listening/unit05…37.md  (본문 듣기 sheets, user's pencil checked; key = textbook dialogue; 23–37 added 2026-11-01 from the 23–37 vocab book —
               every sheet uses 대화 NN-1, verified against Whisper; O/X and choice keys of 27–37 are the agent's reasoning, the appendix has none for 29–31/33–35)
               review/midterm01_part1.md + _part2.md  (teacher's 중간시험 복습문제; parts are merged by build.py review; since 2026-10-21 the
               듣기 keys are real — derived from the teacher's audio in source/audio/review/, each ฟัง heading has a 🔊 line naming the file)
               listening/scripts_appendix.md  (2026-10-21: the book's 부록 — 듣기 scripts of 8·12·16·20과 with Thai + the printed 읽기/듣기 keys 5–21;
               not part of KMU_Listening.pdf. Disagreements found and NOT yet fixed: guide 01_units/unit12 answers 마키 씨가 아르바이트를 해요? with
               "오늘 아르바이트를 안 해요" where the book says "아니요, 기숙사에서 쉬어요"; unit20 omits 다.3 방학에 뭘 할 거예요?; listening/unit15 A4
               (남자는 영어와 일본어를 배워요 = O) is suspect — in the audio it is the sister; listening/unit19 B6 was fixed 10일 → 20일)
               each file = questions, then its own answer key (`# [PART 2]` / `# 정답`)
               00_header.md in each dir = ONE title line only (a longer header is printed before every unit)
  specs/       SPEC_extraction.md (original scan→md rules) · SPEC_14_22.md (unit 14–22 contract; reuse for 23+)
               SPEC_confusions.md (27 Thai-learner confusion pairs A1–C10 → `### ⚠️ จุดสับสน` in 02_grammar/)
               SPEC_colors.md (colour-by-function classes, the Korean↔Thai mirroring rule, ambiguous Thai words, batch format)
               SPEC_predict_midterm.md (brief for the midterm mock-paper agents: facts, file/markdown rules, house style, mistake list)
               SPEC_23_37.md (2026-10-26: contract for book 1-2 — sources, the fixed grammar numbering 36–64, templates per deliverable)
               SPEC_derivations.md (2026-10-28: the "สูตรและวิธีทำ" contract — teacher-whiteboard-style numbered rules + step-column worked tables
               for every formula-type grammar point; §5 = topic→agent/unit assignment, §3 = which stem classes each family must show, §4 = the user's ✗ forms)
               SPEC_book_style.md (2026-10-27: the book-style contract for both guides — heading levels, INTRO/SUMMARY boxes, lead sentences,
               one-example-per-line density rules, chapter/topic skeletons, what may never be dropped, the pre-submit checks)
  predictions/ everyday/unitNN.md (매일시험 — unit17 … unit20, unit22 … unit28) · miniexam/examNN.md (복습시험 — exam02) ·
               midterm/midterm01.md (중간시험 1–21과, 2026-10-18) = ASSEMBLED from midterm/parts/01_analysis.md (Fable) +
               02_writing · 03_reading · 04_listening · 05_speaking (+ _key.md, Sonnet agents) by the scratch script
               assemble_midterm.py (questions, then `# 정답` + keys) — edit the parts, re-assemble, `build.py predict`
               🔮 analysis + mock tests, then `# 정답`; the kinds never share a folder
  mindmaps/    unit05…37.md + all.md — mind-map OUTLINES (see scripts/build_mindmaps.py for the grammar). Per unit: 문법 (forms,
               conditions, ⚠️) · 어휘 · 표현·대화 · 연결 (← 이전 / → 이후 / 시험). all.md = 11 cross-unit threads (문장 끝맺기 · 조사 ·
               시제 · 숫자·시간 · 높임 · 부정·질문 · 묘사·장소 + since 10/26 연결어미 · 관형형 · 희망·능력·의무 · 불규칙; 240 nodes, a tall poster page) — the per-unit 연결 branches must agree with it.
  mockweb/     practice-site data, one JSON per source: mini02.json (복습시험② prediction) · mini02_real.json (② as sat, ids mini02r-*, Agent T
               2026-10-20) · mid_writing / mid_reading / mid_listen_speak.json = **midterm mock v2** (2026-10-20, ids mid-writing-a/b, mid-reading-a/b,
               mid-listening-a/b, mid-speaking; brief content/specs/BRIEF_midterm_v2.md; the old midterm-* ids are gone) · mini02_b.json / mini02_c.json (papers 2 and 3,
               2026-10-19, 2 Sonnet agents from content/specs/BRIEF_mini02_extra.md; b = most-tested items, c = the user's weak points + 19–20과) · review_p1/p2.json (teacher's
               복습문제; its 듣기 has no script so it is left out) · mid_writing / mid_reading / mid_listen_speak.json (중간시험
               prediction). Written by 6 Sonnet agents 2026-10-18 from the Markdown sources; when a source changes, fix the JSON too.
               (2026-10-21) vocab_a/b.json (vocab-5-13 · vocab-14-21: 30 Thai→Korean blanks + 30 Korean→Thai MC each, most-tested words first) ·
               vocab_spell.json (vocab-spelling: 30 dictation phrases built around the §6b trap words) · mid_speaking_final.json (mid-speaking-final-a/b =
               mocks 1–2 of the interview bank, 25 speak items each) · review_listen.json (review-listening: the teacher's 듣기 1–12 with her real mp3s,
               40 sections = one per audio file, 46 items; ⚠️ 거리/고리, 부모/보모, 형/성, 각자/가자, 신촌/신천 are best guesses from the audio) ·
               textbook_listen.json (tb-listen-5-13 · tb-listen-14-21: one section per unit = the 본문 듣기 sheet items over the real 대화 track N-1.mp3) ·
               scores.json (NOT a set: the grading table → window.KMU_SCORES for the profile view; fill new marks by hand: terms → skills → components
               {name, group, max, got|null, date, note} + daily / review / presentations + `midterm` (the 10/27 slip)).
               (2026-10-27) daily_a.json (units 05–13) · daily_b.json (14–24): every 매일시험 as sat = `daily-NN-writing` (A/B parts) + `daily-NN-listening`
               (the dictation, one section per sentence, voice T = teacher) + `sheet-NN-writing/-listening` (the practice sheets; sheet-20-listening plays the
               real 20-2.mp3), exam id `daily`, and a per-paper `"group"` string ("매일시험 23과 · 27 Oct · 4.5/10") that the home board groups by ·
               daily_predict24.json = the 24과 prediction (3 writing mocks + `predict-24-listening`, 35 dictation candidates read by the teacher voice). (2026-10-28) daily_b.json gained `daily-24-writing/-listening` (test 24, 8/10) and `sheet-25-writing`; daily_predict25.json = the
               25과 prediction (`predict-25-1/2/3-writing` = textbook / workbook / sheet-table mocks, `predict-25-vocab` 30 words, `predict-25-listening` 20 short
               dictation phrases); the predict-24 sets' group lost its 🔮 ("เก็ง 매일시험 24과 · สอบแล้ว …") so the board no longer pins a finished prediction —
               do the same to each old prediction when its test comes back. Site published as version 45: 96 sets · 1,882 items · 723 clips.
               (2026-11-01) v46: daily_b.json + daily-25-writing/-listening (test 25, 9/10) and sheet-26-writing; daily_predict26.json (predict-26-1/2/3-writing =
               workbook / sheet / textbook mocks, predict-26-vocab 30, predict-26-listening 20; predict-25 lost its 🔮); textbook_listen2.json = tb-listen-23-29 ·
               tb-listen-30-37 (본문 듣기 23–37 over the real NN-1.mp3, 41 items); vocab.js = 950 words from the centre's 23–37 sheets (v47, same evening: 1,366 with the textbook/workbook gap fill); VOCAB_PRIO now starts
               28, 22, 26, 27, 25, 24, 23 … (11/3: the teacher said test 28 WILL ask 28 · 22 · 26 words — colours, fruits, animals, weather, sports 하다/타다/치다). The word clips are split by build_mockweb.py over VCLIP_FILES = clips3.js + clips4.js (13.5 MB cap each; clips3 alone
               had reached 14.1 MB) — app.html loads both; add a file + <script> tag when the build says so. 106 sets · 2,029 items · 834 clips + 947 word clips ·
               73 real mp3s. **Publish files now = {data.js, clips.js, clips2.js, clips3.js, clips4.js, vocab.js, vendor.js} + any NEW mp3** (v46 sent 23-1 … 37-1).
               Rules learned: the validator accepts `s` = F/M/T/S now; `<보기>` is rejected (write [보기]); a file whose name starts with `_` is a draft the
               build ignores (agents validate `_x.json`, then rename) — several agents can write sets while another builds the site.
               A section may carry `"audio": "audio/<textbook|review>/<file>.mp3"`: the site plays that real recording for ▶ ฟัง (no karaoke) and
               build_mockweb.py copies it from source/audio/ to output/2_Practice_Web/audio/ — publish those files with the artifact.
  speaking/    발표 scripts in the my_room.md format (Korean line · Thai reading · Thai meaning · swap table · Q&A · pitfalls):
               my_room.md (발표 ① 제 방) · myself.md (발표 ② 자기 소개, 10/21) · vacation_plan.md (방학 계획, 10/20) → build.py speaking
  syllabus/    one-off PDF (Thai syllabus): python3 scripts/make_pdf.py <md> --pdf-dir output
scripts/
  build.py       ⭐ python3 scripts/build.py [guide|exercises|everyday|miniexam|predict|review|speaking|all]
  make_pdf.py    Markdown → PDF (WeasyPrint); `--pdf-dir DIR` puts the PDF somewhere other than next to the .md. Book stylesheet since
                 2026-10-27: Sarabun (Laksaman) 15.5px + Noto Serif CJK KR; running heads (chapter left from h2 `string-set`, part right
                 from h1; cleared on part pages), page x / y bottom right, colour legend bottom left, nothing on the cover; h1 = part title
                 page, h2 = chapter page, h3 = section auto-numbered per chapter inside `<body class="book">` (set by the `<!-- kmu:book -->`
                 marker build.py puts on the two guides; any other document with `[TOC]` gets class `cover` = cover page + TOC leaders, no
                 numbering); TOC = chapters only (toc_depth 1-2) with dot leaders + page numbers, cover/TOC entries hidden; callouts
                 `> [!NOTE|TIP|IMPORTANT|WARNING|CAUTION|INTRO|SUMMARY] optional title` with Thai labels; `wrap_korean_words()` wraps every
                 Hangul chunk in `<span class="kw">` (nowrap, 0.95em) so a Korean word never breaks mid-word; orphans/widows 2,
                 `tbody > tr:nth-child(-n+2) { break-after: avoid }` (a table never leaves 1–2 rows at a page bottom), thead repeats.
  book_style_check.py  checks guide files against SPEC_book_style.md (bold pseudo-headings, INTRO/SUMMARY count, `·`-chains, ### without
                 a lead sentence, tables in list items, ~~, and the Korean-token count vs git HEAD — < 95 % = content was dropped)
  pdf_artifact_scan.py  pdftotext every PDF under output/ (or the ones given) and prints file:page for raw tags (<span, class=, &lt;),
                 unrendered Markdown (**, ~~, *(, `, > [!, ####, |---), colour braces or \_ — run it after every full build; exit 1 = hits.
                 Found on 2026-10-27: Korean inside `code spans` got the kw wrapper (now skipped), a #### right after a table row (needs a
                 blank line), 4-space-indented ①②③④ option lines in the midterm prediction (= code blocks; de-indented), nested italics in
                 everyday/unit23.md, and quoted calendar tables in workbook 13과/19과 (github_compat's hard-break suffix broke them; fixed).
  ocr_extract.py textbook PDFs → extracted/textbook/   (args = unit numbers)
  build_mindmaps.py   ⭐ content/mindmaps/*.md outlines → output/1_Guides/mindmaps/KMU_Mindmap_<name>.{html,pdf,png}
                 Bilateral mind map in the diagram-design plugin's visual grammar (paper/ink tokens, 4px grid, rounded
                 right-angle connectors with a sibling bus, accessible SVG, header/legend/footer). Outline grammar:
                 `# root` · `## branch [@left|@right]` · `### node` · `- leaf` (two-space indent = level 4);
                 "한국어 | ไทย" = two-line label. `--check` = parse + layout only. The web .html keeps SVG text
                 (Google Fonts incl. Noto Sans KR/Thai); the print variant puts labels in HTML divs over the SVG
                 shapes because WeasyPrint's SVG text drops Thai combining marks (dotted circles). PDF → PNG via pdftoppm.
  mindmap_midterm.py  (superseded 2026-10-16) Graphviz card poster of exam week — the user rejected it as "not a mind map".
  build_mockweb.py ⭐ content/mockweb/*.json (exercise sets, schema = content/specs/SPEC_mockweb.md, checked by
                 mockweb_validate.py) + scripts/mockweb/app.html → output/2_Practice_Web/. Voice clips via the free edge-tts
                 library (pip --user; SSL context patched to the system CA bundle because the sandbox proxy re-signs TLS),
                 cached in extracted/mockweb_clips/<sha1>.mp3 — only new lines are generated. Since 2026-10-27 it also writes vocab.js
                 (window.KMU_VOCAB = every word of content/guide/04_vocabulary/unit05…37.md + the picture-theme sheet, 912 words, deduplicated,
                 sorted in drill priority 24 → 23 → 25 → 22 → 26 … 37 → 21 … 5, VOCAB_PRIO) and clips3.js (one SunHi clip per word, 13.4 MB — the 16 MB
                 artifact file limit is the ceiling; split it when more words come). Needed because Chrome on Ubuntu
                 has no Korean voice (espeak-ng). After a rebuild, republish the artifact (file_path scripts/mockweb/app.html,
                 files data.js + clips.js from output/2_Practice_Web, url above).
  build_speech_audio.py  (see 6_Speaking) — since 10/21 also: interview format (`**N. 질문**` + one or more `**→ 답**` lines, questions voiced
                 by SunHi, answers by the chosen voice, hide mode "ซ่อนคำตอบ" blurs answers until tapped and play-all leaves 6 s to answer),
                 colour by word function via kotag (nested .w karaoke spans → .k<cls> segments; Thai gloss coloured with tag_thai),
                 collapsible options row (⚙, folded by default under 640 px).
  Speech-to-text: faster-whisper 1.2.1 (pip --user; model "small", int8 CPU, decode the mp3 with ffmpeg to f32le 16 kHz and pass a numpy
                 array — the bundled `av` 19 breaks faster-whisper's own decoder). ~95 % right on the clean course audio; numbers and rare
                 words need checking. Scratch script: scratchpad/whisper_run.py (not in the repo).
  _archive/      superseded: mindmap_midterm.py (rejected poster), mock_clips.py + exam02_mock.html (first single-set mock page)
  kotag.py       ⭐ colour-by-function tagger used by make_pdf.py and build_mindmaps.py at render time. Tag syntax in
                 Markdown: `{n:학생}{p:이} {x:아니에요}` (one letter, UPPERCASE = honorific). Korean runs are tagged
                 automatically (kiwipiepy + user words from 04_vocabulary + override rules for pattern tokens like
                 `-(으)ㄹ 거예요`, `은/는`); Thai glosses `*(…)*`, 🇹🇭 lines and ไทย/ความหมาย table columns get an
                 automatic first pass (pythainlp newmm + TH_FUNC lexicon + vocab-derived lexicon). Anything already
                 carrying `{c:}` tags is left alone → to fix a wrong colour, write the explicit tag into content/*.md.
                 CLI: `kotag.py tag "…"` · `kotag.py check file.md` (prints tagged lines) · `kotag.py thdebug "ไทย"` ·
                 `kotag.py extract files… > batch.tsv` + `kotag.py merge batch_out.tsv` (agent review round-trip).
output/        🤖 GENERATED — overwritten every build, never hand-edit. Reorganised 2026-10-18 by PURPOSE (the user was lost in
               a flat folder of PDFs). Entry point for the user = output/START_HERE.html (hand-written Thai index — update its
               links when a deliverable is added or renamed) + README.md at the workspace root.
  START_HERE.html
  1_Guides/      KMU_Guide_By_Unit.pdf (เล่ม 1, 613 pp since the 10/27 book-style rewrite + textbook completeness audit + the complete 26과; was 200) ·
                 KMU_Guide_By_Topic.pdf (เล่ม 2, 642 pp; was 357)
                 · KMU_Mindmaps.pdf (34 maps) — the page growth comes from Sarabun (BASE_PX 14.5 after the user asked for one step smaller;
                 15.5 gave 521/692), one-example-per-row tables and the intro/summary boxes; BASE_PX in make_pdf.py is the one knob
                 · KMU_Syllabus_2026_Fall_TH.pdf (one-off: make_pdf.py <abs path to content/syllabus/syllabus_th.md> --pdf-dir
                 output/1_Guides, then rename) · mindmaps/KMU_Mindmap_<name>.{html,pdf,png} (build_mindmaps.py)
  2_Practice_Web/ ⭐ practice website (build_mockweb.py): index.html + data.js (window.KMU_SETS, 26 sets, 601 items as of 2026-10-20 evening) + vendor.js + clips.js
                 (window.KMU_CLIPS, 252 neural clips ~6 MB) + start.sh (localhost server → microphone works in Chrome).
                 Published as https://claude.ai/artifact/14Xbi9kWyQgDryHzk7kuzm from scripts/mockweb/app.html with
                 files {data.js, clips.js}; the claude.ai frame refuses the microphone (no capability for it) → typing only there.
                 Since v9 the artifact declares capabilities {db, user}: answers/scores per set sync through the viewer's private
                 db subtree data/users/<id>/<setId> (last change wins per set, `stamp:<id>` in localStorage) — iPad ↔ PC on the
                 claude.ai link only; the local index.html keeps its own localStorage. Since v11 also `sample`: unmatched sentence
                 answers show ? (pending) and a 🤖 AI ตรวจ button — one batched sample.json call (passage/script + q + models + answer)
                 fills the ○ △ ✕ self-grade and an `ai:<setId>` Thai comment (synced). Republish without `capabilities` to keep them.
                 v13 (2026-10-19): per-set cover page → ▶ เริ่มสอบจริง (exam clock from an absolute endAt, auto-run listening/interview,
                 Thai glosses hidden, auto-submit at time-up) or ✎ ฝึกทำ; ⏸ pause/resume via `attempt:<id>`; results card with per-section
                 scores + `hist:<id>`; on submit AI grades every typed write/blank/speak answer that missed exact match (chunks of 12, 2 at once).
                 Old bug fixed: the per-section answer countdown used to overwrite the exam clock (15 min looked like 15 s).
                 v20–23 (10-19/20): text size = --ts font factor (CSS zoom double-scaled inputs in Chrome) · conjugation rows render as a
                 .conj grid · fix lines: .corr red vs .tip blue-grey under correct items · karaoke: clips.js also carries KMU_WORDS
                 (edge-tts WordBoundary → [start,end,word], cache <sha1>.mp3.json; all clips were regenerated) and say(text, voice, el)
                 lights .w spans; transport bar #tp (pause keeps the clip alive via userPaused/curFin).
                 Test harness (fake Audio, virtual time): scratchpad/harness/run.py — not in the repo.
                 v25 (2026-10-20, Sonnet port from content/specs/BRIEF_preact_port.md, 245k tokens / 14 min): the engine is **Preact 10.29 +
                 @preact/signals 2.11 + htm 3.1**, vendored as UMD builds in scripts/mockweb/vendor.js (copied to output/, published as a third
                 artifact file; no CDN, works offline). CSS, ids, `kmuweb:` keys, cloud/AI/karaoke modules and window.__kmu are unchanged, so old
                 progress loads as before; every harness driver matches v24 (only wall-clock stamps differ). Under the harness (window.__fake)
                 rendering is flushed synchronously; real browsers keep Preact's batched rendering.
                 v28 (2026-10-21): 34 sets · 906 items · 586 clips. clips.js is split in two (clips.js + clips2.js, each < 16 MB = the artifact file limit;
                 clips2.js also carries KMU_WORDS) · sections with `audio` play real mp3s (57 files under output/2_Practice_Web/audio/, 33 MB) ·
                 👤 โปรไฟล์ view (#profile, Sonnet agent): grading tables per term from scores.json, stacked earned/lost/pending bars, practice results per
                 skill from hist:<id> with sparklines, Thai summary. v29: the home board names its groups through `GROUPS` in app.html (regex on set id →
                 label + note: สัมภาษณ์จำลอง · ชุด A · ชุด B · ฟังหนังสือ · เขียนตามคำบอก · ทดสอบศัพท์ · ข้อสอบจริง); ids with no rule fall back to ชุดที่ N —
                 add a rule when a new kind of set is added. v30 (10/21 night): speaking sets get a real score — per speak item self ○△✕ > AI o/h/x > pending
                 (grade() no longer skips them; score entries carry spoken:true + n = answered count, old entries without n are shown as 'ตอบ s/t' via oldSpk());
                 SpeakOut shows ถูก/ครึ่ง/ผิด buttons + the verdict line; its ✓/✕ checks ignore spaces (a space in a check regex = \s*, sentence check = ≥3 syllables or a
                 요/다/까 ending) because the answer is a speech-to-text transcript, and AI_RULES tells the grader the same for type speak only. v32–v34: viewing an old result regrades and writes the score back (upgrades pre-v30 speaking
                 entries), the home group header shows คะแนน + ตอบ n ข้อ for speaking, and the cover has 🗑 ล้างผลชุดนี้ (two-step confirm; resetSet() store.set(null) on
                 ans/self/ai/score/hist/attempt so the removal also syncs to the cloud). v35 (10/22): dlg() in app.html puts every speaker turn of a dialogue prompt (q text and sec.box) on its own line at render time — a 가/나/A/B/남자/여자/○○ 씨 label, or any short label after .?!) or ___, starts a new line; 21 prompts in mid_writing.json were run-on, the rest already had \n. v36: Fix() under each graded item = three labelled rows 📘 เฉลย (stored key + why) · 🤖 AI (verdict/comment/แก้เป็น or ยังไม่ได้ตรวจ) · ✋ ตรวจเอง (ถูก/ครึ่ง/ผิด); the row whose result sets the score carries a นับคะแนน tag. v37: aiV(r, answer) — an AI h/x whose own `fix` equals the answer (spaces/punctuation ignored, squash()) is scored and shown as ถูก (with a note); applied in grade(), Fix, SpeakOut, AiBox, also to verdicts already stored. AI_RULES gained: fix == answer ⇒ v must be o, no h/x without a named error, open personal questions (뭐 하세요?) accept any sensible content. v38: the grader call uses AI_OPTS = {model 'claude-opus-5-5', effort 'high', modelTier 'complex' as fallback} (user's choice 10/22; was modelTier 'default'). It is the only sample call in app.html. v39: results AI line has 🔄 ให้ AI ตรวจใหม่อีกรอบ (RedoBtn, two-step confirm) → aiRedo() clears ai:<id> (self marks kept, they still win), regrade(), aiGradeAll() — re-grades without retaking. v40: new set vocab-mistakes (content/mockweb/vocab_mistakes.json, 73 items: A 40 Thai→Korean words the user has misspelled · B 8 number+counter · C 13 word-choice MC · D 12 spelling MC; every `why` names what the user wrote and where). Sources = the user's synced practice answers (ArtifactData list data/users/me on the site artifact → 94 wrong items) + §6b. Home group 🎯 ศัพท์ที่เคยผิด. **v41 (2026-10-27, Sonnet agent from content/specs/BRIEF_vocab_drill.md, 550k tokens / 39 min):** 🔤 ศัพท์ view (`#vocab`, Strip button, home teaser card): วันนี้ = a Leitner session over KMU_VOCAB (due words first, then new words; chips 20/30/40/50 words, default 40, and "คำใหม่อย่างน้อย" 0/10/15/20, default 15 — with 0 a simulation met only ~180 of 912 words in 24 days), typed mode (Thai → type Korean, judgeText, near miss = half, ▶ plays the word clip) or card mode (tap to reveal, จำได้/ไม่แน่ใจ/จำไม่ได้, keys 1/2/3); boxes 0–5, intervals [1, 2, 4, 7, 14, 30] days after a right answer, half = same box due tomorrow, wrong = box 0 re-queued until right; end card with the missed words + ทำอีกรอบเฉพาะที่ผิด; ตามบท = all words of one unit (chips 5–37, shuffle); สถิติ = seen/learned (box ≥ 2)/mastered (box ≥ 4)/due, streak, per-unit bars, 20 most-missed words, two-step reset. Progress = `kmuweb:vocab:srs` {w: {ko: {b, d, n, x, l}}, days}, synced as cloud doc `srs` (3 s debounce); preferences vocab:size/mode/auto/shuffle/newmin are store.put only (store.set would make cloud docs). Home board: EXAMS gained `daily` (date null → no countdown) and `final`; a set's own `group` string beats the GROUPS rules (🔮 first, then newest unit); sets with a group render full cards; the strip collapses to icons ≤ 560 px. Test hooks window.__kmu.vocab.{start, answer, next, giveUp, reveal, grade, unit, mode, …}. 87 sets · 1,733 items · 699 clips + 909 word clips · 58 real mp3s. Published 10/27 as version 41. **v44 (10/27 night):** the card mode is a **4-choice quiz** (the user: "flash card = choices, not จำได้/จำไม่ได้"): `vocab:dir` = k2t (한국어 → ไทย, ▶ before answering) · t2k (ไทย → 한국어, silent until answered) · mix (default, drawn per card); vMc() picks 3 distractors from the same unit first, then the same cat, then units ±2, never a word with the same th/ko; s.mc = {dir, opts:[{ko,d}], ans}; keys 1–4 pick, a right pick auto-advances after 0.7 s, a wrong one shows the feedback (correct green, chosen red, 「chosen」 = its meaning) and waits for ถัดไป/Enter; score 1/0 only (no half) into the same Leitner boxes. Hooks: vocab.dir(d), vocab.pick(i), state().mc. Checked in headless Chrome (window.__fake, scratch test page) — no harness in the repo. v43 = the 24과 vocab prediction set predict-24-vocab (32 items) in daily_predict24.json + §2.0 vocab tables and ชุดที่ 4 in predictions/everyday/unit24.md. **Publish files = {data.js, clips.js, clips2.js, clips3.js, vocab.js, vendor.js} + every audio/**/*.mp3 (files left out of a publish are kept, so after a rebuild send only the .js files + any NEW mp3)**/*.mp3**
                 (`Artifact list scope files` first; 61 files ≈ 49 MB per publish, under the 64 MB limit). The scratchpad harness was lost with /tmp —
                 regression now = headless-Chrome screenshots of #profile, a set cover and the home page.
  3_Exam_Prep/   KMU_Predict_midterm01_speaking.pdf (2026-10-21, from content/predictions/midterm/speaking_exam.md via make_pdf.py --pdf-dir + rename:
                 interview question bank A table/B 19과 sheet/C 자기 소개/D 가족 with 해요체·합니다체 model answers + alternatives, 3 mock interviews, key) ·
                 KMU_Review_Midterm01.pdf (teacher's 중간시험 복습문제) · KMU_Predict_midterm01.pdf (v2 2026-10-20, 45 pp; parts assembled by
                 scripts/assemble_midterm.py, then build.py predict) · KMU_Predict_miniexam02.pdf · past/KMU_MiniExam_02.pdf (② as sat + AI key)
                 · past/KMU_MiniExam_NN.pdf (복습시험 as sat)
  4_Daily_Tests/ KMU_Everyday_unitNN.pdf ⭐ one small PDF per unit (what the user prints day to day) · predictions/KMU_Predict_unitNN.pdf
  5_Homework/    KMU_Workbook.pdf (워크북 5–22 + 종합문제) · KMU_Listening.pdf (본문 듣기 5–22)
  6_Speaking/    KMU_Speaking_MyRoom.pdf · KMU_Speaking_Myself.pdf · KMU_Speaking_VacationPlan.pdf
                 · KMU_Speaking_Myself_Audio.html (2026-10-20, `python3 scripts/build_speech_audio.py myself`: one InJoon edge-tts clip per
                 numbered line of content/speaking/<name>.md with word timings, cached in extracted/speech_clips/; single-file player with
                 per-line / whole-speech play, karaoke highlight, 0.7–1× speed, hide-Thai / hide-Korean drill modes; published as
                 https://claude.ai/artifact/UB8eXhn7DoTV6pVQDVMPSC (public link since 10/20) — works for vacation_plan / my_room too)
                 · KMU_Speaking_Interview_Audio.html (2026-10-21, `build_speech_audio.py interview` from content/speaking/interview.md = the question bank of
                 speaking_exam.md in Q/A format: 75 questions × 2–3 answers = 299 clips, 8 MB; Thai readings were script-generated by the agent, spot-checked
                 only; the flat list was superseded the same evening — kept on disk only)
                 · KMU_Speaking_FoodIntro.pdf + _Audio.html (2026-11-04, content/speaking/food_intro.md + food_intro.jpeg = the user's Gemini picture, dish + ingredients: 음식 소개 for the 말하기 on Fri 11/6, slide = -(으)ㄴ · -고 싶다 · -고 · -지만 · 보다 · 중에서 제일 + 5 questions; 팟타이, 13 lines 해요체; audio page published PRIVATE as https://claude.ai/artifact/FNs9oSPq3pgC49LfRR6bpE)
                 · KMU_Speaking_InterviewCards.html ⭐ (2026-10-21, `python3 scripts/build_interview.py interview_cards` from content/speaking/interview_cards.md:
                 `## emoji 한국어 · ไทย` category → `### Thai intent (Korean key)` card → `**Q. …**` variants + `**→ …**` answers + `💡` tip, every Korean line with
                 `*reading*` and `🇹🇭`; 12 categories · 68 cards · 198 question variants · 267 answers, 12 MB; Sonnet agent regrouped the bank, readings of the
                 added lines are the agent's). Page = category chips filter + collapsible cards (▶ on a card = first question then every answer), same controls
                 as the speech player (speed/loop/ซ่อนไทย/ซ่อนเกาหลี/ซ่อนคำตอบ/คำอ่าน/size/theme, kotag colours). Published PRIVATE as
                 https://claude.ai/artifact/LCavjNUStqqQL4txtesUvj (the interview artifact's URL, replaced), watch stopped. build_interview.py imports clip()/
                 ko_html()/th_html() from build_speech_audio.py.)
  _build/md/     the intermediate Markdown behind each PDF (grep here: `grep -c '~~' output/_build/md/*.md output/_build/md/*/*.md`)
```

### Daily routine — the teacher hands out a new test/sheet
1. Save the scan as `source/everyday/KMU everyday test unit NN.pdf` (or `… sheet unit NN.pdf`).
2. `pdftoppm -r 110 -png "<that pdf>" extracted/everyday/unitNN/test` → read the pages.
3. Write / extend `content/exercises/everyday/unitNN.md` (questions, then `# 정답`; ⚠️ = teacher marked wrong).
4. `python3 scripts/build.py everyday` → `output/4_Daily_Tests/KMU_Everyday_unitNN.pdf` (seconds; nothing else rebuilt).
5. If the user wants a prediction for tomorrow's test: write `content/predictions/unitNN.md`, then
   `python3 scripts/build.py predict`. Pattern evidence lives in unit18.md §1 (with the 17과 scorecard) — the
   practice sheet handed out the day before becomes section B of the test (checked 2026-10-14 for every unit that
   has a sheet: 8, 11, 12, 15, 16, 17 match outright, 10 and 13 partly — the rest of B then came from 대화/준비;
   units 5, 6, 7, 9 and 14 have no sheet, so nothing to compare); dictation (C) is sentences from that unit's
   textbook 대화/읽기 **and the 발음 practice sentences** (9과, 11과, 17과 all drew on the 다. list), sometimes a bare
   two-word phrase (옛날 물건, 회사 생활). Verified against the textbook for 6–17과 on 2026-10-14: 27 of 33 dictated
   items are verbatim 대화/읽기/발음/준비 lines, 4 come from 연습 pattern lists, 2 were not found (9과 학생회관 뒤,
   12과 기숙사에서 쉬어요 — probably the 12과 듣기 audio); 5과 had no C. A is the unit's picture vocabulary, often the
   workbook's exercise 1 pictures, or "pick the word from <보기>". Both tables live in predictions/everyday/unit18.md §1.
   The 17과 prediction scored: format = mock 1, A items 3–4 word-for-word, C8 exact, C9/C10 partial.
   The 18과 prediction scored even better (test = 10/10): mock 1 had two of the four clocks (08:15, 11:20), two of the
   three B pairs (도서관/책을 빌리러, 은행/돈을 찾으러) and C8 exact, C10 half (체육관에 가요). The teacher now also drops
   hints the day before (19과: "부터~까지 time + 거예요") — put them at the top of the prediction when given.
   Since 22과 the paper is always A 4 (grammar 1) + B 4 (grammar 2) + C 2–3 dictation, and A/B items are lifted from the textbook 연습 and the
   workbook almost verbatim (24과: workbook C2/C4, 연습 2 p.243 cues, 연습 2 p.245 signs); the sheet the day before names the grammar but not the item
   format. Mock set 1 of a prediction should therefore copy the textbook 연습 lists, set 2 the workbook (predictions/everyday/unit25.md does this). 25과 B was the
   workbook F pictures in full (2nd time in a row a workbook section was lifted whole) → since 26과 mock 1 = workbook, 2 = sheet, 3 = textbook, and the dictation
   list also carries grammar example sentences (25과 C10 기숙사에 삽니다 was one).
6. A returned 복습시험 (the user says "mini exam"): save as `source/miniexam/KMU mini exam NN unit AA - BB.pdf`
   (score sheet + all papers in one PDF), `pdftoppm -r 110 -png "<pdf>" extracted/miniexam/examNN/page`, transcribe to
   `content/exercises/miniexam/examNN.md` (one `##` per paper, Thai glosses, ⚠️ where the teacher deducted; there is
   no audio script — the 듣기 key is whatever the red pen shows), `python3 scripts/build.py miniexam`. The prediction
   for the next one goes in `content/predictions/miniexam/examNN.md` → `build.py predict`. In the transcription use
   Thai `###` headings with the Korean instruction in the italic line when the items must NOT get ruled lines
   (쓰세요 in a `###` heading triggers them — see §5); keep the Korean heading for 문장을 만드세요 items, which should.
   There is no combined everyday book (user asked to drop it 2026-10-10); `… all` refreshes guide + workbook too.

### 2.1 Source file naming scheme
`KMU <material> [<qualifier>] unit <NN>[ - <NN>].pdf` — every source PDF carries the word `unit`
and a zero-padded unit number or range. `KMU` is the only capitalised word; material names are
lowercase (`workbook`, `everyday test`, `everyday sheet`, `syllabus`, `student's book`).
Zero-padding matters: without it `unit 10` sorts before `unit 5`.
`scripts/ocr_extract.py` builds the textbook paths with `f"...unit {unit:02d}.pdf"`, so a file that
is not zero-padded will not be found.

### 2.2 git (since 2026-10-20)
- Folder renamed `KMU Korean` → `KMU_Korean`; remote `origin` = https://github.com/beamkeerati/KMU_Korean.git (branch `main`).
  The user's first push ("Initial commit", 14:24) carried extracted/ and .vscode/; the next commit untracked them.
- `.gitignore`: the 349 MB lecture-photo PDF (GitHub refuses files > 100 MB), `extracted/` (regenerable; add
  `!extracted/lecture/` if the slide photos are needed on another machine), `.vscode/`, `__pycache__/`.
- A reverted/amended commit keeps its blobs alive through the reflog, `ORIG_HEAD` and `FETCH_HEAD`; to really free disk run
  `git reflog expire --expire=now --expire-unreachable=now --all && git prune --expire=now` (848 MB of orphans were cleared this way).
- Commit only when the user asks. **No Co-Authored-By / Claude attribution line in commit messages** (user's request 2026-10-20;
  the two local commits that had it were reworded before pushing).

## 3. How the books are assembled
- **Guide = two books** (`build_guide()`, split 2026-10-16; parts renamed ส่วนที่ and slides merged inline the same evening):
  *By_Unit* = `00_exam_info.md` (title swapped by `guide_cover()`) + `01_units/00_header.md` + for each unit 5–22:
  `01_units/unitNN.md` + `04_vocabulary/unitNN.md`.
  *By_Topic* = cover + `02_grammar/00_header.md` + `02_grammar/[0-9][0-9]_*.md` (00_ excluded — including it once printed the
  banner twice) + 03 + 03b + `# ส่วนที่ 4` (90_themes, 91_categories) + 05 + 06. `countdown()` fills the date placeholders.
  `UNITS = range(5, 38)` since 2026-10-26.
- **Review** (`build_review()`): `content/exercises/review/<name>_partN.md` are merged — all parts' questions, then all
  keys (each key gets the part's `##` title) → `output/3_Exam_Prep/KMU_Review_<Name>.pdf`.
- **Speaking** (`build_speaking()`): `content/speaking/<snake>.md` → `output/6_Speaking/KMU_Speaking_<Camel>.pdf`; relative
  `<img src>` is rewritten to an absolute path because the md is copied to output/_build/md/ first.
- Answer-key labels: `KEY_LABEL` accepts `**A.**`, `**14.**`, `**14–16.**`, `**ฟัง 4.**` (anything up to 16 chars ending
  in a dot); items are `1)`, `2)`, `1-a)`. Written that way by the review and listening transcriptions.
- **Workbook**: `EXERCISE_BOOKS` in build.py (workbook only). Each unit file is split at its
  answer-key heading; all questions go first, all keys after, in one PDF.
  `build_everyday_units()` renders each `everyday/unit*.md` as its own PDF (questions + that unit's key).
  `PREDICTION_KINDS` has three kinds (everyday · miniexam · midterm); the banner of `midterm` carries no {n}.
  `add_writing_space()` turns sentence blanks into full-width ruled lines (`.wl`/`.wl2`) and widens
  word blanks to 8 em — matching the printed workbook's spacing.
- Style lives in `CSS_STYLE` (make_pdf.py): banner h1, accent-bar h2, zebra tables, 12.5px/1.75.
- **Colours** are added inside `md_file_to_pdf()`: `kotag.colorize_markdown()` (auto tags) → `kotag.braces_to_html()`
  (`{c:…}` → `<span class="kc">`), CSS from `kotag.CSS_COLORS`, legend strip = `kotag.LEGEND_HTML` as a running element in
  `@top-center`. Headings, code, `[pronunciation]` brackets, HTML tags, table header rows and explanatory glosses
  (GLOSS_EXPLAIN / GLOSS_SKIP regexes) stay uncoloured. 2,312 Thai glosses in guide/review/listening/speaking were reviewed
  by 6 Sonnet agents on 2026-10-17 (one stalled at start and was relaunched; ~240–345k tokens each, 12–30 min) and the
  773 corrections (33%) were written back as explicit tags with `kotag.py merge` (ids = file:line:k, k = k-th auto-tagged
  gloss of that line; merge re-derives the numbering with `resolve_targets()` so partial merges stay consistent).
  Low-resolution page renders (≤120 dpi) make blue/purple Thai look black — check colours at ≥200 dpi before "fixing".
  `KOTAG_DUMP=1 python3 scripts/make_pdf.py x.md --pdf-dir DIR` also writes `x.pdf.html` (the exact HTML WeasyPrint got).

## 4. Unit → grammar map (Units 5–13)
| Unit | Topic | Grammar |
|---|---|---|
| 5과 | 어느 나라 사람입니까? | 입니다/입니까?, 은/는, jobs, countries |
| 6과 | 그것이 마키 씨 지갑입니까? | 이/가, 이것/그것/저것, classroom objects |
| 7과 | 제 사전이 아니에요 | 이에요/예요, 이/가 아니에요, 제/저의 |
| 8과 | 사무실이 몇 층에 있어요? | Sino-Korean numbers, 층/호/번, phone numbers, 에 있다/없다 |
| 9과 | 도서관은 학생회관 옆에 있어요 | position words 위/아래(밑)/앞/뒤/옆/안/밖, places |
| 10과 | 빵 한 개에 얼마예요? | native numbers, counters 개/명/마리/권/병/잔/장, 한/두/세/네/스무 |
| 11과 | 저는 지금 숙제를 해요 | -아/어/여요 conjugation, 을/를 |
| 12과 | 커피숍에서 아르바이트를 해요 | 안 negation (안 + V, N 안 하다), 에서 vs 에 |
| 13과 | 시장에서 과일하고 고기를 사요 | dates/weekdays, 에 for time (no 에 after 오늘/내일/어제/지금/매일/언제), 하고 |

Guide §13–15 add material the course materials never covered explicitly:
**띄어쓰기** (조사 and 이다 attach; 안 takes a space), forced collocations
(춤을 추다 / 사진을 찍다 / 돈을 찾다 — never 하다), 아니요 vs 아니에요, 뭐예요 vs 무엇이에요,
주다/받다/주세요, 주어 생략, and why several 이/가 may appear in one sentence.

## 5. make_pdf.py gotchas
- Extensions loaded: `tables, fenced_code, sane_lists, toc`. **No strikethrough** — `~~x~~`
  prints literally. Use `x ✗` instead. Check with `grep -c '~~' output/_build/md/*.md` after a build.
- Alert blocks (`> [!TIP]`) and `<details>` run their body through `github_compat()` before
  `render_md()`; without that, Markdown lists inside them collapse into one paragraph.
- Fonts load from `/usr/share/fonts/truetype/noto/` via `@font-face`. **Don't add
  'Noto Color Emoji' to the font stack** — fontconfig then switches Latin/digits to a TeX Live font.
- `h2` and `h1` both `page-break-before: always`; `h1:first-of-type` is exempt so the cover
  doesn't start with a blank page.
- Needs packages from `~/.local/lib/python3.12/site-packages` (path inserted in the script).
- `pdftotext` mangles Thai vowel marks when you verify output — the rendered PDF is fine.
- WeasyPrint 70 **ignores `<ol start="N">`**; `render_md()` rewrites it to `counter-reset: list-item N-1`
  (fixed 2026-10-07 — before that every list starting at 11/13/16 printed as 1/2/3).
- `add_writing_space()` blank regexes use `[ \t]*`, never `\s*`, after the blank: `\s*` swallowed the
  newline whenever a `→ (　　)` blank ended a line, gluing the next item (or a `##` heading) onto it.
- A `###` heading containing 쓰세요/바꾸세요 puts two ruled lines under every item — **unless it contains
  고르 or 단어**; since 2026-10-18 a `####` heading does the same only with an explicit sentence instruction (문장을 만드세요/쓰세요/
  바꾸세요/완성, 대화를 완성, 대답하세요, 바꾸세요) — a bare 쓰세요 in `####` draws nothing (unit17/18 predictions rely on that) (word-answer sections; 단어 exclusion added 2026-10-10, it had put sentence lines under
  one-word blanks in 14 sections).
- Consecutive `> ` dialogue lines merge into one paragraph — put a bare `>` line between them.
- In a 쓰세요/바꾸세요 section, an item line starting `N.` also gets two ruled lines. For one-word blanks
  inside a dialogue, write `나: 회사에서 2)(　　).` (number inside the line, blank line between lines)
  — see everyday/unit16.md test A. Don't change the rule itself: ~38 workbook sentence answers rely on it.
- `{c:…}` braces are reserved for colour tags in every content/*.md (single letter + colon). `{{today}}` placeholders are
  untouched because the tag regex needs exactly one letter before the colon.
- The Write tool turns a `\u3000` escape inside Python source into the literal U+3000 character (kotag.py KO_RUN has the
  literal ideographic space in its regex) — a patch script that searches for the escape text will not match.
- Korean used to wrap mid-word (빔입니/다): WeasyPrint 70 ignores `word-break: keep-all` (tested 2026-10-18). Since 2026-10-27
  `wrap_korean_words()` in make_pdf.py puts every space-delimited Hangul chunk in `<span class="kw">` with `white-space: nowrap` —
  words now break only at spaces (tested; nested kotag colour spans inside are fine). A chunk whose span tags are unbalanced (a kotag
  span containing a space) is left alone. Headings and raw-HTML lines are skipped. A single Korean run longer than a table cell will
  overflow instead of wrapping — keep cells to a few words.
- Book-style renderer rules (2026-10-27): callout labels are Thai (`> [!TIP]` → 💡 เคล็ดลับ …) and `> [!INTRO] title` / `> [!SUMMARY]`
  exist; the TOC lists h1–h2 only (toc_depth 1-2) and hides its first entry (the cover + "목차"); `### 08. …` headings that already start
  with a number get class `nonum` so the per-chapter counter does not print "8. 08."; a bold line used as a heading (`**📝 …**`) gets no
  spacing, no number and no running head — write `###`/`####` instead (book_style_check.py flags it); `tbody > tr:nth-child(-n+2)
  { break-after: avoid }` moves a table whose first 1–2 rows would be orphaned to the next page (tested: 3+ rows still split normally);
  `h1:first-of-type` is the cover only inside `.book`/`.cover` (a document without `[TOC]` keeps a plain first heading).
- **Thai never wrapped (found 2026-11-03, the user saw tables running off the right edge "in many files"):** this WeasyPrint/Pango has no
  Thai line breaking (measured: a 90 px box with a spaceless Thai phrase overflows, with or without colour spans; with U+200B between words it
  wraps). So a table column of Thai glosses had a min-width of the whole phrase and pushed the table past the margin (20+ pages: predictions
  26–28, the midterm prediction, both guides). `thai_break_opportunities()` in make_pdf.py now puts U+200B between Thai words (PyThaiNLP via
  kotag's tokenizer) and at colour-span boundaries, never before a following vowel/tone mark or after a leading vowel; text nodes only. Word
  blanks in tables of 6+ columns are 5 em instead of 8 (build.py add_writing_space; the 10과 number table overflowed). Overflow check =
  scratchpad overflow_scan.py (pdftotext -bbox, any word with xMax > 548 pt on A4; mind maps are posters, skip them) → 0 pages after the
  fix; guides 655 → 651 and 728 → 721 pp, no dotted circles (U+25CC) in any PDF.
- kiwipiepy 0.24 and pythainlp 5.4 live in `~/.local/lib/python3.12/site-packages` (pip --user, 2026-10-17); the first
  `kotag` call per process takes ~2 s to load Kiwi + the vocabulary user words. Known Kiwi traps handled in kotag.py:
  누가 = nougat (pre-analysed), 마셔요 = 말+셔요, 주무세요/계세요/드세요 (user stems 주무·계·드), 어제 → 어+제 (MAG user word),
  공부하 tagged XSA (noun set keeps 공부 blue), 을/를·이/가 standalone lists (direct rules, no Kiwi).

## 6. Status of the content
- **Units 14–22 (added 2026-10-07)** were written by Sonnet subagents from OCR + page images, to
  `content/specs/SPEC_14_22.md`. Provenance caveats, not yet verified against anything:
  - workbook 15–22 scans are *blank* pages → their keys were AI-solved until 2026-10-27, when a Sonnet agent checked every key of 5–22 and the
    5~21과 종합문제 against the publisher's printed key (key-01…06): ~70 items corrected in 16 files (full conjugated forms where the question
    prints the ending after the blank, the print's 〈예시 답안〉 instead of invented samples, 께/께서/주십니다 for parents and teachers in 20과,
    잡수세요/드세요 in 15과, objects added to the 19과 time sentences …); only unit14 carries real ⚠️ teacher marks. Two prints contradict the
    transcribed question: 6과 F.3 = 지갑입니다 (the question's picture was read as 필통; the user also wrote 필통) and 9과 C.4 = 텔레비전 뒤에
    (read as 위; the user wrote 위에) — the print was kept and the mismatch noted in the key. `unit21_review_5-21.md` has 42 items (scan numbers
    1–42), key self-solved; agent flagged Q29/Q36/Q39/Q40 as judgment calls.
  - guide vocab tables for 14–22 came from noisy OCR; Thai glosses unverified against the page images.
  - 18과 clock items C.2/C.5 and 22과 food pictures A.2/A.5 were read from small line art — check.
- **Textbook completeness audit (2026-10-27, all units 5–37):** the user found 22과 읽기 나 listing 2 of the book's 3 O/X items (missing since
  the original OCR-based transcription). 6 Sonnet agents (430–640k tokens, 10–44 min each) then opened the 300-dpi page images of every unit
  (대화 page, 읽기/듣기 exercise page, 활동/발음 page, grammar pages) and compared item by item: every 연습 item, 대화 확인 question + swap table,
  가 · 나 · 다 (underlined phrases) · 라 (summary frame) · 활동 prompt · 문화 page now appear with Korean as printed, Thai gloss and the appendix
  answer (sample answers are labelled "ตัวอย่างตอบ"). Findings: units 5–10 had 가/나 complete but no 다/라/활동/연습; 11–22 were missing items in
  every unit (nothing was "already complete"); 23–37 mostly complete, 활동 prompts and warm-up questions added; corrections: 8과 나 3 = ○ per
  the appendix, 12과/16과 듣기 keys DO exist in the appendix (the files had said no), 14과 나 2/4 and 34과 가 2·나 1–3 wording, 21과 가 2,
  젓가락 [젇까락] (23과 + topic 40), 칫솔 [친쏠/치쏠], 편의점 [펴늬점/펴니점], 33과 book typo 어미니 noted. Still unreadable from the scans:
  10과 연습 1 coffee/book counts, 9과 연습 3 pairings, 18과 clock 6 (2:50 or 2:55), 30과 map answers (guesses) — all flagged in the files;
  pages 285, 294, 296–297, 315, 323, 332, 359, 368 are BLANK pages in the printed book (user, 2026-10-27 — the "missing scan" notes in
  unit28/29/31/32/33 were rewritten accordingly), so books 1-2's scans are complete. Korean tokens in 01_units: 25k → 43k.
  **26과 completed the same afternoon** after the user re-scanned the unit (8 pp): one agent (460k tokens) verified pp.262–264, added p.265
  (연습 2 cue cards, 연습 3 기상 캐스터 chart + model text), p.266 (확인해 봅시다, swap + conjugation table), p.267 (활동 phone-frame game,
  4 steps), pp.268–269 (투이의 일기 header, warm-up, 가/나 with the 372쪽 keys ○ ○ ×, 다 underlines 끝나고 / 학생들과 같이 / 많겠지만,
  라 frame, closing 활동, 4 발음 items) and 25 vocabulary words; the Whisper transcriptions of 대화 26-1 / 읽기 26-2 matched the print
  word for word (one comma). Topics 41/42 got the real 보다 / -겠- sentences from those pages instead of the "pages missing" notes.
- **Units 23–37 (added 2026-10-26, book 1-2)** — 8 Sonnet agents from content/specs/SPEC_23_37.md (5 × unit chapter + vocab + mind map for 3 units
  each, 3 × grammar topics 36–64 with quickref snippets; 300–460k tokens each, 11–22 min) + 1 integration agent (all.md threads, ส่วนที่ 3 to 5–37,
  ส่วนที่ 5 sets N–T). Fable: SPEC, ส่วนที่ 0 (table 36–64, final-term plan, exam→reading map), quickref assembly, covers/headers, builds.
  Provenance caveats: everything is from the textbook page images only (no workbook/exercise scans for 23+); all 연습/활동 answers the book
  does not print are the agents' own and are labelled so; 읽기/듣기 keys come from the 22–37 appendix. Missing scans: 26과 had only pp.262–264 until
  2026-10-27 (대화 26-1 / 읽기 26-2 were first transcribed from the mp3s by Whisper, then corrected against the re-scanned pages the same day —
  see the 26과 note in the audit entry above); pages 285, 294, 296–297, 315, 323, 332, 359, 368 are blank in the printed book (user, 10/27), not missing;
  23/25/29/30/31/33/34/35 have no 듣기 in the appendix (scripts exist only for 24, 28, 32, 36). Book typos noted in the files: 33과 -(으)ㄹ box
  "verb ending with 있다/없다", 32과 box "Lesson 9" (= 29), 35과 읽기 key 배우 vs 영화감독, 30과/28과 appendix keys not matching the printed
  questions. Grammar the book has beyond the table was folded in as 📌 เสริม: 24과 -(으)세요 (ข้อ 39), 25과 ㄹ 탈락 (40), 28과 그래서/못 (48/46),
  34과 frequency adverbs 자주·가끔·거의·전혀 (58), 35과 N이/가 되다 (59/60), 36과 -아/어도 되다 (61/64), 37과 -(으)려고 (unit file เสริม).
  Agent-glossed words to double-check: 바뀌다, 길이 막히다, 보령, 스포츠 댄스, 하숙집, 포장하다, 돌아가시다, 호박 (zucchini), 게르, 앞머리; 25과 margin
  word 이상하다 is not in its reading; 23과 reading has 카페 where the centre's sheet lists 카레.
  **25과 teacher's slide 문법 1 (photo 2026-10-28):** the -지만 table has a 명사 row — 이지만 (both 받침) · past 이었지만 (받침 O) / 였지만
  (받침 X), annotated "17과 +". The book's 준비 1 box (p.250) is V/A only, but 연습 2-6 cues 저는 학생이다. Topic 40's table was
  mis-labelled "(เสริม)" and had no noun-past row → rewritten to mirror the slide (topic 40 + unit25 + quickref 40, 10/28).
  Same day the whiteboard gave ㄹ 탈락 as a 2-rule procedure (① ㄹ + (으) → drop 으 · ② ㄹ + ㄴ ㅂ ㅅ 받침ㄹ → drop the stem ㄹ; 만들러 ·
  만드네요 · 만드세요 · 만들 거예요) — the user asked for it "as numbered steps showing what merges/dissolves" → step tables added to
  topic 40 (full, 10 rows + TIP), unit25 (4 board rows) and quickref 40. Slide 문법 2 (252쪽): 받침 ㄹ + 으 ✗ for -(으)러/-(으)ㄹ 거예요/
  -(으)ㄹ까요?/-(으)세요 with 놀다 O/X (놀러 가요 O · 놀ㄹ 거예요 ✗ · 놀ㄹ까요 ✗ · 놀세요 ✗ → 노세요) and 살 + (스)ㅂ니다 → 삽니다 vs 읽습니다/봅니다
  (ㄹ-stem picks ㅂ니다 like a vowel stem) → O/X tables added to topic 40 + unit25, ✗ 놀세요 row in the pitfalls table. Its second half
  (받침 ㄹ + ㄴ/ㅂ/ㅅ/받침ㄹ → 놀다: 노네요 놉니다 노세요 놀 거예요 놀까요? vs 놀러 가요) → one-verb-all-endings strip table (5 verbs) in topic 40, 2 rows in unit25.
- **"สูตรและวิธีทำ" blocks (2026-10-28, 6 Sonnet agents from content/specs/SPEC_derivations.md, 245–265k tokens / 9–11 min each):** the user asked that every
  formula-type grammar point be explained "like the teacher, like showing the work in a math solution". 45 topics (all except 03 05 09 11 12 13 14 15 17 18 24
  27 29 31 35 41 45 52, which have no formula) now carry `#### สูตรและวิธีทำ: … (แบบกระดานครู)` as the last sub-section of 📌 รูปแบบและเงื่อนไข (rules table
  กฎ 1–5 → "ลำดับทำคือ ①②③" → step-column worked table, 8–24 rows, ✗ forms from §6b → `> [!TIP] วิธีจำสั้น ๆ`; many also a one-verb-all-endings strip and a
  ✗/✓ table) and the owning unit chapter carries `#### แสดงวิธีทำ: … (ย่อ · ตารางเต็มในไวยากรณ์ข้อ NN)` (4–8 rows) inside its 📝 section. Each block shows only the
  irregulars taught by that unit (ㅂ 23과 · ㄹ 25과 · ㄷ 31과 · 르 32과). Agents' own illustrative ✗ forms (읽아요, 쓰어요, 앉어서, 가실게요 …) are labelled as risky
  forms, not as the user's; Thai lead sentences are the agents' and not proofread beyond spot checks (06, 40). +2,633 lines over 82 files; both books rebuilt.
- **Workbook 23–37 + 22~37과 종합문제 (2026-10-27, 6 Sonnet agents, 340–460k tokens each)** → content/exercises/workbook/unit23…37.md +
  unit37_review_22-37.md, keys copied from the publisher's printed 워크북 정답 (source/workbook/KMU workbook key unit 05 - 37.pdf) — the first
  workbook keys in this repo that are not AI-solved. Scans: only 23과 carries the user's pencil (and a pink teacher highlight + signature on
  p.115 = homework checked); 24–37 are blank pages. Pencil ≠ key in 23과: 어렵니다 → 어렵습니다 (ㅂ받침 + 습니다; teacher highlighted 니다),
  중식집/중식당 → 중국집, 어려웠어요 → 쉬웠어요 (picture reading), 일본음식 spacing. Printed-key quirks the files note: the key prints the full form
  incl. the suffix printed after the blank (쉽지 않아요, 취소해야 해요 …); 〈예시 답안〉 items are labelled ตัวอย่างตอบ; 27과 E numbers 1) 2) 3) 4) 6);
  29과 key typo 외국이다; 31과 에서~까지 ex.1 numbered 6) for the 5th item; 33과 F.1 key has 일요일에 만날 한국 친구는; 34과 G sample switches
  speaker names; 종합문제 key heading says 22~41과; 종합문제 11 and 39 are ③ (my first reading of the key page had ② / ④ — the agent re-read it).
  Renderer lessons: a `---` directly under another `---` printed a heading "---" (11 pages of the old workbook book; build.py now collapses
  them); 가:/나: lines inside a list item need two trailing spaces or they merge; headings with 쓰세요 / 문장을 완성하세요 put ruled lines
  under example items too (left as is). The same agents' key-verification pass over 5–22 is recorded in the history entry below.
- **The workbook 5–13 has been fully proofread against the scans** (all 41 `extracted/workbook/unit05-13/wb-*.png` pages compared
  line by line, 2026-10-05). Two defects were found and fixed: 8과 A1 had the wrong number of
  blanks, and 13과 F had no answer key at all. Everything else matched.
- **The daily test and practice sheet 5–13 have also been fully proofread** (all 9 `test-*.png` and
  10 `sheet-*.png` in `extracted/everyday/unit05-13/`, 2026-10-05). `p2_sheet.md` matched everything. `p1_test.md` had three defects,
  all fixed:
  - 13과 C.17 asked for "ของหลายอย่าง" and answered `여러 물건`. Both were wrong: items 16 and 17
    are dictated from one sentence of the 13과 reading ("인사동에 **옛날 물건이** 많아요"), so the
    answer is **`옛날 물건`** (ของเก่า). `여러` appears nowhere in 13과.
  - 5과 A.1 was missing its ⚠️ (the teacher corrected `선셍님` → `선생님`).
  - 13과 B13 had Thai characters embedded in the Korean (`유월 유กิล이에요`).
- **`extracted/everyday/unit05-13/test-N.png` is not unit N.** The mapping is: test-1→9과, test-2→8과, test-3→11과, test-4→7과,
  test-5→6과, test-6→13과, test-7→12과, test-8→10과, test-9→5과. Check the page header
  (`1급 매일 시험_N과`) before comparing anything.
- The `⚠️` convention differs between files: in `p1_test.md` and `p3_workbook.md` it marks items the
  teacher marked wrong; in `p2_sheet.md` 13과 A it marks the tricky no-particle items instead.
- ⚠️ in an answer key = the teacher marked that item wrong on the scan. The set is good but not
  exhaustive — a few red marks carry no ⚠️.
- **Unit 14 test / unit 15 sheet (2026-10-07)** were transcribed by Fable directly from the scans
  (`extracted/everyday/unit14`, `unit15`), including the teacher's marks: test 14 scored 7.5/10
  (A1 blank, A5 blank, A6 피곤나요, C14 사라요); sheet 15 had one slip (사람 → 분).
- **Test 15 / sheet 16 (2026-10-10)**, same method. Test 15 = 8.5/10: dictation 8–10 each got △ (half);
  8/9 for letter shapes (ㅈ in 족 looks like ㅊ, ㅎ in 향), 10 wrote 맛이세요 — the dictation comes from the
  15과 reading ("할머니 요리가 정말 맛있어요"), so the answer is 맛있어요. Sheet 16 is the user's own pencil, NOT teacher-marked: its ⚠️ are
  Fable's corrections, and C (picture grid) answers marked (?) are guesses from small line art.
- `source/KMU_Speaking_Myself.md` (the user's own 자기 소개 draft) was moved to `content/speaking/myself.md`
  on 2026-10-12 so source/ holds only the teacher's PDFs. The user still edits it by hand; don't rewrite it.
- **Test 16 / sheet 17 (2026-10-12).** Test 16 = 10/10; item 1 the user wrote 합니까 where 하십니까 keeps the
  original's 시 — the teacher still gave the mark, the key gives 하십니까. Sheet 17 (-았/었/였-) is the
  user's own pen, every cell correct.
- **Test 17 / sheet 18 (2026-10-13).** Test 17 = 8/10; all four lost half-marks are spelling, not grammar:
  6) 젝을 for 책을 (ㅊ→ㅈ and ㅐ→ㅔ), 7) the ㅊ of 청소 (teacher re-wrote 청; also 청소 했어요 spaced),
  9) 생할 for 생활 (second sighting — it was already in §6b), 10) 열심이 for 열심히. The teacher's correction
  on item 10 is cut off at the bottom of the scan, so the dictated sentence is keyed as 열심히 공부합니다 with a
  note that 하겠습니다 is possible. Sheet 18 = time table p.1 (left blank by the user), 15 -(으)러 pictures
  p.2 (user's pencil, all correct, including 씻으러), 확장 연습 dialogue + 15 place pictures p.3 (no blanks on the
  sheet; unit18.md turns the places into a write-the-word exercise).
- **복습시험 ① (mini exam 1, sat 2026-10-06, scanned 10-13):** score sheet 말하기 10.0 · 쓰기 8.8 · 듣기 7.5 · 읽기 10.0.
  The scan = the question papers with the user's pencil and the teacher's red pen; the 읽기 and 말하기 answers are
  not in it. 쓰기 lost 12 = 학생식당하고 가요 (→ 에), 네 게 (→ 개), 십월 (→ 시월), 4 each. 듣기 lost 2.5 = room number
  203/204 (−1) and three of four floor O/X items (−1.5); the teacher also rewrote 안 아르바이트 해요 → 아르바이트 안 해요
  and added 생일 파티 to item 8 without a visible deduction. Item 10's blank carries only a Thai phonetic note
  ("청소해요"), so whether it scored is unknown. No listening script exists.
- **Workbook 18과 key corrected 2026-10-13** from the user's photos: C1 다섯 시 십오 분, C2 열한 시 오십오 분,
  C3 여섯 시 사십오 분 (hour hand between 6 and 7; still a small-picture reading), E4 장을 보러 / 과일을 사러.
- **Answer-key rendering (fixed 2026-10-07):** `one_answer_per_line()` must emit top-level `- ` bullets
  with a blank line before each `**A.**` block. Indented bullets became a `<pre>` code block (literal
  `**1)**` on the page) and a key written on consecutive `**A.**/**B.**` lines lazy-continued into one item.
- **Guide additions this round:** `02_grammar/02_ida-anida.md` got `### ⚠️ จุดสับสน: โครงสร้างประโยค 이에요/예요 vs 있어요
  — ต้องมี 이/가 ไหม?` (type table, three structures, look-alike pairs, 와/과 table with the 15과 workbook
  examples; PDF pp 42–43). Written 2026-10-07 after the user said this was their main confusion.
- **Test 18 / sheet 19 (2026-10-14).** Test 18 = 10/10, no corrections (A four digital clocks with 오전/오후, B 도서관·은행·커피숍에
  뭘 하러 가요?, C 몇 시예요 · 여덟 시 삼십 분 · 체육관에 가요). Sheet 19 = 거예요 form table p.1 (user's pencil; teacher highlighted
  살어요/살었어요 → 살아요/살았어요), 과거-현재-미래 picture table p.2 and 주말 계획 dialogue p.3 (both blank; unit19.md keys them).
- **Test 19 / sheet 20 (2026-10-16).** Test 19 = 8.5/10: A 부터~까지 from the 24-h clock (= 연습 1 p.171), B 뭐 할 거예요 dialogues,
  C dictation 운동할 거예요 · 몇 시부터 몇 시까지예요 · 한식집에 갈 거예요. Lost: B7 answered 언제 고향에 갈 거예요? with 가족을 만날 거예요
  (−1; the exact pair 언제…→방학에 갈 거예요 was printed in the prediction §3) and C9 몇 written with ㅈ twice (−0.5). The 19과
  prediction scored well: A/B content both predicted (as B), C 3/3 partial; scorecard at the top of predictions/everyday/unit19.md.
  Sheet 20 = 듣기 20-2 fill-in (8 blanks), user's pencil, not teacher-checked; unit20.md keys it (⚠️ 가르칠 거요, 고향 친구 without 한테서).
  No audio script exists — the dates 7월 25일~29일 are what the user heard (consistent with the textbook's 5일 O/X item).
- **Centre's vocabulary book (2026-10-16)** → `content/guide/04_vocabulary/unit05…22.md` + `90_themes.md`: the printed Korean
  is from the scan, the Thai/English glosses are Sonnet's (the user's own pencil glosses were ignored). Pages 18–35 (본문 듣기)
  → `content/exercises/listening/`: keys = textbook dialogue; pencil differed in 5과 B2/B4, 6과 B2, 7과 B2, 8과 B3, 10과 B2/B4,
  13과 B4, 15과 A4 (listed by the agent, not re-checked by Fable). 17–22과 sheets have ①–④ choice items instead of O/X.
- **Teacher's slides (2026-10-16)** → `content/guide/07_lecture/unit09…22.md` (12 files, no 17과 — its slides were filed under 16/18
  by content). Transcribed by Sonnet from phone photos; the handwritten Thai margin notes carry `(?)` where unreadable
  (pages 5, 7, 10, 11, 17, 18 of the scan were the hard ones). Not proofread against the photos by Fable.
- **중간시험 복습문제 (2026-10-16)** → `content/exercises/review/midterm01_part1.md` (쓰기 1–14 + 읽기 1–13) and `_part2.md`
  (읽기 14–25, 듣기 1–12 headed `ฟัง N`, 말하기 table 1–20). Paper is blank (no pencil). Key is Sonnet's; shaky items: 쓰기 7
  picture positions, 쓰기 3 items 2/4 (도/만), 읽기 5 (job not in passage), 읽기 22 ordering; 듣기 has no script so most of its
  key says "ต้องฟังเสียง". The 10-column number table (쓰기 5) uses `(　)` single-space blanks — `(　　)` overflowed the page.
- **Guide overhaul (2026-10-16 evening)** after the user found the old books incoherent (grammar table stopped at 13과, "ภาค 2" printed
  twice, stale ส่วนที่ 0, slides appended instead of merged): 8 Sonnet agents rewrote all 35 topic files and all 18 unit chapters to the
  templates in §2, checking Korean against the textbook page images / OCR; 03b was extended to 5–22; 06_quickref was assembled from
  their snippets. Corrections they made to earlier content (now in the files): 와/과 = 15과, 께서 first in 20과, 하고 = 13과,
  작년에/지난주에 take 에, 한국에서 왔어요 is fine, -(으)시- can honour the listener, 서점 앞에 (textbook) not 옆에 (slide),
  phone numbers read with 의, textbook calls -지 않다 colloquial like 안, "있다/없다 never with 은/는" was false. Items labelled
  "เสริม" are not in the textbook (ㄹ-drop before ㅂ니다, 생신/댁, 에서~까지). Known leftovers: review key midterm01 is AI-solved.
- **매일시험 score log** (teacher's red pen, all transcribed): 14과 7.5 · 15과 8.5 · 16과 10 · 17과 8 · 18과 10 · 19과 8.5 · 22과 8.5 (2026-10-26: A 4 × -(으)ㄹ까요? from
  picture+word-pair cues, B 3 × -고 answers, C 무슨 색깔을 좋아해요? · 정문 앞에서 만나요 · 친구가 멋있고 똑똑해요; lost 산책고 → 산책하고, 좋아 하고 → 좋고, 색아리 → 색깔을;
  the 22과 prediction matched A/B formats and C 3/3 partially — scorecard at the top of predictions/everyday/unit22.md). 23과 sheet (10/26, user's pencil): the ㅂ table
  and all 16 (으)ㄴ cells right except 메워요 for 매워요. **23과 test (10/27) = 4.5/10, the term's low:** A 4 picture dialogues answered with a ㅂ adjective
  (더려워요 → 더러워요 half · blank for 시끄러워요 · 귀워요 for 귀여워요 · 무서 워요 with a space, half), B 4 × adjective + (으)ㄴ (큰 ✓ 매운 ✓ · blank for
  어려운 · 영화은 for 재미있는), C only 2 dictation items (불고기가 안 매워요 ✓ · 친절한 사람은 → 사람을, half). The per-item split is inferred from the red
  pen (ticks = deducted, circles = given) and sums to 4.5. The user's own diagnosis: "I could not remember the words" — the sheet tables the day
  before were almost all right, so the failure is recall under exam conditions, not the rule. 24과 sheet (10/27, user's pencil): -(으)세요 / -지 마세요
  tables all 12 right (incl. 돕다 → 도우세요); the teacher's own restaurant dialogue (듣기 보충, 13 blanks) filled plausibly, no audio to check. **24과 test (10/28) = 8/10:** A 4 × situation sentence → -고 싶어요
  (보기 경치가 아름다워요. 사진을 찍고 싶어요 · 피곤해요. 집에서 자고 · 배가 고파요. 빨리 밥을 먹고 · 다리가 아파요. 의자에 앉고 · 예쁜 가방… 사고) — items 2–3 are
  workbook 24과 C2/C4 almost word for word and all four cues are in textbook 연습 2 p.243; B 4 × no-entry pictogram → -지 마세요 (보기 쓰레기를 버리지 ·
  사진을 찍지 · 전화를 하지 · 담배를 피우지 · 이야기하지 — 3 of the 4 signs are textbook 연습 2 p.245); C 2 bare phrases from 대화 24-1 (뭘 시킬까요 · 냉면 한 그릇).
  Lost: 만나고 for 앉고 (−1, word recall), 담배 피우지 without 를 (−0.5), 뭘 시킬까요 half (teacher gave no reason; the pencil spaces 시킬 까요). The 24과
  prediction's mock 2 (textbook-based) matched A's format and 3 of 4 items; its dictation list had both phrases but at ranks 5 and 9 inside long sentences —
  the user said "none matched", which is how it looked. Lesson used for 25과: rank 대화 lines first and list the short form. 25과 sheet (10/28, user's pencil):
  -지만 table 18/18 and ㄹ 탈락 table (-네요 · -ㅂ니다 · -(으)세요 · -(으)ㄹ 거예요 · -(으)러 가요 · -(으)ㄴ) 38/38 right; the 어때요 dialogue page has no answers. **25과 test (~10/29, scanned 10/30) = 9/10:** A 4 × pick a word from a 보기 box (재미있다 · 어렵다 · 깨끗하다 ·
  불친절하다) after -지만 (좁지만 깨끗해요 · 재미있지만 좀 어려워요 · 종업원이 불친절해요 · 무섭지만 재미있어요), B 4 × **the workbook 25과 F pictures, all of them**
  (보기 아기가 웁니다 · 집이 멉니다 · 창문을 여세요 · 케이크를 만드세요 · 바람이 많이 부네요 — endings mixed), C 맛있게 드셨어요 (rank 1 of the prediction's list) ·
  기숙사에 삽니다 (a grammar example, not a 대화 line). Lost only 요리하세요 for 만드세요 (−1: grammatical, but the test targets ㄹ 탈락 — pick the ㄹ verb).
  The 25과 prediction's mock 2 had the four B pictures exactly. 26과 sheet (~10/30, user's pencil on 문장 연습 2 only): 5 of 6 보다 sentences right, ★ item 2
  reversed the winner (압둘라 씨가 왕쯔이보다 시험을 잘 봤어요 — 왕쯔이 had 90점).  **26과 test (11/2) = 5.5/10:** A 4 × 보다 picture pairs (1 = workbook C1, 4 = the workbook C 보기 몽골이 한국보다 더 추워요 verbatim) — lost 3: two winners reversed (빵이 우유보다 싸요 · 윤아 집이 가오루 집보다) + the Mongolian flag read as 사우디아라비아; B 4 × -겠- = all four cue cards of textbook 연습 2 pp.264–265 — 패가 고파겠어요 (ㅂ→ㅍ, 고프 + 겠) and 덥겠어요 with 겠 drawn like 첬 got half; C 기온이 영하 40도예요 (대화 26-1) ✓ · 힘들러지만 for 힘들었지만 (읽기 26-2) half. The teacher marks ○ full · △ half · / zero. 27과 sheet (11/2, user's pencil, 4 pink highlights): -아/어지다 picture table 20/21 (아파요 → 아파졌어요; cell 20 = 생겼어요), school afternoon/night = textbook 연습 3 (책을 읽어졌어요 ✗), -는 table 22/24 (팔는 → 파는 · 정소 → 청소). 27과 prediction (Sonnet agent, 280k tokens / 12 min; mock 1 = workbook G/D/E, 2 = sheet, 3 = textbook 연습 + the teacher's slide sentences) + site v48 (114 sets · 2,166 items). **27과 test (11/3) = 7.5/10:** A 4 × -는 "who is who" pictures ([보기] 운동하는 사람이 윤아 씨입니다; same format as sheet 27 p.4 / workbook E) — all four half for 이/가 on the object (책이 읽는 · 주스가 마시는 · 음식이 먹는 · 한국어가 공부하는, copied from the 보기's 사람이); B 4 × -아/어지다 from the afternoon/night picture (textbook 연습 3 p.271 = sheet 27 p.2) 4/4 — the 27 prediction's mock 2 A had all four; C 자주 입는 옷이에요 ✓ (연습 1 p.272 example) · 유즘은 장마절입니다 for 요즘은 장마철입니다 (first line of 읽기 27-2) half. The teacher put the SECOND grammar point in A — the A/B order is not fixed. Sheet 28 (11/3, blank): 중에서 제일 class dialogue + -(으)ㄹ 수 있다/없다 12-cell table → exercises/everyday/unit28.md. 28과 prediction (Sonnet agent, 243k tokens / 9 min; 34 pp; the teacher's hint "28 · 22 · 26 words: colours, fruits, animals, weather, sports, 타다/치다" = the centre's picture-theme sheets 과일/색깔/동물/음식 (22과) · 계절/날씨 (26과) · 운동 (28과), 61 words → set 4 + predict-28-vocab 97 items incl. a 하다/타다/치다 drill; mock 1 = workbook C/F/G, 2 = sheet 28 + hint, 3 = textbook 연습 pp.278–281; set 2/3 ○× picture marks are the agent's choice; it read the guide chapter, not the scans) + site **v49** (122 sets · 2,332 items · 878 clips; daily-27-writing/-listening, sheet-28-writing; predict-27 lost its 🔮; sent data.js, clips.js, clips2.js, vocab.js). **28과 test (11/4) = 7/10:** A 4 picture rows → 저는 [category] 중에서 [item]을/를 제일 좋아해요 — exactly the teacher's hinted categories 동물 · 음식 · 과일 · 운동 (= mock 2 A + set 4); item 1 half (category word not recalled, 동물 pencilled in afterwards); B ○/× table 마키/지훈 × 자전거 · 운전 · 피아노 → 탈/칠/탈/할 수 있어요/없어요 — 6 할 for 피아노 (→ 칠) and 8 탈 for 운전 (→ 할) zero, although the paper itself printed 운전도 할 수 있어요 and 피아노를 칠 수 없어요; C 단풍이 아름다운 가을 (대화 28-1, rank 6 of the prediction list) half for the dropped 이 · 봄에 꽃구경을 해요 (듣기 28-2) ✓. Scorecard at the top of predictions/everyday/unit28.md. Sheet 29 (11/4, user's pencil, 5 pink marks on p.5): -(으)ㄴ picture table 23/23 (17 테니스를 친 on a golf picture — 친 fits both), two-sentence → -(으)ㄴ 9/9 except 만든 음식은 + printed 은, 보기 page mixing -는/-(으)ㄴ 6/7 (지금 배운 → 배우는), -아/어/여서 table 21/23 (도와 without 서 · 맛있서); pp.4/6/7 speaking (blank) → exercises/everyday/unit29.md. 29과 prediction (Sonnet agent, 285k tokens / 12 min; 27 pp; mock 1 = workbook F/D/C, 2 = sheet 29 E + C (A/B swapped on purpose, -는 vs -(으)ㄴ by time words), 3 = textbook 연습 + the teacher's slide ✗ list) + site **v50** (130 sets · 2,488 items · 900 clips; daily-28-writing/-listening, sheet-29-writing, predict-29-1/2/3-writing · -vocab 40 · -listening 20; predict-28 lost its 🔮; sent data.js, clips.js, clips2.js). Earlier tests
  5–13 DO carry a red score at the top of each scan (re-read 2026-10-27, CLAUDE.md said otherwise before): 5과 7.5 (the paper is titled 단어 시험) ·
  6과 7 · 7과 8 · 8과 9.5 · 9과 5 · 10과 8.5 · 11과 5.7 · 12과 6.2 · 13과 4. All 19 daily tests so far average 7.57/10 (25과 = 9); the ≤ 5 papers (9과, 13과,
  23과) are the vocabulary-heavy units (position words · dates/places · ㅂ adjectives) — recall of words, not grammar, is the chronic loss. All
  19 are in scores.json `daily`. The 11과 test key was wrong in two places and is fixed (scan re-read 10/27): A1 = 기다려요 (the teacher circled the
  student's answer; the old key said 만나요) and A14 = 가르쳐요 (a teaching scene; the student's 기다려요 was slashed — the old key had copied it).
- Known cosmetic gaps: 10과 A's third table row (30–10,000) is printed as given reference rather
  than as blanks; `왕쯔이` is transliterated `หวางจิ้ง` where `หวางจื่ออี` is closer.

## 6b. The user's recurring mistakes (from homework photos checked 2026-10-07 → 10-12)
Use these to pre-empt errors when checking new work or writing predictions. Each was seen at least once;
starred ones cost real marks.
- ★ **Handwritten ㅈ has an extra top stroke and reads as ㅊ** (저 → 처, 가족 → 가촉). The teacher circled
  it in the 쓰기(1) essay and gave half marks on test-15 dictation. 좋아요 also came out as 촣아요 in the
  speech draft. **It goes the other way too:** test 17 lost half marks on 책 → 젝 (plus ㅐ → ㅔ) and on the
  ㅊ of 청소 missing its top stroke. Three tests have now lost marks to ㅈ/ㅊ shapes.
- ★ **생활 → 생할** cost half a mark on test 17 (dictation 회사 생활) after appearing earlier in the speech draft.
- ★ **ㅐ/ㅔ**: 네 게 for 네 개 (mini exam 1, −4) and 젝 for 책 (test 17) — the same vowel slip, both cost marks.
- 십월 for 시월 (mini exam 1, −4): 6월 = 유월, 10월 = 시월.
- Destination needs 에: 학생식당하고 가요 (mini exam 1, −4) — reached for 하고 because it sat in the 보기.
- 안 + N하다: 안 아르바이트 해요 → 아르바이트 안 해요 (mini exam 1 듣기 9).
- Listening: heard 204호 as 203호 and missed three of four floor O/X statements — numbers and detail retention,
  not grammar. Suggest note-taking while the teacher reads.
- 열심히 → 열심이 (test 17 dictation) — the adverb ending 히.
- Time expressions (workbook 18과): dropped 분 (사십오 이에요 for 사십오 분이에요), 시/분 written without spaces
  (두시 이십분), and a 7:45 reading for a clock showing 6:45 (hour hand before the 7).
- -(으)러 answers without the object the 보기 shows: 사러 / 찍으러 for 과일을 사러 / 사진을 찍으러 (workbook 18과 2-4, 2-5).
- ★ Dropping **으** after a 받침 before 시: 받십니다 (×2: sheet 16 and the rebuilt sheet), 읽세요.
  Same slip with -(으)러: 씻러 for 씻으러 (workbook 18과 2-3, 2026-10-13), even though the -(으)러 table
  on the page before was all correct. It happens in free production, not in drill tables.
- 마시다 → 맙니다 (cut the stem) instead of 마십니다; 운동하다 copied from the row above (공부합니까).
- Noun past tense: 학생였어요 / 공원였어요 instead of 학생이었어요 / 공원이었어요 (knows 의사였어요).
- 어떻다: wrote 어떻었어요 for 어땠어요 even with 어땠어요 printed two lines below.
- 에 vs 에서: 백화점에 샀어요 (should be 갔어요, or 백화점에서 샀어요).
- Mixing 니다/니까 when converting a dialogue — reads the source line, not the punctuation of the target line.
- Time words: forgot 에 after 오전·일요일·아침 in the essay (teacher added it); **but 작년에 / 지난주에 /
  지난 주말에 are correct** (textbook p.152 작년에 이 책을 읽었어요) — only 어제·오늘·내일·지금·매일 take no 에.
- Spelling slips in own writing: 메일 for 매일, 막어요, 생할, 고등생, 여동새, 안녀하습니까, 된강찌개 for 된장찌개 and 친구에요 for
  친구예요 (review set 읽기 14/16, 2026-10-17, with the word printed in the passage above the answer).
- Vocabulary confusions seen: 조문합니다 (asked; probably meant 주문합니다), 어때요 vs 어떻게.
- ㅏ-stem + 어요: 살어요 / 살었어요 for 살아요 / 살았어요 (sheet 19, teacher highlighted) — the 아/어 choice slips on 살다.
  Same family: 받었어요 for 받았어요 (workbook 20과).
- ★ **Answers the wrong question word**: 언제 고향에 갈 거예요? → 가족을 만날 거예요 (test 19, −1). Also 몇 시 for 며칠 and
  한 월 for 한 달 (workbook 19과). Check 언제/며칠/몇 시/뭐 before answering a 거예요 item.
- ★ ㅈ/ㅊ again: 몇 written 몆 twice (test 19 C9, −0.5) — fifth test to lose marks on this shape.
- 거예요 spelling: 가르칠 거요 (sheet 20) — drops 예; also writes 갈거예요 / 청소할거예요 without the space (accepted, but wrong).
- 부터/까지: writes them detached (이십 일 부터) or leaves 까지 out; 한시부터 두시까지 with no space before 시 (accepted on test 19).
- **Direction of 한테/한테서** (workbook 20과, sheet 20): 부모님한테서 이야기를 했어요 (→ 한테), 고향 친구 … 들었어요 without 한테서,
  라디오한테서 / 사무실한테 for things and places (→ 에서 / 에), 한테 + 드리다 (→ 께 + 드리다). Guide topic 29 now has the
  verb-direction table; point there.
- Honorific slips: 빌렸십니다 (→ 빌리셨습니다 / 빌렸습니다 — mixed 셨 and 십니다).
- ★ **Position words — reversed reference point** (review set 쓰기 7, 2026-10-16): 소파가 테이블 앞 for 뒤 (described the table
  from the sofa), 신문이 텔레비전 아래 for 위, 우산이 소파 앞 for 옆. In "A가 B ___에 있어요" B is the landmark: say where A sits
  as seen from B. **Second sighting 2026-10-17** in the same set, 읽기 8: 우체국 옆에 서점이 있어요 marked O (text says 서점 앞에
  우체국이 있어요 → the bookstore is *behind* the post office → X); the user also asked why the second 우체국 (우체국 위층에) has no
  이/가. Guide topic 05 now has the sub-section "คำนามที่อยู่หน้า 위치 명사 ไม่มี 이/가 — จุดอ้างอิง" with the A/B roles and the flip table
  (앞↔뒤 · 위↔아래 · 안↔밖 · 옆=옆). Rest of 읽기 7–13 on that page was right (9–11 answered as fragments 한 개에 1000원 · 한 장 · 11,550원). 읽기 14–16 (13과 passage, same day): content right (저하고 친구예요 · 인사동에 가요 · 된장찌개를
  먹어요. 그리고 한국 차를 마셔요) but the spelling was not — Fable first passed it from the low-res photo and the user objected; zoomed crops
  (PIL rotate + crop at 2–3×, the only reliable way to read this handwriting) showed **저 하고** (space before the particle), **친구에요**
  (에요 after a vowel; 에/예 hard to tell), **된강찌개** (ㅈ written as ㄱ) and **자를** for 차를 (ㅈ/ㅊ, 6th sighting) — both 16 words were
  printed in the passage, so the advice given was "copy letter by letter from the text". The user also did not understand what 14
  ('㉠우리'는 누구예요? = who does the underlined 우리 refer to) and the two-part 16 were asking — explained in chat.
- ★ **좋아 안 해요** for 안 좋아해요 (review set 쓰기 9-3, 2026-10-16): split 좋아하다 like a N하다 verb (운동 안 해요 was right on
  the next line). 좋아하다 / 싫어하다 are single verbs — 안 goes in front. Guide topic 08 already has this ✗ line.
- Counter answers written as the counter alone (review set 쓰기 10: 권 · 마리 · 병 …) when 보기 shows 사탕 세 개 — the full
  noun + native number + counter is required (책 네 권).
- 열넷 명 for 열네 명 (review set 쓰기 11-6, 2026-10-16) — the 넷→네 short form before a counter, right after 쓰기 10.
- Register conversion that drops the tense: 숙제를 안 했어요 → 하지 않습니다 (review set 쓰기 13, → 안 했습니다). Change the ending only.
  Same page got 시월 and 유월 right (the mini-exam-1 십월 slip did not recur).
- Review set 쓰기 14 (2026-10-17): 한구가 아니에요 for 한국 사람이 아니에요 (answer must mirror the question's noun; 받침 ㄱ dropped),
  드시세요 (double honorific → 드세요), 지금 하고 있어요? answered 연구실에 숙제 했어요 (progressive question answered in the past,
  에 for an action place, 를 dropped), 경치에 구경할 거예요 (구경하다 takes 을/를). Correct: 무엇이에요, 돈이 있어요, 며칠, 토요일이에요, 재미있었어요.
- ★ **Reading-test instruction formats not understood** (review set 읽기 17–19, 2026-10-17, scored 1/3): in `(　)에 무엇이 맞아요?` the
  first bracket *is* the passage blank (수업이 (　)) — the user wrote 한국 into it and circled ② 재미있어요 (key ③ 없어요); they had
  pencilled 끝나요 into the passage blank, which is not among the options and clashes with 방학. Same format recurs in 읽기 21/23/25 and
  will be on the midterm: read the passage blank → test each option in it → write the number in the last bracket.
- **다니다 ≠ 가다**: marked 지훈 씨는 대학교에 다녀요 as X because the passage says 학교에 가지 않아요 (vacation). 다니다 = be enrolled /
  go regularly (대학생이에요 ⇒ 대학교에 다녀요 = O); 가다 = the act of going. Already uses 회사에 다녀요 / 법대에 다녀요 correctly in output.
- Mock 복습시험② 쓰기 (exam02 prediction, done 2026-10-18, ≈80/100 by Fable): A/B/D all right. ★ 읽어세요 in free answer E1 although the
  drill table C1 on the same page had 읽으세요 (fourth sighting of the dropped 으 — drills right, free production wrong). 만들습니다 /
  만들으세요 (→ 만듭니다 / 만드세요, ㄹ-drop) · 바빱니다 (→ 바쁩니다: ㅡ drops only before 아/어) · 7:30 answered 일곱 시에 (반 dropped) ·
  어디에 가요? answered 서점에 갈 거예요 (tense of the question not kept) · 북간산 갈 거예요 (북한산에) · 연수장 for 향수.
- Mock 듣기 page (2026-10-18, 6/10 before the near-miss rule): items 8–10 understood but typed 도교 (ㅋ→ㄱ), 회서 (ㅏ→ㅓ), 빠빴어요
  (ㅃ copied onto the first syllable). The page now gives half marks for answers within 2 jamo of the key and names the letter.
- 20과 prediction mock 1, B+C (2026-10-18, photo): 남차 for 남자 (ㅈ/ㅊ, 7th sighting) · 양말 드릴 거예요 without 을 · 이야기가 들었어요
  (듣다 takes 을/를) · 고향 아이한테 … 가르치겠어요 for 고향에서 아이들에게 … 가르칠 거예요 (에서 dropped, 겠 for 거예요) · 자주 for 많이 (the
  Thai prompt said บ่อย ๆ — fixed to มาเยอะ). Full mock pass later (sets 1–3): 시계가 받았어요 (2nd 가-for-를 on a 받다/듣다 object) ·
  교수님이 사무실한테 전화해요 (→ 사무실에, 께서 … 하세요) · 어디에 전화가 왔어요 (→ 에서) · 눈이 오네요 written 와네요 · 부테 for 부터 · 지훈 씨 without 는.
  Right: 친구한테 전화해요, 한테서 + 받았어요, 할아버지께 + 드릴, 여자 친구한테 선물을 줬어요.
- Practice-site 읽기 sentence answers (2026-10-18): 고양 친구 for 고향 친구 (ㅎ→ㅇ, 가 dropped) · 학교 근처가 한식집에 (stray 가 inside a noun
  phrase) · 몇 시에 일어났어요? → 10시 20분이었습니다 (answered with 이다 instead of the verb asked about) · 쇼핑 하러 갔어요 where the text
  said 윤아 씨를 만나러. Content of 7/8/12/14 was right — the site had only marked them ✕ because they did not match the model string.
- 복습시험② (2026-10-20, pencil on the paper, not yet marked): ★ **테국** for 태국 (ㅐ/ㅔ, in the very first answer) · **먹으세요** for 드세요 (special
  honorific missed in a drill, next to 계세요 in the 보기) · **사과과** for 사과와 (와 after a vowel) · **먹습니다** for 먹습니까? (question mark ignored
  when converting) · section 5 "answer with -네요 / -(으)시 / -(으)러" has no pencil on the question paper (the answers went on a separate answer sheet, user 10/21 — not a blank) ·
  6-5 무엇을 드시겠습니까? → 저는 ___ unsure (→ 비빔밥을 먹겠습니다). 듣기 5 changed O→X (지훈 그림을 좋아하지 않아요).
- 매일시험 22과 (2026-10-26, 8.5): **산책고 달립니다** for 산책하고 달려요 (dropped the 하 of a N하다 verb before -고, and answered a 해요 question in
  ㅂ니다) · ★ **좋아 하고 재미있어요** for 좋고 재미있어요 (reached for the verb 좋아하다 where the adjective 좋다 was needed — the mirror image of the
  earlier 좋아 안 해요) · dictation **색아리** for 색깔을 (ㄹ받침 + 을 heard as one syllable). Sheet 23과 the same day: **메워요** for 매워요 (ㅐ/ㅔ again,
  in the very first cell) — everything else on the ㅂ/(으)ㄴ sheet was right.
- ★ **23과 test (2026-10-27, 4.5/10 — the term's low):** 더려워요 (ㅓ→ㅕ) · 귀워요 for 귀여워요 · blanks for 시끄러워요 and 어려운 (word not recalled) ·
  무서 워요 for 무서웠어요 (question in the past, answer in the present + a space inside the word) · 영화은 for 재미있는 (noun + 은 where an adjective
  + 는 modifier was needed) · 친절안 (ㅎ drawn like ㅇ) · 사람은 → 사람을 (object of 좋아하다). The sheet tables the day before were all right:
  the loss is recall under test conditions. Workbook 23과 (teacher-checked): 어렵니다 → 어렵습니다, 중식집 → 중국집.
- 24과 prediction mock 1 (2026-10-28, photo, ≈9.5/10): all -고 싶어요 / -(으)세요 / -지 마세요 forms right — 앉으세요 · 닫으세요 (으 kept) ·
  도우세요 (ㅂ irregular) · 넣지 (ㅎ받침) · 매운 (ㅐ) · 산책하고 (하 kept). Only slip: **비빔밥은 고기를 넣지 마세요** for 비빔밥에 — 넣다 marks the
  container with 에 (where it goes in), 은/는 belongs on the thing left out (고기는).
- 매일시험 24과 (2026-10-28, 8/10): ★ **만나고 싶어요** for 의자에 앉고 싶어요 (knew the grammar, could not recall 앉다 = sit — vocabulary again) ·
  **담배 피우지 마세요** without 를 (−0.5) · dictation **시킬 까요** written with a space (half).
- Workbook 25과 (2026-10-28, photos, no teacher marks): A–C all right; ★ **만들아요** for 만들어요 (took ㅏ from 만, the first syllable — 힘들어요 in the
  same table was right) · ★ **머세요** in F5 where the printed ending was (스)ㅂ니다 → 멉니다 (carried (으)세요 over from F3–F4; also 멀다 is an adjective) ·
  **여쁘지만** for 예쁘지만 (ㅖ/ㅕ, the word was printed in the 보기 above) · 맑지만 춥지 않아요 (grammatical but both halves positive — -지만 needs a
  contrast) · G5 냉면을 잘 만듭니다 to 어머니께서 … 만드세요? (→ 만드십니다) · G4 어디에서 사십니까? left blank — did not recognise 사십니까 as 살다 +
  (으)시 + ㅂ니까 (explained in chat; answer = …에서 삽니다, no 시 for oneself). Pencil glosses: what looks like "Unkind" over 불편하다 (small photo, uncertain; 불편하다 =
  uncomfortable/inconvenient, unkind = 불친절하다 — the C page has "Unkind" over 불친절하다 correctly) and "Happy" over 재미있다 (= fun, not 행복하다).
- Workbook 26과 C/D 보다 (2026-10-30, photos): C1–2 and D1 right; ★ D2/D3 **국민식당이 분위기가 학생식당이 분위기보다** / **학생식당이 음식보다** —
  a stray 이 on the noun inside the 보다 phrase (→ 국민식당이 학생 식당보다 분위기가 더 좋아요, or 학생식당의 분위기보다). The user asked why 식당이 분위기가
  carries two 이/가 (whole + part, like 저는 키가 커요) and why 싸다/좋다/맛있다 take no 을/를 (adjectives have a subject, not an object) — explained in chat.
- 매일시험 25과 (9/10): ★ **요리하세요** for 케이크를 만드세요 — grammatical, but the paper tested ㄹ 탈락 (same picture as workbook F): in a unit's test, reach for the
  unit's target verb. Sheet 26 (~10/30): ★ **압둘라 씨가 왕쯔이보다 시험을 잘 봤어요** with 왕쯔이 90점 / 압둘라 70점 — reversed winner (the 보다 noun is the loser).
  본문 듣기 23–25 (pencil, checked 11/1): 매운 음식이에요 written into a blank followed by the printed 음식이에요 (copy only what the gap needs) · 냉면 먹고
  싶어요 without 을 · 우리 for 우리 집. Vocab-sheet pencil glosses (11/1): 만지다 = "to teach" (→ to touch), 스키장 = คนเล่นสกี (→ ลานสกี), 부터 = "first" (→ from).
- Workbook 27과 (2026-11-02, photos, no teacher marks): vocab / -는 table / -아/어지다 table and G all right (ㄹ 탈락 사는·만드는·여는, 듣는 kept). ★ **자가 / 자는 for 차가 / 차는** in H (차를 right one line above — ㅈ/ㅊ, 8th sighting) · **음식를** (E2, → 음식을) · **음료수이에요** (→ 음료수예요) · E answers broader than the picture (음식을 먹는 for 빵을, 책을 읽는 for 공부하는) · H 따뜻해졌어요 + "drunk in winter" (contradiction) · spacing 추워 졌어요 / 쉬워 졌어요 / 길어 졌어요 (-아/어지다 is one word) · ㅈ of 졌 in 쉬워졌어요 drawn with a crossbar (reads ㅊ) · ㅎ of 하 in 좋아하는 floats (reads 아). Asked in chat: 있어졌어요 ✗ → 생기다 (33과), 돼요 vs -아/어지다, 잘 vs 좋아요, ช่วย = 돕다 vs -아/어 주세요.
- ★ **매일시험 27과 (2026-11-03, 7.5):** **책이 읽는 · 주스가 마시는 · 음식이 먹는 · 한국어가 공부하는** — 이/가 on the object inside a -는 clause in all four items (−2; the 보기 ended 사람이 and the 이 was copied forward). The object keeps 을/를 inside -는 / -(으)ㄹ 수 있다 phrases (책을 읽는 사람 · 자전거를 탈 수 있어요). Same family as 음식를 / 시계가 받았어요. Dictation **유즘은 장마절입니다** for 요즘은 장마철입니다 (ㅛ → ㅠ, and ㅈ/ㅊ for the 9th time).
- ★ **매일시험 28과 (2026-11-04, 7):** 피아노를 **할** 수 없어요 (→ 칠) · 운전을 **탈** 수 있어요 (→ 할) — the verb for each noun was printed two lines away in the same paragraph; read the given sentences before choosing 하다/타다/치다 · could not recall **동물** as the category word · 단풍 아름다운 (→ 단풍이). Workbook 29과 (photos 11/4): ★ **맛있서 · 재미없서** (dropped 어 before 서; again 맛있서 on sheet 29 p.5) · **여뻐서** for 예뻐서 (ㅖ/ㅕ, 2nd time after 여쁘지만) · ㅍ곤해서 (ㅣ of 피 missing) · F 공원이 for 공원에 and 좀 dropped (copy the second sentence's particles) · 가르친/가르쳐서 written so 가 reads 기 · sheet 29 C 지금 배운 → 배우는 (지금 = -는). Right: ㅂ (더워서 · 추워서 · 도운 · 가까워서), ㅡ (아파서 · 배가 고파서), ㄹ (만든 · 산 · 연 · 논), 이어서/여서 (학생이어서 · 의사여서 · 아홉 시여서).
What the user does well: ㅂ니다/습니다 choice by 받침, -지 않- forms, 겠 forms, the ㅡ-drop past
(바빴어요·컸어요), special honorific words (드세요·주무세요·계세요), 에서 for activity places.

## 6c. Presentations and writing tasks
- 발표 ① 제 방 소개 — done, script in `content/speaking/my_room.md` → `output/6_Speaking/KMU_Speaking_MyRoom.pdf`.
- 발표 방학 계획 — **Tue 2026-10-20**, from the teacher's slide (-(으)ㄹ 거예요 + 부터~까지 + 4 questions). Script
  `content/speaking/vacation_plan.md` → `output/6_Speaking/KMU_Speaking_VacationPlan.pdf`; dates = **2027-02-15 → 03-15** (user's real plan,
  Thailand, family). Illustration `content/speaking/vacation_plan.png` = an AI image the user generated elsewhere (1024×576) and
  dropped in on 2026-10-16; a PIL-drawn fallback of the same content was made first and discarded (Fable cannot generate images).
- 발표 ② 자기 소개 — **Wed 2026-10-21** (the day before the 말하기 midterm). Draft = `content/speaking/myself.md`;
  **family section removed 2026-10-16** — the teacher said a self-introduction should not talk about family; replaced by
  취미/주말 (운동 · 한국 음식 · 명동 · 경복궁) and 계획 (열심히 공부 · 이월 태국 → 삼월 한국) sentences, 15 lines as before;
  **vacation_plan.md changed back 2026-10-19**: the teacher told the user not every sentence has to be formal → only the greeting/intro
  (1, 3) and the closing (11) stay 합니다체, the plan sentences use -(으)ㄹ 거예요 / 좋아해요. myself.md stays fully 합니다체 (the user
  briefly asked to convert it too, then took it back the same hour). Note for myself.md:
  **both speeches are in 합니다체 since 2026-10-16 night** (the user asked "이에요 → 입니다 ให้หมด"): 공부합니다 · 왔습니다 ·
  공부하겠습니다 · and -(으)ㄹ 거예요 → **-(으)ㄹ 것입니다** [거심니다] (the vacation slide's target form written formally; the
  PDF says to swap back to 거예요 if the teacher insists). Closing line 이상입니다. 감사합니다;
  Fable's corrected version was given in chat on 2026-10-10 (16 fixes: 안녕하십니까, 매일, 먹어요, 좋아해요,
  한국 생활, 고등학생, 여동생은, 가족은, 다섯 명, 법대에 다녀요, + 감사합니다). The user pasted it into the file
  themselves. 기말 발표 2026-11-24, topic announced 11/10.
- 쓰기(1) essay (200-cell manuscript paper, 2026-10-10): teacher's fixes were 에 after time words, 한국어
  spelling, cutting a repeated 국민대학교, 오늘 날씨 → 한국 날씨, and she added 한국 생활이 재미있어요 as a closer.
  쓰기② (일기, diary) is due in class 2026-10-13 — workbook 17과 ex.5 is the same task; a model diary was
  given in chat.

## 7. Environment notes
- OS: Linux. `setlocale: LC_ALL` warnings are harmless.
- `.vscode/` once held a 2.6 GB C++ IntelliSense database; it is gone (8 KB now). If `browse.vc.db*`
  reappears, delete it and add a `.vscode/settings.json` C_Cpp exclusion.
- Checking the user's homework means reading handwritten Korean off a photo. There is no OCR help
  available for this — read the image directly and **say so when the handwriting is ambiguous**
  rather than asserting what it says. See §8.

## 8. Plugins — the user only wants free, local ones
**`pdf-viewer` is the only plugin enabled for this project.** It runs locally
(`npx @modelcontextprotocol/server-pdf`), costs nothing and needs no login. Use its skills
(`pdf-viewer:open`, `:annotate`, `:fill-form`, `:view-pdf`) when the user wants to look at or mark
up a PDF together.

**Disabled on the user's instruction (2026-10-05):**
- Paid services: `handwritingocr`, `extend`, `pdfbolt`, `pandadoc`
- Unrelated to this project: `data`, `engineering`, `presenton`, `read-paper`,
  `the-stoic-library`, `skill-creator`

Each was disabled twice — once as the locally installed copy and once as the `@synced` copy from
claude.ai. Disabling only the local copy makes the `@synced` copy load in its place, so **both must
be disabled** (`claude plugin disable <name>` then `claude plugin disable <name>@synced`); verify
with `claude mcp list` that no paid server is left connected.

Still enabled besides `pdf-viewer`: `document-skills` and `diagram-design`, both pre-existing and
free. A plugin's **skill descriptions load into every session whether or not its MCP server is
authenticated** — only the tool schemas wait for auth. The six unrelated plugins cost ~2,950
always-on tokens between them, which is negligible against the context budget; the real reason to
keep them off is that broad skill descriptions (e.g. `engineering:documentation`) can misfire on
this project's document work.

Do not re-enable these or suggest installing them again unless the user asks. In particular,
HandwritingOCR would read the homework scans more reliably than reading them by eye, but it uploads
the images to a third party and bills per page — the user considered that and declined.

## 9. History
Built across two agent sessions: an Antigravity session (2026-10-02 → 10-05) that did the
extraction and wrote the first drafts, and a Claude Code session (2026-10-05) that proofread the
workbook, added guide §13–15, split the exercises into question/answer books, and reorganised the
folder into the layout in §2.
Third session (Claude Code, 2026-10-07 → 10-13, Fable 5.1): added the 이에요/있어요 confusion section to the
guide; transcribed tests 14–16 and sheets 15–17 from scans; split the everyday book into per-unit PDFs and
later deleted the combined book on request; renamed every folder level to textbook/workbook/everyday/
syllabus; fixed three latent renderer bugs (newline-swallowing blanks, `<ol start>`, answer keys rendered
as `<pre>`) and the 단어-section ruled-line bug; added `content/predictions/` + `build.py predict` and wrote
the 17과 prediction (3 mock tests); moved the user's speech draft out of source/. In between, most turns
were homework checks from photos (workbook 16–17, sheet 16, essay, speech draft) — findings in §6b.
2026-10-13 (same session, after compaction): checked workbook 18과 ex.1–3 and the -(으)러 table from photos,
translated the 19과 vocab page, transcribed test 17 (8/10) and sheet 18, scored the 17과 prediction against the
real test (format, A3–4 and C8 exact), corrected the workbook 18과 key from the photos, and wrote the 18과
prediction (time + -(으)러; 3 mock tests). Later the same evening: the user dropped the 복습시험 ① scan; it was moved
to source/miniexam/ under the naming scheme, transcribed (exam01.md), and a 복습시험 ② prediction was written
(exam02.md with 쓰기 100, 듣기, 읽기 and 말하기 mocks plus the 19과 낭독 texts); build.py gained the `miniexam`
target and predictions were split into everyday/ and miniexam/ sub-folders at content, output/md and output level.
2026-10-14: back-checked the prediction statistics the user asked about — dictation sources for 6–13과 against the
textbook (grep on extracted/textbook/*.txt, four page images) and the sheet→B pairing for 8–13과; results recorded
in §2 step 5 and in predictions/everyday/unit18.md §1.3–1.4. No multi-agent run: the job was a handful of greps and
four images, so agents would have cost more tokens, not fewer. Afternoon: test 18 (10/10) and sheet 19 arrived; transcribed,
18과 prediction scored (mock 1 nearly matched the paper), 19과 prediction written from the teacher's hint (부터~까지 + 거예요;
3 mocks), everyday + predict rebuilt.
2026-10-16 (Fable 5.1 + 7 Sonnet subagents in parallel, on the user's instruction "Fable plans, cheaper models transcribe, save
tokens"): five new scans arrived (test 19, sheet 20, the teacher's 중간시험 복습문제, the centre's vocabulary book, photos of the
teacher's slides). Fable filed them under source/{everyday,review,vocabulary,lecture}/ per §2.1, extracted the pages, transcribed
test 19 + sheet 20 and scored the 19과 prediction; Sonnet agents transcribed the review set (2 agents), the vocab lists (2), the
picture themes (1), the 본문 듣기 sheets (1) and the slides (1) — agent costs 62k–145k tokens each. build.py gained the two-book guide
split, `review`, `speaking` and the `KMU_Listening` book; the single Master Guide was removed. Speaking scripts for 10/20 (방학 계획,
from the teacher's slide: -(으)ㄹ 거예요 + 부터~까지 + the four questions) and 10/21 (자기 소개, user's draft kept intact + 4 🆕
sentences) were written and built. §6b gained the week's workbook 19–20과 and test 19 mistakes.
Evening: the user rejected a Graphviz card poster ("not a mind map, ชุ่ยมาก") and asked for real mind maps in the
diagram-design plugin's style — one per unit + one combined, showing how units connect with conditions and methods.
Built scripts/build_mindmaps.py (bilateral map, elbow connectors, print labels as HTML divs over SVG because WeasyPrint's
SVG text breaks Thai marks), wrote content/mindmaps/all.md (7 cross-unit threads) and unit19.md as the exemplar, then
4 Sonnet agents wrote units 5–18/20–22 (≈350–440k tokens each — they read every source file per unit). Agent corrections
taken: 와/과 is 15과 not 16과; 께서 first appears in 20과 not 15과; 사이 is not in 9과. Output: output/mindmaps/*.{html,pdf,png}
+ output/KMU_Mindmaps.pdf (19 pages, one map per page).
Later that evening: the user rejected the two guide books as incoherent → full rewrite (see §6 "Guide overhaul"): build.py guide
assembly fixed (duplicate banner, ส่วนที่ names, build-time countdowns, slides no longer appended), ส่วนที่ 0 rewritten with the
complete 5–22 grammar table and the week plan, 8 agents rewrote 02_grammar + 01_units + 03b, 06_quickref assembled. While reading
the 19과 slide photo the teacher's whiteboard schedule turned up: **복습시험② is Tue 10/20** (not 10/19), Mon 10/19 = 21·22과,
중간시험 = 1~21과 — dates corrected in ส่วนที่ 0, CLAUDE.md §1, exam02 prediction, mind maps, syllabus_th.
2026-10-17: homework checks of the review set pp.2–5 (§6b gained 좋아 안 해요, 열넷 명, reversed position words, tense-dropping
register conversion); ส่วนที่ 3 gained §3.3 "รูปแบบคำตอบครบทุกคำถาม" (5 rules · yes/no answers by question ending with example
questions · every 의문사 answer template · checklist). Then the user asked for **colour by word function in every PDF** (Korean
segment and its Thai translation in the same colour, instead of bold only): built scripts/kotag.py (Kiwi + PyThaiNLP, the user
pointed at PyThaiNLP), wired it into make_pdf.py (running legend) and build_mindmaps.py (coloured tspans/spans + colour legend
row), wrote the legend page in ส่วนที่ 0 and content/specs/SPEC_colors.md, and had 6 Sonnet agents review the 2,312 auto-tagged
Thai glosses (output = only corrected lines; merged with `kotag.py merge`). All eight PDFs the user listed were rebuilt.
2026-10-18 (after midnight): the user asked for a **중간시험 prediction**. Fable wrote the blueprint (SPEC_predict_midterm.md), the analysis
part (evidence = the teacher's 복습문제 + 복습시험 ①; grammar ranked by how often she has tested it; the user's own loss list; a 6-day plan)
and registered the `midterm` prediction kind; 4 Sonnet agents wrote the mock papers in parallel (쓰기 2 papers 496k tokens · 읽기 473k ·
듣기 395k · 말하기 315k; 20–35 min each): output/predictions/midterm/KMU_Predict_midterm01.pdf, 44 pp. Agent findings taken: only
17과 of the unused units has a printed 읽기 (8/12/16/20 have 대화+듣기); `add_writing_space` ignored `####` headings (now explicit-marker
rule); `→ (　　)` chains render as stacked ruled lines (review item 22 rewritten with `( 　 )`); WeasyPrint ignores `word-break: keep-all`.
Earlier that evening: homework checks of the review set 읽기 7–25 (§6b: reversed landmark again, 다니다, question formats, 된강찌개/자를
spelling read only after zooming the photo), guide topic 05 gained the landmark sub-section and topic 03 the 여기/거기/저기 table, and
three kotag fixes (bold 안+에 = noun, bare 해요 = verb, no duplicate Korean after a consumed table gloss).
2026-10-18 (evening): mock-exam website. First a single-set page for the 복습시험② prediction (browser TTS + Web Speech mic), then —
because Chrome on Ubuntu has no Korean voice — neural clips from edge-tts, then on request **one site for every exercise needed for
복습시험② and the 중간시험**: SPEC_mockweb.md + mockweb_validate.py, 6 Sonnet agents converted the sources to content/mockweb/*.json
(85–117k tokens each, 1–3 min), Fable wrote scripts/mockweb/app.html + build_mockweb.py → output/2_Practice_Web/ (16 sets, 472 items,
252 clips). Spelling near-misses (≤2 jamo) score half and name the letter (the user's 도교/회서/빠빴어요 slips). Same evening the user said
the workspace had become confusing → output/ reorganised by purpose (1_Guides … 6_Speaking, _build), START_HERE.html + README.md,
build.py/build_mindmaps.py paths updated, superseded scripts moved to scripts/_archive/.
2026-10-19 (Fable 5.1 → Opus 5.5 → Fable; the user watches their token quota closely — **save tokens, no multi-agent audits**): 20과 daily-test
prediction (Sonnet agent from the unit19 template; Fable fixed section C to Thai prompts and glossed every Korean line) + photo checks of
the user's mock answers (§6b). vacation_plan.md register changed to 해요체 except greeting/closing after the teacher said so (myself.md stays
formal; 뭐 → 무엇을 on request). Practice site rebuilt as a real mock exam (§2 2_Practice_Web, v13–v24): the user's complaints were "15 min
became 15 s" (the per-section answer countdown overwrote the exam clock — reproduced with the fake-Audio harness, root cause), "what is the
difference between จับเวลา and จำลองห้องสอบ" (→ one cover page with เริ่มสอบจริง / ฝึกทำ), whole-item colours instead of ○△✕, pause must
freeze the clock (attempt.left, synced), progress sync across devices (cloud module syncs ans/self/ai/score/hist/attempt, home+cover pull
every 20 s), big sticky progress bar (page scrolls inside #scroller because iPad Safari grows the claude.ai iframe), split left/right layout
option, text-size option, conjugation rows as a grid, tip vs correction colours, karaoke word highlight + transport bar. AI grades every typed
answer on submit. A started Workflow audit (5 lenses + refuters) was cancelled on the user's request mid-run — do not relaunch. 복습시험②
papers 2 and 3 (mini02_b/c.json, 2 Sonnet agents from content/specs/BRIEF_mini02_extra.md; Fable swapped a 학생일 거예요 item for 바쁘다 and
de-duplicated the conjugation/word-order items between the papers) → the home board groups 복습시험② by paper (ชุดที่ 1–3, 4 skills each).
The user scored 100/100 쓰기, 10/10 읽기, 9/10 듣기 on paper 1 before the exam. Framework question: the user wants a "better frontend"
later — Fable recommended Preact + Signals (no build step, works as a single-file artifact) or React+Vite+shadcn with own hosting; the user
chose **A = wait until after the midterm (after 2026-10-23)**, then decide. Pending ideas offered but not built: export/import of progress,
HTTPS hosting for the iPad microphone, loading clips per set instead of one 6 MB file.
2026-10-20 (afternoon/evening, Fable 5.1 + Sonnet agents): folder renamed KMU_Korean and put under git (§2.2). The practice site was ported to
**Preact + Signals** (v25, one Sonnet agent from content/specs/BRIEF_preact_port.md, 245k tokens; harness drivers all matched v24). A speech
audio player for the 자기 소개 발표 was built (scripts/build_speech_audio.py → output/6_Speaking/KMU_Speaking_Myself_Audio.html, artifact
https://claude.ai/artifact/UB8eXhn7DoTV6pVQDVMPSC; theme / reading / text-size controls added on request). The 복습시험② scan arrived (§1, §6b):
Fable read it, scored the prediction (format ~50 % for 쓰기, content ~85 %; 듣기/읽기 matched), and wrote content/specs/BRIEF_midterm_v2.md; four
Sonnet agents (125–160k tokens, 3–7 min each) transcribed the real paper (exercises/miniexam/exam02.md + mockweb/mini02_real.json → past/KMU_MiniExam_02.pdf)
and rewrote the midterm mock as **v2** (parts 02–05 + mockweb mid_*.json: every section mirrors 복습시험①/② or the review set with changed words;
쓰기 2 papers, 읽기 25+15, 듣기 29+10 with scripts, 말하기 25 questions with 해요/합니다 answers). scripts/assemble_midterm.py now lives in the repo.
Site v26/v27 (26 sets · 601 items · 311 clips) published; the real paper shows as its own row "ข้อสอบจริง". Marks for ② are due 10/21.
2026-10-26 (Fable 5.1 + 9 Sonnet agents, ~3.3M agent tokens): the user dropped the book 1-2 scans (23–37과, appendix 22–37, contents) →
filed, OCR'd (extracted/textbook/unit23…37), then **both guide books, the vocab sheets and the mind maps were extended to 37과** (§6 "Units 23–37"):
SPEC_23_37.md fixes grammar numbering 36–64; ส่วนที่ 0 gained the 23–37 table, the final-term plan and the exam→reading map; ส่วนที่ 3/5/6 and
all.md extended; UNITS = range(5, 38); covers/headers/START_HERE say 5–37. Earlier that day: 매일시험 22과 prediction (Sonnet agent, no 22과
practice sheet on file), the vocab-mistakes practice set (v40), AI grader switched to Opus high (v38) with a re-grade button (v39), dialogue
prompts split per speaker (v35), three-row answer key under each item (v36), self-contradicting AI verdicts auto-corrected (v37).
2026-10-27 (Fable 5.1 + 15 Sonnet agents, ~6.2M agent tokens, 22–36 min each): the user rejected the two guides as crammed notes
("อัด ๆ ยัด ๆ", examples chained with `·` in one paragraph, bold lines as headings, no introductions, Korean words split across lines) and
asked for a real book — and chose the fonts from a five-sample sheet (TH Sarabun for Thai/Latin, serif Korean). Fable rewrote
scripts/make_pdf.py as a book stylesheet (§2 scripts, §5 gotchas), wrote content/specs/SPEC_book_style.md + scripts/book_style_check.py,
rewrote 01_units/unit23.md and 02_grammar/37_b-irregular.md by hand as the exemplars, the two part headers and the "วิธีอ่าน" section of
ส่วนที่ 0; 15 agents then reflowed every other file (units 5–22/24–37 · grammar 01–36/38–64 · ส่วนที่ 2, 3, 5, 6) to the spec — no
sources re-read, Korean-token count per file 107–147 % of the committed version (table headers and added glosses; nothing dropped per
the agents' own diffs). Fable fixes afterwards: unit22 🧪 now carries the real 매일시험 22과 facts, unit34's -(으)러 link 26과 → 18과,
90_themes.md bold lines → `####`, ส่วนที่ 4 intro boxes, `nonum` for pre-numbered quickref headings. Every PDF was rebuilt (39 files):
KMU_Guide_By_Unit 521 pp (was 200), KMU_Guide_By_Topic 692 pp (was 357); the other books only changed fonts/spacing. Morning of 10/27 the
user spotted literal `<span class="kw">…</span>` text in book 2 (Korean inside `code spans` had been wrapped) and asked for one font step
down → wrap_korean_words() now skips code spans, BASE_PX 15.5 → 14.5 (headings/margins one step too), scripts/pdf_artifact_scan.py was
written and run over all 39 PDFs (it also caught a #### glued to a table row in unit22, 4-space-indented ①②③④ option lines in the
midterm prediction, nested italics in everyday/unit23.md and quoted calendar tables in workbook 13과/19과 — all fixed at the source or in
github_compat); final counts 488 / 642 pp, scan clean on every PDF. Then the user spotted that 22과 읽기 나 had 2 of the book's 3 O/X items → the
textbook completeness audit of all 33 units (§6, 6 Sonnet agents, ~3.3M tokens): book 1 grew to 605 pp. Not committed — the user did not
ask. Open: agents' Thai lead sentences/glosses were not proofread by Fable beyond sample pages; the sample answers they wrote for
unanswered 연습/활동 items are labelled ตัวอย่างตอบ but unchecked.
2026-10-27 (evening, Fable 5.1 + 11 Sonnet agents, ~4.6M agent tokens, 15–39 min each): the user dropped 20 files (workbook 23–37, the printed workbook key,
the 22~37과 종합문제, test 23과, sheet 24과, the 중간시험 score slip) → filed per §2.1 (new source/midterm/), rendered; Fable transcribed test 23 (4.5/10, with
the red pen) and sheet 24, put the midterm marks + every daily score into scores.json, wrote four briefs (BRIEF_workbook_23_37, BRIEF_daily_sets,
BRIEF_predict24, BRIEF_vocab_drill) and build_mockweb.py's vocab.js/clips3.js. Agents: workbook 23–37 (5) + 종합문제 (1) with the printed keys;
every daily test/sheet 5–24 as site sets (2); the 24과 prediction + 23과 scorecard + its site sets (1); site v41 vocabulary drill (1). The
key-verification agent for 5–22 stalled on the first launch (no file touched in 84 min; stopped) and succeeded on a retry (22 min, 410k tokens, ~70 key
corrections, see §6) — note that an agent's task output file is not a live transcript, so judge a stalled agent by `git status`, not by that file's mtime. Builds: KMU_Workbook 261 pp (was ~150), everyday 23/24,
predictions 23/24, site published as version 41 (87 sets · 1,733 items). The user's 4.5 on 23과 and "I cannot remember the words" set the day's priority: a
daily all-words drill. Not committed — the user did not ask.
2026-10-21: 복습시험② marks arrived (쓰기 7.5 · 듣기 8.5 · 읽기 9.0 · 말하기 10; grading system explained, §1). The teacher's hints for the 말하기 midterm (25 Q /
15 min from the 말하기 table + the 19과 sheet + self-intro + family) and three new sources arrived: the publisher's textbook audio, her own 듣기 audio for the
복습문제, and the book's 부록 (filed under source/audio/ and source/textbook/, §2). faster-whisper transcribed both audio folders (~8 + 35 min). Four Sonnet
agents (90–215k tokens): interview bank + 3 mocks + interview.md (speech-player Q/A format), vocab sets, real-audio listening sets + 부록 transcription +
review 듣기 keys, profile view. Fable: speech player got a collapsible options row, the Q/A format with "ซ่อนคำตอบ", and kotag colours (nested karaoke/colour
spans); the site got `audio` sections, clips split, v28 published with 57 mp3s; the user's old family paragraph was recovered from the 10/10 chat transcript.

2026-11-01 (Opus 5.5 + 3 Sonnet agents, ~660k agent tokens, 6–9 min each): the user dropped test 25 (9/10), sheet 26 and the centre's vocabulary book 23–37 in
source/ root → filed (§2), test 25 + sheet 26 transcribed by hand, 25과 prediction scored (B = workbook F pictures, C9 = rank 1). Agents: vocab 23–37 sheets →
04_vocabulary/unit23…37 + 90_themes (950 words on the site) · 본문 듣기 23–37 → listening/unit23…37 + textbook_listen2.json · 26과 prediction (24 pp) + its site
sets + daily-25/sheet-26 sets. Site v46 published; both guides rebuilt (639 / 726 pp). Earlier on 10/30: workbook 26과 checked from photos (§6b). Not committed.
Evening (same day, 3 more Sonnet agents, ~420k tokens, 2–3 min each): the user asked why 26과 still showed 0/46 after a full pass (all 46 words sat in box 1 —
"จำได้" = box ≥ 2 needs a second right answer, and a correct first answer gives box 1) and whether the words came from the workbook/textbook too (they did
not: centre's sheets only). Site v47: unit chips + stats rows carry a blue "ฝึกแล้ว N" segment (VBar component: mastered · learned · seen) and the vocab
gap fill above (950 → 1,366 words; 410 new word clips, clips3 13.5 MB + clips4 7.7 MB; v47 sent app.html + vocab.js + clips3.js + clips4.js); guides rebuilt 655 / 728 pp, scan clean. Note: srsApply() does not check the due date, so re-doing a unit the same day also promotes words — left as is.
