# Brief — 복습시험③ mock (22–29과) · 쓰기 + 읽기 (2026-11-04)

> **Update 2026-11-05:** the 예비 sections this brief asks for were split out of the timed sets into `mini03x-<skill>` sets (own points and clock) — see docs/LAYOUT.md v54. Keep spares out of a timed set.

The student sits 복습시험③ on **Fri 2026-11-06**, scope **22–29과** (textbook 1-2, units 22–29). Four papers in the real exam: 말하기 (a 음식 소개 speech, NOT in
this mock) · 쓰기 100 (counts /10) · 듣기 10 · 읽기 10. This brief covers the two papers written by agents: **쓰기** (agent W) and **읽기** (agent R).
The lead writes 듣기. Goal = the most accurate prediction possible, so every item must be lifted from, or built on, material the teacher really uses.

## §1 What ① and ② taught us (evidence, do not re-derive)
| Paper | What the real exam did | Consequence for ③ |
|:---|:---|:---|
| 쓰기 | ① had 5 sections, ② had 7 — the **format changes every time** (only 조사 and a picture/time section repeated); the **content** always came from the range's grammar (~85 % of ②'s items were in the prediction) | Main 100 points follow ②'s 7-section skeleton with 22–29 content; the other formats (word-order, question words, theme words) go in as **예비 sections (0 pts)** |
| 읽기 | 3 textbook 읽기 passages turned into 가/나 dialogues with numbered blanks, 1 point each (1–3 · 4–7 · 8–10). ① = 읽기 6-2, 9-2, 13-2 nearly verbatim. Format matched 100 % | The textbook itself prints a "읽은 내용을 대화로 만들어 봅시다" frame in **26과 and 29과** (also 30과) → these two are the top picks; 23-2 is the third (food theme) |
| 듣기 | Items were built on the center's 본문 듣기 dialogues (track X-1) — the sheet's fill-in answers became the exam's answers | the lead writes it |
| Student | lost marks on word recall, spelling (ㅈ/ㅊ, ㅐ/ㅔ), numbers in listening | put these traps into each item's `why` |

The real ② paper is `content/exercises/miniexam/exam02.md` (쓰기 from line ~150, 읽기 ~85–140); ① is `exam01.md`. **Read the 쓰기 part of exam02.md first.**

## §2 Contract (read before writing)
- Format = `content/specs/SPEC_mockweb.md`. Validate with `python3 scripts/mockweb_validate.py <your file>` — it must print `OK` before you report. `exam` is `"mini03"`.
- Write ONLY your own draft file (name starts with `_`, so the build ignores it): W → `content/mockweb/_mini03_writing.json`, R → `content/mockweb/_mini03_reading.json`.
  Do not edit any other file, do not run build_mockweb.py / build.py, do not publish anything.
- Plain text only. Write the box as `[보기]` — never `<보기>` (the validator rejects `<` + `>`). No `**`, no `*italics*`, no `{c:…}` colour tags.
- `n` = the printed number with the section, e.g. `"1-1"`, `"1-2"`, `"2-1"` (section-item). Reserve items: `"예비-1"`.
- Every Korean prompt, option, passage line has a Thai translation (`th`). Pictures do not exist → `"pic": "🖼️ …Thai description…"`.
- A blank in a `blank` item is written `___` (three underscores) and needs one accepted-answer list per blank (list every acceptable spelling/variant, e.g. `["매운"]`, `["갈 수 있어요","갈 수 있습니다"]`).
  A `write` item shows `나: (　　　　　　　　　　).` in `q` and lists 1–4 accepted full answers in `model` (best first); `hint` (Thai) may say which grammar to use.
  Where the answer can be personal ("ตอบตามจริง"), still give 2–3 model answers and say so in `hint`.
- `why` = one short Thai line: the rule + the student's likely slip. `pts` as stated per section.
- Lift real items **nearly verbatim** from the pool and change only what the format needs. Never invent a sentence when the pool has one.
  Korean must be natural and correct; if unsure about a form, use the form printed in the pool and say "ไม่แน่ใจ" in your report.

## §3 The student's recurring slips (bake these into `why` and into distractors)
ㅈ/ㅊ shapes (책/젝, 몇) · ㅐ/ㅔ (네→게, 태국→테국) · object marked with 이/가 instead of 을/를 (esp. inside -는/-(으)ㄴ N phrases) · verb choice 하다/타다/치다
(피아노를 칠, 운전을 할, 자전거를 탈) · dropped 으 / 어 (맛있서 ✗ → 맛있어서; 읽어세요 ✗) · -아/어서: no tense before 서 (✗ 왔어서), no command/suggestion after it ·
-는 vs -(으)ㄴ by time word (지금/자주 → -는, 어제/지난주 → -(으)ㄴ) · ㄹ-stems (만들은 ✗ → 만든; 길다 → 긴) · ㅂ-irregular (맵다 → 매운, 매워요) ·
보다: the noun before 보다 is the LOSER · answers the wrong question word · rewrite tasks: copy the second sentence's particles exactly, don't drop words (좀) ·
spacing: 갈 거예요, 할 수 있어요, 추워졌어요 (one word).

