#!/usr/bin/env python3
"""Check content/guide/04_vocabulary/examples/unitNN.json (example sentences for the practice site's vocabulary drill).

usage: python3 scripts/vocab_examples_check.py 35 36 …      (unit numbers, or file paths, or nothing = every file)

Each file = {"unit": NN, "words": [{ko, th, en, [cat], note, ex: [{ko, th, b}]}]} and must list exactly the words that
build_mockweb.load_vocab() gives that unit, in the same order (ko/th/en/cat are copied from 04_vocabulary/unitNN.md for
reference only; the meanings are edited there, not here). Errors (exit 1): wrong word list, empty example, b not found
exactly once in the sentence, no Thai translation, sentence without final . ? !, note longer than 90 characters.
Warnings: the blank does not start like the word (fine for irregular stems such as 듣다 → 들어).
"""
import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXDIR = os.path.join(ROOT, 'content', 'guide', '04_vocabulary', 'examples')
HANGUL = re.compile(r'[가-힣]')
THAI = re.compile(r'[฀-๿]')


def vocab_by_unit():
    spec = importlib.util.spec_from_file_location('bm', os.path.join(ROOT, 'scripts', 'build_mockweb.py'))
    bm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bm)
    out = {}
    for w in bm.load_vocab():
        out.setdefault(w['u'], []).append(w['ko'])
    return out


def base(ko):
    """the spelling a blank should start with: '정류장 [정뉴장]' → 정류장 · '(돈을) 쓰다' → 쓰다 · '상(을) 받다' → 상"""
    s = re.sub(r'\s*\[[^\]]*\]', '', ko)
    s = re.sub(r'^\([^)]*\)\s*', '', s)
    return s.strip()


def check(path, want):
    errs, warns = [], []
    try:
        d = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        return [f'not valid JSON: {e}'], [], 0
    words = d.get('words', [])
    got = [w.get('ko') for w in words]
    if got != want:
        miss = [k for k in want if k not in got]; extra = [k for k in got if k not in want]
        errs.append(f'word list differs from 04_vocabulary (missing {miss[:5]}, extra {extra[:5]}, or the order changed)')
    filled = 0
    for i, w in enumerate(words):
        tag = f'#{i + 1} {w.get("ko")}'
        note = w.get('note', '')
        if not isinstance(note, str): errs.append(f'{tag}: note must be a string')
        elif len(note) > 90: errs.append(f'{tag}: note is {len(note)} characters (max 90)')
        ex = w.get('ex') or []
        if not ex or not any(e.get('ko') for e in ex):
            errs.append(f'{tag}: no example sentence'); continue
        if len(ex) > 2: errs.append(f'{tag}: at most 2 examples')
        filled += 1
        for j, e in enumerate(ex):
            ko, th, b = e.get('ko', ''), e.get('th', ''), e.get('b', '')
            t = f'{tag} ex{j + 1}'
            if not HANGUL.search(ko): errs.append(f'{t}: ko has no Korean'); continue
            if not re.search(r'[.?!]$', ko.strip()): errs.append(f'{t}: ko must end with . ? or !')
            if not THAI.search(th): errs.append(f'{t}: th (Thai translation of the whole sentence) missing')
            if HANGUL.search(th): warns.append(f'{t}: th contains Korean — translate it')
            if not b: errs.append(f'{t}: b (the blank) is empty'); continue
            n = ko.count(b)
            if n != 1: errs.append(f'{t}: b {b!r} occurs {n}× in the sentence (must be exactly once)')
            if b.strip() == ko.strip().rstrip('.?!'): errs.append(f'{t}: b is the whole sentence')
            k = base(w.get('ko', ''))
            if k and b[0] != k[0] and k.split()[0] not in b:
                warns.append(f'{t}: blank {b!r} does not start like {k!r} (ok only for an irregular stem)')
    return errs, warns, filled


def main():
    want = vocab_by_unit()
    args = sys.argv[1:]
    paths = []
    for a in args:
        paths.append(a if a.endswith('.json') else os.path.join(EXDIR, f'unit{int(a):02d}.json'))
    if not paths:
        paths = sorted(glob.glob(os.path.join(EXDIR, 'unit*.json')))
    bad = False
    for p in paths:
        u = int(re.search(r'unit(\d+)', os.path.basename(p)).group(1))
        errs, warns, filled = check(p, want.get(u, []))
        total = len(want.get(u, []))
        for e in errs[:40]: print(f'  ✗ unit{u:02d} {e}')
        if len(errs) > 40: print(f'  … {len(errs) - 40} more errors')
        for w in warns[:20]: print(f'  ⚠ unit{u:02d} {w}')
        print(f'unit{u:02d}: {"OK" if not errs else "FAIL"} · {filled}/{total} words have examples · {len(errs)} errors · {len(warns)} warnings')
        bad = bad or bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
