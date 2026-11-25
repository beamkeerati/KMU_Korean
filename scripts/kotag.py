#!/usr/bin/env python3
"""Colour-by-function markup for the study material (Korean + Thai).

Tag syntax inside Markdown:  {c:text}   c = one letter
    n คำนาม/สรรพนาม   p 조사 (particle)   v กริยา/คุณศัพท์ (stem)   e ตัวลงท้าย/กาล/이다
    q 의문사           x ปฏิเสธ           m ตัวเลข/ลักษณนาม          a วิเศษณ์/คำบอกเวลา
    UPPERCASE letter = the same class but honorific (dotted underline): {E:세요} {P:께서} {V:드리}

Korean text is tagged automatically at build time (Kiwi morphological analyser + override rules);
Thai glosses `*(…)*`, speaking 🇹🇭 lines and the ไทย columns of tables get a first-pass automatic tagging
(PyThaiNLP segmentation + lexicons).  Anything that already carries {c:} tags is left untouched, so
hand/agent corrections written into content/*.md always win.

CLI:  python3 scripts/kotag.py tag "저는 학생이에요 *(ฉันเป็นนักเรียน)*"
      python3 scripts/kotag.py check content/guide/02_grammar/02_ida-anida.md   # print tagged lines
      python3 scripts/kotag.py extract <md files…> > batch.tsv                  # gloss pairs for review
      python3 scripts/kotag.py merge batch_out.tsv                              # write reviewed tags back
"""
import glob
import html
import os
import re
import sys

sys.path.insert(0, os.path.expanduser('~/.local/lib/python3.12/site-packages'))

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)
VOCAB_GLOB = os.path.join(ROOT, 'content', 'guide', '04_vocabulary', 'unit*.md')

# ------------------------------------------------------------------ palette & legend
CLASSES = {
    'n': ('คำนาม', '명사', '#1d4ed8'),
    'p': ('조사', '조사', '#c2410c'),
    'v': ('กริยา·คุณศัพท์', '동사·형용사', '#15803d'),
    'e': ('ตัวลงท้าย·กาล·이다', '어미', '#7e22ce'),
    'q': ('คำถาม', '의문사', '#0f766e'),
    'x': ('ปฏิเสธ', '부정', '#dc2626'),
    'm': ('ตัวเลข·ลักษณนาม', '숫자', '#b45309'),
    'a': ('วิเศษณ์·เวลา', '부사', '#57534e'),
}
P_BG = '#ffedd5'

CSS_COLORS = """
/* ---- colour by function (scripts/kotag.py) ---- */
.kn { color: #1d4ed8; }
.kp { color: #c2410c; background: #ffedd5; border-radius: 3px; padding: 0 1px; }
.kv { color: #15803d; }
.ke { color: #7e22ce; }
.kq { color: #0f766e; }
.kx { color: #dc2626; }
.km { color: #b45309; }
.ka { color: #57534e; }
.kh { text-decoration: underline dotted; text-underline-offset: 2px; }
span[class^="k"] strong { color: inherit; }
th .kp { background: none; }
.klegend { font-size: 8.5px; color: #57606a; white-space: nowrap; }
.klegend span { margin-right: 6px; }
"""

LEGEND_HTML = ('<div class="klegend" style="position: running(klegend)">สี = หน้าที่ของคำ: '
               + ' '.join(f'<span class="k{c}">{th}</span>' for c, (th, ko, _) in CLASSES.items())
               + ' <span class="kh">ขีดจุด = ยกย่อง</span></div>')

# ------------------------------------------------------------------ Korean lexicons
PARTICLES = {'은', '는', '이', '가', '을', '를', '에', '에서', '도', '만', '하고', '와', '과', '의', '한테', '한테서',
             '에게', '에게서', '께', '께서', '부터', '까지', '이랑', '랑', '으로', '로', '보다', '처럼', '마다', '밖에',
             '이나', '나', '(이)랑', '(으)로', '(이)나'}
HON_PARTICLES = {'께', '께서'}
ENDINGS = {'이에요', '예요', '입니다', '입니까', '아요', '어요', '여요', '해요', '습니다', '습니까', 'ㅂ니다', 'ㅂ니까',
           '세요', '으세요', '십니다', '으십니다', '십니까', '으십니까', '셨어요', '으셨어요', '시', '으시', '겠', '겠어요',
           '겠습니다', '았', '었', '였', '았어요', '었어요', '였어요', '이었어요', '였어요', '거예요', '것입니다', '을', 'ㄹ',
           '고', '지', '네요', '까요', '을까요', 'ㄹ까요', '러', '으러', '고 있어요', '다', '이다', '아', '어', '여',
           '았습니다', '었습니다', '였습니다', '아서', '어서', '여서', '면', '으면', '니까', '으니까', '는', 'ㄴ', '은', '을래요',
           '고요', '죠', '지요', '세요?', '거야'}
HON_ENDINGS = {'세요', '으세요', '십니다', '으십니다', '십니까', '으십니까', '셨어요', '으셨어요', '시', '으시', '세요?'}
NEG_TOKENS = {'안', '못', '않아요', '않다', '않습니다', '아니에요', '아니다', '아닙니다', '아니요', '아니오', '없어요', '없다',
              '없습니다', '마세요', '않았어요', '아니었어요', '지 않아요', '지 않다', '지 마세요'}
Q_WORDS = {'누구', '누가', '뭐', '무엇', '뭘', '무엇을', '어디', '언제', '왜', '어떻게', '얼마', '얼마나', '몇', '어느', '무슨',
           '어떤', '어때요', '어땠어요', '어때', '며칠', '누구를', '누구하고', '누구한테', '누구한테서', '어디에', '어디에서',
           '어디서', '언제부터', '언제까지', '누구세요', '누구예요', '뭐예요', '어디예요'}
Q_MM = {'어느', '무슨', '어떤', '몇'}
Q_NP = {'누구', '뭐', '무엇', '어디'}
Q_MAG = {'언제', '왜', '어떻게', '얼마나'}
NATIVE_NUM_MM = {'한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉', '열', '스무', '스물', '서른', '마흔', '쉰',
                 '열한', '열두', '열세', '열네', '스물한', '스물두', '스물세', '스물네'}
COUNTERS = {'개', '명', '마리', '권', '병', '잔', '장', '살', '분', '시', '층', '호', '번', '원', '년', '월', '일', '달', '주',
            '시간', '그릇', '켤레', '벌', '송이', '대', '과', '학년', '쪽', '번째', '인분', '킬로', '미터', '센티', '도',
            '사람', '분의', '개월', '주일', '학기', '교시', '등', '위', '회', '곡', '편', '통', '봉지', '상자', '컵', '조각',
            '바이트'}
HON_VERB_LEMMAS = {'드리', '드시', '잡수시', '계시', '주무시', '주무', '드', '계', '잡수', '뵙', '모시', '여쭈', '여쭙'}
HON_NOUNS = {'분', '님', '댁', '생신', '말씀', '연세', '성함', '진지', '분들'}
TIME_ADVERBS = {'어제', '오늘', '내일', '모레', '그제', '지금', '매일', '매주', '매달', '매년', '요즘', '보통', '아까', '이따가',
                '나중에', '먼저', '자주', '가끔', '항상', '늘', '벌써', '아직', '다시', '또', '같이', '함께', '혼자', '일찍',
                '늦게', '빨리', '천천히', '열심히', '많이', '조금', '좀', '아주', '정말', '너무', '참', '잘', '제일', '가장',
                '곧', '금방', '방금', '오래', '잠깐', '잠시', '거의', '전혀', '별로', '꼭', '그냥', '정도'}
NAMES = {'마키', '투이', '카오루', '간토야', '왕쯔이', '윤아', '빔', '유키', '리처드', '마이클', '왕징', '안나', '제임스',
         '하루키', '수잔', '톰', '민수', '지영', '수진', '영희', '철수', '준호', '미나', '링링', '왕밍', '흐엉', '나타샤',
         '사라', '다니엘', '이반', '아이린', '매튜', '제니', '케빈', '폴', '메리', '존', '마리아', '소피아', '루카스',
         '마이크', '빌', '앤디', '리사', '에밀리', '타쿠야', '유코', '리에', '히로', '밍밍', '샤오밍', '왕리', '첸',
         '이리나', '알렉세이', '바트', '장핑', '압둘라', '제프리', '지훈', '이지훈', '뚜언', '아민', '마르코', '스티브', '제시카',
         '마리코', '유리', '소피', '레이', '왕핑', '리밍', '하나', '다나카', '스미스'}

