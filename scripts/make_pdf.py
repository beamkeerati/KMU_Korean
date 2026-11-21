#!/usr/bin/env python3
"""Convert the Markdown study sheets in this folder to PDF — book style (2026-10-27).

Usage:  python3 make_pdf.py "Some File.md" [more.md ...] [--pdf-dir DIR]
        (normally you want scripts/build.py instead)

Uses WeasyPrint (per-glyph font fallback) so Thai, Korean, Latin and emoji
all render correctly.

Fonts (the user's choice 2026-10-27, replacing the earlier Noto-only rule):
  Thai + Latin  = Laksaman (TLWG's free clone of TH SarabunPSK — the TH Sarabun letter shapes; regular/bold/italic)
  Korean        = Noto Serif CJK KR (명조, serif Hangul)
  symbols/emoji = Noto Sans Symbols2 / Noto Color Emoji by fontconfig fallback (→ ✓ ✗ ★ are not in Laksaman)
  mono          = Noto Sans Mono
Sarabun is a small-bodied face, so the base size is 15.5px where Noto Sans Thai needed 12.5px.

Book features (all CSS, no content change needed):
  - running head: current chapter (string-set from h2) left, current part (from h1) right; page x / y bottom right;
    the colour legend bottom left; nothing on the cover page
  - h1 = part title page, h2 = chapter (own page, big title + rule), h3 = numbered section (counter per chapter
    inside <body class="book">), h4 = sub-section
  - TOC with dot leaders + page numbers (books), chapters only (toc_depth 1-2)
  - Korean words never break mid-word: wrap_korean_words() puts every space-delimited Hangul chunk in
    <span class="kw"> (white-space: nowrap); breaks still happen at the spaces between words
  - callouts: > [!NOTE|TIP|IMPORTANT|WARNING|CAUTION|INTRO|SUMMARY] optional title → styled box (Thai labels)
  - orphans/widows 2, headings never left alone at a page bottom, table rows never split, thead repeats
"""
import os
import re
import sys

sys.path.insert(0, os.path.expanduser('~/.local/lib/python3.12/site-packages'))

import markdown
from weasyprint import HTML

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, WORKSPACE)
import kotag                                   # colour-by-function tagging (Korean auto, Thai glosses auto)

TLWG_DIR = '/usr/share/fonts/truetype/tlwg'
NOTO_DIR = '/usr/share/fonts/truetype/noto'
# Thai/Latin and Mono are loaded straight from files so fontconfig cannot substitute another font
# (e.g. TeX Live's Mezenets) for them. The Korean serif comes from the system TTC via fontconfig.
FONT_FACES = f"""
@font-face {{ font-family: 'KMU Thai'; font-weight: normal; font-style: normal; src: url('file://{TLWG_DIR}/Laksaman.ttf'); }}
@font-face {{ font-family: 'KMU Thai'; font-weight: bold;   font-style: normal; src: url('file://{TLWG_DIR}/Laksaman-Bold.ttf'); }}
@font-face {{ font-family: 'KMU Thai'; font-weight: normal; font-style: italic; src: url('file://{TLWG_DIR}/Laksaman-Italic.ttf'); }}
@font-face {{ font-family: 'KMU Thai'; font-weight: bold;   font-style: italic; src: url('file://{TLWG_DIR}/Laksaman-BoldItalic.ttf'); }}
@font-face {{ font-family: 'KMU Mono'; font-weight: normal; src: url('file://{NOTO_DIR}/NotoSansMono-Regular.ttf'); }}
@font-face {{ font-family: 'KMU Mono'; font-weight: bold;   src: url('file://{NOTO_DIR}/NotoSansMono-Bold.ttf'); }}
"""
# NOTE: don't list 'Noto Color Emoji' here — doing so makes fontconfig pick
# TeX Live's Mezenets for Latin/digits. Emoji fall back to it automatically.
FONT_STACK = "'KMU Thai', 'Noto Serif CJK KR', 'Noto Sans Symbols2', 'Noto Sans Math'"
MONO_STACK = "'KMU Mono', 'KMU Thai', 'Noto Serif CJK KR', 'Noto Sans Symbols2'"
BASE_PX = 14.5          # body size (user asked for one step smaller on 10/27; was 15.5) — Sarabun-class fonts read like Noto Sans at ~12px

