// two devices, one fake cloud: replay today's incident through the real v55 sync code (live listener + queued read-merge-write)
const fs = require('fs'), assert = require('assert');
const SRC = fs.readFileSync(process.argv[2], 'utf8');
const realST = setTimeout; global.setTimeout = (f, ms) => realST(f, Math.min(ms, 15)); // fast clock
const cloudDocs = {}, listeners = []; let writes = 0;
const clone = o => JSON.parse(JSON.stringify(o));
const snapOf = (ids) => ({ docs: Object.keys(cloudDocs).map(id => ({ id, exists: true, data: () => clone(cloudDocs[id]) })),
  docChanges() { return ids.map(id => ({ type: 'modified', doc: { id, exists: true, data: () => clone(cloudDocs[id]) } })); }, metadata: { fromCache: false, hasPendingWrites: false } });
const fakeDb = { collection: () => ({
  doc: id => ({ get: async () => ({ exists: id in cloudDocs, data: () => clone(cloudDocs[id]) }),
                set: async body => { writes++; cloudDocs[id] = clone(body); listeners.forEach(l => realST(() => l(snapOf([id])), 2)); } }),
  onSnapshot(next) { listeners.push(next); realST(() => next({ ...snapOf(Object.keys(cloudDocs)), docChanges() { return Object.keys(cloudDocs).map(id => ({ type: 'added', doc: { id, exists: true, data: () => clone(cloudDocs[id]) } })); } }), 2); return () => {}; } }) };
function device(name) {
  const mem = {}, signal = v => ({ value: v, peek() { return this.value; } });
  const window = { claude: { use: async n => n === 'db' ? fakeDb : { id: async () => 'u1' } } }, document = { addEventListener() {}, visibilityState: 'visible' };
  const SETS = [{ id: 'mini03-writing' }];
  const store = { get(k, d) { const v = mem['kmuweb:' + k]; return v ? JSON.parse(v) : d; }, put(k, v) { if (v === null || v === undefined) delete mem['kmuweb:' + k]; else mem['kmuweb:' + k] = JSON.stringify(v); },
    set(k, v) { this.put(k, v); const m = /^(ans|self|score|ai|hist|attempt|vocab):(.+)$/.exec(k); if (m) { const now = Date.now(), kt = this.get('kt:' + m[2], null) || {}; kt[m[1]] = now; this.put('kt:' + m[2], kt); this.put('stamp:' + m[2], now); cloud.queue(m[2]); } } };
  const later = f => f(), storeVer = signal(0), view = signal('home'), curSt = signal(null), mode = signal('cover'), openSet = () => {};
  let cloud; eval(SRC.replace('var cloud =', 'cloud =').replace('window.addEventListener', '(()=>{})'));
  return { name, store, mem };
}
const wait = ms => new Promise(r => realST(r, ms));
(async () => {
  const A = device('PC'), B = device('iPad');
  const id = 'mini03-writing';
  // the iPad once touched the set long ago (its copy has no score) — that stale copy is what wiped the result under v54
  B.store.set('ai:' + id, { old: { v: 'o' } });
  await wait(300);
  // PC takes the exam and submits
  A.store.set('ans:' + id, {}); A.store.set('attempt:' + id, { mode: 'exam', left: 1800 });
  await wait(20); A.store.set('ans:' + id, { '0-0': ['불벼워요'] });
  await wait(20); const entry = { s: 57, t: 100, at: Date.now(), mode: 'exam' };
  A.store.set('attempt:' + id, null); A.store.set('score:' + id, entry); A.store.set('hist:' + id, [entry]);
  // meanwhile the iPad writes its stale ai (as an in-flight AI reply would)
  B.store.set('ai:' + id, { old: { v: 'o' }, more: { v: 'x' } });
  await wait(300);
  A.store.set('ai:' + id, { '0-0': { v: 'x' } });   // the PC's AI grades land after
  await wait(500);
  const c = cloudDocs[id];
  assert.deepStrictEqual(c.score, entry, 'cloud keeps the score'); assert.deepStrictEqual(c.hist, [entry]);
  assert.deepStrictEqual(c.ans, { '0-0': ['불벼워요'] });
  for (const D of [A, B]) { assert.deepStrictEqual(D.store.get('score:' + id), entry, D.name + ' has the score'); assert.deepStrictEqual(D.store.get('ans:' + id), { '0-0': ['불벼워요'] }, D.name + ' has the answers'); }
  assert.strictEqual(canon_(A.store.get('ai:' + id)), canon_(B.store.get('ai:' + id)), 'both devices agree on ai');
  const w0 = writes; await wait(400); assert.strictEqual(writes, w0, 'no write loop once settled');
  console.log('E2E OK — cloud + both devices keep 57/100 and the answers; writes total', writes, '; settled with no further writes');
  process.exit(0);
})().catch(e => { console.error('E2E FAIL', e.message); process.exit(1); });
function canon_(v) { return JSON.stringify(v, Object.keys(v || {}).sort()); }