_kiwi = None
_noun_set = None


def _nouns():
    global _noun_set
    if _noun_set is None:
        _noun_set = {ko.split('(')[0].strip() for ko, _ in _vocab_rows()}
        _noun_set |= {w[:-2] for w in list(_noun_set) if w.endswith('하다') and w[:-2] not in ('좋아', '싫어', '미안', '죄송', '피곤', '깨끗', '조용', '유명', '친절', '따뜻', '시원', '복잡', '심심', '건강', '행복', '안녕')}
        _noun_set |= {'공부', '운동', '숙제', '일', '요리', '전화', '청소', '산책', '쇼핑', '수영', '노래', '이야기', '말', '준비',
                      '시작', '도착', '출발', '결혼', '사랑', '생각', '구경', '여행', '식사', '연습', '질문', '대답', '세수', '목욕',
                      '샤워', '빨래', '설거지', '운전', '등산', '소개', '초대', '약속', '계획', '졸업', '입학', '취직', '퇴근',
                      '출근', '수업', '아르바이트', '감사', '축하', '사진', '게임', '데이트', '회의', '발표', '인사', '주문', '예약'}
    return _noun_set


def _vocab_rows():
    """(korean, thai) pairs from the centre's vocabulary tables."""
    rows = []
    for path in sorted(glob.glob(VOCAB_GLOB)):
        with open(path, encoding='utf-8') as f:
            for line in f:
                if not line.startswith('|'):
                    continue
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) < 2 or cells[0] in ('단어', '한국어') or set(cells[0]) <= set('-: '):
                    continue
                ko = re.sub(r'\*\*', '', cells[0]).strip()
                th = re.sub(r'\*\*', '', cells[1]).strip()
                if ko and re.search(r'[가-힣]', ko):
                    rows.append((ko, th))
    return rows


def _korean_vocab_class(ko):
    """Class of a vocabulary head-word (used for the Thai lexicon): what the Korean tagger says, else heuristics."""
    w = ko.split('(')[0].strip()
    try:
        found = {c.lower() for c, _ in TAG_RE.findall(tag_korean(w))} - {'e', 'p'}
        if len(found) == 1:
            return found.pop()
    except Exception:
        pass
    if w in Q_WORDS:
        return 'q'
    if w in TIME_ADVERBS:
        return 'a'
    if w in PARTICLES or w.startswith('-') or w.startswith('('):
        return 'p' if w.strip('-') in PARTICLES else 'e'
    if w in NEG_TOKENS:
        return 'x'
    if re.fullmatch(r'[0-9]+|[일이삼사오육칠팔구십백천만억]+|하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉|열|스물', w):
        return 'm'
    if w.endswith('다'):
        return 'v'
    return 'n'


def kiwi():
    global _kiwi
    if _kiwi is None:
        from kiwipiepy import Kiwi
        _kiwi = Kiwi()
        for w in TIME_ADVERBS:
            _kiwi.add_user_word(w, 'MAG', 6)
        for w in NAMES:
            _kiwi.add_user_word(w, 'NNP', 5)
        for w, t in (('싫어하', 'VV'), ('주무', 'VV'), ('계', 'VV'), ('드', 'VV'), ('잡수', 'VV'), ('지난', 'MM'),
                     ('이번', 'MM'), ('다음', 'MM'), ('매', 'MM'), ('여러', 'MM'), ('모든', 'MM')):
            _kiwi.add_user_word(w, t, 5)
        pre = {'누가': [('누구', 'NP'), ('가', 'JKS')],
               '드세요': [('드', 'VV'), ('세요', 'EF')], '드셨어요': [('드', 'VV'), ('시', 'EP'), ('었', 'EP'), ('어요', 'EF')],
               '드십니다': [('드', 'VV'), ('시', 'EP'), ('\u11b8니다', 'EF')], '드십니까': [('드', 'VV'), ('시', 'EP'), ('\u11b8니까', 'EF')],
               '드실': [('드', 'VV'), ('시', 'EP'), ('\u11af', 'ETM')],
               '계세요': [('계', 'VV'), ('세요', 'EF')], '계셨어요': [('계', 'VV'), ('시', 'EP'), ('었', 'EP'), ('어요', 'EF')],
               '계십니다': [('계', 'VV'), ('시', 'EP'), ('\u11b8니다', 'EF')], '계십니까': [('계', 'VV'), ('시', 'EP'), ('\u11b8니까', 'EF')],
               '주무세요': [('주무', 'VV'), ('세요', 'EF')], '주무셨어요': [('주무', 'VV'), ('시', 'EP'), ('었', 'EP'), ('어요', 'EF')],
               '주무십니다': [('주무', 'VV'), ('시', 'EP'), ('\u11b8니다', 'EF')], '주무십니까': [('주무', 'VV'), ('시', 'EP'), ('\u11b8니까', 'EF')],
               '마셔요': [('마시', 'VV'), ('어요', 'EF')], '마셔': [('마시', 'VV'), ('어', 'EF')],
               '잡수세요': [('잡수', 'VV'), ('세요', 'EF')], '잡수십니다': [('잡수', 'VV'), ('시', 'EP'), ('\u11b8니다', 'EF')]}
        for form, analysis in pre.items():
            try:
                _kiwi.add_pre_analyzed_word(form, analysis, 10)
            except Exception as ex:
                print('pre-analyzed failed:', form, ex, file=sys.stderr)
        skip = Q_WORDS | PARTICLES | NEG_TOKENS | ENDINGS | TIME_ADVERBS | {'누가', '뭘', '제', '내', '네', '저', '나', '우리'}
        for ko, _ in _vocab_rows():
            w = ko.split('(')[0].strip()
            if ' ' in w or not re.fullmatch(r'[가-힣]+', w) or w in skip:
                continue
            if w.endswith('하다') and len(w) > 3 and w[:-2] not in ('좋아', '싫어'):
                _kiwi.add_user_word(w[:-2], 'NNG', 3)
            elif not w.endswith('다') and w not in TIME_ADVERBS and len(w) >= 2:
                _kiwi.add_user_word(w, 'NNG', 3)
    return _kiwi


# ------------------------------------------------------------------ Korean tagging
HANGUL = re.compile(r'[가-힣]')
JAMO = re.compile(r'[ㄱ-ㅎㅏ-ㅣ]')
KO_RUN = re.compile(r'(?:-?\((?=[으이스아어]))?-?(?:[0-9][0-9,.:]*(?=[가-힣]))?[가-힣ㄱ-ㅎㅏ-ㅣ][가-힣ㄱ-ㅎㅏ-ㅣ0-9 　.,?!~·/()\-\'"…:;%]*')
TAG_RE = re.compile(r'\{([a-zA-Z]):([^{}]*)\}')


def _is_pattern_token(tok):
    t = tok.strip('*.,?!·')
    return bool(JAMO.search(t)) or t.startswith('-') or '(으)' in t or '(이)' in t or '(스)' in t or '(아/어)' in t


def _direct_class(part, prev_tok=None):
    p = part.strip('-?.,!·()')
    if p in Q_WORDS:
        return 'q'
    if p in NEG_TOKENS or '않' in p or '마세요' in p or p in ('안', '못'):
        return 'x'
    if p in HON_PARTICLES:
        return 'P'
    if p in PARTICLES:
        return 'p'
    if p in HON_ENDINGS or p.startswith(('세요', '으세요', '십니', '으십니', '셨', '으셨', '(으)세요', '(으)시', '(으)십니')):
        return 'E'
    if prev_tok and prev_tok.strip('-') == '고' and p in ('있어요', '있다', '있습니다', '계세요', '계십니다'):
        return 'e'
    if p in ENDINGS or _is_pattern_token(part) or p.startswith('-'):
        return 'e'
    return None


PATTERN_PAREN = ('으)', '이)', '스)', '아/어', '어/아')


