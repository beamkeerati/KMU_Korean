(function () {   // test prelude: per-"device" storage namespace + fake claude runtime backed by the parent's fake cloud
window.addEventListener("error", e => { (parent.ERRS = parent.ERRS || []).push(location.search + " " + e.message + " @" + e.lineno); });
  const q = new URLSearchParams(location.search), P = q.get('dev') || '';
  if (P) { const S = Storage.prototype, g = S.getItem, s = S.setItem, r = S.removeItem;
    S.getItem = function (k) { return g.call(this, P + k); }; S.setItem = function (k, v) { return s.call(this, P + k, v); }; S.removeItem = function (k) { return r.call(this, P + k); }; }
  const noListen = q.get('nolisten') === '1';
  window.claude = { use: async name => { await new Promise(r => setTimeout(r, 30));
    if (name === 'db') return parent.FAKE.db(noListen); if (name === 'user') return { id: async () => 'u1' }; return null; } };
})();
