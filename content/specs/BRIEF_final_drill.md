# BRIEF — practice-site sets after 복습시험④ (for the 기말 Fri 11/20)

Write ONE new file `content/mockweb/final_drill.json` holding 5 sets. Read `content/specs/SPEC_mockweb.md` (schema) and copy the item style of
`content/mockweb/final_review.json` (set `final-review-writing`: fields n / type / q / model[] / th / why / hint; section fields h / th / box).
Validate with `python3 scripts/mockweb_validate.py content/mockweb/final_drill.json` until it prints no error.
**Do NOT run build_mockweb.py, do NOT publish, do NOT edit app.html or any other file.** Report back: set ids, item counts, minutes, validator output.

Rules for all text: Korean in 해요체 unless stated; every item has a Thai `th` translation; `why` = short Thai explanation (one or two clauses,
name the grammar rule and the trap); `model` lists every acceptable answer (2–4 variants where natural); never write `<보기>` (write `[보기]`);
no markdown, no `**`, no colour tags. Use only words from the course (check `content/guide/04_vocabulary/unitNN.md`, 5–37).

The learner's known slips (build traps around them): object marked 이/가 instead of 을/를 (esp. inside modifier phrases: 책을 읽는 ✓ 책이 읽는 ✗);
adjective + -는 (작는 · 예쁘는 · 다르는 ✗ → 작은 · 예쁜 · 다른); -아/어서 followed by a command/suggestion (✗ → -(으)니까); tense before 서 (왔어서 ✗);
ㄹ-stems (만들은 ✗ → 만든 · 멀으니까 ✗ → 머니까 · 만들 음식); ㄷ (듣다 → 들을 · 걷다 → 걸어서); ㅂ (추우니까 · 매우면 · 어려운); 르 (빨라서 · 몰라서);
writing the printed ending again (물어요 보세요 ✗ — write only what goes before the printed part); ignoring a printed particle (학생증이 ___ → 있어야 해요).

## Set 1 · `mini04r-writing` — the real 복습시험④ 쓰기 paper (exam `mini04`, skill writing, minutes 30)
title "쓰기 · 복습시험④ ข้อสอบจริง (18 พ.ย.)". intro: Thai, says this is the real paper transcribed, ⚠️ marks the 6 items lost on the day.
Reproduce the paper verbatim, 7 sections, 25 items. Pictures become Thai text `🖼️ …`. In `why` of the lost items start with
"⚠️ สอบจริงพลาด:" + what was written. Sections (Korean instruction = `h`, Thai = `th`):
1. [보기]처럼 반대말을 쓰세요. (각 2점×3=6점) — box: "다르다 · 느리다 · 내리다 · 어둡다 (예: 같다 ↔ 다르다)" — 1) 타다 ↔ (내리다)
   2) 밝다 ↔ (어둡다) ⚠️ wrote 느리다 3) 빠르다 ↔ (느리다) ⚠️ wrote 어둡다 (the two were swapped).
2. [보기]에서 알맞은 단어를 찾아서 쓰세요. (각 2점×5=10점) — box: 버스 · 배 · 비행기 · 기차 · 택시 — 1) 🖼️ เครื่องบิน (비행기) 2) 🖼️ รถบัส (버스)
   3) 🖼️ รถไฟหัวกระสุน (기차) 4) 🖼️ แท็กซี่ (택시) 5) 🖼️ เรือ (배).
3. 마리아 씨 달력입니다. [보기]에서 고르세요. (각 2점×2=4점) — box: 매일 · 자주 · 거의 안 · 전혀 안 — describe the calendar in Thai: 운동 every
   Mon/Wed/Fri (12 times in the month), 요리 3 times (3rd, 14th, 26th), no 등산 at all. 1) 마리아 씨는 운동을 (자주) 해요. 2) 마리아 씨는 등산을 (전혀 안) 해요.
