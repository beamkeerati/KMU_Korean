"""Where things live (2026-11-25, one folder per level).

    REPO/                 shared: scripts/ specs/ docs/ tools/ inbox/ CLAUDE.md
    REPO/levels/<N>/      one level (1 = 1급, 2 = 2급 …): source/ content/ output/ extracted/
    REPO/levels/current   the level scripts build by default (one number)

Every script imports ROOT from here instead of computing the repo root, so all the level-relative paths
('content/...', 'source/...', 'output/...', 'extracted/...') keep working unchanged.
Build another level:  KMU_LEVEL=1 python3 scripts/build.py everyday
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def current_level():
    env = os.environ.get('KMU_LEVEL', '').strip()
    if env:
        return env
    with open(os.path.join(REPO, 'levels', 'current'), encoding='utf-8') as f:
        return f.read().strip()


LEVEL = current_level()
ROOT = os.path.join(REPO, 'levels', LEVEL)          # the level's root: source/ content/ output/ extracted/
SPECS = os.path.join(REPO, 'specs')                 # SPEC_* contracts and BRIEF_* agent briefs (shared by every level)
TOOLS = os.path.join(REPO, 'tools')                 # git-ignored binaries (Real-ESRGAN …)

if not os.path.isdir(ROOT):
    raise SystemExit(f'kmu_paths: level folder {ROOT} does not exist (levels/current or KMU_LEVEL = {LEVEL!r})')