def _grammar_parts(tok):
    """Pieces of '이/가(은/는)' or '에서~까지' that must each be a grammar item."""
    core = tok
    for pre in ('-(', '('):
        if core.startswith(pre) and core[len(pre):].startswith(PATTERN_PAREN):
            core = core.replace('(', '', 1).replace(')', '', 1)
            break
    return [p for p in re.split(r'[/~()]', core.strip('*.,?!·')) if p]


def _tag_direct_token(tok, prev_tok=None):
    """A grammar-item token: '은/는', '-(으)ㄹ', '이에요/예요', '께서', '이/가(은/는)', '에서~까지'."""
    out = []
    pattern_paren = tok.lstrip('-').startswith('(') and tok.lstrip('-')[1:].startswith(PATTERN_PAREN)
    pieces = [tok] if pattern_paren else re.split(r'([/~()])', tok)
    for part in pieces:
        if part in ('/', '~', '(', ')') or not part:
            out.append(part)
            continue
        m = re.match(r'^([(\-]*)(.*?)([?.,!·)]*)$', part)
        lead, core, trail = m.groups()
        c = _direct_class(part, prev_tok)
        if c is None or not core:
            out.append(part)
        elif lead.endswith('(') and not pattern_paren:
            out.append(f'{lead}{{{c}:{core}}}{trail}')
        else:
            out.append(f'{{{c}:{lead}{core}}}{trail}')     # keep "-" / "-(으)" inside the span
    return ''.join(out)


def _classify_kiwi(toks):
    cls = [None] * len(toks)
    for i, t in enumerate(toks):
        f, tag = t.form, t.tag
        base = tag.split('-')[0]
        prev = cls[i - 1] if i else None
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        c = None
        if base in ('SF', 'SP', 'SS', 'SSO', 'SSC', 'SE', 'SO', 'SW', 'SH', 'SL', 'SB') or base.startswith('W_'):
            c = None
        elif base == 'SN' or base == 'NR':
            c = 'm'
        elif base == 'MM':
            c = 'q' if f in Q_MM else 'm' if f in NATIVE_NUM_MM else 'n'
        elif base == 'NP':
            c = 'q' if f in Q_NP else 'n'
        elif base == 'MAG':
            c = 'x' if f in ('안', '못') else 'q' if f in Q_MAG else 'a'
        elif base in ('MAJ', 'IC'):
            c = 'x' if f in ('아니요', '아니오', '아뇨') else 'a'
        elif base in ('NNG', 'NNP', 'XSN', 'XR', 'XPN'):
            if f in ('얼마', '누가', '뭘', '무엇', '누구', '어디', '언제'):
                c = 'q'
            elif f in COUNTERS and prev == 'm':
                c = 'm'
            elif nxt is not None and nxt.tag.startswith('XSA') and f not in _nouns():
                c = 'v'                       # 피곤 + 하다 → adjective root (but 공부 + 하 stays a noun)
            elif f in HON_NOUNS:
                c = 'N'
            else:
                c = 'n'
        elif base == 'NNB':
            if f in COUNTERS and prev in ('m', 'q'):
                c = 'm'
            elif f in ('거', '것') and i and toks[i - 1].tag.startswith('ETM'):
                c = 'e'
            elif f in HON_NOUNS:
                c = 'N'
            else:
                c = 'n'
        elif base in ('VV', 'VA', 'VX', 'VCP', 'VCN', 'XSV', 'XSA'):
            if base == 'VCN' or (base == 'VX' and f == '않') or (base == 'VA' and f == '없') or f == '못하' \
                    or (base == 'VX' and f == '말' and i and toks[i - 1].form == '지'):
                c = 'x'
            elif base == 'VA' and f == '어떻':
                c = 'q'
            elif base == 'VCP':
                c = 'e'
            elif base == 'VX':
                c = 'e'
            elif f in HON_VERB_LEMMAS:
                c = 'V'
            else:
                c = 'v'
        elif base == 'EP':
            c = 'E' if f in ('시', '으시') else 'e'
        elif base in ('EF', 'EC', 'ETM', 'ETN'):
            if base == 'EC' and f == '지' and nxt is not None and nxt.form in ('않', '말') and nxt.tag.startswith('VX'):
                c = 'x'
            elif base == 'EF' and f.startswith(('세요', '으세요', '십니', '으십니', '셔요', '으셔요')):
                c = 'E'
            else:
                c = 'e'
        elif base.startswith('J'):
            c = 'm' if f in COUNTERS and prev == 'm' and f != '의' else 'P' if f in HON_PARTICLES else 'p'
        else:
            c = 'n' if HANGUL.search(f) else None
        # inheritance: endings after a negation / honorific / 어떻 stem keep that colour
        if c == 'e' and prev in ('x', 'E'):
            c = prev
        elif c == 'e' and prev == 'q' and toks[i - 1].form == '어떻':
            c = 'q'
        elif c == 'E' and prev == 'x':
            c = 'x'
        cls[i] = c
    return cls


def _tag_kiwi_chunk(s):
    """Tag a plain Korean chunk (sentence or phrase) with Kiwi, earliest morpheme wins each character."""
    if not HANGUL.search(s):
        return s
    toks = kiwi().tokenize(s)
    cls = _classify_kiwi(toks)
    chars = [None] * len(s)
    for t, c in zip(toks, cls):
        if c is None or t.len == 0:
            continue
        split_at = None
        if c == 'v' and t.form.endswith('하') and len(t.form) >= 3 and t.form[:-1] in _nouns() and t.len >= 2:
            split_at = t.start + t.len - 1                 # 공부해요 → 공부 (n) + 해 (v)
        for k in range(t.start, min(t.start + t.len, len(s))):
            if chars[k] is None:
                chars[k] = 'n' if split_at is not None and k < split_at else c
    for k, ch in enumerate(s):                 # spaces and punctuation stay outside the spans
        if ch in ',:' and 0 < k < len(s) - 1 and s[k - 1].isdigit() and s[k + 1].isdigit():
            continue
        if ch.isspace() or ch in '.,?!~·/()\'"…:;%　':
            chars[k] = None
    out, i = [], 0
    while i < len(s):
        c = chars[i]
        j = i
        while j < len(s) and chars[j] == c:
            j += 1
        seg = s[i:j]
        out.append(f'{{{c}:{seg}}}' if c else seg)
        i = j
    return ''.join(out)


def tag_korean(run, glued=False):
    """Tag one Korean run (no markdown inside). Returns the run with {c:} tags.
    glued=True: the run continues a word (…**이 있어요**), so a leading 이/가/은/는 is a particle."""
    if '{' in run or not HANGUL.search(run) and not JAMO.search(run):
        return run
    toks = run.split(' ')
    if toks and re.fullmatch(r'[가-힣]{2,6}:', toks[0]):           # speaker label 이리나: / 아주머니:
        return f'{{n:{toks[0][:-1]}}}:' + (' ' + tag_korean(' '.join(toks[1:]), glued) if len(toks) > 1 else '')
    kinds = []
    for tok in toks:
        core = tok.strip('*.,?!·()')
        if not core:
            kinds.append('plain')
        elif _is_pattern_token(tok) or (re.search(r'[/~()]', core) and all(
                p.strip('-?.,!·') in PARTICLES | ENDINGS | NEG_TOKENS | Q_WORDS for p in _grammar_parts(core))):
            kinds.append('direct')
        elif core == '해요' and not tok.startswith('-'):
            kinds.append('kiwi')          # bare 해요 after '**안**' / '청소**를**' is the verb 하다, not the ending -해요
        elif core in PARTICLES | ENDINGS | NEG_TOKENS | Q_WORDS:
            kinds.append('cand')
        else:
            kinds.append('kiwi')
    grammar_only = all(k != 'kiwi' for k in kinds)
    out, buf, prev_tok = [], [], None

    def flush():
        if buf:
            out.append(_tag_kiwi_chunk(' '.join(buf)))
            buf.clear()

    for ti, (tok, kind) in enumerate(zip(toks, kinds)):
        if kind == 'cand' and not buf and (glued or not (tok.strip('*.,?!·()') in ('이', '그', '저') and ti + 1 < len(toks))):
            kind = 'direct'
        if kind == 'direct' or (kind == 'cand' and grammar_only):
            flush()
            out.append(_tag_direct_token(tok, prev_tok))
        elif kind == 'plain':
            flush()
            out.append(tok)
        else:
            buf.append(tok)
        prev_tok = tok
    flush()
    return ' '.join(out)


