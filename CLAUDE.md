# CLAUDE.md — KMU Korean 1 exam-prep workspace

Claude Code loads this file into every message, so it is kept short (target ≤ 30,000 characters).
**Long logs live in `docs/` — read them only when the task needs them; append new logs there, not here:**

| File | What it holds |
|:---|:---|
| docs/COURSE.md | full course facts: exam schedule details, pass rules, grading, 복습시험 formats, midterm notes, 낭독시험, unit→grammar map 5–13, presentations |
| docs/LAYOUT.md | full folder tree with every file's provenance, practice-site version log v9–v53, how the books are assembled |
| docs/RENDERER.md | every make_pdf.py gotcha, environment notes, plugin policy (why each plugin is off) |
| docs/STATUS.md | content status + provenance caveats per unit, textbook/workbook audits, **the daily-test score log with per-item details** |
| docs/MISTAKES.md | the user's recurring mistakes, every sighting with dates |
| docs/HISTORY.md | session-by-session history |

## 1. User, goal, exams
- Thai GKS scholar at Kookmin University Korean Language Center, level 1 (국민한국어 1). **Reply in Thai, short.** Study material = Korean with Thai explanations.
- Course = 자모 + Units 5–37. Midterm covered 1–21과 (book 1-1); final = 23–37과 (book 1-2).
- **Dates still ahead:** 11/19 총복습 (no new unit; a 37과 매일시험 is unconfirmed) · 기말 **11/20** (쓰기·듣기·읽기; analysis = content/predictions/final/final02.md) / **11/23** (말하기) · 기말 발표 11/24 (topic announced 11/10). (The handout's 10/20 for 기말 was corrected to 11/20 by the teacher.) 복습시험③ was sat 11/6, ④ (30–37과) 11/18. **Teacher after ④: its ข้อ 6 type
  (두 문장 → 한 문장 with a 보기 of 4 grammar points, connectors + -(으)ㄹ/-는/-(으)ㄴ + N mixed) WILL be on the 기말** — drill sets final-combine + 복습문제 §3/§5.
  **총복습 11/19 hints:** 3 h, 쓰기 (50 min, includes a ~300-자 composition on the 쓰기 (3) 계절 or 쓰기 (4) 취미 topic — source/writing/) → 듣기 (all
  multiple choice) → 읽기; review ④ (words + task types); memorise 대화 32-1 + 37-1; picture description from textbook 245쪽 연습 2 · 263쪽 연습 2 ·
  271쪽 연습 3; 말하기 11/23 = review handout pp.14–16 (p.16 식사 예절 new). Pack = content/predictions/final/final03.md + site sets final_0_hints.json.
- **Pass rule:** every skill's average of 중간 + 기말 ≥ 70; < 60 = fail; 60–69 may re-test. Each skill /100 = 시험 50 + 복습시험 20 + coursework 30 (per term). Details → docs/COURSE.md.
- **Results so far:** 중간 말하기 41.2 · 듣기 42.0 · 쓰기 45.5 · 읽기 49.0 (/50). 복습시험①+② 말하기 20 · 쓰기 16.3 · 듣기 16.0 · 읽기 19.0 (/20). 복습시험③ (slip 11/10)
  말하기 10 · 쓰기 8.9 · 듣기 9.0 · 읽기 10 (/10 each, 37.9/40 — best of the three). ④ by the user's recall (official score not out): 말하기 ≈ 10 · 쓰기 ≈ 7.7 · 듣기 9 · 읽기 8.5. Weakest: 말하기, 듣기. 매일시험 average ≈ 7.5/10; the losses are **word recall**, not grammar.
- 복습시험 (user says "mini exam") = 말하기 interview + 쓰기 (several short sections) + 듣기 + 읽기 (textbook 읽기 passages lifted almost verbatim). Exams "look like the book": predictions should lift textbook 대화/읽기/연습 nearly verbatim.

### 1.1 Stated preferences (all deliverables)
- Deliverables as **PDF**. Fonts: Thai/Latin = TH Sarabun (installed as Laksaman), Korean = Noto Serif CJK KR; mind maps keep Noto Sans.
- **Book style** for the two guides (contract content/specs/SPEC_book_style.md, checker scripts/book_style_check.py): page look = "book layout v2" block in make_pdf.py (`.book` only: 6-rank type scale, open tables, paging rules + what was rejected → docs/RENDERER.md — the user wants neither cramped nor empty pages; teacher-slide material is MERGED into the chapter's own sections, never a separate "from the slides" section); INTRO box per chapter, lead sentence per section, one Korean example per line with its gloss, no `·`-chains, no bold pseudo-headings.
- Every exercise needs a **Thai translation**; pictures = the **real picture** (crop of the book/paper, or a clear redraw when none exists — user 11/19)
  + its Thai `🖼️ …` caption; in PDFs the picture sits left of ALL its item text (never 가 beside and 나 below). Docs need a TOC; each `#`/`##` starts a page.
- Answer keys ordered by question number, one item per line; sentence answers get long ruled lines.
- Wants detail and full coverage; likes deep-dive explanations.
- **Colour by word function** in every PDF (scripts/kotag.py, SPEC content/specs/SPEC_colors.md): n blue · p orange · v green · e purple · q teal · x red · m brown · a grey · dotted underline = honorific; the Thai gloss mirrors the colours. Fix a wrong colour by writing an explicit `{c:…}` tag in content.
- If the user only asks a question ("ถ้ามันถูกอยู่แล้วไม่ต้องแก้ ฉันแค่ถามเฉยๆ"), answer it; do not edit files.
- The user watches the token quota: delegate bulk transcription/writing to Sonnet agents with a strict brief; no multi-agent audits unless asked.

## 2. Layout (one folder per material type at every level; full tree → docs/LAYOUT.md)
```
source/       originals — never modify contents; only move/rename (naming §2.1). The user drops new scans in source/ root → file them.
  textbook/ workbook/ everyday/ miniexam/ review/ vocabulary/ lecture/ syllabus/ midterm/ speaking/ audio/ (git-ignored mp3s)
extracted/    regenerable page images/OCR (git-ignored)
content/      ✍️ SOURCE OF TRUTH — edit here, never in output/
  guide/        00_exam_info.md (ส่วนที่ 0) · 01_units/unitNN.md (book 1, 5–37) · 02_grammar/NN_slug.md (book 2, topics 01–64;
                23–37과 = 36–64, numbering in content/specs/SPEC_23_37.md) · 03_particles · 03b_question_words · 04_vocabulary/unitNN.md
                + 90_themes.md · 05_selftest · 06_quickref.md (+ 06_quickref_parts/) · 07_lecture/ (archive)
  exercises/    workbook/unitNN.md (printed publisher keys 5–37) · everyday/unitNN.md (매일시험 + 연습지 per unit) ·
                miniexam/examNN.md · listening/unitNN.md · review/midterm01_part*.md
  predictions/  everyday/unitNN.md · miniexam/examNN.md · midterm/ (parts assembled by scripts/assemble_midterm.py)
  mindmaps/     unitNN.md + all.md (outline grammar in scripts/build_mindmaps.py)
  mockweb/      practice-site JSON sets (schema content/specs/SPEC_mockweb.md) + scores.json (grading data, not a set)
  speaking/     발표 scripts: my_room · myself · vacation_plan · food_intro (+ images) · interview(_cards)
  specs/        SPEC_* contracts and BRIEF_* agent briefs
docs/         long logs moved out of this file (see the table at the top)
scripts/      build.py ⭐ · make_pdf.py · kotag.py · build_mockweb.py ⭐ · mockweb_validate.py · build_speech_audio.py ·
              build_interview.py · build_mindmaps.py · ocr_extract.py · assemble_midterm.py · pdf_artifact_scan.py · book_style_check.py
output/       🤖 GENERATED, never hand-edit. Entry = output/START_HERE.html (hand-written Thai index — update its links when a
              deliverable is added/renamed) + README.md
  1_Guides/ (KMU_Guide_By_Unit.pdf · KMU_Guide_By_Topic.pdf · KMU_Mindmaps.pdf · mindmaps/) · 2_Practice_Web/ · 3_Exam_Prep/ ·
  4_Daily_Tests/ (KMU_Everyday_unitNN.pdf + predictions/) · 5_Homework/ (KMU_Workbook · KMU_Listening) · 6_Speaking/ · _build/md/
```

### 2.1 Source file naming
`KMU <material> [<qualifier>] unit <NN>[ - <NN>].pdf` — lowercase material names, zero-padded unit numbers
(e.g. `source/everyday/KMU everyday test unit 28.pdf`, `KMU everyday sheet unit 29.pdf`, `source/miniexam/KMU mini exam 03 unit 22 - 29.pdf`).
`git mv -k` silently skips untracked files — use `mv`. 복습시험 scans go to source/miniexam/, never everyday/.

### 2.2 Builds
- `python3 scripts/build.py [guide|exercises|everyday|miniexam|predict|review|speaking|all]` → PDFs in output/.
  `everyday` = one PDF per unit (seconds). `predict` rebuilds every prediction PDF. `guide` = both books (slow).
- After building: `python3 scripts/pdf_artifact_scan.py <pdfs>` (exit 1 = raw markup on a page). Overflow check: pdftotext -bbox, any word with
  xMax > 548 pt on A4 = overflow (scratch script; mind maps are posters, skip).
- Speech audio page: `python3 scripts/build_speech_audio.py <name>` → output/6_Speaking/KMU_Speaking_<Camel>_Audio.html (numbered lines
  `**N. 한국어**` + `*reading*` + `🇹🇭 ไทย` in content/speaking/<name>.md; clips cached in extracted/speech_clips/).
- Mind maps: `python3 scripts/build_mindmaps.py` (`--check` = parse only).
- **Real pictures** (11/19): `![🖼️ caption](img:ID)` in Markdown / `"img": "ID"` on a site item or section; crops listed in content/img/*.tsv (one
  manifest per writer; `card:` = drawn), built by `python3 scripts/crop_images.py` (`--grid`, `--sheet`, `--check`); make_pdf puts a picture LEFT of its
  item text (stacked when > 100 mm wide); site packs = img_<json>.js. Open 🖼️ list: `scripts/pic_inventory.py`; agents' site rows: content/img/map_*.tsv
  → `scripts/apply_pic_map.py`. Brief: content/specs/BRIEF_pictures.md. Crops are remastered by Real-ESRGAN (extracted/tools/esrgan, GPU; raw crops in
  extracted/img/_raw/) — details docs/RENDERER.md. 원고지 essay pictures: `scripts/wongoji.py --plain <txt> <prefix>`.

### 2.3 Practice website (output/2_Practice_Web/)
- Build: `python3 scripts/build_mockweb.py` (reads content/mockweb/*.json; files starting `_` are drafts and ignored; edge-tts clips cached in
  extracted/mockweb_clips/). Validate a set file: `python3 scripts/mockweb_validate.py <file>` — `<보기>` is rejected (write `[보기]`); voice `s` = F/M/T/S.
- **Publish:** Artifact publish, file_path `scripts/mockweb/app.html`, url **https://claude.ai/artifact/14Xbi9kWyQgDryHzk7kuzm**, `files` = only the
  output/2_Practice_Web files that changed (from {data.js, clips.js, clips2.js, clips5.js, clips3.js, clips4.js, vocab.js, vendor.js} + any NEW audio/*.mp3);
  omit `capabilities` (keeps db, sample, user). If refused as "unread", run `Artifact list scope:files` on the url first. Compare file sizes with that
  listing to see what changed. Each clips file must stay < 16 MB (build_mockweb splits spoken-line clips over SCLIP_FILES and word clips over VCLIP_FILES; add a file + `<script>` tag in
  app.html when the build says so). Do not re-enable the artifact watch on your own.
- Current: **v71** (11/19: 693 real pictures — Real-ESRGAN remastered — via `img` in 31 lazy packs img_<json>.js — publish the packs that changed; written answers auto-grow, essays get a big box + ⤢ full-screen popup; 📌 hint sets final_0_hints.json) · v68 — 기말 tile (hero) gathers everything for 23–37 (match exam final|mini03|mini04, so the ③ ④ tiles hide): 기말 mock A (복습문제 shape) + B
  (복습시험 shape) in final_1_{writing,reading,listening}.json (brief BRIEF_final_mock.md) · ⭐ final_drill.json · 📋 final_review.json (renamed so it sorts
  before 말하기; group order = file order) — 217 sets · 4,128 items · 1,139 clips · 1,366 vocab words (vocab.js, Leitner drill, VOCAB_PRIO in build_mockweb.py line ~74).
  **v61:** every word has an example sentence + Thai translation + usage note in content/guide/04_vocabulary/examples/unitNN.json (brief
  content/specs/BRIEF_vocab_examples.md, check `python3 scripts/vocab_examples_check.py`); card mode gained 📝 เติมคำในประโยค (cloze); a new word in
  04_vocabulary/unitNN.md needs its example entry too (the checker compares the lists) **and a row in 04_vocabulary/91_categories.tsv** (meaning category +
  -아/어요 form → the By-Topic book's 📂 คำศัพท์แยกหมวด; check `python3 scripts/vocab_categories.py --check`, brief content/specs/BRIEF_vocab_categories.md).
  **v63 meaning audit** (content/specs/BRIEF_vocab_meaning_audit.md): two words must never share a gloss (고민 ≠ 걱정하다, 놀다 ≠ 치다, 늦게 ≠ 느리다) —
  give each a nuance in brackets; same-spelling words (개 · 반 · 배 · 쓰다 · 일) are merged into one card by `HOMONYMS` in build_mockweb.py (one example per meaning).
  **Sizing rule (v54):** a set's `minutes` must fit its own items — listening clock ≥ flow (2 plays + answer pauses, ffprobe the mp3s) + ~3 min; spare/예비 items go in their own set
  (`mini03x-<skill>`, own clock), never inside a timed set (the clock auto-submits). 복습시험③ = `mini03-*` (scored: 30/20/15 min) + `mini03x-*` (예비: 10/25/14); two GROUPS rules in app.html.
  **Navigation (v51):** home = hub of tiles (`CATS` in app.html, first match wins, `other` = catch-all) → `#x/<cat>` → daily tests only `#x/daily/<unit>`
  (unit titles = `window.KMU_UNITS`, read from the first line of content/guide/01_units/unitNN.md by build_mockweb.py) → set cover `#<setId>` (back button =
  `parentOf(st)`). A new exam family = a `CATS` entry + its `exam` id in mockweb_validate.py `EXAMS` (+ EXAMS in app.html for the cover title).
- Daily sets: content/mockweb/daily_a.json (05–13) · daily_b.json (14+): `daily-NN-writing` / `daily-NN-listening` (voice T) / `sheet-NN-writing`, each
  with a `group` string like "매일시험 28과 · 4 Nov · 7/10". Predictions: daily_predictNN.json, group "🔮 เก็งข้อสอบ 매일시험 NN과 (…)"; **when the
  test comes back, change it to "เก็ง 매일시험 NN과 · สอบแล้ว D Mon · X/10"** so the board stops pinning it.
- **Cloud sync (v55):** per-key times (`kt:<id>` / field `t`), score+hist = union, never a whole-doc overwrite — keep it that way when touching `cloud` in app.html
  (a whole-doc push lost the 복습시험③ 쓰기 score on 11-05). Recovery source if it ever happens again: Chrome `Local Storage/leveldb` (*.log keeps old values).
  After touching sync / store / attempt code run `bash scripts/mockweb/test/run.sh` (merge tests + 5-window headless test on a fake cloud; must print no FAIL).
- scores.json: load, append to `daily` ({unit, got, max, note}), dump with indent=1, ensure_ascii=False. The profile view reads it.
- The claude.ai frame refuses the microphone; local `start.sh` serves it for mic use. Feature history → docs/LAYOUT.md.

### 2.4 Other published pages
- 자기 소개 speech audio: https://claude.ai/artifact/UB8eXhn7DoTV6pVQDVMPSC (public)
- Interview cards: https://claude.ai/artifact/LCavjNUStqqQL4txtesUvj (private)
- 음식 소개 (팟타이) speech audio: https://claude.ai/artifact/FNs9oSPq3pgC49LfRR6bpE (private)

## 3. Daily routine — the teacher hands out a new test/sheet
1. Move the scan to `source/everyday/KMU everyday test unit NN.pdf` (or `… sheet unit NN.pdf`); check source/ root after every drop.
2. `pdftoppm -r 110 -png "<pdf>" extracted/everyday/unitNN/test` (or `sheet`); zoom red-pen/handwriting at 250 dpi crops.
3. Write/extend `content/exercises/everyday/unitNN.md`: test section first (`## NN과 · 매일 시험 (…)` + italic summary with score, ○ full · △ half ·
   / zero), sheet section (`## NN과 · 연습지 (…)`), then `# 정답` with one `## …` key per paper; ⚠️ = marked wrong (teacher) or self-checked (sheet).
4. `python3 scripts/build.py everyday` + artifact scan.
5. Score: append to scores.json `daily`; add a "✅ ผลจริงหลังสอบ" table at the top of predictions/everyday/unitNN.md; retire the 🔮 group;
   add `daily-NN-*` / `sheet-NN+1-writing` sets.
6. Prediction for tomorrow: Sonnet agent → predictions/everyday/unitNN+1.md (template = the previous unit's file) + daily_predictNN+1.json;
   then `build.py predict`, `build_mockweb.py`, publish. Update START_HERE.html and §1/§6 here (one line), the full log goes to docs/STATUS.md.

**What the papers look like (since 22과):** A 4 items (one grammar) + B 4 (the other) + C 2 dictation, 10 points. **A/B order is not fixed** (27과
flipped). Items are lifted almost verbatim from the workbook (25과 B = workbook F in full), the textbook 연습 and the sheet handed out the day
before. Dictation = 대화/읽기 first lines, 연습 examples, grammar example sentences — rank 대화 lines first and list the SHORT phrase.
Mock 1 = workbook · 2 = sheet (+ any teacher hint) · 3 = textbook. **Teacher hints are reliable** (28과: the hinted categories 동물/음식/과일/운동
all appeared) — put them at the top of the prediction and drill them first.

**Predicting a 복습시험** (method + evidence: content/specs/BRIEF_mini03.md §1): 쓰기 format changes every time (① 5 sections, ② 7) → keep ②'s 7-section skeleton for the
main 100 and put the other formats in 예비 sections; 읽기 = textbook 읽기 passages, and the textbook itself prints a 대화로 만들기 frame in 23·26·29·30과 (top picks);
듣기 = the centre's 본문 듣기 sheets (track NN-1) + the formal 듣기 of 8·12·16·20·24·28·32·36과 (tracks NN-2/-3). ③ mock = content/mockweb/mini03_{writing,reading,listening}.json.
**How ③ scored** (exam03.md §2): 읽기 passages 3/3 · 듣기 9/10 items from mock dialogues · 쓰기 grammar 100 % but format 4/7 sections — for ④ put picture → theme-word
sections (with a 보기) in the MAIN set, keep 보기 word-choice + 질문에 대답하세요, add a paragraph fill with irregular verbs.
**How ④ scored** (exam04.md §2): 읽기 3/3 passages in the same order · 듣기 10/10 items from mock tracks (6 main + 4 예비) · 쓰기 5/7 sections in the main set
(+ 달력 in 예비; 반대말 new). ④ = a cut-down 기말 복습문제 (§4 ← §1 · §6 ← §3+§5, 6-1 verbatim · §7 ← §6): the 기말 will lift that handout.

**A returned 복습시험:** `source/miniexam/KMU mini exam NN unit AA - BB.pdf` → extracted/miniexam/examNN/ → content/exercises/miniexam/examNN.md
(one `##` per paper, ⚠️ where deducted) → `build.py miniexam`. Prediction for the next one → content/predictions/miniexam/examNN.md → `build.py predict`.

## 4. Renderer rules that bite (full list → docs/RENDERER.md)
- Never write `~~` (prints literally); use `x ✗`.
- Inside `*( … )*`, a digit directly before `)` breaks the italics and splits the key (`อันดับ 6)*` ✗) — reword.
- A `###` heading containing 쓰세요/바꾸세요 puts two ruled lines under every item (not with 고르/단어); `####` only with an explicit sentence
  instruction. One-word blanks inside dialogue: `나: 회사에서 2)(　　).` with a blank line between lines.
- Consecutive `> ` dialogue lines merge — put a bare `>` line between them. `가:`/`나:` lines inside a list item need two trailing spaces.
- Leave a blank line before any heading that follows a table. No 4-space indent before ①②③④ (becomes code). Two `---` in a row print "---".
- `{c:…}` braces are reserved for colour tags. `{{today}}` / `{{days:YYYY-MM-DD}}` are build-time placeholders in 00_exam_info.md.
- Thai has no line breaking in this Pango: make_pdf.py inserts U+200B between Thai words (thai_break_opportunities); word blanks in tables of 6+
  columns are 5 em. Korean words never split (wrap_korean_words). Keep table cells to a few Korean words.
- Low-res renders make blue/purple Thai look black — check colours at ≥ 200 dpi. `pdftotext` mangles Thai marks; the PDF is fine.
- Python packages are in ~/.local/lib/python3.12/site-packages (kiwipiepy, pythainlp, edge-tts, faster-whisper "small" int8 — decode mp3 with ffmpeg
  to f32le 16 kHz and pass a numpy array).

## 5. Content status (details and caveats → docs/STATUS.md)
- Guides, vocab, mind maps, listening sheets, workbook (with the publisher's printed keys) cover **5–37과**. Everyday tests transcribed for 5–36, sheets
  for 5–37; predictions for 17–37 (scorecards on 22–36; **from 35과 predictions are SHORT — ≤ 22 KB / ≤ 12 pages, the user found 30–50 pages too long; same for exam predictions**). 기말 pack (teacher's handout 11/13, source/review/KMU final review 02 unit 23 - 37.pdf): content/exercises/review/final02_part{1,2}.md (AI key) · content/predictions/final/final01.md (말하기 기말 연습, 19 questions) · 복습시험④ mock = content/predictions/miniexam/exam04.md + content/mockweb/mini04_*.json; real ④ = content/exercises/miniexam/exam04.md + sets mini04r-* and the 기말 drills final-combine/-antonym/-question in content/mockweb/final_drill.json; 기말 mock A/B = final_1_*.json. 복습시험 ①②③④ papers in content/exercises/miniexam/ (exam03.md §2 = how the ③ mock scored). The 중간시험 복습문제 key is AI-solved; agents' sample answers are labelled ตัวอย่างตอบ.
- `extracted/everyday/unit05-13/test-N.png` is not unit N — check the page header (`1급 매일 시험_N과`).
- 매일시험 score log (details per item in docs/STATUS.md): 5과 7.5 · 6과 7 · 7과 8 · 8과 9.5 · 9과 5 · 10과 8.5 · 11과 5.7 · 12과 6.2 · 13과 4 · 14과 7.5 ·
  15과 8.5 · 16과 10 · 17과 8 · 18과 10 · 19과 8.5 · 22과 8.5 · 23과 4.5 · 24과 8 · 25과 9 · 26과 5.5 · 27과 7.5 · 28과 7 · 29과 7.5 · 30과 9 · 31과 7.5 · 32과 8 · 33과 8.5 · 34과 8.5 (lost 차→자, 책→젝, an extra 에 in dictation) · **35과 10** ("단어 시험": inline blanks -는 것 + -아/어 보다 + 2 dictation) · 36과 8.5 (8-cell table: present form written in 2 past-column cells; 약속 → 야속) (31과–32과 used an 8-cell picture conjugation table × 0.5 + 3 picture sentences + 3 dictation;
  33과 went back to sentences A 4 + B 3 + C 3 — the format is not fixed; 32과 lost 빠르다 written 바르다 ×3; 33과 lost only vowel spellings).
- Low papers (9과, 13과, 23과, 26과) are the vocabulary-heavy units → recall of words is the chronic loss; the site's daily vocab drill targets it.

## 6. The user's recurring mistakes — top list (every sighting → docs/MISTAKES.md)
Use these when checking work or writing predictions. ★ = has cost marks repeatedly.
- ★ **ㅈ/ㅊ shapes** (9+ tests: 젝/책, 몆/몇, 장마절, 자가/차가, 남차) · ★ **ㅐ/ㅔ** (네 게, 테국, 메워요) · ★ **other vowels written as ㅡ** (글음 · 아르바으트 · 음료스, tests 32–33) · **ㅖ/ㅕ** (여쁘지만, 여뻐서) · 가 written like 기 · **ㅃ/ㅂ** (runner picture = 빠르다 written 바르다 ×3 on test 32) · 길을 → 글음 ·
  ★ **걸려요 written 거려요** ×4 on test 31 (−2) · 선물 written 성물.
- ★ **Object marked with 이/가 instead of 을/를**, esp. inside -는/-(으)ㄴ/-(으)ㄹ 수 phrases (책이 읽는 ×4 on test 27; 시계가 받았어요; 음식를).
- ★ **Vocabulary recall under test conditions** (23과 4.5; 만나고 for 앉고; 요리하세요 for 만드세요 — use the unit's target verb; 동물).
- ★ **Verb choice 하다/타다/치다** (피아노를 할 ✗ → 칠; 운전을 탈 ✗ → 할) — read the printed sentences first; the answer is often on the paper.
- ★ **Dropped 으 / 어** in free production though drill tables are right (받십니다, 씻러, 읽어세요; 맛있서, 재미없서 → 맛있어서; 29과 멀서 ×2 → 멀어서 —
  ㄹ-stems keep ㄹ before 어, drop it only before ㄴ: 머니까).
- -아/어서: no tense before 서 (✗ 왔어서); not before commands/suggestions (-(으)세요, -(으)ㄹ까요, 같이 -아요 ✗ → -(으)니까).
- -는 vs -(으)ㄴ by time words: 지금/자주/요즘 → -는; 어제/지난주 → -(으)ㄴ (지금 배운 ✗). Adjective -(으)ㄴ = present (큰), verb -(으)ㄴ = past (먹은).
  ★ The time-word test is for VERBS only: 작는 / 예쁘는 ✗ → 작은 / 예쁜 (복습시험③, −6); 다르는 / 빠르는 ✗ → 다른 / 빠른 (workbook 32).
- ㄹ-stems: 만들은 ✗ → 만든, 만들아요 ✗ → 만들어요, 머세요 vs 멉니다; **ㄷ-irregular -(으)ㄹ 거예요 keeps 을** (걸 거예요 · 들 거예요 · 물 거예요 ✗ → 걸을 · 들을 · 물을 거예요 on sheet 31); ㅂ-irregular is right in tables but slips in sentences (아름다왔어요 ✗ → 아름다웠어요, only 돕다/곱다 → 와; 맵으면 ✗ → 매우면, workbook 33); -(으)ㄹ forms written with 다 (잘다 · 살다 ✗ → 잘 · 살) and 르 + ㄹ = 자를 · 부를 (잘를 · 불를 ✗); 르: 부르다 → **불러요** (불라요 ✗ in a sentence while the table was right — the other five give 라요).
- N(이)나 / Noun + 이다 by the final: 김치이나 ✗ → 김치나 (workbook 34); 학생였어요 ✗ → 학생이었어요 (also 학생여서 ✗ → 학생이어서); 친구에요 ✗ → 친구예요.
- 보다 comparisons: the noun before 보다 is the loser (reversed winners twice); no stray 이 on the noun inside the 보다 phrase.
- Position words: landmark reversed (A가 B 앞에 = A is in front of B). 한테/한테서/께 direction; places/things take 에/에서, not 한테.
- Answers the wrong question word (언제 → 가족을 만날 거예요); keeps the question's tense and noun when answering.
- ★ **Reads past what is printed around a blank** (복습시험④ −14): wrote the printed ending again (물어요 + 아/어 보세요 ✗ → 물어), ignored a printed particle
  (학생증이 ___ → 있어야 해요, wrote 을 가지고 와야), left a -(으)면 item blank instead of reusing the question's verb. Also 반대말 swapped (밝다↔어둡다 · 빠르다↔느리다), 포장하다 unknown.
- Rewrite tasks: copy the second sentence's particles exactly (공원에 → 공원이 ✗; two sentences → -(으)ㄹ + N: 이사할 아파트로는 ✗ → 아파트는) and don't drop words (좀); no doubled particle (음식은 은).
- Spacing: 학생 중에서 · -아/어지다 is one word (추워졌어요) · 갈 거예요 has a space · particles attach.
- Does well: ㅂ니다/습니다, -지 않-, 겠, ㅡ-drop past, special honorific verbs, 에서 for activity places, ㅂ irregular tables.

## 7. Presentations (details → docs/COURSE.md §6c)
- Done: 제 방 · 방학 계획 (10/20) · 자기 소개 (10/21, myself.md — the user edits it by hand; don't rewrite it).
- **음식 소개 = 팟타이** (content/speaking/food_intro.md + food_intro.jpeg, the user's Gemini picture) for Fri 11/6: slide requires -(으)ㄴ · -고 싶다 ·
  -고 · -지만 · 보다 · 중에서 제일 and 5 questions (이름 · 무엇으로 · 언제/어디/누구 · 왜 · 맛). 13 lines in 해요체.
- **기말 발표 11/24 = 쓰고 발표하기 「여러분이 여행한 곳」** (handout source/speaking/KMU speaking final presentation unit 23 - 37.pdf: 16-question table + a
  합니다체 speech like its 제주도 <보기>). Topic = the user's Aug 2026 Chengdu trip → content/speaking/travel_chengdu.md (script + slide-by-slide plan in ONE file since 11/15; the real deck = `python3 scripts/build_chengdu_deck.py` → output/6_Speaking/KMU_Speaking_TravelChengdu_Deck.pdf from content/speaking/travel_chengdu_img/NNx_*.jpg (NN = slide); `python3 scripts/wongoji.py <name>` lays a script on the 발표 (2) 원고지 (20 cells × front 14 + back 16 rows = 600 cells, ONE sheet, for 11/24) → `<name>_wongoji_N.png`, rerun after editing; slides 3 + 8 lost their keyword chips 11/16 (teacher; pictures fill the band); cut 11/15 to 24 lines = exactly 30 rows ≈ 4–4.7 min — no room to add words, §❔ lists
  the guessed parts). The teacher said a self-introduction should not talk about family; not every sentence has to be formal.

## 8. Working rules
- **Checking homework from photos:** rotate with PIL `ImageOps.exif_transpose` + `rotate(90, expand=True)`, crop and zoom (2–3×); say when the
  handwriting is ambiguous instead of asserting. No paid OCR (the user declined HandwritingOCR).
- **Agents:** Fable/Opus plans; Sonnet agents transcribe and write predictions from a brief that names sources, format and the user's slips.
  Judge a stalled agent by `git status` / file mtimes, not by its output file. Agents must not run build_mockweb.py or publish.
- **Git:** remote origin = github.com/beamkeerati/KMU_Korean (main). Commit only when the user asks. **Never add a Co-Authored-By / Claude
  attribution line.** extracted/, the lecture-photo PDF, source/audio/ and .vscode/ are git-ignored.
- **Plugins:** only free, local ones. `pdf-viewer` enabled; `document-skills` and `diagram-design` allowed. Paid (`handwritingocr`, `extend`,
  `pdfbolt`, `pandadoc`) and unrelated plugins stay disabled — disable both the local and the `@synced` copy. Don't suggest re-enabling.
- **Environment:** Linux; `setlocale` warnings are harmless; the Write tool turns `　` into the literal character.
- **Keep this file short:** a new fact goes here only if every future session needs it; logs, per-item details and history go to docs/.
