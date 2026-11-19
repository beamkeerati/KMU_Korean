# make_pdf.py gotchas, environment notes, plugin policy

*Moved verbatim from CLAUDE.md on 2026-11-04 to keep the always-loaded file small. Section numbers are the old CLAUDE.md numbers. Add new long logs here, not in CLAUDE.md.*

## 5. make_pdf.py gotchas
- Extensions loaded: `tables, fenced_code, sane_lists, toc`. **No strikethrough** — `~~x~~`
  prints literally. Use `x ✗` instead. Check with `grep -c '~~' output/_build/md/*.md` after a build.
- Alert blocks (`> [!TIP]`) and `<details>` run their body through `github_compat()` before
  `render_md()`; without that, Markdown lists inside them collapse into one paragraph.
- Fonts load from `/usr/share/fonts/truetype/noto/` via `@font-face`. **Don't add
  'Noto Color Emoji' to the font stack** — fontconfig then switches Latin/digits to a TeX Live font.
- `h2` and `h1` both `page-break-before: always`; `h1:first-of-type` is exempt so the cover
  doesn't start with a blank page.
- Needs packages from `~/.local/lib/python3.12/site-packages` (path inserted in the script).
- `pdftotext` mangles Thai vowel marks when you verify output — the rendered PDF is fine.
- WeasyPrint 70 **ignores `<ol start="N">`**; `render_md()` rewrites it to `counter-reset: list-item N-1`
  (fixed 2026-10-07 — before that every list starting at 11/13/16 printed as 1/2/3).
- `add_writing_space()` blank regexes use `[ \t]*`, never `\s*`, after the blank: `\s*` swallowed the
  newline whenever a `→ (　　)` blank ended a line, gluing the next item (or a `##` heading) onto it.
- A `###` heading containing 쓰세요/바꾸세요 puts two ruled lines under every item — **unless it contains
  고르 or 단어**; since 2026-10-18 a `####` heading does the same only with an explicit sentence instruction (문장을 만드세요/쓰세요/
  바꾸세요/완성, 대화를 완성, 대답하세요, 바꾸세요) — a bare 쓰세요 in `####` draws nothing (unit17/18 predictions rely on that) (word-answer sections; 단어 exclusion added 2026-10-10, it had put sentence lines under
  one-word blanks in 14 sections).
- Consecutive `> ` dialogue lines merge into one paragraph — put a bare `>` line between them.
- In a 쓰세요/바꾸세요 section, an item line starting `N.` also gets two ruled lines. For one-word blanks
  inside a dialogue, write `나: 회사에서 2)(　　).` (number inside the line, blank line between lines)
  — see everyday/unit16.md test A. Don't change the rule itself: ~38 workbook sentence answers rely on it.