CSS_BOOK = """
/* ================= page ================= */
@page {
    size: A4;
    margin: 24mm 19mm 22mm 19mm;
    @top-left  { content: string(chapter); font-family: __FONT__; font-size: 10.5px; color: #6e7781;
                 vertical-align: bottom; padding-bottom: 7px; }
    @top-right { content: string(part);    font-family: __FONT__; font-size: 10.5px; color: #6e7781;
                 vertical-align: bottom; padding-bottom: 7px; }
    @bottom-left  { content: element(klegend); vertical-align: top; padding-top: 7px; }
    @bottom-right { content: counter(page) " / " counter(pages); font-family: __FONT__; font-size: 10.5px;
                    color: #6e7781; vertical-align: top; padding-top: 7px; }
}
@page :first {
    @top-left { content: none; } @top-right { content: none; }
    @bottom-left { content: none; } @bottom-right { content: none; }
}
h1 { string-set: part content(), chapter ''; }   /* a part page clears the chapter head */
h2 { string-set: chapter content(); }

/* ================= type ================= */
body { font-family: __FONT__; font-size: __BASE__px; line-height: 1.62; color: #1f2328; }
p { margin: 0 0 0.75em; orphans: 2; widows: 2; }
strong { color: #0b2e4f; }
em { color: #4b5563; }
.kw { white-space: nowrap; font-size: 0.95em; }   /* a Korean word never breaks mid-word; Hangul fills its em box, so 5 % smaller matches Sarabun */
.klegend { font-size: 10px; color: #6e7781; white-space: nowrap; }
.klegend span { margin-right: 7px; }

/* ================= headings ================= */
/* h1 = part title page · h2 = chapter (own page) · h3 = section · h4 = sub-section */
h1 {
    font-size: 34px; line-height: 1.3; color: #0f4c81;
    margin: 150px 0 30px; padding: 0 0 18px; border-bottom: 3px solid #0f4c81;
    page-break-before: always; page-break-after: avoid;
}
h1:first-of-type { page-break-before: auto; margin-top: 0; }
.book h1:first-of-type, .cover h1:first-of-type {          /* the cover page of a document that has a TOC */
    margin-top: 220px; text-align: center; border-bottom: none; font-size: 38px;
}
.book h1:first-of-type + p, .cover h1:first-of-type + p { text-align: center; color: #57606a; font-size: 1.1em; margin-top: 10px; }
h1 + p, h1 + blockquote { font-size: 1.05em; color: #3a3f44; }
h2 {
    font-size: 25px; line-height: 1.35; color: #0f4c81;
    margin: 0 0 24px; padding: 0 0 12px; border-bottom: 2px solid #0f4c81;
    page-break-before: always; page-break-after: avoid;
}
h3 {
    font-size: 18.5px; line-height: 1.35; color: #0f4c81;
    margin: 36px 0 12px; padding: 0 0 5px; border-bottom: 1px solid #c9d1d9;
    page-break-after: avoid;
}
h2 + h3, h2 + p + h3, h2 + .alert + h3 { margin-top: 20px; }
h4 { font-size: 16px; color: #1a4d7a; margin: 26px 0 8px; page-break-after: avoid; }
h5 { font-size: 14.5px; color: #333; margin: 18px 0 6px; page-break-after: avoid; }
h1 + h2, h2 + h3 { page-break-before: auto; }   /* no blank page after a part title */
h3 + table, h4 + table, h3 + ul, h4 + ul, h3 + ol, h4 + ol { margin-top: 0.4em; }

/* section numbers per chapter (books only) */
.book h2 { counter-reset: sec; }
.book h3::before { counter-increment: sec; content: counter(sec) ". "; color: #8c959f; font-weight: normal; }
.book h3.nonum::before { content: none; }

/* ================= tables ================= */
table { border-collapse: collapse; width: 100%; margin: 0.5em 0 1.4em; font-size: 0.94em; line-height: 1.5;
        page-break-inside: auto; }
th, td { border: 1px solid #d0d7de; padding: 6px 10px; vertical-align: top; orphans: 2; widows: 2; }
th { background: #eaf1f8; color: #0f4c81; font-weight: bold; text-align: left; }
tr:nth-child(even) td { background: #f8fafc; }
tr { page-break-inside: avoid; }
tbody > tr:nth-child(-n+2) { break-after: avoid; }   /* never leave 1–2 orphan rows at a page bottom (tested 2026-10-27) */
thead { display: table-header-group; }
td > p:last-child { margin-bottom: 0; }

/* ================= lists ================= */
ul, ol { margin: 0.2em 0 1em; padding-left: 1.7em; }
li { margin: 0 0 0.42em; orphans: 2; widows: 2; }
li > ul, li > ol { margin: 0.3em 0 0.2em; }
li p { margin: 0 0 0.3em; }
li > table { margin-top: 0.5em; }

/* ================= dialogue / quotes ================= */
blockquote {
    margin: 0.6em 0 1.3em; padding: 10px 18px; color: #1f2328;
    border-left: 4px solid #94a3b8; background: #f8fafc; border-radius: 0 6px 6px 0;
    page-break-inside: avoid;
}
blockquote p { margin: 0 0 0.4em; }
blockquote p:last-child { margin-bottom: 0; }
hr { border: none; border-top: 1px solid #d0d7de; margin: 1.4em 0; }
img { max-width: 100%; }
/* real pictures from the scans (content/img/*.tsv): printed at their paper size, side by side when a line holds several */
img.pic { vertical-align: middle; margin: 3px 10px 3px 0; max-height: 120mm; }
.picrow { display: table; width: 100%; page-break-inside: avoid; margin: 2px 0; }
.picrow > .pc { display: table-cell; vertical-align: middle; white-space: nowrap; width: 1%; padding-right: 6px; }
.picrow > .pt { display: table-cell; vertical-align: middle; }
.picrow.stack, .picrow.stack > .pc, .picrow.stack > .pt { display: block; width: auto; }
.picrow.stack > .pc { white-space: normal; margin-bottom: 4px; }
td img.pic { display: block; margin: 2px 0 3px; width: auto !important; max-width: 100%; max-height: 24mm; }   /* a row per item: keep rows short */

/* ================= write-in space ================= */
.wl { display: block; height: 2.2em; margin: 2px 0 6px; border-bottom: 1.2px solid #6e7781; }
.wl2 { display: block; height: 4.8em; margin: 2px 0 8px;
       background: repeating-linear-gradient(to bottom, transparent 0, transparent 2.3em, #6e7781 2.3em, #6e7781 calc(2.3em + 1.2px)); }

/* ================= code ================= */
code { font-family: __MONO__; font-size: 0.82em; background: #f6f8fa; padding: 1px 5px; border-radius: 4px; }
pre { font-family: __MONO__; font-size: 0.82em; background: #f6f8fa; padding: 10px 12px; border-radius: 6px;
      border: 1px solid #d0d7de; white-space: pre-wrap; margin: 0.5em 0 1.2em; }
pre code { background: none; padding: 0; }

/* ================= callouts ================= */
.alert { border-left: 5px solid; border-radius: 0 6px 6px 0; padding: 10px 16px; margin: 0.8em 0 1.3em;
         page-break-inside: avoid; }
.alert p { margin: 0 0 0.4em; }
.alert p:last-child, .alert ul:last-child, .alert table:last-child { margin-bottom: 0; }
.alert-title { font-weight: bold; margin-bottom: 4px; }
.alert-note      { background: #ddf4ff; border-color: #0969da; }
.alert-tip       { background: #dafbe1; border-color: #1a7f37; }
.alert-important { background: #fbefff; border-color: #8250df; }
.alert-warning   { background: #fff8c5; border-color: #9a6700; }
.alert-caution   { background: #ffebe9; border-color: #cf222e; }
.alert-intro     { background: #f0f6fc; border-color: #0f4c81; page-break-inside: auto; }
.alert-intro .alert-title { color: #0f4c81; font-size: 1.05em; }
.alert-summary   { background: #f6f8fa; border-color: #57606a; }
.answer { background: #f6f8fa; border: 1px dashed #8c959f; border-radius: 6px; padding: 8px 12px; margin: 8px 0 14px; }
.answer-title { font-weight: bold; margin-bottom: 4px; }

/* ================= TOC ================= */
.toc { font-size: 0.95em; line-height: 1.5; column-count: 2; column-gap: 28px; }
.toc ul { padding-left: 16px; margin: 0; list-style: none; }
.toc li { margin: 2px 0; }
.toc a { color: #0f4c81; text-decoration: none; }
.book .toc, .cover .toc { column-count: 1; font-size: 1em; }
.toc > ul > li:first-child { display: none; }    /* the cover title and the TOC heading themselves */
.book .toc > ul > li, .cover .toc > ul > li { margin: 0.5em 0 0.2em; font-weight: bold; }
.book .toc > ul > li > ul > li, .cover .toc > ul > li > ul > li { font-weight: normal; margin: 1px 0; }
.book .toc a::after, .cover .toc a::after { content: leader('. ') target-counter(attr(href), page); color: #6e7781; font-weight: normal; }
@page { @top-center { content: none; } }

/* ================= book layout v2 (2026-11-15) =================
   The two guides only (<body class="book">). Content is untouched; this is typography.
   Principles (the user: "not cramped, not empty — know what is small, what sits together, what shares a page"):
   1. A type scale with clear ranks: chapter 27 > section 20 > sub-section 16.5 > body 14.5 > table 13.5 >
      table head / gloss / note 12.5. Hangul is the thing being studied, so it is 6 % larger than the Thai around it.
   2. Proximity: a heading has a big gap above and a small one below (it belongs to what follows); a lead sentence
      sits close to its table or list; rows and list items are tight inside their group; the gap comes after the group.
   3. Tables are open (horizontal hairlines only) but their rows stay compact — a conjugation table is one unit.
   4. Paging: a chapter starts a page; a heading never ends a page and keeps its lead sentence; a table of up to
      6 rows, a nested list item and a SHORT dialogue or callout (< 420 characters) are never split (class "keep" is added in md_file_to_pdf). */
.book { line-height: 1.66; }
.book p { margin: 0 0 0.7em; orphans: 3; widows: 3; }
.book .kw { font-size: 1.06em; }
.book em { font-size: 0.94em; color: #5b6570; }                 /* glosses and asides: one rank below the text */

/* --- headings: rank by size AND by form --- */
.book h2 {
    font-size: 27px; line-height: 1.35; border-bottom: none; border-left: 8px solid #0f4c81; background: #f1f6fb;
    border-radius: 0 10px 10px 0; padding: 15px 20px; margin: 0 0 20px;
}
.book h3 { font-size: 20px; margin: 34px 0 8px; padding: 0 0 6px; border-bottom: 2px solid #dbe5ef; }
.book h2 + h3, .book h2 + p + h3, .book h2 + .alert + h3 { margin-top: 22px; }
.book h4 { font-size: 16.5px; margin: 24px 0 6px; padding: 0 0 0 10px; border-left: 4px solid #9db9d6; border-bottom: none; }
.book h5 { font-size: 14.5px; margin: 16px 0 4px; color: #1a4d7a; }
.book h3 + h4 { margin-top: 12px; }

/* --- tables: open, compact, one rank smaller --- */
.book table { margin: 0.1em 0 1.5em; font-size: 0.93em; line-height: 1.5;
              border-top: 2px solid #0f4c81; border-bottom: 1.5px solid #9aa7b4; }
.book th, .book td { border: none; border-bottom: 1px solid #e4e9ef; padding: 5px 11px; }
.book th { background: #eef4fa; border-bottom: 1.5px solid #0f4c81; font-size: 0.92em; color: #3d5a78; padding: 6px 11px; }
.book tr:nth-child(even) td { background: none; }
.book tbody tr:last-child td { border-bottom: none; }
.book td strong .kw, .book td strong.kw { font-size: 1.1em; }          /* the answer form in a table is the largest thing in its row */
.book table.keep { page-break-inside: avoid; }
.book tbody > tr:nth-child(2) { break-after: auto; }                   /* one row after the head is enough company (two cost big gaps) */
.book tbody > tr:last-child { break-before: avoid; }                    /* never one row alone on the next page (16 pages in the 11/15 audit) */
.book p.lead { page-break-after: avoid; margin-bottom: 0.4em; }        /* a short line right before a table goes with the table (class set in md_file_to_pdf) */
/* no "last bullet stays with the list" rule: WeasyPrint backtracks over the whole table before the list to satisfy it (70 % blank page, measured 11/16) */
.book h3 + table, .book h4 + table { margin-top: 0.5em; }

/* --- lists: tight inside, space after --- */
.book ul, .book ol { margin: 0.1em 0 1.1em; padding-left: 1.8em; }
.book li { margin: 0 0 0.3em; }
.book li li { page-break-inside: avoid; }
.book li > ul, .book li > ol { margin: 0.25em 0 0.35em; }
.book li li { font-size: 0.97em; }

/* --- dialogue and callouts: a little air inside, kept whole --- */
.book blockquote { margin: 0.5em 0 1.4em; padding: 12px 20px; line-height: 1.8; border-left-width: 5px; border-radius: 0 8px 8px 0; }
.book blockquote p { margin: 0 0 0.35em; }
.book .alert { padding: 12px 18px; margin: 0.7em 0 1.5em; border-radius: 0 8px 8px 0; font-size: 0.96em; line-height: 1.6; }
.book .alert p { margin: 0 0 0.45em; }
.book .alert-title { margin-bottom: 5px; font-size: 1.04em; break-after: avoid; }
.book .alert > :last-child, .book blockquote > :last-child { break-before: avoid; }   /* no one-line sliver of a box on the next page */
.book .alert p, .book blockquote p { orphans: 2; widows: 2; }
/* bullets INSIDE a box: never the title plus one bullet at a page bottom, never one bullet alone on the next page
   (10 pages in the second audit). Scoped to boxes on purpose — the same rule for every list dragged whole tables. */
.book .alert li:first-child, .book blockquote li:first-child { break-after: avoid; }
.book .alert li:last-child, .book blockquote li:last-child { break-before: avoid; }
.book p.lead + ul > li:first-child, .book p.lead + ol > li:first-child { break-after: avoid; }
.book h3 + ul > li:first-child, .book h4 + ul > li:first-child, .book h5 + ul > li:first-child,
.book h3 + ol > li:first-child, .book h4 + ol > li:first-child, .book h5 + ol > li:first-child { break-after: avoid; }   /* a heading never keeps just one bullet */
.book .alert-intro { font-size: 0.95em; margin-bottom: 1.2em; }
.book .alert table { margin: 0.4em 0 0.3em; }
.book hr { margin: 1.6em 0; }
.book .toc { line-height: 1.6; }
""".replace('__FONT__', FONT_STACK).replace('__MONO__', MONO_STACK).replace('__BASE__', str(BASE_PX))

