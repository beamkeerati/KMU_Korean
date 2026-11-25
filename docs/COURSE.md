# Course facts, grammar map and presentations

*Moved verbatim from CLAUDE.md on 2026-11-04 to keep the always-loaded file small. Section numbers are the old CLAUDE.md numbers. Add new long logs here, not in CLAUDE.md.*

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
  ③ (sat 11/6, 22–29과): **score slip 11/10: 말하기 10.0 · 쓰기 8.9 · 듣기 9.0 · 읽기 10.0 = 37.9/40** (the class-key marking had 쓰기 90/100;
  the official 89 took one more point, item unknown). Slip: source/miniexam/KMU mini exam 03 score unit 22 - 29.pdf.
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
  themselves. 기말 발표 2026-11-24, topic announced 11/10: 「쓰고 발표하기」 — 1. 여러분이 여행한 곳은 어디예요? = a 16-question table in 6 groups
  (어떤 곳 · 날씨/경치 · 유명 · 있어요 / 언제 · 누구와 · 어떻게 · 얼마나 / 했어요 · 좋았어요 · 힘들었어요 / 음식 · 맛 / 쇼핑 · 샀어요 · 왜 / 그곳 · 여행) with
  the teacher's 제주도 column; 2. [보기]와 같이 쓰세요 = a 합니다체 speech (발표 시작 · 내용 · 마무리). The user's topic: Chengdu, Aug 2026, 3 days, with a
  Thai 선배 met on the trip, BKK→CTU 3 h by plane, bikes in town + subway when far (fast), malls (Global Center · SKP fake bamboo · IFS · Taikoo Li),
  철상사 · 무후사 · 콴자이샹즈 street food · 안순교 · 인민공원 marriage market, 훠궈 + spicy noodles, bought nothing, never saw a panda.
  Script content/speaking/travel_chengdu.md → output/6_Speaking/KMU_Speaking_TravelChengdu.pdf.
- 쓰기(1) essay (200-cell manuscript paper, 2026-10-10): teacher's fixes were 에 after time words, 한국어
  spelling, cutting a repeated 국민대학교, 오늘 날씨 → 한국 날씨, and she added 한국 생활이 재미있어요 as a closer.
  쓰기② (일기, diary) is due in class 2026-10-13 — workbook 17과 ex.5 is the same task; a model diary was
  given in chat.

## 기말 format as announced 11/19 (총복습)
- 11/20: 3 hours in the order 쓰기 → 듣기 → 읽기. 쓰기 = 50 minutes and includes a composition of about 300 characters whose topic comes from the
  class 쓰기 (3) (좋아하는 계절 / 고향의 날씨) or 쓰기 (4) (취미 소개) — the question frames are the boxes on review handout p.15. 듣기 = all multiple choice.
  읽기 format not announced. Review 복습시험④ (vocabulary and task types). Memorise 대화 32-1 and 37-1. Picture description from textbook 245쪽 연습 2
  (-지 마세요 signs), 263쪽 연습 2 (보다), 271쪽 연습 3 (오후 vs 밤, -아/어졌어요).
- 11/23 말하기: everything on review handout pp.14–16 (19 questions · subway routes · hamburger shop · 계절/취미 소개 · p.16 식사 예절), pictures and questions.

## Level 1 result (2026-11-24)
- 1급 성적표: 과목 평균 말하기 90.3 · 듣기 89.0 · 쓰기 91.3 · 읽기 94.4 · 평균 91.2 → **진급 2급**; 출석 100 % (개근상). Every skill passed the ≥ 70 rule with
  20+ points to spare. Next term (2급) starts **Mon 2026-12-14**. Full table → docs/STATUS.md "Level 1 result".

## 기말 lead-up notes (moved out of CLAUDE.md §1 on 2026-11-25, verbatim)
- **Dates still ahead:** 11/19 총복습 (no new unit; a 37과 매일시험 is unconfirmed) · 기말 **11/20** (쓰기·듣기·읽기; analysis = content/predictions/final/final02.md) / **11/23** (말하기) · 기말 발표 11/24 (topic announced 11/10). (The handout's 10/20 for 기말 was corrected to 11/20 by the teacher.) 복습시험③ was sat 11/6, ④ (30–37과) 11/18. **Teacher after ④: its ข้อ 6 type
  (두 문장 → 한 문장 with a 보기 of 4 grammar points, connectors + -(으)ㄹ/-는/-(으)ㄴ + N mixed) WILL be on the 기말** — drill sets final-combine + 복습문제 §3/§5.
  **총복습 11/19 hints:** 3 h, 쓰기 (50 min, includes a ~300-자 composition on the 쓰기 (3) 계절 or 쓰기 (4) 취미 topic — source/writing/) → 듣기 (all
  multiple choice) → 읽기; review ④ (words + task types); memorise 대화 32-1 + 37-1; picture description from textbook 245쪽 연습 2 · 263쪽 연습 2 ·
  271쪽 연습 3; 말하기 11/23 = review handout pp.14–16 (p.16 식사 예절 new). Pack = content/predictions/final/final03.md + site sets final_0_hints.json.
