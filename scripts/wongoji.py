#!/usr/bin/env python3
"""Lay a 발표 script out on the centre's 원고지 sheet (발표 (2): 20 cells per row, front 14 rows + back 16 rows = 600 cells) so it can be copied cell by cell.

    python3 scripts/wongoji.py <name>      # reads content/speaking/<name>.md, writes content/speaking/<name>_wongoji_N.png

Text = the numbered `**N. 한국어**` lines; every `### ` heading starts a new paragraph.
Rules applied: a paragraph starts with one empty cell · one character per cell · two digits / two lowercase letters share
a cell · no empty cell after . or , · one empty cell after ? and ! · a line never starts with a space or with . , ? !
(the mark shares the last cell of the line above).
"""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)
COLS, ROWS = 20, 14
SHEET = [14, 16]          # 발표 (2): front = 14 rows (to 280), back = 16 rows (300 … 600) -> 600 cells per sheet
FONT = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'


def kr_font(size):
    for i in range(8):
        try:
            f = ImageFont.truetype(FONT, size, index=i)
        except OSError:
            break
        if 'KR' in f.getname()[0]:
            return f
    return ImageFont.truetype(FONT, size)


def paragraphs(md):
    paras, cur = [], []
    for line in md.splitlines():
        if line.startswith('#'):
            if cur:
                paras.append(' '.join(cur)); cur = []
        m = re.match(r'\*\*\d+\.\s*(.+?)\*\*\s*$', line)
        if m:
            cur.append(m.group(1).strip())
    if cur:
        paras.append(' '.join(cur))
    return paras


def tokens(text):
    """Split into cell contents: pairs of digits / lowercase letters share a cell."""
    out, i = [], 0
    while i < len(text):
        c = text[i]
        if c.isdigit() and i + 1 < len(text) and text[i + 1].isdigit():
            out.append(text[i:i + 2]); i += 2
        elif c.isascii() and c.islower() and i + 1 < len(text) and text[i + 1].isascii() and text[i + 1].islower():
            out.append(text[i:i + 2]); i += 2
        else:
            out.append(c); i += 1
    return out


def layout(paras):
    """-> list of rows, each a list of COLS cell strings ('' = empty); a mark pushed back is appended to the last cell."""
    rows, row = [], []

    def flush():
        nonlocal row
        rows.append(row + [''] * (COLS - len(row))); row = []

    for p in paras:
        if row:
            flush()
        row = ['']                                   # paragraph indent
        toks = tokens(p)
        for k, t in enumerate(toks):
            if t == ' ':
                prev = toks[k - 1] if k else ''
                if prev in '.,':                     # no empty cell after . ,
                    continue
                if len(row) == COLS or not row:      # a line never starts with a space
                    if len(row) == COLS:
                        flush()
                    continue
                row.append('')
                continue
            if len(row) == COLS:
                if t in '.,?!':                      # mark shares the last cell
                    row[-1] += t
                    continue
                flush()
            row.append(t)
    if row:
        flush()
    return rows


def draw(rows, path, first_row, ROWS=ROWS):
    cell, gap, pad = 54, 22, 60
    w = pad * 2 + cell * COLS + 50
    h = pad * 2 + (cell + gap) * ROWS
    im = Image.new('RGB', (w, h), 'white')
    d = ImageDraw.Draw(im)
    f, small = kr_font(34), kr_font(20)
    for r in range(ROWS):
        y = pad + r * (cell + gap)
        cells = rows[r] if r < len(rows) else [''] * COLS
        for c in range(COLS):
            x = pad + c * cell
            d.rectangle([x, y, x + cell, y + cell], outline='#555', width=1)
            t = cells[c]
            if t:
                main, mark = (t[:-1], t[-1]) if len(t) > 1 and t[-1] in '.,?!' and not t[:-1].isascii() else (t, '')
                ff = f if len(main) == 1 else kr_font(26)
                if main in '.,':
                    d.text((x + 8, y + cell - 44), main, font=f, fill='black')
                else:
                    tw = d.textlength(main, font=ff)
                    d.text((x + (cell - tw) / 2 - (6 if mark else 0), y + (3 if len(main) == 1 else 9)), main, font=ff, fill='black')
                if mark:
                    d.text((x + cell - 13, y + cell - 40), mark, font=small, fill='black')
        n = (first_row + r + 1) * COLS
        if n % 100 == 0:
            d.text((pad + COLS * cell + 8, y + 16), str(n), font=small, fill='#888')
    im.save(path)


def main(name):
    src = os.path.join(ROOT, 'content', 'speaking', name + '.md')
    rows = layout(paragraphs(open(src, encoding='utf-8').read()))
    pages, start, i = [], 0, 0
    while start < len(rows):
        n = SHEET[i % len(SHEET)]
        pages.append((start, n, rows[start:start + n])); start += n; i += 1
    for i, (first, n, pg) in enumerate(pages, 1):
        draw(pg, os.path.join(ROOT, 'content', 'speaking', f'{name}_wongoji_{i}.png'), first, n)
    used = (len(rows) - 1) * COLS + sum(1 for i, c in enumerate(rows[-1]) if any(rows[-1][i:]))
    print(f'{name}: {len(rows)} rows = {len(pages)} side(s) (front 14 rows + back 16 rows = 600 cells per sheet) · ~{used} cells')


def main_plain(src, prefix, rows_per_side=10):
    """A plain-text essay (paragraphs separated by blank lines) on the 쓰기 sheet: 20 cells × 10 rows = 200 cells per side.
    Writes <prefix>_1.png, <prefix>_2.png … (the numbers 100/200/300 … in the margin as on the paper)."""
    paras = [' '.join(p.split()) for p in open(src, encoding='utf-8').read().split('\n\n') if p.strip() and not p.lstrip().startswith('#')]
    rows = layout(paras)
    out = []
    for i, start in enumerate(range(0, len(rows), rows_per_side), 1):
        path = f'{prefix}_{i}.png'
        draw(rows[start:start + rows_per_side], path, start, rows_per_side)
        out.append(path)
    used = (len(rows) - 1) * COLS + sum(1 for i, c in enumerate(rows[-1]) if any(rows[-1][i:]))
    print(f'{os.path.basename(src)}: {len(rows)} rows · ~{used} cells → ' + ' '.join(os.path.relpath(x, ROOT) for x in out))


if __name__ == '__main__':
    if sys.argv[1:2] == ['--plain']:          # python3 scripts/wongoji.py --plain content/img/gen/essay_season.txt content/img/gen/essay-season
        main_plain(sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1])
