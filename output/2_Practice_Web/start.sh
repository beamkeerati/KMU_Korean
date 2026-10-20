#!/bin/sh
# Serve the practice site on localhost (Chrome allows the microphone there) and open it.
cd "$(dirname "$0")"
( sleep 1; xdg-open http://localhost:8000/index.html >/dev/null 2>&1 ) &
python3 -m http.server 8000 --bind 127.0.0.1
