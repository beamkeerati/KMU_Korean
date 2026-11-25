# SPEC_derivations — "สูตรและวิธีทำ" blocks (teacher's whiteboard style) for every formula-type grammar point

Written 2026-10-28 by Fable for the Sonnet agents. Read this whole file before touching anything.

## 0. Why

On 2026-10-28 the teacher taught ㄹ 탈락 on the whiteboard as a numbered procedure, not as a result table:

```
받침 ㄹ
1. ㄹ + (으)          → 으 is crossed out            만들 + (으)러  → 만들러
   ↓
2. ㄹ + ㄴ ㅂ ㅅ 받침ㄹ → the stem's ㄹ is crossed out  만들 + 네요    → 만드네요
                                                      만들 + (으)세요 → 만드세요
                                                      만들 + (으)ㄹ 거예요 → 만들 거예요
```

and on the slide: `받침 ㄹ + ㄴ(-네요) ㅂ(-(스)ㅂ니다) ㅅ(-(으)세요) 받침ㄹ(-(으)ㄹ 거예요 · -(으)ㄹ까요?)` with one verb across every
ending in one line: `놀다 : 노네요 놉니다 노세요 놀 거예요 놀까요? 놀러 가요`, and O/X pairs (`놀세요 X → 노세요`).

The user (a Thai level-1 student who loses marks on *free production* of forms they get right in drill tables — 만들으세요, 읽어세요,
받십니다, 살어요, 산책고, 좋아 안 해요 …) asked: **"ทุกบทที่ต้องใช้สูตร ให้บรรยายให้ชัดเหมือนอาจารย์ เหมือนแสดงวิธีทำทางคณิตศาสตร์"** —
every grammar point that is a formula must show its working step by step, like a math solution: numbered rules, then worked examples
where each column is one step and the reader sees exactly what is cut, added or merged.

The exemplar is already in the repo — copy its shape exactly:

- `content/guide/02_grammar/40_jiman.md` → the four `####` sections starting at `#### สูตรรวมคำ 2 กฎ 3 ขั้น ตามกระดานครู (10/28)`
  (rules table → "ลำดับทำคือ ① ② ③" sentence → worked table with step columns → `> [!TIP] วิธีจำสั้น ๆ` → slide O/X table → one-verb-all-endings strip).
- `content/guide/01_units/unit25.md` → `#### ขั้นตอนรวมคำตามกระดานครู (10/28)` (the compact version inside the unit chapter).

## 1. Deliverable

For every topic in your list (§5) insert **two** blocks:

1. **FULL block** in `content/guide/02_grammar/NN_*.md`, as the LAST `####` sub-section of `### 📌 รูปแบบและเงื่อนไข`
   (i.e. immediately before the next `###` heading, usually `### 📖 ตัวอย่างและการใช้`).
2. **COMPACT block** in `content/guide/01_units/unitUU.md` — only in the unit that OWNS the topic (the `[Unit UU]` tag in
   `content/guide/06_quickref.md`; also listed in §5). Insert it inside the matching `### 📝 ไวยากรณ์: … (ไวยากรณ์ข้อ NN)` section,
   right after that section's first table (or after its lead paragraph if it has no table), as a `####` sub-section.

Do not touch any other section, file, or the PDFs. Fable rebuilds the books.

## 2. Block templates

### 2.1 FULL block (topic file)

```markdown
#### สูตรและวิธีทำ: <ending as the book prints it> (แบบกระดานครู)

<ONE lead sentence: what is combined with what, and what can change.>

| กฎ | เงื่อนไข | ทำอะไร | ทำไม |
|:---|:---|:---|:---|
| **กฎ 1** | … | … | … |
| **กฎ 2** | … | … | … |
(2–4 rules; each rule = one decision the student makes, in the order they make it)

ลำดับทำคือ ① <step 1> ② <step 2> ③ <step 3> ตารางนี้แสดงทุกขั้นกับคำที่ตำราใช้

| ราก + คำต่อ | ① <step name> | ② <step name> | ③ ผล | หมายเหตุ |
|:---|:---|:---|:---|:---|
| 먹 + 어요 | … | … | **먹어요** | … |
(8–14 rows; see §3 for which stem classes MUST appear; bold the part that changed in ③; use ✗ for a wrong form in หมายเหตุ)

> [!TIP] วิธีจำสั้น ๆ
> One or two sentences the student can recite before writing the form.
```

