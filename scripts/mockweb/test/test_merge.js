// scenario tests for the v55 cloud merge (pure functions; no claude runtime)
const fs = require('fs'), assert = require('assert');
const mem = {};
global.window = {}; global.document = { addEventListener() {} };
const signal = v => ({ value: v, peek() { return this.value; } });
const SETS = [{ id: 'mini03-writing' }, { id: 'mid-speaking' }];
const store = { get(k, d) { const v = mem['kmuweb:' + k]; return v ? JSON.parse(v) : d; }, put(k, v) { if (v === null || v === undefined) delete mem['kmuweb:' + k]; else mem['kmuweb:' + k] = JSON.stringify(v); } };
const later = f => f(), storeVer = signal(0), view = signal('home'), curSt = signal(null), mode = signal('cover'), openSet = () => {};
eval(fs.readFileSync(process.argv[2], 'utf8') + '\nglobal.cloud = cloud; global.canon = canon;');
const { _merge: merge, _local: localDoc, _remote: remoteDoc, _body: bodyOf } = cloud;
const id = 'mini03-writing', T0 = 1793873000000;
const setLocal = (vals, kt, stamp) => { Object.keys(mem).forEach(k => delete mem[k]); Object.entries(vals).forEach(([k, v]) => store.put(k + ':' + id, v)); if (kt) store.put('kt:' + id, kt); if (stamp) store.put('stamp:' + id, stamp); };
const run = r => merge(id, localDoc(id), remoteDoc(id, r));
const entry = { s: 57, t: 100, at: T0 + 1000, mode: 'exam' };

// 1. today's incident: this browser finished (ans/score/hist), a pre-v55 doc with a LATER at and nulls arrives
setLocal({ ans: { '0-0': ['x'] }, score: entry, hist: [entry], ai: { '0-0': { v: 'x' } } }, null, T0 + 1000);
let M = run({ at: T0 + 5000, ans: null, self: null, ai: { '0-0': { v: 'x' }, '6-2': { v: 'x' } }, attempt: null, score: null, hist: null });
assert.deepStrictEqual(M.vals.score, entry); assert.deepStrictEqual(M.vals.hist, [entry]); assert.deepStrictEqual(M.vals.ans, { '0-0': ['x'] });
assert.ok(M.vals.ai['6-2'], 'newer legacy ai still wins');
console.log('1 ok  stale pre-v55 doc cannot erase score/hist/answers');

// 2. a stale device starts a fresh attempt later: its new attempt wins, the finished score stays
setLocal({ ans: {}, self: {}, ai: {}, attempt: { mode: 'exam', left: 1800 } }, { ans: T0 + 9000, self: T0 + 9000, ai: T0 + 9000, attempt: T0 + 9000 });
M = run({ at: T0 + 2000, t: { ans: T0 + 900, ai: T0 + 2000, score: T0 + 1000, hist: T0 + 1000, attempt: T0 + 1000 }, ans: { '0-0': ['x'] }, ai: { a: 1 }, attempt: null, self: null, score: entry, hist: [entry] });
assert.deepStrictEqual(M.vals.ans, {}); assert.deepStrictEqual(M.vals.attempt, { mode: 'exam', left: 1800 }); assert.deepStrictEqual(M.vals.score, entry); assert.deepStrictEqual(M.vals.hist, [entry]);
console.log('2 ok  new attempt elsewhere keeps the old score in the history');

// 3. submit on two devices: hist is the union, score = newest attempt
const e2 = { s: 80, t: 100, at: T0 + 20000, mode: 'exam' };
setLocal({ score: e2, hist: [e2] }, { score: T0 + 20000, hist: T0 + 20000 });
M = run({ at: T0 + 1000, t: { score: T0 + 1000, hist: T0 + 1000 }, score: entry, hist: [entry] });
assert.deepStrictEqual(M.vals.hist, [entry, e2]); assert.deepStrictEqual(M.vals.score, e2);
console.log('3 ok  two finished attempts → both kept, newest is the score');

