#!/usr/bin/env python3
"""Mind maps from outline files — one per unit plus the combined map.

    python3 scripts/build_mindmaps.py            # every content/mindmaps/*.md
    python3 scripts/build_mindmaps.py unit19     # one outline (basename without .md)
    python3 scripts/build_mindmaps.py --check unit19   # parse + layout only, no files written

content/mindmaps/<name>.md  →  output/mindmaps/KMU_Mindmap_<name>.html  (self-contained, Google Fonts)
                               output/mindmaps/KMU_Mindmap_<name>.pdf   (WeasyPrint, local Noto fonts, one page)
                               output/mindmaps/KMU_Mindmap_<name>.png   (pdftoppm 150 dpi)

Outline grammar (Markdown-ish):
    # root label            ← one per file
    ## branch  [@left|@right]  ← level 1; side is optional, otherwise balanced automatically
    ### node                ← level 2
    - leaf                  ← level 3 (two-space indent = level 4, the maximum)
    label text "한국어 | ไทย" renders as a Korean line over a smaller Thai line.

Visual grammar = the diagram-design skill (paper/ink/muted tokens, 4px grid, rounded right-angle
connectors r=8 with a sibling bus, accessible SVG, header/legend/footer). The node budget is
exceeded on purpose: the user asked for detailed per-unit maps, so each level-1 branch gets one
desaturated hue so a reader can trace it across 40+ nodes. Coral stays on the root only.
"""
import datetime
import glob
import html
import os
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.expanduser('~/.local/lib/python3.12/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kotag                                   # colour-by-function for the Korean half of every label

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content', 'mindmaps')
OUT = os.path.join(ROOT, 'output', '1_Guides', 'mindmaps')
OUT_MD = os.path.join(ROOT, 'output', '_build', 'md', 'mindmaps')
NOTO_DIR = '/usr/share/fonts/truetype/noto'

# ---- tokens (diagram-design style-guide.md, light skin)
PAPER, PAPER2, INK, MUTED, SOFT = '#f5f5f5', '#ececec', '#2d3142', '#4f5d75', '#7a8399'
RULE, ACCENT, ACCENT_TINT = 'rgba(45,49,66,0.12)', '#eb6c36', 'rgba(235,108,54,0.08)'
HUES = ['#5e7a9b', '#7c8f6f', '#b8915a', '#9c6b50', '#6e6479', '#5f8a8b', '#8a6a8f', '#8f8a5a', '#a3645b', '#4f6d8a', '#7a8a5a', '#8c6d4f']
FONT_WEB = "'Geist','Noto Sans KR','Noto Sans Thai',sans-serif"
FONT_PRINT = "'Noto Sans CJK KR','Noto Sans Thai','Noto Sans',sans-serif"
FONT_LINK = ('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600'
             '&family=Geist+Mono:wght@400;500;600&family=Noto+Sans+KR:wght@400;500;600&family=Noto+Serif+KR:wght@400'
             '&family=Noto+Sans+Thai:wght@400;500;600&family=Noto+Serif+Thai:wght@400&display=swap')

# ---- per-level metrics (all multiples of 4)
#          kr_size, th_size, pad, h_single, h_double, boxed
METRICS = {0: (20, 12, 20, 48, 72, True),
           1: (14, 11, 12, 32, 48, True),
           2: (12, 11, 12, 28, 44, True),
           3: (12, 11, 8, 20, 36, False),
           4: (12, 11, 8, 20, 36, False)}
HGAP = 48                       # parent edge → child edge (bus sits half-way, at +24)
VGAP = {1: 32, 2: 16, 3: 8, 4: 8}   # vertical gap between siblings of that level
MARGIN = 32


class Node:
    def __init__(self, label, level, parent=None):
        label = label.strip().replace('\ufe0f', '')   # emoji presentation selector draws as a dotted circle in print
        m = re.search(r'\s@(left|right)\s*$', label)
        self.side_hint = m.group(1) if m else None
        if m:
            label = label[:m.start()]
        kr, _, th = label.partition(' | ')
        self.kr, self.th = kr.strip(), th.strip()
        self.level, self.parent, self.children = level, parent, []
        self.side = 1
        self.hue = INK
        kr_s, th_s, pad, h1, h2, self.boxed = METRICS[min(level, 4)]
        self.kr_size, self.th_size, self.pad = kr_s, th_s, pad
        w = max(text_w(self.kr, kr_s, bold=level <= 2), text_w(self.th, th_s) if self.th else 0)
        self.w = r4(w + 2 * pad)
        self.h = h2 if self.th else h1
        self.x = self.y = 0          # top-left corner
        self.h_sub = self.h

    # geometry helpers
    @property
    def x2(self): return self.x + self.w
    @property
    def cy(self): return self.y + self.h // 2
    @property
    def attach_y(self):           # leaves attach on their underline, boxes at mid-height
        return self.cy if self.boxed else self.y + self.h - 4


def r4(v):
    return int(-(-v // 4) * 4)    # ceil to multiple of 4


def text_w(s, size, bold=False):
    """diagram-design width budget: wide/full-width char = 1em, other = 0.6em, combining mark = 0."""
    em = 0.0
    for ch in s:
        if unicodedata.category(ch) in ('Mn', 'Me', 'Mc'):
            continue
        em += 1.0 if unicodedata.east_asian_width(ch) in ('W', 'F') else 0.6
    return em * size * (1.04 if bold else 1.0)


def parse(path):
    root, stack = None, {}
    with open(path, encoding='utf-8') as f:
        for raw in f:
            line = raw.rstrip('\n')
            if not line.strip() or line.lstrip().startswith('<!--'):
                continue
            m = re.match(r'^(#{1,3})\s+(.*)$', line)
            if m:
                level = len(m.group(1)) - 1
                node = Node(m.group(2), level, None if level == 0 else stack[level - 1])
            else:
                m = re.match(r'^(\s*)-\s+(.*)$', line)
                if not m:
                    sys.exit(f'{path}: cannot parse line: {line!r}')
                level = 3 + len(m.group(1)) // 2
                if level > 4:
                    sys.exit(f'{path}: deeper than level 4: {line!r}')
                parent_level = max(k for k in stack if k < level)   # a leaf may hang straight off a ## branch
                node = Node(m.group(2), level, stack[parent_level])
            if node.parent:
                node.parent.children.append(node)
            else:
                root = node
            stack[level] = node
            for k in [k for k in stack if k > level]:
                del stack[k]
    if root is None:
        sys.exit(f'{path}: no "# root" line')
    return root


# ---- layout
def measure(n):
    if not n.children:
        n.h_sub = n.h
        return n.h_sub
    gap = VGAP[n.children[0].level]
    total = sum(measure(c) for c in n.children) + gap * (len(n.children) - 1)
    n.h_sub = max(n.h, total)
    return n.h_sub


def place(n, edge_x, top, side):
    """edge_x = the node's inner edge (left edge on the right wing, right edge on the left wing)."""
    n.side = side
    n.y = top + r4((n.h_sub - n.h) // 2) if n.h_sub > n.h else top
    n.x = edge_x if side > 0 else edge_x - n.w
    if not n.children:
        return
    gap = VGAP[n.children[0].level]
    total = sum(c.h_sub for c in n.children) + gap * (len(n.children) - 1)
    cursor = top + r4((n.h_sub - total) // 2) if n.h_sub > total else top
    child_edge = n.x2 + HGAP if side > 0 else n.x - HGAP
    for c in n.children:
        place(c, child_edge, cursor, side)
        cursor += c.h_sub + gap


def layout(root):
    for i, b in enumerate(root.children):
        b.hue = HUES[i % len(HUES)]
        for d in walk(b):
            d.hue = b.hue
    for b in root.children:
        measure(b)
    # wings: honour @left/@right hints, balance the rest greedily by height (keeps declared order)
    right, left = [], []
    undecided = []
    for b in root.children:
        (right if b.side_hint == 'right' else left if b.side_hint == 'left' else undecided).append(b)
    hr, hl = sum(b.h_sub for b in right), sum(b.h_sub for b in left)
    for b in sorted(undecided, key=lambda b: -b.h_sub):
        if hr <= hl:
            right.append(b); hr += b.h_sub
        else:
            left.append(b); hl += b.h_sub
    order = {id(b): i for i, b in enumerate(root.children)}
    right.sort(key=lambda b: order[id(b)]); left.sort(key=lambda b: order[id(b)])
    gap = VGAP[1]
    H_r = sum(b.h_sub for b in right) + gap * max(len(right) - 1, 0)
    H_l = sum(b.h_sub for b in left) + gap * max(len(left) - 1, 0)
    H = max(H_r, H_l, root.h)
    root.y = r4((H - root.h) // 2)
    root.x = 0
    for wing, side in ((right, 1), (left, -1)):
        Hw = H_r if side > 0 else H_l
        cursor = r4((H - Hw) // 2)
        edge = root.x2 + HGAP if side > 0 else root.x - HGAP
        for b in wing:
            place(b, edge, cursor, side)
            cursor += b.h_sub + gap
    nodes = list(walk(root))
    min_x = min(n.x for n in nodes)
    max_x = max(n.x2 for n in nodes)
    dx = MARGIN - min_x
    for n in nodes:
        n.x += dx
        n.y += MARGIN
    return max_x - min_x + 2 * MARGIN, H + 2 * MARGIN, right, left


def walk(n):
    yield n
    for c in n.children:
        yield from walk(c)


# ---- drawing
def rgba(hex_color, a):
    h = hex_color.lstrip('#')
    return f'rgba({int(h[0:2], 16)},{int(h[2:4], 16)},{int(h[4:6], 16)},{a})'


def arc(sweep, x, y):
    return f'A 8 8 0 0 {sweep} {x} {y}'


def connectors(parent, children, side, color):
    """Rounded right-angle connectors: parent stub → vertical sibling bus → one stub per child."""
    out = []
    px = parent.x2 if side > 0 else parent.x
    py = parent.attach_y
    bus = px + 24 * side
    attrs = f'fill="none" stroke="{color}" stroke-width="1.2" stroke-linecap="round"'
    def child_edge(c):
        return c.x if side > 0 else c.x2
    if len(children) == 1:
        c = children[0]; cy = c.attach_y; cx = child_edge(c)
        if cy == py:
            out.append(f'<path d="M {px} {py} H {cx}" {attrs}/>')
        else:
            down = cy > py
            s1 = 1 if (side > 0) == down else 0
            s2 = 1 - s1
            d = (f'M {px} {py} H {bus - 8 * side} {arc(s1, bus, py + (8 if down else -8))} '
                 f'V {cy - (8 if down else -8)} {arc(s2, bus + 8 * side, cy)} H {cx}')
            out.append(f'<path d="{d}" {attrs}/>')
        return out
    out.append(f'<path d="M {px} {py} H {bus}" {attrs}/>')          # parent stub (T-junction on the bus)
    top, bot = children[0], children[-1]
    ty, by = top.attach_y, bot.attach_y
    s_top = 0 if side > 0 else 1
    s_bot = 0 if side > 0 else 1
    d = (f'M {child_edge(top)} {ty} H {bus + 8 * side} {arc(s_top, bus, ty + 8)} '
         f'V {by - 8} {arc(s_bot, bus + 8 * side, by)} H {child_edge(bot)}')
    out.append(f'<path d="{d}" {attrs}/>')
    for c in children[1:-1]:
        out.append(f'<path d="M {bus} {c.attach_y} H {child_edge(c)}" {attrs}/>')
    return out


def node_shapes(n):
    """Boxes and underlines only — text is added by node_text_svg (web) or node_text_html (print)."""
    out = []
    if n.level == 0:
        fill, stroke, sw, rx = ACCENT_TINT, ACCENT, 1.2, 8
    elif n.level == 1:
        fill, stroke, sw, rx = rgba(n.hue, 0.12), n.hue, 1.2, 6
    elif n.level == 2:
        fill, stroke, sw, rx = '#ffffff', rgba(n.hue, 0.7), 0.8, 6
    else:
        fill = stroke = sw = rx = None
    if n.boxed:
        out.append(f'<rect x="{n.x}" y="{n.y}" width="{n.w}" height="{n.h}" rx="{rx}" fill="{PAPER}"/>')
        out.append(f'<rect x="{n.x}" y="{n.y}" width="{n.w}" height="{n.h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    else:
        out.append(f'<rect x="{n.x}" y="{n.y}" width="{n.w}" height="{n.h}" fill="{PAPER}"/>')
        out.append(f'<path d="M {n.x} {n.attach_y} H {n.x2}" stroke="{rgba(n.hue, 0.45)}" stroke-width="0.8" fill="none"/>')
    return out


def kr_markup(kr, mode):
    """Korean label → tspans (svg) or spans (html) coloured by word function (scripts/kotag.py)."""
    e = html.escape
    tagged = kotag.tag_korean(kr)
    out, pos = [], 0
    for m in kotag.TAG_RE.finditer(tagged):
        out.append(e(tagged[pos:m.start()]))
        c, body = m.group(1), m.group(2)
        color = kotag.CLASSES[c.lower()][2]
        if mode == 'svg':
            deco = ' text-decoration="underline"' if c.isupper() else ''
            out.append(f'<tspan fill="{color}"{deco}>{e(body)}</tspan>')
        else:
            out.append(f'<span class="k{c.lower()}{" kh" if c.isupper() else ""}">{e(body)}</span>')
        pos = m.end()
    out.append(e(tagged[pos:]))
    return ''.join(out)


def node_text_svg(n, font):
    e = html.escape
    out = []
    if n.boxed:
        cx = n.x + n.w // 2
        if n.th:
            ky = n.y + n.kr_size + (n.h - n.kr_size - n.th_size - 4) // 2 - 2
            out.append(f'<text x="{cx}" y="{ky}" text-anchor="middle" font-family="{font}" font-size="{n.kr_size}" font-weight="600" fill="{INK}">{kr_markup(n.kr, 'svg')}</text>')
            out.append(f'<text x="{cx}" y="{ky + n.th_size + 4}" text-anchor="middle" font-family="{font}" font-size="{n.th_size}" fill="{MUTED}">{e(n.th)}</text>')
        else:
            out.append(f'<text x="{cx}" y="{n.cy + n.kr_size // 2 - 2}" text-anchor="middle" font-family="{font}" font-size="{n.kr_size}" font-weight="600" fill="{INK}">{kr_markup(n.kr, 'svg')}</text>')
    else:
        anchor = 'start' if n.side > 0 else 'end'
        tx = n.x + n.pad if n.side > 0 else n.x2 - n.pad
        ly = n.attach_y
        if n.th:
            out.append(f'<text x="{tx}" y="{n.y + n.kr_size + 1}" text-anchor="{anchor}" font-family="{font}" font-size="{n.kr_size}" fill="{INK}">{kr_markup(n.kr, 'svg')}</text>')
            out.append(f'<text x="{tx}" y="{ly - 4}" text-anchor="{anchor}" font-family="{font}" font-size="{n.th_size}" fill="{SOFT}">{e(n.th)}</text>')
        else:
            out.append(f'<text x="{tx}" y="{ly - 5}" text-anchor="{anchor}" font-family="{font}" font-size="{n.kr_size}" fill="{INK}">{kr_markup(n.kr, 'svg')}</text>')
    return out


def node_text_html(n):
    """Print variant: WeasyPrint's SVG text drops Thai combining marks (dotted circles), its HTML text does not —
    so every label becomes an absolutely positioned <div> over the SVG shapes."""
    e = html.escape
    th = f'<div class="th" style="font-size:{n.th_size}px">{e(n.th)}</div>' if n.th else ''
    if n.boxed:
        return (f'<div class="nd" style="left:{n.x}px;top:{n.y}px;width:{n.w}px;height:{n.h}px">'
                f'<div class="kr" style="font-size:{n.kr_size}px">{kr_markup(n.kr, "html")}</div>{th}</div>')
    side = 'r' if n.side > 0 else 'l'
    return (f'<div class="lf {side}" style="left:{n.x + n.pad}px;top:{n.y}px;width:{n.w - 2 * n.pad}px;height:{n.h - 4}px">'
            f'<div class="kr" style="font-size:{n.kr_size}px">{kr_markup(n.kr, "html")}</div>{th}</div>')


def render(root, slug, font, mono, text_mode='svg'):
    """Returns (svg, html_overlay, W, H). text_mode 'svg' puts labels in the SVG; 'html' returns them as divs."""
    W, H, right, left = layout(root)
    LEG = 76
    e = html.escape
    parts = [f'<svg viewBox="0 0 {W} {H + LEG}" width="{W}" height="{H + LEG}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="{slug}-title {slug}-desc">',
             f'<title id="{slug}-title">{e(root.kr)}</title>',
             f'<desc id="{slug}-desc">Mind map: {e(root.kr)} — {e(root.th)}. กิ่ง: {e(" · ".join(b.kr for b in root.children))}.</desc>',
             f'<rect width="100%" height="100%" fill="{PAPER}"/>']
    for wing, side in ((right, 1), (left, -1)):      # connectors first, behind the nodes
        if wing:
            parts += connectors(root, wing, side, MUTED)
        for b in wing:
            for n in walk(b):
                if n.children:
                    parts += connectors(n, n.children, side, n.hue)
    overlay = []
    for n in walk(root):
        parts += node_shapes(n)
        if text_mode == 'svg':
            parts += node_text_svg(n, font)
        else:
            overlay.append(node_text_html(n))
    y = H + 8                                           # legend strip (Korean/Latin only — safe in SVG text)
    parts.append(f'<line x1="{MARGIN}" y1="{y}" x2="{W - MARGIN}" y2="{y}" stroke="{RULE}" stroke-width="0.8"/>')
    parts.append(f'<text x="{MARGIN}" y="{y + 24}" font-family="{mono}" font-size="8" letter-spacing="0.14em" fill="{MUTED}">LEGEND</text>')
    x = MARGIN + 80
    for b in root.children:
        parts.append(f'<rect x="{x}" y="{y + 16}" width="12" height="12" rx="2" fill="{rgba(b.hue, 0.12)}" stroke="{b.hue}" stroke-width="1"/>')
        parts.append(f'<text x="{x + 20}" y="{y + 26}" font-family="{font}" font-size="12" font-weight="500" fill="{INK}">{e(b.kr)}</text>')
        x += r4(text_w(b.kr, 12, True)) + 48
    parts.append(f'<text x="{MARGIN}" y="{y + 52}" font-family="{mono}" font-size="8" letter-spacing="0.14em" fill="{MUTED}">COLOUR</text>')
    x = MARGIN + 80
    for c, (th, ko, color) in kotag.CLASSES.items():
        parts.append(f'<text x="{x}" y="{y + 54}" font-family="{font}" font-size="11" font-weight="500" fill="{color}">{e(ko)}</text>')
        x += r4(text_w(ko, 11, True)) + 28
    parts.append(f'<text x="{x}" y="{y + 54}" font-family="{font}" font-size="11" fill="{INK}" text-decoration="underline">높임</text>')
    parts.append('</svg>')
    return '\n'.join(parts), '\n'.join(overlay), W, H + LEG


def page(root, svg, overlay, W, H, source, print_mode=False):
    e = html.escape
    today = datetime.date.today().isoformat()
    if print_mode:
        font_css = f"""
    @font-face {{ font-family: 'Noto Sans Thai'; src: url('file://{NOTO_DIR}/NotoSansThai-Regular.ttf'); }}
    @font-face {{ font-family: 'Noto Sans Thai'; font-weight: bold; src: url('file://{NOTO_DIR}/NotoSansThai-Bold.ttf'); }}
    @page {{ size: {W + 64}px {H + 208}px; margin: 0; }}
    body {{ padding: 24px 32px; }}
    :root {{ --font-sans: {FONT_PRINT}; --font-serif: 'Noto Serif CJK KR','Noto Serif Thai',serif; --font-mono: 'Noto Sans Mono',monospace; }}
    .stage {{ position: relative; width: {W}px; height: {H}px; }}
    .stage svg {{ position: absolute; left: 0; top: 0; }}
    .nd {{ position: absolute; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; line-height: 1.15; }}
    .nd .kr {{ font-weight: 600; color: {INK}; white-space: nowrap; }}
    .nd .th {{ color: {MUTED}; margin-top: 2px; white-space: nowrap; }}
    .lf {{ position: absolute; display: flex; flex-direction: column; justify-content: flex-end; line-height: 1.2; }}
    .lf.r {{ text-align: left; }}  .lf.l {{ text-align: right; }}
    .lf .kr {{ color: {INK}; white-space: nowrap; }}
    .lf .th {{ color: {SOFT}; white-space: nowrap; }}
    {kotag.CSS_COLORS}
    """
        link = ''
        body = f'<div class="stage">{svg}\n{overlay}</div>'
    else:
        font_css = f"""
    :root {{ --font-sans: {FONT_WEB}; --font-serif: 'Instrument Serif','Noto Serif KR','Noto Serif Thai',serif; --font-mono: 'Geist Mono',ui-monospace,monospace; }}
    body {{ padding: 3rem 2rem; min-height: 100vh; display: flex; align-items: center; justify-content: center; }}
    """
        link = f'<link href="{FONT_LINK}" rel="stylesheet">'
        body = svg
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(root.kr)} · Mind map</title>
{link}
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  :root {{ --color-paper: {PAPER}; --color-ink: {INK}; --color-muted: {MUTED}; --color-accent: {ACCENT}; }}
  {font_css}
  body {{ font-family: var(--font-sans); background: var(--color-paper); color: var(--color-ink); }}
  .frame {{ width: {W}px; max-width: 100%; }}
  .eyebrow {{ font-family: var(--font-mono); font-size: 0.66rem; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; color: var(--color-muted); margin-bottom: 0.5rem; }}
  h1 {{ font-family: var(--font-serif); font-size: 1.75rem; font-weight: 400; letter-spacing: -0.02em; line-height: 1.15; margin-bottom: 0.25rem; }}
  .sub {{ font-family: var(--font-sans); font-size: 0.9rem; color: var(--color-muted); margin-bottom: 1.25rem; }}
  svg {{ width: {W}px; height: {H}px; display: block; }}
  footer {{ margin-top: 1rem; padding-top: 0.5rem; border-top: 1px solid {RULE}; font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.06em; color: var(--color-muted); }}
</style>
</head>
<body>
<div class="frame">
  <p class="eyebrow">Mind map · 국민한국어 1 · KMU Korean 1</p>
  <h1>{e(root.kr)}</h1>
  <p class="sub">{e(root.th)}</p>
  {body}
  <footer>source: content/mindmaps/{e(source)} · scripts/build_mindmaps.py · diagram-design grammar · {today}</footer>
</div>
</body>
</html>
"""


def build(path, check_only=False):
    name = os.path.splitext(os.path.basename(path))[0]
    slug = 'mm-' + name
    root = parse(path)
    n_nodes = sum(1 for _ in walk(root))
    if check_only:
        W, H, _, _ = layout(root)
        print(f'{name:10s}: OK · {n_nodes:3d} nodes · {W}×{H}px')
        return
    os.makedirs(OUT, exist_ok=True); os.makedirs(OUT_MD, exist_ok=True)
    svg, _, W, H = render(root, slug, FONT_WEB, "'Geist Mono',monospace", 'svg')
    html_path = os.path.join(OUT, f'KMU_Mindmap_{name}.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(page(root, svg, '', W, H, os.path.basename(path)))
    svg_p, overlay, _, _ = render(root, slug, FONT_PRINT, "'Noto Sans Mono',monospace", 'html')
    print_html = os.path.join(OUT_MD, f'KMU_Mindmap_{name}.print.html')
    with open(print_html, 'w', encoding='utf-8') as f:
        f.write(page(root, svg_p, overlay, W, H, os.path.basename(path), print_mode=True))
    from weasyprint import HTML
    pdf_path = os.path.join(OUT, f'KMU_Mindmap_{name}.pdf')
    HTML(print_html).write_pdf(pdf_path)
    subprocess.run(['pdftoppm', '-r', '150', '-png', '-singlefile', pdf_path, os.path.join(OUT, f'KMU_Mindmap_{name}')], check=True)
    print(f'{name:10s}: {n_nodes:3d} nodes · {W}×{H}px → {os.path.basename(html_path)} + .pdf + .png')


if __name__ == '__main__':
    args = sys.argv[1:]
    check = '--check' in args                      # parse + layout only (used by the outline-writing agents)
    args = [a for a in args if a != '--check']
    targets = args or sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(CONTENT, '*.md')))
    for t in targets:
        build(os.path.join(CONTENT, t + '.md'), check_only=check)
    if not args and not check:                     # full run: also bind every map into one PDF, all.pdf first
        pdfs = [os.path.join(OUT, 'KMU_Mindmap_all.pdf')] + sorted(
            p for p in glob.glob(os.path.join(OUT, 'KMU_Mindmap_unit*.pdf')))
        pdfs = [p for p in pdfs if os.path.exists(p)]
        bound = os.path.join(ROOT, 'output', '1_Guides', 'KMU_Mindmaps.pdf')
        subprocess.run(['pdfunite', *pdfs, bound], check=True)
        print(f'bound     : {len(pdfs)} maps -> output/1_Guides/KMU_Mindmaps.pdf')
