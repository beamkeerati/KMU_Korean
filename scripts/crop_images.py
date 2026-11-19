#!/usr/bin/env python3
"""Real pictures for the exercises — crops from the source scans (textbook, workbook, teacher's papers) or redrawn images.

Manifests: content/img/*.tsv (one per area, so parallel writers never touch the same file). Tab-separated, '#' = comment:
    id      src                                             page  box (% of page: x0 y0 x1 y1)  w   note
    tb24-245-signs  source/textbook/KMU student's book unit 24.pdf  4  14 22 72 41               80  ป้ายห้าม 6 ป้าย
  id   : [a-z0-9-]+, unique over all manifests
  src  : a PDF under source/ (rendered at DPI) or an image file (content/img/gen/*.png for redrawn pictures, extracted/…)
         or card:<panel> → <panel> | <panel> — a drawn picture; panel = emoji (single code points) · clock=7:30 · text=3,500원,
         optional @caption under it (only what the paper itself printed: a name, a price — never the answer word)
  page : 1-based PDF page (empty for an image src)
  box  : four numbers in % of the page (empty = the whole page/image); white margins are trimmed automatically
  w    : display width in the PDFs, % of the text width (empty = the picture's printed size, i.e. as big as on paper)
  note : Thai description (alt text; the content keeps its own 🖼️ caption line)

Content refers to a picture as  ![🖼️ caption](img:ID)  (Markdown, make_pdf.py) or  "img": "ID" / ["ID", …]  (practice-site JSON,
item or section). Crops land in extracted/img/ID.jpg (git-ignored, regenerated from the manifests).

usage:
  python3 scripts/crop_images.py                 build every missing/changed crop, then --check
  python3 scripts/crop_images.py --only ID …     rebuild these crops and write previews (extracted/img/_preview/ID.png)
  python3 scripts/crop_images.py --sheet ID … | --sheet content/img/X.tsv
                                                 build them and put them all on ONE labelled contact sheet (extracted/img/_sheet_….png)
  python3 scripts/crop_images.py --grid SRC PAGE page image with a % grid (to pick a box) → extracted/img/_grid/…png
  python3 scripts/crop_images.py --check         every img:ID used in content/ exists in a manifest (exit 1 if not)
"""
import glob
import hashlib
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFESTS = os.path.join(ROOT, 'content', 'img')
OUT = os.path.join(ROOT, 'extracted', 'img')
PAGES = os.path.join(OUT, '_pages')
DPI = 300                 # crops (the scans are ~340 ppi); the PDFs print them at their natural size (TEXT_PX = text width at this DPI)
TEXT_PX = 1984            # 168 mm text width at 300 dpi
MAX_PX = 2400
ID_RE = re.compile(r'^[a-z0-9][a-z0-9-]*$')
USE_MD = re.compile(r'\]\(img:([a-z0-9-]+)\)')