# ------------------------------------------------------------------ Thai tagging
THAI = re.compile(r'[ก-๙]')
_th_tok = None
_th_tok2 = None
_th_lex = None
TH_UNTAGGED = {'ค่ะ', 'ครับ', 'คะ', 'นะ', 'สิ', 'เลย', 'ล่ะ', 'หรือ', 'เหรอ', 'ไหม', 'มั้ย', 'น่ะ', 'ซิ', 'จ้ะ', 'จ้า', 'เถอะ',
               'เถิด', 'หรอ', 'เนี่ย', 'ยัง', 'ว่า', 'ที่ว่า', 'อ่ะ', 'อะ', 'กัน', 'ซะ', 'เสีย'}
TH_FUNC = {
    # e: copula / tense / aspect
    'เป็น': 'e', 'คือ': 'e', 'แล้ว': 'e', 'จะ': 'e', 'กำลัง': 'e', 'เคย': 'e', 'ได้': 'e', 'อยู่': 'e', 'ไว้': 'e',
    'กำลังจะ': 'e', 'เพิ่ง': 'e', 'เพิ่งจะ': 'e',
    # p: particle counterparts
    'ที่': 'p', 'ใน': 'p', 'กับ': 'p', 'และ': 'p', 'ก็': 'p', 'ด้วย': 'p', 'แค่': 'p', 'เท่านั้น': 'p', 'จาก': 'p',
    'ถึง': 'p', 'จนถึง': 'p', 'ตั้งแต่': 'p', 'ของ': 'p', 'แก่': 'p', 'ตอน': 'p', 'เมื่อ': 'p', 'ละ': 'p', 'สำหรับ': 'p',
    'โดย': 'p', 'ทาง': 'p', 'บน': 'p', 'ใต้': 'p', 'ข้าง': 'p', 'หน้า': 'p', 'หลัง': 'p', 'นอก': 'p', 'ยัง': 'p',
    'ให้แก่': 'p', 'ไปยัง': 'p', 'ส่วน': 'p', 'เฉพาะ': 'p', 'ทั้ง': 'p', 'แม้แต่': 'p', 'หรือ': 'p', 'เพียง': 'p',
    # q
    'ใคร': 'q', 'อะไร': 'q', 'ที่ไหน': 'q', 'ไหน': 'q', 'เมื่อไร': 'q', 'เมื่อไหร่': 'q', 'กี่': 'q', 'เท่าไร': 'q',
    'เท่าไหร่': 'q', 'อย่างไร': 'q', 'ยังไง': 'q', 'ทำไม': 'q', 'แบบไหน': 'q', 'อันไหน': 'q', 'เป็นอย่างไร': 'q',
    'เป็นยังไง': 'q', 'เป็นไง': 'q', 'บ่ายโมง': 'm', 'เที่ยง': 'm', 'เที่ยงคืน': 'm', 'เที่ยงวัน': 'm', 'ตรงไหน': 'q', 'กี่โมง': 'q', 'วันที่เท่าไร': 'q', 'วันที่เท่าไหร่': 'q',
    'เมื่อไรถึงเมื่อไร': 'q', 'นานแค่ไหน': 'q', 'แค่ไหน': 'q', 'หรือเปล่า': 'q', 'ไหม': None,
    # x
    'ไม่': 'x', 'ไม่ใช่': 'x', 'ไม่มี': 'x', 'ไม่ได้': 'x', 'ไม่ค่อย': 'x', 'ไม่เคย': 'x', 'มิใช่': 'x', 'ห้าม': 'x',
    'อย่า': 'x', 'ไม่ครับ': 'x', 'ไม่ค่ะ': 'x', 'เปล่า': 'x',
    # a
    'มาก': 'a', 'มากๆ': 'a', 'จริงๆ': 'a', 'จริง ๆ': 'a', 'ด้วยกัน': 'a', 'บ่อย': 'a', 'บ่อยๆ': 'a', 'เสมอ': 'a',
    'ทุกวัน': 'a', 'วันนี้': 'a', 'พรุ่งนี้': 'a', 'เมื่อวาน': 'a', 'เมื่อวานนี้': 'a', 'ตอนนี้': 'a', 'ช่วงนี้': 'a',
    'เดี๋ยวนี้': 'a', 'ก่อน': 'a', 'ทีหลัง': 'a', 'ค่อนข้าง': 'a', 'นิดหน่อย': 'a', 'หน่อย': 'a', 'อีก': 'a', 'แล้วก็': 'a',
    'ดังนั้น': 'a', 'งั้น': 'a', 'ถ้างั้น': 'a', 'แต่': 'a', 'เก่ง': 'a', 'ขยัน': 'a', 'เร็ว': 'a', 'ช้า': 'a', 'ช้าๆ': 'a',
    'เร็วๆ': 'a', 'เช้า': 'a', 'มะรืน': 'a', 'ตั้งใจ': 'a', 'สุดๆ': 'a', 'ที่สุด': 'a', 'เกินไป': 'a', 'ปกติ': 'a',
    'มักจะ': 'a', 'ยังคง': 'a', 'คนเดียว': 'a', 'เอง': 'a', 'พร้อมกัน': 'a', 'ทันที': 'a', 'เดี๋ยว': 'a', 'เมื่อกี้': 'a',
    'แล้วจึง': 'a', 'ตรง': 'a', 'ทุกสัปดาห์': 'a', 'ทุกเดือน': 'a', 'ทุกปี': 'a', 'แรก': 'a', 'ตอนแรก': 'a', 'ล่วงหน้า': 'a',
    'ก่อนหน้า': 'a', 'นาน': 'a', 'ไม่นาน': 'a', 'สักครู่': 'a', 'ค่อย': 'a', 'ตลอด': 'a', 'บางที': 'a', 'บางครั้ง': 'a',
    'เสร็จ': 'a', 'หมด': 'a', 'น้อย': 'a', 'เยอะ': 'a', 'สักหน่อย': 'a', 'เท่า': 'a', 'เช่นกัน': 'a', 'เหมือนกัน': 'a',
    'เดิน': 'v', 'เล่น': 'v', 'เดินเล่น': 'v', 'วิ่ง': 'v', 'นั่ง': 'v', 'ยืน': 'v', 'นอน': 'v', 'ตื่น': 'v', 'ล้าง': 'v',
    'อาบน้ำ': 'v', 'แปรงฟัน': 'v', 'ใส่': 'v', 'สวม': 'v', 'ถอด': 'v', 'เปิด': 'v', 'ปิด': 'v', 'ส่ง': 'v', 'รับ': 'v',
    'ถ่าย': 'v', 'ถ่ายรูป': 'v', 'โอน': 'v', 'ถอน': 'v', 'ยืม': 'v', 'คืน': 'v', 'สอน': 'v', 'พบ': 'v', 'เจอ': 'v',
    'คุย': 'v', 'ถาม': 'v', 'ตอบ': 'v', 'รอ': 'v', 'ช่วย': 'v', 'ขอ': 'v', 'เริ่ม': 'v', 'จบ': 'v', 'เลิก': 'v',
    'ออก': 'v', 'เข้า': 'v', 'ขึ้น': 'v', 'ลง': 'v', 'ขับ': 'v', 'ขี่': 'v', 'ว่ายน้ำ': 'v', 'เต้น': 'v', 'เต้นรำ': 'v',
    'ร้องเพลง': 'v', 'ร้อง': 'v', 'มอง': 'v', 'เที่ยว': 'v', 'ไปเที่ยว': 'v', 'พัก': 'v', 'พักผ่อน': 'v', 'เหนื่อย': 'v',
    'สนุก': 'v', 'น่าเบื่อ': 'v', 'สวย': 'v', 'หล่อ': 'v', 'ใหญ่': 'v', 'เล็ก': 'v', 'สูง': 'v', 'เตี้ย': 'v', 'ยาว': 'v',
    'สั้น': 'v', 'แพง': 'v', 'ถูก': 'v', 'ดี': 'v', 'แย่': 'v', 'อร่อย': 'v', 'ร้อน': 'v', 'หนาว': 'v', 'เย็น': 'v',
    'อุ่น': 'v', 'ยุ่ง': 'v', 'ว่าง': 'v', 'ง่าย': 'v', 'ยาก': 'v', 'ใกล้': 'v', 'ไกล': 'v', 'ใจดี': 'v', 'น่ารัก': 'v',
    'สะอาด': 'v', 'สกปรก': 'v', 'เงียบ': 'v', 'ดัง': 'v', 'กว้าง': 'v', 'แคบ': 'v', 'หนัก': 'v', 'เบา': 'v', 'อ้วน': 'v',
    'ผอม': 'v', 'ป่วย': 'v', 'สบาย': 'v', 'หิว': 'v', 'อิ่ม': 'v', 'ง่วง': 'v', 'เบื่อ': 'v', 'ดีใจ': 'v', 'เสียใจ': 'v',
    'กลับ': 'v', 'กลับบ้าน': 'v', 'มาถึง': 'v', 'ไปถึง': 'v', 'ย้าย': 'v', 'อาศัย': 'v', 'พัง': 'v', 'ซ่อม': 'v', 'จ่าย': 'v',
    'สั่ง': 'v', 'จอง': 'v', 'นัด': 'v', 'แต่งงาน': 'v', 'เกิด': 'v', 'ตาย': 'v', 'ใช้': 'v', 'ลอง': 'v', 'คิด': 'v',
    'ลืม': 'v', 'จำ': 'v', 'เข้าใจ': 'v', 'หัด': 'v', 'ฝึก': 'v', 'สมัคร': 'v', 'เตรียม': 'v', 'ล้างจาน': 'v', 'ซักผ้า': 'v',
    'ทำสวน': 'v', 'ปลูก': 'v', 'เลี้ยง': 'v', 'อยาก': 'e', 'ต้อง': 'e', 'ควร': 'e', 'สามารถ': 'e', 'ลอง…ดู': 'e',
    'ไป': 'v', 'มา': 'v', 'ทะเล': 'n', 'ภูเขา': 'n', 'แล้วจะ': 'e', 'คิมชีจีแก': 'n', 'คิมชีจจีแก': 'n', 'จจีแก': 'n', 'จีแก': 'n', 'ซุป': 'n', 'บ่อย ๆ': 'a',
    'มกราคม': 'n', 'กุมภาพันธ์': 'n', 'มีนาคม': 'n', 'เมษายน': 'n', 'พฤษภาคม': 'n', 'มิถุนายน': 'n', 'กรกฎาคม': 'n',
    'สิงหาคม': 'n', 'กันยายน': 'n', 'ตุลาคม': 'n', 'พฤศจิกายน': 'n', 'ธันวาคม': 'n', 'มกรา': 'n', 'กุมภา': 'n', 'มีนา': 'n',
    'เมษา': 'n', 'พฤษภา': 'n', 'มิถุนา': 'n', 'กรกฎา': 'n', 'สิงหา': 'n', 'กันยา': 'n', 'ตุลา': 'n', 'พฤศจิกา': 'n', 'ธันวา': 'n',
    'วันจันทร์': 'n', 'วันอังคาร': 'n', 'วันพุธ': 'n', 'วันพฤหัสบดี': 'n', 'วันพฤหัส': 'n', 'วันศุกร์': 'n', 'วันเสาร์': 'n',
    'วันอาทิตย์': 'n', 'สุดสัปดาห์': 'n', 'ปิดเทอม': 'n', 'ตอนเช้า': 'n', 'ตอนบ่าย': 'n', 'ตอนเย็น': 'n', 'ตอนกลางคืน': 'n',
    'ผม': 'n', 'ฉัน': 'n', 'ดิฉัน': 'n', 'เรา': 'n', 'พวกเรา': 'n', 'คุณ': 'n', 'เขา': 'n', 'เธอ': 'n', 'พวกเขา': 'n',
    'มัน': 'n', 'นี่': 'n', 'นั่น': 'n', 'โน่น': 'n', 'นี้': 'n', 'นั้น': 'n', 'โน้น': 'n', 'ที่นี่': 'n', 'ที่นั่น': 'n',
    'ที่โน่น': 'n', 'ตรงนี้': 'n', 'ตรงนั้น': 'n', 'อันนี้': 'n', 'อันนั้น': 'n', 'สิ่งนี้': 'n', 'สิ่งนั้น': 'n', 'คนนี้': 'n',
    'คนนั้น': 'n', 'ตัวเอง': 'n', 'ทุกคน': 'n', 'ใครๆ': 'n', 'บางคน': 'n',
    'ขอโทษ': 'v', 'ขอบคุณ': 'v', 'สวัสดี': 'v', 'ใช่': 'a', 'ค่ะ ใช่': 'a', 'ไม่อยู่': 'x', 'ไม่ชอบ': 'x', 'ไม่รู้': 'x',
    'ไม่เป็นไร': 'x', 'ไม่ได้ไป': 'x', 'ยังไม่': 'x', 'ไม่เคย': 'x',
    # names & proper nouns (transliterations the Thai dictionary does not know)
    'มากิ': 'n', 'ทูย': 'n', 'คาโอรุ': 'n', 'คันโตยะ': 'n', 'หวางจื่ออี': 'n', 'หวางจิ้ง': 'n', 'ยุนอา': 'n', 'บีม': 'n',
    'ยูกิ': 'n', 'ริชาร์ด': 'n', 'ไมเคิล': 'n', 'แอนนา': 'n', 'เจมส์': 'n', 'ฮารุกิ': 'n', 'ซูซาน': 'n', 'ทอม': 'n',
    'มินซู': 'n', 'จียอง': 'n', 'ซูจิน': 'n', 'ยองฮี': 'n', 'ชอลซู': 'n', 'จุนโฮ': 'n', 'มินา': 'n', 'หลิงหลิง': 'n',
    'หวางหมิง': 'n', 'เฮือง': 'n', 'ฮืออง': 'n', 'นาตาชา': 'n', 'ซาร่า': 'n', 'ดาเนียล': 'n', 'อีวาน': 'n', 'บาท': 'n',
    'กุกมิน': 'n', 'มหาวิทยาลัยกุกมิน': 'n', 'โซล': 'n', 'ปูซาน': 'n', 'พูซาน': 'n', 'คยองบกกุง': 'n', 'มยองดง': 'n',
    'อินซาดง': 'n', 'ทงแดมุน': 'n', 'นัมซาน': 'n', 'ฮันกัง': 'n', 'เชจู': 'n', 'เชจูโด': 'n', 'ชองนึง': 'n', 'ชงโน': 'n',
    'ฮงแด': 'n', 'คังนัม': 'n', 'อิแทวอน': 'n', 'กรุงเทพฯ': 'n', 'กรุงเทพ': 'n', 'เชียงใหม่': 'n', 'ภูเก็ต': 'n',
    'เกาหลี': 'n', 'ประเทศเกาหลี': 'n', 'ญี่ปุ่น': 'n', 'จีน': 'n', 'ไทย': 'n', 'ประเทศไทย': 'n', 'อเมริกา': 'n',
    'เวียดนาม': 'n', 'มองโกเลีย': 'n', 'ฝรั่งเศส': 'n', 'เยอรมนี': 'n', 'อังกฤษ': 'n', 'รัสเซีย': 'n', 'อินเดีย': 'n',
    'ศูนย์ภาษาเกาหลี': 'n', 'ศูนย์': 'n', 'พุลโกกี': 'n', 'พุลโกกิ': 'n', 'คิมบับ': 'n', 'คิมจิ': 'n', 'พิบิมบับ': 'n',
    'ราเมียน': 'n', 'ราเมน': 'n', 'ต๊อกปกกี': 'n', 'ซัมกเยทัง': 'n', 'จาจังมยอน': 'n', 'เทควันโด': 'n', 'โทร': 'v', 'ทำ': 'v', 'เรียน': 'v', 'ทำงาน': 'v', 'ออกกำลังกาย': 'v',
    'ทำความสะอาด': 'v', 'ซื้อ': 'v', 'ขาย': 'v', 'กิน': 'v', 'ดื่ม': 'v', 'ดู': 'v', 'อ่าน': 'v', 'เขียน': 'v', 'ฟัง': 'v',
    'พูด': 'v', 'ชอบ': 'v', 'รัก': 'v', 'รู้': 'v', 'รู้จัก': 'v', 'มี': 'v', 'ชื่อ': 'n', 'เชิญ': 'v',
    # honorific
    'ท่าน': 'N', 'ท่านนี้': 'N', 'มอบ': 'V', 'รับประทาน': 'V', 'ทาน': 'V', 'บรรทม': 'V', 'เรียน': 'v',
}
TH_CLASSIFIERS = {'คน', 'ตัว', 'เล่ม', 'ขวด', 'แก้ว', 'ใบ', 'ชิ้น', 'อัน', 'ลูก', 'ชั้น', 'โมง', 'นาที', 'วอน', 'บาท', 'ปี',
                  'เดือน', 'วัน', 'ครั้ง', 'ห้อง', 'เบอร์', 'ขวบ', 'ทุ่ม', 'คู่', 'จาน', 'ถ้วย', 'ดอก', 'คัน', 'หลัง',
                  'ฉบับ', 'แผ่น', 'เครื่อง', 'ที่', 'สัปดาห์', 'อาทิตย์', 'ชั่วโมง', 'วินาที', 'ครึ่ง', 'ท่าน', 'บท',
                  'เทอม', 'ภาค', 'ข้อ', 'หน้า', 'ด้าน', 'ถุง', 'กล่อง', 'กิโล', 'เมตร', 'องศา', 'ชุด', 'ดวง', 'เรื่อง',
                  'ช่อ', 'ก้อน', 'เส้น', 'ชาม', 'ขอน', 'ม้วน', 'ชิ้นส่วน', 'คัน', 'ลำ', 'เที่ยว', 'รอบ', 'ครั้ง',
                  'ผล', 'ต้น', 'ด้าม', 'แท่ง', 'ซอง', 'กระป๋อง', 'องค์', 'รูป', 'มื้อ', 'คำ', 'หน', 'วง', 'คณะ', 'กลุ่ม', 'คัน',
                  'ชั่วโมง', 'นาที', 'วินาที', 'ทุ่ม', 'โมง', 'ขวบ', 'ปี', 'เดือน', 'สัปดาห์', 'วัน', 'คืน'}
