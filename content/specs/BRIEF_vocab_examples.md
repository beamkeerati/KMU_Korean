# BRIEF — example sentences for every vocabulary word (practice-site drill) · 2026-11-12

The learner (Thai, Korean level 1, Kookmin University) asked for every word of the site's daily vocabulary drill to carry
"the explanation the 35과 answer had": Thai meaning, English, ONE short Korean example sentence with its Thai translation,
and a short Thai usage note. The site turns each sentence into a fill-in-the-blank question (the sentence with the word
blanked + the Thai translation of the whole sentence + 4 Korean choices) and shows sentence + note after every answer.

## Your job

Fill `note` and `ex` for every word in the files you were given: `content/guide/04_vocabulary/examples/unitNN.json`.
Gold sample (copy its style exactly): `content/guide/04_vocabulary/examples/unit35.json`.

- Do NOT add, delete, reorder or rename words, and do not change `ko` / `th` / `en` / `cat` (they are copied from
  `content/guide/04_vocabulary/unitNN.md`; the checker compares the list).
- Write the file back as JSON with `ensure_ascii=False, indent=1` (use a small Python script, as the gold file was made).
- Run `python3 scripts/vocab_examples_check.py NN …` for your units until every unit prints `OK` with N/N words.
  Read each ⚠ warning and fix it unless the blank really is an irregular stem (듣다 → 들어요, 모르다 → 몰라요).
- Do not edit any other file, do not run build_mockweb.py or build.py, do not publish, do not commit.

## Fields

```json
{"ko": "반지", "th": "แหวน", "en": "ring", "note": "ใส่แหวนใช้ 끼다",
 "ex": [{"ko": "언니가 예쁜 반지를 끼고 있어요.", "th": "พี่สาวใส่แหวนสวยอยู่", "b": "반지"}]}
```

- `ex` — normally ONE sentence. Two only when the word has two clearly different uses (또 = "again" / "and also"; 눈 = eye / snow
  is two separate entries, so no). Each example:
  - `ko` — a natural Korean sentence, 3–10 words, 해요체 (합니다체 or a short 가:/나: line only when that is how the word is used,
    e.g. 처음 뵙겠습니다). Ends with `.` `?` or `!`. Correct spelling and spacing — check irregular forms and particles.
  - `th` — natural Thai translation of the WHOLE sentence (not word by word), so the learner sees the context. No Korean inside.
  - `b` — the blank: the exact substring of `ko` that is the target word **as it appears in the sentence** — conjugated for verbs
    and adjectives (설명해 · 간단해요 · 떠날까요 · 즐거운), WITHOUT the particle for nouns (반지 in 반지를). It must occur exactly once.
    Entries written with optional parts: `상(을) 받다` → b = `상을 받았어요`; `(비가) 오다` → b = the 오다 form only (와요);
    `정류장 [정뉴장]` → the spelling 정류장; `(1)초` → b = the number + counter as written (10초); `노래/이름 부르다` → one of them.
    Pair entries `A · B` → two examples, one per word. A word that is a whole expression (안녕하세요, 감사합니다, 괜찮아요) → b = the expression.
- `note` — Thai, ≤ 70 characters, or `""` when nothing useful. Never repeat the meaning. Good notes (pick the one that helps most):
  the verb that goes with it (ใช้กับ 입다 · ใส่แหวนใช้ 끼다 · เล่นเทนนิสใช้ 치다), how it is read when 받침 changes the sound
  (อ่านว่า 사진작까), a word it is confused with (อย่าสับสนกับ 지난주), an irregular conjugation (ผันแบบ ㅂ ไม่ปกติ: 즐거워요),
  the honorific partner (คำยกย่องคือ 드시다), where/when it is said (ใช้ในห้องเรียนเวลาไม่เข้าใจ), the opposite (ตรงข้ามกับ 도시).

## What a good sentence is

1. **Take it from the course when you can** — the exams lift textbook sentences almost verbatim, so a textbook/workbook sentence is
   the best example. Look in this order: `content/guide/01_units/unitNN.md` (대화, 읽기, 연습 tables, example boxes),
   `content/exercises/workbook/unitNN.md`, `content/exercises/everyday/unitNN.md`. Shorten a long one to ≤ 10 words.
   Picture-theme words (they have `cat`) rarely appear there — write an everyday sentence.
2. **Grammar the learner already has.** Unit NN may only use grammar taught in units ≤ NN. Units 5–13: `docs/COURSE.md` §4;
   later units: the `[!INTRO]` box at the top of each `content/guide/01_units/unitMM.md`. Early units (5–10) = N이에요/예요,
   있어요/없어요, 이/가, 은/는, 을/를, 에, 에서, -아요/어요, 안, 뭐/어디/누구 — keep those sentences very simple.
   Other words in the sentence should be basic (from the same or earlier units).
3. **Context that points to the word.** The blanked sentence + Thai translation must make the target the natural answer:
   `여름에는 더워서 반바지를 입어요.` is good, `반바지를 샀어요.` is weak (any noun fits). Show the typical partner word
   (입다/신다/쓰다/끼다/하다 for clothes, 타다 for vehicles, 치다/하다/타다 for sports, 에 vs 에서 for places).
4. **The word's main meaning** — the one in `th`. If `th` lists two meanings, use the more common one.
5. **Model the right forms of the learner's known slips** (never write the wrong form):
   object particle 을/를 (not 이/가) before a transitive verb · 걸려요 (not 거려요) · ㅈ/ㅊ and ㅐ/ㅔ spelling (책 · 몇 · 네/게) ·
   ㄹ-stems (만든 · 만들어요 · 머니까) · ㅂ irregular (아름다워요, 매우면; only 돕다/곱다 → 와) · 르 irregular (불러요) ·
   ㄷ irregular (걸어요 · 들어요 · 걸을 거예요) · N이에요/예요 (친구예요, 학생이에요) · adjectives take -(으)ㄴ (작은 · 다른) not -는 ·
   no tense before -아/어서 · 보다 marks the loser. Where a word belongs to one of these traps, say so in `note`.
6. Thai: natural spoken Thai; ครับ/ค่ะ only when the Korean is a polite request to someone. Proper names may stay in Thai
   transliteration (คุณบัท, คุณคันโตยะ).

## Report back

Per unit: the checker line, how many sentences came from the textbook/workbook/everyday files vs written by you, and any word
whose meaning in `th` looked wrong (do not change it — list it).
