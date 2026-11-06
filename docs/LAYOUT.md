# Folder layout, deliverables, practice-site version log, book assembly

*Moved verbatim from CLAUDE.md on 2026-11-04 to keep the always-loaded file small. Section numbers are the old CLAUDE.md numbers. Add new long logs here, not in CLAUDE.md.*

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
               (2026-11-04) v51: **home hub** — Home() is now a hub of tiles (`CATS`: mini03 hero · daily · vocab tests · textbook listening · mini02 · midterm · review · other) →
               `#x/<cat>` category page (groupsOf/Group) → `#x/daily/<unit>` unit page (UnitGrid/UnitPage, titles from window.KMU_UNITS in data.js) → cover; Crumbs, ResumeBar (⏸ attempts),
               Cover back button = parentOf(st). mini03 = 복습시험③ (11/6, 22–29과) prediction: mini03_writing.json (43 items, 쓰기 100 = ②'s 7 sections + 예비 H/I/J, incl. -겠- item 5-4),
               mini03_reading.json (23·26·29과 main = 10 pts, 24·25·22·27과 예비; 26·29 use the textbook's own 대화로 만들기 frames), mini03_listening.json (10 pts over real tracks
               29-1 · 24-1 · 26-1 · 28-2 · 24-2 · 25-1 + 예비 22-1 · 23-1 · 27-1; 22-1 / 24-2 / 28-2 are NEW mp3s to publish). Agents wrote 쓰기 + 읽기 from content/specs/BRIEF_mini03.md.
               133 sets · 2,576 items · 924 clips. Publish files = {data.js (+ clips*.js when the build changed them)} + the new mp3s.
               (2026-11-05) v52: + `tb-listen-22` in textbook_listen.json (22과 본문 듣기 over the real 22-1.mp3: A = 4-statement choice, B = 5-blank dictation, 6 pts, 10 min) — 22 was the one unit
               missing from the textbook-listening sets (tb-listen jumped 21 → 23); the listen tile now says 5~37과. 134 sets · 2,578 items · 924 clips. Published as artifact version 52 with
               files = {data.js} only (clips/vocab/vendor sizes unchanged, 22-1.mp3 already live from v51).
               (2026-11-05) v53: the group sort in groupsOf() is now `a.id.localeCompare(b.id, undefined, { numeric: true })` (5-13 before 14-21 on the listening page); new exam families `textbook`
               (the 5 tb-listen sets) and `vocab` (vocab-5-13 · vocab-14-21 · vocab-mistakes · vocab-spelling) in EXAMS + mockweb_validate.py + SPEC, so their cover no longer says 중간시험 (the 9 real
               mid-* sets keep it). Checked by dumping the card order of all 32 category/unit pages and the cover subtitle of 18 sets before and after: only #x/listen and those 9 covers changed.
               Published as artifact version 53, files = {data.js}.
               (2026-11-05) v54: 복습시험③ split. The single `mini03-<skill>` sets had counted the 예비 spares (pts 0) inside the clock: 43 / 22 / 23 items in 30 / 20 / 15 min, and the listening flow alone (2 plays +
               answer pause per section, from the mp3 lengths) = 23.1 min, so the 15-min clock cut the spares off mid-section. Now `mini03-<skill>` = scored items only (쓰기 27 · 100 pts · 30 min; 읽기 10 · 20 min;
               듣기 10 · 15 min, flow 12.2 min) and `mini03x-<skill>` = the old 예비 sections as real sets, 1 pt per item (쓰기 16 · 10 min; 읽기 12 · 25 min; 듣기 13 · 14 min, flow 11.1 min); exam stays "mini03".
               Two GROUPS rules in app.html (/^mini03-/, /^mini03x-/) give #x/mini03 two titled groups with notes. The extras are renumbered 1–n (the teacher's `일 번부터 이 번까지` announcements are built
               from `n` → 3 new clips). Sizing rule: listening clock = measured flow + ~3 min; 읽기/쓰기 clocks from a slow-case estimate (0.8 s/syllable reading, 1.5 s/syllable writing + think time) — an
               estimate: the real 복습시험 clock is recorded nowhere and the site stores no time-used (hist = {s,t,at,mode}). 137 sets · 2,578 items · 922 clips. Published as artifact version 54,
               files = {data.js, clips.js, clips2.js}; live data.js sha256 = local, live clips sizes = local.
               Rules learned: the validator accepts `s` = F/M/T/S now; `<보기>` is rejected (write [보기]); a file whose name starts with `_` is a draft the
               build ignores (agents validate `_x.json`, then rename) — several agents can write sets while another builds the site.
               A section may carry `"audio": "audio/<textbook|review>/<file>.mp3"`: the site plays that real recording for ▶ ฟัง (no karaoke) and
               build_mockweb.py copies it from source/audio/ to output/2_Practice_Web/audio/ — publish those files with the artifact.
               (2026-11-05) v55: cloud sync MERGES, never overwrites. v54 pushed the whole per-set doc with "last change wins"; a stale copy elsewhere (no score) beat the
               finished mini03-writing (57/100) at 19:21 and wiped ans/score/hist on every device (seen in Chrome's Local Storage LevelDB log; mini02-listening lost its score the same way on 10-21).
               Now: per-key write times (localStorage kmuweb:kt:<id>, cloud field `t`); ans/self/ai/attempt = newer key wins; score + hist = union by attempt `at` (only 🗑 ล้างผล's t.reset drops
               attempts); vocab srs merged per word (more answers wins, `ep` = clear count, higher ep wins whole); a pre-v55 doc (no t) counts as written at its `at` and its nulls never erase.
               Every write = get → merge → set, one doc at a time (global chain); a live collection onSnapshot merges other devices' writes (falls back to a 20-s collection get when the
               runtime has no listener); pending writes flush on tab hide. AI replies are pinned to their set + attempt (gens). Tests: scratch merge scenarios + a 2-device fake-cloud replay.
               mini03-writing restored into the cloud from the LevelDB log (ans of 19:21:13 + the AI verdicts, regraded with the app's rules = 57/100). Artifact versions 55–56.
               (2026-11-05 night) v56: "results vanish until I reload". Reproduced in headless Chrome: a 2nd tab of the same browser never redrew — the cloud merge found
               the data already in the shared localStorage, so no refresh. Fix: `storage` listener → externalChange() (redraw; a cover re-reads in place without scrolling); an exam/practice
               paper whose attempt was submitted/cancelled/restarted elsewhere (staleAttempt: stored attempt.startedAt ≠ C.startedAt) returns to its cover instead of writing stale answers
               or auto-submitting an empty paper at time-up; saveLeft only rewrites its own attempt; regrade() only rewrites the attempt on screen (C.resAt) and its hist entry.
               Cards carry data-set; __kmu also exposes go / setAns / store / C. Tests kept in scripts/mockweb/test/ (run.sh: merge + 2-device node tests, then the built page in
               5 iframes — 3 same-storage tabs, a 2nd device, a poll-only device — on a fake cloud; 14 checks; before the fix 3 of them failed). Artifact version 57.
               (2026-11-06) v57 (data only, app.html unchanged): daily-29-writing/-listening (7.5/10) + sheet-30-writing in daily_b.json, predict-29 lost its 🔮,
               daily_predict30.json (predict-30-1/2/3-writing · -vocab 45 · -listening 22), scores.json: 29과 daily + 복습시험③ unofficial (쓰기 9 · 듣기 9 · 읽기 10).
               145 sets · 2,705 items · 945 clips (23 new). Sent data.js, clips.js, clips2.js. Artifact version 58.
               Same day: the profile's "หลักฐาน 매일시험" line ran past the card (1216 px in an 818 px box) — `.hist span` was nowrap and the spans are emitted with no
               whitespace between them, so the whole list was one unbreakable run; fix = `display: inline-block` on `.hist span` (also covers the set-history and 복습시험 ②
               lines). Checked in headless Chrome at 1000 px (818/818). Artifact version 59 (page only).
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
  5_Homework/    KMU_Workbook.pdf (워크북 5–22 + 종합문제) · KMU_Listening.pdf (본문 듣기 5–37, 71 pp)
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