CSS_STYLE = FONT_FACES + CSS_BOOK + kotag.CSS_COLORS + """
.klegend { font-size: 10px; }
"""

ALERT_LABELS = {
    'note': 'ℹ️ หมายเหตุ',
    'tip': '💡 เคล็ดลับ',
    'important': '❗ สำคัญ',
    'warning': '⚠️ ระวัง',
    'caution': '🛑 ห้าม',
    'intro': '🧭 บทนี้ว่าด้วยอะไร',
    'summary': '📌 สรุปท้ายบท',
}

md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists', 'toc'],
                                 extension_configs={'toc': {'toc_depth': '1-2'}})


IMG_MD = re.compile(r'!\[[^\]\n]*\]\(img:([a-z0-9-]+)\)')
_img_rows = None


def convert_images(text):
    """![🖼️ caption](img:ID) → the real picture (crop listed in content/img/*.tsv, built by scripts/crop_images.py).
    Runs before kotag: the <img> carries no Korean/Thai text (alt=""), so a line that also holds text is safe to colour."""
    global _img_rows
    if '](img:' not in text:
        return text
    import crop_images
    if _img_rows is None:
        _img_rows = crop_images.load_manifest()

    def repl(m):
        iid = m.group(1)
        row, path = _img_rows.get(iid), os.path.join(crop_images.OUT, iid + '.jpg')
        if row is None or not os.path.exists(path):
            print(f'WARNING: picture {iid} is not built (python3 scripts/crop_images.py)', file=sys.stderr)
            return f'🖼️ [{iid}?]'
        svg = os.path.join(crop_images.MANIFESTS, 'gen', iid + '.svg')      # redrawn pictures (scripts/draw_speaking_pics.py) stay vector in the PDF
        if os.path.exists(svg):
            path = svg
        return f'<img class="pic" src="file://{path}" style="width:{round(crop_images.display_width(row) * 1.68)}mm" alt="" />'   # % of the 168 mm text width (mm, not %: a % inside a table cell shrank to nothing)
    return IMG_MD.sub(repl, text)


