#!/usr/bin/env python3
"""Speech audio player: content/speaking/<name>.md -> output/6_Speaking/KMU_Speaking_<Camel>_Audio.html

usage: python3 scripts/build_speech_audio.py myself [--voice M]

Reads the numbered lines (**N. 한국어**, *คำอ่าน*, 🇹🇭 ความหมาย, ### section) of the speech file, generates one neural clip
per line with edge-tts (word boundaries kept for karaoke), caches them in extracted/speech_clips/<sha1>.{mp3,json}, and
writes a single-file HTML player (clips embedded as base64). Publish the HTML as an artifact so it plays on the iPad.
"""
import asyncio, base64, hashlib, json, os, re, ssl, sys
sys.path.insert(0, os.path.expanduser('~/.local/lib/python3.12/site-packages'))

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)
CACHE = os.path.join(ROOT, 'extracted', 'speech_clips')
VOICES = {'F': 'ko-KR-SunHiNeural', 'M': 'ko-KR-InJoonNeural', 'S': 'ko-KR-HyunsuMultilingualNeural'}

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kotag   # colour by word function — the same classes as every PDF (SPEC_colors.md)
_TAG = re.compile(r'\{([A-Za-z]):([^}]*)\}')

def _segments(tagged):
    """'{n:저}{p:는} 한국' -> [('n','저'),('p','는'),('',' 한국')]"""
    out, pos = [], 0
    for m in _TAG.finditer(tagged):
        if m.start() > pos: out.append(('', tagged[pos:m.start()]))
        out.append((m.group(1).lower(), m.group(2))); pos = m.end()
    if pos < len(tagged): out.append(('', tagged[pos:]))
    return out

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def ko_html(ko, words):
    """Korean line as nested spans: .w per spoken word (karaoke, from the edge-tts boundaries) and .k<cls> per word-function segment."""
    tagged = ko if '{' in ko else kotag.tag_korean(ko)
    segs = _segments(tagged); cls = []
    for c, t in segs: cls += [c] * len(t)
    plain = ''.join(t for _, t in segs)
    widx, pos = [-1] * len(plain), 0
    for j, w in enumerate(words):
        i = plain.find(w[2], pos)
        if i < 0: continue
        for k in range(i, i + len(w[2])): widx[k] = j
        pos = i + len(w[2])
    out, i = '', 0
    while i < len(plain):
        j = i
        while j < len(plain) and widx[j] == widx[i]: j += 1
        inner, a = '', i
        while a < j:
            b = a
            while b < j and cls[b] == cls[a]: b += 1
            inner += f'<span class="k{cls[a]}">{esc(plain[a:b])}</span>' if cls[a] else esc(plain[a:b]); a = b
        out += f'<span class="w">{inner}</span>' if widx[i] >= 0 else inner; i = j
    return out

def th_html(th, ko):
    tagged = th if '{' in th else kotag.tag_thai(th, ko=ko)
    return ''.join(f'<span class="k{c}">{esc(t)}</span>' if c else esc(t) for c, t in _segments(tagged))

