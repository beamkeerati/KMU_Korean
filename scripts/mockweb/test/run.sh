#!/usr/bin/env bash
# Sync regression tests for the practice site (run after touching the `cloud` module or store/attempt code in app.html).
#   1. node: merge scenarios (test_merge.js) + a 2-device fake-cloud replay of the 2026-11-05 loss (test_e2e.js)
#   2. headless Chrome: the built page in 5 windows (3 tabs sharing one localStorage, a 2nd device, a poll-only device) on a fake cloud
# Usage: bash scripts/mockweb/test/run.sh   (needs node, google-chrome, python3; builds nothing — run build_mockweb.py first)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"; T="$ROOT/scripts/mockweb/test"; W="$(mktemp -d)"
LV="$ROOT/levels/${KMU_LEVEL:-$(cat "$ROOT/levels/current")}"   # the level whose built site is tested
trap 'kill $SRV 2>/dev/null || true; rm -rf "$W"' EXIT
python3 - "$ROOT" "$W" "$LV" <<'PY'
import sys, re
root, w, lv = sys.argv[1:]
s = open(root + '/scripts/mockweb/app.html', encoding='utf-8').read()
open(w + '/cloud_only.js', 'w').write('const externalChange = () => {};\n' + s[s.index('const syncS = signal('):s.index('/* ------------------------------------------------------------------ components: top strip')])
b = open(lv + '/output/2_Practice_Web/index.html', encoding='utf-8').read()
open(w + '/app.html', 'w', encoding='utf-8').write(b.replace('<script src="vendor.js"></script>', '<script src="prelude.js"></script>\n<script src="vendor.js"></script>', 1))
PY
node "$T/test_merge.js" "$W/cloud_only.js" | tail -1
node "$T/test_e2e.js" "$W/cloud_only.js"
cp "$LV/output/2_Practice_Web/"{vendor.js,data.js,vocab.js} "$T/harness.html" "$T/prelude.js" "$W/"
echo 'window.KMU_CLIPS = {};' > "$W/clips.js"; for f in clips2 clips3 clips4; do : > "$W/$f.js"; done   # audio is not needed for sync tests
PORT=$((20000 + RANDOM % 20000)); (cd "$W" && exec python3 -m http.server $PORT --bind 127.0.0.1 >/dev/null 2>&1) & SRV=$!; sleep 1
timeout 240 google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir="$W/prof" --virtual-time-budget=120000 --dump-dom "http://127.0.0.1:$PORT/harness.html" 2>/dev/null \
  | sed -n '/<pre id="out">/,/DONE/p' | sed 's/<[^>]*>//g' | cut -c1-220 | tee "$W/out.txt"
! grep -q '^FAIL\|^ERROR' "$W/out.txt"
