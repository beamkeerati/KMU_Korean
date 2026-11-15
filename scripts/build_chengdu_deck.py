#!/usr/bin/env python3
"""Build the 16:9 slide deck for the 기말 발표 (청두 여행, 11/24).

    python3 scripts/build_chengdu_deck.py   ->  output/6_Speaking/KMU_Speaking_TravelChengdu_Deck.pdf

Pictures: content/speaking/travel_chengdu_img/NNx_name.* (NN = slide). Each slide is one justified row: every
picture keeps its whole frame (people are never cut) unless CROP lists a box for it; all pictures in a row share
one height. Prepared copies go to extracted/slides/chengdu/ (regenerable).
"""
import os
import sys

sys.path.insert(0, os.path.expanduser('~/.local/lib/python3.12/site-packages'))
from PIL import Image, ImageOps
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'content', 'speaking', 'travel_chengdu_img')
TMP = os.path.join(ROOT, 'extracted', 'slides', 'chengdu')
OUT = os.path.join(ROOT, 'output', '6_Speaking', 'KMU_Speaking_TravelChengdu_Deck.pdf')

W, H = 338.67, 190.5            # mm, 16:9
MX = 12                         # side margin
TOP, BOT = 37, 157              # picture area (y from / to)
GAP = 4

# fractional crop boxes (left, top, right, bottom) — only where a stranger fills the foreground or the frame is empty
CROP = {
    '05b_old_street': (0, 0, 1, 0.60),        # keeps the wooden houses, lanterns and the panda; drops the crowd's faces
    '06a_marriage_corner': (0, 0.10, 1, 0.70),  # keeps the blue notice boards; drops the man next to the camera
    '08a_mall_night_wide': (0.45, 0.0, 1, 0.72),  # drops the dark railing
}

# (title, [pictures], keyword chips under the pictures)
SLIDES = [
    ('cover', ['01b_city_day', '01a_towers_night'], []),
    ('청두는 어떤 곳?', ['02a_map', '02b_panda_food'], ['중국 서쪽', '큰 도시', '판다 🐼', '매운 음식 🌶️']),
    ('언제? 누구와? 어떻게?', ['03b_friend', '03a_bike'], ['지난 8월', '태국 친구', '비행기 3시간 ✈️', '자전거 🚲', '지하철 🚇']),
    ('판다? <span class="x">✗</span> → 쇼핑몰!', ['04a_ifs_panda', '04c_global_center', '04b_screen', '04d_mall_night'],
     ['판다 🐼 &lt; 쇼핑몰 🛍️']),
    ('절 · 박물관', ['05a_garden_pond', '05c_temple_gate', '05b_old_street'], ['유명한 절', '박물관']),
    ('제일 좋았습니다: 인민공원', ['06a_marriage_corner', '06b_bike_day'], ['결혼할 사람 찾기 💍', '8월 = 더운 날씨 ☀️']),
    ('무슨 음식을 먹었습니까?', ['07a_spicy_pot', '07b_fried_dumpling'], ['훠궈', '매운 국수', '맵다 🌶️ → 맛있다!']),
    ('쇼핑 · 여행이 어땠습니까?', ['08b_mall_inside', '08a_mall_night_wide', '08c_bike_path', '08d_bridge_night'],
     ['구경 ○', '쇼핑 <span class="x">✗</span> (비싸다)', '3일', '즐거웠습니다 😊']),
    ('closing', ['09_closing'], []),
]
WHO = '1A · 빔'
RED, INK, CREAM = '#c0392b', '#2a2420', '#fbf6ee'
FRAME = 2.2                     # white photo border, mm


def prepare(name, cover=None):
    """-> (path of the prepared jpg, aspect ratio w/h). cover = target aspect: centre-crop to fill it (no people only)."""
    src = next(os.path.join(SRC, f) for f in os.listdir(SRC) if os.path.splitext(f)[0] == name)
    im = Image.open(src)
    im.seek(0)
    im = ImageOps.exif_transpose(im).convert('RGB')
    if name in CROP and not cover:
        l, t, r, b = CROP[name]
        im = im.crop((int(l * im.width), int(t * im.height), int(r * im.width), int(b * im.height)))
    if cover:
        im = ImageOps.fit(im, (int(1600 * cover), 1600), Image.LANCZOS, centering=(0.5, 0.62))
    im.thumbnail((2000, 2000), Image.LANCZOS)
    dst = os.path.join(TMP, name + ('_cover' if cover else '') + '.jpg')
    im.save(dst, quality=88)
    return dst, im.width / im.height


