#!/usr/bin/env python3
"""Colour VECTOR redraws of the pictures the 말하기 기말 uses (user 11/21: "ทำใหม่ ขอให้มีสี … คมชัด … เป็น vector"):
  gx-route1 · gx-route2   handout p.15 subway routes          gx-burger   handout p.15 hamburger shop
  gx-sign-1 … gx-sign-6   textbook 245쪽 연습 2 signs          gx-sign-panel   the six signs with the printed verbs
Run:  python3 scripts/draw_speaking_pics.py   -> content/img/gen/<id>.svg (vector, what make_pdf.py embeds) + <id>.png (raster for
      crop_images.py → the practice site). Ids are listed in content/img/final.tsv; the scanned originals stay as rv02-15-* / tb24-245-*.

Same layout and the same printed words as the paper — nothing added that the paper does not show. Shapes and Korean text are SVG;
the emoji are bitmaps (Noto Color Emoji has no vector outlines), enlarged 4× by Real-ESRGAN so they stay clean in print, and embedded
in the SVG as PNG data URIs (librsvg and WeasyPrint both draw emoji TEXT as black silhouettes)."""
import base64
import glob
import io
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import crop_images as ci  # noqa: E402  (emoji font path + the Real-ESRGAN tool)

OUT = os.path.join(ROOT, 'content', 'img', 'gen')
EMO = os.path.join(ROOT, 'extracted', 'img', '_emoji')      # 4× emoji cache (git-ignored, rebuilt on demand)
KR = 'Noto Sans CJK KR'
INK = '#1F2937'
RED = '#D7263D'
LINE = {1: '#0052A4', 3: '#EF7C1C', 4: '#00A5DE'}          # Seoul Metro line colours
EF = ImageFont.truetype(ci.EMOJI, 109)
EMO_PX = 288                                                # long side of an embedded emoji (≥ 500 dpi at its printed size)


def rsvg():
    for c in [shutil.which('rsvg-convert')] + glob.glob(os.path.expanduser('~/anaconda3/envs/*/bin/rsvg-convert')):
        if c and os.path.exists(c):
            return c
    sys.exit('rsvg-convert not found (apt install librsvg2-bin)')


# ---------------------------------------------------------------- emoji → clean high-resolution RGBA
def _key(ch):
    return '-'.join(f'{ord(c):x}' for c in ch)


def _strike(ch):
    """The font's own 109-px bitmap, with a transparent margin so the upscaler sees the edges."""
    im = Image.new('RGBA', (176, 166), (255, 255, 255, 0))
    ImageDraw.Draw(im).text((16, 16), ch, font=EF, embedded_color=True)
    x0, y0, x1, y1 = im.getbbox()
    return im.crop((x0 - 8, y0 - 8, x1 + 8, y1 + 8))


def prepare_emoji(chars):
    """Real-ESRGAN works on RGB: the colours (on white) and the alpha mask are enlarged separately, then the white is taken out again."""
    os.makedirs(EMO, exist_ok=True)
    todo = [c for c in dict.fromkeys(chars) if not os.path.exists(os.path.join(EMO, _key(c) + '.png'))]
    if not todo:
        return
    if not os.path.exists(ci.TOOL):
        for c in todo:                                           # no upscaler: plain enlargement
            im = _strike(c)
            im.resize((im.width * 3, im.height * 3), Image.LANCZOS).save(os.path.join(EMO, _key(c) + '.png'))
        return
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(f'{tmp}/in'); os.makedirs(f'{tmp}/out')
        for c in todo:
            im = _strike(c)
            a = im.getchannel('A')
            white = Image.new('RGB', im.size, 'white')
            white.paste(im, mask=a)
            white.save(f'{tmp}/in/{_key(c)}_c.png')
            Image.merge('RGB', (a, a, a)).save(f'{tmp}/in/{_key(c)}_a.png')
        subprocess.run([ci.TOOL, '-i', f'{tmp}/in', '-o', f'{tmp}/out', '-n', 'realesrgan-x4plus-anime', '-s', '4', '-f', 'png',
                        '-m', os.path.join(ci.TOOL_DIR, 'models')], capture_output=True, text=True)
        for c in todo:
            col = np.asarray(Image.open(f'{tmp}/out/{_key(c)}_c.png').convert('RGB')).astype(np.float32)
            a = np.asarray(Image.open(f'{tmp}/out/{_key(c)}_a.png').convert('L')).astype(np.float32) / 255
            a = np.clip((a - 0.04) / 0.92, 0, 1)
            rgb = np.clip((col - 255 * (1 - a[..., None])) / np.maximum(a[..., None], 0.02), 0, 255)
            rgba = np.dstack([rgb, a * 255]).astype(np.uint8)
            im = Image.fromarray(rgba, 'RGBA')
            im.crop(im.getbbox()).save(os.path.join(EMO, _key(c) + '.png'))
    print(f'emoji enlarged with Real-ESRGAN: {" ".join(todo)}')