4. [보기]에서 맞는 말을 찾아서 쓰세요. (각 3점×3=9점) — box: (이)나 · (으)로 · 에서 · 까지 — 1) 가: 집(에서) 학교(까지) 얼마나 걸려요? 나: 30분쯤 걸려요.
   (two blanks → make it one item whose model is "에서, 까지" and accept "에서 까지") 2) 가: 이 근처에 명동역이 있어요? 나: 네, 사거리에서 오른쪽(으로) 가세요.
   3) 가: 점심에 뭘 먹을 거예요? 나: 비빔밥(이나) 김치찌개를 먹을 거예요.
5. 다음 ( )의 단어를 바꿔서 문장을 완성하세요. (각 4점×4=16점) — the blank stands BEFORE a printed ending: 1) 노래를 ___았/었/였어요. (부르다) → 불렀
   2) 비행기가 ___아/어/여요. (빠르다) → 빨라 3) 공원을 ___(으)ㄹ까요? (걷다) → 걸을 4) 친구에게 ___아/어/여 보세요. (묻다) → 물어 ⚠️ wrote 물어요.
   Accept the full word too (불렀어요 · 빨라요 · 걸을까요) except 4 where only 물어 / 물어 보세요 count.
6. [보기]에서 문법을 골라 문장을 완성하세요. (각 5점×4=20점) — box: -거나 · -(으)ㄹ · -아/어/여서² · -(으)니까 — 1) 아기가 자요. / 조용히 하세요.
   → 아기가 자니까 조용히 하세요. 2) 서점에서 책을 사요. / 도서관에서 빌려요. → 서점에서 책을 사거나 도서관에서 빌려요. 3) 어제 떡볶이를 만들었어요. / 먹었어요.
   → 어제 떡볶이를 만들어서 먹었어요. 4) 주말에 영화를 볼 거예요. / 그 영화는 공포 영화예요. → 주말에 볼 영화는 공포 영화예요.
   (hint: the teacher said this section type WILL be on the 기말; 1) is item 3-7 of the 기말 복습문제 verbatim.)
7. ( )의 문법을 사용해서 문장을 완성하세요. (각 5점×7=35점) — 1) 가: 한국어를 잘해요. 그럼 뭐 하고 싶어요? 나: ___ (-(으)면) → 한국어를 잘하면 한국 회사에서
   일하고 싶어요 (accept any 잘하면 + -고 싶어요) ⚠️ left blank 2) 가: 삼계탕을 먹어 봤어요? 나: 아니요, 안 먹어 봤어요. 가: 그럼 한번 ___. 정말 맛있어요.
   (-아/어/여 보다) → 먹어 보세요 3) 가: 여기서 드실 거예요? 포장하실 거예요? 나: ___ (-아/어/여 주세요) → 포장해 주세요 ⚠️ wrote 불고기를 먹어 주세요
   (포장하다 = take away; 드시다 = honorific eat) 4) 가: 취미가 뭐예요? 나: ___ (-는 것) → 등산하는 것이에요 / 제 취미는 … 는 것이에요
   5) 가: 도서관에서 책을 빌리고 싶어요. 나: 그럼 학생증이 ___ (-아/어/여야 하다) → 있어야 해요 ⚠️ wrote 을 가지고 와야 해요 (the printed 이 needs 있다)
   6) 가: 지금 전화할 수 있어요? 나: 아니요, 이따가 ___ (-(으)ㄹ게요) → 전화할게요 7) 가: 우리 내일 만날까요? 나: 미안해요. ___ (-(으)ㄴ/는데요) → 약속이 있는데요.

