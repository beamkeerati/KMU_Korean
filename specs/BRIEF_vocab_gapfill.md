# BRIEF — vocabulary gap fill from the textbook and workbook (2026-11-01)

## Why
The user (Thai student, KMU Korean level 1) loses most daily-test marks on **word recall**, not grammar. The practice site drills every word of
`content/guide/04_vocabulary/unit05…37.md` + `90_themes.md` (950 words). Those files were built from the language centre's own vocabulary sheets only,
and a measurement on 2026-11-01 (Kiwi lemmatiser over the textbook transcription and the workbook transcription, minus words already on the site)
found a few hundred real course words missing — e.g. 있다 / 없다, the months 일월…십이월, 선물, 빵집, 휴대폰, 계획, 태권도, 중국집, 분위기, 박물관,
설날. The user asked for every word of the textbook and workbook to be on the site. Your job: add the missing words of **your unit range** to the
vocabulary files, with Thai and English glosses.

## Inputs
- **Candidate list for your range** (main input): `<SCRATCH>/vcov/cand_<A|B|C>.md`. One line per lemma:
  `lemma · count · sources (t = textbook, w = workbook) · up to two context lines`. It is grouped by the **first unit (across 5–37)** where the lemma
  appears. It is machine output and noisy: Kiwi misparses (드세다 from 드세요, 스다 from 쓰다 forms), OCR pronunciation spellings from the 발음 tables
  (이르미, 지거비, 짤바), person names, instruction words, half-words. Judge every line; most junk is obvious.
- **The current site word list**: `<SCRATCH>/vcov/site_words.json` (950 strings, exactly as written in the files). Never add a word already there —
  also not under another spelling: `공부(를) 하다` covers 공부하다, `이야기` covers 이야기하다, `있다/없다` would cover both.
- The sources, only when a context line is not enough: the textbook transcription `content/guide/01_units/unitNN.md` (checked against the page images),
  the workbook `content/exercises/workbook/unitNN.md` (+ `unit21_review_5-21.md`, `unit37_review_22-37.md`). Use `grep -n`, read only the lines you
  need. Also take **one quick look per unit** at the 💬 대화 and 📖 읽기/듣기 sections of the unit chapter (`grep -n '^##\|^###' …` to find them) for
  set expressions the lemmatiser cannot see (사진(을) 찍다, 길이 막히다, 배가 고프다 …) and adverbs. Do not read whole chapters — they are 30–60 kB each.

## What to add
- Content words the course teaches or uses in 대화 / 읽기 / 듣기 / 연습 / 활동 and workbook items: nouns, verbs and adjectives in **dictionary form**
  (먹다, 춥다), adverbs (자주, 빨리), set expressions written the way the files already do (`사진(을) 찍다`, `기분이 좋다`). Place names, countries,
  languages and Korean dishes count. Numbers/months: months go in 13과 as 일월 … 십이월 (gloss 유월 and 시월 with "ไม่ใช่ 육월 / 십월").
- **Not**: person names (투이, 카오루, 지영, 소라 …), grammar endings or particles, misparses, pronunciation spellings, a bare noun when only a
  compound is a real word, words of units 1–4 that never appear in 5–37.
- **First unit only.** Add a word in the unit given by the candidate file. For a word you found yourself (not in the candidate file), check where it
  first appears: `grep -l '<word stem>' content/guide/01_units/unit*.md content/exercises/workbook/unit*.md` — if the first unit is outside your range,
  leave it (another agent owns that range). Within your range, never add the same word twice.
- Words that are already a different entry's meaning on the site (e.g. 휴대폰 when 핸드폰 exists) — add only if the course really uses that
  spelling, and say "= 핸드폰" in the Thai gloss.

## Where and how to write it
In each `content/guide/04_vocabulary/unitNN.md` of your range, append at the end of the file (keep everything already there unchanged):

```
#### ศัพท์เพิ่มเติมจากตำราและเวิร์กบุ๊ก (ไม่อยู่ในชีตของศูนย์)

คำต่อไปนี้ใช้ในบทนี้ของตำราหรือเวิร์กบุ๊ก แต่ไม่มีในชีตคำศัพท์ของศูนย์ เรียงจากคำที่พบบ่อยที่สุด

| 단어 | ไทย | English |
|---|---|---|
| 선물 | ของขวัญ | gift, present |
```

- Units 23–37 already end with `#### ศัพท์เพิ่มเติมจากตำรา (ไม่อยู่ในชีตของศูนย์)`: **rename that heading** to the one above, replace its lead sentence
  with the one above, keep its rows and append yours to the same table.
- A unit with nothing to add gets no section.
- Exactly three columns, one word per row, no `|` inside a cell, no `~~`, no `{x:…}` braces, no `<보기>` (write [보기]), no bold.
  Pronunciation in brackets only where it differs from the spelling and the textbook shows it: `정류장 [정뉴장]`.
- Thai gloss: short and natural like the existing rows (2–6 words, alternatives separated by a space; a usage hint in brackets is fine:
  `고프다 | หิว (배가 고프다 = หิวข้าว)`). English: short dictionary gloss, verbs/adjectives as "to …".
- Order inside a unit: most frequent first (the candidate count), then the expressions you found yourself.

**Agent A only (units 5–13)** also adds the instruction words of the exam papers as one theme section at the end of
`content/guide/04_vocabulary/90_themes.md` — the heading format matters, the site's loader parses it:

```
#### ◆ 문제 지시어 — คำในคำสั่งโจทย์ (5과)

คำที่อยู่ในคำสั่งของข้อสอบและแบบฝึกหัด อ่านคำสั่งไม่ออกก็ทำข้อนั้นไม่ได้ จึงรวมไว้ท่องด้วย

| 단어 | ไทย | English |
|---|---|---|
| 보기 | ตัวอย่าง (กล่อง [보기] ในโจทย์) | example |
```

Collect them from the workbook and test headings of all units (보기, 알맞다, 고르다, 완성하다, 밑줄, 연결하다, 반대말, 대답하다, 질문, 문장, 단어, 어휘, 대화, 그림,
다음, 맞다, 틀리다, 동사, 형용사, 명사, 표, 빈칸, 바꾸다, 쓰다 … — skip any already in site_words.json). Agents B and C do not touch 90_themes.md.

## Checks before you finish
1. `cd /home/beamkeerati/Documents/KMU_Korean && python3 -c "import sys; sys.path.insert(0,'scripts'); import build_mockweb as b; v=b.load_vocab(); print(len(v))"`
   — must run without error; the count rises by what all agents added (other agents work in parallel, so it may jump by more than yours).
2. `grep -c '~~\|{[a-zA-Z]:' content/guide/04_vocabulary/unitNN.md` → 0 for your files.
3. Every new row matches `^\| [^|]+ \| [^|]+ \| [^|]* \|$`.
4. Do not build anything else, do not touch other files, do not commit.

## Report (short)
Per unit: number of words added. Total. Words whose meaning or first unit you were unsure of (≤ 15). Any candidate-file pattern that looked like a
real gap the lemmatiser missed.
