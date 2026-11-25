# BRIEF_predict24 — 매일시험 24과 prediction for Wed 2026-10-28 (+ the 23과 scorecard)

## What happened today (27 Oct) — use all of it
- The 23과 daily test came back **4.5/10** (worst of the term). Transcription with marks: `content/exercises/everyday/unit23.md`
  (test part at the top, key under `# 정답`). Format: A = 4 picture dialogues answered with a ㅂ-irregular adjective in -아/어요,
  B = 4 picture dialogues answered with adjective + (으)ㄴ/는, C = **2** dictation sentences (not 3). Lost: 더려워요, blank 시끄러워요,
  귀워요, 무서 워요 (space), blank 어려운, 영화은 for 재미있는, 사람은 for 사람을. Cause: the student cannot recall vocabulary in the
  exam and cannot conjugate ㅂ adjectives in free production (the sheet tables were all correct the day before).
- The **24과 practice sheet** handed out today: `content/exercises/everyday/unit24.md` — page 1 = -고 싶다 extension dialogue + 8 cue
  words (고향 음식 · 농구 · 커피숍 · 산책 · 영화 · 쇼핑 · 책 · 자전거), page 2 = -(으)세요 / -지 마세요 conjugation table (가다 타다 쓰다
  주다 읽다 앉다 닫다 *돕다 / 가다 타다 읽다 앉다), pages 5–6 = the teacher's own restaurant dialogue (listening fill-in with 13 blanks:
  어때요 · 깨끗하고 · 좋네요 · 맛있는 · 싸요 · 친구하고 · 매운 음식 · 드세요 · 여기요 · 일 · 한 · 넣지 마세요 · 알겠습니다).
- Pattern evidence (CLAUDE.md §2 step 5 and `content/predictions/everyday/unit18.md` §1, `unit22.md` / `unit23.md` scorecards): the sheet
  handed out the day before becomes the grammar section(s) of the test; dictation sentences are verbatim lines from the unit's
  대화 / 읽기·듣기 / 발음 practice / 연습 pattern lists, sometimes a bare phrase; A is picture vocabulary. For 23과 the teacher built
  BOTH grammar sections from the sheet's two grammar points and used picture dialogues — expect the same for 24과:
  A = 4 picture dialogues with -고 싶어요 (what do you want to do/eat), B = 4 items with -(으)세요 / -지 마세요 (very likely the
  textbook's 연습 2 p.245 prohibition signs and 연습 1 p.244 requests), C = 2 dictation sentences.
- Textbook 24과 (pages 242–249): `extracted/textbook/unit24/page-1.png … page-8.png` (300 dpi) and the guide chapter
  `content/guide/01_units/unit24.md` (대화 24-1, 듣기 24-2, 발음 list, 연습 1–3, 활동). Workbook 24과: `extracted/workbook/unit24/wb-1..4.png`.
  Vocabulary: `content/guide/04_vocabulary/unit24.md`. Grammar topics 38 (-고 싶다) and 39 (-(으)세요) in `content/guide/02_grammar/`.
- Tomorrow is also 낭독시험 ⑤ (read-aloud of 23과) — mention it in the plan line but the prediction is the 24과 daily test.

## Deliverables
1. `content/predictions/everyday/unit24.md` — same structure as `unit23.md` (read it first): title line, IMPORTANT box (this is a guess;
   teacher hint if any), §1 evidence table + predicted format table, §2 what to memorise before bed (dictation candidates ranked ★★★/★★☆/★☆☆
   with Thai and source page — include the sheet's restaurant dialogue lines 김치찌개 일 인분하고 비빔밥 한 그릇 주세요 / 비빔밥에 고기는 넣지
   마세요 / 저는 매운 음식을 먹고 싶어요 and the textbook's 불고기 2인분하고 냉면 한 그릇 주세요 / 전 냉면을 먹고 싶어요 / 손님, 뭘 드시겠어요? /
   the 연습 sentences / the 발음 words 북한산 넣지 먹지 마세요 지각하다 싫어합니다), the -고 싶다 and -(으)세요/-지 마세요 tables with the
   student's known traps (dropping 으 after a 받침: 읽세요 ✗ · ㄹ-drop: 만드세요 · 돕다 → 도우세요 · 먹다/마시다/자다/있다 → 드세요/주무세요/계세요 ·
   -고 싶다 vs -고 싶어 하다 · 전 = 저는), §3 three mock tests of exactly the predicted format (10 items each: A 4 · B 4 · C 2) with
   Thai for every Korean line, pictures as 🖼️ Thai descriptions, and `# 정답` with the three keys and one-line reasons.
   Markdown rules: Thai gloss `*(…)*` after every Korean line; blanks `(　　　　)`; no `**` inside items, no `~~`, no HTML.
2. Prepend to `content/predictions/everyday/unit23.md` a scorecard block exactly like the one at the top of `unit22.md`
   (`## ✅ ผลจริงหลังสอบ — ได้ 4.5/10 (สอบ 2026-10-27)` + table real vs predicted per section + lost marks + lesson), followed by `---`.
   Compare against the mock sets in that file honestly (which items/forms were predicted, which were not).
3. `content/mockweb/daily_predict24.json` — the three mocks as practice-site sets, per `specs/SPEC_mockweb.md`
   (example: `content/mockweb/mini02.json`): `predict-24-1-writing`, `predict-24-2-writing`, `predict-24-3-writing` (sections A and B,
   `blank`/`write` items, `pic` = Thai picture description, `why` = reason) and `predict-24-listening` (every dictation candidate of §2 as
   its own section: `script: [{"s":"T","ko":…,"th":…}]` + one `blank` item `q: "___"`, `ans: [[sentence]]`; no digits in `ko` — write
   numbers in Hangul as read, e.g. 이 인분). All sets: `"exam": "daily"`, `"group": "🔮 เก็งข้อสอบ 매일시험 24과 (พุธ 28 ต.ค.)"`,
   `minutes` 10, Thai `intro`. Validate with `python3 scripts/mockweb_validate.py content/mockweb/_daily_predict24.json` on a draft named
   with a leading underscore, then rename to `daily_predict24.json` (other agents build the site concurrently).
Do not run build.py or build_mockweb.py. Report: files + line/item counts + which evidence you weighed most. No content summary.
