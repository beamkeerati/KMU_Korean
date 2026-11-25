#!/usr/bin/env python3
"""Scaffold levels/<N>/ for a new level by copying level 1's FOLDER tree (folders only, no files).

    python3 scripts/new_level.py 2            # create levels/2/{source,content,output,docs}/… (empty folders)
    python3 scripts/new_level.py 2 --switch   # …and make it the default level (levels/current = 2)

Copied: source/<type>/, content/<subtree>/, output/<purpose>/ and docs/ — the layout the scripts expect.
Not copied: extracted/ (caches, rebuilt on demand) and any file. Existing folders are left alone.
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(REPO, 'levels', '1')
COPY = ('source', 'content', 'output', 'docs')
SKIP = {'__pycache__', '_build', 'audio'}            # build caches · publisher mp3 copies


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1 or not args[0].isdigit():
        raise SystemExit(__doc__)
    n, dest = args[0], os.path.join(REPO, 'levels', args[0])
    made = 0
    for top in COPY:
        for d, subs, _ in os.walk(os.path.join(TEMPLATE, top)):
            subs[:] = [s for s in subs if s not in SKIP]
            rel = os.path.relpath(d, TEMPLATE)
            target = os.path.join(dest, rel)
            if not os.path.isdir(target):
                os.makedirs(target)
                made += 1
    print(f'levels/{n}: {made} new folders (template = levels/1)')
    if '--switch' in sys.argv:
        with open(os.path.join(REPO, 'levels', 'current'), 'w', encoding='utf-8') as f:
            f.write(n + '\n')
        print(f'levels/current = {n}')


if __name__ == '__main__':
    main()
