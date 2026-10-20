#!/usr/bin/env python3
"""Build the practice website: content/mockweb/*.json + scripts/mockweb/app.html -> output/2_Practice_Web/

    python3 scripts/build_mockweb.py            # validate data, make missing voice clips, write the site
    python3 scripts/build_mockweb.py --no-audio # skip clip generation (browser voice is used for missing lines)

Output: index.html (standalone page), data.js (window.KMU_SETS), clips.js (window.KMU_CLIPS = {"F|text": dataURI}),
start.sh (serves the folder on localhost so Chrome allows the microphone).
Voices (free edge-tts, Microsoft neural): T teacher + F female = SunHi, M male = InJoon, S the student's model answers = Hyunsu.
Clips are cached in extracted/mockweb_clips/<sha1>.mp3, so only new or changed lines are generated.
"""
import asyncio, base64, glob, hashlib, json, os, re, shutil, ssl, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from mockweb_validate import validate  # noqa: E402

DATA = os.path.join(ROOT, 'content', 'mockweb')
APP = os.path.join(ROOT, 'scripts', 'mockweb', 'app.html')
OUT = os.path.join(ROOT, 'output', '2_Practice_Web')
CACHE = os.path.join(ROOT, 'extracted', 'mockweb_clips')
VOICES = {'T': ('ko-KR-SunHiNeural', '-5%'), 'F': ('ko-KR-SunHiNeural', '+0%'),
          'M': ('ko-KR-InJoonNeural', '+0%'), 'S': ('ko-KR-HyunsuMultilingualNeural', '+0%')}
FIXED_T = ['지금부터 듣기 시험을 시작하겠습니다.', '듣기 시험이 끝났습니다. 수고하셨습니다.',
           '안녕하세요. 지금부터 말하기 시험을 시작하겠습니다.', '수고하셨습니다.']
DIG = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']


def sino(n):
    """1..99 in Sino-Korean (item numbers are read 일 번, 십이 번)."""
    t, o = divmod(n, 10)
    return ((DIG[t] if t > 1 else '') + ('십' if t else '') + DIG[o]) or '영'


def item_no(n):
    m = re.match(r'\D*(\d+)', str(n))
    return int(m.group(1)) if m else None


def announce(sec):
    nums = [x for x in (item_no(it['n']) for it in sec['items']) if x]
    if not nums:
        return None
    a, b = nums[0], nums[-1]
    return f'{sino(a)} 번.' if a == b else f'{sino(a)} 번부터 {sino(b)} 번까지.'


def load_sets():
    sets, bad = [], False
    for f in sorted(glob.glob(os.path.join(DATA, '*.json'))):
        errs = validate(f)
        if errs:
            bad = True
            print(f'{os.path.basename(f)}: {len(errs)} problem(s)'); [print('  -', e) for e in errs[:20]]
            continue
        sets += json.load(open(f, encoding='utf-8'))['sets']
    if bad:
        sys.exit('fix the data files first')
    for st in sets:
        if st['skill'] == 'listening':
            for sec in st['sections']:
                sec['say'] = announce(sec)
    return sets


def spoken(sets):
    lines = [('T', t) for t in FIXED_T]
    for st in sets:
        for sec in st['sections']:
            if sec.get('say'):
                lines.append(('T', sec['say']))
            lines += [(ln['s'], ln['ko']) for ln in sec.get('script', [])]
            for it in sec['items']:
                if it['type'] == 'speak':
                    lines += [('T', it['q']), ('S', it['model'])]
    return list(dict.fromkeys(lines))


def clip_path(voice, text):
    v, r = VOICES[voice]
    return os.path.join(CACHE, hashlib.sha1(f'{v}|{r}|{text}'.encode()).hexdigest() + '.mp3')