PIC_LEAD = re.compile(r'(<li>\s*(?:<p>)?|<p>)(\s*(?:<img class="pic"[^>]*/>\s*)+)')
PIC_SIDE_MM = 100          # pictures up to this total width sit LEFT of their text (as in the textbook); wider ones sit above it


def arrange_pictures(body):
    """An item/paragraph that starts with pictures keeps ALL its text in one place: beside the pictures (picture left,
    가:/나:/blank lines right, like the textbook) or, for a wide panel, under it — never one line beside and the next below."""
    out, pos = [], 0
    for m in PIC_LEAD.finditer(body):
        if m.start() < pos:
            continue
        opener, imgs = m.group(1), m.group(2)
        if opener.endswith('<p>'):
            end = body.find('</p>', m.end())
        else:                                          # tight list item: up to the item's end or its nested list
            ends = [e for e in (body.find('</li>', m.end()), body.find('<ul', m.end()), body.find('<ol', m.end())) if e != -1]
            end = min(ends) if ends else -1
        if end == -1:
            continue
        rest = body[m.end():end]
        if not re.sub(r'<[^>]+>|\s', '', rest) and 'class="wl' not in rest:
            continue                                   # pictures only: nothing to arrange
        wide = sum(int(x) for x in re.findall(r'width:(\d+)mm', imgs)) > PIC_SIDE_MM
        rest = re.sub(r'^\s*(<br\s*/?>\s*)+', '', rest)
        out.append(body[pos:m.start()] + opener +
                   f'<span class="picrow{" stack" if wide else ""}"><span class="pc">{imgs.strip()}</span><span class="pt">{rest}</span></span>')
        pos = end
    out.append(body[pos:])
    return ''.join(out)