## §4 Agent W — 쓰기 (one set, 100 pts, 30 min)
Set: `id "mini03-writing"`, `exam "mini03"`, `skill "writing"`, `title "쓰기 · 복습시험③"`, `minutes 30`, an `intro` (Thai, ≤ 2 sentences: 22–29과, ทำโดยไม่เปิดหนังสือ, โครงสร้างตาม ②, ระวัง ㅈ/ㅊ ㅐ/ㅔ).
Sections IN THIS ORDER (headers in Korean as in the real paper; `th` = Thai instruction; `pts` per item as shown; the section total is in the header):

| § | `h` (verbatim) | items | type | target (22–29 grammar) | primary pool |
|:--|:---|:--|:--|:--|:--|
| 1 | `[보기]처럼 반대말을 쓰세요. (각 3점×3=9점)` · box `가: 교실이 커요? 나: 아니요, (작아요).` | 3 × 3 pts | `blank` ("가: 이 가방이 가벼워요?\n나: 아니요, ___.") | antonym pairs of the 22–29 vocabulary; **at least two answers are ㅂ-irregular -워요 forms** (무거워요, 어려워요, 추워요, 가까워요…) | vocab sheets, workbook 23·25·26 |
| 2 | `[보기]처럼 바꿔 쓰세요. (각 3점×4=12점)` · box `음식이 매워요. → 매운 음식` | 4 × 3 | `blank` ("날씨가 더워요. → ___ 날씨") | the three modifiers: (1) ㅂ adjective → -(으)ㄴ, (2) 있다/없다 adjective → -는 (맛있는, 재미없는), (3) verb present → -는 (+ a time word 지금/자주/요즘), (4) verb past → -(으)ㄴ with a ㄹ-stem or 으-verb (만든, 먹은) | workbook 23·27·29, 연습지 27·29 |
| 3 | `[보기]처럼 바꿔 쓰세요. (각 3점×3=9점)` · box `여기에 앉다 → 앉지 마세요` | 3 × 3 | `blank` | -지 마세요 (×2) and -고 싶어 하다 (3rd person, ×1: "마키 씨는 냉면을 먹고 싶어 해요") | workbook 24, 연습지 24 |
| 4 | `[보기]에서 알맞은 말을 찾아서 쓰세요. (각 2.5점×4=10점)` · box `보다 · 중에서 · 제일 · 더 · 무슨` (one distractor) | 4 × 2.5 | `blank` | N보다 (+ 더), 중에서 … 제일, 무슨 + N | workbook 22·26·28 |
| 5 | `[보기]에서 문법을 한 번만 골라 대답하세요. (각 4점×3=12점)` · box `-고 싶어요 · -아/어서 · -지만` | 3 × 4 | `write` (dialogue "가: …\n나: (　　　　　　　　　　).") | each of the three used exactly once; the question must make exactly one of them natural | 매일시험 24·25·29, workbook 24·25·29 |
| 6 | `질문에 대답하세요. (각 5점×6=30점)` | 6 × 5 | `write` | six questions from **six different units** of 22–29, units 26–29 each at least once; target grammar spread over: -(으)ㄹ까요? / 무슨 (22) · A-(으)ㄴ N, ㅂ (23) · -고 싶다 / 드시겠어요 (24) · -지만 (25) · N보다 (26) · -아/어지다 / -는 N (27) · 중에서 제일, -(으)ㄹ 수 있다 (28) · -(으)ㄴ N, -아/어서 (29). Style like ②: "가: 어제 왜 학교에 안 왔어요? 나: (　　)."; one may give the start of the answer ("나: 아니요, ___. 쉬어요.") | 연습지 / 매일시험 / workbook speaking-style items |
| 7 | `[보기]처럼 그림을 보고 쓰세요. (*한국어로 쓰세요.) (6점×3=18점)` · box with one worked example | 3 × 6 | `write` + `pic` | (a) an ability table ○/× → "자전거를 탈 수 있어요. 하지만 피아노를 칠 수 없어요." (28과 B) (b) a row of 5 pictures of one category → 중에서 … 제일 좋아해요 (28과 A) (c) two temperatures/places → N보다 더 (26과 C). Use the workbook/daily picture descriptions already in the pool | 매일시험 28, workbook 26·28 |
| 예비 H | `[보기]처럼 문장을 만드세요. (예비 · 점수에 넣지 않음)` · box one example | 3 × 0 | `write` (word order "냉면을 / 싶어요 / 먹고 / 저는") | ①'s format: -고 싶다, 보다, -(으)ㄹ 수 있다 | workbook |
| 예비 I | `[보기]에서 알맞은 말을 골라 쓰세요. (예비 · 점수에 넣지 않음)` · box `무슨 · 어떤 · 어느 · 왜 · 어때요 · 몇` | 5 × 0 | `blank` | question words in 22–29 contexts | workbook 22·23 |
| 예비 J | `그림을 보고 알맞은 단어를 쓰세요. (예비 · 단어 · 점수에 넣지 않음)` | 8 × 0 | `blank` with `pic` | **theme words** (the teacher hinted theme words of 22·26·28): weather (비가 오다, 눈이 오다, 맑다, 흐리다, 따뜻하다, 시원하다…), seasons, fruit, animals, sports; answer in dictionary form, accept the 해요 form too | vocab sheets 22·26·28, 워크북 26 A |