## Set 2 · `mini04r-reading` — the real 읽기 paper (exam `mini04`, skill reading, minutes 20)
Three passages printed in the paper (put each passage in its section `box`, verbatim), 10 write items; answers = sentences lifted from the passage.
Passage A (items 1–4) — 이리나 씨는 지난 주말에 친구들과 같이 N서울타워에 갔어요. 명동역에서 N서울타워까지 케이블카를 타고 갔어요. N서울타워에는 아주 빠른
엘리베이터가 있었어요. 그 엘리베이터를 타고 전망대로 올라갔어요. 날씨가 더웠지만 손을 잡고 데이트하는 사람들이 많았어요. 저녁에는 N서울타워 안에 있는
식당에서 스파게티를 먹었어요. 그리고 서울 야경도 봤어요. 서울 야경이 정말 아름다웠어요. 다음에는 남자친구하고 같이 가고 싶어요.
Items: 1) 가: 이리나 씨, 지난 주말에 뭐 했어요? → 친구들과 같이 N서울타워에 갔어요. 2) 가: 전망대에 어떻게 올라갔어요? → (아주 빠른) 엘리베이터를 타고 올라갔어요.
3) 가: 거기에서 뭐 했어요? → N서울타워 안에 있는 식당에서 스파게티를 먹었어요. 그리고 서울 야경도 봤어요. (⚠️ สอบจริงได้ครึ่ง: เขียนแค่สปาเกตตี — the next
question asks about 야경, so 야경 belongs here too) 4) 가: 야경이 어땠어요? → 정말 아름다웠어요.
Passage B (items 5–7, 합니다체) — 투이 씨는 영화 보는 것을 좋아합니다. 특히 영화배우 장범준을 좋아해서 장범준이 나오는 영화는 항상 봅니다. 지난주에 친구가 투이 씨에게
영화 표를 줬습니다. 그 표에는 장범준의 이름이 있었습니다. 투이 씨는 너무 기뻐서 그 영화를 보러 갔습니다. 제일 앞자리에 앉아서 영화를 봤습니다. 그런데 영화가
좀 이상했습니다. 장범준의 얼굴은 나오지 않고 목소리만 나왔습니다. 투이 씨는 실망했지만 장범준의 목소리를 열심히 들었습니다. 다음에는 장범준의 얼굴도
나오는 영화를 보고 싶습니다.
Items: 5) 가: 투이 씨, 취미가 뭐예요? → 영화 보는 것이에요. 6) 가: 좋아하는 영화배우가 누구예요? → 장범준이에요. (put the printed follow-up line
"나: 지난주에도 그 영화배우가 나오는 영화를 봤어요. 그런데 좀 실망했어요." into item 7's q) 7) 가: 왜요? → 장범준의 얼굴은 나오지 않고 목소리만 나왔어요.
Passage C (items 8–10) — 마키 씨는 주말에 간토야 씨와 명동에서 쇼핑하고 싶었어요. 그런데 갑자기 고향에 있는 친구한테서 전화가 왔어요. 그 친구는 토요일에 서울에
올 거예요. 한국말을 전혀 몰라서 마키 씨가 서울을 안내해야 해요. 마키 씨는 간토야 씨에게 미안했지만 전화를 해서 약속을 취소했어요. 그리고 주말에 친구하고
같이 여행할 곳을 계획했어요. 맛있는 한국 식당도 예약했어요. 드디어 토요일이 되었어요. 마키 씨는 공항에 가서 친구를 만났어요. 아주 반가웠어요.
Items: 8) 가: 여보세요. 나: 간토야 씨, 저 마키예요. 미안하지만 ___고 싶어요. → (주말) 약속을 취소하 9) 가: 왜요? 무슨 일이 있어요? → 고향에 있는 친구가 토요일에
서울에 올 거예요. 친구가 한국말을 전혀 몰라서 제가 서울을 안내해야 해요. 10) 가: 그래요? ___? 나: 그 친구와 여행도 하고 한국 식당에도 갈 거예요.
→ 그 친구와 뭐 할 거예요? / 주말에 친구하고 뭐 할 거예요? (⚠️ สอบจริงผิดทั้งข้อ — this blank is a QUESTION; read the answer line after it.)