class Pic:
    """One picture: SVG fragments + emoji placed by their centre."""

    def __init__(self, w, h):
        self.w, self.h, self.body, self._uri = w, h, [], {}

    def add(self, *parts):
        self.body.extend(parts)

    def emoji(self, ch, cx, cy, size):
        if ch not in self._uri:
            prepare_emoji([ch])
            im = Image.open(os.path.join(EMO, _key(ch) + '.png')).convert('RGBA')
            k = EMO_PX / max(im.size)
            im = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, 'PNG', optimize=True)
            self._uri[ch] = (im.width / max(im.size), im.height / max(im.size),
                             'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode())
        rw, rh, uri = self._uri[ch]
        w, h = size * rw, size * rh
        self.body.append(f'<image x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" href="{uri}" xlink:href="{uri}"/>')

    def save(self, name, zoom=2.0):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.w}" height="{self.h}" '
               f'viewBox="0 0 {self.w} {self.h}"><rect width="{self.w}" height="{self.h}" fill="#fff"/>{"".join(self.body)}</svg>')
        os.makedirs(OUT, exist_ok=True)
        dst = os.path.join(OUT, name + '.svg')
        open(dst, 'w', encoding='utf-8').write(svg)
        subprocess.run([rsvg(), '-z', str(zoom), dst, '-o', os.path.join(OUT, name + '.png')], check=True, stderr=subprocess.DEVNULL)
        print(f'{name}: {self.w}×{self.h} → content/img/gen/{name}.svg ({os.path.getsize(dst) // 1024} KB) + .png')


def text(x, y, s, size, fill=INK, weight=700, anchor='middle'):
    return (f'<text x="{x}" y="{y}" font-family="{KR}" font-weight="{weight}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}">{s}</text>')


def arrow(x0, y, x1, color=INK, width=12):
    head = width * 2.3
    return (f'<line x1="{x0}" y1="{y}" x2="{x1 - head}" y2="{y}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
            f'<polygon points="{x1},{y} {x1 - head * 1.25},{y - head * 0.8} {x1 - head * 1.25},{y + head * 0.8}" fill="{color}"/>')


def frame(w, h):
    return f'<rect x="5" y="5" width="{w - 10}" height="{h - 10}" rx="26" fill="#fff" stroke="#AAB6C5" stroke-width="5"/>'


