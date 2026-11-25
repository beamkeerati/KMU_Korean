#!/usr/bin/env python3
"""
build_interview.py — content/speaking/<name>.md (category → question cards) → output/6_Speaking/KMU_Speaking_<Camel>_Cards.html
usage: python3 scripts/build_interview.py interview_cards [--voice M]

Markup:  `## emoji 한국어 · ไทย` = category · `### Thai intent (Korean key)` = card · `**Q. …**` question variant · `**→ …**` answer
         each Korean line is followed by `*Thai reading*` and `🇹🇭 meaning`; `💡 …` = one tip per card.
Clips (edge-tts, cached in extracted/speech_clips/) and the colour/karaoke HTML come from build_speech_audio.py.
"""
import asyncio, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_speech_audio as sa
import kotag

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)


def parse(path):
    title, sub, cats, cards = '', '', [], []
    for ln in open(path, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('# ') and not title: title = ln[2:].strip(); continue
        if not sub and title and ln.startswith('*') and not cards and not ln.startswith('**'): sub = ln.strip('*').strip(); continue
        m = re.match(r'^## (.+)$', ln)
        if m: cats.append(m.group(1).strip()); continue
        m = re.match(r'^### (.+?)(?:\s*\((.+)\))?\s*$', ln)
        if m and cats: cards.append({'cat': len(cats) - 1, 'ttl': m.group(1).strip(), 'key': (m.group(2) or '').strip(), 'lines': [], 'tip': ''}); continue
        if not cards: continue
        m = re.match(r'^\*\*(Q\.|→) (.+)\*\*$', ln)
        if m: cards[-1]['lines'].append({'role': 'q' if m.group(1) == 'Q.' else 'a', 'ko': m.group(2).strip(), 'read': '', 'th': ''}); continue
        L = cards[-1]['lines'][-1] if cards[-1]['lines'] else None
        if ln.startswith('💡'): cards[-1]['tip'] = ln[1:].strip(); continue
        if L and ln.startswith('🇹🇭'): L['th'] = ln[2:].strip(); continue
        if L and ln.startswith('*') and not ln.startswith('**') and not L['read']: L['read'] = ln.strip('*').strip()
    return title, sub, cats, cards


PAGE = r'''<title>@@title@@</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Sans+Thai:wght@400;500;700&display=swap">
<style>
/* question cards: category chips filter the list; a card = one meaning, its question variants on top, the answers under them */
:root { --bg:#f7f6f2; --fg:#1d2326; --mute:#6b7378; --line:#dedbd3; --card:#ffffff; --acc:#1f6f5f; --acc-ink:#ffffff; --now:#ffd166; --sung:#1f6f5f; --soft:#eef4f2;
  --ko:'Noto Sans KR', 'Noto Sans CJK KR', sans-serif; --th:'Noto Sans Thai', 'Noto Sans', sans-serif; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#15191b; --fg:#e8e6e0; --mute:#9aa3a8; --line:#2c3338; --card:#1d2326; --acc:#4fb39b; --acc-ink:#0f1a17; --soft:#1f2a27; color-scheme: dark } }
:root[data-theme="dark"] { --bg:#15191b; --fg:#e8e6e0; --mute:#9aa3a8; --line:#2c3338; --card:#1d2326; --acc:#4fb39b; --acc-ink:#0f1a17; --soft:#1f2a27; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font-family: var(--th); font-size: 16px; line-height: 1.6; margin: 0; }
body::before { content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); z-index:10; background:var(--bg); }
.wrap { max-width: 760px; margin: 0 auto; padding-block: 0 60px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
header { padding: 20px 0 6px; }
h1 { font-family: var(--ko); font-size: 24px; font-weight: 700; margin: 0; text-wrap: balance; }
header p { margin: 4px 0 0; color: var(--mute); font-size: 14px; }
.legend { font-size: 12px; color: var(--mute); margin: 4px 0 0; line-height: 1.8; } .legend span { margin-right: 8px; white-space: nowrap; }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); border-bottom: 1px solid var(--line); padding: 8px 0; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
button { font: inherit; font-size: 15px; border: 1px solid var(--line); background: var(--card); color: var(--fg); border-radius: 8px; padding: 8px 12px; cursor: pointer; min-height: 40px; }
button:focus-visible { outline: 2px solid var(--acc); outline-offset: 2px; }
button.pri { background: var(--acc); color: var(--acc-ink); border-color: var(--acc); font-weight: 500; }
button.on { border-color: var(--acc); color: var(--acc); font-weight: 500; }
.seg { display: inline-flex; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
.seg button { border: 0; border-radius: 0; min-width: 44px; } .seg button + button { border-left: 1px solid var(--line); }
.seg button.on { background: var(--acc); color: var(--acc-ink); }
.opts { display: contents; } .bar.fold .opts { display: none; } #fold { margin-left: auto; }
.bar.fold #fold::after { content: " ▾"; } .bar:not(.fold) #fold::after { content: " ▴"; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; padding: 10px 0 6px; }
@media (max-width: 600px) { .chips { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: thin; -webkit-overflow-scrolling: touch; padding-bottom: 8px; } }
.chip { flex: 0 0 auto; border-radius: 999px; padding: 6px 12px; min-height: 36px; font-size: 14px; white-space: nowrap; }
.chip .c { color: var(--mute); font-size: 12px; margin-left: 4px; } .chip.on .c { color: inherit; opacity: .8; }
.tools { display: flex; justify-content: space-between; align-items: center; color: var(--mute); font-size: 13px; padding: 2px 0 8px; }
.tools button { min-height: 32px; padding: 4px 10px; font-size: 13px; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; margin: 10px 0; overflow: hidden; }
.card.hide { display: none; }
.card > .hd { display: grid; grid-template-columns: 34px 1fr auto; gap: 4px 10px; align-items: center; padding: 10px 12px; cursor: pointer; user-select: none; }
.card > .hd:hover { background: var(--soft); }
.hd .no { grid-column: 1; grid-row: 1; color: var(--mute); font-size: 13px; font-variant-numeric: tabular-nums; }
.hd .tw { grid-column: 2; grid-row: 1; min-width: 0; }
.hd .ttl { font-weight: 600; font-size: 16px; } .hd .key { font-family: var(--ko); color: var(--mute); font-size: 14px; margin-left: 6px; font-weight: 400; }
.hd .pv { grid-column: 2; grid-row: 2; font-family: var(--ko); color: var(--mute); font-size: calc(15px * var(--ts, 1)); }
.card.open .hd .pv { display: none; }
.hd .right { display: flex; align-items: center; gap: 6px; grid-column: 3; grid-row: 1 / span 2; }
.hd .meta { color: var(--mute); font-size: 12px; white-space: nowrap; }
.hd .chev { color: var(--mute); transition: transform .2s; } .card.open .hd .chev { transform: rotate(180deg); }
.hd .pc { width: 40px; height: 40px; padding: 0; border-radius: 50%; }
.card.playing .hd .pc { background: var(--acc); color: var(--acc-ink); border-color: var(--acc); }
.bd { display: none; border-top: 1px solid var(--line); padding: 4px 12px 10px; } .card.open .bd { display: block; }
.lbl { font-size: 12px; letter-spacing: .05em; text-transform: uppercase; color: var(--mute); margin: 10px 0 2px; }
.grp.a .lbl { color: var(--acc); }
.ln { display: grid; grid-template-columns: 28px 1fr 44px; gap: 2px 8px; align-items: start; padding: 8px 0; border-bottom: 1px dashed var(--line); }
.ln:last-child { border-bottom: 0; }
.ln .n { color: var(--mute); font-size: 13px; padding-top: 5px; font-variant-numeric: tabular-nums; } .grp.a .ln .n { color: var(--acc); }
.ln .ko { font-family: var(--ko); font-size: calc(20px * var(--ts, 1)); line-height: 1.5; font-weight: 500; grid-column: 2; min-width: 0; cursor: pointer; }
.ln .read, .ln .th { grid-column: 2; font-size: calc(14px * var(--ts, 1)); color: var(--mute); margin: 0; } .ln .th { color: var(--fg); }
.ln .play { grid-column: 3; grid-row: 1 / span 3; justify-self: end; width: 40px; height: 40px; padding: 0; border-radius: 50%; font-size: 15px; }
.ln.playing { background: color-mix(in srgb, var(--acc) 8%, transparent); margin: 0 -8px; padding-left: 8px; padding-right: 8px; border-radius: 8px; }
.ln.playing .play { background: var(--acc); color: var(--acc-ink); border-color: var(--acc); }
.w.sung { color: var(--sung); } .w.now { background: var(--now); color: #1d2326; border-radius: 4px; } .w.now span { color: #1d2326; }
.tip { margin: 10px 0 0; font-size: 14px; color: var(--mute); background: var(--soft); border-radius: 8px; padding: 8px 10px; }
body[data-hide="th"] .read, body[data-hide="th"] .th { display: none; }
body[data-hide="ko"] .ko { filter: blur(7px); user-select: none; }
body[data-hide="ko"] .ko.show, body[data-hide="ko"] .ln.playing .ko { filter: none; }
body[data-hide="a"] .grp.a .ln:not(.show):not(.playing) .ko, body[data-hide="a"] .grp.a .ln:not(.show):not(.playing) .read, body[data-hide="a"] .grp.a .ln:not(.show):not(.playing) .th { filter: blur(7px); user-select: none; }
body[data-noread] .read { display: none; }
.hint { color: var(--mute); font-size: 13px; margin-top: 24px; }
@media (max-width: 480px) { .hd .meta { display: none; } .ln .ko { font-size: calc(19px * var(--ts, 1)) } button { padding: 8px 10px } }
@@colors@@
.kp { background: color-mix(in srgb, #c2410c 14%, transparent); }
:root[data-theme="dark"] .kn { color: #93c5fd } :root[data-theme="dark"] .kp { color: #fdba74 } :root[data-theme="dark"] .kv { color: #86efac }
:root[data-theme="dark"] .ke { color: #d8b4fe } :root[data-theme="dark"] .kq { color: #5eead4 } :root[data-theme="dark"] .kx { color: #fca5a5 }
:root[data-theme="dark"] .km { color: #fcd34d } :root[data-theme="dark"] .ka { color: #d6d3d1 }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .kn { color: #93c5fd } :root:not([data-theme="light"]) .kp { color: #fdba74 }
  :root:not([data-theme="light"]) .kv { color: #86efac } :root:not([data-theme="light"]) .ke { color: #d8b4fe } :root:not([data-theme="light"]) .kq { color: #5eead4 }
  :root:not([data-theme="light"]) .kx { color: #fca5a5 } :root:not([data-theme="light"]) .km { color: #fcd34d } :root:not([data-theme="light"]) .ka { color: #d6d3d1 } }
</style>
<div class="wrap">
<header><h1>@@title@@</h1><p>@@sub@@</p>
<p class="legend">สี = หน้าที่ของคำ: <span class="kn">คำนาม</span><span class="kp">조사</span><span class="kv">กริยา/คุณศัพท์</span><span class="ke">ลงท้าย·กาล·이다</span><span class="kq">คำถาม</span><span class="kx">ปฏิเสธ</span><span class="km">ตัวเลข·ลักษณนาม</span><span class="ka">คำบอกเวลา·วิเศษณ์</span></p></header>
<div class="bar">
  <button id="all" class="pri">▶ เล่นหมวดนี้</button>
  <button id="pause">⏸ หยุดชั่วคราว</button>
  <button id="stop">■ หยุด</button>
  <button id="fold" aria-expanded="true" aria-controls="opts" title="ซ่อน/แสดงตัวเลือก">⚙</button>
  <div class="opts" id="opts">
  <span class="seg" id="rate"><button data-r="0.7">0.7×</button><button data-r="0.85">0.85×</button><button data-r="1" class="on">1×</button></span>
  <button id="loop">↻ วนประโยค</button>
  <span class="seg" id="hide"><button data-h="" class="on">ครบ</button><button data-h="th">ซ่อนไทย</button><button data-h="ko">ซ่อนเกาหลี</button><button data-h="a">ซ่อนคำตอบ</button></span>
  <button id="read" class="on">คำอ่าน</button>
  <span class="seg" id="size" aria-label="ขนาดตัวอักษร"><button data-s="0.85">A−</button><button data-s="1" class="on">A</button><button data-s="1.25">A+</button><button data-s="1.5">A++</button></span>
  <span class="seg" id="theme" aria-label="ธีม"><button data-t="" class="on">อัตโนมัติ</button><button data-t="light">☀ สว่าง</button><button data-t="dark">☾ มืด</button></span>
  </div>
</div>
<div class="chips" id="chips"></div>
<div class="tools"><span id="count"></span><span><button id="openall">กางทั้งหมด</button> <button id="closeall">พับทั้งหมด</button></span></div>
<div id="list"></div>
<p class="hint">แตะหัวการ์ดเพื่อกาง · ▶ ที่การ์ด = ถาม 1 แบบแล้วตอบทุกแบบ · "ซ่อนคำตอบ": ฟังคำถาม ตอบเอง 6 วินาที แล้วเฉลย · "ซ่อนเกาหลี": ดูไทยแล้วพูด แตะเพื่อเฉลย · เสียง: @@voice@@ (edge-tts)</p>
</div>
<script>
const CATS = @@cats@@, CARDS = @@cards@@, D = @@data@@;   // D = flat lines; each has c (card index) and role q|a
const $ = s => document.querySelector(s);
function esc(s) { return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'})[c]); }
let cur = null, idx = -1, queue = [], rate = 1, loop = false, userPaused = false, cat = -1;
/* ---- render ---- */
$('#chips').innerHTML = '<button class="chip on" data-c="-1">ทั้งหมด<span class="c">' + CARDS.length + '</span></button>'
  + CATS.map((c, i) => '<button class="chip" data-c="' + i + '">' + esc(c) + '<span class="c">' + CARDS.filter(k => k.cat === i).length + '</span></button>').join('');
let html = '';
CARDS.forEach((K, ci) => {
  const qs = K.lines.filter(j => D[j].role === 'q'), as = K.lines.filter(j => D[j].role === 'a');
  const line = (j, n) => { const L = D[j]; return '<div class="ln" id="l' + j + '"><div class="n">' + n + '</div><div class="ko">' + L.html + '</div>'
    + '<p class="read">' + esc(L.read) + '</p><p class="th">' + L.thh + '</p><button class="play" aria-label="เล่น">▶</button></div>'; };
  html += '<article class="card" id="c' + ci + '" data-cat="' + K.cat + '"><div class="hd"><span class="no">' + (ci + 1) + '</span>'
    + '<span class="tw"><span class="ttl">' + esc(K.ttl) + '</span><span class="key">' + esc(K.key) + '</span></span>'
    + '<span class="right"><span class="meta">' + qs.length + ' คำถาม · ' + as.length + ' คำตอบ</span><button class="pc" aria-label="เล่นการ์ด">▶</button><span class="chev">▾</span></span>'
    + '<span class="pv">' + esc(D[qs[0]].ko) + '</span></div><div class="bd">'
    + '<div class="grp q"><div class="lbl">คำถาม · ถามได้หลายแบบ</div>' + qs.map((j, k) => line(j, 'Q' + (k + 1))).join('') + '</div>'
    + '<div class="grp a"><div class="lbl">ตอบได้ว่า</div>' + as.map(j => line(j, '↳')).join('') + '</div>'
    + (K.tip ? '<p class="tip">💡 ' + esc(K.tip) + '</p>' : '') + '</div></article>';
});
$('#list').innerHTML = html;
const card = ci => document.getElementById('c' + ci), el = j => document.getElementById('l' + j);
function visible() { return CARDS.map((K, i) => i).filter(i => cat < 0 || CARDS[i].cat === cat); }
function setCat(c) { cat = c; document.querySelectorAll('.chip').forEach(b => b.classList.toggle('on', +b.dataset.c === c));
  CARDS.forEach((K, i) => card(i).classList.toggle('hide', !(c < 0 || K.cat === c)));
  const v = visible(); $('#count').textContent = v.length + ' การ์ด · ' + v.reduce((s, i) => s + CARDS[i].lines.filter(j => D[j].role === 'q').length, 0) + ' คำถาม';
  window.scrollTo({ top: 0 }); }
$('#chips').onclick = ev => { const b = ev.target.closest('.chip'); if (b) setCat(+b.dataset.c); };
$('#chips').addEventListener('wheel', ev => { const c = $('#chips'); if (c.scrollWidth > c.clientWidth && ev.deltaY) { c.scrollLeft += ev.deltaY; ev.preventDefault(); } }, { passive: false });
$('#openall').onclick = () => visible().forEach(i => card(i).classList.add('open'));
$('#closeall').onclick = () => CARDS.forEach((K, i) => card(i).classList.remove('open'));
/* ---- playback ---- */
function clear(j) { const e = el(j); if (!e) return; e.classList.remove('playing'); e.querySelectorAll('.w').forEach(s => s.classList.remove('sung', 'now')); card(D[j].c).classList.remove('playing'); }
function stop() { if (cur) { const a = cur; cur = null; a.pause(); } if (idx >= 0) clear(idx); idx = -1; queue = []; userPaused = false; $('#pause').textContent = '⏸ หยุดชั่วคราว'; }
function play(j) {
  if (cur) { const a = cur; cur = null; a.pause(); } if (idx >= 0) clear(idx);
  idx = j; const L = D[j], e = el(j), K = card(L.c); K.classList.add('open', 'playing'); e.classList.add('playing'); userPaused = false; $('#pause').textContent = '⏸ หยุดชั่วคราว';
  const spans = [...e.querySelectorAll('.w')];
  const a = new Audio('data:audio/mpeg;base64,' + L.mp3); a.preservesPitch = true; a.playbackRate = rate; cur = a;
  const top = e.getBoundingClientRect().top, barH = $('.bar').offsetHeight + 12;
  if (top < barH || top > innerHeight - 120) e.scrollIntoView({ block: 'center', behavior: 'smooth' });
  function tick() { if (cur !== a) return; const t = a.currentTime; let k = -1;
    L.words.forEach((w, i) => { if (t >= w[0] - 0.05) k = i; });
    spans.forEach((s, i) => { s.classList.toggle('sung', i < k); s.classList.toggle('now', i === k); });
    if (!a.paused && !a.ended) requestAnimationFrame(tick); }
  a.onplay = () => requestAnimationFrame(tick);
  a.onended = () => { if (cur !== a) return; spans.forEach(s => { s.classList.add('sung'); s.classList.remove('now'); });
    if (loop) return play(j);
    if (queue.length) { const n = queue[0]; const gap = document.body.dataset.hide === 'a' && D[n].role === 'a' && L.role === 'q' ? 6000 : 500;
      return setTimeout(() => { if (cur === a) play(queue.shift()); }, gap); }
    cur = null; setTimeout(() => { if (idx === j && !cur) { clear(j); idx = -1; } }, 1200); };
  a.play().catch(() => {});
}
function cardSeq(ci) { const q = CARDS[ci].lines.filter(j => D[j].role === 'q'), a = CARDS[ci].lines.filter(j => D[j].role === 'a'); return [q[0], ...a]; }
$('#list').addEventListener('click', ev => {
  const pc = ev.target.closest('.pc'); if (pc) { ev.stopPropagation(); const ci = +pc.closest('.card').id.slice(1); queue = cardSeq(ci); play(queue.shift()); return; }
  const hd = ev.target.closest('.hd'); if (hd) { hd.parentNode.classList.toggle('open'); return; }
  const ln = ev.target.closest('.ln'); if (!ln) return; const j = +ln.id.slice(1);
  const h = document.body.dataset.hide, inA = ln.closest('.grp.a');
  if (h === 'ko' && !ev.target.closest('.play')) { ln.querySelector('.ko').classList.toggle('show'); return; }
  if (h === 'a' && inA && !ev.target.closest('.play') && !ln.classList.contains('show')) { ln.classList.add('show'); return; }
  queue = []; play(j);
});
$('#all').onclick = () => { queue = visible().flatMap(cardSeq); if (queue.length) play(queue.shift()); };
$('#pause').onclick = () => { if (!cur) return; if (cur.paused) { userPaused = false; cur.play(); $('#pause').textContent = '⏸ หยุดชั่วคราว'; } else { userPaused = true; cur.pause(); $('#pause').textContent = '▶ เล่นต่อ'; } };
$('#stop').onclick = stop;
$('#loop').onclick = () => { loop = !loop; $('#loop').classList.toggle('on', loop); };
$('#rate').onclick = ev => { const b = ev.target.closest('button'); if (!b) return; rate = +b.dataset.r; if (cur) cur.playbackRate = rate;
  $('#rate').querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b)); try { localStorage.setItem('rate', rate); } catch (e) {} };
$('#hide').onclick = ev => { const b = ev.target.closest('button'); if (!b) return; document.body.dataset.hide = b.dataset.h;
  $('#hide').querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b)); document.querySelectorAll('.ko.show, .ln.show').forEach(x => x.classList.remove('show')); };
const setTheme = (t, save) => { if (t) document.documentElement.dataset.theme = t; else delete document.documentElement.dataset.theme;
  $('#theme').querySelectorAll('button').forEach(x => x.classList.toggle('on', x.dataset.t === t)); if (save) try { localStorage.setItem('theme', t); } catch (e) {} };
$('#theme').onclick = ev => { const b = ev.target.closest('button'); if (b) setTheme(b.dataset.t, true); };
const setRead = (on, save) => { if (on) delete document.body.dataset.noread; else document.body.dataset.noread = '1';
  $('#read').classList.toggle('on', on); if (save) try { localStorage.setItem('read', on ? '1' : '0'); } catch (e) {} };
$('#read').onclick = () => setRead(!!document.body.dataset.noread, true);
const setSize = (v, save) => { document.documentElement.style.setProperty('--ts', v);
  $('#size').querySelectorAll('button').forEach(x => x.classList.toggle('on', x.dataset.s === String(v))); if (save) try { localStorage.setItem('size', v); } catch (e) {} };
$('#size').onclick = ev => { const b = ev.target.closest('button'); if (b) setSize(b.dataset.s, true); };
const setFold = (f, save) => { $('.bar').classList.toggle('fold', f); $('#fold').setAttribute('aria-expanded', f ? 'false' : 'true'); if (save) try { localStorage.setItem('fold', f ? '1' : '0'); } catch (e) {} };
$('#fold').onclick = () => setFold(!$('.bar').classList.contains('fold'), true);
try { const f = localStorage.getItem('fold'); setFold(f === null ? window.innerWidth < 640 : f === '1', false); } catch (e) { setFold(window.innerWidth < 640, false); }
try { if (localStorage.getItem('read') === '0') setRead(false, false); const z = localStorage.getItem('size'); if (z) setSize(z, false); } catch (e) {}
try { const t = localStorage.getItem('theme'); if (t !== null) setTheme(t, false); } catch (e) {}
try { const r = localStorage.getItem('rate'); if (r) { const b = $('#rate button[data-r="' + r + '"]'); if (b) b.click(); } } catch (e) {}
setCat(-1);
document.addEventListener('keydown', ev => { if (ev.target.tagName === 'INPUT') return;
  if (ev.key === ' ') { ev.preventDefault(); if (cur) $('#pause').click(); else $('#all').click(); }
  if (ev.key === 'ArrowDown' && idx >= 0 && idx + 1 < D.length) { ev.preventDefault(); queue = []; play(idx + 1); }
  if (ev.key === 'ArrowUp' && idx > 0) { ev.preventDefault(); queue = []; play(idx - 1); } });
</script>
'''


def main():
    name = next(a for a in sys.argv[1:] if not a.startswith('--'))
    voice = sa.VOICES[sys.argv[sys.argv.index('--voice') + 1]] if '--voice' in sys.argv else sa.VOICES['M']
    title, sub, cats, cards = parse(os.path.join(ROOT, 'content', 'speaking', f'{name}.md'))
    D = []
    for ci, K in enumerate(cards):
        idxs = []
        for L in K['lines']:
            L = dict(L, c=ci); idxs.append(len(D)); D.append(L)
        K['lines'] = idxs
    async def run():
        for L in D: L['mp3'], L['words'] = await sa.clip(L['ko'], sa.VOICES['F'] if L['role'] == 'q' else voice)
    asyncio.run(run())
    for L in D:
        L['html'] = sa.ko_html(L['ko'], L['words']); L['thh'] = sa.th_html(L['th'], L['ko']) if L['th'] else ''
        L['ko'] = kotag.strip_tags(L['ko']); L['th'] = kotag.strip_tags(L['th'])
    nq = sum(1 for L in D if L['role'] == 'q'); na = len(D) - nq
    vals = {'title': title, 'sub': sub or f'{len(cats)} หมวด · {len(cards)} การ์ด · {nq} คำถาม · {na} คำตอบ', 'voice': voice.replace('ko-KR-', '').replace('Neural', ''),
            'cats': json.dumps(cats, ensure_ascii=False), 'cards': json.dumps([{k: K[k] for k in ('cat', 'ttl', 'key', 'lines', 'tip')} for K in cards], ensure_ascii=False),
            'data': json.dumps(D, ensure_ascii=False), 'colors': kotag.CSS_COLORS}
    out = PAGE
    for k, v in vals.items(): out = out.replace('@@' + k + '@@', v)
    camel = ''.join(p.capitalize() for p in name.split('_'))
    dst = os.path.join(ROOT, 'output', '6_Speaking', f'KMU_Speaking_{camel}.html')
    open(dst, 'w', encoding='utf-8').write(out)
    print(f'{dst}  {os.path.getsize(dst) // 1024} KB, {len(cats)} cats, {len(cards)} cards, {nq} questions, {na} answers, voice {voice}')


if __name__ == '__main__':
    main()
