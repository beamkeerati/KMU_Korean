#!/usr/bin/env python3
"""Assemble the KMU study books from content/ and render them to output/.

    python3 scripts/build.py            # everything
    python3 scripts/build.py guide      # output/KMU_Guide_By_Unit.pdf + KMU_Guide_By_Topic.pdf (two books)
    python3 scripts/build.py exercises  # output/KMU_Workbook.pdf + KMU_Listening.pdf
    python3 scripts/build.py review     # output/review/KMU_Review_*.pdf — teacher's 복습문제 sets (parts merged)
    python3 scripts/build.py speaking   # output/KMU_Speaking_*.pdf — 발표 scripts from content/speaking/
    python3 scripts/build.py everyday   # output/everyday/KMU_Everyday_unitNN.pdf — ONE PDF PER UNIT
    python3 scripts/build.py miniexam   # output/miniexam/KMU_MiniExam_NN.pdf — 복습시험 (mini exam) as sat + key
    python3 scripts/build.py predict    # output/predictions/{everyday,miniexam}/KMU_Predict_*.pdf — exam-prediction sheets
                                        # (the teacher adds a test most days: drop a new
                                        #  content/exercises/everyday/unitNN.md and run `everyday`)

Intermediate Markdown goes to output/md/ (handy for grep); only PDFs sit in output/ itself.
Edit the Markdown in content/; never edit anything under output/ — it is overwritten on every build.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
OUTPUT = os.path.join(ROOT, 'output')
# output/ is organised by what the student does with each file (reorganised 2026-10-18, see output/START_HERE.html):
OUTPUT_GUIDES = os.path.join(OUTPUT, '1_Guides')         # the two guide books, mind maps, syllabus
OUTPUT_EXAM = os.path.join(OUTPUT, '3_Exam_Prep')        # teacher's review set + 복습시험/중간시험 predictions
OUTPUT_DAILY = os.path.join(OUTPUT, '4_Daily_Tests')     # per-unit 매일시험/연습지 + 매일시험 predictions
OUTPUT_HOMEWORK = os.path.join(OUTPUT, '5_Homework')     # workbook + 본문 듣기 sheets
OUTPUT_SPEAKING = os.path.join(OUTPUT, '6_Speaking')     # 발표 scripts
OUTPUT_MD = os.path.join(OUTPUT, '_build', 'md')         # intermediate .md, one per PDF (grep here)
OUTPUT_EVERYDAY = OUTPUT_DAILY
OUTPUT_MINIEXAM = os.path.join(OUTPUT_EXAM, 'past')      # 복습시험 papers as sat
OUTPUT_REVIEW = OUTPUT_EXAM
PREDICT_DIRS = {'everyday': os.path.join(OUTPUT_DAILY, 'predictions'), 'miniexam': OUTPUT_EXAM, 'midterm': OUTPUT_EXAM}
UNITS = range(5, 38)                                   # units the study material covers

# 매일시험 and 복습시험 predictions are kept apart at every level (the user asked for that):
# (sub-folder under content/predictions/, file glob, PDF basename prefix, banner title with {n})
PREDICTION_KINDS = [
    ('everyday', 'unit*.md', 'KMU_Predict_unit', '🔮 매일 시험 เก็งข้อสอบ — {n}과'),
    ('miniexam', 'exam*.md', 'KMU_Predict_miniexam', '🔮 복습시험 (mini exam) เก็งข้อสอบ — ครั้งที่ {n}'),
    ('midterm', 'midterm*.md', 'KMU_Predict_midterm', '🔮 중간시험 (สอบกลางภาค) เก็งข้อสอบ — 1~21과'),
]

# Each exercise source holds its questions, then its answer key. The heading
# below is the split point; everything from it onwards is the answer key.
# A source may be a single .md file, or a DIRECTORY of per-unit files
# (unit05.md, unit06.md, ...) that are concatenated in filename order — each
# unit file carries its own questions and its own answer key, split on the same
# heading. Files not matching unit*.md (e.g. 00_header.md) are ignored.
# (source dir, output basename, book title, subtitle, answer-key heading pattern)
EXERCISE_BOOKS = [
    ('workbook', 'KMU_Workbook',
     '📘 KMU Korean 1 — เวิร์กบุ๊ก (워크북)',
     'แบบฝึกหัดจากเวิร์กบุ๊กทุกบท พร้อมคำแปลไทย · เฉลยอยู่ท้ายเล่ม',
     r'^# \[PART 2\]'),
    ('listening', 'KMU_Listening',
     '🎧 KMU Korean 1 — 본문 듣기 (ชีตฟังบทสนทนาหลัก 5–22과)',
     'ใบฟังของศูนย์ทุกบท พร้อมคำแปลไทย · เฉลย = ประโยคจากบทสนทนาในตำรา · ใช้ซ้อมเขียนตามคำบอก (받아쓰기) ได้',
     r'^# 정답'),
]
EVERYDAY_ANSWER_PATTERN = r'^# 정답'


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    text = re.sub(r'\n{3,}', '\n\n', text).rstrip() + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    return text


def strip_own_titles(md):
    """Drop a part file's own `#` headings — the book supplies its own."""
    return re.sub(r'^# .*$', '', md, flags=re.M)


