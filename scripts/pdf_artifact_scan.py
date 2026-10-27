#!/usr/bin/env python3
"""Scan built PDFs for Markdown/HTML that leaked into the page text (2026-10-27).

usage: python3 scripts/pdf_artifact_scan.py [output/1_Guides/KMU_Guide_By_Topic.pdf …]   (default: every PDF under output/)

Runs pdftotext on each PDF, splits the text into pages and prints file:page for every page that contains a
raw tag (<span …>, </span>, class=, &lt;), an unrendered Markdown mark (**, ~~, *(, `, > [!, ####, |---),
a colour-tag brace ({n:…}) or an escaped underscore. Exit status 1 when anything was found.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS = [
    ('raw tag', re.compile(r'</?span|class="|&lt;|&gt;|&amp;|<details>|<summary>|<br>')),
    ('markdown', re.compile(r'\*\*|~~|\*\(|(?<![A-Za-z0-9])`|> \[!|\[!(INTRO|SUMMARY|TIP|WARNING|NOTE)\]|^#{1,6} |\|:?-{2,}', re.M)),
    ('colour brace', re.compile(r'\{[a-zA-Z]:')),
    ('escaped', re.compile(r'\\_')),
]


def scan(pdf):
    text = subprocess.run(['pdftotext', pdf, '-'], capture_output=True, text=True).stdout
    hits = []
    for pno, page in enumerate(text.split('\f'), 1):
        for name, rx in PATTERNS:
            m = rx.search(page)
            if m:
                start = max(0, m.start() - 30)
                snippet = page[start:m.end() + 30].replace('\n', ' ')
                hits.append((pno, name, snippet.strip()))
    return hits


if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'output', '**', '*.pdf'), recursive=True))
    files = [f for f in files if 'Mindmap' not in f]
    total = 0
    for f in files:
        hits = scan(f)
        rel = os.path.relpath(f, ROOT)
        for pno, name, snippet in hits:
            print(f'{rel}:{pno}: {name}: {snippet}')
        print(f'= {rel}: {len(hits)} page(s) with leftovers')
        total += len(hits)
    sys.exit(1 if total else 0)