Optional (only when the material gives it): a `#### ผันคำเดียวครบทุกคำต่อ` strip table (one verb per row, one ending per column,
≤ 7 columns) and a `#### รูปผิด / รูปถูก` O/X table built from the user's recorded mistakes (§4).

The number of step columns is whatever the formula needs (2–4), but every row must fill every column — write `ไม่มี` / `ไม่ตัด` /
`ไม่เปลี่ยน` rather than leaving a cell empty, because the point is to show that the step was *considered*.

### 2.2 COMPACT block (unit file)

```markdown
#### แสดงวิธีทำ: <ending> (ย่อ · ตารางเต็มในไวยากรณ์ข้อ NN)

<ONE lead sentence that states the rules in order: "กฎ 1 … กฎ 2 …">

| ราก + คำต่อ | ① … | ② … | ③ ผล |
|:---|:---|:---|:---|
(4–6 rows: the textbook's own verbs of that unit, one per stem class that the unit teaches)
```

### 2.3 SHORT topics

Topics marked SHORT in §5 have no letter-level change (particle choice, word-order rule). They still get both blocks, but the
FULL block has 2–3 rules and 4–8 worked rows (e.g. `학생 + 은/는 → 받침 ○ → 학생은`), and the step columns are the decision
(ดูตัวสะกด / ดูชนิดคำ / ดูตำแหน่ง) and the result.

## 3. Which stem classes must appear (completeness checklist)

Only include a class the course has taught **by that unit** (ㅂ 불규칙 = 23과 · ㄹ 탈락 = 25과 · ㄷ 불규칙 = 31과 · 르 불규칙 = 32과).
A topic taught earlier does not get later irregulars; a topic taught later must include every irregular taught before it.

**A. -아/어/여 family** (06 -아/어요 · 23 -았/었/였- · 43 -아/어지다 · 48/53 -아/어서 · 60 -아/어 보다 · 63 -아/어 주세요 · 64 -아/어야 하다):
rows for ㅏ/ㅗ stem with 받침 (받 + 아 → 받아) · ㅏ stem no 받침 (가 + 아 → 가, the 아 merges) · ㅗ (오 + 아 → 와 · 보 + 아 → 봐) ·
other vowel with 받침 (먹 + 어 → 먹어 · 읽어) · ㅓ no 받침 (서 + 어 → 서) · ㅜ (배우 + 어 → 배워 · 주 + 어 → 줘) · ㅣ (마시 + 어 → 마셔 ·
기다리 + 어 → 기다려) · ㅟ (쉬 + 어 → 쉬어, no merge) · ㅚ (되 + 어 → 돼) · 하 → 해 (공부하 → 공부해, 여 of 여요) · ㅡ drop (바쁘 → 바빠 ·
예쁘 → 예뻐 · 쓰 → 써 · 크 → 커 — the 아/어 is chosen by the vowel BEFORE ㅡ, 쓰 alone → 어) · ㄹ stem keeps ㄹ (살 + 아 → 살아 — the
user wrote 살어요) · and, from 23과 on, ㅂ 불규칙 (덥 + 어 → 더워 · 돕 + 아 → 도와 · 입 + 어 → 입어 regular) · from 31과 ㄷ (듣 + 어 → 들어 ·
닫 + 아 → 닫아 regular) · from 32과 르 (모르 + 아 → 몰라 · 부르 + 어 → 불러 · 다르 + 아 → 달라). For 23: add N이었어요 / N였어요 and
-았/었- + the ending (먹었어요, 갔어요, 했어요 — ✗ 하였어요 is bookish, ✗ 학생였어요). For 20 add 시 + 어요 → 세요 and 셨어요.