def load_manifest(strict=True):
    """{id: row} over every content/img/*.tsv. strict: a malformed or duplicate row raises SystemExit; otherwise it is
    reported on stderr and skipped (so one writer's bad row never blocks another writer's --only/--sheet run)."""
    rows, errs = {}, []
    for path in sorted(glob.glob(os.path.join(MANIFESTS, '*.tsv'))):
        if os.path.basename(path).startswith('map_'):          # practice-site mappings (scripts/apply_pic_map.py), not pictures
            continue
        for ln, line in enumerate(open(path, encoding='utf-8'), 1):
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            f = line.rstrip('\n').split('\t')
            f += [''] * (6 - len(f))
            iid, src, page, box, w, note = (x.strip() for x in f[:6])
            where = f'{os.path.relpath(path, ROOT)}:{ln}'
            if not ID_RE.match(iid):
                errs.append(f'{where}: bad id {iid!r}'); continue
            if iid in rows:
                errs.append(f'{where}: duplicate id {iid} (first in {rows[iid]["where"]})'); continue
            if not src.startswith('card:') and not os.path.exists(os.path.join(ROOT, src)):
                errs.append(f'{where}: {iid}: src not found: {src}'); continue
            try:
                b = [float(x) for x in box.replace(',', ' ').split()] if box else None
                if b is not None and (len(b) != 4 or not (0 <= b[0] < b[2] <= 100 and 0 <= b[1] < b[3] <= 100)):
                    raise ValueError
            except ValueError:
                errs.append(f'{where}: {iid}: box must be 4 numbers 0–100 (x0 y0 x1 y1), got {box!r}'); continue
            try:
                w = float(w) if w else None
            except ValueError:
                errs.append(f'{where}: {iid}: w (5th column) must be a number or empty, got {w!r} — 6 tab-separated columns: id src page box w note'); continue
            if src.lower().endswith('.pdf') and not page.isdigit():
                errs.append(f'{where}: {iid}: a PDF src needs a page number'); continue
            rows[iid] = dict(id=iid, src=src, page=int(page) if page.isdigit() else None, box=b,
                             w=w, note=note, where=where)
    if errs:
        if strict:
            raise SystemExit('\n'.join(errs))
        print('\n'.join('WARNING ' + e for e in errs), file=sys.stderr)
    return rows


EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
SANS = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'


def _kr(size):
    for i in range(10):
        try:
            f = ImageFont.truetype(SANS, size, index=i)
        except OSError:
            break
        if 'KR' in f.getname()[0]:
            return f
    return ImageFont.truetype(SANS, size)


def _clock(h, m, size=230):
    import math
    im = Image.new('RGB', (size, size), 'white'); d = ImageDraw.Draw(im)
    c, r = size / 2, size / 2 - 8
    d.ellipse([c - r, c - r, c + r, c + r], outline='#222', width=7, fill='#fffdf5')
    for k in range(60):
        a = math.radians(k * 6); r1 = r - (20 if k % 5 == 0 else 9)
        d.line([(c + r1 * math.sin(a), c - r1 * math.cos(a)), (c + (r - 6) * math.sin(a), c - (r - 6) * math.cos(a))],
               fill='#222', width=5 if k % 5 == 0 else 2)
    f = _kr(26)
    for n in range(1, 13):
        a = math.radians(n * 30); rr = r - 42
        d.text((c + rr * math.sin(a), c - rr * math.cos(a)), str(n), font=f, fill='#222', anchor='mm')
    for ang, ln, w in ((math.radians((h % 12) * 30 + m * 0.5), r * 0.5, 10), (math.radians(m * 6), r * 0.78, 6)):
        d.line([(c, c), (c + ln * math.sin(ang), c - ln * math.cos(ang))], fill='#111', width=w)
    d.ellipse([c - 9, c - 9, c + 9, c + 9], fill='#c62828')
    return im