# ---------------------------------------------------------------- 길 묻기 (subway route)
def route(name, label, stops, exit_no, place, place_colors, minutes):
    """stops = [(line, 한글, English)] × 3; place = (line 1, line 2) printed on the building."""
    w, h = 1650, 450
    p = Pic(w, h)
    xs = [250, 660, 1070]
    p.add(frame(w, h), text(34, 108, label, 54, anchor='start'))
    for (ln, kr, en), cx in zip(stops, xs):
        c = LINE[ln]
        p.add(f'<rect x="{cx - 128}" y="60" width="256" height="60" rx="30" fill="{c}"/>',
              text(cx, 103, f'지하철 {ln}호선', 35, '#fff'),
              f'<rect x="{cx - 152}" y="160" width="304" height="128" rx="64" fill="#fff" stroke="{c}" stroke-width="8"/>',
              f'<circle cx="{cx - 100}" cy="224" r="37" fill="{c}"/>',
              text(cx - 100, 240, ln, 46, '#fff'),
              text(cx + 40, 232, kr, 46, '#111'),
              text(cx + 38, 264, en, 19 if len(en) < 19 else 16, '#6B7280', 400))
    for i in (0, 1):                                            # the arrow has the colour of the line you ride
        mx = (xs[i] + xs[i + 1]) / 2
        p.add(arrow(xs[i] + 166, 224, xs[i + 1] - 166, LINE[stops[i][0]]),
              f'<rect x="{mx - 78}" y="350" width="156" height="66" rx="33" fill="#FFF4C2" stroke="#E0B93B" stroke-width="4"/>',
              text(mx, 397, f'{minutes[i]}분', 40))
    p.add(f'<circle cx="{xs[1]}" cy="383" r="46" fill="#fff" stroke="{INK}" stroke-width="6"/>')
    p.emoji('🚇', xs[1], 383, 54)
    ex = 1250                                                   # exit sign (Seoul exits: yellow plate, black number)
    p.add(f'<rect x="{ex}" y="132" width="128" height="196" rx="16" fill="{INK}"/>',
          f'<rect x="{ex + 10}" y="224" width="108" height="94" rx="10" fill="#FFD400"/>',
          text(ex + 64, 264, f'{exit_no}번', 36, '#111'), text(ex + 64, 304, '출구', 33, '#111'))
    p.emoji('🚇', ex + 64, 180, 66)
    bx, body, roof = 1418, place_colors[0], place_colors[1]     # building with its name on it
    p.add(f'<polygon points="{bx - 16},148 {bx + 206},148 {bx + 180},92 {bx + 10},92" fill="{roof}"/>',
          f'<rect x="{bx}" y="148" width="190" height="220" fill="{body}"/>')
    for wx in (bx + 22, bx + 78, bx + 134):
        p.add(f'<rect x="{wx}" y="164" width="34" height="26" rx="4" fill="#FFF7D6"/>')
    fs = 44 if len(place[1]) < 3 else 40
    p.add(f'<rect x="{bx + 72}" y="314" width="46" height="54" rx="6" fill="#FFF7D6"/>',
          text(bx + 95, 242, place[0], fs, '#fff'), text(bx + 95, 294, place[1], fs, '#fff'),
          f'<line x1="{bx - 30}" y1="370" x2="{bx + 220}" y2="370" stroke="#9CA3AF" stroke-width="5" stroke-linecap="round"/>')
    p.save(name)


# ---------------------------------------------------------------- 햄버거 가게
def person(cx, top, skin, hair, shirt, cap=None, arm=None):
    """A flat cartoon figure: head centre (cx, top + 44); the body runs down from there (clip it with the scene)."""
    hy = top + 44
    s = [f'<rect x="{cx - 52}" y="{hy + 46}" width="104" height="260" rx="34" fill="{shirt}"/>',
         f'<rect x="{cx - 13}" y="{hy + 30}" width="26" height="30" fill="{skin}"/>']
    if arm:                                                     # (x, y) of the hand
        s.append(f'<line x1="{cx + (40 if arm[0] > cx else -40)}" y1="{hy + 86}" x2="{arm[0]}" y2="{arm[1]}" stroke="{shirt}" '
                 f'stroke-width="26" stroke-linecap="round"/><circle cx="{arm[0]}" cy="{arm[1]}" r="15" fill="{skin}"/>')
    s.append(f'<circle cx="{cx}" cy="{hy}" r="42" fill="{skin}"/>')
    s.append(f'<path d="M{cx - 42},{hy - 2} a42,42 0 0 1 84,0 q-42,-26 -84,0z" fill="{hair}"/>')
    if cap:
        s.append(f'<path d="M{cx - 44},{hy - 12} a44,40 0 0 1 88,0z" fill="{cap}"/>'
                 f'<rect x="{cx - 14}" y="{hy - 20}" width="74" height="12" rx="6" fill="{cap}"/>')
    s.append(f'<circle cx="{cx - 15}" cy="{hy + 6}" r="5" fill="#222"/><circle cx="{cx + 15}" cy="{hy + 6}" r="5" fill="#222"/>')
    s.append(f'<path d="M{cx - 13},{hy + 21} q13,12 26,0" fill="none" stroke="#B4533A" stroke-width="5" stroke-linecap="round"/>')
    return ''.join(s)


def curved(x0, x1, y, color=INK):
    """The sheet's big arrow that arcs from one thing over to the next."""
    r = (x1 - x0) / 2
    return (f'<path d="M{x0},{y} a{r},{r * 0.82} 0 0 1 {x1 - x0 - 6},-4" fill="none" stroke="{color}" stroke-width="13" stroke-linecap="round"/>'
            f'<polygon points="{x1 + 4},{y + 34} {x1 - 34},{y - 8} {x1 + 26},{y - 16}" fill="{color}"/>')