async def make_clips(lines):
    import edge_tts
    import edge_tts.communicate as ec
    ec._SSL_CTX = ssl.create_default_context(cafile='/etc/ssl/certs/ca-certificates.crt')  # sandbox proxy re-signs TLS
    todo = [(v, t) for v, t in lines if not (os.path.exists(clip_path(v, t)) and os.path.exists(clip_path(v, t) + '.json'))]
    sem = asyncio.Semaphore(6)

    async def one(v, t):
        async with sem:
            voice, r = VOICES[v]
            for attempt in range(3):
                try:
                    buf = b''; words = []
                    async for ch in edge_tts.Communicate(t, voice, rate=r, boundary='WordBoundary').stream():
                        if ch['type'] == 'audio':
                            buf += ch['data']
                        elif ch['type'] == 'WordBoundary':   # offsets in 100-ns ticks → seconds; drives the karaoke highlight
                            words.append([round(ch['offset'] / 1e7, 3), round((ch['offset'] + ch['duration']) / 1e7, 3), ch['text']])
                    if buf:
                        open(clip_path(v, t), 'wb').write(buf)
                        json.dump(words, open(clip_path(v, t) + '.json', 'w', encoding='utf-8'), ensure_ascii=False)
                        return
                except Exception as e:  # network hiccup: retry
                    err = e
                await asyncio.sleep(1 + attempt)
            print(f'  ! no clip for {v}|{t[:30]}: {err if "err" in dir() else "empty"}')
    await asyncio.gather(*(one(v, t) for v, t in todo))
    return len(todo)


def standalone(fragment):
    head = ('<!doctype html>\n<html lang="th">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
    e = fragment.index('</style>') + len('</style>')
    return head + fragment[:e] + '\n</head>\n<body>\n' + fragment[e:] + '\n</body>\n</html>\n'


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)
    sets = load_sets()
    lines = spoken(sets)
    if '--no-audio' not in sys.argv:
        made = asyncio.run(make_clips(lines))
        print(f'clips     : {len(lines)} spoken lines, {made} newly generated')
    clips = {f'{v}|{t}': 'data:audio/mpeg;base64,' + base64.b64encode(open(clip_path(v, t), 'rb').read()).decode()
             for v, t in lines if os.path.exists(clip_path(v, t))}
    with open(os.path.join(OUT, 'data.js'), 'w', encoding='utf-8') as f:
        f.write('window.KMU_SETS = ' + json.dumps(sets, ensure_ascii=False) + ';\n')
    words = {f'{v}|{t}': json.load(open(clip_path(v, t) + '.json', encoding='utf-8'))
             for v, t in lines if os.path.exists(clip_path(v, t) + '.json')}
    with open(os.path.join(OUT, 'clips.js'), 'w', encoding='utf-8') as f:
        f.write('window.KMU_CLIPS = ' + json.dumps(clips, ensure_ascii=False) + ';\n')
        f.write('window.KMU_WORDS = ' + json.dumps(words, ensure_ascii=False) + ';\n')
    shutil.copyfile(os.path.join(os.path.dirname(APP), 'vendor.js'), os.path.join(OUT, 'vendor.js'))   # Preact + Signals + htm (UMD)
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(standalone(open(APP, encoding='utf-8').read()))
    sh = os.path.join(OUT, 'start.sh')
    with open(sh, 'w') as f:
        f.write('#!/bin/sh\n# Serve the practice site on localhost (Chrome allows the microphone there) and open it.\n'
                'cd "$(dirname "$0")"\n( sleep 1; xdg-open http://localhost:8000/index.html >/dev/null 2>&1 ) &\n'
                'python3 -m http.server 8000 --bind 127.0.0.1\n')
    os.chmod(sh, 0o755)
    n = sum(len(s['items']) for st in sets for s in st['sections'])
    size = sum(os.path.getsize(os.path.join(OUT, x)) for x in ('data.js', 'clips.js', 'vendor.js', 'index.html')) // 1024
    print(f'mockweb   : {len(sets)} sets · {n} items · {len(clips)}/{len(lines)} clips · {size} KB -> output/2_Practice_Web/')


if __name__ == '__main__':
    main()
