# BRIEF_pictures — put the REAL pictures next to every 🖼️ description

The student (Thai, Korean level 1, exam 11/20 + 11/23) asked: everywhere the PDFs or the practice site describe a picture in
words only (`🖼️ …`), show the real picture from the book / the teacher's paper. Style follows the original (textbook,
workbook, teacher's sheet) first; only when no original exists or the scan is unreadable, draw a clear replacement.

You own a set of units (given in your task). Work only in your files. Read this whole brief first.

## 1. Tools (already built — do not modify them)
| command | what it does |
|:---|:---|
| `python3 scripts/pic_inventory.py --unit NN` | every open 🖼️ of unit NN (Markdown `file:line` and practice-site `json:set §sec #item`) |
| `python3 scripts/pic_inventory.py --file PATH` | same for one file (grammar files, exam files) |
| `python3 scripts/crop_images.py --grid "<pdf>" <page>` | writes `extracted/img/_grid/<name>-p<page>.png`: the page with a % grid (red lines every 5 %, blue labels every 10 %) — Read it, read the box off the grid |
| `python3 scripts/crop_images.py --sheet content/img/<yours>.tsv` | builds all your crops (white margins auto-trimmed) and puts them on ONE labelled contact sheet `extracted/img/_sheet_<yours>-tsv.png` — Read it to check many crops at once |
| `python3 scripts/crop_images.py --sheet ID ID …` | same for a few ids |
| `python3 scripts/apply_pic_map.py --dry` | checks your practice-site map rows resolve (never run it without `--dry`) |

Page images already rendered (cheaper to look at than a grid): `extracted/textbook/unitNN/page-K.png` (= PDF page K of
`source/textbook/KMU student's book unit NN.pdf`), `extracted/workbook/unitNN/wb-K.png`, `extracted/everyday/unitNN/test-K.png`
/ `sheet-K.png`. Combined PDFs: workbook 05–13 and 14–22, everyday test/sheet 05–13 — the page header names the unit
(`extracted/everyday/unit05-13/test-N.png` is NOT unit N; check the header `1급 매일 시험_N과`).

## 2. Manifest = your own file `content/img/<name>.tsv` (name given in your task)
6 **tab-separated** columns, `#` = comment line:
```
id	src	page	box	w	note
wb30-1-signs	source/workbook/KMU workbook unit 30.pdf	1	12 18 88 36		ป้าย 6 แบบ (ซ้าย ขวา ทางม้าลาย …)
tb30-304-1	source/textbook/KMU student's book unit 30.pdf	3	20 40 38 52	24	ไอคอนคนเดินเข้าประตู
cd30-left	card:⬅️				ลูกศรชี้ซ้าย (ไม่มีภาพต้นฉบับ)
```
- **id**: lowercase `a-z0-9-`, unique. Prefix by source: `tbNN-<printed page>-…` textbook · `wbNN-<pdf page>-…` workbook ·
  `evNN-t-…` / `evNN-s-…` everyday test / sheet · `mxNN-…` 복습시험 paper · `rv01-…` / `rv02-…` 복습문제 handouts ·
  `lcNN-…` lecture · `cdNN-…` drawn card. Never reuse another agent's prefix range (you own your units only).
- **src**: the PDF path exactly as in `source/` (page = 1-based PDF page), or `card:…` (see §5).
- **box**: `x0 y0 x1 y1` in % of the page, read off the grid. A little white margin is fine (trimmed automatically); never
  cut into the picture; never include a neighbouring item's picture.
- **w**: print width in % of the PDF text width. Leave empty (= printed size, usually right). Use 90–100 for a full-width
  panel/map/scene, 15–25 for a small icon that should stay small.
- **note**: short Thai description (copy the essence of the 🖼️ caption).

## 3. What to crop
- **One crop per item** when each item has its own picture (icons, people, signs). **One crop of the whole panel** when one
  picture serves several items (a map, a scene, a 보기 strip) — show it once, above the items.
- Include labels printed as part of the picture (names under people, prices, floor numbers, 〈오후〉/〈밤〉). Leave out the
  item number, the answer blank, and printed answers when you can.
- **Clean original first:** 매일시험/연습지 items are usually lifted from the workbook/textbook. If the same picture exists in
  the workbook or textbook, crop it from there (clean print) and reuse that id for the test item too. Crop the teacher's
  paper only when the picture exists only there; the student's pencil inside the picture is acceptable, red pen is not if avoidable.