def split_exercise(md, answer_pattern):
    """Return (questions, answers) for one exercise source file."""
    lines = md.split('\n')
    cut = next((i for i, l in enumerate(lines) if re.match(answer_pattern, l)), len(lines))
    return '\n'.join(lines[:cut]), '\n'.join(lines[cut:])


def split_exercise_source(src, answer_pattern):
    """Same as split_exercise, but `src` may be a directory of unit*.md files."""
    if os.path.isfile(src):
        return split_exercise(read(src), answer_pattern)
    units = sorted(glob.glob(os.path.join(src, 'unit*.md')))
    if not units:
        sys.exit(f'no unit*.md files in {src}')
    # '---' reproduces the rule that sat under the PART heading in the old
    # single-file layout, so the rendered books are byte-identical.
    header = os.path.join(src, '00_header.md')
    qs = ([read(header).strip()] if os.path.exists(header) else []) + ['---']
    ans = ['---']
    for u in units:
        q, a = split_exercise(read(u), answer_pattern)
        qs.append(q.strip())
        ans.append(a.strip())
    return '\n\n'.join(qs), '\n\n'.join(ans)


WL  = '<span class="wl"></span>'    # one ruled line, full width
WL2 = '<span class="wl2"></span>'   # two ruled lines (sentence / short composition)


def add_writing_space(md):
    """Give write-in items the room the printed workbook gives them.

    - a whole-sentence answer (`나: (　　).`, `→ (　　)`, legacy `_____`) becomes a full-width ruled line
    - a word-sized blank `(　　)` is widened to 8 em so a real word fits
    - an item whose instruction asks to *write/make/change a sentence* gets two ruled lines
    """
    md = re.sub(r'(^|\s)(나|가)\s*:\s*\(　+\)\s*[.?]', lambda m: f'{m.group(1)}{m.group(2)}: {WL}', md, flags=re.M)
    md = re.sub(r'→[ \t]*\(　+\)[ \t]*[.?]?', '→ ' + WL, md)   # [ \t] not \s: never swallow the newline
    md = re.sub(r'_{6,}[ \t]*[.?]?', WL, md)
    md = re.sub(r'\(　{2,}\)', '(　　　　　　　　)', md)
    # sentence-writing sections: every numbered item that ends a line gets two ruled lines
    out, writing = [], False
    for line in md.split('\n'):
        if line.startswith('### '):
            writing = bool(re.search(r'문장을 (만|쓰|바꾸|완성)|쓰세요|바꾸세요|대답하세요', line)) and '고르' not in line and '단어' not in line
        elif line.startswith('#### '):
            # sub-sections (prediction papers): only explicit sentence instructions switch the ruled lines on
            writing = bool(re.search(r'문장을 (만|쓰|바꾸|완성)|대화를 완성|대답하세요|바꾸세요', line)) and '고르' not in line and '단어' not in line
        out.append(line)
        if writing and re.match(r'^\s*\d+[.)]\s', line) and WL not in line and WL2 not in line:
            out.append('   ' + WL2)
    return '\n'.join(out)