def row(pics, x0, y0, x1, y1):
    """Justified row of framed photos inside the box, centred. Up to 3 photos get a slight tilt."""
    items = [prepare(p) for p in pics]
    total = sum(a for _, a in items)
    pad = 2 * FRAME
    h = min(y1 - y0 - pad, (x1 - x0 - (GAP + pad) * len(items) + GAP) / total)
    width = h * total + (GAP + pad) * len(items) - GAP
    x, y, out = x0 + (x1 - x0 - width) / 2, y0 + (y1 - y0 - h - pad) / 2, []
    tilt = [-1.6, 1.4, -1.0] if len(items) <= 3 else [0, 0, 0, 0]
    for k, (path, a) in enumerate(items):
        w = h * a
        out.append(
            f'<div class="ph" style="left:{x:.2f}mm; top:{y:.2f}mm; width:{w + pad:.2f}mm; height:{h + pad:.2f}mm; '
            f'transform:rotate({tilt[k]}deg);"><div class="sh"></div><div class="fr"></div>'
            f'<img src="file://{path}" style="left:{FRAME}mm; top:{FRAME}mm; width:{w:.2f}mm; height:{h:.2f}mm;"></div>')
        x += w + pad + GAP
    return ''.join(out)


def dots(n):
    return '<div class="dots">' + ''.join(
        f'<span class="{"on" if k == n else "off"}"></span>' for k in range(1, len(SLIDES) + 1)) + '</div>'


