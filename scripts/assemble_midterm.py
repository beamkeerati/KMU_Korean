#!/usr/bin/env python3
"""Assemble content/predictions/midterm/midterm01.md from parts/ (01_analysis + 02..05 questions, then # 정답 + keys). Run before build.py predict."""
"""Assemble content/predictions/midterm/parts/*.md into midterm01.md (questions, then # 정답 + keys)."""
import pathlib, re
from kmu_paths import ROOT   # levels/<N>/
root = pathlib.Path(ROOT) / 'content' / 'predictions' / 'midterm'
parts = root / 'parts'
q = [parts / '01_analysis.md', parts / '02_writing.md', parts / '03_reading.md', parts / '04_listening.md', parts / '05_speaking.md']
k = [parts / '02_writing_key.md', parts / '03_reading_key.md', parts / '04_listening_key.md', parts / '05_speaking_key.md']
body = '\n\n'.join(p.read_text(encoding='utf-8').strip() for p in q)
keys = '\n\n'.join(p.read_text(encoding='utf-8').strip() for p in k)
md = body + '\n\n# 정답\n\n' + keys + '\n'
bad = [l for l in md.split('\n') if '~~' in l or re.search(r'\{[a-zA-Z]:', l) and 'kotag' not in l]
print('lines with ~~ or {c: tags:', len(bad))
for l in bad[:5]: print('  ', l[:100])
(root / 'midterm01.md').write_text(md, encoding='utf-8')
print('written', len(md), 'bytes;', md.count('\n### '), '### sections;', md.count('\n#### '), '#### sub-sections')