TH_TIME_M = {'โมง', 'นาที', 'ทุ่ม', 'ตี', 'เที่ยง', 'ครึ่ง', 'บ่ายโมง', 'เที่ยงคืน', 'บ่าย', 'โมงเช้า', 'โมงเย็น'}
TH_NUM = {'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า', 'สิบ', 'ยี่สิบ', 'ร้อย', 'พัน', 'หมื่น',
          'แสน', 'ล้าน', 'สิบเอ็ด', 'สิบสอง', 'ยี่', 'เอ็ด', 'สิบห้า', 'สิบสาม', 'สิบสี่', 'สิบหก', 'สิบเจ็ด', 'สิบแปด',
          'สิบเก้า', 'สามสิบ', 'สี่สิบ', 'ห้าสิบ', 'หกสิบ', 'เจ็ดสิบ', 'แปดสิบ', 'เก้าสิบ', 'สองพัน', 'ห้าหมื่น', 'หมื่นห้า'}
POS_MAP = {'NOUN': 'n', 'PROPN': 'n', 'PRON': 'n', 'DET': 'n', 'VERB': 'v', 'ADJ': 'v', 'ADV': 'a', 'AUX': 'e',
           'NUM': 'm', 'ADP': 'p', 'CCONJ': 'p', 'SCONJ': None, 'PART': None, 'INTJ': 'a', 'PUNCT': None, 'SYM': None,
           'X': None}