def build():
    os.makedirs(TMP, exist_ok=True)
    pages = []
    for n, (title, pics, kw) in enumerate(SLIDES, 1):
        if title == 'cover':
            half = W / 2
            a, _ = prepare(pics[0], cover=half / H)
            b, _ = prepare(pics[1], cover=half / H)
            body = (f'<img class="bleed" src="file://{a}" style="left:0; top:0; width:{half}mm; height:{H}mm;">'
                    f'<img class="bleed" src="file://{b}" style="left:{half}mm; top:0; width:{half}mm; height:{H}mm;">'
                    '<div class="veil"></div>'
                    '<div class="card"><div class="ck">내가 여행한 곳</div><div class="ct">청두 여행</div>'
                    f'<div class="bar"></div><div class="cs">중국 청두 · 2026년 8월</div><div class="cn">{WHO}</div></div>')
        elif title == 'closing':
            path, _ = prepare(pics[0])
            body = (f'<img class="bleed" src="file://{path}" style="left:0; top:0; width:{W}mm; height:{H}mm;">'
                    '<div class="veil2"></div>'
                    '<div class="end"><div class="et">여러분도 청두에 꼭 가 보세요!</div>'
                    f'<div class="bar"></div><div class="es">감사합니다</div><div class="ew">{WHO}</div></div>')
        else:
            chips = ''.join(f'<span class="chip">{c}</span>' for c in kw)
            body = ('<div class="blob"></div><div class="blob2"></div><div class="side"></div>'
                    f'<div class="num">{n:02d}</div><div class="title">{title}</div><div class="rule"></div>'
                    + row(pics, MX + 6, TOP, W - MX, BOT) +
                    f'<div class="kw">{chips}</div>{dots(n)}<div class="who">청두 여행 · {WHO}</div>')
        pages.append(f'<section>{body}</section>')
    css = f"""
@page {{ size: {W}mm {H}mm; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: "Noto Sans CJK KR", sans-serif; color: {INK}; }}
section {{ position: relative; width: {W}mm; height: {H}mm; background: {CREAM}; overflow: hidden; page-break-after: always; }}
section:last-child {{ page-break-after: auto; }}
img {{ position: absolute; border-radius: 1.6mm; }}
img.bleed {{ border-radius: 0; }}
.blob {{ position: absolute; right: -45mm; top: -55mm; width: 150mm; height: 150mm; border-radius: 75mm; background: #f6e6d6; }}
.blob2 {{ position: absolute; left: -30mm; bottom: -50mm; width: 110mm; height: 110mm; border-radius: 55mm; background: #f8ecdf; }}
.side {{ position: absolute; left: 0; top: 0; width: 7mm; height: {H}mm; background: linear-gradient({RED}, #8e2a20); }}
.num {{ position: absolute; left: 15mm; top: 7mm; font-size: 46pt; font-weight: bold; color: {RED}; line-height: 1; }}
.title {{ position: absolute; left: 44mm; top: 11.5mm; width: {W - 60}mm; font-size: 31pt; font-weight: bold; line-height: 1.1; }}
.rule {{ position: absolute; left: 15mm; top: 29.5mm; width: {W - 30}mm; height: 0.5mm; background: #e2d3c2; }}
.ph {{ position: absolute; }}
.sh {{ position: absolute; left: 1.4mm; top: 1.8mm; right: -1.4mm; bottom: -1.8mm; background: rgba(60,35,20,.18); border-radius: 2.6mm; }}
.fr {{ position: absolute; left: 0; top: 0; right: 0; bottom: 0; background: white; border-radius: 2.4mm; border: 0.2mm solid #e6dbcd; }}
.kw {{ position: absolute; left: {MX}mm; top: 161.5mm; width: {W - 2 * MX}mm; text-align: center; }}
.chip {{ display: inline-block; margin: 0 2mm; padding: 1.6mm 6mm 2.2mm; background: white; border: 0.5mm solid {RED};
        border-radius: 8mm; font-size: 19pt; font-weight: bold; }}
.dots {{ position: absolute; left: 0; bottom: 5mm; width: {W}mm; text-align: center; }}
.dots span {{ display: inline-block; width: 2.6mm; height: 2.6mm; border-radius: 1.3mm; margin: 0 1.2mm; }}
.dots .on {{ background: {RED}; width: 9mm; }}
.dots .off {{ background: #dccbb8; }}
.who {{ position: absolute; right: 9mm; bottom: 4.2mm; font-size: 10pt; color: #9a8b7a; }}
.x {{ color: {RED}; }}
.veil {{ position: absolute; left: 0; top: 0; width: {W}mm; height: {H}mm; background: rgba(25,15,20,.28); }}
.card {{ position: absolute; left: {(W - 176) / 2}mm; top: 39mm; width: 176mm; height: 112mm; background: rgba(251,246,238,.94);
        border-radius: 6mm; text-align: center; padding-top: 13mm; border-top: 3mm solid {RED}; }}
.ck {{ font-size: 16pt; color: {RED}; font-weight: bold; letter-spacing: 1.5pt; }}
.ct {{ font-size: 66pt; font-weight: bold; line-height: 1.2; }}
.bar {{ width: 30mm; height: 1.6mm; background: {RED}; margin: 5mm auto; border-radius: 1mm; }}
.cs {{ font-size: 15pt; color: #6b5f52; }}
.cn {{ font-size: 22pt; font-weight: bold; margin-top: 5mm; }}
.veil2 {{ position: absolute; left: 0; top: 0; width: {W}mm; height: 105mm; background: linear-gradient(rgba(30,10,40,.62), rgba(30,10,40,0)); }}
.end {{ position: absolute; left: 0; top: 22mm; width: {W}mm; text-align: center; color: white; }}
.et {{ font-size: 44pt; font-weight: bold; }}
.end .bar {{ background: white; }}
.es {{ font-size: 26pt; }}
.ew {{ font-size: 14pt; margin-top: 4mm; color: #f3e6ea; }}
"""
    html = f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pages)}</body></html>'
    HTML(string=html).write_pdf(OUT)
    print('Created:', OUT, f'({len(SLIDES)} slides)')
    # one picture per slide next to the script (content/speaking/travel_chengdu_deck_N.jpg) for the script PDF
    import subprocess
    stem = os.path.join(TMP, 'page')
    subprocess.run(['pdftoppm', '-r', '75', '-jpeg', OUT, stem], check=True)
    for k in range(1, len(SLIDES) + 1):
        os.replace(f'{stem}-{k}.jpg', os.path.join(ROOT, 'content', 'speaking', f'travel_chengdu_deck_{k}.jpg'))


if __name__ == '__main__':
    build()
