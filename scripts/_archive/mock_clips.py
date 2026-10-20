"""Generate neural Korean clips for every line the mock page speaks; write clips.json {spk|text: dataURI}."""
import asyncio, base64, json, re, ssl, sys, pathlib
import edge_tts, edge_tts.communicate as ec
ec._SSL_CTX = ssl.create_default_context(cafile='/etc/ssl/certs/ca-certificates.crt')   # sandbox proxy CA
html = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
js = html[html.index('<script>'):]
items = []
for spk, ko in re.findall(r"\{ s: '([MF])',(?: who: '[^']+',)? ko: '([^']+)'", js): items.append((spk, ko))
for say in re.findall(r"say: '([^']+)'", js): items.append(('T', say))
for t in re.findall(r"sayLine\('([^']+)', 'T'\)", js): items.append(('T', t))
sp = js[js.index('const SPEAK'):js.index('/* ---', js.index('const SPEAK'))]
for q in re.findall(r"\{ q: '([^']+)'", sp): items.append(('T', q))
for m in re.findall(r"model: '([^']+)'", sp): items.append(('M', m.replace(' / ', '. ')))
VOICE = {'T': ('ko-KR-SunHiNeural', '-5%', '+0Hz'), 'F': ('ko-KR-SunHiNeural', '+0%', '+0Hz'),
         'M': ('ko-KR-InJoonNeural', '+0%', '+0Hz')}
STUDENT = ('ko-KR-HyunsuMultilingualNeural', '+0%', '+0Hz')
out = {}
async def one(key, spk, text, model):
    v, r, p = STUDENT if model else VOICE[spk]
    buf = b''
    async for ch in edge_tts.Communicate(text, v, rate=r, pitch=p).stream():
        if ch['type'] == 'audio': buf += ch['data']
    out[key] = 'data:audio/mpeg;base64,' + base64.b64encode(buf).decode()
async def main():
    models = set(m.replace(' / ', '. ') for m in re.findall(r"model: '([^']+)'", sp))
    seen = set()
    for spk, text in items:
        key = f'{spk}|{text}'
        if key in seen: continue
        seen.add(key)
        await one(key, spk, text, spk == 'M' and text in models)
asyncio.run(main())
pathlib.Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
print(len(out), 'clips', sum(len(v) for v in out.values()) // 1024, 'KB base64')