## Set 3 · `final-combine` — ⭐ 쓰기 ข้อ 6 (teacher: this type WILL be on the 기말) (exam `final`, skill writing, minutes 30)
title "쓰기 · ข้อ 6 รวมสองประโยค (ครูย้ำว่าออกแน่)". 6 sections × 4 items = 24 items, real format: h = "[보기]에서 문법을 골라 문장을 완성하세요.",
each section's box = 4 grammar points, each used exactly once in that section, items are "A. / B. →".
Grammar pool (each must appear in at least two sections): -고 · -지만 · -아/어서① (이유) · -아/어서② (순서) · -(으)니까 · -(으)면 · -거나 ·
-(으)ㄹ + N · -(으)ㄴ + N (past verb) · -(으)ㄴ + N (adjective) · -는 + N. Modifier items follow the 복습문제 §5 shape: two sentences sharing a noun →
"주말에 볼 영화는 공포 영화예요" (drop the repeated noun + its particle; keep the object particle 을/를 inside the modifier phrase).
Sentences must come from 23–37과 textbook/workbook language (look at content/guide/02_grammar/36_*.md … 64_*.md examples and
content/exercises/workbook/unit23–37.md). Do NOT reuse the 17 sentences of 복습문제 §3/§5 (already in set final-review-writing) and do not reuse ④'s 4.
Plant at least: 3 command/suggestion items where only -(으)니까 works; 3 adjective modifiers (작은 · 다른 · 어려운 style); 2 ㄹ-stem forms; 1 ㄷ, 1 르, 2 ㅂ forms;
2 modifier items whose noun is an object (음식을 만들어요 / 그 음식은 … → 제가 만든 음식은 …). `why` names the relation (เหตุผล · ลำดับ · เงื่อนไข · ขัดแย้ง ·
เลือก · เพิ่ม · ขยายนาม) and the trap.

## Set 4 · `final-antonym` — 반대말 (exam `final`, skill writing, minutes 10)
title "쓰기 · 반대말 (④ ตอน 1 พลาด 2 ข้อ)". 2 sections × 8 items, real format: h = "[보기]처럼 반대말을 쓰세요.", box lists the 8 answers shuffled + an example
pair. Each section contains at least one easily-swapped pair of adjectives (like 밝다/어둡다 + 빠르다/느리다 in the same section — the learner swapped them).
Use pairs from the course vocabulary only (verify each word in 04_vocabulary): e.g. 밝다–어둡다 · 빠르다–느리다 · 타다–내리다 · 같다–다르다 · 크다–작다 ·
많다–적다 · 길다–짧다 · 비싸다–싸다 · 덥다–춥다 · 가깝다–멀다 · 쉽다–어렵다 · 넓다–좁다 · 무겁다–가볍다 · 뜨겁다–차갑다 · 열다–닫다 · 켜다–끄다 ·
올라가다–내려가다 · 들어가다–나오다 · 입다–벗다 · 주다–받다 · 사다–팔다 · 알다–모르다 · 시작하다–끝나다 · 출발하다–도착하다 · 일찍–늦게.
`th` = both meanings in Thai; `why` = a memory hook in Thai.

## Set 5 · `final-question` — แต่งคำถามจากคำตอบ (읽기 ข้อ 10 type) (exam `final`, skill reading, minutes 15)
title "읽기 · แต่งคำถามให้เข้ากับคำตอบ (④ ข้อ 10 ผิดทั้งข้อ)". 1 section, 10 items: a short 가/나 exchange where 가's line is the blank question and 나's
answer is printed (q = "가: (    )? / 나: <answer>"). Build them on the 23–37과 읽기 passages (content/guide/01_units/unit23.md … unit37.md, 읽기 sections) and
cover 뭐 · 언제 · 어디(에서) · 누구하고 · 왜 · 어떻게 · 얼마나 · 몇 · 무슨 · 어때요; keep the tense of the answer (갈 거예요 → 뭐 할 거예요? · 갔어요 → 어디에 갔어요?).
model = 2–3 acceptable questions; `why` = which word of the answer tells the question word.

Set-level fields for all five: `exam`, `skill`, `title`, `intro` (Thai, 1–2 sentences), `minutes`. Sets 3–5 also get
`"group": "⭐ หลัง 복습시험④ · ครูย้ำข้อ 6 + จุดที่พลาด"`. Sets 1–2 get no group.
