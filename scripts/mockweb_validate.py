#!/usr/bin/env python3
"""Validate a practice-site data file (content/mockweb/*.json) against content/specs/SPEC_mockweb.md.

usage: python3 scripts/mockweb_validate.py content/mockweb/<file>.json [more.json ...]
Prints OK per file, or the list of problems (exit 1).
"""
import json, re, sys

EXAMS = {'mini02', 'review', 'midterm'}
SKILLS = {'writing', 'reading', 'listening', 'speaking'}
TYPES = {'mc', 'ox', 'blank', 'write', 'speak'}
TAG = re.compile(r'\{[a-zA-Z]:')
HANGUL = re.compile(r'[가-힣]')
DIGIT_IN_SCRIPT = re.compile(r'\d')


def check_text(where, s, errs):
    if not isinstance(s, str):
        errs.append(f'{where}: expected a string'); return
    if TAG.search(s): errs.append(f'{where}: colour tag left in text: {s[:60]}')
    if '**' in s or '<' in s and '>' in s: errs.append(f'{where}: markdown/HTML left in text: {s[:60]}')


def validate(path):
    errs, ids = [], set()
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        return [f'not valid JSON: {e}']
    sets = data.get('sets') if isinstance(data, dict) else None
    if not isinstance(sets, list) or not sets:
        return ['top level must be {"sets": [...]} with at least one set']
    for si, st in enumerate(sets):
        w = f'set[{si}]'
        for k in ('id', 'exam', 'skill', 'title', 'sections'):
            if k not in st: errs.append(f'{w}: missing {k}')
        if st.get('id') in ids: errs.append(f'{w}: duplicate id {st.get("id")}')
        ids.add(st.get('id'))
        if st.get('exam') not in EXAMS: errs.append(f'{w}: exam must be one of {sorted(EXAMS)}')
        if st.get('skill') not in SKILLS: errs.append(f'{w}: skill must be one of {sorted(SKILLS)}')
        w = f'{st.get("id", w)}'
        for ci, sec in enumerate(st.get('sections', [])):
            sw = f'{w} §{ci + 1}'
            if 'h' not in sec or 'items' not in sec or not sec['items']:
                errs.append(f'{sw}: needs h and a non-empty items list')
            for k in ('h', 'th', 'box'):
                if k in sec: check_text(f'{sw}.{k}', sec[k], errs)
            for li, ln in enumerate(sec.get('passage', [])):
                if not ln.get('ko') or 'th' not in ln: errs.append(f'{sw} passage[{li}]: needs ko and th')
                check_text(f'{sw} passage[{li}]', ln.get('ko', ''), errs)
            for li, ln in enumerate(sec.get('script', [])):
                if ln.get('s') not in ('F', 'M'): errs.append(f'{sw} script[{li}]: s must be F or M')
                if not ln.get('ko') or 'th' not in ln: errs.append(f'{sw} script[{li}]: needs ko and th')
                if DIGIT_IN_SCRIPT.search(ln.get('ko', '')): errs.append(f'{sw} script[{li}]: write numbers in Hangul: {ln["ko"][:50]}')
                check_text(f'{sw} script[{li}]', ln.get('ko', ''), errs)
            if st.get('skill') == 'listening' and not sec.get('script'):
                errs.append(f'{sw}: a listening section needs a script')
            for ii, it in enumerate(sec.get('items', [])):
                iw = f'{sw} item {it.get("n", ii)}'
                t = it.get('type')
                if t not in TYPES: errs.append(f'{iw}: type must be one of {sorted(TYPES)}'); continue
                if 'n' not in it: errs.append(f'{iw}: missing n')
                if 'th' not in it: errs.append(f'{iw}: missing th (Thai translation)')
                if not it.get('q'): errs.append(f'{iw}: missing q')
                for k in ('q', 'th', 'why', 'hint', 'pic', 'mth'):
                    if k in it: check_text(f'{iw}.{k}', it[k], errs)
                if 'pts' in it and not isinstance(it['pts'], (int, float)): errs.append(f'{iw}: pts must be a number')
                if t == 'mc':
                    o = it.get('opts')
                    if not isinstance(o, list) or not 2 <= len(o) <= 5 or not all(isinstance(x, list) and len(x) == 2 for x in o):
                        errs.append(f'{iw}: opts must be 2–5 [ko, th] pairs')
                    elif not isinstance(it.get('ans'), int) or not 0 <= it['ans'] < len(o):
                        errs.append(f'{iw}: ans must be a 0-based index into opts')
                elif t == 'ox':
                    if it.get('ans') not in ('O', 'X'): errs.append(f'{iw}: ans must be "O" or "X"')
                elif t == 'blank':
                    nb = it.get('q', '').count('___')
                    a = it.get('ans')
                    if nb == 0: errs.append(f'{iw}: q has no ___ blank')
                    if not isinstance(a, list) or len(a) != nb or not all(isinstance(x, list) and x and all(isinstance(y, str) and y for y in x) for x in a):
                        errs.append(f'{iw}: ans must be one non-empty list of strings per ___ ({nb} blanks)')
                elif t == 'write':
                    m = it.get('model')
                    if not isinstance(m, list) or not m or not all(isinstance(x, str) and HANGUL.search(x) for x in m):
                        errs.append(f'{iw}: model must be a non-empty list of Korean answers')
                elif t == 'speak':
                    if not it.get('model') or 'mth' not in it: errs.append(f'{iw}: speak needs model and mth')
                    for c in it.get('checks', []):
                        if not (isinstance(c, list) and len(c) == 2): errs.append(f'{iw}: checks entries are [regex, label]'); continue
                        if '(?<' in c[0]: errs.append(f'{iw}: no lookbehind in checks')
                        try: re.compile(c[0])
                        except re.error as e: errs.append(f'{iw}: bad regex {c[0]!r}: {e}')
    return errs


if __name__ == '__main__':
    bad = 0
    for p in sys.argv[1:]:
        e = validate(p)
        if e:
            bad = 1
            print(f'{p}: {len(e)} problem(s)')
            for x in e[:60]: print('  -', x)
        else:
            d = json.load(open(p, encoding='utf-8'))
            n = sum(len(s['items']) for st in d['sets'] for s in st['sections'])
            print(f'{p}: OK ({len(d["sets"])} sets, {n} items)')
    sys.exit(bad)
