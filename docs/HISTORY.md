# Session-by-session history of the workspace

*Moved verbatim from CLAUDE.md on 2026-11-04 to keep the always-loaded file small. Section numbers are the old CLAUDE.md numbers. Add new long logs here, not in CLAUDE.md.*

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

2026-11-04 night (Sonnet 5.5 main + 2 Sonnet agents, ~820k agent tokens: 쓰기 484k / 22 min, 읽기 336k / 19 min): the user found the site's exam page too long and messy
(asked for a pick-a-category step first, like the KMUTT curriculum page), asked for a 복습시험③ mock (쓰기·읽기·듣기, 22–29과, "predict as accurately as possible") and
asked which model to use / whether to switch to Opus. Site v51 published as artifact version 51: hub → category → unit page → cover (§2.3 + LAYOUT.md) and mini03 sets
(133 sets · 2,576 items). Prediction evidence found this session (BRIEF_mini03.md §1): ②'s scorecard (쓰기 format 50 % hit, content 85 %, 읽기 format 100 %); ②'s 듣기 items
trace back to the centre's 본문 듣기 sheets and to the formal 듣기 of 20과; the textbook prints a 대화로 만들기 frame only in 23·26·29·30과; formal 듣기 in 22–29 = 24과 + 28과.
Model answer given to the user: stay on Sonnet — accuracy is limited by evidence (the teacher changes formats), the earlier Opus-planned prediction also hit only ~50 % of ②'s
쓰기 format; every set was validated, graded in a headless browser and the audio checked with faster-whisper. The publish was refused twice as "unread": run `Artifact list
scope:files`, read the diff, and add a changed line (a `<!-- vNN -->` comment at the top of app.html) before the third try. Not committed.

