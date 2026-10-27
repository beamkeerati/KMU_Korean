#!/usr/bin/env python3
"""Check a guide Markdown file against content/specs/SPEC_book_style.md (2026-10-27).

usage: python3 scripts/book_style_check.py content/guide/01_units/unit23.md [more files…]

Prints one line per problem; the last line per file is a summary with the Korean-token count now vs. the
last committed version (git HEAD) so that a reflow that silently dropped examples is caught (> 5 % loss = ⚠️).
Exit status 1 when any file has a hard problem (bold pseudo-heading, missing INTRO/SUMMARY, ~~, token loss).
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANGUL = re.compile(r'[가-힣]+')


def head_version(path):
    rel = os.path.relpath(path, ROOT)
    try:
        return subprocess.run(['git', '-C', ROOT, 'show', f'HEAD:{rel}'], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None


def check(path):
    text = open(path, encoding='utf-8').read()
    lines = text.split('\n')
    rel = os.path.relpath(path, ROOT)
    needs_boxes = ('/01_units/' in path or '/02_grammar/' in path) and not os.path.basename(path).startswith('00_')
    hard, soft = [], []

    for i, line in enumerate(lines, 1):
        s = line.strip()
        if re.match(r'^\*\*[^*]+\*\*\s*$', s):
            hard.append(f'{rel}:{i}: bold line used as a heading → make it ### or ####')
        if '~~' in line:
            hard.append(f'{rel}:{i}: ~~ is not rendered (use ✗)')
        if not s.startswith('|') and not s.startswith('#') and s.count('·') > 3 and len(s) > 140:   # short word lists are fine
            soft.append(f'{rel}:{i}: {s.count("·")} × "·" in one line outside a table — split into a list/table')
        if s.startswith('###'):
            # the next non-empty line must be prose, not a table/list
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            nxt = lines[j].strip() if j < len(lines) else ''
            if nxt.startswith(('|', '- ', '* ', '1. ', '> [!')) and not s.startswith('####') and '🔗' not in s:
                soft.append(f'{rel}:{i}: ### heading followed directly by a table/list — add a lead sentence')
        if re.search(r'^\s*(\d+\.|[-*])\s.*\|.*\|', line):
            soft.append(f'{rel}:{i}: table row inside a list item')
    if needs_boxes:
        if text.count('[!INTRO]') != 1:
            hard.append(f'{rel}: expected exactly one > [!INTRO] box (found {text.count("[!INTRO]")})')
        if text.count('[!SUMMARY]') != 1:
            hard.append(f'{rel}: expected exactly one > [!SUMMARY] box (found {text.count("[!SUMMARY]")})')
        if not re.match(r'^## ', text.lstrip()):
            hard.append(f'{rel}: must start with the ## chapter heading')

    now = len(HANGUL.findall(text))
    before_text = head_version(path)
    before = len(HANGUL.findall(before_text)) if before_text else None
    loss = ''
    if before:
        ratio = now / before
        loss = f'Korean tokens {before} → {now} ({ratio:.0%})'
        if ratio < 0.95:
            hard.append(f'{rel}: {loss} — more than 5 % of the Korean content is gone')
    else:
        loss = f'Korean tokens {now} (no committed version to compare)'
    for m in hard:
        print('✗', m)
    for m in soft:
        print('·', m)
    print(f'= {rel}: {len(hard)} hard · {len(soft)} soft · {loss}')
    return not hard


if __name__ == '__main__':
    ok = True
    for p in sys.argv[1:]:
        ok = check(os.path.abspath(p)) and ok
    sys.exit(0 if ok else 1)
