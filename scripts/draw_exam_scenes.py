#!/usr/bin/env python3
"""Redrawn pictures for exam items that have no original to crop (agent: exams).
Run:  python3 scripts/draw_exam_scenes.py   -> content/img/gen/ex_*.png (used by content/img/exams.tsv)
Simple line-and-emoji scenes in the style of the book's black-and-white drawings; captions only where a paper would print them."""
import os
import sys

from PIL import Image, ImageDraw

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import crop_images as ci  # noqa: E402  (only its font + clock helpers)

OUT = os.path.join(ROOT, 'content', 'img', 'gen')
from PIL import ImageFont  # noqa: E402

EF = ImageFont.truetype(ci.EMOJI, 109)


def emoji(ch, size):
    im = Image.new('RGBA', (136, 136), (255, 255, 255, 0))
    ImageDraw.Draw(im).text((5, 5), ch, font=EF, embedded_color=True)
    bb = im.getbbox()
    im = im.crop(bb)
    k = size / max(im.size)
    return im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)


def put(canvas, ch, cx, cy, size):
    e = emoji(ch, size)
    canvas.paste(e, (round(cx - e.width / 2), round(cy - e.height / 2)), e)


def new(w=620, h=380):
    im = Image.new('RGB', (w, h), 'white')
    return im, ImageDraw.Draw(im)


def label(d, xy, text, size=38, anchor='mm'):
    d.text(xy, text, font=ci._kr(size), fill='#111', anchor=anchor)


def sign(d, cx, cy, text, size=38):
    f = ci._kr(size)
    w = int(d.textlength(text, font=f)) + 36
    d.rounded_rectangle([cx - w / 2, cy - size * 0.8, cx + w / 2, cy + size * 0.8], 10, outline='#333', width=4, fill='white')
    d.text((cx, cy), text, font=f, fill='#111', anchor='mm')


def save(im, name):
    im.save(os.path.join(OUT, name))


def pos_book_in_bag():
    im, d = new(420, 360)
    put(im, '📕', 210, 120, 150)
    put(im, '👜', 210, 215, 260)
    save(im, 'ex_pos_1.png')


def desk(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y0 + 22], fill='#a9743a', outline='#5a3a14', width=4)
    for x in (x0 + 18, x1 - 30):
        d.rectangle([x, y0 + 22, x + 12, y1], fill='#a9743a', outline='#5a3a14', width=3)


def pos_hat_on_desk():
    im, d = new(480, 340)
    desk(d, 80, 210, 400, 320)
    put(im, '🧢', 240, 150, 150)
    save(im, 'ex_pos_2.png')