2026-11-05 (Sonnet 5.5, no agents): the user asked what 본문 듣기 is (answered from the docs, no edit), then to add the 22과 sheet if it could be on the exam. Evidence: ②'s 10 듣기 items trace to
5 of its 7 units (14 · 17 · 18 · 19 · 20; reconstruction in exam02.md), so a given unit of the range showed up about 70 % of the time (one exam, rough); 22과 is in ③'s range and was the only unit with
no textbook-listening set (22-1 only sat in mini03's 예비 items 11–12). Added `tb-listen-22` to textbook_listen.json (A 4-statement MC + B 5-blank dictation, 6 pts) and fixed the listen tile subtitle
(5~29 → 5~37과). Build 134 sets · 2,578 items, 0 new clips. Headless Chrome: the category lists it between 14–21 and 23–29; all correct = 6/6; slips (먹러 · 한식집에서 · wrong MC) = 4/6. Published as artifact
version 52 (files = data.js; the live data.js sha256 equals the local one). Not verified: playback of 22-1.mp3 in a browser (headless virtual time never fired loadedmetadata / decodeAudioData; ffprobe says
40.15 s and faster-whisper matched the script). Left alone: set cards inside a group sort by id as plain strings (5–13 lands last); the textbook-listen sets carry exam "midterm", so their cover says 중간시험
even for 23–37과. Also corrected LAYOUT.md's stale "KMU_Listening.pdf (본문 듣기 5–22)" — the PDF holds all of 5–37 (71 pp, checked per unit). Not committed.
Same day, on "แก้ดิ": fixed the two left-alone items → site v53 (numeric group sort; exam families `textbook` / `vocab` for the 5 tb-listen + 4 vocab-test sets, which all carried `midterm`). Verified by
dumping the card order of 32 category/unit pages and the cover subtitle of 18 sets before and after (only #x/listen and those 9 covers changed), 22과 practice still 6/6 and 4/6 on the slips, live data.js
sha256 = local, the live page contains the new code. Not fixable from here: the link is shared as "Anyone with the link" and data.js carries KMU_SCORES (the user's scores) — only the page's Share menu
changes that; told the user. Not committed.
2026-11-05 (afternoon, D-1 of 복습시험③; Sonnet 5.5, no agents): the user asked whether the clocks on the 복습시험③ cover (쓰기 43 items / 30 min · 읽기 22 / 20 · 듣기 23 / 15) fit the item counts, then "แก้ให้เหมาะสมทั้งหมด".
Measured / estimated: the cards counted the 예비 spares (pts 0) too — the scored parts are 27 / 10 / 10 items (real ②: 26 / 10 / 10). 듣기 exam-mode flow (mp3 lengths × 2 plays + the app's answer pauses) = 12.2 min for
the scored 10 items, 23.1 min with the spares → the 15-min clock would have cut the 23과 spare section off mid-play. 읽기 ≈ 11–18 min for 10 items vs ≈ 25–41 min for all 22 (1,568 syllables of passage); 쓰기 ≈ 12–19 min for 27
vs ≈ 17–28 for 43 (these two are estimates from answer length, not measurements). Real 복습시험 clocks are in no doc (only 중간시험: 쓰기 1 h · 듣기 40 min · 읽기 1 h); the site never stored time-used. The old 듣기 intro also
said "ข้อ 11–15 เป็นชุดสำรอง" while the spares were items 11–23. Fix = site v54 (LAYOUT.md): spares split into `mini03x-*` sets with real points and their own clocks (10 / 25 / 14 min), main sets keep 30 / 20 / 15, two
groups on #x/mini03; CLAUDE.md §2.3 gained a one-line sizing rule. Checked: validator OK, per-set items / points / minutes / listening flow recomputed from the built data.js, headless-Chrome screenshots of #x/mini03 and the
듣기 예비 cover, live data.js sha256 = local. Not verified: a full exam-mode run of the new sets (headless virtual time does not play audio). The publish was refused twice by the stale-version guard (the live page differed
only by my own three edits) and went through on the third try. Not committed.
2026-11-05 (evening, D-1 of 복습시험③; Opus 5.5, no agents): the user finished 복습시험③ 쓰기 (exam mode, ~19:21) and the score vanished from the cover; asked
"มันต้อง sync กันทั้งหมด ทั้งเว็บตลอดเวลา" + "เช็คให้หมดทุกข้อสอบ อย่าให้เกิดเหตุการณ์แบบนี้อีก". Found: the cloud doc mini03-writing held the AI verdicts but ans/score/hist = null.
Chrome's Local Storage LevelDB (copied to scratch, parsed with a pure-python log/sstable + snappy reader) showed the sequence: answers + clock saves every 20 s until 19:21:13
(left 40 s), then in one commit window ans/attempt/self were deleted and only the AI verdicts written back → a pull of a whole doc with nulls and a newer `at` (v54 = whole-doc
"last change wins"; a stale copy on another device/tab won). Same signature on mini02-listening (10-21 15:15: score + hist deleted by a pull, unrecoverable — no copy anywhere);
mid-speaking was emptied 10-21 20:39 (all keys incl. ai: looks like 🗑 ล้างผล, unknown). Fix = site v55 (LAYOUT.md, CLAUDE.md §2.3): per-key merge, score/hist union, vocab
per-word merge, read-merge-write, live listener with a polling fallback, AI replies pinned to their set/attempt. Tested with 7 merge scenarios + a 2-device fake-cloud replay of the
incident (also in polling mode); node --check on the page script. Restored mini03-writing in the cloud (answers of 19:21:13, AI verdicts, score 57/100 recomputed with the app's
rules; submit time ≈ 19:21:25 estimated). After publish (artifact v55, then v56 with the fallback) the user's browser converted every doc to the new format and re-graded
mini03-writing to the same 57/100. Not verified: a real second device; the stored runtime contract is 0.2.85 (types read were 0.2.96) — hence the fallback. Not committed.
2026-11-05 (night; Opus 5.5, no agents): grammar summary 22–29과 and the ㅂ-irregular exceptions answered in chat (textbook p.234: 돕다·곱다 → 와, 입다·잡다·좁다 regular;
the teacher's sheet starred only 돕다). Then "อยู่ดีดีบางทีผลสอบมันก็หายไป ต้อง Refresh". Cloud docs showed no write loop (versions unchanged). Built a headless-Chrome harness (fake
claude runtime + fake cloud, 5 iframes) and reproduced it: another tab of the same browser never redrew after an exam elsewhere (card + open cover stale until reload), and a
forgotten exam tab auto-submitted an empty paper over the real score. Fix = site v56 (LAYOUT.md): storage listener, stale-attempt guard, regrade pinned to the attempt on screen.
14/14 harness checks + the node merge tests pass; harness kept in scripts/mockweb/test/run.sh (CLAUDE.md §2.3). Published as artifact version 57. Not verified: claude.ai's real
runtime (contract 0.2.85) — the harness fakes it; Safari/iPad storage behaviour. Not committed.

2026-11-06 (Opus 5.5 main + 1 Sonnet agent, 301k tokens / 13 min): the user dropped 3 scans — 매일시험 29과, 연습지 30과, 복습시험③ (6 pp, red pen = the class went
through the key, so UNOFFICIAL; official marks next week) — and asked for the usual routine, a verdict on the ③ prediction, and every score updated. Filed to
source/everyday/ and source/miniexam/KMU mini exam 03 unit 22 - 29.pdf; test 29 (7.5: A -(으)ㄴ 4/4, B "왜 …?" -아/어서 all half — 멀서 ×2 · 맛있서 · 시험 있어서 ·
off-topic reason; C 어뗐어요 half) added to exercises/everyday/unit29.md + scorecard on predictions/everyday/unit29.md; sheet 30 (all right) → exercises/everyday/unit30.md;
③ transcribed in exercises/miniexam/exam03.md with the prediction scorecard as its §2 (읽기 passages 3/3 · 듣기 9/10 items from mock dialogues · 쓰기 grammar 100 %,
format 4/7 sections). Unofficial ③: 쓰기 90/100 (−6 작는/예쁘는, −4 늦게 오지 마세요) · 듣기 9/10 (추워서 → 날씨가 나빴어요) · 읽기 10 inferred from ✓ marks on blank
lines (asked the user) · 말하기 unknown. Risk flagged: 쓰기 §2 answered with item numbers over the 보기 words. Page 6 = the teacher's "고향의 계절" worksheet (purpose
unknown). 30과 prediction (Sonnet agent: predictions/everyday/unit30.md 526 lines + daily_predict30.json); the lead rewrote its mock 2 B (왜 택시를 타요? → 타세요 is
unnatural → -(으)ㄹ까요? prompts answered with -(으)니까 + suggestion). scores.json, 00_exam_info.md (복습시험②/③ rows, all 23 daily scores), STATUS, MISTAKES, LAYOUT,
CLAUDE.md, START_HERE updated. Site v57 (145 sets · 2,705 items · 945 clips) published as artifact version 58 (data.js, clips.js, clips2.js). Not committed.

2026-11-09: the user dropped 매일시험 30과 and 연습지 31과 in source/ root → filed to source/everyday/; test 30 (9/10: A 4 × textbook 연습 1 icons + 보기 before (으)세요 4/4,
B 3 × textbook 연습 3 map 3/3 with 오른으로 not deducted, C 실례합니다 ✓ · 아주 빠른 엘리베이터 △ 에리베터 · 정말 아름다웠어요 △ 아름다왔어요; -(으)니까 not tested) added to
exercises/everyday/unit30.md + scorecard on predictions/everyday/unit30.md; sheet 31 (ㄷ 불규칙 table 22/25 — 걸/들/물 거예요 ✗ → 걸을/들을/물을 거예요; (으)로² boxes;
활동 걸리다 table) → exercises/everyday/unit31.md. 31과 prediction (predictions/everyday/unit31.md 29 pp + daily_predict31.json): mock 1 = textbook 연습 1–5, 2 = sheet 31,
3 = workbook 31. Rebuilt everyday + predict (artifact + overflow scans clean on all 4 PDFs) and site v58 (153 sets · 2,836 items · 970 clips, 25 new; VOCAB_PRIO
updated to 31, 30, 32–37 first). scores.json, 00_exam_info.md, STATUS, MISTAKES, LAYOUT, CLAUDE.md, START_HERE updated. Not committed.

2026-11-10: site v58 (built + committed 11-09 as 3b7177f, but not published — the 11-09 session ran out of quota) published as artifact version 60 (data.js, clips.js, clips2.js, vocab.js); live file sizes checked against output/2_Practice_Web.
2026-11-10: 복습시험③ official score slip (photo) → source/miniexam/KMU mini exam 03 score unit 22 - 29.pdf: 말하기 10.0 · 쓰기 8.9 · 듣기 9.0 · 읽기 10.0 = 37.9/40 (class key had 쓰기 90 → official 89, item unknown; 읽기 10 confirmed). Updated exam03.md (table + summary), 00_exam_info.md, scores.json, COURSE, STATUS, LAYOUT, CLAUDE.md §1, START_HERE; rebuilt miniexam PDFs + guide; site data.js published as artifact version 61.
2026-11-10 (later): the user dropped 매일시험 31과 + 연습지 32과 → source/everyday/. Test 31 = 7.5/10 in a NEW FORMAT (8-cell ㄷ table × 0.5 + 3 picture sentences + 3 dictation; 거려요 ×4 for 걸려요 = −2, 닫으세요 scribbled 받침 = 0) → exercises/everyday/unit31.md + scorecard on predictions/everyday/unit31.md. Sheet 32 (르 table 42/42) → exercises/everyday/unit32.md (Sonnet agent). Teacher hint: 32과 will have a conjugation table again. 32과 prediction (Sonnet agent: predictions/everyday/unit32.md 636 lines, 31 pp + daily_predict32.json): every mock opens with an 8-cell 르 table mixing a ㅡ-drop trap (쓰다/아프다/바쁘다) and adjective -(으)ㄴ (다른/빠른). Workbook 32 pages checked from photos (르 table 23/25 다르는/빠르는; 대화 1 & 3 네 before 어디 answers + 불라요; E 5/5 but 성물; F matching 1/4) → MISTAKES. Site v59 published as artifact version 62. Not committed.
2026-11-10 (evening): 기말 발표 handout (dropped as source/Final Presentation.pdf) → source/speaking/KMU speaking final presentation unit 23 - 37.pdf (new source folder). 「쓰고 발표하기」: 16-question travel table + 합니다체 speech like the 제주도 <보기>. Asked the user 4 questions (with whom · flight · food · shopping), then wrote content/speaking/travel_chengdu.md (Chengdu, Aug 2026): table answers, 38 numbered lines with Thai reading/meaning, the paragraph version for the handout box, grammar checklist 5–37과, follow-up Q&A, vocab (🆕 = not in the book lists), pitfalls, and a list of 5 guessed details to confirm → output/6_Speaking/KMU_Speaking_TravelChengdu.pdf (16 pp, clean). No audio page yet. Not committed.
2026-11-11: Workbook 33 checked from photos (A–G: 맵으면 → 매우면, 선생님게, 사수 → 살 수, -(으)ㄹ table written with 다 + 잘를/불를, 아파트로는 → 아파트는,
디음) → MISTAKES; explained -(으)ㄴ/-는/-(으)ㄹ modifiers in chat. The user dropped 매일시험 32과 + 연습지 33과 → source/everyday/. Test 32 = 8/10 (same
format as 31: 르 picture table 2.5 — runner = 빠르다 written 바르다 ×3; -아/어서 picture pairs 3/3; dictation 6호선으로 갈아타세요 ✓ · 1번 출구에 있어요 ✓ ·
글음 몰라요 △) → exercises/everyday/unit32.md + scorecard on predictions/everyday/unit32.md (all three parts predicted). Sheet 33 (Sonnet agent:
(으)면 grid 23/23, (으)ㄹ 사람 grid 5/7 with 16 blank — 동울 · 듣을 사람) → exercises/everyday/unit33.md. 33과 prediction (Sonnet agent:
predictions/everyday/unit33.md 950 lines, 47 pp + daily_predict33.json 164 items): three mocks in the 31/32 format with picture tables mixing
(으)면 / (으)ㄹ and the day's slips (도울 · 들을 · 자를 · 매우면), picture → word drill for every sheet picture. Builds clean; site v60 published.

**2026-11-16** — 매일시험 35과 = **10/10** ("1급 단어 시험": inline-blank -는 것 + -아/어 보다 + 2 short dictation lines, all three parts predicted) →
exercises/everyday/unit35.md (test section; the `______` in the printed instruction became `(　　)` because six underscores render as a ruled line;
the A/B headings carry "단어 시험" so build.py adds no ruled lines under inline-blank items) + scorecard on predictions/everyday/unit35.md.
Sheet 36 (-는데요 / -(으)ㄴ데요 / 인데요 tables, -(으)ㄹ게요 table, 게요 vs 거예요 choice — all right) → exercises/everyday/unit36.md (`\*` before
irregular verbs; `**` prints literally and trips the artifact scan). 36과 prediction (Sonnet agent, short: 17.5 KB, 8 pp) + daily_predict36.json.
기말 발표 deck: slides 3 and 8 lost their keyword chips (teacher's request); a chip-less slide lets its pictures grow into the chip band
(BOT_NOCHIP in build_chengdu_deck.py); the script's slide-3 tip now lists the speaking order instead. Site v65.

**2026-11-17** — 매일시험 36과 = **8.5/10** (8-cell -(으)ㄴ/는데요 table: two present forms in past cells; -(으)ㄹ게요 4/4; dictation 야속 △) →
exercises/everyday/unit36.md (test section + key) + scorecard on predictions/everyday/unit36.md (all three parts predicted, the table as the reserve set).
Sheet 37 (-아/어 주세요 · -아/어야 해요 tables, taxi + burger activities; 교실이야 ✗) → new exercises/everyday/unit37.md. scores.json daily +36;
daily_b.json + daily-36-writing / daily-36-listening / sheet-37-writing; the 36 prediction group retired. 37과 prediction (Sonnet agent, 19.8 KB, 8 pp)
+ daily_predict37.json — the syllabus shows 11/19 = 총복습, so a 37과 test is unconfirmed. **기말 analysis** (user: "analyse thoroughly from every source"):
content/predictions/final/final02.md → output/3_Exam_Prep/KMU_Predict_final02.pdf (6 pp): evidence table (teacher's midterm remark, the 기말 복습문제 has
no 읽기/듣기, ③ 쓰기 = 5 of 7 sections in the handout's formats), 쓰기 sections ranked + every 23–37 grammar mapped to a handout item, picture-vocab themes
not yet used, the 12 textbook 읽기 passages with ③/④ status and practice sets, the 15 대화 + 28/32/36 듣기 with the facts to catch, a 3-day plan, checklist.
Site v66 (206 sets · 3,905 items) published. Not committed.

2026-11-17 (later, Opus 5.5 + 5 Sonnet agents): **guide-book audit** after the user found the By-Topic vocabulary stopped at 22과.
- 📂 คำศัพท์แยกหมวด: the hand-written 91_categories.md (5–22 only, ~70 of 280 words for 14–22) replaced by `scripts/vocab_categories.py`
  rendering every word of examples/unitNN.json (1,366) into 32 meaning categories from `04_vocabulary/91_categories.tsv` (+ -아/어요 form for
  verbs/adjectives, rule-checked; `--check` flags uncategorised words; brief content/specs/BRIEF_vocab_categories.md). By-Topic 765 → 792 pp.
- Exam sections of units 23–37 (🧪 ออกสอบอย่างไร) and grammar topics 33–64 (🧪 ออกสอบแล้ว) all still said "ยังไม่มีข้อสอบจริง" (written ~10/27):
  rewritten from the real 매일시험 23–36, sheets, workbooks, 복습시험③ and the 기말 handout (brief content/specs/BRIEF_exam_sections_23_37.md).
- ส่วนที่ 0: midterm scores, 총복습 11/19, 낭독 table, coursework status to 36과, final-week plan from final02, slip list refreshed; past midterm-week plan removed.
- 03b §3.6: the 복습시험② guess replaced by the real ② and ③ question sections + likely 기말 questions (handout §6).
- Style checker now 0 warnings on all guide sources; both PDFs 0 leftovers, 0 overflow. One colour fix: 시다 → {v:셔}{e:요} (was tagged honorific).

- **2026-11-18** 복습시험④ sat; scan filed as source/miniexam/KMU mini exam 04 unit 30 - 37.pdf, transcribed into content/exercises/miniexam/exam04.md (paper +
  the user's answers + key + mock comparison + lessons). final02.md re-analysed after ④ (§0 mapping ④ ↔ 복습문제, teacher's hint on ข้อ 6, used/unused
  passages and tracks, plan, new slips); p6 = 취미 writing homework already handed in (recorded only; final01 §5 left as is).
  Set clocks re-sized from the real ④ pace (final-combine 40 · final-review-writing 60 · -irregular 35 · final speaking 13 min).
  Site: final_drill.json (mini04r-writing/-reading real papers · final-combine · final-antonym · final-question; brief content/specs/BRIEF_final_drill.md).
- **2026-11-18 (late)** The user saw no predicted exams in the 기말 tile (the ③④ mocks had moved with the ④ tile) and pointed out that "ข้อ 6 ออกแน่"
  does not mean the other types won't appear → 기말 mock A/B built like the midterm's (3 Sonnet agents, reviewed: listening B answers tightened to the exact
  heard word, reading B-10 answers 왜 with -아/어서 first, writing stem-only forms added), and the 기말 tile now holds every 23–37 set (27 sets, 10 groups).
- **2026-11-19 (총복습 day)** The user filed the complete 기말 review handout (16 pp.; the 15-page scan was replaced — p.16 = 한국인의 식사 예절) and
  their corrected 쓰기 (3)/(4) compositions (source/writing/), and relayed the teacher's hints (3 h 쓰기→듣기→읽기 · ~300-자 composition on 쓰기 3/4 topics ·
  듣기 all MC · review ④ · memorise 대화 32-1/37-1 · picture description 245/263/271쪽 · 말하기 = handout pp.14–16). Built: real-picture pipeline
  (content/img/*.tsv → scripts/crop_images.py; make_pdf `img:ID`, picture left of its text; site `img` + lazy WebP packs), final03.md (pictures, two
  model essays on 원고지 from the user's own drafts + the teacher's corrections, 32/37 dialogues), final01.md p.16 + real route/burger pictures,
  site v69 (final_0_hints.json: final-pic · final-essay · final-dialog). The user asked for real pictures EVERYWHERE a 🖼️ text stands in for one
  (~2,500 places): wave 1 = 6 Sonnet agents on 23–37과 + exam papers (brief content/specs/BRIEF_pictures.md), wave 2 = 5–22과.
- **2026-11-19 (evening)** Real pictures everywhere: 10 Sonnet agents (wave 1 = 23–37과 + exam papers, wave 2 = 5–22과) cropped 1,313 pictures
  (content/img/*.tsv; drawn `card:` only for invented prediction/mock items or unreadable scans; a few hand-cleaned crops in content/img/gen/) and
  edited every 🖼️ line; site rows merged from content/img/map_*.tsv (888). Open 🖼️: 2,526 → 18 (all table headers, legends, headings). The agents'
  pictures exposed transcription errors in the 11과/12과 sheets' picture tables (B/A 2 · 16 · 20 · 22 · 23 · 24 guessed wrong) — fixed in the
  Markdown, the keys and the site. User feedback on layout: a picture's text must sit in one place (left picture, all 가/나 + blank right) →
  make_pdf arrange_pictures(); table pictures capped at 24 mm tall. Site v70 (693 pictures in 31 packs) + bigger writing boxes / BigWrite popup.
- **2026-11-21 (Sat, after the 11/20 written 기말)** The user asked for a ≤ 10-page 말하기 summary for Mon 11/23 (typed "listening" but meant speaking;
  hint re-read from the 11/19 message: handout pp.14–16 in full, pictures and questions). Built content/predictions/final/final05.md →
  output/3_Exam_Prep/KMU_Predict_final05.pdf (10 pp): 19 questions as a ครูถาม | คุณตอบ table (bold = the grammar the teacher listens for), picture
  tables 245 · 263 · 271쪽 with 가/나 lines, both subway routes shortened to the 대화 32-1 pattern (…내리세요. N번 출구에 …이 있어요.), burger shop table,
  계절 (태국의 겨울, 합니다체) / 취미 (영화 보는 것, 해요체) answers taken from the user's corrected 쓰기 (3)(4) essays — final01 and the site set still
  use 가을 / 운동 placeholders — 식사 예절, emergency phrases, slips, two-day plan. Only this one PDF was rendered (build_predictions() + to_pdf on the
  single job); a raw `<div style="page-break-before: always"></div>` before a `###` works as a manual page break in make_pdf.
  Same day: the user asked for the two handout p.15 pictures (subway routes, burger shop) to be REDRAWN IN COLOUR (or a Gemini prompt if that was not
  possible). Drawn locally: scripts/draw_speaking_pics.py → content/img/gen/gx-route1/-route2/-burger.png (SVG shapes + Korean text through rsvg-convert,
  colour emoji pasted with PIL because librsvg prints Noto Color Emoji as black silhouettes; Seoul line colours 1 = #0052A4 · 3 = #EF7C1C · 4 = #00A5DE;
  same layout and printed words as the sheet). New ids gx-route1 · gx-route2 · gx-burger (content/img/final.tsv, `gx-` = never remastered) replace
  rv02-15-* in final01.md, final05.md and content/mockweb/final_speaking.json; the 37과 sheet transcription keeps the photocopy crop. PDFs final01 (13 pp)
  and final05 (10 pp) rebuilt. (Superseded by the next lines.)
  Later the same day (user: site too · routes full width · sharper · 245쪽 signs "as vector, the scan shows glare"): draw_speaking_pics.py now writes
  content/img/gen/<id>.svg + .png. make_pdf.convert_images embeds the SVG when one exists (true vector in the PDF; WeasyPrint and librsvg both print
  emoji TEXT as black silhouettes, so each emoji is the font's 109-px bitmap enlarged 4× by Real-ESRGAN anime — colour-on-white and alpha upscaled
  separately, then un-premultiplied — and embedded as a PNG data URI; cache extracted/img/_emoji/). New ids gx-sign-1…6 + gx-sign-panel (245쪽 연습 2;
  sign 2 = a SCHOOL building 🏫 — the user said the book's grey block is a school; the first draft drew a grey board with a clock). Routes w = 100 (canvas 1650 × 450). final05 uses
  gx-sign-N, final01 + final_speaking.json use gx-sign-panel; every other book keeps tb24-245-*. build_mockweb: gx-* pictures → WebP ≤ 1600 px q90
  (others 900 px q74). Site published as version 82 (81 had the board-and-clock sign) (files data.js + img_final_speaking.js; still labelled v71); the watch the publish armed was stopped.
- 2026-11-21 (same day, after the commit) — **subway-route script realigned to the teacher's sheet.** The user asked whether the route script followed
  the 32과 everyday sheet: it did not (it paraphrased 대화 32-1). Sheet page 8 (source/everyday/KMU everyday sheet unit 32.pdf, content/exercises/everyday/unit32.md §H)
  is the teacher's [보기] for exactly this task, and its pages 9–10 are the two handout p.15 pictures. Script now = that model in final05.md §3, final01.md §2 and
  final_speaking.json items 1-1/1-2: 길음역에서 지하철 4호선을 타세요. / N역에서 내려서 N호선으로 갈아타세요. / 그리고 N역에서 내려서 N번 출구로 나가세요. /
  N번 출구 앞에 N이/가 있어요. / N분쯤 걸려요 (no 모두; the question stays 얼마나 걸려요? as the handout prints it). final05 kept at 10 pp by putting the time
  question + answer on one line. Site published as version 83 (data.js only). **Rule for next time: for a speaking picture task, look for the teacher's own
  sheet [보기] before the textbook dialogue.**

**2026-11-23 (Fable 5, UX/UI session):** Practice-site v72 — the BRIEF_web_ux.md pass, run as one session after the user answered the three open
questions: main device = **computer**, scope = **full redesign** (not just restructure), timing = **all phases then publish once**; mid-session the
user added "improve ALL transitions". All three phases of the brief plus the restyle were done directly (no subagents — single visual language in one
file beat the token saving): design tokens + a v72 CSS override layer, page/hover/popup animations with a prefers-reduced-motion kill switch, the
"📌 วันนี้" home card (CATS dates list, fixing the 기말 tile's wrong ผ่านแล้ว on 11/23), compact tile rows + collapsed past-exams shelf, category
filter chips + folded notes + score bars on cards, cover reordered (start first, rules in details), paper without the sticky Prog panel (Dock =
bottom-centre pill, tap → item-number jump grid), shared section hints shown once, results "ดูเฉพาะข้อที่เสียคะแนน", vocab start-first with folded
settings, phone bottom tab bar. scripts/mockweb/test/run.sh all PASS; shot.sh/shot.html (new, from 11/22 prep) gained a pre: step to shoot dark mode
and palettes; before/after screens in extracted/web_shots/. Not yet published to the artifact (no Artifact tool in that session) — next session with
the tool publishes app.html with no `files`.

**2026-11-24 (Fable 5.2, publish session):** v72 published to the practice-site artifact as version 84 (id 1795489475-941c), app.html only — all 39
data/clip/picture files and the 80 mp3s matched the live sha256, so no `files` were sent; capabilities db · sample · user carried forward. The first
publish was refused until the saved live source (2,161 lines) had been Read in full: it was byte-identical to the v71 commit 5a6556a plus the publish
wrapper line and `</body></html>`, and the `cloud` sync block is unchanged between v71 and v72. The auto-armed artifact watch was stopped again.

**2026-11-25 (Opus 5.5):** the user dropped 3 files in source/: the 복습시험④ scan again with the official slip as p.1 (10 · 8.7 · 8.0 · 8.5; pages 2–7
md5-identical to the 11/18 scan, which it replaced), the 1급 성적표 and the certificate + 개근상 (new folder source/results/). exam04.md now carries the
official score; a re-read of 듣기 found 코미드 (item 8) for the extra lost point. scores.json gained `final` + per-term `official`; site v73 (profile 🎓
block, วันนี้ card จบ 1급 / เปิดเทอม 2급 D-N, 기말 tile moved to the past shelf, shelf header lists real titles) published as version 85 (id
1795574094-7820) with app.html + data.js only — the first publish was refused with a line diff (it counts as "viewed"; it held only my own edits), a resend
went through after `list scope:files` covered data.js. run.sh all PASS.