def burger():
    w, h = 1720, 620
    p = Pic(w, h)
    p.add(frame(w, h))
    for cx, t, c in [(195, '〈햄버거 가게〉', '#FFE3B8'), (565, '〈주문〉', '#FFD9D9'), (905, '〈식사/포장〉', '#D9ECFF'),
                     (1215, '〈영수증〉', '#DDF3DF'), (1535, '〈얼음〉', '#D5F3F8')]:
        tw = 44 + 36 * len(t)
        p.add(f'<rect x="{cx - tw / 2}" y="34" width="{tw}" height="62" rx="31" fill="{c}"/>', text(cx, 79, t, 36))
    # 1) the shop: clerk behind the counter, customer in front
    x0, y0, sw, sh = 36, 128, 318, 446
    s = [f'<clipPath id="shop"><rect x="{x0}" y="{y0}" width="{sw}" height="{sh}" rx="18"/></clipPath><g clip-path="url(#shop)">',
         f'<rect x="{x0}" y="{y0}" width="{sw}" height="{sh}" fill="#FFF6E3"/>']
    for i in range(8):                                          # awning
        c = '#E63946' if i % 2 == 0 else '#FFFFFF'
        s.append(f'<rect x="{x0 + i * 40}" y="{y0}" width="40" height="46" fill="{c}"/><circle cx="{x0 + i * 40 + 20}" cy="{y0 + 46}" r="20" fill="{c}"/>')
    s.append(f'<rect x="{x0 + 22}" y="{y0 + 84}" width="{sw - 44}" height="78" rx="10" fill="#2D3142"/>')       # menu board
    s.append(person(x0 + 92, y0 + 186, '#F7CDA4', '#3B2A20', '#E63946', cap='#E63946'))
    s.append(f'<rect x="{x0}" y="{y0 + 330}" width="196" height="{sh - 330}" fill="#C98B55"/>')                 # counter
    s.append(f'<rect x="{x0}" y="{y0 + 318}" width="206" height="22" rx="8" fill="#8A5A33"/>')
    s.append(f'<rect x="{x0 + 138}" y="{y0 + 262}" width="52" height="58" rx="6" fill="#4B5563"/>'              # till
             f'<rect x="{x0 + 145}" y="{y0 + 269}" width="38" height="24" rx="3" fill="#A7F3D0"/>')
    s.append(person(x0 + 252, y0 + 200, '#F2C29B', '#1F2937', '#3A86FF', arm=(x0 + 196, y0 + 300)))
    s.append(f'</g><rect x="{x0}" y="{y0}" width="{sw}" height="{sh}" rx="18" fill="none" stroke="#D9A066" stroke-width="5"/>')
    p.add(*s)
    for ch, dx, size in [('🍔', 80, 52), ('🍟', 158, 50), ('🥤', 236, 52)]:
        p.emoji(ch, x0 + dx, y0 + 123, size)
    # 2) the order: two sets
    for i, (label, badge) in enumerate([('불고기버거 세트', '🐮'), ('치킨버거 세트', '🐔')]):
        cy = 150 + i * 222
        p.add(f'<rect x="420" y="{cy - 22}" width="290" height="206" rx="20" fill="#FFFBF2" stroke="#F4A261" stroke-width="5"/>',
              text(565, cy + 166, label, 33))
        for ch, ex, ey, size in [('🍔', 526, 62, 96), ('🍟', 612, 72, 64), ('🥤', 670, 68, 66), (badge, 452, 10, 46)]:
            p.emoji(ch, ex, cy + ey, size)
    # 3) eat in or take out
    p.add('<rect x="790" y="150" width="230" height="170" rx="20" fill="#EEF6FF" stroke="#7FB3E6" stroke-width="5"/>',
          text(905, 296, '매장 식사', 40),
          '<line x1="800" y1="351" x2="1010" y2="351" stroke="#6B7280" stroke-width="6" stroke-dasharray="14 12" stroke-linecap="round"/>',
          '<rect x="790" y="382" width="230" height="170" rx="20" fill="#FFF3E6" stroke="#E9A15B" stroke-width="5"/>',
          text(905, 528, '포장', 40))
    p.emoji('🍽', 905, 210, 84)
    p.emoji('🛍', 905, 442, 84)
    # 4) the receipt goes into the bin
    p.add(curved(1150, 1290, 286))
    p.emoji('🧾', 1140, 400, 128)
    p.emoji('🗑', 1292, 414, 132)
    # 5) ice goes into the cola
    p.add(curved(1446, 1590, 286))
    cx = 1614                                                   # a glass of cola with ice
    p.add(f'<polygon points="{cx - 62},330 {cx + 62},330 {cx + 46},520 {cx - 46},520" fill="#F3FAFD" stroke="#6B7280" stroke-width="6" stroke-linejoin="round"/>',
          f'<polygon points="{cx - 55},376 {cx + 55},376 {cx + 43},514 {cx - 43},514" fill="#6B3A1E"/>')
    for ix, iy, rot in [(-26, 392, -12), (16, 384, 14), (-6, 432, 8)]:
        p.add(f'<rect x="{cx + ix - 20}" y="{iy - 20}" width="40" height="40" rx="7" fill="#DDF4FB" stroke="#8ECFE3" stroke-width="4" '
              f'transform="rotate({rot} {cx + ix} {iy})"/>')
    p.add(f'<line x1="{cx + 24}" y1="500" x2="{cx + 50}" y2="290" stroke="#E63946" stroke-width="10" stroke-linecap="round"/>')
    p.emoji('🧊', 1452, 420, 112)
    for x in (366, 728, 1036, 1356):                             # the sheet's arrows from one step to the next
        p.add(arrow(x, 351, x + 46, INK, 10))
    p.save('gx-burger')