def pos_clock_over_board():
    im, d = new(520, 540)
    d.rectangle([70, 330, 450, 500], fill='#2f5d3a', outline='#7a5a2a', width=12)
    d.line([(110, 470), (200, 470)], fill='white', width=4)
    c = ci._clock(3, 0, 270)
    im.paste(c, (260 - c.width // 2, 20))
    save(im, 'ex_pos_3.png')


def pos_store_post():
    im, d = new(560, 330)
    put(im, '🏪', 150, 140, 210)
    put(im, '🏤', 410, 140, 210)
    sign(d, 150, 270, '편의점')
    sign(d, 410, 270, '우체국')
    save(im, 'ex_pos_4.png')


def pos_street():
    im, d = new(560, 420)
    d.rectangle([0, 330, 560, 420], fill='#9a9a9a')
    d.line([(0, 375), (560, 375)], fill='white', width=6)
    put(im, '🏦', 280, 70, 110)
    sign(d, 280, 148, '은행', 30)
    put(im, '🏢', 280, 255, 170)
    sign(d, 280, 335, '서점', 32)
    save(im, 'ex_pos_5.png')


def pos_outside_class():
    im, d = new(600, 340)
    d.rectangle([40, 50, 330, 300], outline='#333', width=7, fill='#f4f1e6')
    d.rectangle([250, 140, 320, 300], outline='#333', width=5, fill='#c9a46a')
    sign(d, 150, 110, '교실')
    put(im, '🪑', 110, 235, 90)
    put(im, '🧑', 420, 230, 110)
    put(im, '🧑', 540, 230, 110)
    save(im, 'ex_pos_6.png')


def chair(d, x, y, s=1.0):
    """simple side-on chair; (x, y) = left end of the seat."""
    w, t, lg, bk = int(150 * s), int(16 * s), int(110 * s), int(130 * s)
    d.rectangle([x, y, x + w, y + t], fill='#a9743a', outline='#5a3a14', width=4)
    d.rectangle([x, y - bk, x + int(16 * s), y + t], fill='#a9743a', outline='#5a3a14', width=4)
    for dx in (int(8 * s), w - int(14 * s)):
        d.rectangle([x + dx, y + t, x + dx + int(12 * s), y + t + lg], fill='#a9743a', outline='#5a3a14', width=3)
    return w, t, lg, bk


def cats():
    im, d = new(1000, 410)
    base = 300
    for i, kind in enumerate(('on', 'under', 'beside')):
        ox = 40 + i * 320
        w, t, lg, bk = chair(d, ox + 30, base - 120)
        sy = base - 120
        if kind == 'on':
            put(im, '🐱', ox + 105, sy - 52, 100)
        elif kind == 'under':
            put(im, '🐱', ox + 105, sy + t + 52, 88)
        else:
            put(im, '🐱', ox + 250, base - 40, 100)
        label(d, (ox + 130, 372), '①②③'[i], 40)
        d.line([(ox, base + 6), (ox + 290, base + 6)], fill='#777', width=3)
    save(im, 'ex_cats.png')


def campus_map():
    im, d = new(640, 450)
    x0, y0, cw, ch = 40, 30, 180, 170
    for r in range(2):
        for c in range(3):
            d.rectangle([x0 + c * cw, y0 + r * ch, x0 + (c + 1) * cw, y0 + (r + 1) * ch], outline='#777', width=3, fill='#f6f6f6')
    cells = {(1, 0): ('🏢', '학생회관', None), (1, 1): ('🏢', None, '①'), (0, 1): ('🏢', None, '②'), (0, 2): ('🏢', None, '③')}
    for (r, c), (e, name, num) in cells.items():
        cx, cy = x0 + c * cw + cw / 2, y0 + r * ch + ch / 2 - 10
        put(im, e, cx, cy, 90)
        if name:
            sign(d, cx, cy + 62, name, 24)
        if num:
            d.ellipse([cx + 40, cy - 70, cx + 90, cy - 20], fill='white', outline='#333', width=4)
            label(d, (cx + 65, cy - 45), num, 34)
    label(d, (x0 + 1.5 * cw, y0 + 2 * ch + 44), '▼ 앞', 28)
    save(im, 'ex_map.png')


def calendar(name, marks, days=28, start=0, title=None, w=1000, circle=None):
    """4-week calendar (일..토), marks = {day: text}."""
    cols, rows = 7, 1 + (days + start + 6) // 7
    cw, rh = (w - 20) // cols, 70
    im, d = new(w, rows * rh + 20 + (60 if title else 0))
    top = 10 + (60 if title else 0)
    if title:
        label(d, (w / 2, 38), title, 40)
    for c, n in enumerate('일월화수목금토'):
        d.rectangle([10 + c * cw, top, 10 + (c + 1) * cw, top + rh], fill='#e4e4e4', outline='#222', width=3)
        label(d, (10 + c * cw + cw / 2, top + rh / 2), n, 36)
    f = ci._kr(30)
    for day in range(1, days + 1):
        i = day - 1 + start
        r, c = 1 + i // 7, i % 7
        x, y = 10 + c * cw, top + r * rh
        d.rectangle([x, y, x + cw, y + rh], outline='#222', width=3)
        d.text((x + 8, y + 6), str(day), font=ci._kr(28), fill='#111')
        if day in marks and marks[day] in ('🎂',):
            put(im, marks[day], x + cw / 2 + 22, y + rh / 2 + 8, 44)
        elif day in marks:
            d.text((x + cw / 2 + 10, y + rh / 2 + 6), marks[day], font=f, fill='#111', anchor='mm')
        if day == circle:
            d.ellipse([x + 6, y + 4, x + cw - 6, y + rh - 4], outline='#c62828', width=5)
    save(im, name)


def composite(name, parts, cols=3, cell=(300, 240)):
    """parts = [(PIL image, '1'), ...] laid out in a numbered grid (one panel for a whole 그림 section)."""
    rows = (len(parts) + cols - 1) // cols
    im, d = new(cols * (cell[0] + 20) + 10, rows * (cell[1] + 50) + 10)
    for i, (pic, lab) in enumerate(parts):
        k = min(cell[0] / pic.width, cell[1] / pic.height)
        pic = pic.convert('RGB').resize((round(pic.width * k), round(pic.height * k)), Image.LANCZOS)
        x, y = 10 + (i % cols) * (cell[0] + 20), 10 + (i // cols) * (cell[1] + 50)
        d.rectangle([x - 4, y - 4, x + cell[0] + 4, y + cell[1] + 34], outline='#999', width=2)
        im.paste(pic, (x + (cell[0] - pic.width) // 2, y + 34 + (cell[1] - pic.height) // 2))
        d.text((x + 8, y + 2), lab, font=ci._kr(28), fill='#111')
    save(im, name)


def main():
    pos_book_in_bag(); pos_hat_on_desk(); pos_clock_over_board(); pos_store_post(); pos_street(); pos_outside_class()
    cats(); campus_map()
    marks = {d_: '청소' for d_ in (1, 8, 15, 22)}
    marks[17] = '영화'
    calendar('ex_cal_alexei.png', marks, title='알렉세이 씨 달력')
    calendar('ex_cal_june.png', {16: '🎂'}, days=30, start=0, title='6월', w=760, circle=16)
    L = lambda n: Image.open(os.path.join(OUT, n))
    composite('ex_pos_all.png', [(L('ex_pos_1.png'), '1)'), (L('ex_pos_2.png'), '2)'), (L('ex_pos_3.png'), '3) · 8)'),
                                 (L('ex_pos_4.png'), '4)'), (L('ex_pos_5.png'), '5) · 6)'), (L('ex_pos_6.png'), '7)')])
    atm, ad = new(420, 330)
    put(atm, '👩', 110, 170, 190); put(atm, '🏧', 300, 150, 190); sign(ad, 300, 280, '은행', 30)
    atm.save(os.path.join(OUT, 'ex_atm.png'))
    composite('ex_q10_all.png', [(ci._clock(4, 45, 300), '1)'), (L('ex_cal_june.png'), '2)'), (atm, '3)')])
    print('done')


if __name__ == '__main__':
    main()