def _thai_init():
    global _th_tok, _th_tok2, _th_lex
    if _th_tok is not None:
        return
    from pythainlp import word_tokenize
    from pythainlp.corpus import thai_words
    from pythainlp.util import dict_trie
    lex = {}
    for ko, th in _vocab_rows():
        c = _korean_vocab_class(ko)
        if ko.endswith('하다'):
            c = 'v'
        th = re.sub(r'\([^)]*\)', ' ', th)
        for alt in re.split(r'[·,/;]| หรือ ', th):
            alt = alt.strip(' .')
            if not alt or not THAI.search(alt) or len(alt) < 2:
                continue
            if alt not in TH_FUNC and alt not in TH_UNTAGGED:
                lex.setdefault(alt, c)
            for part in alt.split():
                if len(part) >= 2 and THAI.search(part) and part not in TH_FUNC and part not in TH_UNTAGGED:
                    lex.setdefault(part, c)
    words = set(thai_words()) | set(lex) | {k for k in TH_FUNC if ' ' not in k} | TH_UNTAGGED | TH_NUM | TH_CLASSIFIERS
    trie = dict_trie(words)
    _th_lex = lex
    _th_tok = lambda s: word_tokenize(s, engine='newmm', custom_dict=trie, keep_whitespace=True)
    small = dict_trie(set(lex) | {k for k in TH_FUNC if ' ' not in k} | TH_UNTAGGED | TH_NUM | TH_CLASSIFIERS)
    _th_tok2 = lambda s: word_tokenize(s, engine='newmm', custom_dict=small, keep_whitespace=False)


def _thai_pos(tokens):
    try:
        from pythainlp.tag import pos_tag
        return [p for _, p in pos_tag([t for t in tokens], corpus='orchid_ud')]
    except Exception:
        return [None] * len(tokens)


def _known(t):
    return t in TH_FUNC or t in TH_UNTAGGED or t in TH_NUM or t in TH_CLASSIFIERS or t in _th_lex


def _lookup(t):
    if t in TH_FUNC:
        return TH_FUNC[t]
    return _th_lex.get(t)


def _resegment(toks):
    """Split dictionary compounds the lexicon knows the parts of: ทำการบ้าน → ทำ + การบ้าน."""
    out = []
    for t in toks:
        if not t.strip() or _known(t) or not THAI.search(t) or len(t) < 4:
            out.append(t); continue
        parts = _th_tok2(t)
        if len(parts) > 1 and all(_known(p) for p in parts) and _lookup(parts[0]) in ('v', 'n', 'a', 'q', 'x'):
            out.extend(parts)                              # ทำการบ้าน → ทำ + การบ้าน
        elif len(parts) > 1 and _lookup(parts[0]) == 'v':
            out.append(('V', t))                           # นอนหลับ: verb head, unknown tail → whole = verb
        else:
            out.append(t)
    return out