// 4. regrade (AI) of the same attempt: the later regrade wins, no duplicate
const e1b = { ...entry, s: 61 };
setLocal({ score: e1b, hist: [e1b] }, { score: T0 + 30000, hist: T0 + 30000 });
M = run({ at: T0 + 1000, t: { score: T0 + 1000, hist: T0 + 1000 }, score: entry, hist: [entry] });
assert.deepStrictEqual(M.vals.hist, [e1b]); assert.deepStrictEqual(M.vals.score, e1b);
console.log('4 ok  same attempt regraded → one entry, newer points');

// 5. 🗑 reset here removes the older attempts even though the cloud still has them; an attempt after the reset survives
setLocal({}, { ans: T0 + 40000, score: T0 + 40000, hist: T0 + 40000, reset: T0 + 40000 });
M = run({ at: T0 + 20000, t: { score: T0 + 20000, hist: T0 + 20000 }, score: e2, hist: [entry, e2] });
assert.strictEqual(M.vals.score, null); assert.strictEqual(M.vals.hist, null); assert.strictEqual(M.t.reset, T0 + 40000);
const e3 = { s: 90, t: 100, at: T0 + 50000 };
setLocal({ score: e3, hist: [e3] }, { score: T0 + 50000, hist: T0 + 50000 });
M = run({ at: T0 + 40000, t: { reset: T0 + 40000, score: T0 + 40000 }, score: null, hist: null });
assert.deepStrictEqual(M.vals.hist, [e3]);
const pre = { s: 1, t: 100, at: T0 + 100 };
setLocal({ score: pre, hist: [pre] }, { score: T0 + 100, hist: T0 + 100 });
M = run({ at: T0 + 40000, t: { reset: T0 + 40000 }, score: null, hist: null });
assert.strictEqual(M.vals.score, null, 'a device that missed the reset cannot bring old attempts back');
console.log('5 ok  reset propagates both ways; later attempts survive');

// 6. convergence: merging the written body back gives the same body (no write loop), even with the store reordering keys
setLocal({ ans: { b: ['2'], a: ['1'] }, ai: { k: { v: 'x', fb: 'f', fix: 'g' } }, score: entry, hist: [entry] }, null, T0 + 1000);
M = run({ at: T0 + 5000, ans: null, ai: null, score: null, hist: null, self: null, attempt: null });
const body = bodyOf(M); const shuffled = JSON.parse(JSON.stringify(body, Object.keys(body).sort().reverse()));
const keysRev = o => o && typeof o === 'object' && !Array.isArray(o) ? Object.fromEntries(Object.keys(o).reverse().map(k => [k, keysRev(o[k])])) : o;
const M2 = merge(id, { vals: M.vals, t: M.t, legacy: false }, remoteDoc(id, keysRev(body)));
assert.strictEqual(canon(bodyOf(M2)), canon(keysRev(body))); assert.strictEqual(canon(bodyOf(M2)), canon(body));
console.log('6 ok  merge is stable → no write ping-pong');

// 7. vocabulary: per word, more answers wins; a cleared record (higher ep) wins whole
const V = 'srs';
Object.keys(mem).forEach(k => delete mem[k]);
store.put('vocab:' + V, { w: { 가: { b: 2, n: 5, l: 10 }, 나: { b: 0, n: 1, l: 9 } }, days: { d1: { n: 6, r: 4 } } }); store.put('kt:' + V, { vocab: T0 });
M = merge(V, localDoc(V), remoteDoc(V, { at: T0 + 1, t: { vocab: T0 + 1 }, vocab: { w: { 가: { b: 1, n: 3, l: 10 }, 다: { b: 1, n: 1, l: 10 } }, days: { d1: { n: 3, r: 2 }, d2: { n: 1, r: 1 } } } }));
assert.strictEqual(M.vals.vocab.w.가.n, 5); assert.ok(M.vals.vocab.w.나 && M.vals.vocab.w.다); assert.strictEqual(M.vals.vocab.days.d1.n, 6); assert.ok(M.vals.vocab.days.d2);
M = merge(V, localDoc(V), remoteDoc(V, { at: T0 + 1, t: { vocab: T0 + 1 }, vocab: { w: {}, days: {}, ep: 1 } }));
assert.deepStrictEqual(M.vals.vocab, { w: {}, days: {}, ep: 1 });
console.log('7 ok  vocab merges per word; clearing statistics wins');
console.log('ALL OK');