KEY_LABEL = r'\*\*[^*\n]{1,16}\.\*\*'     # **A.** · **14.** · **14–16.** · **ฟัง 4.**
KEY_ITEM = r'(\d+(?:-[a-z0-9])?)\)'          # 1) · 2) · 1-a)


def one_answer_per_line(md):
    """`**A.** 1) x 2) y` renders as a bullet per item, ordered by number."""
    def fmt(m):
        # top-level '- ' bullets: an indented bullet after the **A.** paragraph is a code block to Python-Markdown
        line = re.sub(r' ' + KEY_ITEM, r'\n- **\1)**', m.group(0))
        return re.sub(r'(' + KEY_LABEL + r')\s*' + KEY_ITEM, r'\1\n- **\2)**', line)
    # blank line before every **A.** block so a key written on consecutive lines doesn't lazy-continue
    return re.sub(r'^' + KEY_LABEL + r'.*$', lambda m: '\n' + fmt(m), md, flags=re.M)


def read_part(path):
    """A guide part is one .md file, or a directory whose .md files are joined in name order."""
    if os.path.isdir(path):
        files = sorted(glob.glob(os.path.join(path, '*.md')))
        return '\n\n'.join(read(f).strip() for f in files)
    return read(path).strip()


def countdown(md, today=None):
    """{{today}} → ISO date · {{days:YYYY-MM-DD}} → 'อีก N วัน' / 'วันนี้' / 'ผ่านแล้ว' — so ส่วนที่ 0 never goes stale."""
    import datetime
    today = today or datetime.date.today()
    def days(m):
        d = (datetime.date.fromisoformat(m.group(1)) - today).days
        return 'วันนี้' if d == 0 else (f'อีก {d} วัน' if d > 0 else 'ผ่านแล้ว')
    md = md.replace('{{today}}', today.isoformat())
    return re.sub(r'\{\{days:(\d{4}-\d{2}-\d{2})\}\}', days, md)


def guide_cover(title, subtitle):
    """00_exam_info.md (ส่วนที่ 0, shared by both books) with its own title/subtitle swapped for the book's."""
    body = read(os.path.join(CONTENT, 'guide', '00_exam_info.md')).strip()
    body = re.sub(r'^# .*\n+\*.*\*\n', f'# {title}\n\n*{subtitle}*\n', body, count=1)
    return body


def unit_part(sub, unit):
    f = os.path.join(CONTENT, 'guide', sub, f'unit{unit:02d}.md')
    return read(f).strip() if os.path.exists(f) else ''