def _panel(p):
    """One panel of a card: emoji string · clock=H:MM · text=… ; '@label' adds a caption under it."""
    p, _, label = p.partition('@')
    p = p.strip()
    if p.startswith('clock='):
        h, m = p[6:].split(':'); body = _clock(int(h), int(m))
    elif p.startswith('text='):
        f = _kr(64); t = p[5:]
        w = int(ImageDraw.Draw(Image.new('RGB', (1, 1))).textlength(t, font=f)) + 50
        body = Image.new('RGB', (w, 120), 'white'); d = ImageDraw.Draw(body)
        d.rounded_rectangle([3, 3, w - 4, 116], 16, outline='#333', width=4); d.text((w / 2, 60), t, font=f, fill='#111', anchor='mm')
    else:
        chars = [ch for ch in p if ch not in '\ufe0f\u200d ']
        ef = ImageFont.truetype(EMOJI, 109)
        body = Image.new('RGB', (136 * max(1, len(chars)) + 10, 140), 'white')
        d = ImageDraw.Draw(body)
        for i, ch in enumerate(chars):
            d.text((5 + 136 * i, 6), ch, font=ef, embedded_color=True)
        body = body.resize((round(body.width * 1.25), round(body.height * 1.25)), Image.LANCZOS)
    if label.strip():
        f = _kr(40); t = label.strip()
        tw = int(ImageDraw.Draw(body).textlength(t, font=f))
        out = Image.new('RGB', (max(body.width, tw + 20), body.height + 64), 'white')
        out.paste(body, ((out.width - body.width) // 2, 0))
        ImageDraw.Draw(out).text((out.width / 2, body.height + 32), t, font=f, fill='#111', anchor='mm')
        body = out
    return body


def draw_card(spec):
    """card:<panel> [→ <panel>] [| <panel>] … — a clear drawn picture for an item whose paper had none we can crop
    (or whose scan is unreadable). → draws the book's red arrow between panels, | leaves a gap."""
    parts = re.split(r'\s+(→|\|)\s+', spec.strip())
    panels, seps = [_panel(x) for x in parts[0::2]], parts[1::2]
    gap = 90
    W = sum(x.width for x in panels) + gap * len(seps) + 40
    H = max(x.height for x in panels) + 40
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    x = 20
    for i, pn in enumerate(panels):
        im.paste(pn, (x, (H - pn.height) // 2)); x += pn.width
        if i < len(seps):
            if seps[i] == '→':
                y = H // 2
                d.polygon([(x + 18, y - 9), (x + 50, y - 9), (x + 50, y - 22), (x + 74, y), (x + 50, y + 22), (x + 50, y + 9), (x + 18, y + 9)], fill='#c62828')
            x += gap
    return im


def page_image(src, page):
    """The source page as a PIL image at DPI (PDF pages cached in extracted/img/_pages); card:… specs are drawn."""
    if src.startswith('card:'):
        return draw_card(src[5:])
    path = os.path.join(ROOT, src)
    if not src.lower().endswith('.pdf'):
        return Image.open(path).convert('RGB')
    os.makedirs(PAGES, exist_ok=True)
    key = hashlib.sha1(f'{src}|{page}|{DPI}|{os.path.getmtime(path)}'.encode()).hexdigest()[:16]
    cache = os.path.join(PAGES, key + '.jpg')
    if not os.path.exists(cache):
        from pdf2image import convert_from_path
        im = convert_from_path(path, dpi=DPI, first_page=page, last_page=page)[0].convert('RGB')
        im.save(cache, quality=93)
    return Image.open(cache).convert('RGB')


def trim(im, pad=10, thr=238):
    """Cut near-white margins (a loose box still gives a tight picture)."""
    g = im.convert('L').point(lambda v: 255 if v < thr else 0)
    bb = g.getbbox()
    if not bb:
        return im
    x0, y0, x1, y1 = bb
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))


def stamp_of(r):
    mt = 0 if r['src'].startswith('card:') else os.path.getmtime(os.path.join(ROOT, r['src']))
    return hashlib.sha1(json.dumps([r['src'], r['page'], r['box'], mt, remaster_policy(r) and REMASTER_VER]).encode()).hexdigest()


# ---------------------------------------------------------------- remaster (user 11/19: "ชัด สดใส คมเหมือน svg")
# Real-ESRGAN (ncnn-vulkan, GPU) redraws each scanned crop 4× sharper; the result is kept at 2× the scan size, the paper is made
# pure white and colours a little livelier. Halftone/photocopy dots are smoothed first, or the model erases faces (pilot 11/19).
# Without the tool (extracted/tools/esrgan, git-ignored) the plain crop is used.
TOOL_DIR = os.path.join(ROOT, 'extracted', 'tools', 'esrgan')
TOOL = os.path.join(TOOL_DIR, 'realesrgan-ncnn-vulkan')
RAW = os.path.join(OUT, '_raw')
REMASTER_VER = 'r1'
DOTTY = 28.0                 # mean high-frequency energy on ink pixels: teacher photocopies ≈ 30–33, book print ≈ 20


def remaster_policy(r):
    """ESRGAN model for this crop, or None (drawn cards, generated scenes and essays are already clean)."""
    if r['src'].startswith('card:') or re.match(r'(gx|cd|essay)-', r['id']):
        return None
    return 'realesrgan-x4plus' if r['id'].startswith('lc') else 'realesrgan-x4plus-anime'


def _dotty(g):
    import numpy as np
    g = np.asarray(g, dtype=np.float32)
    import cv2
    hf = np.abs(g - cv2.GaussianBlur(g, (0, 0), 1.5))
    ink = g < 235
    return float(hf[ink].mean()) if ink.mean() > 0.02 else 0.0


def remaster(rows, ids):
    """Raw crops in RAW/<id>.jpg → OUT/<id>.jpg; returns the ids remastered (others are copied as they are)."""
    import shutil, subprocess, tempfile
    import cv2, numpy as np
    todo = {}
    for iid in ids:
        pol = remaster_policy(rows[iid])
        if pol and os.path.exists(TOOL):
            todo.setdefault(pol, []).append(iid)
        else:
            shutil.copyfile(os.path.join(RAW, iid + '.jpg'), os.path.join(OUT, iid + '.jpg'))
    done = []
    for model, group in todo.items():
        with tempfile.TemporaryDirectory(dir=OUT) as tmp:
            os.makedirs(f'{tmp}/in'); os.makedirs(f'{tmp}/out')
            meta = {}
            for iid in group:
                raw = cv2.imread(os.path.join(RAW, iid + '.jpg'))
                h, w = raw.shape[:2]
                img = raw
                hsv = cv2.cvtColor(raw, cv2.COLOR_BGR2HSV)
                colour = float(np.mean(hsv[..., 1] > 60)) > 0.04
                if not colour and _dotty(cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)) >= DOTTY:
                    img = cv2.GaussianBlur(img, (0, 0), 1.0)
                    if w >= 260:
                        img = cv2.resize(img, (w // 2, h // 2), interpolation=cv2.INTER_AREA)
                if img.shape[1] > 1000:
                    img = cv2.resize(img, (1000, round(img.shape[0] * 1000 / img.shape[1])), interpolation=cv2.INTER_AREA)
                cv2.imwrite(f'{tmp}/in/{iid}.png', img)
                meta[iid] = (w, h, colour)
            res = subprocess.run([TOOL, '-i', f'{tmp}/in', '-o', f'{tmp}/out', '-n', model, '-s', '4', '-f', 'png',
                                  '-m', os.path.join(TOOL_DIR, 'models')], capture_output=True, text=True)
            for iid in group:
                w, h, colour = meta[iid]
                out = cv2.imread(f'{tmp}/out/{iid}.png')
                if out is None:                      # the tool failed for this one: keep the plain crop
                    shutil.copyfile(os.path.join(RAW, iid + '.jpg'), os.path.join(OUT, iid + '.jpg')); continue
                tw = min(MAX_PX, w * 2)
                out = cv2.resize(out, (tw, round(h * tw / w)), interpolation=cv2.INTER_AREA)
                f = np.clip((out.astype(np.float32) - 14.0) * 255.0 / (232.0 - 14.0), 0, 255).astype(np.uint8)
                if colour:
                    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV).astype(np.float32)
                    hsv[..., 1] = np.clip(hsv[..., 1] * 1.3, 0, 255)
                    f = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
                cv2.imwrite(os.path.join(OUT, iid + '.jpg'), f, [cv2.IMWRITE_JPEG_QUALITY, 90])
                done.append(iid)
    return done


def natural_px(iid):
    """(w, h) of the plain crop at 300 dpi — the printed size; a remastered file is 2× larger."""
    for d in (RAW, OUT):
        try:
            return Image.open(os.path.join(d, iid + '.jpg')).size
        except OSError:
            pass
    return None


def build(rows, only=None):
    os.makedirs(OUT, exist_ok=True)
    stamps_path = os.path.join(OUT, '_stamps.json')
    try:
        stamps = json.load(open(stamps_path))
    except (OSError, ValueError):
        stamps = {}
    made, fresh = 0, []
    os.makedirs(RAW, exist_ok=True)
    for iid, r in rows.items():
        dst = os.path.join(OUT, iid + '.jpg')
        st = stamp_of(r)
        if only is None and os.path.exists(dst) and stamps.get(iid) == st:
            continue
        if only is not None and iid not in only:
            continue
        im = page_image(r['src'], r['page'])
        if r['box']:
            x0, y0, x1, y1 = r['box']
            im = im.crop((round(x0 / 100 * im.width), round(y0 / 100 * im.height),
                          round(x1 / 100 * im.width), round(y1 / 100 * im.height)))
        im = trim(im)
        if im.width > MAX_PX:
            im = im.resize((MAX_PX, round(im.height * MAX_PX / im.width)), Image.LANCZOS)
        im.save(os.path.join(RAW, iid + '.jpg'), quality=92)
        fresh.append(iid)
        stamps[iid] = st
        made += 1
        if only is not None:
            os.makedirs(os.path.join(OUT, '_preview'), exist_ok=True)
            pv = im.copy()
            pv.thumbnail((900, 900))
            pv.save(os.path.join(OUT, '_preview', iid + '.png'))
            print(f'{iid}: {im.width}×{im.height}px → extracted/img/_preview/{iid}.png')
    if fresh:
        n = len(remaster(rows, fresh))
        if n:
            print(f'remastered {n} crop(s) with Real-ESRGAN')
    try:                                   # several writers may run at once: merge with what is on disk, replace atomically
        stamps = {**json.load(open(stamps_path)), **{k: v for k, v in stamps.items()}}
    except (OSError, ValueError):
        pass
    tmp = f'{stamps_path}.{os.getpid()}'
    json.dump(stamps, open(tmp, 'w'), indent=0)
    os.replace(tmp, stamps_path)
    return made


def sheet(ids, name='_sheet'):
    """All the given crops on one labelled image (extracted/img/<name>.png, ≤ 1600 px wide) — check many crops at one glance."""
    ims = []
    for iid in ids:
        try:
            im = Image.open(os.path.join(OUT, iid + '.jpg')).convert('RGB')
        except OSError:
            print(f'not built: {iid}'); continue
        im.thumbnail((380, 300)); ims.append((iid, im))
    W, x, y, rowh, pos = 1600, 0, 0, 0, []
    for iid, im in ims:
        if x + im.width > W:
            x, y, rowh = 0, y + rowh + 30, 0
        pos.append((x, y)); x += im.width + 16; rowh = max(rowh, im.height)
    out = Image.new('RGB', (W, y + rowh + 32), 'white'); d = ImageDraw.Draw(out)
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    for (iid, im), (px, py) in zip(ims, pos):
        out.paste(im, (px, py + 22)); d.rectangle([px, py + 22, px + im.width - 1, py + 22 + im.height - 1], outline='#bbb')
        d.text((px, py + 2), iid, fill=(200, 0, 0), font=f)
    path = os.path.join(OUT, name + '.png')
    out.save(path)
    print(os.path.relpath(path, ROOT), f'({len(ims)} pictures)')


def display_width(r):
    """% of the text width the PDF prints this picture at."""
    if r['w']:
        return max(8.0, min(100.0, r['w']))
    size = natural_px(r['id'])
    if not size:
        return 40.0
    px = size[0]
    return max(12.0, min(100.0, round(100 * px / TEXT_PX, 1)))


def grid(src, page):
    im = page_image(src, int(page) if page else None)
    im.thumbnail((1300, 1800))
    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    except OSError:
        font = None
    for p in range(0, 101, 5):
        x = round(p / 100 * (im.width - 1)); y = round(p / 100 * (im.height - 1))
        col = (230, 0, 0) if p % 10 == 0 else (255, 150, 150)
        d.line([(x, 0), (x, im.height)], fill=col, width=1)
        d.line([(0, y), (im.width, y)], fill=col, width=1)
        if p % 10 == 0:
            for yy in (2, im.height // 2, im.height - 20):
                d.text((x + 2, yy), str(p), fill=(0, 0, 200), font=font)
            for xx in (2, im.width // 2, im.width - 30):
                d.text((xx, y + 1), str(p), fill=(0, 0, 200), font=font)
    os.makedirs(os.path.join(OUT, '_grid'), exist_ok=True)
    name = re.sub(r'[^a-z0-9]+', '-', os.path.splitext(os.path.basename(src))[0].lower()).strip('-') + (f'-p{page}' if page else '')
    dst = os.path.join(OUT, '_grid', name + '.png')
    im.save(dst)
    print(os.path.relpath(dst, ROOT))


def used_ids():
    """{id: [where, …]} for every picture referenced in content/ (Markdown img:ID and JSON "img")."""
    use = {}
    for path in glob.glob(os.path.join(ROOT, 'content', '**', '*.md'), recursive=True):
        if os.sep + 'specs' + os.sep in path:          # briefs quote example ids
            continue
        for ln, line in enumerate(open(path, encoding='utf-8'), 1):
            for m in USE_MD.finditer(line):
                use.setdefault(m.group(1), []).append(f'{os.path.relpath(path, ROOT)}:{ln}')
    for path in glob.glob(os.path.join(ROOT, 'content', 'mockweb', '*.json')):
        def walk(o, where):
            if isinstance(o, dict):
                v = o.get('img')
                for iid in ([v] if isinstance(v, str) else v or []):
                    use.setdefault(iid, []).append(where)
                for x in o.values():
                    walk(x, where)
            elif isinstance(o, list):
                for x in o:
                    walk(x, where)
        walk(json.load(open(path, encoding='utf-8')), os.path.relpath(path, ROOT))
    return use


def check(rows):
    use = used_ids()
    missing = {k: v for k, v in use.items() if k not in rows}
    for k, v in sorted(missing.items()):
        print(f'missing in content/img/*.tsv: {k}  (used at {v[0]}{" …" if len(v) > 1 else ""})')
    unbuilt = [k for k in use if k in rows and not os.path.exists(os.path.join(OUT, k + '.jpg'))]
    for k in unbuilt:
        print(f'not built: {k}')
    print(f'{len(rows)} pictures in manifests · {len(use)} used in content · {len(missing)} missing')
    return 1 if missing or unbuilt else 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--grid']:
        grid(a[1], a[2] if len(a) > 2 else None); sys.exit(0)
    if a[:1] == ['--check']:
        sys.exit(check(load_manifest()))
    if a[:1] in (['--only'], ['--sheet']):
        rows = load_manifest(strict=False)
        ids = a[1:]
        if len(ids) == 1 and ids[0].endswith('.tsv'):            # every id of one manifest
            ids = [l.split('\t')[0] for l in open(ids[0], encoding='utf-8') if l.strip() and not l.startswith('#')]
        unknown = [x for x in ids if x not in rows]
        if unknown:
            sys.exit('unknown id: ' + ' '.join(unknown))
        if a[0] == '--only':
            build(rows, only=set(ids))
        else:
            build({k: rows[k] for k in ids})
            sheet(ids, '_sheet_' + re.sub(r'[^a-z0-9]+', '-', os.path.basename(a[1]).lower())[:40])
        sys.exit(0)
    rows = load_manifest()
    n = build(rows)
    print(f'built {n} crop(s)')
    sys.exit(check(rows))
