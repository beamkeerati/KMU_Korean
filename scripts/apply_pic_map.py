#!/usr/bin/env python3
"""Merge picture mappings for the practice site into content/mockweb/*.json.

Writers (agents) never edit the shared JSON files; they list rows in content/img/map_<name>.tsv:
    <json file name>  <where>  <id[,id…]>
    daily_b.json	daily-24-writing §2 #3	ev24-t-b3
    daily_b.json	sheet-25-writing §1	ev24-s-panel          (no #n = the whole section shows the picture)
<where> is exactly what scripts/pic_inventory.py prints after the file name ("<set id> §<section> #<item n>").

    python3 scripts/apply_pic_map.py            apply every map, report rows that match nothing (exit 1 if any)
    python3 scripts/apply_pic_map.py --dry      report only
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'content', 'mockweb')
WHERE = re.compile(r'^(\S+)\s+§(\d+)(?:\s+#(.+))?$')


def main(dry):
    rows, bad = [], 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'content', 'img', 'map_*.tsv'))):
        for ln, line in enumerate(open(path, encoding='utf-8'), 1):
            if not line.strip() or line.startswith('#'):
                continue
            f = [x.strip() for x in line.rstrip('\n').split('\t')]
            m = WHERE.match(f[1]) if len(f) >= 3 else None
            if not m or not f[2]:
                print(f'{os.path.basename(path)}:{ln}: need 3 tab-separated columns: json · "<set> §N #n" · ids'); bad += 1; continue
            ids = [x.strip() for x in f[2].split(',') if x.strip()]
            rows.append((f'{os.path.basename(path)}:{ln}', os.path.basename(f[0]), m.group(1), int(m.group(2)), m.group(3), ids))
    by_file = {}
    for r in rows:
        by_file.setdefault(r[1], []).append(r)
    done = 0
    for fname, rs in sorted(by_file.items()):
        path = os.path.join(DATA, fname)
        if not os.path.exists(path):
            for r in rs: print(f'{r[0]}: no such file content/mockweb/{fname}'); bad += 1
            continue
        raw = open(path, encoding='utf-8').read()
        m = re.search(r'\n( +)"', raw)
        indent = len(m.group(1)) if m else None
        data = json.loads(raw)
        sets = {st['id']: st for st in data['sets']}
        for where, _, sid, si, n, ids in rs:
            st = sets.get(sid)
            if not st or not 1 <= si <= len(st['sections']):
                print(f'{where}: {fname}: no set {sid} §{si}'); bad += 1; continue
            sec = st['sections'][si - 1]
            target = sec if n is None else next((it for it in sec['items'] if str(it.get('n')) == n), None)
            if target is None:
                print(f'{where}: {fname}: {sid} §{si} has no item #{n}'); bad += 1; continue
            target['img'] = ids[0] if len(ids) == 1 else ids
            done += 1
        if not dry:
            out = json.dumps(data, ensure_ascii=False, indent=indent)
            open(path, 'w', encoding='utf-8').write(out + ('\n' if raw.endswith('\n') else ''))
    print(f'{done} picture mapping(s) {"would be " if dry else ""}applied · {bad} problem(s)')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main('--dry' in sys.argv))
