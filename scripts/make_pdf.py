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

    text = kotag.braces_to_html(kotag.colorize_markdown(text))   # {c:…} → <span class="kc">
    text = wrap_korean_words(text)
    text = convert_alerts(text)
    text = convert_details(text)
    text = github_compat(text)
    body = render_md(text)
    # a section heading that already carries its own number (06_quickref: "### 08. 안 …") gets no automatic counter
    body = re.sub(r'<h3 id="([^"]*)">(\s*(?:<[^>]+>\s*)*\d{1,2}\.)', r'<h3 id="\1" class="nonum">\2', body)
    body = thai_break_opportunities(body)         # Thai would otherwise never wrap (tables ran off the page)

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
