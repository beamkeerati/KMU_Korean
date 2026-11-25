# SPEC_mockweb — exercise data for the practice website (output/web/)

The practice site renders exercise *sets* from JSON files in `content/mockweb/*.json`. Each file holds a list of sets.
`python3 scripts/mockweb_validate.py content/mockweb/<file>.json` must print `OK` before you finish.

## 1. File shape
```json
{ "sets": [ SET, SET, ... ] }
```

## 2. SET
```json
{
  "id": "mini02-writing",            // unique, lowercase-kebab: <exam>-<skill>[-<n>]
  "exam": "mini02",                  // mini02 = 복습시험② 10/20 (14–20과) · mini03 = 복습시험③ 11/6 (22–29과) · review = teacher's 중간시험 복습문제 · midterm = 중간시험 prediction · textbook = tb-listen-* (본문 듣기 over the textbook tracks) · vocab = vocab-* word tests
  "skill": "writing",                // writing | reading | listening | speaking
  "title": "쓰기 · 제1회",            // short, Korean/Thai
  "intro": "คำแนะนำภาษาไทย 1–2 ประโยค", // optional
  "minutes": 30,                     // suggested time limit
  "sections": [ SECTION, ... ]
}
```

## 3. SECTION
```json
{
  "h": "[보기]에서 알맞은 단어를 골라 쓰세요. (각 4점×6=24점)",   // the paper's Korean instruction line, verbatim
  "th": "เลือกคำจาก [보기] มาเติม",                               // Thai instruction
  "box": "와/과 · 도 · 에게/한테 · 부터 · 까지",                  // optional [보기] content, plain text
  "passage": [ {"ko": "…", "th": "…"} ],                        // optional reading text, one entry per sentence or line
  "script":  [ {"s": "F", "who": "마키", "ko": "…", "th": "…"} ], // listening only: what the audio says; s = F (female) | M (male)
  "items": [ ITEM, ... ]
}
```
- `script` lines are spoken by a neural voice. Write numbers and times **in Hangul as they are read** (열 시 이십 분, 만 천오백오십 원,
  삼 층 이백사 호) — never digits — so the voice reads them correctly. `who` is optional (only for dialogues).
- A listening section without a real script (the teacher's paper said "ต้องฟังเสียง") is **left out**.

## 4. ITEM (every item has `n`, `type`, `th`; `pts` defaults to 1; `why` = short Thai reason shown after grading, optional)
| type | fields | graded how |
|:---|:---|:---|
| `mc` | `q` (Korean, blank written `(　)`), `opts`: `[["ko","th"], …]` 2–5 options (th may be ""), `ans`: 0-based index | auto |
| `ox` | `q`, `ans`: `"O"` or `"X"` | auto |
| `blank` | `q` with each blank written `___` (three underscores), `ans`: one list of accepted strings **per blank** (`[["와"],["한테","에게"]]`) | auto (spaces/punctuation ignored; near-miss spelling = half) |
| `write` | `q` (prompt), `model`: list of accepted full answers (first = best), `hint` optional | auto if it matches a model, otherwise the student self-grades ○ △ ✕ against the model |
| `speak` | `q` (the question the teacher asks), `model` (sample answer), `mth` (its Thai), `checks`: `[["regex","Thai label"], …]` 0–3 | mic/typing + regex checks (JS regex syntax, Korean literals, no lookbehind) |

- `n` = the item number as printed ("1", "2-1", "A3"). `th` = Thai translation of the Korean prompt (or 🖼️ picture description in Thai).
- Pictures: keep the Thai description in `pic` (e.g. `"pic": "🖼️ แมวอยู่ใต้โต๊ะ"`) and show the real picture with `"img": "ID"` (or a list)
  on the item — or on the SECTION when one picture serves all its items. IDs come from content/img/*.tsv (scripts/crop_images.py);
  agents never edit these JSON files for pictures: they write content/img/map_<name>.tsv rows (scripts/apply_pic_map.py merges them).
  The site shows the picture above the item, the `pic` text under it (hidden in exam mode). Never put a picture that shows the answer
  (e.g. a model essay) on the question.
- Put the student's word-order / tense traps in `why`.
- A blank whose answer is a choice of two forms (e.g. 일곱 시 반 / 일곱 시 삼십 분) lists both in its accepted list.
- A dialogue item is one item: `q` = `"가: 지금 뭐 해요?\n나: ___"` (use `\n` between lines).
- Ordering (순서를 쓰세요) = `blank` with one blank per position (`ans`: `[["1"],["2"],["6"],…]`), the options listed in `box`.
- A conjugation table row = one `blank` item with several blanks (`"읽다 → -았/었어요 ___ · -(스)ㅂ니다 ___ · -(으)세요 ___"`).

## 5. Rules
- **Plain text only.** Source Markdown carries colour tags like `{n:학생}{p:이}` — strip them to `학생이`. No `**bold**`, no `*italics*`, no HTML.
- Korean exactly as in the source; Thai translation for every Korean prompt, option, passage line and script line.
- Keep every item of the source (except audio-only listening items) — the student wants everything in one place.
- Answers come from the source's `# 정답` / key file. Where the key says "ตอบตามจริง", use `write` with the key's example as `model`
  and `hint` saying it can be personal.
- Points: copy the paper's points when it states them; otherwise 1 per item (0.5 for O/X if the paper says so).
