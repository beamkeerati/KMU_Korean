# BRIEF — 기말시험 mock exams A + B (2026-11-18 evening, exam Fri 11/20)

The learner (Thai, level 1, Kookmin KLC) sits the 기말 쓰기 · 듣기 · 읽기 on Fri 11/20 (units **23–37**). The midterm got two full mocks per
skill (A = shaped like the teacher's 복습문제 with the words changed, B = shaped like the 복습시험 papers) — see specs/BRIEF_midterm_v2.md.
The 기말 has no mock yet. Build it the same way, as practice-site sets only (no markdown/PDF).

## Evidence (read these, in this order)
1. Teacher before the midterm: "not far from the 복습시험 and the 복습문제 — maybe only the words change". The midterm proved it (88.8 %).
2. **기말 복습문제** (teacher's handout 11/13): content/exercises/review/final02_part1.md (6 sections: §1 [보기] particles · §2 choose the word ·
   §3 combine two sentences with 7 connectors · §4 O-mark the right form · §5 two sentences → noun modifier · §6 complete the dialogue with a
   given grammar) and final02_part2.md (불규칙 정리: ㅡ · ㅂ · ㄹ · ㄷ · 르, tables + sentence fills). Already on the site as sets
   final-review-writing / final-review-irregular in content/mockweb/final_review.json — **do not reuse their sentences; change the words**.
3. **The real 복습시험④ (today, 30–37과)**: content/exercises/miniexam/exam04.md — 쓰기 7 sections (반대말 · picture → transport words ·
   calendar → 자주/전혀 안 · [보기] particles · irregular verb before a printed ending · ⭐ combine two sentences from a [보기] of 4 grammar points
   (connectors AND -(으)ㄹ/-는/-(으)ㄴ + N mixed) · complete a dialogue with the grammar in brackets) · 읽기 3 textbook passages → dialogue (incl. one
   blank that is a QUESTION) · 듣기 = textbook tracks 30-1 31-1 32-1 32-2 36-1 37-1. **The teacher said the ⭐ combine type WILL be on the 기말.**
   ④ was a cut-down 복습문제: §4 ← 복습문제 §1 · §6 ← §3 + §5 (6-1 was 3-7 verbatim) · §7 ← §6.
4. The real 복습시험③ (22–29과): content/exercises/miniexam/exam03.md. Analysis of everything: content/predictions/final/final02.md.
5. Midterm times: 쓰기 1 h · 듣기 40 min · 읽기 1 h (assume the 기말 is the same).

Existing practice sets you must NOT duplicate (read them to avoid repeats): content/mockweb/final_review.json, final_drill.json,
mini03_*.json, mini04_*.json. Reusing a textbook passage or track is fine (the teacher does); reusing a question sentence is not.

## The learner's slips — plant traps on them
Object marked 이/가 instead of 을/를 (also inside modifier phrases) · adjective + -는 (작는 ✗ → 작은; 다른, 빠른, 어려운) · -아/어서 + command/suggestion
(✗ → -(으)니까) · tense before 서 · ㄹ-stems (만든 · 머니까 · 만들 · 사는) · ㄷ (들을 · 걸어서 · 물어) · ㅂ (추우니까 · 매우면 · 도와) · 르 (불러요 · 빨라요 · 몰라요) ·
writing the printed ending again (물어요 + 보세요 ✗) · ignoring a printed particle (학생증이 ___ → 있어야 해요) · 하다/타다/치다 · 포장하다 · antonym pairs
swapped (밝다↔어둡다, 빠르다↔느리다) · in listening: writing a summary instead of the verb actually heard (추워서 · 바꾸다 ≠ 취소하다).

## Common rules
- Schema: specs/SPEC_mockweb.md. Item style: copy final_review.json (write/blank/mc items with q · th · model/ans · why · hint) and
  mini04_*.json (passages, listening sections with `audio` + `script`). Every item has a Thai `th` and a short Thai `why` (rule + trap).
- `exam: "final"`. Group strings (field `group` on the set): A sets `"🎯 ข้อสอบจำลอง 기말 · ชุด A (แบบ 복습문제 ของครู · เปลี่ยนคำ)"`,
  B sets `"🎯 ข้อสอบจำลอง 기말 · ชุด B (แบบ 복습시험 ①–④)"`. Titles like "쓰기 · 기말 ชุด A". intro = 1–2 Thai sentences saying what it mirrors.
- Course vocabulary only (content/guide/04_vocabulary/unitNN.md, 5–37). Korean must be correct — re-check every irregular form and modifier.
- Never write `<보기>` (use `[보기]`); no markdown, no `**`, no colour tags in JSON text.
- **Size the clock** (the site auto-submits at time-up): one-word/choice item ≈ 30 s, sentence item ≈ 110 s (pace of the real ④ paper);
  listening = sum over sections of (2 × track length + 15 s per item) + 3 min; ffprobe the mp3 in output/2_Practice_Web/audio/textbook/.
- Validate: `python3 scripts/mockweb_validate.py <your file>` until OK. **Do NOT run build_mockweb.py, do NOT publish, do NOT touch any other file.**
- Final reply ≤ 200 words: file, set ids, items per section, minutes and how you got them, anything you were unsure of.

## Agent W — content/mockweb/final_1_writing.json
- `final-writing-a` (60 min): 복습문제 shape with new words: §1 [보기] particles (6: (으)로 ×2 · 에서~까지 · 보다 · (이)나 · 중에서) · §2 choose the word (5 mc:
  이따가/아까 · 꼭 · 전혀 · 드디어 · 잠깐만 style adverbs) · §3 combine with 7 connectors -고 · -지만 · -아/어서① · -(으)니까 · -아/어서② · -(으)면 · -거나 (7) ·
  §4 O-mark the right form (8 mc) · §5 two sentences → noun modifier (6) · §6 dialogue with the given grammar (10, endings printed after the blank like the
  handout) · §7 irregular verb before a printed ending (8, all five groups). Keep the total inside 60 min by the pace rule.
- `final-writing-b` (30 min, 100 points like the real ④): 7 sections in ④'s order — 반대말 (3) · picture → theme words with a [보기] (5; a theme NOT used in
  ③④: 28과 sports + 하다/타다/치다, or 30과 movement verbs 나가다/들어가다/올라가다/내려가다/건너다) · calendar → 매일/자주/가끔/거의 안/전혀 안 (2) · [보기]
  particles (3) · irregular before a printed ending (4) · ⭐ combine from a [보기] of 4 grammar points incl. one modifier (4) · dialogue with the grammar
  in brackets (7: -(으)면 · -아/어 보다 · -아/어 주세요 · -는 것 · -아/어야 하다 · -(으)ㄹ게요 · -(으)ㄴ/는데요, new situations). Points per section as ④.