def build_guide():
    """Two books from the same content/guide/ sources (split on the user's request 2026-10-16; parts renamed ส่วนที่ 10/16):

    KMU_Guide_By_Unit  = ส่วนที่ 0 exam info + ส่วนที่ 1: per unit 5–37 the 01_units chapter (teacher's slides merged inline)
                         followed by the centre's word list (04_vocabulary/unitNN.md)
    KMU_Guide_By_Topic = ส่วนที่ 0 + ส่วนที่ 1 grammar topics 01–35 (02_grammar, slides merged inline) + ส่วนที่ 2 은/는 vs 이/가
                         + ส่วนที่ 3 의문사 + ส่วนที่ 4 vocabulary by theme + ส่วนที่ 5 self-test + ส่วนที่ 6 quick table
    07_lecture/ is the slide transcription archive; its content now lives inside the chapters, so it is not assembled.
    """
    g = os.path.join(CONTENT, 'guide')
    chapters = []
    for u in UNITS:
        parts = [unit_part('01_units', u), unit_part('04_vocabulary', u)]
        chapters.append('\n\n'.join(p for p in parts if p))
    by_unit = '\n\n'.join([
        guide_cover('📘 KMU Korean 1 — คู่มือรายบท (5–37과)',
                    'เล่ม 1 จาก 2 · ส่วนที่ 0 ข้อมูลสอบ + ตารางไวยากรณ์ตามบท · ส่วนที่ 1 สรุปรายบท 5–37 (ไวยากรณ์ · สไลด์อาจารย์ · '
                    '대화 · 읽기 · ข้อสอบ) ตามด้วยคำศัพท์ของศูนย์ทุกบท · ไวยากรณ์เจาะลึกตามหัวข้ออยู่ในเล่ม 2 "คู่มือตามหัวข้อ" (อ้างเป็น ไวยากรณ์ข้อ NN)'),
        read(os.path.join(g, '01_units', '00_header.md')).strip(),
        *chapters])
    grammar = [read(f).strip() for f in sorted(glob.glob(os.path.join(g, '02_grammar', '[0-9][0-9]_*.md')))
               if not os.path.basename(f).startswith('00_')]
    vocab = ['# ส่วนที่ 4 · คลังคำศัพท์',
             '## 🖼️ คำศัพท์ตามหมวด (ชีตภาพของศูนย์)', read(os.path.join(g, '04_vocabulary', '90_themes.md')).strip()]
    cats = os.path.join(g, '04_vocabulary', '91_categories.md')
    if os.path.exists(cats):
        vocab += ['## 📂 คำศัพท์แยกหมวด (รวบรวมจากตำรา 5–37과)', strip_own_titles(read(cats)).strip()]
    by_topic = '\n\n'.join([
        guide_cover('📘 KMU Korean 1 — คู่มือตามหัวข้อ (5–37과)',
                    'เล่ม 2 จาก 2 · ส่วนที่ 0 ข้อมูลสอบ · ส่วนที่ 1 ไวยากรณ์เจาะลึก 64 หัวข้อ (สไลด์อาจารย์รวมอยู่ในแต่ละข้อ) · ส่วนที่ 2 은/는 vs 이/가 · '
                    'ส่วนที่ 3 คำถาม · ส่วนที่ 4 คำศัพท์ตามหมวด · ส่วนที่ 5 แบบทดสอบตัวเอง · ส่วนที่ 6 ตารางสรุป · สรุปรายบทอยู่ในเล่ม 1 "คู่มือรายบท"'),
        read(os.path.join(g, '02_grammar', '00_header.md')).strip(),
        *grammar,
        read_part(os.path.join(g, '03_particles.md')),
        read_part(os.path.join(g, '03b_question_words.md')),
        *vocab,
        read_part(os.path.join(g, '05_selftest.md')),
        read_part(os.path.join(g, '06_quickref.md'))])
    out = []
    for name, md in (('KMU_Guide_By_Unit', by_unit), ('KMU_Guide_By_Topic', by_topic)):
        path = os.path.join(OUTPUT_MD, name + '.md')
        write(path, countdown(md))
        out.append((path, OUTPUT_GUIDES))
    print('guide     : 2 books -> KMU_Guide_By_Unit.md, KMU_Guide_By_Topic.md')
    return out


def build_exercises():
    out = []
    for src_dir, base, title, subtitle, answer_pattern in EXERCISE_BOOKS:
        src = os.path.join(CONTENT, 'exercises', src_dir)
        q, a = split_exercise_source(src, answer_pattern)
        md = (f'# {title}\n\n*{subtitle}*\n\n## 목차 (สารบัญ)\n\n[TOC]\n\n'
              f'# ส่วนที่ 1 · แบบฝึกหัด (문제)\n\n{add_writing_space(strip_own_titles(q)).strip()}\n\n'
              f'# ส่วนที่ 2 · เฉลย (정답)\n\n{one_answer_per_line(strip_own_titles(a)).strip()}')
        path = os.path.join(OUTPUT_MD, base + '.md')
        write(path, md)
        print(f'{src_dir:9s} : -> {os.path.basename(path)}')
        out.append((path, OUTPUT_HOMEWORK))
    return out


