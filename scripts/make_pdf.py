#!/usr/bin/env python3
"""Convert the Markdown study sheets in this folder to PDF.

Usage:  python3 make_pdf.py                 # converts the default sheets
        python3 make_pdf.py "Some File.md"  # converts specific files

Uses WeasyPrint (per-glyph font fallback) so Thai, Korean, Latin and emoji
all render correctly. Fonts: Noto family only.
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

# Noto everywhere: Latin -> Noto Sans, Thai -> Noto Sans Thai,
# Korean -> Noto Sans CJK KR, emoji -> Noto Color Emoji.
# Latin/Thai/Mono are loaded straight from files so fontconfig cannot
# substitute another font (e.g. TeX Live's Mezenets) for them.
NOTO_DIR = '/usr/share/fonts/truetype/noto'
FONT_FACES = f"""
@font-face {{ font-family: 'KMU Latin'; font-weight: normal; src: url('file://{NOTO_DIR}/NotoSans-Regular.ttf'); }}
@font-face {{ font-family: 'KMU Latin'; font-weight: bold;   src: url('file://{NOTO_DIR}/NotoSans-Bold.ttf'); }}
@font-face {{ font-family: 'KMU Thai';  font-weight: normal; src: url('file://{NOTO_DIR}/NotoSansThai-Regular.ttf'); }}
@font-face {{ font-family: 'KMU Thai';  font-weight: bold;   src: url('file://{NOTO_DIR}/NotoSansThai-Bold.ttf'); }}
@font-face {{ font-family: 'KMU Mono';  font-weight: normal; src: url('file://{NOTO_DIR}/NotoSansMono-Regular.ttf'); }}
@font-face {{ font-family: 'KMU Mono';  font-weight: bold;   src: url('file://{NOTO_DIR}/NotoSansMono-Bold.ttf'); }}
"""
# NOTE: don't list 'Noto Color Emoji' here — doing so makes fontconfig pick
# TeX Live's Mezenets for Latin/digits. Emoji fall back to it automatically.
FONT_STACK = "'KMU Latin', 'KMU Thai', 'Noto Sans CJK KR', 'Noto Sans Symbols2', 'Noto Sans Math'"
MONO_STACK = "'KMU Mono', 'KMU Thai', 'Noto Sans CJK KR', 'Noto Sans Symbols2'"

CSS_STYLE = FONT_FACES + f"""
@page {{
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-center {{
        content: counter(page) " / " counter(pages);
        font-family: {FONT_STACK}; font-size: 9px; color: #8c959f;
    }}
}}
body {{ font-family: {FONT_STACK}; line-height: 1.75; color: #1f2328; font-size: 12.5px; }}
p {{ margin: 6px 0 10px; }}

/* ---- headings: h1 = part/unit banner, h2 = chapter (own page), h3 = exercise/section ---- */
h1 {{
    font-size: 24px; color: #fff; background: #0f4c81;
    padding: 12px 16px; margin: 0 0 18px; border-radius: 6px;
    page-break-before: always; page-break-after: avoid;
}}
h1:first-of-type {{ page-break-before: auto; }}
h2 {{
    font-size: 19px; color: #0f4c81; margin: 0 0 14px;
    padding: 8px 0 8px 12px; border-left: 6px solid #0f4c81; background: #f0f6fc;
    page-break-before: always; page-break-after: avoid;
}}
h3 {{
    font-size: 15px; color: #1a4d7a; margin: 22px 0 8px; padding-bottom: 4px;
    border-bottom: 1.5px solid #d0d7de; page-break-after: avoid;
}}
h4 {{ font-size: 13.5px; color: #333; margin: 16px 0 6px; page-break-after: avoid; }}
h1 + h2, h2 + h3 {{ page-break-before: auto; }}   /* no blank page after a banner */

/* ---- tables ---- */
table {{ border-collapse: collapse; width: 100%; margin: 10px 0 16px; font-size: 12px; page-break-inside: auto; }}
th, td {{ border: 1px solid #d0d7de; padding: 7px 10px; vertical-align: top; }}
th {{ background: #e8f0f8; color: #0f4c81; font-weight: bold; text-align: left; }}
tr:nth-child(even) td {{ background: #f8fafc; }}
tr {{ page-break-inside: avoid; }}

/* ---- lists & exercise items: breathing room ---- */
ul, ol {{ margin: 6px 0 12px; padding-left: 26px; }}
li {{ margin: 5px 0; }}
li > ul, li > ol {{ margin: 3px 0 4px; }}

/* ---- write-in space ---- */
.wl {{ display: block; height: 2.4em; margin: 2px 0 6px; border-bottom: 1.2px solid #6e7781; }}
.wl2 {{ display: block; height: 5.2em; margin: 2px 0 8px;
        background: repeating-linear-gradient(to bottom, transparent 0, transparent 2.5em, #6e7781 2.5em, #6e7781 calc(2.5em + 1.2px)); }}

/* ---- code / mono ---- */
code {{ font-family: {MONO_STACK}; font-size: 11.5px; background: #f6f8fa; padding: 1px 5px; border-radius: 4px; }}
pre {{ font-family: {MONO_STACK}; font-size: 11.5px; background: #f6f8fa; padding: 10px 12px; border-radius: 6px;
       border: 1px solid #d0d7de; white-space: pre-wrap; margin: 8px 0 14px; }}
pre code {{ background: none; padding: 0; }}

blockquote {{ margin: 10px 0 14px; padding: 8px 14px; color: #3a3f44; border-left: 4px solid #0f4c81; background: #f6f8fa; border-radius: 0 6px 6px 0; }}
hr {{ border: none; border-top: 1px solid #d0d7de; margin: 18px 0; }}
img {{ max-width: 100%; }}
strong {{ color: #0b2e4f; }}

/* ---- callouts ---- */
.alert {{ border-left: 5px solid; border-radius: 0 6px 6px 0; padding: 9px 14px; margin: 12px 0 16px; page-break-inside: avoid; }}
.alert p {{ margin: 4px 0; }}
.alert-title {{ font-weight: bold; margin-bottom: 3px; }}
.alert-note      {{ background: #ddf4ff; border-color: #0969da; }}
.alert-tip       {{ background: #dafbe1; border-color: #1a7f37; }}
.alert-important {{ background: #fbefff; border-color: #8250df; }}
.alert-warning   {{ background: #fff8c5; border-color: #9a6700; }}
.alert-caution   {{ background: #ffebe9; border-color: #cf222e; }}
.answer {{ background: #f6f8fa; border: 1px dashed #8c959f; border-radius: 6px; padding: 8px 12px; margin: 8px 0 14px; }}
.answer-title {{ font-weight: bold; margin-bottom: 4px; }}

/* ---- TOC ---- */
.toc {{ font-size: 11.5px; line-height: 1.55; column-count: 2; column-gap: 24px; }}
.toc ul {{ padding-left: 16px; margin: 0; }}
.toc li {{ margin: 1px 0; }}
.toc a {{ color: #0f4c81; text-decoration: none; }}
@page {{ @top-center {{ content: element(klegend); }} }}
""" + kotag.CSS_COLORS

ALERT_LABELS = {
    'note': 'ℹ️ NOTE',
    'tip': '💡 TIP',
    'important': '❗ IMPORTANT',
    'warning': '⚠️ WARNING',
    'caution': '🛑 CAUTION',
}

md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists', 'toc'])


def render_md(text):
    md_converter.reset()
    html = md_converter.convert(text)
    # WeasyPrint (70.0) ignores <ol start="N">; counter-reset: list-item N-1 is honoured.
    return re.sub(r'<ol start="(\d+)">',
                  lambda m: f'<ol start="{m.group(1)}" style="counter-reset: list-item {int(m.group(1)) - 1}">', html)


def convert_alerts(content):
    """Turn GitHub alert blockquotes (> [!TIP] ...) into styled divs."""
    pattern = re.compile(
        r'^> ?\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\][ \t]*\n((?:>.*\n?)*)',
        re.MULTILINE,
    )

    def repl(m):
        kind = m.group(1).lower()
        body = '\n'.join(re.sub(r'^> ?', '', line) for line in m.group(2).splitlines())
        inner = render_md(github_compat(body))
        return (f'<div class="alert alert-{kind}">'
                f'<div class="alert-title">{ALERT_LABELS[kind]}</div>{inner}</div>\n\n')

    return pattern.sub(repl, content)


def convert_details(content):
    """Expand <details> answer blocks so they show in print."""
    pattern = re.compile(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', re.DOTALL)

    def repl(m):
        inner = render_md(github_compat(m.group(2).strip()))
        return (f'<div class="answer"><div class="answer-title">✅ {m.group(1).strip()}</div>'
                f'{inner}</div>\n\n')

    return pattern.sub(repl, content)


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
        # Hard line break between consecutive quote lines
        if line.startswith('>') and prev.startswith('>') and prev.strip() != '>' and line.strip() != '>':
            out[-1] = out[-1].rstrip() + '  '
        out.append(line)
        prev = line
    return '\n'.join(out)


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

    text = kotag.braces_to_html(kotag.colorize_markdown(text))   # {c:…} → <span class="kc">
    text = convert_alerts(text)
    text = convert_details(text)
    text = github_compat(text)
    body = render_md(text)

    title = os.path.splitext(md_filename)[0]
    html = f"""<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8"><title>{title}</title>
<style>{CSS_STYLE}</style></head>
<body>{kotag.LEGEND_HTML}{body}</body></html>"""

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
