#!/usr/bin/env python3
"""Where the content still describes a picture in words (🖼️) without showing the real one.

    python3 scripts/pic_inventory.py                 counts per file (md lines + practice-site items/sections)
    python3 scripts/pic_inventory.py --unit 24       every open 🖼️ that belongs to 24과 (file name unit24 / set id -24- / guide unit24)
    python3 scripts/pic_inventory.py --file PATH     every open 🖼️ in one file
    python3 scripts/pic_inventory.py --all           every open 🖼️ everywhere

"Open" = a Markdown line with 🖼 but no ](img:…) on it, or a JSON item/section with "pic" (or 🖼 in its text) but no "img".
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIC = '🖼'


def unit_of(path, setid=''):
    m = re.search(r'unit(\d\d)', os.path.basename(path)) or re.search(r'-(\d\d)(?:-|$)', setid) or re.search(r'predict(\d\d)', path)
    return int(m.group(1)) if m else None


def md_open():
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'content', '**', '*.md'), recursive=True)):
        rel = os.path.relpath(path, ROOT)
        if rel.startswith('content/specs/'):
            continue
        lines = open(path, encoding='utf-8').read().split('\n')
        for i, line in enumerate(lines):
            if PIC not in line or '](img:' in line:
                continue
            covered = False                      # a caption under a picture shown a few lines above (same block) counts as covered
            for back in lines[max(0, i - 14):i][::-1]:
                if back.startswith('#'):
                    break
                if '](img:' in back:
                    covered = True; break
            if not covered:
                out.append((rel, unit_of(rel), f'{i + 1}', line.strip()[:160]))
    return out


def json_open():
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'content', 'mockweb', '*.json'))):
        rel = os.path.relpath(path, ROOT)
        if rel.endswith('scores.json'):
            continue
        data = json.load(open(path, encoding='utf-8'))
        for st in data.get('sets', []):
            for si, sec in enumerate(st['sections']):
                stext = ' '.join(str(sec.get(k, '')) for k in ('h', 'th', 'box'))
                if PIC in stext and 'img' not in sec:
                    out.append((rel, unit_of(rel, st['id']), f'{st["id"]} §{si + 1}', stext.strip()[:160]))
                for it in sec.get('items', []):
                    text = ' '.join(str(it.get(k, '')) for k in ('pic', 'q', 'th'))
                    if (it.get('pic') or PIC in text) and 'img' not in it and 'img' not in sec:
                        out.append((rel, unit_of(rel, st['id']), f'{st["id"]} §{si + 1} #{it.get("n")}', (it.get('pic') or text).strip()[:160]))
    return out


if __name__ == '__main__':
    a = sys.argv[1:]
    rows = md_open() + json_open()
    if a[:1] == ['--unit']:
        u = int(a[1])
        rows = [r for r in rows if r[1] == u]
    elif a[:1] == ['--file']:
        rows = [r for r in rows if r[0] == os.path.relpath(os.path.abspath(a[1]), ROOT)]
    elif a[:1] != ['--all']:
        counts = {}
        for r in rows:
            counts[r[0]] = counts.get(r[0], 0) + 1
        for k, v in sorted(counts.items()):
            print(f'{v:5d}  {k}')
        print(f'{len(rows):5d}  open pictures in {len(counts)} files')
        sys.exit(0)
    for f, u, where, text in rows:
        print(f'{f}:{where}\t{text}')
    print(f'{len(rows)} open')
