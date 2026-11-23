#!/usr/bin/env bash
# Screenshots of the BUILT practice site (output/2_Practice_Web — run scripts/build_mockweb.py after editing app.html) for UI work.
# Audio clips are stubbed out; all shots of one run share one fresh Chrome profile (empty scores; steps of an earlier line persist).
#
#   bash scripts/mockweb/test/shot.sh <<'EOF'
#   m_home   390  844 -             -
#   m_paper  390  844 final-combine text:.mode-btn:ฝึกทำ;;scroll:900
#   t_home  1024  768 -             -
#   EOF
#   one shot per line: name width height hash (- = home) steps (- = none; see shot.html) → extracted/web_shots/<name>.png
#
#   bash scripts/mockweb/test/shot.sh --sheet A m_home m_paper ...   → extracted/web_shots/A.png (side by side, to view in ONE image read)
# A 390×844 shot costs ≈ 440 tokens to view, a 4-phone sheet ≈ 1.8k.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"; OUT="$ROOT/extracted/web_shots"; mkdir -p "$OUT"
if [ "${1:-}" = "--sheet" ]; then
  shift; name="$1"; shift
  python3 - "$OUT" "$name" "$@" <<'PY'
import sys
from PIL import Image
out, name, parts = sys.argv[1], sys.argv[2], sys.argv[3:]
ims = [Image.open(f'{out}/{p}.png').convert('RGB') for p in parts]
g = 12; o = Image.new('RGB', (sum(i.width for i in ims) + g * (len(ims) - 1), max(i.height for i in ims)), '#444'); x = 0
for i in ims: o.paste(i, (x, 0)); x += i.width + g
o.save(f'{out}/{name}.png'); print(f'{out}/{name}.png', o.size)
PY
  exit 0
fi
W="$(mktemp -d)"; trap 'kill $SRV 2>/dev/null || true; rm -rf "$W"' EXIT
for f in "$ROOT"/output/2_Practice_Web/*.js "$ROOT"/output/2_Practice_Web/index.html; do b=$(basename "$f"); case $b in clips*.js) : > "$W/$b";; *) ln -s "$f" "$W/$b";; esac; done
echo 'window.KMU_CLIPS = {};' > "$W/clips.js"; cp "$ROOT/scripts/mockweb/test/shot.html" "$W/"
PORT=$((20000 + RANDOM % 20000)); (cd "$W" && exec python3 -m http.server $PORT --bind 127.0.0.1 >/dev/null 2>&1) & SRV=$!; sleep 1
while read -r name w h hash steps; do
  [ -z "${name:-}" ] && continue; case $name in \#*) continue;; esac
  url="http://127.0.0.1:$PORT/shot.html?w=$w&h=$h&hash=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$hash")&do=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "${steps:--}")"
  timeout 60 google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --user-data-dir="$W/prof" --window-size="$w,$h" \
    --virtual-time-budget=12000 --screenshot="$OUT/$name.png" "$url" >/dev/null 2>&1 || echo "FAIL $name"
  echo "$OUT/$name.png"
done