def build_everyday_units():
    """One small PDF per everyday unit file: questions, then that unit's own answer key."""
    src = os.path.join(CONTENT, 'exercises', 'everyday')
    answer_pattern = EVERYDAY_ANSWER_PATTERN
    os.makedirs(os.path.join(OUTPUT_MD, 'everyday'), exist_ok=True)
    out = []
    for u in sorted(glob.glob(os.path.join(src, 'unit*.md'))):
        name = os.path.splitext(os.path.basename(u))[0]            # unit14
        q, a = split_exercise(read(u), answer_pattern)
        unit = re.sub(r'^unit0*', '', name).replace('_', ' ')          # 14 · 00 classroom
        md = (f'# 📝 매일 시험 · 연습지 — {unit}\n\n{add_writing_space(strip_own_titles(q)).strip()}\n\n'
              f'# 정답 (เฉลย)\n\n{one_answer_per_line(strip_own_titles(a)).strip()}')
        path = os.path.join(OUTPUT_MD, 'everyday', f'KMU_Everyday_{name}.md')
        write(path, md)
        out.append((path, OUTPUT_EVERYDAY))
    print(f'everyday  : {len(out)} unit files -> output/4_Daily_Tests/')
    return out


def build_miniexam():
    """One PDF per content/exercises/miniexam/examNN.md: the 복습시험 as sat (score sheet, 듣기, 읽기, 쓰기), then its key."""
    src = os.path.join(CONTENT, 'exercises', 'miniexam')
    os.makedirs(os.path.join(OUTPUT_MD, 'miniexam'), exist_ok=True)
    out = []
    for u in sorted(glob.glob(os.path.join(src, 'exam*.md'))):
        name = os.path.splitext(os.path.basename(u))[0]            # exam01
        n = re.sub(r'^exam0*', '', name)                           # 1
        q, a = split_exercise(read(u), EVERYDAY_ANSWER_PATTERN)
        md = (f'# 📝 복습시험 (mini exam) {n}\n\n{add_writing_space(strip_own_titles(q)).strip()}\n\n'
              f'# 정답 (เฉลย)\n\n{one_answer_per_line(strip_own_titles(a)).strip()}')
        path = os.path.join(OUTPUT_MD, 'miniexam', f'KMU_MiniExam_{n.zfill(2)}.md')
        write(path, md)
        out.append((path, OUTPUT_MINIEXAM))
    print(f'miniexam  : {len(out)} exam files -> output/3_Exam_Prep/past/')
    return out


def build_review():
    """Teacher's review problem sets. content/exercises/review/<name>_partN.md (or <name>.md)
    -> output/review/KMU_Review_<Name>.pdf: every part's questions, then every part's key."""
    src = os.path.join(CONTENT, 'exercises', 'review')
    os.makedirs(os.path.join(OUTPUT_MD, 'review'), exist_ok=True)
    groups = {}
    for f in sorted(glob.glob(os.path.join(src, '*.md'))):
        groups.setdefault(re.sub(r'_part\d+$', '', os.path.splitext(os.path.basename(f))[0]), []).append(f)
    out = []
    for name, files in groups.items():
        qs, ans = [], []
        for f in files:
            q, a = split_exercise(read(f), EVERYDAY_ANSWER_PATTERN)
            title = re.search(r'^## (.*)$', q, re.M)
            qs.append(q.strip())
            ans.append((f'## {title.group(1)}\n\n' if title else '') + re.sub(EVERYDAY_ANSWER_PATTERN, '', a, flags=re.M).strip())
        md = (f'# 📝 {name.replace("midterm", "중간시험 복습문제 ")} (แบบฝึกทบทวนที่ครูแจก)\n\n'
              f'*โจทย์ทุกข้อพร้อมคำแปลไทย · เฉลยท้ายเล่มเป็นเฉลยที่ AI ทำ ไม่ใช่ของครู*\n\n## 목차 (สารบัญ)\n\n[TOC]\n\n'
              f'# ส่วนที่ 1 · โจทย์ (문제)\n\n' + add_writing_space('\n\n'.join(qs)) +
              f'\n\n# ส่วนที่ 2 · เฉลย (정답)\n\n' + one_answer_per_line('\n\n'.join(ans)))
        path = os.path.join(OUTPUT_MD, 'review', 'KMU_Review_' + name.capitalize() + '.md')
        write(path, md)
        out.append((path, OUTPUT_REVIEW))
    print(f'review    : {len(out)} sets -> output/3_Exam_Prep/')
    return out