def tag_thai(s, copy_class=None, ko=''):
    """Tag a Thai gloss. copy_class: a single class to apply to the whole text (vocabulary rows).
    ko: the tagged Korean the gloss translates — used to disambiguate ให้ (give vs. 한테)."""
    if '{' in s or not THAI.search(s):
        return s
    if copy_class:
        return f'{{{copy_class}:{s}}}'
    _thai_init()
    toks = _resegment(_th_tok(s))
    forced = {i: 'v' for i, t in enumerate(toks) if isinstance(t, tuple)}
    toks = [t[1] if isinstance(t, tuple) else t for t in toks]
    pos = _thai_pos(toks)
    has_dative = bool(re.search(r'\{[pP]:(한테|에게|께)\}', ko))
    has_give = bool(re.search(r'\{[vV]:(주|줬|줘|드리|드렸|드려|줍)', ko))
    n = len(toks)
    cls = [None] * n
    for i, t in enumerate(toks):
        if not t.strip():
            continue
        if HANGUL.search(t) or JAMO.search(t):
            cls[i] = 'K'
            continue
        if re.fullmatch(r'[0-9๐-๙][0-9๐-๙,.:]*', t):
            cls[i] = 'm'
            continue
        if not THAI.search(t) or len(t) == 1:
            cls[i] = None                                  # · — / ( ) Latin and stray single letters stay plain
            continue
        if i in forced:
            cls[i] = forced[i]
            continue
        if t in TH_UNTAGGED:
            cls[i] = None
            continue
        if t in TH_FUNC:
            cls[i] = TH_FUNC[t]
            continue
        if t in TH_NUM:
            cls[i] = 'm'
            continue
        if t in _th_lex:
            cls[i] = _th_lex[t]
            continue
        cls[i] = POS_MAP.get(pos[i]) if pos[i] else None
        if cls[i] is None and THAI.search(t) and len(t) >= 2:
            cls[i] = 'n'
    # context rules
    def prev_i(i):
        j = i - 1
        while j >= 0 and not toks[j].strip():
            j -= 1
        return j

    def next_i(i):
        j = i + 1
        while j < n and not toks[j].strip():
            j += 1
        return j if j < n else -1

    for i, t in enumerate(toks):
        pi, ni = prev_i(i), next_i(i)
        pc = cls[pi] if pi >= 0 else None
        nt = toks[ni] if ni >= 0 else ''
        nc = cls[ni] if ni >= 0 else None
        if t == 'ไม่' and nt in ('ใช่', 'มี', 'ได้', 'เคย', 'ค่อย', 'ชอบ'):
            cls[ni] = 'x'
        elif t == 'อยู่':
            cls[i] = 'e' if pc == 'v' else 'v'
        elif t == 'ให้':
            if has_give and pc != 'v':
                cls[i] = 'v'
            elif has_dative or pc == 'v':
                cls[i] = 'p'
            else:
                cls[i] = 'v'
        elif t == 'หา':
            cls[i] = 'p' if pc == 'v' else 'v'
        elif t == 'ละ':
            cls[i] = 'p' if (pi >= 0 and toks[pi] in TH_CLASSIFIERS) or pc == 'm' else None
            if cls[i] == 'p' and pi >= 0 and toks[pi] in TH_CLASSIFIERS:
                cls[pi] = 'm'
        elif t in ('บ่าย', 'ตี') and (nc == 'm' or nt in TH_TIME_M):
            cls[i] = 'm'
        elif t == 'ที่':
            cls[i] = 'm' if nc == 'm' else None if nc == 'v' else 'p'
        elif t == 'ได้':
            cls[i] = 'e' if pc == 'v' or nc == 'v' else 'v'
        elif t == 'กัน' and pc == 'v':
            cls[i] = 'a'
        elif t in TH_CLASSIFIERS and pc == 'm':
            cls[i] = 'm'
        elif t in TH_TIME_M and (pc == 'm' or nc == 'm'):
            cls[i] = 'm'
        elif t == 'เป็น' and nt in ('อย่างไร', 'ยังไง', 'ไง'):
            cls[i] = 'q'
        elif t in ('ไป', 'มา') and pc == 'v':
            cls[i] = None      # directional serial verb after another verb (กลับมา): keep plain
        elif t == 'ๆ':
            cls[i] = pc        # repetition mark takes the colour of the word it repeats
    # Korean tokens → Korean tagger; merge adjacent same-class tokens
    out, i = [], 0
    while i < n:
        c = cls[i]
        if c == 'K':
            out.append(tag_korean(toks[i]))
            i += 1
            continue
        j = i
        while j < n and (cls[j] == c or (not toks[j].strip() and j + 1 < n and cls[j + 1] == c and c)):
            j += 1
        seg = ''.join(toks[i:j])
        if c and seg.strip():
            lead = seg[:len(seg) - len(seg.lstrip())]
            trail = seg[len(seg.rstrip()):]
            out.append(f'{lead}{{{c}:{seg.strip()}}}{trail}')
        else:
            out.append(seg)
        i = j if j > i else i + 1
    return ''.join(out)


# ------------------------------------------------------------------ Markdown processing
GLOSS_RE = re.compile(r'\*\(((?:[^()*]|\([^()]*\))+?)\)\*')
GLOSS_SKIP = re.compile(r'^(เสริม|ตำรา|ดู ?(ข้อ|ส่วน|ไวยากรณ์|บท|หน้า|ตาราง)|ข้อ ?\d|หน้า ?\d|교과서|워크북|복습시험|매일시험|ไวยากรณ์ข้อ|ส่วนที่|'
                        r'บท ?\d|ยังไม่|ไม่พบ|ค้น|อ่านว่า|=|เหมือน|ไม่ใช่ ?[0-9]|ตามรูป|คำสั่ง|ครูกา|ครูเขียน|ครูแก้|ครูให้|เขียนผิด)')
PROTECT_RE = re.compile(r'(`[^`]*`|<[^>]+>|\{[a-zA-Z]:[^{}]*\}|\[[^\]]*\]\([^)]*\)|\[[^\]]*\]|\{\{[^}]*\}\}|https?://\S+)')
GLOSS_EXPLAIN = re.compile(r'รวมจาก|รอยแก้|กาลไม่ตรง|ห้าม|ต้องมี|ต้องใส่|ใส่ [가-힣]|คำนาม|คำกริยา|คำคุณศัพท์|คำชี้|ประโยค|รูป(แบบ|ทางการ|สุภาพ|พูด|ยกย่อง)|'
                           r'ตำรา|หมายถึง|แปลว่า|ไวยากรณ์|ข้อ ?\d|บท ?\d|หน้า ?\d|สังเกต|ระวัง|เทียบ|โจทย์|เฉลย|ตัวสะกด|สระ|พยางค์|'
                           r'ออกเสียง|อ่านว่า|ไม่ต้อง|เสริม|워크북|교과서|쪽|คะแนน|ข้อสอบ|ตอบว่า|ถามว่า|เติม|ช่อง|ตาราง|ละได้|'
                           r'ตัวหนา|สีเดียว|ความหมายว่า|แบบที่|กรณี|ใช้ได้|ใช้ไม่ได้|ผิด|ถูกต้อง|ลืม|เคยพลาด')
THAI_COL = re.compile(r'ไทย|ความหมาย|แปล')
READ_COL = re.compile(r'อ่าน|เสียง|ผัน|English|영어')


def _run_class_set(tagged):
    return {c.lower() for c, _ in TAG_RE.findall(tagged)}


def _tag_glosses_and_korean(text, in_table=False):
    """Tag the Korean runs and the Thai glosses of one text segment (no protected parts inside)."""
    parts, pos = [], 0
    for m in GLOSS_RE.finditer(text):
        before = text[pos:m.start()]
        parts.append(_tag_korean_runs(before, in_table))
        inner = m.group(1)
        prev_char = re.sub(r'[\s*_]+$', '', before)[-1:] if before.strip() else ''
        if ('{' in inner or GLOSS_SKIP.match(inner.strip()) or '→' in inner or '✗' in inner or '✓' in inner
                or GLOSS_EXPLAIN.search(inner) or (prev_char and THAI.match(prev_char))):
            parts.append(m.group(0))
        else:
            ko_ctx = parts[-1][-160:]
            head, sep, note = inner.partition(' — ')
            parts.append(f'*({tag_thai(head, ko=ko_ctx)}{sep}{note})*')
        pos = m.end()
    parts.append(_tag_korean_runs(text[pos:], in_table))
    return ''.join(parts)


def _tag_korean_runs(text, in_table=False):
    out, pos = [], 0
    for m in KO_RUN.finditer(text):
        if m.start() < pos:
            continue                      # Korean inside a gloss that was already consumed with its head word
        run = m.group(0)
        trail = re.search(r'[ 　.,?!~·/()\-\'"…:;%]*$', run).group(0)
        core = run[:len(run) - len(trail)] if trail else run
        if not (HANGUL.search(core) or JAMO.search(core)):
            continue
        out.append(text[pos:m.start()])
        glued = m.start() >= 3 and text[m.start() - 2:m.start()] == '**' and bool(HANGUL.search(text[m.start() - 3]))
        if core == '안' and re.match(r'^\*{0,2}에', text[m.end():]):
            tagged = '{n:안}'            # '옷장 **안**에' = position noun, not the negation 안
        else:
            tagged = tag_korean(core, glued=glued)
        rest = text[m.end():]
        # table cells: "만나다 (พบ)" → the parenthesised Thai takes the class of the Korean word
        if in_table:
            pm = re.match(r'^(\*\*)?\s*\(([ก-๙][^()]{0,40})\)', trail + rest)
            if pm and trail.strip() == '':
                classes = _run_class_set(tagged) - {'e'}
                cc = next(iter(classes)) if len(classes) == 1 else None
                thai = pm.group(2)
                tagged_thai = tag_thai(thai, cc) if cc else tag_thai(thai, ko=tagged)
                out.append(tagged + (pm.group(1) or '') + ' (' + tagged_thai + ')')
                pos = m.end() + (pm.end() - len(trail))
                continue
        out.append(tagged + trail)
        pos = m.end()
    out.append(text[pos:])
    return ''.join(out)