## Agent R — content/mockweb/final_1_reading.json
Passages = the textbook 읽기 of 23–37과 nearly verbatim, as the teacher does. The 12 passages are already transcribed in mini03_reading.json /
mini04_reading.json (main + 예비 sets) and exam03.md / exam04.md — copy their text, do not re-type from memory. Not used on a real paper yet:
**24 · 25 · 27 · 31 · 33 · 35과** — favour these.
- `final-reading-a` (60 min, 25 items): shaped like the 중간 복습문제 읽기 (content/exercises/review/midterm01_part1.md / part2.md: passage-blank
  `(　)에 무엇이 맞아요?` mc · O/X on a passage · short answers · 가/나 dialogue completion · ㉠ refers to what · put events in order), 5–6 passages.
- `final-reading-b` (20 min, 10 items): ④ shape — 3 passages → 가/나 dialogue, 나's blank lifted from the passage; include one blank that is a QUESTION
  (answer printed after it) and one answer that needs two sentences of the passage.

## Agent L — content/mockweb/final_1_listening.json
Real publisher audio only (`"audio": "audio/textbook/NN-N.mp3"`, files in output/2_Practice_Web/audio/textbook/), with the full `script`
(copy dialogue text from content/exercises/listening/unitNN.md and the mini03/mini04 listening JSONs — do not invent lines). Tracks not used on a real
paper yet: **24-1 · 25-1 · 27-1 · 33-1 · 34-1 · 35-1 · 36-2 · 24-2** — use these first; 23-1 and 26-1/28-2 only if needed.
- `final-listening-a` (12 items): shaped like the 중간 복습문제 듣기 (midterm01_part2.md "ฟัง 1…": which word is heard · where · which picture (🖼️ Thai text) · O/X).
- `final-listening-b` (10 items): ④ shape — [1~3] which ending/number/picture · [4~6] O/X · [7~8] short answer · [9~10] short answer with a printed frame
  (`(　　)고 싶어서 전화했어요` style) whose answer is the exact verb heard.
- Minutes for each set from the clock rule (ffprobe); state the numbers in your reply.