def build_speaking():
    """content/speaking/<snake_name>.md -> output/KMU_Speaking_<CamelName>.pdf (images resolved to content/speaking/)."""
    src = os.path.join(CONTENT, 'speaking')
    out = []
    for f in sorted(glob.glob(os.path.join(src, '*.md'))):
        stem = os.path.splitext(os.path.basename(f))[0]
        camel = ''.join(w.capitalize() for w in stem.split('_'))
        md = re.sub(r'src="([^"/]+)"', lambda m: f'src="{os.path.join(src, m.group(1))}"', read(f))
        path = os.path.join(OUTPUT_MD, f'KMU_Speaking_{camel}.md')
        write(path, md)
        out.append((path, OUTPUT_SPEAKING))
    print(f'speaking  : {len(out)} scripts -> output/6_Speaking/')
    return out


def build_predictions():
    """One PDF per prediction file: analysis + mock tests, then the mock tests' key.

    content/predictions/everyday/unitNN.md -> output/predictions/everyday/KMU_Predict_unitNN.pdf
    content/predictions/miniexam/examNN.md -> output/predictions/miniexam/KMU_Predict_miniexamNN.pdf
    content/predictions/midterm/midtermNN.md -> output/predictions/midterm/KMU_Predict_midtermNN.pdf
    """
    out = []
    for sub, pattern, prefix, banner in PREDICTION_KINDS:
        src = os.path.join(CONTENT, 'predictions', sub)
        md_dir = os.path.join(OUTPUT_MD, 'predictions', sub)
        pdf_dir = PREDICT_DIRS[sub]
        os.makedirs(md_dir, exist_ok=True)
        os.makedirs(pdf_dir, exist_ok=True)
        for u in sorted(glob.glob(os.path.join(src, pattern))):
            name = os.path.splitext(os.path.basename(u))[0]        # unit18 · exam02
            n = re.sub(r'^[a-z]+0*', '', name)                     # 18 · 2
            q, a = split_exercise(read(u), EVERYDAY_ANSWER_PATTERN)
            md = (f'# {banner.format(n=n)}\n\n{add_writing_space(strip_own_titles(q)).strip()}\n\n'
                  f'# 정답 (เฉลยข้อสอบจำลอง)\n\n{one_answer_per_line(strip_own_titles(a)).strip()}')
            path = os.path.join(md_dir, f'{prefix}{n.zfill(2)}.md')
            write(path, md)
            out.append((path, pdf_dir))
    print(f'predict   : {len(out)} files -> output/3_Exam_Prep/ · output/4_Daily_Tests/predictions/')
    return out


def to_pdf(jobs):
    """jobs = [(md_path, pdf_dir), ...] — rendered in groups by destination directory."""
    make_pdf = os.path.join(ROOT, 'scripts', 'make_pdf.py')
    for pdf_dir in dict.fromkeys(d for _, d in jobs):
        mds = [m for m, d in jobs if d == pdf_dir]
        subprocess.run([sys.executable, make_pdf] + mds + ['--pdf-dir', pdf_dir], check=True)


if __name__ == '__main__':
    for d in (OUTPUT, OUTPUT_MD, OUTPUT_GUIDES, OUTPUT_EXAM, OUTPUT_DAILY, OUTPUT_HOMEWORK, OUTPUT_SPEAKING, OUTPUT_MINIEXAM, *PREDICT_DIRS.values()):
        os.makedirs(d, exist_ok=True)
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    built = []
    if what in ('all', 'guide'):
        built += build_guide()
    if what in ('all', 'exercises'):
        built += build_exercises()
    if what in ('all', 'everyday'):
        built += build_everyday_units()
    if what in ('all', 'miniexam'):
        built += build_miniexam()
    if what in ('all', 'predict'):
        built += build_predictions()
    if what in ('all', 'review'):
        built += build_review()
    if what in ('all', 'speaking'):
        built += build_speaking()
    if not built:
        sys.exit(f'unknown target {what!r}; use: guide | exercises | everyday | miniexam | predict | review | speaking | all')
    to_pdf(built)