**B. (으) family** (20 -(으)세요/-(으)시- · 26 -(으)러 · 28 -(으)ㄹ 거예요 · 33 -(으)ㄹ까요? · 36 -(으)ㄴ · 46 -(으)ㄹ 수 있다 · 47 -(으)ㄴ past ·
50 -(으)니까 · 55 -(으)면 · 56 -(으)ㄹ · 61 -(으)ㄴ/는데요 · 62 -(으)ㄹ게요 · 49/51 (으)로 · 58 (이)나):
rows for no 받침 (가 + (으)세요 → 가세요: 으 ✗) · 받침 (읽 + (으)세요 → 읽으세요: 으 ○ — the user drops it: ✗ 읽세요 · 읽어세요 · 씻러 · 받십니다) ·
ㄹ stem (으 ✗ always; stem ㄹ drops before ㄴ ㅂ ㅅ 받침ㄹ → 만드세요 · 긴 · 살 거예요 · 놀까요?; stays before 러/면/니까 → 만들러 · 살면 · 사니까
⚠ 니까 starts with ㄴ so ㄹ DOES drop: 사니까, 만드니까) · from 23과 ㅂ 불규칙 (덥 + (으)ㄴ → 더운 · 돕 + (으)세요 → 도우세요 · 가깝 + (으)니까 →
가까우니까 · 춥 + (으)면 → 추우면) · from 31과 ㄷ (듣 + (으)세요 → 들으세요 · 걷 + (으)면 → 걸으면) · 있다/없다 with a modifier → 는 (36/44/56/61:
맛있는 · 재미없는 · 있는데요). For particles (49/51/58): ㄹ-final noun takes 로 not 으로 (지하철로 · 연필로), 받침 → 으로 / 이나, none → 로 / 나.

**C. 받침 switch only** (01 은/는 · 02 이에요/예요 · 입니다 · 이/가 아니에요 · 07 을/를 · 19 와/과 · 21 -(스)ㅂ니다/-(스)ㅂ니까? · 30 -네요):
rows for 받침 ○ / ✗ and, for 21 and 30, ㄹ stem (살 → 삽니다 · 멀 → 머네요; ✗ 살습니다 · 만들습니다 — ㄹ counts as NO 받침 for the
ㅂ니다/습니다 choice, then drops). 02: 이에요 vs 예요 by 받침, 입니다 unchanged, 이/가 아니에요 by 받침. 21: question = 까 (✗ 먹습니다 for 먹습니까? —
the user ignored the ?).

**D. Numbers / time** (04 native vs Sino + counters · 25 N시 N분): the 하나 → 한 · 둘 → 두 · 셋 → 세 · 넷 → 네 · 스물 → 스무 cut before a counter
(✗ 열넷 명 → 열네 명), which numbers go with which counter, hours native (두 시) / minutes Sino (삼십 분 · 반), 분 never dropped (✗ 사십오 이에요).

**E. Structure / word order** (08 안 · 10 time + 에 · 16 -지 않다 · 22/42 -겠- · 32 -고 있다 · 34 -고 · 38 -고 싶다 · 39 -지 마세요 · 57 -거나 · 59 -는 것):
the decision is *where* things go, not letters — 안 before a plain verb, N 안 하다 (✗ 안 아르바이트 해요), 좋아하다/싫어하다 are one verb (✗ 좋아 안 해요);
N하다 before -고 keeps 하 (✗ 산책고); tense on the last verb (먹고 싶었어요, ✗ 먹었고 싶어요); -지 마세요 with special honorific stems (드시지 마세요 · 주무시지
마세요; ✗ 먹지 마세요 to an elder is fine grammatically, just not polite — say so); 10: no 에 after 오늘·내일·어제·지금·매일·언제 but 에 after 작년·지난주·주말·아침.

## 4. The user's recorded wrong forms — use them as ✗ rows where the topic matches

읽세요 · 읽어세요 · 받십니다 · 씻러 (dropped 으) · 만들습니다 · 만들으세요 · 만들을까요 (ㄹ) · 살어요 · 살었어요 · 받었어요 (ㅏ + 어) · 학생였어요 · 공원였어요
(N + 였 after 받침) · 어떻었어요 (→ 어땠어요) · 맙니다 for 마십니다 · 빌렸십니다 · 드시세요 (double honorific) · 바빱니다 (ㅡ dropped before ㅂ니다) · 먹습니다 for
먹습니까? · 좋아 안 해요 · 안 아르바이트 해요 · 산책고 · 좋아 하고 for 좋고 · 열넷 명 · 사십오 이에요 · 두시 이십분 (spacing) · 가르칠 거요 · 갈거예요 (space) ·
네 게 / 테국 / 메워요 / 젝 (ㅐ·ㅔ) · 더려워요 · 귀워요 (ㅂ forms) · 영화은 for 재미있는 · 무서 워요 · 사과과 (와 after vowel) · 먹으세요 for 드세요 · 하지 않습니다 for
안 했습니다 (tense dropped in register change). Put each one in the topic where it belongs; never invent new "user mistakes".