def render_md(text):
    md_converter.reset()
    html = md_converter.convert(text)
    # WeasyPrint (70.0) ignores <ol start="N">; counter-reset: list-item N-1 is honoured.
    return re.sub(r'<ol start="(\d+)">',
                  lambda m: f'<ol start="{m.group(1)}" style="counter-reset: list-item {int(m.group(1)) - 1}">', html)


def convert_alerts(content):
    """Turn GitHub alert blockquotes (> [!TIP] optional title ...) into styled divs."""
    pattern = re.compile(
        r'^> ?\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION|INTRO|SUMMARY)\][ \t]*([^\n]*)\n((?:>.*\n?)*)',
        re.MULTILINE,
    )

    def repl(m):
        kind = m.group(1).lower()
        title = m.group(2).strip() or ALERT_LABELS[kind]
        if m.group(2).strip():
            title = ALERT_LABELS[kind].split(' ')[0] + ' ' + title      # keep the icon, custom text
        body = '\n'.join(re.sub(r'^> ?', '', line) for line in m.group(3).splitlines())
        inner = render_md(github_compat(body))
        return (f'<div class="alert alert-{kind}">'
                f'<div class="alert-title">{title}</div>{inner}</div>\n\n')

    return pattern.sub(repl, content)


def convert_details(content):
    """Expand <details> answer blocks so they show in print."""
    pattern = re.compile(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', re.DOTALL)

    def repl(m):
        inner = render_md(github_compat(m.group(2).strip()))
        return (f'<div class="answer"><div class="answer-title">✅ {m.group(1).strip()}</div>'
                f'{inner}</div>\n\n')

    return pattern.sub(repl, content)


HANGUL = re.compile(r'[가-힣ㄱ-ㅎㅏ-ㅣ]')
_SPAN_OPEN = r'<span class="k[a-z ]*">'
# a "word" = run of kotag span tags and plain characters; Markdown markup, table bars and tag brackets end a word
_CHUNK = re.compile(r'(?:' + _SPAN_OPEN + r'|</span>|[^\s<>|*_`\[\]{}])+')
_OPEN_RE = re.compile(_SPAN_OPEN)
_CODE_SPLIT = re.compile(r'(`+[^`\n]*?`+)')      # keeps the code spans as the odd parts of the split


def wrap_korean_words(text):
    """<span class="kw">…</span> around every space-delimited chunk that contains Hangul, so WeasyPrint
    (which ignores word-break: keep-all) never breaks 가까워요 into 가/까워요. Breaks still happen at spaces.
    Skips headings, raw-HTML lines and fenced code; leaves a chunk alone when its span tags are unbalanced
    (a kotag span whose text contains a space)."""
    out = []
    fence = False
    for line in text.split('\n'):
        s = line.lstrip()
        if s.startswith('```'):
            fence = not fence
            out.append(line); continue
        if fence or s.startswith('#') or s.startswith('<') or s.startswith('!['):
            out.append(line); continue

        def repl(m):
            chunk = m.group(0)
            if not HANGUL.search(chunk):
                return chunk
            if len(_OPEN_RE.findall(chunk)) != chunk.count('</span>'):
                return chunk
            return f'<span class="kw">{chunk}</span>'
        # inline code spans (`…`) are rendered verbatim by Markdown — HTML inside them would print literally
        parts = _CODE_SPLIT.split(line)
        out.append(''.join(part if i % 2 else _CHUNK.sub(repl, part) for i, part in enumerate(parts)))
    return '\n'.join(out)


ZWSP = '​'
_THAI_RUN = re.compile(r'[ก-๛]{4,}')
_THAI_CHAR = re.compile(r'[ก-๛]')
# a line may not start with a following vowel / tone mark, nor end on a leading vowel
_TH_NOSTART = set('ะัาำิีึืฺุูๅ'
                  '็่้๊๋์ํ๎')
_TH_LEAD = set('เแโใไ')
_TAG_SPLIT = re.compile(r'(<[^>]+>)')
_thai_cache = {}


def _can_break(left, right):
    return bool(left and right and _THAI_CHAR.match(left[-1]) and _THAI_CHAR.match(right[0])
                and right[0] not in _TH_NOSTART and left[-1] not in _TH_LEAD)


def _thai_words(run):
    if run not in _thai_cache:
        kotag._thai_init()
        out = ''
        for tok in kotag._th_tok(run):
            out += (ZWSP if _can_break(out, tok) else '') + tok
        _thai_cache[run] = out
    return _thai_cache[run]


def thai_break_opportunities(html):
    """Measured 2026-11-03: this WeasyPrint/Pango has no Thai line breaking — Thai has no spaces between words, so a
    Thai phrase never wraps and a table cell full of Thai pushes the table past the right margin. Put U+200B (invisible)
    between Thai words (PyThaiNLP, the tokenizer kotag already uses) and at colour-span boundaries between two Thai words.
    Text nodes only; <style> is skipped."""
    parts = _TAG_SPLIT.split(html)
    prev = None                                   # index of the last non-empty text part
    in_style = False
    for i, p in enumerate(parts):
        if i % 2:
            low = p[:7].lower()
            if low.startswith('<style'):
                in_style = True
            elif low.startswith('</style'):
                in_style = False
            continue
        if in_style or not p:
            continue
        if _THAI_CHAR.search(p):
            p = parts[i] = _THAI_RUN.sub(lambda m: _thai_words(m.group(0)), p)
            if prev is not None and _can_break(parts[prev], p):
                parts[prev] += ZWSP
        prev = i
    return ''.join(parts)


def github_compat(content):
    """Make GitHub-flavoured quirks work with Python-Markdown.

    - GitHub renders a table/list right after a paragraph line; Python-Markdown
      needs a blank line first.
    - Consecutive '>' lines (dialogue) should keep their line breaks.
    """
    out = []
    prev = ''
    for line in content.split('\n'):
        # Python-Markdown needs 4-space indents for nested list items
        line = re.sub(r'^ {2,3}(?=([-*+]|\d+\.)\s)', '    ', line)
        stripped = line.lstrip()
        starts_block = stripped.startswith('|') or re.match(r'([-*+]|\d+\.)\s', stripped)
        prev_stripped = prev.lstrip()
        prev_is_same_block = (prev_stripped.startswith('|') if stripped.startswith('|')
                              else bool(re.match(r'([-*+]|\d+\.)\s', prev_stripped)) or prev.startswith((' ', '\t')))
        if starts_block and prev.strip() and not prev_is_same_block and not prev_stripped.startswith('>'):
            out.append('')
        # A quoted table needs a bare '>' line before its header row, or Markdown glues it into the previous paragraph
        if (line.startswith('>') and line.lstrip('> ').startswith('|') and prev.startswith('>')
                and prev.strip() != '>' and not prev.lstrip('> ').startswith('|')):
            out.append('>')
            prev = '>'
        # Hard line break between consecutive quote lines
        if (line.startswith('>') and prev.startswith('>') and prev.strip() != '>' and line.strip() != '>'
                and not prev.lstrip('> ').startswith('|')):      # a quoted table row must not get a hard-break suffix
            out[-1] = out[-1].rstrip() + '  '
        out.append(line)
        prev = line
    return '\n'.join(out)


BOOK_MARK = '<!-- kmu:book -->'      # build.py puts this on the first line of the two guide books


def md_file_to_pdf(md_filename, pdf_dir=None):
    """Render one Markdown file; the PDF lands next to it, or in `pdf_dir` if given."""
    md_path = os.path.join(WORKSPACE, md_filename)
    pdf_name = os.path.splitext(os.path.basename(md_path))[0] + '.pdf'
    pdf_path = os.path.join(pdf_dir, pdf_name) if pdf_dir else os.path.splitext(md_path)[0] + '.pdf'
    if not os.path.exists(md_path):
        print(f'File not found: {md_path}')
        return

    with open(md_path, encoding='utf-8') as f:
        text = f.read()
    body_class = 'book' if text.lstrip().startswith(BOOK_MARK) else ('cover' if '[TOC]' in text else '')

    text = convert_images(text)                                    # ![…](img:ID) → <img> (before kotag: it skips '<' lines)
    text = kotag.braces_to_html(kotag.colorize_markdown(text))   # {c:…} → <span class="kc">
    text = wrap_korean_words(text)
    text = convert_alerts(text)
    text = convert_details(text)
    text = github_compat(text)
    body = arrange_pictures(render_md(text))      # picture + its text side by side (or stacked when wide)
    # a section heading that already carries its own number (06_quickref: "### 08. 안 …") gets no automatic counter
    body = re.sub(r'<h3 id="([^"]*)">(\s*(?:<[^>]+>\s*)*\d{1,2}\.)', r'<h3 id="\1" class="nonum">\2', body)
    body = thai_break_opportunities(body)         # Thai would otherwise never wrap (tables ran off the page)
    if body_class == 'book':                       # a short table is one unit: never split it across pages
        # a short paragraph directly before a table or a dialogue box (lead sentence or bold label) must not be left at a page bottom
        # (tried 11/16: the same for EVERY lead paragraph after a heading — pages with > 1/3 blank went 8 → 27 in By_Unit; rejected)
        body = re.sub(r'<p>((?:(?!</p>).)*)</p>(\s*)<(table|blockquote)',
                      lambda m: (('<p class="lead">' if len(re.sub(r'<[^>]+>', '', m.group(1))) < 220 else '<p>')
                                 + m.group(1) + '</p>' + m.group(2) + '<' + m.group(3)), body, flags=re.S)
        # a bold label line directly before a list ("⚠️ 주의", "ระวัง") stays with the first two bullets
        body = re.sub(r'<p>(<strong>(?:(?!</p>).)*</strong>)</p>(\s*)<(ul|ol)>',
                      lambda m: (f'<p class="lead">{m.group(1)}</p>{m.group(2)}<{m.group(3)}>'
                                 if len(re.sub(r'<[^>]+>', '', m.group(1))) < 80 else m.group(0)), body, flags=re.S)
        # a long callout or dialogue may split (kept whole it pushed half a page of white space ahead of it)
        def _long(m):
            plain = re.sub(r'<[^>]+>', '', m.group(0))
            return m.group(0) if len(plain) < 420 else m.group(0).replace(m.group(1), m.group(1)[:-1] + ' style="page-break-inside:auto">', 1)
        body = re.sub(r'(<div class="alert alert-(?!intro)[a-z]+">)\s*<div class="alert-title">.*?</div>.*?</div>', _long, body, flags=re.S)
        body = re.sub(r'(<blockquote>).*?</blockquote>', _long, body, flags=re.S)
        body = re.sub(r'<table>(.*?)</table>',
                      lambda m: ('<table class="keep">' if m.group(1).count('<tr') <= 7 and len(re.sub(r'<[^>]+>', '', m.group(1))) < 520
                                 else '<table>') + m.group(1) + '</table>',   # few rows AND little text: tall rows made 'short' tables half a page
                      body, flags=re.S)

    title = os.path.splitext(md_filename)[0]
    html = f"""<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8"><title>{title}</title>
<style>{CSS_STYLE}</style></head>
<body class="{body_class}">{kotag.LEGEND_HTML}{body}</body></html>"""

    if os.environ.get('KOTAG_DUMP'):
        with open(pdf_path + '.html', 'w', encoding='utf-8') as f:
            f.write(html)
    HTML(string=html, base_url=os.path.dirname(md_path)).write_pdf(pdf_path)
    print(f'Created: {pdf_path}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('usage: python3 scripts/make_pdf.py <file.md> [more.md ...] [--pdf-dir DIR]\n'
                 '       (normally you want scripts/build.py instead)')
    args = sys.argv[1:]
    pdf_dir = None
    if '--pdf-dir' in args:                      # python3 scripts/make_pdf.py a.md b.md --pdf-dir output
        i = args.index('--pdf-dir'); pdf_dir = args[i + 1]; del args[i:i + 2]
        os.makedirs(pdf_dir, exist_ok=True)
    for name in args:
        md_file_to_pdf(name, pdf_dir)
