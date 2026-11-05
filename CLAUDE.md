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
- **Dates still ahead:** 복습시험③ **Fri 2026-11-06** (22–29과, also a 말하기 = 음식 소개 speech) · 낭독시험 ⑥ 11/6 · ⑦ 11/12 (31과) · ⑧ 11/18 · 복습시험④ 11/18 (30–37과) · 기말 **11/20** (쓰기·듣기·읽기) / **11/23** (말하기) · 기말 발표 11/24 (topic announced 11/10). (The handout's 10/20 for 기말 was corrected to 11/20 by the teacher.)
- **Pass rule:** every skill's average of 중간 + 기말 ≥ 70; < 60 = fail; 60–69 may re-test. Each skill /100 = 시험 50 + 복습시험 20 + coursework 30 (per term). Details → docs/COURSE.md.
- **Results so far:** 중간 말하기 41.2 · 듣기 42.0 · 쓰기 45.5 · 읽기 49.0 (/50). 복습시험①+② 말하기 20 · 쓰기 16.3 · 듣기 16.0 · 읽기 19.0 (/20). Weakest: 말하기, 듣기. 매일시험 average ≈ 7.5/10; the losses are **word recall**, not grammar.
- 복습시험 (user says "mini exam") = 말하기 interview + 쓰기 (several short sections) + 듣기 + 읽기 (textbook 읽기 passages lifted almost verbatim). Exams "look like the book": predictions should lift textbook 대화/읽기/연습 nearly verbatim.

### 1.1 Stated preferences (all deliverables)
- Deliverables as **PDF**. Fonts: Thai/Latin = TH Sarabun (installed as Laksaman), Korean = Noto Serif CJK KR; mind maps keep Noto Sans.
- **Book style** for the two guides (contract content/specs/SPEC_book_style.md, checker scripts/book_style_check.py): INTRO box per chapter, lead sentence per section, one Korean example per line with its gloss, no `·`-chains, no bold pseudo-headings.
- Every exercise needs a **Thai translation**; pictures become Thai text `🖼️ …`. Docs need a TOC; each `#`/`##` starts a page.
- Answer keys ordered by question number, one item per line; sentence answers get long ruled lines.
- Wants detail and full coverage; likes deep-dive explanations.
- **Colour by word function** in every PDF (scripts/kotag.py, SPEC content/specs/SPEC_colors.md): n blue · p orange · v green · e purple · q teal · x red · m brown · a grey · dotted underline = honorific; the Thai gloss mirrors the colours. Fix a wrong colour by writing an explicit `{c:…}` tag in content.
- If the user only asks a question ("ถ้ามันถูกอยู่แล้วไม่ต้องแก้ ฉันแค่ถามเฉยๆ"), answer it; do not edit files.
- The user watches the token quota: delegate bulk transcription/writing to Sonnet agents with a strict brief; no multi-agent audits unless asked.

## 2. Layout (one folder per material type at every level; full tree → docs/LAYOUT.md)
```
source/       originals — never modify contents; only move/rename (naming §2.1). The user drops new scans in source/ root → file them.
  textbook/ workbook/ everyday/ miniexam/ review/ vocabulary/ lecture/ syllabus/ midterm/ audio/ (git-ignored mp3s)
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

### 2.3 Practice website (output/2_Practice_Web/)
- Build: `python3 scripts/build_mockweb.py` (reads content/mockweb/*.json; files starting `_` are drafts and ignored; edge-tts clips cached in
  extracted/mockweb_clips/). Validate a set file: `python3 scripts/mockweb_validate.py <file>` — `<보기>` is rejected (write `[보기]`); voice `s` = F/M/T/S.
- **Publish:** Artifact publish, file_path `scripts/mockweb/app.html`, url **https://claude.ai/artifact/14Xbi9kWyQgDryHzk7kuzm**, `files` = only the
  output/2_Practice_Web files that changed (from {data.js, clips.js, clips2.js, clips3.js, clips4.js, vocab.js, vendor.js} + any NEW audio/*.mp3);
  omit `capabilities` (keeps db, sample, user). If refused as "unread", run `Artifact list scope:files` on the url first. Compare file sizes with that
  listing to see what changed. Each clips file must stay < 16 MB (build_mockweb splits word clips over VCLIP_FILES; add a file + `<script>` tag in
  app.html when the build says so). Do not re-enable the artifact watch on your own.
- Current: **v53** — 134 sets · 2,578 items · 924 clips · 1,366 vocab words (vocab.js, Leitner drill, VOCAB_PRIO in build_mockweb.py line ~74).
  **Navigation (v51):** home = hub of tiles (`CATS` in app.html, first match wins, `other` = catch-all) → `#x/<cat>` → daily tests only `#x/daily/<unit>`
  (unit titles = `window.KMU_UNITS`, read from the first line of content/guide/01_units/unitNN.md by build_mockweb.py) → set cover `#<setId>` (back button =
  `parentOf(st)`). A new exam family = a `CATS` entry + its `exam` id in mockweb_validate.py `EXAMS` (+ EXAMS in app.html for the cover title).
- Daily sets: content/mockweb/daily_a.json (05–13) · daily_b.json (14+): `daily-NN-writing` / `daily-NN-listening` (voice T) / `sheet-NN-writing`, each
  with a `group` string like "매일시험 28과 · 4 Nov · 7/10". Predictions: daily_predictNN.json, group "🔮 เก็งข้อสอบ 매일시험 NN과 (…)"; **when the
  test comes back, change it to "เก็ง 매일시험 NN과 · สอบแล้ว D Mon · X/10"** so the board stops pinning it.
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
- Guides, vocab, mind maps, listening sheets, workbook (with the publisher's printed keys) cover **5–37과**. Everyday tests/sheets transcribed for
  5–29; predictions for 17–29 (scorecards on 22–28). The 중간시험 복습문제 key is AI-solved; agents' sample answers are labelled ตัวอย่างตอบ.
- `extracted/everyday/unit05-13/test-N.png` is not unit N — check the page header (`1급 매일 시험_N과`).
- 매일시험 score log (details per item in docs/STATUS.md): 5과 7.5 · 6과 7 · 7과 8 · 8과 9.5 · 9과 5 · 10과 8.5 · 11과 5.7 · 12과 6.2 · 13과 4 · 14과 7.5 ·
  15과 8.5 · 16과 10 · 17과 8 · 18과 10 · 19과 8.5 · 22과 8.5 · 23과 4.5 · 24과 8 · 25과 9 · 26과 5.5 · 27과 7.5 · **28과 7** (B: 피아노 → 칠, 운전 → 할;
  A: could not recall 동물; C: 단풍이 dropped 이).
- Low papers (9과, 13과, 23과, 26과) are the vocabulary-heavy units → recall of words is the chronic loss; the site's daily vocab drill targets it.

## 6. The user's recurring mistakes — top list (every sighting → docs/MISTAKES.md)
Use these when checking work or writing predictions. ★ = has cost marks repeatedly.
- ★ **ㅈ/ㅊ shapes** (9+ tests: 젝/책, 몆/몇, 장마절, 자가/차가, 남차) · ★ **ㅐ/ㅔ** (네 게, 테국, 메워요) · **ㅖ/ㅕ** (여쁘지만, 여뻐서) · 가 written like 기.
- ★ **Object marked with 이/가 instead of 을/를**, esp. inside -는/-(으)ㄴ/-(으)ㄹ 수 phrases (책이 읽는 ×4 on test 27; 시계가 받았어요; 음식를).
- ★ **Vocabulary recall under test conditions** (23과 4.5; 만나고 for 앉고; 요리하세요 for 만드세요 — use the unit's target verb; 동물).
- ★ **Verb choice 하다/타다/치다** (피아노를 할 ✗ → 칠; 운전을 탈 ✗ → 할) — read the printed sentences first; the answer is often on the paper.
- ★ **Dropped 으 / 어** in free production though drill tables are right (받십니다, 씻러, 읽어세요; 맛있서, 재미없서 → 맛있어서).
- -아/어서: no tense before 서 (✗ 왔어서); not before commands/suggestions (-(으)세요, -(으)ㄹ까요, 같이 -아요 ✗ → -(으)니까).
- -는 vs -(으)ㄴ by time words: 지금/자주/요즘 → -는; 어제/지난주 → -(으)ㄴ (지금 배운 ✗). Adjective -(으)ㄴ = present (큰), verb -(으)ㄴ = past (먹은).
- ㄹ-stems: 만들은 ✗ → 만든, 만들아요 ✗ → 만들어요, 머세요 vs 멉니다; ㅂ-irregular is usually right.
- Noun + 이다: 학생였어요 ✗ → 학생이었어요 (also 학생여서 ✗ → 학생이어서); 친구에요 ✗ → 친구예요.
- 보다 comparisons: the noun before 보다 is the loser (reversed winners twice); no stray 이 on the noun inside the 보다 phrase.
- Position words: landmark reversed (A가 B 앞에 = A is in front of B). 한테/한테서/께 direction; places/things take 에/에서, not 한테.
- Answers the wrong question word (언제 → 가족을 만날 거예요); keeps the question's tense and noun when answering.
- Rewrite tasks: copy the second sentence's particles exactly (공원에 → 공원이 ✗) and don't drop words (좀); no doubled particle (음식은 은).
- Spacing: 학생 중에서 · -아/어지다 is one word (추워졌어요) · 갈 거예요 has a space · particles attach.
- Does well: ㅂ니다/습니다, -지 않-, 겠, ㅡ-drop past, special honorific verbs, 에서 for activity places, ㅂ irregular tables.

## 7. Presentations (details → docs/COURSE.md §6c)
- Done: 제 방 · 방학 계획 (10/20) · 자기 소개 (10/21, myself.md — the user edits it by hand; don't rewrite it).
- **음식 소개 = 팟타이** (content/speaking/food_intro.md + food_intro.jpeg, the user's Gemini picture) for Fri 11/6: slide requires -(으)ㄴ · -고 싶다 ·
  -고 · -지만 · 보다 · 중에서 제일 and 5 questions (이름 · 무엇으로 · 언제/어디/누구 · 왜 · 맛). 13 lines in 해요체.
- 기말 발표 11/24 — topic on 11/10. The teacher said a self-introduction should not talk about family; not every sentence has to be formal.

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
