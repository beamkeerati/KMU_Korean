# BRIEF — audit the MEANINGS of every vocabulary word · 2026-11-13

The learner (Thai, Korean level 1, Kookmin University) found that the site taught **고민 = "ความกังวล ความลำบากใจ / worry, concern"**
while **걱정하다 = "กังวล เป็นห่วง / to worry"** — two different words, one meaning, so the learner could not tell them apart
(고민 = trouble you keep turning over / can't decide what to do; 걱정 = fear that something bad will happen, also for others).
They asked for every meaning to be checked. You audit one slice of the word lists and **report proposed fixes; you edit nothing**.

## Files in your slice

- `content/guide/04_vocabulary/unitNN.md` for your units — tables `| 단어 | ไทย | English |`.
- `content/guide/04_vocabulary/90_themes.md` — only the `#### ◆ … (NN과)` sections whose NN is in your units.
- `content/guide/04_vocabulary/examples/unitNN.json` for your units — `{ko, th, en, cat, note, ex:[{ko, th, b}]}`; `th`/`en` there
  are copies of the md row (report the md row; the fix is copied over by script). Check `note` and each `ex` (Korean sentence +
  its Thai translation).
- Reference: `extracted/vocab_audit/collisions.txt` — Thai/English glosses shared by 2+ different words across ALL units
  (`TH กังวล: 걱정하다 · 고민`). Use it to find overlaps with words outside your slice.
- When the course sense of a word is unclear, `grep -n "<word>" content/guide/01_units/unitNN.md` to see the textbook 대화/읽기
  line — do not read whole unit files.

## What to flag (only these)

| kind | meaning | example |
|:--|:--|:--|
| `W` wrong | the gloss is not a meaning of the word, or not the sense this course uses | a homonym's other sense; wrong English |
| `O` overlap | two different course words get glosses so close that a learner shown the Thai gloss would pick either — and they are NOT used the same way | 고민 / 걱정하다 · 알다 / 모르다 fine, but e.g. 잘하다 vs 좋아하다 if both said "ชอบ" |
| `I` incomplete / misleading | the main meaning is missing or a rare sense comes first; the Thai gloss is the wrong part of speech (verb glossed as a noun: 걱정하다 = ความกังวล ✗); English convention broken: verbs `to …`, adjectives (descriptive verbs) `to be …`, nouns with no `to` | 간단하다 = "simple" → "to be simple" |
| `H` honorific / register | an honorific or humble word glossed like the plain one without saying so | 댁 = บ้าน → "บ้าน (คำยกย่อง)" |
| `T` typo | Thai/English misspelling, garbled or broken characters, Korean head-word misspelt (report only — never change `ko`) | |
| `X` example | in examples/unitNN.json: the Thai translation says something different from the Korean sentence; the sentence uses the word in another sense than the gloss; the `note` is wrong | |

For an overlap, the fix gives EACH word a gloss that shows the difference — keep the plain dictionary meaning first, then a few
words of nuance in brackets. Report both words (each in its own finding, linked by `pair`). True synonyms that the course uses
interchangeably (휴대폰 / 핸드폰) are not overlaps.

**Do not flag** wording you merely prefer, extra synonyms, gloss order, missing ครับ/ค่ะ, or anything that is already right.
A short list of real problems beats a long list of polish. If a slice has no problems, say so.

## Fix style

- `th`: like the existing rows — 1–3 short Thai glosses separated by a space, optional `(…)` nuance; ≤ 45 characters.
- `en`: like the existing rows, ≤ 45 characters, conventions above.
- Gold sample: 고민 → th `เรื่องกลุ้มใจ ความลังเลคิดไม่ตก` · en `worry, trouble (can't decide what to do)`;
  걱정하다 → th `กังวล เป็นห่วง (กลัวเรื่องไม่ดี)` · en `to worry (fear something bad)`.

## Output

Write `extracted/vocab_audit/findings_<SLICE>.json` with Python (`json.dump(..., ensure_ascii=False, indent=1)`), a list of:

```json
{"file": "content/guide/04_vocabulary/unit35.md", "ko": "고민", "kind": "O", "field": "th+en",
 "old": {"th": "ความกังวล ความลำบากใจ", "en": "worry, concern"},
 "new": {"th": "เรื่องกลุ้มใจ ความลังเลคิดไม่ตก", "en": "worry, trouble (can't decide what to do)"},
 "why": "ซ้ำกับ 걱정하다 — 고민 = คิดไม่ตกว่าจะทำยังไง, 걱정 = กลัวเรื่องไม่ดี", "pair": "걱정하다"}
```

- md rows: `field` = `th`, `en` or `th+en`; `old`/`new` = objects with the changed keys; `ko` = the first cell exactly as written.
- examples: `file` = the json path, `field` = `note`, `ex1.th`, `ex1.ko`, `ex2.th` …; `old`/`new` = plain strings. If `ex1.ko`
  changes, also give `ex1.th` and `ex1.b` (b = exact substring of the new sentence, the word as it appears, no particle).
- `why`: Thai, ≤ 80 characters, written for the learner.
- `pair`: the other word of an overlap, else `""`.

Edit no other file. Do not run build.py / build_mockweb.py, do not publish, do not commit.

## Report back

Counts per kind, the 5 most important findings (one line each), and anything you were unsure about (with the word).