## 5. Assignment (unit ownership → no two agents edit the same unit file)

| Agent | Units owned | Topics (FULL unless marked SHORT) |
|---|---|---|
| A | 05–13 | 01 은/는 SHORT (U5) · 02 이에요/예요·입니다·아니에요 SHORT (U5/7 → put the compact block in unit07) · 04 numbers+counters SHORT (U10) · 06 -아/어/여요 FULL (U11) · 07 을/를 SHORT (U11) · 08 안 SHORT (U12) · 10 time + 에 SHORT (U13) |
| B | 14–18 | 16 -지 않다 SHORT (U14) · 19 와/과 SHORT (U15) · 20 -(으)시-·-(으)세요 FULL (U15) · 21 -(스)ㅂ니다 FULL (U16) · 22 -겠- SHORT (U16) · 23 -았/었/였-·N이었/였 FULL (U17) · 25 N시 N분 SHORT (U18) · 26 -(으)러 FULL (U18) |
| C | 19–24 | 28 -(으)ㄹ 거예요 FULL (U19) · 30 -네요 SHORT (U20) · 32 -고 있다 SHORT (U21) · 33 -(으)ㄹ까요? FULL (U22) · 34 -고 SHORT (U22) · 36 -(으)ㄴ FULL (U23) · 37 ㅂ 불규칙 FULL (U23) · 38 -고 싶다 SHORT (U24) · 39 -지 마세요 SHORT (U24) |
| D | 26–30 | 42 -겠- guess SHORT (U26) · 43 -아/어지다 FULL (U27) · 44 -는 FULL (U27) · 46 -(으)ㄹ 수 있다 FULL (U28) · 47 -(으)ㄴ past FULL (U29) · 48 -아/어서 reason FULL (U29) · 49 (으)로 direction SHORT (U30) · 50 -(으)니까 FULL (U30) |
| E | 31–34 | 51 (으)로·ㄷ 불규칙 FULL (U31) · 53 -아/어서 sequence FULL (U32) · 54 르 불규칙 FULL (U32) · 55 -(으)면 FULL (U33) · 56 -(으)ㄹ + N FULL (U33) · 57 -거나 SHORT (U34) · 58 (이)나 SHORT (U34) |
| F | 35–37 | 59 -는 것 SHORT (U35) · 60 -아/어 보다 FULL (U35) · 61 -(으)ㄴ/는데요 FULL (U36) · 62 -(으)ㄹ게요 FULL (U36) · 63 -아/어 주세요 FULL (U37) · 64 -아/어야 하다 FULL (U37) |

Unit 25 / topic 40 are done (the exemplar) — do not edit them. Topics not listed (03 05 09 11 12 13 14 15 17 18 24 27 29 31 35 41 45 52)
have no formula and get nothing.

## 6. House rules (the renderer and the style checker enforce these)

- Headings: `####` only inside the block; never a bold line as a heading.
- Every table is preceded by a lead sentence (plain paragraph). No `·`-chains of examples inside the new blocks — one form per cell.
- ≤ 7 columns per table; a cell holds at most ~5 Korean syllable blocks or a short Thai phrase (Korean never wraps mid-word, long runs overflow).
- Korean as the textbook prints it; bold only the changed part in the result column; `✗` for wrong, `✓`/`(O)` for right; never `~~`.
- Thai glosses only where they help (`*(…)*` after a form), keep them short; no English.
- `{c:…}` braces are reserved for colour tags — never write braces in content.
- Callouts: `> [!TIP] วิธีจำสั้น ๆ` exactly (Thai label is added by the renderer).
- Verify any form you are not sure of against the OCR text `extracted/textbook/unitNN.txt` or the page images `extracted/textbook/unitNN/page-N.png`;
  the topic file's own example tables are already verified — reuse their verbs.
- After editing run `python3 scripts/book_style_check.py <every file you touched>` — must print `0 hard`; Korean-token ratio > 100 % is expected.
- Do not rebuild PDFs, do not edit CLAUDE.md, do not commit.

## 7. Report back (final message)

List per topic: file + the heading inserted + number of worked rows, the unit file + heading, anything you were unsure about
(a form, a rule, a page you could not read), and the checker output. Keep it under 40 lines.