def _process_segment(text, in_table=False, thai_line=False):
    """Split out protected spans, tag the rest."""
    out, pos = [], 0
    for m in PROTECT_RE.finditer(text):
        chunk = text[pos:m.start()]
        out.append(tag_thai(chunk) if thai_line else _tag_glosses_and_korean(chunk, in_table))
        out.append(m.group(0))
        pos = m.end()
    chunk = text[pos:]
    out.append(tag_thai(chunk) if thai_line else _tag_glosses_and_korean(chunk, in_table))
    return ''.join(out)


def _split_cells(line):
    """Split a table row into cells, keeping '|' inside {tags} and code intact."""
    cells, buf, depth, code = [], [], 0, False
    for ch in line:
        if ch == '`':
            code = not code
        if ch == '{' and not code:
            depth += 1
        elif ch == '}' and not code and depth:
            depth -= 1
        if ch == '|' and not depth and not code:
            cells.append(''.join(buf))
            buf = []
        else:
            buf.append(ch)
    cells.append(''.join(buf))
    return cells


def colorize_markdown(text):
    lines = text.split('\n')
    out = []
    fence = False
    header_cells = None
    for idx, line in enumerate(lines):
        s = line.strip()
        if s.startswith('```'):
            fence = not fence
            out.append(line); continue
        if fence or s.startswith('#') or s == '[TOC]' or s.startswith('<') or s.startswith('!['):
            if not s.startswith('|'):
                header_cells = None
            out.append(line); continue
        if s.startswith('🇹🇭'):
            out.append(line[:line.index('🇹🇭') + len('🇹🇭')] + _process_segment(line[line.index('🇹🇭') + len('🇹🇭'):], thai_line=True))
            continue
        if s.startswith('|'):
            nxt = lines[idx + 1].strip() if idx + 1 < len(lines) else ''
            if re.fullmatch(r'\|[-:| ]+\|?', s):          # separator row
                out.append(line); continue
            if re.fullmatch(r'\|[-:| ]+\|?', nxt):        # header row
                header_cells = [c.strip() for c in _split_cells(s.strip('|'))]
                out.append(line); continue
            cells = _split_cells(line)
            # which columns are Thai-translation columns (by header)?
            th_cols = set()
            if header_cells:
                for ci, h in enumerate(header_cells):
                    if THAI_COL.search(h) and not READ_COL.search(h):
                        th_cols.add(ci + 1)                  # +1: cells[0] is the text before the first '|'
            new_cells = []
            ko_tagged = None
            for ci, cell in enumerate(cells):
                raw = cell.strip()
                if ci in th_cols and raw and THAI.search(raw) and not HANGUL.search(raw) and '{' not in raw and '*(' not in raw:
                    classes = (_run_class_set(ko_tagged) - {'e'}) if ko_tagged else set()
                    cc = next(iter(classes)) if len(classes) == 1 and len(raw) <= 40 and not re.search(r'[()·→+]', raw) else None
                    body = tag_thai(re.sub(r'\*\*', '', raw), cc) if cc else _process_segment(raw, in_table=True, thai_line=True)
                    new_cells.append(cell.replace(raw, body))
                    continue
                tagged = _process_segment(cell, in_table=True)
                if HANGUL.search(raw):
                    ko_tagged = tagged
                new_cells.append(tagged)
            out.append('|'.join(new_cells))
            continue
        header_cells = None
        out.append(_process_segment(line))
    return '\n'.join(out)


def braces_to_html(text):
    def repl(m):
        c, body = m.group(1), m.group(2)
        cls = f'k{c.lower()}' + (' kh' if c.isupper() else '')
        return f'<span class="{cls}">{body}</span>'
    return TAG_RE.sub(repl, text)


def strip_tags(text):
    return TAG_RE.sub(lambda m: m.group(2), text)


# ------------------------------------------------------------------ review batches
def extract_items(paths):
    """Yield (id, korean_tagged, thai_gloss) for every auto-tagged Thai gloss in the files."""
    for path in paths:
        with open(path, encoding='utf-8') as f:
            lines = f.read().split('\n')
        tagged = colorize_markdown('\n'.join(lines)).split('\n')
        for li, (orig, tl) in enumerate(zip(lines, tagged)):
            if orig == tl:
                continue
            k = 0
            for m in GLOSS_RE.finditer(tl):
                inner = m.group(1)
                if '{' not in inner:
                    continue
                before = tl[:m.start()]
                ko = re.findall(r'(?:\{[a-zA-Z]:[^{}]*\}|[가-힣ㄱ-ㅎㅏ-ㅣ0-9 .,?!~·/()\-]|\*\*)+$', before.rstrip())
                ko = (ko[0] if ko else '').strip(' *')
                yield f'{os.path.relpath(path, ROOT)}:{li + 1}:{k}', ko, inner
                k += 1


def resolve_targets(lines):
    """For every line: list of (gloss match in the ORIGINAL line) in the order extract_items numbered them
    (= the glosses that the auto-tagger tagged, k-th tagged gloss of the tagged line)."""
    tagged_lines = colorize_markdown('\n'.join(lines)).split('\n')
    targets = {}
    for i, (orig, tl) in enumerate(zip(lines, tagged_lines)):
        if orig == tl:
            continue
        ms_o = list(GLOSS_RE.finditer(orig))
        ms_t = list(GLOSS_RE.finditer(tl))
        if len(ms_o) != len(ms_t):
            continue
        targets[i + 1] = [ms_o[j] for j, m in enumerate(ms_t) if '{' in m.group(1)]
    return targets


def _same_text(a, b):
    return re.sub(r'\s+', '', strip_tags(a)) == re.sub(r'\s+', '', strip_tags(b))


def merge_fixes(fixes, dry_run=False):
    """fixes: {rel: {(line, k): new_gloss}} → write explicit tags into the source files."""
    from collections import defaultdict
    written = skipped = 0
    for rel, items in fixes.items():
        path = os.path.join(ROOT, rel)
        with open(path, encoding='utf-8') as f:
            lines = f.read().split('\n')
        targets = resolve_targets(lines)
        by_line = defaultdict(dict)
        for (ln, k), new in items.items():
            by_line[ln][k] = new
        for ln, ks in by_line.items():
            line = lines[ln - 1]
            ms = targets.get(ln, [])
            for k in sorted(ks, reverse=True):                 # replace from the right so offsets stay valid
                new = ks[k]
                well_formed = re.fullmatch(r'(?:[^{}]|\{[a-zA-Z]:[^{}]*\})*', new) is not None
                if k < len(ms) and well_formed and _same_text(new, ms[k].group(1)):
                    m = ms[k]
                    line = line[:m.start()] + f'*({new})*' + line[m.end():]
                    written += 1
                else:
                    skipped += 1
                    print(f'skip {rel}:{ln}:{k}', file=sys.stderr)
            lines[ln - 1] = line
        if not dry_run:
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
    return written, skipped


def load_fixes(paths):
    from collections import defaultdict
    fixes = defaultdict(dict)
    for p in paths:
        with open(p, encoding='utf-8') as f:
            for line in f:
                parts = line.rstrip('\n').split('\t')
                if len(parts) >= 2 and ':' in parts[0]:
                    rel, ln, k = parts[0].rsplit(':', 2)
                    fixes[rel][(int(ln), int(k))] = parts[-1]
    return fixes


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'tag'
    if cmd == 'tag':
        print(colorize_markdown(' '.join(sys.argv[2:])))
    elif cmd == 'thdebug':
        _thai_init()
        for s_ in sys.argv[2:]:
            toks = _resegment(_th_tok(s_))
            print([(t, _th_lex.get(t), TH_FUNC.get(t), p) for t, p in zip(toks, _thai_pos(toks)) if t.strip()])
            print(tag_thai(s_))
    elif cmd == 'check':
        for p in sys.argv[2:]:
            with open(p, encoding='utf-8') as f:
                src = f.read()
            for a, b in zip(src.split('\n'), colorize_markdown(src).split('\n')):
                if a != b:
                    print(b)
    elif cmd == 'extract':
        for item in extract_items(sys.argv[2:]):
            print('\t'.join(item))
    elif cmd in ('merge', 'merge-dry'):
        written, skipped = merge_fixes(load_fixes(sys.argv[2:]), dry_run=(cmd == 'merge-dry'))
        print(f'{cmd}: {written} glosses written, {skipped} skipped')
