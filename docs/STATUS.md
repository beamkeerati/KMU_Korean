# Content status, provenance caveats and the daily-test score log

*Moved verbatim from CLAUDE.md on 2026-11-04 to keep the always-loaded file small. Section numbers are the old CLAUDE.md numbers. Add new long logs here, not in CLAUDE.md.*

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
  reversed the winner (압둘라 씨가 왕쯔이보다 시험을 잘 봤어요 — 왕쯔이 had 90점).  **26과 test (11/2) = 5.5/10:** A 4 × 보다 picture pairs (1 = workbook C1, 4 = the workbook C 보기 몽골이 한국보다 더 추워요 verbatim) — lost 3: two winners reversed (빵이 우유보다 싸요 · 윤아 집이 가오루 집보다) + the Mongolian flag read as 사우디아라비아; B 4 × -겠- = all four cue cards of textbook 연습 2 pp.264–265 — 패가 고파겠어요 (ㅂ→ㅍ, 고프 + 겠) and 덥겠어요 with 겠 drawn like 첬 got half; C 기온이 영하 40도예요 (대화 26-1) ✓ · 힘들러지만 for 힘들었지만 (읽기 26-2) half. The teacher marks ○ full · △ half · / zero. 27과 sheet (11/2, user's pencil, 4 pink highlights): -아/어지다 picture table 20/21 (아파요 → 아파졌어요; cell 20 = 생겼어요), school afternoon/night = textbook 연습 3 (책을 읽어졌어요 ✗), -는 table 22/24 (팔는 → 파는 · 정소 → 청소). 27과 prediction (Sonnet agent, 280k tokens / 12 min; mock 1 = workbook G/D/E, 2 = sheet, 3 = textbook 연습 + the teacher's slide sentences) + site v48 (114 sets · 2,166 items). **27과 test (11/3) = 7.5/10:** A 4 × -는 "who is who" pictures ([보기] 운동하는 사람이 윤아 씨입니다; same format as sheet 27 p.4 / workbook E) — all four half for 이/가 on the object (책이 읽는 · 주스가 마시는 · 음식이 먹는 · 한국어가 공부하는, copied from the 보기's 사람이); B 4 × -아/어지다 from the afternoon/night picture (textbook 연습 3 p.271 = sheet 27 p.2) 4/4 — the 27 prediction's mock 2 A had all four; C 자주 입는 옷이에요 ✓ (연습 1 p.272 example) · 유즘은 장마절입니다 for 요즘은 장마철입니다 (first line of 읽기 27-2) half. The teacher put the SECOND grammar point in A — the A/B order is not fixed. Sheet 28 (11/3, blank): 중에서 제일 class dialogue + -(으)ㄹ 수 있다/없다 12-cell table → exercises/everyday/unit28.md. 28과 prediction (Sonnet agent, 243k tokens / 9 min; 34 pp; the teacher's hint "28 · 22 · 26 words: colours, fruits, animals, weather, sports, 타다/치다" = the centre's picture-theme sheets 과일/색깔/동물/음식 (22과) · 계절/날씨 (26과) · 운동 (28과), 61 words → set 4 + predict-28-vocab 97 items incl. a 하다/타다/치다 drill; mock 1 = workbook C/F/G, 2 = sheet 28 + hint, 3 = textbook 연습 pp.278–281; set 2/3 ○× picture marks are the agent's choice; it read the guide chapter, not the scans) + site **v49** (122 sets · 2,332 items · 878 clips; daily-27-writing/-listening, sheet-28-writing; predict-27 lost its 🔮; sent data.js, clips.js, clips2.js, vocab.js). **28과 test (11/4) = 7/10:** A 4 picture rows → 저는 [category] 중에서 [item]을/를 제일 좋아해요 — exactly the teacher's hinted categories 동물 · 음식 · 과일 · 운동 (= mock 2 A + set 4); item 1 half (category word not recalled, 동물 pencilled in afterwards); B ○/× table 마키/지훈 × 자전거 · 운전 · 피아노 → 탈/칠/탈/할 수 있어요/없어요 — 6 할 for 피아노 (→ 칠) and 8 탈 for 운전 (→ 할) zero, although the paper itself printed 운전도 할 수 있어요 and 피아노를 칠 수 없어요; C 단풍이 아름다운 가을 (대화 28-1, rank 6 of the prediction list) half for the dropped 이 · 봄에 꽃구경을 해요 (듣기 28-2) ✓. Scorecard at the top of predictions/everyday/unit28.md. Sheet 29 (11/4, user's pencil, 5 pink marks on p.5): -(으)ㄴ picture table 23/23 (17 테니스를 친 on a golf picture — 친 fits both), two-sentence → -(으)ㄴ 9/9 except 만든 음식은 + printed 은, 보기 page mixing -는/-(으)ㄴ 6/7 (지금 배운 → 배우는), -아/어/여서 table 21/23 (도와 without 서 · 맛있서); pp.4/6/7 speaking (blank) → exercises/everyday/unit29.md. 29과 prediction (Sonnet agent, 285k tokens / 12 min; 27 pp; mock 1 = workbook F/D/C, 2 = sheet 29 E + C (A/B swapped on purpose, -는 vs -(으)ㄴ by time words), 3 = textbook 연습 + the teacher's slide ✗ list) + site **v50** (130 sets · 2,488 items · 900 clips; daily-28-writing/-listening, sheet-29-writing, predict-29-1/2/3-writing · -vocab 40 · -listening 20; predict-28 lost its 🔮; sent data.js, clips.js, clips2.js). **29과 test (11/5) = 7.5/10:** A 4 × picture + blank before the noun, verb NOT given ([보기] 어제 본 영화가 재미있었어요 = textbook 연습 1) → 먹은 떡볶이 · 배운 문법 · 찍은 사진 · 만든 케이크 4/4; B 4 × "왜 …?" answered freely with -아/어서 (왜 택시를 탔어요? · 왜 그 식당에 자주 가요? · 왜 늦게까지 도서관에서 공부를 했어요? · 왜 공포 영화를 안 봐요? = sheet 29 F cards + textbook 연습 2, in the prediction only under "ฝึกเพิ่ม") — all four half: 멀서 ×2 and 맛있서 (dropped 어), 시험 있어서 (dropped 이), 영화관이 멀어서 for a horror-film question (→ 무서워서) + 인 봐요; C 영화가 어땠어요? written 어뗐어요 (ㅐ/ㅔ) half · 바다에 다녀왔어요 ✓ (both = words of 대화 29-1, prediction rank 1). Scorecard at the top of predictions/everyday/unit29.md. Sheet 30 (11/5, user's pencil, all right; 오른 쪽 spacing): 이동 vocabulary 10 pictures (나가다 들어가다 내려가다 올라가다 건너다 · 왼쪽 오른쪽 똑바로 사거리 횡단보도) + -(으)니까 table 16/16 (머니까 · 기니까 · 만드니까 · 추우니까 · 주말이니까) → exercises/everyday/unit30.md; no sentence drill and no (으)로 drill on the sheet. 30과 prediction for Mon 11/9 (Sonnet agent). **30과 test (11/9) = 9/10:** tested ONLY (으)로 direction + movement verbs (-(으)니까 did not appear; format = A 4 + B 3 + C 3): A 4 × textbook 연습 1 p.298 pictogram icons + `<보기> 들어가다 나오다 올라가다 내려가다` before a printed `(으)세요` → 안으로 들어가 · 1층으로 내려가 · 밖으로 나오 · 9층으로 올라가 4/4 (wrote the full 들어가세요 etc. into the blank — accepted); B 3 × textbook 연습 3 p.299 map (약국 · 빵집 · 백화점에 어떻게 가요?) → 사거리에서 오른쪽으로 / 왼쪽으로 / 똑바로 가세요 3/3 (item 5 wrote 오른으로, 쪽 missing, not deducted) — mock 3 of the 30과 prediction had all of A and B; C 3 dictation items: 8) 실례합니다 ✓ (대화 30-1) · 9) 아주 빠른 엘리베이터 △ (wrote 에리베터; 읽기 30-2) · 10) 정말 아름다웠어요 △ (wrote 아름다왔어요, ㅂ → 워; 읽기 30-2). Scorecard at the top of predictions/everyday/unit30.md. Sheet 31 (11/9, user's pencil): ㄷ 불규칙 table 22/25 (걷다 · 듣다 · 묻다 · ※닫다 · ※받다 × -(스)ㅂ니다 · -고 · -아/어요 · -(으)세요 · -(으)ㄹ 거예요 — missed the -(으)ㄹ 거예요 column of the three irregulars: 걸 거예요 · 들 거예요 · 물 거예요 ✗ → 걸을 · 들을 · 물을 거예요) + (으)로² reference boxes (transport, *걸어서 가다/오다, languages with pencil note 한국말로 해요, utensils, tools) + 활동 table (학교→대학로 · 서울→부산 · 부산→일본 × 교통수단 · 요금 · 걸리는 시간) → exercises/everyday/unit31.md. 31과 prediction for Tue 11/10. Earlier tests
  5–13 DO carry a red score at the top of each scan (re-read 2026-10-27, CLAUDE.md said otherwise before): 5과 7.5 (the paper is titled 단어 시험) ·
  6과 7 · 7과 8 · 8과 9.5 · 9과 5 · 10과 8.5 · 11과 5.7 · 12과 6.2 · 13과 4. All 19 daily tests so far average 7.57/10 (25과 = 9); the ≤ 5 papers (9과, 13과,
  23과) are the vocabulary-heavy units (position words · dates/places · ㅂ adjectives) — recall of words, not grammar, is the chronic loss. All
  19 are in scores.json `daily`. The 11과 test key was wrong in two places and is fixed (scan re-read 10/27): A1 = 기다려요 (the teacher circled the
  student's answer; the old key said 만나요) and A14 = 가르쳐요 (a teaching scene; the student's 기다려요 was slashed — the old key had copied it).
  **31과 test (11/10) = 7.5/10 — NEW FORMAT** (exercises/everyday/unit31.md): ※ <보기>처럼 맞는 단어를 쓰세요 (각 0.5점) = picture rows 걷다 · 묻다 ·
  닫다 · 받다 (verb not printed) × 습니다 · 아/어요 · 으세요 · 을 거예요 with crossed cells, 8 blanks — 3.5 (6 닫으세요 scribbled 받침 → 0; the regular
  verbs are the trap) · ※ 그림을 보고 문장을 완성하세요 (각 1점) = 서울→제주도 비행기 1시간 · 국민대→서울역 버스 30분 · 기숙사→교실 걸어서 10분
  (blanks 에서 · 까지 · means · 걸려요) — 1.5, half each for 거려요 · dictation 어떻게 가요 ✓ · 얼마나 걸려요 △ (거려요) · 백 미터쯤 똑바로 오세요 ✓.
  The table = sheet 31 page 1; item 9 = the prediction's mock 3 extra (서울 → 제주도 비행기 1시간); all 3 dictation lines were in its list (ranks 1, 3, 12).
  The teacher said the 32과 paper will again have a conjugation table. 32과 sheet (11/10): 르불규칙 형태 연습 42/42 right (exercises/everyday/unit32.md).
  **32과 test (11/11) = 8/10 — same format as 31과** (exercises/everyday/unit32.md): table = picture rows [보기] 모르다 → 몰라요 · 부르다 · 자르다 ·
  빠르다 (runner) × ㅂ니다 · 고 · 아/어요 · 았/었어요 · 니까 — 2.5 (불렀어요 · 부르니까 · 자릅니다 · 잘라요 · 잘랐어요 ✓; the runner read as 바르다 →
  바르고 · 발라요 · 바르니까 all 0: conjugation right, word wrong) · picture pairs with -아/어서 sequence (학교에 가서 한국어를 공부했어요 · 음식을 요리해서
  먹을 거예요 · 케이크를 만들어서 친구한테 선물을 줬어요) 3/3 · dictation 6호선으로 갈아타세요 ✓ · 1번 출구에 있어요 ✓ · 길을 몰라요 △ (글음). All three parts
  were in the prediction (table = sheet 32 page 7; pictures = textbook 연습 1 + sheet p.4 + workbook E; dictation = short tails of 대화 32-1 ranks 1 · 5 · 7,
  with the exit number changed 3 → 1). 33과 sheet (11/11): (으)면 / (으)ㄹ picture grids + 문장 연습 (exercises/everyday/unit33.md).
  **33과 test (11/12) = 8.5/10 — back to the sentence format of 22–30과** (not the 31–32 table): A 4 = match two columns → -(으)면 sentence ([보기] 제주도에 가면
  수영할까요? · 날씨가 좋으면 등산을 해요 · 김치가 매우면 먹지 마세요 · 방학이 되면 아르바이트 할 거예요 · 돈이 있으면 컴퓨터를 사고 싶어요) 3.5 (아르바으트 △) ·
  B 3 = -(으)ㄹ 거예요 → -(으)ㄹ + N (만날 친구 · 먹을 빵 · 할 일, from sheet p.4) 3/3 · C dictation 예약할 수 있어요 △ (예약갈) · 걱정하지 마세요 ✓ · 음료수를
  준비할까요 △ (음료스를). Content all predicted (A = textbook 연습 -(으)면 first exercise; all 3 dictation lines ★★★ from 대화 33-1); format not.
  34과 sheet (11/12): (이)나 / -거나 응답 연습, picture pairs, blank (exercises/everyday/unit34.md).
  **34과 test (11/13) = 8.5/10 — picture pairs + calendar + dictation** (exercises/everyday/unit34.md): A 4 = picture pair → write 나's answer with (이)나 / -거나
  ([보기] 옷이나 모자를 선물 받고 싶어요 · 1 커피나 차를 마실 거예요 · 2 커피숍이나 공원에서 친구를 만나요 · 3 책을 읽거나 영화를 봐요 · 4 운동하거나 친구를 만나요;
  questions 3–4 = sheet 34 p.2 items 2 · 1 verbatim) 3/4 — **자를** for 차를 △ and **젝을** for 책을 △ (ㅈ/ㅊ, 10th + 11th sightings) · B 3 = calendar of 제프리 씨
  (운동 Mon/Wed/Fri × 4 weeks = 12 · 요리 3 · 등산 0) choose from 자주 · 가끔 · 거의 안 · 전혀 안 → 자주 · 거의 안 · 전혀 안, 3/3 (가끔 unused) · C dictation
  주말 잘 보내셨어요 △ (wrote **주말에** — extra 에, circled and struck) · 액션 영화를 좋아해요 ✓ · 집에서 쉬어요 ✓. All three dictation lines = trimmed 대화 34-1 lines
  (prediction ranks 9 · 4/10 · 1/7); the calendar format was not predicted (the frequency words were). The student's pencil note at the top: "Adj, verb 거나 / Noun 이나".
  35과 sheet (11/13): -는 것 table (12 verbs, left blank) + -아/어 보다 table (12 verbs × 봤어요 / 보세요, all 24 cells written, all right incl. 도와 · 들어 · 걸어 · 불러) +
  활동 취미 questions (speaking, blank) (exercises/everyday/unit35.md).
  **35과 test (11/16) = 10/10** — paper titled "1급 단어 시험_35과" (exercises/everyday/unit35.md): A 4 = picture → one inline blank with V-는 것 (영화 보는 것 ·
  사진 찍는 것 · 음식 만드는 것 · 음악 듣는 것) · B 4 = picture → 가/나 dialogue with -아/어 보다, 0.5 per blank (말을 타 봤어요 · 한국 음식을 안 만들어 봤어요 ·
  안 들어 봤어요) + 8 그럼 한번 들어 보세요 (1 pt) · C 2 dictation cut shorter than 대화 35-1 (스포츠 댄스를 배워요 · 어렵지 않아요). All three parts predicted (rank 4 + 5
  dictation; the format was inline blanks, not whole sentences). Third full mark (16과, 18과).
  36과 sheet (11/16): -는데요/-었는데요 verb table (10) · adjective -(으)ㄴ데요 + noun 인데요 table (7) · -(으)ㄹ게요 table (12, incl. 걸을게요 · 도울게요 · 고를게요 ·
  열게요) · -(으)ㄹ게요 vs -(으)ㄹ 거예요 choice (8) — every cell and circle right (exercises/everyday/unit36.md).
- Known cosmetic gaps: 10과 A's third table row (30–10,000) is printed as given reference rather
  than as blanks; `왕쯔이` is transliterated `หวางจิ้ง` where `หวางจื่ออี` is closer.

## 복습시험③ mock (2026-11-04) — provenance
- content/mockweb/mini03_{writing,reading,listening}.json are a PREDICTION (the real paper is unknown until Fri 11/6). Method + evidence = content/specs/BRIEF_mini03.md §1.
- 듣기 plays the real publisher tracks 22-1 · 24-1 · 24-2 · 25-1 · 26-1 · 27-1 · 28-2 · 29-1 and 23-1; their wording was checked with faster-whisper against the scripts
  (24-1 이인분, 26-1 영하 40도, 29-1 날씨가 추워서, 25-1 맛있지만 / 친절한 all match). The O/X and short-answer items of 28-2 and 24-2 are the textbook's own 나/가 questions.
- 읽기 main = 23·26·29과 (26 and 29 use the textbook's printed 대화로 만들기 frames); 쓰기 items are lifted from the workbook / 매일시험 22–29 with the student's past slips in `why`.
  Written by two Sonnet agents; the lead added the -겠- item 5-4 (26과 daily test: 고파겠어요 ✗) and reviewed every item. Grammar coverage 22–29: every point appears at least once.
- **Result (paper sat 2026-11-06, transcribed in content/exercises/miniexam/exam03.md — the prediction scorecard is its section 2, not a separate predictions/ file, because the
  ③ prediction lived on the site, not in a PDF).** Red pen = the class went through the key, so the scores are UNOFFICIAL (official ones due the week of 11/9):
  쓰기 90/100 · 듣기 9/10 · 읽기 10/10 (all ten answer lines carry a red ✓ but 3–10 are blank — ① and ② papers had no written 읽기 answers either; ask the user) · 말하기 unknown.
  **Official slip 11/10: 말하기 10.0 · 쓰기 8.9 · 듣기 9.0 · 읽기 10.0 (37.9/40)** — 읽기 10 confirmed; 쓰기 one point below the class key (item unknown;
  the §2 numbers-over-보기 risk cost at most that point, so the teacher accepted the section).
  - 읽기: passages 3/3 (23 · 29 · 26과, textbook text shortened by the teacher), format 100 %, 6/10 questions were mock items, the 26과 frame was the textbook's printed one.
  - 듣기: 9/10 items from dialogues that are in the mock (6 main set: 26-1, 28-2 ×3, 29-1 ×2; 3 spare set: 22-1, 23-1 ×2); item 2 = the 24과 sheet's restaurant dialogue.
    Items 1–3 = pick the ending heard (갈까요 · 좋네요 · 따뜻해요). Lost: 9 바트 왜 바다에 가지 않았어요? → wrote 날씨가 나빴어요 (heard gist, not 추워서) — mock item 1 verbatim.
  - 쓰기 (7 sections, 10·15·15·15·12·9·24): 1 taste words from a picture + 보기 (달다 맵다 시다 짜다) · 2 weather words from pictures + 보기 · 3 보기 보다/중에서/무슨/어떤/어느 ·
    4 -(으)ㄴ/-는 from (dictionary form) · 5 short paragraph, fill a 보기 verb before a printed ending (아+ㅂ니다, 만들 수, 어려웠, 매웠) · 6 combine two sentences with
    -아/어서/-지만/-고 · 7 answer by filling before a printed ending (칠 · 배가 고프겠 · 깨끗해졌 · 늦게 오지 마세요 · 사고 싶어요 · 갈까요). Every grammar point was in the mock;
    format matched 4/7 sections (63 pts: mock §4/§2/§5/§6); §2 matched only the spare set; §1 and §5 were new; mock §1 antonyms, §3 -지 마세요 transform, §7 picture
    sentences did not come. Lost −6 작는/예쁘는 (adjective + 는; mock 2-1 귀여운 drilled exactly this) and −4 늦게 오지 마세요 (wrote only 오). Risk: §2 answered by writing the
    item numbers over the 보기 words instead of the words in the blanks (accepted in class; 15 pts the teacher may not accept).
  - Lessons for ④ (exam03.md §2): keep 보기 word-choice + 질문에 대답하세요 (the only sections in 2+ papers), put picture → theme-word sections in the MAIN set,
    add a paragraph-fill with irregular verbs (ㄷ 31과, 르 34과), 읽기 = textbook passages with printed 대화로 만들기 frames (30과 has one).
- Page 6 of the scan = the teacher's 4-slide worksheet "고향의 계절" (questions about each season of the hometown, use 22–29 grammar; writing frame "제 고향에는 사계절이
  있습니다 …"). Purpose unknown (speaking topic or 글쓰기 homework); Thailand has 3 seasons, not 4 — worth flagging if the user writes it.