# ---------------------------------------------------------------- 245쪽 연습 2: six "don't" signs
SIGNS = ['먹다', '지각하다', '이야기하다', '만지다', '담배를 피우다', '사진을 찍다']


def sign(p, n, ox, oy, k=1.0):
    """Sign n (1–6) in a 480 × 480 box at (ox, oy), scaled by k. Like the book: red ring, the bar runs from bottom left to top right."""
    X, Y = (lambda v: ox + v * k), (lambda v: oy + v * k)
    if n == 1:
        p.emoji('🍝', X(240), Y(246), 236 * k)
    elif n == 2:                                                # the book's grey block is a school building (user 11/21)
        p.emoji('🏫', X(240), Y(244), 240 * k)
    elif n == 3:
        p.emoji('👧', X(172), Y(270), 156 * k)
        p.emoji('👩', X(312), Y(270), 156 * k)
        p.emoji('💬', X(240), Y(148), 92 * k)
    elif n == 4:
        p.emoji('✋', X(240), Y(240), 250 * k)
    elif n == 5:
        p.emoji('🚬', X(240), Y(244), 240 * k)
    else:
        p.emoji('📷', X(240), Y(244), 236 * k)
    d = 142
    p.add(f'<line x1="{X(240 - d)}" y1="{Y(240 + d)}" x2="{X(240 + d)}" y2="{Y(240 - d)}" stroke="{RED}" stroke-width="{38 * k}"/>',
          f'<circle cx="{X(240)}" cy="{Y(240)}" r="{200 * k}" fill="none" stroke="{RED}" stroke-width="{44 * k}"/>')


def signs():
    for n in range(1, 7):
        p = Pic(480, 480)
        sign(p, n, 0, 0)
        p.save(f'gx-sign-{n}')
    w, h = 1700, 930                                            # the book's panel: number + verb over each sign
    p = Pic(w, h)
    for i, verb in enumerate(SIGNS):
        cx, top = 290 + (i % 3) * 560, 30 + (i // 3) * 460
        p.add(text(cx - 190, top + 58, f'{i + 1}. {verb}', 50, INK, 700, 'start'))
        sign(p, i + 1, cx - 180, top + 84, 0.75)
    p.save('gx-sign-panel', zoom=1.5)


if __name__ == '__main__':
    route('gx-route1', '1)', [(4, '길음역', 'Gireum Station'), (3, '충무로역', 'Chungmuro Station'), (3, '경복궁역', 'Gyeongbokgung Station')],
          3, ('국민', '호텔'), ('#E76F51', '#9D4234'), (15, 10))
    route('gx-route2', '2)', [(4, '길음역', 'Gireum Station'), (1, '서울역', 'Seoul Station'), (1, '시청역', 'City Hall Station')],
          4, ('국민', '백화점'), ('#6D5BD0', '#4838A3'), (10, 10))
    burger()
    signs()
