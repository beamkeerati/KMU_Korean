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
- 낭독시험 (read-aloud, 20 marks of 읽기): ① 9/30 9과 · ② 10/6 · ③ 10/12 15과 · ④ **10/15** (announced 10/14, the 19과
  day — the plan names no unit; ① and ③ were the unit taught on the announcement day, so 19과 is the working assumption)
  · ⑤ 10/28 23과 · ⑥ 11/6 · ⑦ 11/12 31과 · ⑧ 11/18. The 19과 texts with pronunciation are in exam02.md §7.
- **Talk to the user in Thai, keep replies short.** Study material = Korean with Thai explanations.
- Stated preferences:
  - Deliverables as **PDF**; fonts **Noto only** (Noto Sans / Noto Sans Thai / Noto Sans CJK KR).
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
  workbook/    KMU workbook unit 05 - 13.pdf · KMU workbook unit 14 - 22.pdf
  everyday/    KMU everyday test unit 05 - 13.pdf · KMU everyday sheet unit 05 - 13.pdf
               KMU everyday test unit 14.pdf · test unit 15, 16, 17, 18, 19, 22 · sheet unit 15, 16, 17, 18, 19, 20, 23   ← daily hand-outs land HERE
               (the user dropped the 23과 sheet as "sheet unit 22" on 10/26 — its content is 23과 ㅂ불규칙/(으)ㄴ 형태 연습, renamed to unit 23)
  miniexam/    KMU mini exam 01 unit 05 - 13.pdf   (복습시험 ①: score sheet + 듣기/읽기/쓰기 papers in one PDF)
               KMU mini exam 02 unit 14 - 20.pdf   (복습시험 ②, sat 2026-10-20: 쓰기 4 pp + 듣기 + 읽기, the student's pencil, no marks yet)
               ← 복습시험 scans land HERE, never in everyday/ (the user wants the two kept apart at every level)
  review/      KMU midterm review 01 unit 05 - 22.pdf   (teacher's 「1급 중간시험 복습문제」, 16 pp: 쓰기 1–14 · 읽기 1–25 · 듣기 1–12 · 말하기 1–20;
               p.17 of the scan is the 19과 sheet again — ignored)
  vocabulary/  KMU vocabulary unit 05 - 22.pdf   (centre's own vocab book, 48 pp: 1–17 word lists per unit · 18–35 본문 듣기 sheets · 36–48 picture themes)
  lecture/     KMU lecture note unit 05 - 12.pdf   (18 pp of the user's PHOTOS of the teacher's slides + notebook; 366 MB; slides actually run 9–22과)
  syllabus/    KMU syllabus 2026 fall unit 05 - 37.pdf · KMU orientation guide 2026 fall GKS.pdf (2026-10-21, 33 pp English, was
               「KOOKMIN_KLC_Fall 2026 GKS Freshman Orientation Guide(노현서수정)」; pages → extracted/syllabus/orientation_2026fall/)
  audio/       (2026-10-21, git-ignored: 147 MB of publisher/teacher mp3s) textbook/KMU audio student's book unit 01 - 37/N-M.mp3
               (N = unit, M = track: 1 대화 · 2 읽어봅시다/듣기 text · 3 발음 drill; units 1–4 have more tracks = 자모) ·
               review/KMU audio midterm review 01 listening/*.mp3 (the teacher's audio for her 복습문제 듣기 1–12; file ids = the
               codes in the ฟัง headings of exercises/review/midterm01_part2.md, e.g. 1-1:01-06 ↔ 1-01…1-06.mp3)
  textbook/    + KMU student's book appendices unit 01 - 21.pdf (2026-10-21, 6 pp = 부록: 듣기 대본 of 8·12·16·20과 + 읽기/듣기 answer keys
               1–21 on pp.2–4, English 대화 translations 5–21 on pp.5–6) → extracted/textbook/appendices/page-N.png
               + (2026-10-25) KMU student's book unit 23.pdf … unit 37.pdf (book 1-2; ⚠️ unit 26 has only 3 pp = grammar pages, the 대화/읽기/듣기/발음
               pages look missing) · KMU student's book appendices unit 22 - 37.pdf (5 pp; its keys cover 22–37, the 1–21 file has no 22과 key)
               · KMU student's book table of contents.pdf (4 pp) → OCR'd 23–37 into extracted/textbook/unitNN/ + unitNN.txt;
               appendix → extracted/textbook/appendices_22-37/, contents → extracted/textbook/contents/ (200 dpi)
extracted/     intermediate extraction output (regenerable, ~300 MB) — same names as source/
  textbook/    unitNN/page-N.png (300 dpi) + unitNN.txt (tesseract)   ← written by scripts/ocr_extract.py
  workbook/    unit05-13/wb-01..41.png · unit14-22/wb-01..50.png       (graded scans, 150 dpi)
  everyday/    unit05-13/test-1..9.png + sheet-01..10.png · unit14/test-1.png · unit15/sheet-1..3.png + test-1.png · unit16/sheet-1..4.png + test-1.png · unit17/sheet-1..2.png + test-1.png · unit18/sheet-1..2.png + test-1.png · unit19/sheet-1..2.png + test-1.png · unit20/sheet-1.png · unit22/test-1.png · unit23/sheet-1..2.png
  miniexam/    exam01/page-1..5.png (110 dpi; page 1 = score sheet, 2 듣기, 3 읽기, 4–5 쓰기)
  review/      midterm01/page-01..17.png (80 dpi) · vocabulary/page-01..48.png (80 dpi) · lecture/page-01..18.png (150 dpi — photos need it)
content/       ✍️ SOURCE OF TRUTH — edit here, never in output/
  guide/       00_exam_info.md = ส่วนที่ 0 (shared cover of both books; `{{today}}` / `{{days:YYYY-MM-DD}}` are filled at build time,
               so the countdown column never goes stale) · 01_units/unit05…37.md (ส่วนที่ 1 of the By_Unit book, unified template:
               หลังจบบท → 🗣️ vocab → 📝 grammar with 📽️ slide material inline + "ไวยากรณ์ข้อ NN" refs → 💬 대화 → 📖 읽기·듣기 → 🔊 발음
               → 🧪 tests → 🔗 links) · 02_grammar/NN_slug.md (ส่วนที่ 1 of the By_Topic book, topics 01–64 — 36–64 = 23–37과, numbering fixed in content/specs/SPEC_23_37.md, unified template:
               📌 รูปแบบและเงื่อนไข → 📖 ตัวอย่าง (slides merged) → ⚠️ จุดสับสน → 🧪 ออกสอบแล้ว → 🔗 เชื่อมโยง)
               03_particles.md (ส่วนที่ 2) · 03b_question_words.md (ส่วนที่ 3, 5–37과; §3.3 = every answer pattern: 5 rules · yes/no questions by ending · each 의문사 · checklist) · 05_selftest.md (ส่วนที่ 5) ·
               06_quickref.md (ส่วนที่ 6 — ASSEMBLED from per-topic snippets the rewrite agents wrote; 36–64 appended 2026-10-26 from
               06_quickref_parts/NN.md (kept; re-append if a snippet changes); keep 64 entries in topic order)
               04_vocabulary/unit05…22.md (centre's word lists, `###` heading, Thai+English) · unit23…37.md (2026-10-26: the textbook's margin
               word lists — the centre's sheet for 23+ is not scanned except the 23과 photo; glosses are Sonnet's) · 90_themes.md (picture themes) · 91_categories.md (old AI list)
               07_lecture/unitNN.md = ARCHIVE of the slide transcription (`#### 📽️ [topic:NN] …` blocks). Since 2026-10-16 evening
               its content lives inside 01_units and 02_grammar; build.py no longer assembles it.
               (a part = one .md OR a directory joined in name order; dirs start with 00_header.md) · part banners say "ส่วนที่ N", never "ภาค"
  exercises/   workbook/unit05…22.md (+ unit21_review_5-21.md = 5~21과 종합문제)
               everyday/unit00_classroom.md, unit05…20.md, unit22.md (test 22, 8.5/10), unit23.md (sheet 23, user's pencil)  (매일시험 + 연습지 merged per unit)
               miniexam/exam01.md  (복습시험 ① as sat: one `##` per paper — score sheet · 듣기 · 읽기 · 쓰기 — then `# 정답`)
               listening/unit05…22.md  (본문 듣기 sheets, user's pencil checked; key = textbook dialogue)
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
  predictions/ everyday/unitNN.md (매일시험 — unit17 … unit20, unit22, unit23) · miniexam/examNN.md (복습시험 — exam02) ·
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
               {name, group, max, got|null, date, note} + daily / review / presentations).
               A section may carry `"audio": "audio/<textbook|review>/<file>.mp3"`: the site plays that real recording for ▶ ฟัง (no karaoke) and
               build_mockweb.py copies it from source/audio/ to output/2_Practice_Web/audio/ — publish those files with the artifact.
  speaking/    발표 scripts in the my_room.md format (Korean line · Thai reading · Thai meaning · swap table · Q&A · pitfalls):
               my_room.md (발표 ① 제 방) · myself.md (발표 ② 자기 소개, 10/21) · vacation_plan.md (방학 계획, 10/20) → build.py speaking
  syllabus/    one-off PDF (Thai syllabus): python3 scripts/make_pdf.py <md> --pdf-dir output
scripts/
  build.py       ⭐ python3 scripts/build.py [guide|exercises|everyday|miniexam|predict|review|speaking|all]
  make_pdf.py    Markdown → PDF (WeasyPrint); `--pdf-dir DIR` puts the PDF somewhere other than next to the .md
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
                 cached in extracted/mockweb_clips/<sha1>.mp3 — only new lines are generated. Needed because Chrome on Ubuntu
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
  1_Guides/      KMU_Guide_By_Unit.pdf (เล่ม 1, 200 pp since 10/26) · KMU_Guide_By_Topic.pdf (เล่ม 2, 357 pp) · KMU_Mindmaps.pdf (34 maps)
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
                 ans/self/ai/score/hist/attempt so the removal also syncs to the cloud). v35 (10/22): dlg() in app.html puts every speaker turn of a dialogue prompt (q text and sec.box) on its own line at render time — a 가/나/A/B/남자/여자/○○ 씨 label, or any short label after .?!) or ___, starts a new line; 21 prompts in mid_writing.json were run-on, the rest already had \n. v36: Fix() under each graded item = three labelled rows 📘 เฉลย (stored key + why) · 🤖 AI (verdict/comment/แก้เป็น or ยังไม่ได้ตรวจ) · ✋ ตรวจเอง (ถูก/ครึ่ง/ผิด); the row whose result sets the score carries a นับคะแนน tag. v37: aiV(r, answer) — an AI h/x whose own `fix` equals the answer (spaces/punctuation ignored, squash()) is scored and shown as ถูก (with a note); applied in grade(), Fix, SpeakOut, AiBox, also to verdicts already stored. AI_RULES gained: fix == answer ⇒ v must be o, no h/x without a named error, open personal questions (뭐 하세요?) accept any sensible content. v38: the grader call uses AI_OPTS = {model 'claude-opus-5-5', effort 'high', modelTier 'complex' as fallback} (user's choice 10/22; was modelTier 'default'). It is the only sample call in app.html. v39: results AI line has 🔄 ให้ AI ตรวจใหม่อีกรอบ (RedoBtn, two-step confirm) → aiRedo() clears ai:<id> (self marks kept, they still win), regrade(), aiGradeAll() — re-grades without retaking. v40: new set vocab-mistakes (content/mockweb/vocab_mistakes.json, 73 items: A 40 Thai→Korean words the user has misspelled · B 8 number+counter · C 13 word-choice MC · D 12 spelling MC; every `why` names what the user wrote and where). Sources = the user's synced practice answers (ArtifactData list data/users/me on the site artifact → 94 wrong items) + §6b. Home group 🎯 ศัพท์ที่เคยผิด. **Publish files = {data.js, clips.js, clips2.js, vendor.js} + every audio/**/*.mp3**
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
- Korean wraps mid-word in narrow table cells (빔입니/다). WeasyPrint 70 ignores `word-break: keep-all` (tested 2026-10-18: output identical
  to normal). U+2060 word joiners between syllables do keep words together, but they break text search/copy in the PDF, so they were
  not adopted — syllable-level wrapping is normal Korean typography; leave it.
- kiwipiepy 0.24 and pythainlp 5.4 live in `~/.local/lib/python3.12/site-packages` (pip --user, 2026-10-17); the first
  `kotag` call per process takes ~2 s to load Kiwi + the vocabulary user words. Known Kiwi traps handled in kotag.py:
  누가 = nougat (pre-analysed), 마셔요 = 말+셔요, 주무세요/계세요/드세요 (user stems 주무·계·드), 어제 → 어+제 (MAG user word),
  공부하 tagged XSA (noun set keeps 공부 blue), 을/를·이/가 standalone lists (direct rules, no Kiwi).

## 6. Status of the content
- **Units 14–22 (added 2026-10-07)** were written by Sonnet subagents from OCR + page images, to
  `content/specs/SPEC_14_22.md`. Provenance caveats, not yet verified against anything:
  - workbook 15–22 scans are *blank* pages → every answer key there is AI-solved, not the teacher's;
    only unit14 carries real ⚠️ teacher marks. `unit21_review_5-21.md` has 42 items (scan numbers
    1–42), key self-solved; agent flagged Q29/Q36/Q39/Q40 as judgment calls.
  - guide vocab tables for 14–22 came from noisy OCR; Thai glosses unverified against the page images.
  - 18과 clock items C.2/C.5 and 22과 food pictures A.2/A.5 were read from small line art — check.
- **Units 23–37 (added 2026-10-26, book 1-2)** — 8 Sonnet agents from content/specs/SPEC_23_37.md (5 × unit chapter + vocab + mind map for 3 units
  each, 3 × grammar topics 36–64 with quickref snippets; 300–460k tokens each, 11–22 min) + 1 integration agent (all.md threads, ส่วนที่ 3 to 5–37,
  ส่วนที่ 5 sets N–T). Fable: SPEC, ส่วนที่ 0 (table 36–64, final-term plan, exam→reading map), quickref assembly, covers/headers, builds.
  Provenance caveats: everything is from the textbook page images only (no workbook/exercise scans for 23+); all 연습/활동 answers the book
  does not print are the agents' own and are labelled so; 읽기/듣기 keys come from the 22–37 appendix. Missing scans: 26과 has only pp.262–264
  (대화 26-1 / 읽기 26-2 were transcribed from the mp3s by Whisper), pages 285, 294, 315, 323, 332, 359 (unit-closing/culture/발음 pages) are absent;
  23/25/29/30/31/33/34/35 have no 듣기 in the appendix (scripts exist only for 24, 28, 32, 36). Book typos noted in the files: 33과 -(으)ㄹ box
  "verb ending with 있다/없다", 32과 box "Lesson 9" (= 29), 35과 읽기 key 배우 vs 영화감독, 30과/28과 appendix keys not matching the printed
  questions. Grammar the book has beyond the table was folded in as 📌 เสริม: 24과 -(으)세요 (ข้อ 39), 25과 ㄹ 탈락 (40), 28과 그래서/못 (48/46),
  34과 frequency adverbs 자주·가끔·거의·전혀 (58), 35과 N이/가 되다 (59/60), 36과 -아/어도 되다 (61/64), 37과 -(으)려고 (unit file เสริม).
  Agent-glossed words to double-check: 바뀌다, 길이 막히다, 보령, 스포츠 댄스, 하숙집, 포장하다, 돌아가시다, 호박 (zucchini), 게르, 앞머리; 25과 margin
  word 이상하다 is not in its reading; 23과 reading has 카페 where the centre's sheet lists 카레.
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
  and all 16 (으)ㄴ cells right except 메워요 for 매워요. Earlier tests
  5–13 carry ⚠️ marks but no numeric score on the scan.
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
2026-10-21: 복습시험② marks arrived (쓰기 7.5 · 듣기 8.5 · 읽기 9.0 · 말하기 10; grading system explained, §1). The teacher's hints for the 말하기 midterm (25 Q /
15 min from the 말하기 table + the 19과 sheet + self-intro + family) and three new sources arrived: the publisher's textbook audio, her own 듣기 audio for the
복습문제, and the book's 부록 (filed under source/audio/ and source/textbook/, §2). faster-whisper transcribed both audio folders (~8 + 35 min). Four Sonnet
agents (90–215k tokens): interview bank + 3 mocks + interview.md (speech-player Q/A format), vocab sets, real-audio listening sets + 부록 transcription +
review 듣기 keys, profile view. Fable: speech player got a collapsible options row, the Q/A format with "ซ่อนคำตอบ", and kotag colours (nested karaoke/colour
spans); the site got `audio` sections, clips split, v28 published with 57 mp3s; the user's old family paragraph was recovered from the 10/10 chat transcript.