- `{c:…}` braces are reserved for colour tags in every content/*.md (single letter + colon). `{{today}}` placeholders are
  untouched because the tag regex needs exactly one letter before the colon.
- The Write tool turns a `\u3000` escape inside Python source into the literal U+3000 character (kotag.py KO_RUN has the
  literal ideographic space in its regex) — a patch script that searches for the escape text will not match.
- Korean used to wrap mid-word (빔입니/다): WeasyPrint 70 ignores `word-break: keep-all` (tested 2026-10-18). Since 2026-10-27
  `wrap_korean_words()` in make_pdf.py puts every space-delimited Hangul chunk in `<span class="kw">` with `white-space: nowrap` —
  words now break only at spaces (tested; nested kotag colour spans inside are fine). A chunk whose span tags are unbalanced (a kotag
  span containing a space) is left alone. Headings and raw-HTML lines are skipped. A single Korean run longer than a table cell will
  overflow instead of wrapping — keep cells to a few words.
- Book-style renderer rules (2026-10-27): callout labels are Thai (`> [!TIP]` → 💡 เคล็ดลับ …) and `> [!INTRO] title` / `> [!SUMMARY]`
  exist; the TOC lists h1–h2 only (toc_depth 1-2) and hides its first entry (the cover + "목차"); `### 08. …` headings that already start
  with a number get class `nonum` so the per-chapter counter does not print "8. 08."; a bold line used as a heading (`**📝 …**`) gets no
  spacing, no number and no running head — write `###`/`####` instead (book_style_check.py flags it); `tbody > tr:nth-child(-n+2)
  { break-after: avoid }` moves a table whose first 1–2 rows would be orphaned to the next page (tested: 3+ rows still split normally);
  `h1:first-of-type` is the cover only inside `.book`/`.cover` (a document without `[TOC]` keeps a plain first heading).
- **Thai never wrapped (found 2026-11-03, the user saw tables running off the right edge "in many files"):** this WeasyPrint/Pango has no
  Thai line breaking (measured: a 90 px box with a spaceless Thai phrase overflows, with or without colour spans; with U+200B between words it
  wraps). So a table column of Thai glosses had a min-width of the whole phrase and pushed the table past the margin (20+ pages: predictions
  26–28, the midterm prediction, both guides). `thai_break_opportunities()` in make_pdf.py now puts U+200B between Thai words (PyThaiNLP via
  kotag's tokenizer) and at colour-span boundaries, never before a following vowel/tone mark or after a leading vowel; text nodes only. Word
  blanks in tables of 6+ columns are 5 em instead of 8 (build.py add_writing_space; the 10과 number table overflowed). Overflow check =
  scratchpad overflow_scan.py (pdftotext -bbox, any word with xMax > 548 pt on A4; mind maps are posters, skip them) → 0 pages after the
  fix; guides 655 → 651 and 728 → 721 pp, no dotted circles (U+25CC) in any PDF.
- kiwipiepy 0.24 and pythainlp 5.4 live in `~/.local/lib/python3.12/site-packages` (pip --user, 2026-10-17); the first
  `kotag` call per process takes ~2 s to load Kiwi + the vocabulary user words. Known Kiwi traps handled in kotag.py:
  누가 = nougat (pre-analysed), 마셔요 = 말+셔요, 주무세요/계세요/드세요 (user stems 주무·계·드), 어제 → 어+제 (MAG user word),
  공부하 tagged XSA (noun set keeps 공부 blue), 을/를·이/가 standalone lists (direct rules, no Kiwi).

## 7. Environment notes
- OS: Linux. `setlocale: LC_ALL` warnings are harmless.
- `.vscode/` once held a 2.6 GB C++ IntelliSense database; it is gone (8 KB now). If `browse.vc.db*`
  reappears, delete it and add a `.vscode/settings.json` C_Cpp exclusion.
- Checking the user's homework means reading handwritten Korean off a photo. There is no OCR help
  available for this — read the image directly and **say so when the handwriting is ambiguous**
  rather than asserting what it says. See §8.

## 8. Plugins — the user only wants free, local ones
**`pdf-viewer` is the only plugin enabled for this project.** It runs locally
(`npx @modelcontextprotocol/server-pdf`), costs nothing and needs no login. Use its skills
(`pdf-viewer:open`, `:annotate`, `:fill-form`, `:view-pdf`) when the user wants to look at or mark
up a PDF together.

**Disabled on the user's instruction (2026-10-05):**
- Paid services: `handwritingocr`, `extend`, `pdfbolt`, `pandadoc`
- Unrelated to this project: `data`, `engineering`, `presenton`, `read-paper`,
  `the-stoic-library`, `skill-creator`

Each was disabled twice — once as the locally installed copy and once as the `@synced` copy from
claude.ai. Disabling only the local copy makes the `@synced` copy load in its place, so **both must
be disabled** (`claude plugin disable <name>` then `claude plugin disable <name>@synced`); verify
with `claude mcp list` that no paid server is left connected.

Still enabled besides `pdf-viewer`: `document-skills` and `diagram-design`, both pre-existing and
free. A plugin's **skill descriptions load into every session whether or not its MCP server is
authenticated** — only the tool schemas wait for auth. The six unrelated plugins cost ~2,950
always-on tokens between them, which is negligible against the context budget; the real reason to
keep them off is that broad skill descriptions (e.g. `engineering:documentation`) can misfire on
this project's document work.

Do not re-enable these or suggest installing them again unless the user asks. In particular,
HandwritingOCR would read the homework scans more reliably than reading them by eye, but it uploads
the images to a third party and bills per page — the user considered that and declined.

## Book layout v2 (2026-11-15/16)
- Only the two guides (`<body class="book">`); block "book layout v2" at the end of CSS_BOOK in scripts/make_pdf.py.
- Type scale: chapter 27 · section 20 · sub-section 16.5 · body 14.5 · table 0.93em · table head / gloss 0.92–0.94em; Hangul `.kw` 1.06em.
- Proximity: big gap above a heading, small below; rows and list items tight, the gap comes after the group. Tables: horizontal hairlines only.
- Paging rules (each one measured — keep-together rules are expensive):
  - `class="keep"` (never split) only for tables with ≤ 7 `<tr>` AND < 520 characters of text (row count alone kept tall-row tables whole: half-page gaps).
  - `tbody > tr:last-child`, `li:last-child`, the last child of a callout/dialogue: `break-before: avoid` (no one-row / one-line sliver on the next page — the 11/15 audit found 23 such pages).
  - `p.lead` (a paragraph < 220 characters directly before a table; class added in md_file_to_pdf) stays with the table — this also fixes bold labels like "∞ 읽기 ∞" left at a page bottom.
  - Callouts and dialogues ≥ 420 characters may split; short ones stay whole. Top-level list items may split.
  - REJECTED: `h3/h4 + p { break-after: avoid }` for every lead sentence, `li { break-inside: avoid }`, keep for ≤ 10 rows → 174 pages with > 1/5 blank at the bottom (old layout: 17).
  - Bullets: inside a box the first bullet keeps the second and the last keeps the one before it; a list right after an h3–h5 or a bold label keeps its first two bullets with the heading. NO general "last bullet" rule for every list — WeasyPrint satisfies it by backtracking over the whole table that precedes the list (one page 70 % blank, By_Topic 61과).
- Results 11/16 (final): By_Unit 674 pages (was 652), By_Topic 761 (was 722, incl. the merged slide content). Pages with > 1/3 blank at the bottom, chapter ends excluded: Unit 8, Topic 12; > 2/5: 2 + 2 (a heading moving with its small table). Second Haiku audit after the fixes: one-row table slivers 16 → 0 (one doubtful), orphan headings 2 → 0, overflow 0; the box/label slivers it still found (10) were fixed afterwards and checked by eye on those pages only. First attempt (line-height 1.8, 9 px padding) was rejected by the user as "too empty".
- Measuring tool: last text yMax per page from `pdftotext -bbox` (header = yMax < 66, footer > 782); a chapter end = the next page's header differs. Visual audit = 4-page contact sheets at 52 dpi read by Haiku agents (9 agents, ≈ 2 min, 1,419 pages).

## Pictures (2026-11-19)
- `![🖼️ caption](img:ID)` → `convert_images()` runs BEFORE kotag and emits `<img class="pic" src="file://…/extracted/img/ID.jpg" style="width:Nmm" alt="">`
  (alt stays empty so kotag never tags text inside an attribute; width in mm, not %: a % inside a table cell shrank to nothing).
  Width = the manifest's `w` (% of the 168 mm text width) or the crop's printed size at 300 dpi.
- `arrange_pictures()` (after render_md): a `<p>`/`<li>` that STARTS with pictures becomes `.picrow` — pictures left, all the item's text right
  (table layout); > 100 mm of pictures → `.stack` (pictures above, text below). The user rejected 가: beside the picture with 나: under it.
- In table cells pictures are blocks capped at 24 mm tall (a 24-row picture table went 27 → 24 pages, 7 rows a page).
- Crops are regenerated from source/ by scripts/crop_images.py (cache extracted/img/_pages, stamps extracted/img/_stamps.json written atomically);
  `map_*.tsv` files in content/img/ are site mappings, never manifests.
- **Remaster (11/19, user: "ชัด สดใส คมเหมือน svg"):** crop_images.py writes the plain crop to extracted/img/_raw/ and then redraws it with
  Real-ESRGAN (realesrgan-ncnn-vulkan, GPU; official release unzipped in extracted/tools/esrgan, git-ignored — the user approved running it)
  at 4×, kept at 2× the scan size, paper → pure white, colour ×1.3 saturation. Anime model for book/teacher art, x4plus for lecture photos;
  drawn cards (cd-/gx-/essay-) are skipped. Photocopy halftone (dottiness ≥ 28) is blurred σ1 and halved first — without that the model
  erased faces (14과 test woman). Printed size still comes from the _raw crop (natural_px), so remastered files don't print 2× larger.
  Without the tool the plain crop is used. vtracer (pip) was tried for true SVG: fine for colour art, but grey shading turned solid black.