Rules for W: sections 1–7 sum to exactly 100 points (check with a script); 예비 sections have `pts: 0`. Total items ≈ 28 + 16 reserve. Before writing, read in this order:
`exam02.md` 쓰기 part → `content/exercises/everyday/unit22.md … unit29.md` (the REAL 매일시험 + 연습지; items here are the strongest evidence) →
`content/exercises/workbook/unit22.md … unit29.md` (publisher items with printed keys) → `content/guide/04_vocabulary/unit22.md … unit29.md` →
`content/guide/06_quickref_parts/36.md … 48.md` (grammar rules for 23–29; for 22과 grep `(으)ㄹ까요` in `content/guide/06_quickref.md`).
Do NOT read the big `content/guide/01_units/` files or the prediction files unless you need one specific sentence (grep, don't read whole).

## §5 Agent R — 읽기 (one set, 10 pts, 20 min)
Set: `id "mini03-reading"`, `exam "mini03"`, `skill "reading"`, `title "읽기 · 복습시험③"`, `minutes 20`, `intro` (Thai: บทอ่านจริงมักยกจากหนังสือเกือบคำต่อคำ · ตอบเป็นประโยคเต็ม · ตัดประธานออก เปลี่ยน 저는/우리는 ตามบริบท).
Model = `mini02-reading` in `content/mockweb/mini02.json` (same section header, `th`, `passage` as one `{ko, th}` per sentence, items of type `write` with `model` lists).
Sections in order. **Main (1 pt per item, 10 in total):**
1. `다음을 읽으세요. 그리고 대화로 만드세요. (23과 읽기)` — passage = 읽기 23-2 (guide `content/guide/01_units/unit23.md`, section "📖 읽기 23-2"). **Items 1–3.** Frame: a friend asks, the student answers (가/나). 1) which Korean foods the writer likes, 2) what Koreans eat on a hot day (and what it is made of), 3) where they go to eat Korean food / what is there.
2. `… (26과 읽기)` — passage = 읽기 26-2 (the snow diary). **Items 4–7.** Use the textbook's own printed "대화로 만들어 봅시다" frame (투이 ↔ 고향 친구) — it is in unit26.md right after the diary: keep its lines, blank out four answers (what she did after class, how it was, what she will do at the weekend, why the ski area will be fun/crowded…), models = the bold sentences.
3. `… (29과 읽기)` — passage = 읽기 29-2 (보령 머드 축제). **Items 8–10.** Use the textbook's printed frame (바트 ↔ 알렉세이, section "라 — เติมบทสนทนา" in unit29.md) as the question frame; the textbook's `→` answers are the models; pick the three most testable blanks (where he went · what he could do there · why he could not swim) and print the other lines of the frame as plain dialogue.
**Reserve (`pts: 0`, header ends with `· 예비`):** 4. 24과 읽기 (장핑's blog, 습니다체 answers, 3 items) · 5. 25과 읽기 (저녁 식사 초대, 3 items) · 6. 22과 읽기 (KMU 대화방 chat, 3 items) · 7. 27과 읽기 (장마철, 3 items). Number their items 11–25.
Every answer must be a sentence **found in (or a one-word change of) the passage**; give 2–3 accepted variants in `model` (with/without subject, 해요체/합니다체 when the passage is formal), best first.
`why` = what to copy and which ending to use (-았/었어요, -(으)ㄹ 거예요…). Put the Thai gloss of each passage sentence in `th` (reuse the italic Thai in the guide; strip colour tags).
Sources: `content/guide/01_units/unit22.md, unit23.md, unit24.md, unit25.md, unit26.md, unit27.md, unit29.md` — read ONLY the "📖 읽기 NN-2" sections (use grep -n for the heading, then read ~80 lines).

## §6 Report (≤ 150 words)
Files written · validator result · item counts and the W point total · anything uncertain (Korean you doubt, an answer that could be argued) · sources you could not find.