def parse(path):
    lines, sec, title = [], '', ''
    for ln in open(path, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('# ') and not title: title = ln[2:].strip()
        if ln.startswith('## ') and lines: break
        m = re.match(r'^### (.+)$', ln)
        if m: sec = m.group(1); continue
        m = re.match(r'^\*\*(\d+)\. (.+)\*\*$', ln)
        if m: lines.append({'n': int(m.group(1)), 'ko': m.group(2), 'sec': sec, 'read': '', 'th': '', 'role': 'q'}); continue
        m = re.match(r'^\*\*→ (.+)\*\*$', ln)   # interview format: the model answer to the question above (spoken by the other voice)
        if m and lines: lines.append({'n': '', 'ko': m.group(1), 'sec': sec, 'read': '', 'th': '', 'role': 'a'}); continue
        if lines and ln.startswith('*') and not lines[-1]['read']: lines[-1]['read'] = ln.strip('*')
        if lines and ln.startswith('🇹🇭'): lines[-1]['th'] = ln[2:].strip()
    return title, lines

async def clip(text, voice):
    key = hashlib.sha1(f'{voice}|{text}'.encode()).hexdigest()
    mp3, js = os.path.join(CACHE, key + '.mp3'), os.path.join(CACHE, key + '.json')
    if not (os.path.exists(mp3) and os.path.exists(js)):
        import edge_tts, edge_tts.communicate as ec
        ec._SSL_CTX = ssl.create_default_context(cafile='/etc/ssl/certs/ca-certificates.crt')  # sandbox proxy re-signs TLS
        audio, words = b'', []
        async for ch in edge_tts.Communicate(text, voice, rate='+0%', boundary='WordBoundary').stream():
            if ch['type'] == 'audio': audio += ch['data']
            elif ch['type'] == 'WordBoundary':
                s = ch['offset'] / 1e7; words.append([round(s, 3), round(s + ch['duration'] / 1e7, 3), ch['text']])
        os.makedirs(CACHE, exist_ok=True)
        open(mp3, 'wb').write(audio); json.dump(words, open(js, 'w'))
        print(' generated', text[:30], file=sys.stderr)
    return base64.b64encode(open(mp3, 'rb').read()).decode(), json.load(open(js))

PAGE = r'''<title>@@title@@</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Sans+Thai:wght@400;500;700&display=swap">
<style>
/* layout: one column of numbered lines under a sticky transport bar; the Korean line is the stage, Thai sits under it */
:root { --bg:#f7f6f2; --fg:#1d2326; --mute:#6b7378; --line:#dedbd3; --card:#ffffff; --acc:#1f6f5f; --acc-ink:#ffffff; --now:#ffd166; --sung:#1f6f5f;
  --ko:'Noto Sans KR', 'Noto Sans CJK KR', sans-serif; --th:'Noto Sans Thai', 'Noto Sans', sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#15191b; --fg:#e8e6e0; --mute:#9aa3a8; --line:#2c3338; --card:#1d2326; --acc:#4fb39b; --acc-ink:#0f1a17; --now:#ffd166; --sung:#4fb39b; color-scheme: dark } }
:root[data-theme="dark"] { --bg:#15191b; --fg:#e8e6e0; --mute:#9aa3a8; --line:#2c3338; --card:#1d2326; --acc:#4fb39b; --acc-ink:#0f1a17; --now:#ffd166; --sung:#4fb39b; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font-family: var(--th); font-size: 16px; line-height: 1.6; }
body::before { content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); z-index:10; background:var(--bg); }
.wrap { max-width: 760px; margin: 0 auto; padding-block: 0 48px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
header { padding: 20px 0 8px; }
h1 { font-family: var(--ko); font-size: 26px; font-weight: 700; margin: 0; text-wrap: balance; }
header p { margin: 4px 0 0; color: var(--mute); font-size: 14px; }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); border-bottom: 1px solid var(--line); padding: 10px 0; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
button { font: inherit; font-size: 15px; border: 1px solid var(--line); background: var(--card); color: var(--fg); border-radius: 8px; padding: 8px 12px; cursor: pointer; min-height: 40px; }
button:focus-visible { outline: 2px solid var(--acc); outline-offset: 2px; }
button.pri { background: var(--acc); color: var(--acc-ink); border-color: var(--acc); font-weight: 500; }
button.on { border-color: var(--acc); color: var(--acc); font-weight: 500; }
.seg { display: inline-flex; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
.seg button { border: 0; border-radius: 0; min-width: 48px; }
.seg button + button { border-left: 1px solid var(--line); }
.seg button.on { background: var(--acc); color: var(--acc-ink); }
.opts { display: contents; }
.bar.fold .opts { display: none; }
#fold { margin-left: auto; }
.bar.fold #fold::after { content: " ▾"; } .bar:not(.fold) #fold::after { content: " ▴"; }
.sp { flex: 1 }
.sec { margin: 28px 0 8px; font-family: var(--ko); font-size: 13px; letter-spacing: .06em; text-transform: uppercase; color: var(--mute); }
.ln { display: grid; grid-template-columns: 40px 1fr 48px; gap: 6px 10px; align-items: start; padding: 12px 0; border-bottom: 1px solid var(--line); }
.ln .n { font-variant-numeric: tabular-nums; color: var(--mute); font-size: 14px; padding-top: 6px; }
.ln .ko { font-family: var(--ko); font-size: calc(22px * var(--ts, 1)); line-height: 1.55; font-weight: 500; grid-column: 2; min-width: 0; cursor: pointer; }
.ln .read, .ln .th { grid-column: 2; font-size: calc(14px * var(--ts, 1)); color: var(--mute); margin: 0; }
.ln .th { color: var(--fg); }
.ln .play { grid-column: 3; grid-row: 1 / span 3; justify-self: end; width: 44px; height: 44px; padding: 0; border-radius: 50%; font-size: 16px; }
.ln.playing { background: color-mix(in srgb, var(--acc) 8%, transparent); margin: 0 -8px; padding-left: 8px; padding-right: 8px; border-radius: 8px; }
.ln.playing .play { background: var(--acc); color: var(--acc-ink); border-color: var(--acc); }
.w.sung { color: var(--sung); }
.w.now { background: var(--now); color: #1d2326; border-radius: 4px; }
body[data-hide="th"] .read, body[data-hide="th"] .th { display: none; }
body[data-hide="ko"] .ko { filter: blur(7px); user-select: none; }
body[data-hide="ko"] .ko.show, body[data-hide="ko"] .ln.playing .ko { filter: none; }
.ln.a { padding-left: 14px; border-left: 3px solid var(--acc); border-bottom-style: dashed; }
.ln.a .n { color: var(--acc); }
body[data-hide="a"] .ln.a:not(.show):not(.playing) .ko, body[data-hide="a"] .ln.a:not(.show):not(.playing) .read, body[data-hide="a"] .ln.a:not(.show):not(.playing) .th { filter: blur(7px); user-select: none; }
.sec.opt { color: var(--acc); text-transform: none; letter-spacing: 0; font-size: 14px; }
.hint { font-size: 13px; color: var(--mute); margin: 10px 0 0; }
body[data-noread] .read { display: none; }
@media (max-width: 480px) { .ln .ko { font-size: calc(20px * var(--ts, 1)) } button { padding: 8px 10px } }
@media (prefers-reduced-motion: no-preference) { .ln { transition: background .2s } }
@@colors@@
.kp { background: color-mix(in srgb, #c2410c 14%, transparent); }
:root[data-theme="dark"] .kn { color: #93c5fd } :root[data-theme="dark"] .kp { color: #fdba74 } :root[data-theme="dark"] .kv { color: #86efac }
:root[data-theme="dark"] .ke { color: #d8b4fe } :root[data-theme="dark"] .kq { color: #5eead4 } :root[data-theme="dark"] .kx { color: #fca5a5 }
:root[data-theme="dark"] .km { color: #fcd34d } :root[data-theme="dark"] .ka { color: #d6d3d1 }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .kn { color: #93c5fd } :root:not([data-theme="light"]) .kp { color: #fdba74 }
  :root:not([data-theme="light"]) .kv { color: #86efac } :root:not([data-theme="light"]) .ke { color: #d8b4fe } :root:not([data-theme="light"]) .kq { color: #5eead4 }
  :root:not([data-theme="light"]) .kx { color: #fca5a5 } :root:not([data-theme="light"]) .km { color: #fcd34d } :root:not([data-theme="light"]) .ka { color: #d6d3d1 } }
.w.now span { color: #1d2326; }
.legend { font-size: 12px; color: var(--mute); margin: 6px 0 0; line-height: 1.8; } .legend span { margin-right: 8px; white-space: nowrap; }
</style>
<div class="wrap">
<header><h1>@@title@@</h1><p>@@sub@@</p>
<p class="legend">สี = หน้าที่ของคำ: <span class="kn">คำนาม</span><span class="kp">조사</span><span class="kv">กริยา/คุณศัพท์</span><span class="ke">ลงท้าย·กาล·이다</span><span class="kq">คำถาม</span><span class="kx">ปฏิเสธ</span><span class="km">ตัวเลข·ลักษณนาม</span><span class="ka">คำบอกเวลา·วิเศษณ์</span></p></header>
<div class="bar">
  <button id="all" class="pri">▶ เล่นทั้งบท</button>
  <button id="pause">⏸ หยุดชั่วคราว</button>
  <button id="stop">■ หยุด</button>
  <button id="fold" aria-expanded="true" aria-controls="opts" title="ซ่อน/แสดงตัวเลือก">⚙</button>
  <div class="opts" id="opts">
  <span class="seg" id="rate"><button data-r="0.7">0.7×</button><button data-r="0.85">0.85×</button><button data-r="1" class="on">1×</button></span>
  <button id="loop">↻ วนประโยค</button>
  <span class="seg" id="hide"><button data-h="" class="on">ครบ</button><button data-h="th">ซ่อนไทย</button><button data-h="ko">ซ่อนเกาหลี</button>@@hidea@@</span>
  <button id="read" class="on">คำอ่าน</button>
  <span class="seg" id="size" aria-label="ขนาดตัวอักษร"><button data-s="0.85">A−</button><button data-s="1" class="on">A</button><button data-s="1.25">A+</button><button data-s="1.5">A++</button></span>
  <span class="seg" id="theme" aria-label="ธีม"><button data-t="" class="on">อัตโนมัติ</button><button data-t="light">☀ สว่าง</button><button data-t="dark">☾ มืด</button></span>
  </div>
</div>
<div id="list"></div>
<p class="hint">แตะประโยคเพื่อเล่นเฉพาะประโยคนั้น · โหมด "ซ่อนเกาหลี" ให้ดูคำไทยแล้วพูดเอง แตะเพื่อเฉลย · เสียง: @@voice@@ (edge-tts)</p>
</div>
<script>
const D = @@data@@;
const $ = s => document.querySelector(s);
let cur = null, idx = -1, playAll = false, rate = 1, loop = false, userPaused = false;
function wrap(ko, words) {
  let out = '', pos = 0;
  for (const w of words) { const i = ko.indexOf(w[2], pos); if (i < 0) continue;
    out += esc(ko.slice(pos, i)) + '<span class="w">' + esc(ko.slice(i, i + w[2].length)) + '</span>'; pos = i + w[2].length; }
  return out + esc(ko.slice(pos));
}
function esc(s) { return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'})[c]); }
let html = '', sec = '';
D.forEach((L, i) => {
  if (L.sec !== sec) { sec = L.sec; html += '<div class="sec' + (sec.startsWith('➕') ? ' opt' : '') + '">' + esc(sec) + '</div>'; }
  html += '<div class="ln' + (L.role === 'a' ? ' a' : '') + '" id="l' + i + '"><div class="n">' + (L.role === 'a' ? '↳' : L.n) + '</div><div class="ko">' + L.html + '</div>'
    + '<p class="read">' + esc(L.read) + '</p><p class="th">' + L.thh + '</p><button class="play" aria-label="เล่นประโยค ' + L.n + '">▶</button></div>';
});
$('#list').innerHTML = html;
function el(i) { return document.getElementById('l' + i); }
function clear(i) { const e = el(i); if (!e) return; e.classList.remove('playing'); e.querySelectorAll('.w').forEach(s => s.classList.remove('sung', 'now')); }
function stop() { if (cur) { const a = cur; cur = null; a.pause(); } if (idx >= 0) clear(idx); idx = -1; playAll = false; userPaused = false; $('#pause').textContent = '⏸ หยุดชั่วคราว'; }
function play(i) {
  if (cur) { const a = cur; cur = null; a.pause(); } if (idx >= 0) clear(idx);
  idx = i; const L = D[i], e = el(i); e.classList.add('playing'); userPaused = false; $('#pause').textContent = '⏸ หยุดชั่วคราว';
  const spans = [...e.querySelectorAll('.w')];
  const a = new Audio('data:audio/mpeg;base64,' + L.mp3); a.preservesPitch = true; a.playbackRate = rate; cur = a;
  const top = e.getBoundingClientRect().top, barH = $('.bar').offsetHeight + 12;
  if (top < barH || top > innerHeight - 120) e.scrollIntoView({ block: 'center', behavior: 'smooth' });
  function tick() { if (cur !== a) return; const t = a.currentTime; let k = -1;
    L.words.forEach((w, j) => { if (t >= w[0] - 0.05) k = j; });
    spans.forEach((s, j) => { s.classList.toggle('sung', j < k); s.classList.toggle('now', j === k); });
    if (!a.paused && !a.ended) requestAnimationFrame(tick); }
  a.onplay = () => requestAnimationFrame(tick);
  a.onended = () => { if (cur !== a) return; spans.forEach(s => { s.classList.add('sung'); s.classList.remove('now'); });
    if (loop) return play(i);
    if (playAll && i + 1 < D.length) { const gap = document.body.dataset.hide === 'a' && D[i + 1].role === 'a' ? 6000 : 450;   // hide-answer mode: 6 s to answer yourself
      return setTimeout(() => { if (cur === a) play(i + 1); }, gap); }
    cur = null; setTimeout(() => { if (idx === i && !cur) { clear(i); idx = -1; } }, 1200); playAll = false; };
  a.play().catch(() => {});
}
$('#list').addEventListener('click', ev => {
  const ln = ev.target.closest('.ln'); if (!ln) return; const i = +ln.id.slice(1);
  if (document.body.dataset.hide === 'ko' && !ev.target.closest('.play')) { ln.querySelector('.ko').classList.toggle('show'); return; }
  if (document.body.dataset.hide === 'a' && ln.classList.contains('a') && !ev.target.closest('.play') && !ln.classList.contains('show')) { ln.classList.add('show'); return; }
  playAll = false; play(i);
});
$('#all').onclick = () => { playAll = true; play(idx >= 0 && !cur ? idx : 0); };
$('#pause').onclick = () => { if (!cur) return; if (cur.paused) { userPaused = false; cur.play(); $('#pause').textContent = '⏸ หยุดชั่วคราว'; } else { userPaused = true; cur.pause(); $('#pause').textContent = '▶ เล่นต่อ'; } };
$('#stop').onclick = stop;
$('#loop').onclick = () => { loop = !loop; $('#loop').classList.toggle('on', loop); if (loop) playAll = false; };
$('#rate').onclick = ev => { const b = ev.target.closest('button'); if (!b) return; rate = +b.dataset.r; if (cur) cur.playbackRate = rate;
  $('#rate').querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b)); try { localStorage.setItem('rate', rate); } catch (e) {} };
$('#hide').onclick = ev => { const b = ev.target.closest('button'); if (!b) return; document.body.dataset.hide = b.dataset.h;
  $('#hide').querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b)); document.querySelectorAll('.ko.show, .ln.show').forEach(x => x.classList.remove('show')); };
function setTheme(t, save) { const r = document.documentElement; if (t) r.dataset.theme = t; else r.removeAttribute('data-theme');
  $('#theme').querySelectorAll('button').forEach(x => x.classList.toggle('on', x.dataset.t === t)); if (save) try { localStorage.setItem('theme', t); } catch (e) {} }
$('#theme').onclick = ev => { const b = ev.target.closest('button'); if (b) setTheme(b.dataset.t, true); };
function setRead(on, save) { if (on) document.body.removeAttribute('data-noread'); else document.body.dataset.noread = '1';
  $('#read').classList.toggle('on', on); if (save) try { localStorage.setItem('read', on ? '1' : '0'); } catch (e) {} }
$('#read').onclick = () => setRead(document.body.hasAttribute('data-noread'), true);
function setSize(v, save) { document.documentElement.style.setProperty('--ts', v);
  $('#size').querySelectorAll('button').forEach(x => x.classList.toggle('on', x.dataset.s === String(v))); if (save) try { localStorage.setItem('size', v); } catch (e) {} }
$('#size').onclick = ev => { const b = ev.target.closest('button'); if (b) setSize(b.dataset.s, true); };
try { if (localStorage.getItem('read') === '0') setRead(false, false); const z = localStorage.getItem('size'); if (z) setSize(z, false); } catch (e) {}
const setFold = (f, save) => { $('.bar').classList.toggle('fold', f); $('#fold').setAttribute('aria-expanded', f ? 'false' : 'true'); if (save) try { localStorage.setItem('fold', f ? '1' : '0'); } catch (e) {} };
$('#fold').onclick = () => setFold(!$('.bar').classList.contains('fold'), true);
try { const f = localStorage.getItem('fold'); setFold(f === null ? window.innerWidth < 640 : f === '1', false); } catch (e) { setFold(window.innerWidth < 640, false); }
try { const t = localStorage.getItem('theme'); if (t !== null) setTheme(t, false); } catch (e) {}
try { const r = localStorage.getItem('rate'); if (r) { const b = $('#rate button[data-r="' + r + '"]'); if (b) b.click(); } } catch (e) {}
document.addEventListener('keydown', ev => { if (ev.target.tagName === 'INPUT') return;
  if (ev.key === ' ') { ev.preventDefault(); if (cur) $('#pause').click(); else $('#all').click(); }
  if (ev.key === 'ArrowDown' && idx >= 0 && idx + 1 < D.length) { ev.preventDefault(); play(idx + 1); }
  if (ev.key === 'ArrowUp' && idx > 0) { ev.preventDefault(); play(idx - 1); } });
</script>
'''

def main():
    name = next((a for a in sys.argv[1:] if not a.startswith('--')), 'myself')
    voice = VOICES[sys.argv[sys.argv.index('--voice') + 1]] if '--voice' in sys.argv else VOICES['M']
    src = os.path.join(ROOT, 'content', 'speaking', name + '.md')
    title, lines = parse(src)
    if not lines: sys.exit('no numbered lines found in ' + src)
    async def run():
        qa = any(L['role'] == 'a' for L in lines)
        for L in lines: L['mp3'], L['words'] = await clip(L['ko'], VOICES['F'] if qa and L['role'] == 'q' else voice)
        for L in lines:
            L['html'] = ko_html(L['ko'], L['words']); L['thh'] = th_html(L['th'], L['ko']) if L['th'] else ''
            L['ko'] = kotag.strip_tags(L['ko']); L['th'] = kotag.strip_tags(L['th'])
    asyncio.run(run())
    m = re.search(r'^\*\*ผู้พูด:\*\*\s*(.+?)\s*·', open(src, encoding='utf-8').read(), re.M)
    speaker = m.group(1) if m else ''
    page_title = re.sub(r'^.*?·\s*', '', title).split('(')[0].strip() or title   # "자기 소개"
    vals = {'title': page_title + (' · ' + speaker.split(' ')[0] if speaker else ''),
            'sub': f'{len(lines)} ประโยค · {title.split("(")[-1].rstrip(")") if "(" in title else ""} · ซ้อมพูดตามเสียง',
            'voice': voice.replace('ko-KR-', '').replace('Neural', ''), 'data': json.dumps(lines, ensure_ascii=False),
            'hidea': '<button data-h="a">ซ่อนคำตอบ</button>' if any(L['role'] == 'a' for L in lines) else '',
            'colors': kotag.CSS_COLORS}
    out = PAGE
    for k, v in vals.items(): out = out.replace('@@' + k + '@@', v)
    camel = ''.join(p.capitalize() for p in name.split('_'))
    dst = os.path.join(ROOT, 'output', '6_Speaking', f'KMU_Speaking_{camel}_Audio.html')
    open(dst, 'w', encoding='utf-8').write(out)
    print(f'{dst}  {os.path.getsize(dst) // 1024} KB, {len(lines)} lines, voice {voice}')

if __name__ == '__main__': main()