- **Predictions** (`content/predictions/everyday/unitNN.md`, `daily_predictNN.json`) lift items from the workbook,
  textbook and sheets → reuse the SAME id as the source item. Crop only what is new.
- A picture repeated in several files (guide, workbook, prediction, site) = one id used everywhere.

## 4. Edit the Markdown (only lines the inventory lists)
Put `![](img:ID)` directly **before** the 🖼️ on the same line. Change nothing else — keep the caption, the blanks, every word.
```
1. 🖼️ คนเดินเข้ากรอบประตู → (　　)          →   1. ![](img:ev30-t-1) 🖼️ คนเดินเข้ากรอบประตู → (　　)
| 3 | 🖼️ แถบขาวดำบนถนน | 횡단보도 |            →   | 3 | ![](img:wb30-1-3) 🖼️ แถบขาวดำบนถนน | 횡단보도 |
> **<보기>:** 🖼️ ป้าย "휴게실" …              →   > **<보기>:** ![](img:wb30-2-ex) 🖼️ ป้าย "휴게실" …
🖼️ *แผนที่สี่แยก …*                          →   ![](img:tb30-306-map) 🖼️ *แผนที่สี่แยก …*
```
- Never put `![](…)` inside `*…*` italics, inside `**…**`, or inside a `{c:…}` colour tag — always before them.
- Several pictures for one item: `![](img:a) ![](img:b) 🖼️ …`.
- A caption line that only points at part of a panel already shown within the previous lines of the same block counts as
  covered (the inventory skips it) — no need to repeat the panel.
- Table header cells such as `| ข้อ | 🖼️ ภาพ | คำ |` are not pictures — leave them; the row cells get the images.
- A 🖼️ that is not a picture at all (e.g. "ไม่มีภาพในต้นฉบับ", a description of audio) → leave it and list it in your report.

## 5. When there is no original to crop (or it is unreadable)
Some items were invented for predictions, or the scan is too blurry to read. Then:
1. look for a real picture of the same thing in the unit's textbook / workbook pages (vocabulary illustrations, 연습 icons) and use it;
2. otherwise draw a card: `src` = `card:<panel> → <panel> | <panel>` — `→` draws the book's red arrow, `|` a gap. Panel =
   emoji (single code points only: 🏊 ☀️ 🌧️ 🚌 🍜 ⬅️ ➡️ ⬆️ ⬇️ — no ZWJ combinations like 🧑‍🍳), `clock=7:30` (analog clock),
   `text=3,500원` (a framed label), plus optional `@caption` under the panel. Captions only what a paper would print
   (a name, a price, a floor) — **never the answer word**. Check the result on your sheet like any crop.

## 6. Practice site — never edit `content/mockweb/*.json`
Other agents share those files. Instead add rows to your map file `content/img/map_<name>.tsv`:
```
daily_b.json	sheet-30-writing §1 #1	ev30-s-1
daily_b.json	daily-30-writing §2	tb30-306-map
```
Column 2 = exactly what `pic_inventory.py` prints after the file name (`<set id> §<section> #<item n>`). Without `#n` the
picture is shown once at the top of the section (use that for a panel/map). Several ids: `a,b`. Every open site item of your
units needs a row. `python3 scripts/apply_pic_map.py --dry` must report 0 problems for your rows.

## 7. Order of work and checks
For each of your units: inventory → open the source pages → write manifest rows → `--sheet` → Read the sheet, fix boxes,
repeat until every crop shows exactly its picture → edit Markdown lines → add map rows. At the end:
- `python3 scripts/pic_inventory.py --unit NN` (and `--file` for your extra files) lists nothing, or only lines you report as deliberate;
- `python3 scripts/crop_images.py --sheet content/img/<name>.tsv` builds without "not built"/warnings for your rows;
- `python3 scripts/apply_pic_map.py --dry` → 0 problems.

## 8. Rules
- Do NOT run `build.py`, `build_mockweb.py`, `apply_pic_map.py` without `--dry`, or `git`; do not publish; do not edit
  scripts, other agents' manifests/maps, `content/mockweb/*.json`, or any file outside your units.
- Token economy: Read a page image or grid only when you need a box from it; check crops with `--sheet` (one image for many
  crops), not one preview per crop; use the inventory + `Read` with offset instead of re-reading whole files.
- Report back (short): per unit — crops made (count), Markdown lines done, map rows, anything left open and why, any
  picture you drew instead of cropping and why.
