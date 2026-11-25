#!/usr/bin/env python3
"""Vocabulary by meaning category for the By-Topic guide (ส่วนที่ 4 · 📂 คำศัพท์แยกหมวด), 5–37과 complete.

Words come from content/guide/04_vocabulary/examples/unitNN.json: the full course list, one entry per spelling, with the
audited Thai gloss. Each word's category (+ its -아/어요 form when it is a verb/adjective) is in
content/guide/04_vocabulary/91_categories.tsv: `ko <TAB> cat <TAB> 해요-form`, lines starting `#` are comments.
build.py calls render(). Run `python3 scripts/vocab_categories.py --check` after adding a word to 04_vocabulary/unitNN.md
(+ its examples entry): it lists words without a category, stale rows, unknown ids, verbs/adjectives without a -아/어요 form
and -아/어요 forms that the conjugation rules below cannot produce (warnings — check them by hand).
Brief for categorising a batch of words: specs/BRIEF_vocab_categories.md.
"""
import glob
import json
import os
import re
import sys

from kmu_paths import REPO, ROOT   # ROOT = levels/<N>/ (source/ content/ output/ extracted/) · REPO = repo root (scripts/ specs/ tools/)
VOCAB = os.path.join(ROOT, 'content', 'guide', '04_vocabulary')
MAP = os.path.join(VOCAB, '91_categories.tsv')

# (id, family, heading, lead sentence) — family: noun / verb / adj / other; the book prints them in this order.
CATS = [
    ('country', 'noun', '🌍 ประเทศ · เมือง · ภาษา', 'ชื่อประเทศ เมือง และภาษา ใช้ตอบคำถาม 어느 나라 사람이에요? และเล่าเรื่องการเดินทาง'),
    ('people', 'noun', '👨‍👩‍👧 คน · ครอบครัว', 'คำเรียกคนและสมาชิกครอบครัว คำสุภาพอย่าง 분 และ 부모님 ใช้คู่กับกริยารูปยกย่อง -(으)시-'),
    ('job', 'noun', '💼 อาชีพ', 'ชื่ออาชีพและตำแหน่ง ใช้แนะนำตัวด้วย N이에요/예요'),
    ('place', 'noun', '🏢 สถานที่ · อาคาร · ร้าน', 'สถานที่ที่ไปทำกิจกรรม ใช้กับ 에 가다 และ 에서 + กริยา'),
    ('home', 'noun', '🏠 บ้าน · ห้อง · ของในบ้าน', 'ห้อง เฟอร์นิเจอร์ และเครื่องใช้ในบ้าน ใช้กับ 에 있어요 และคำบอกตำแหน่ง'),
    ('things', 'noun', '🎒 ของใช้ · เสื้อผ้า · เครื่องเขียน', 'ของติดตัว เสื้อผ้า และเครื่องเขียน ใช้ตอนซื้อของและบอกว่าใส่อะไร'),
    ('food', 'noun', '🍎 อาหาร · เครื่องดื่ม · ผลไม้', 'ชื่ออาหาร เครื่องดื่ม ผลไม้ และวัตถุดิบ ใช้สั่งอาหารและเล่าเรื่องรสชาติ'),
    ('travel', 'noun', '🚌 การเดินทาง · ทิศทาง · ตำแหน่ง', 'ยานพาหนะ ทิศทาง และคำบอกตำแหน่ง ใช้บอกทางด้วย (으)로 가세요 และบอกที่ตั้งด้วย 에 있어요'),
    ('nature', 'noun', '🌳 ธรรมชาติ · สัตว์ · อากาศ · ฤดู', 'ธรรมชาติ สัตว์ อากาศ และฤดูกาล ใช้เล่าเรื่องสถานที่ท่องเที่ยวและสภาพอากาศ'),
    ('time', 'noun', '⏰ เวลา · วัน · เดือน', 'คำนามบอกเวลา คำเหล่านี้ช่วยเลือกกาลของประโยค (어제 → อดีต · 내일 → -(으)ㄹ 거예요)'),
    ('number', 'noun', '🔢 ตัวเลข · ลักษณนาม · หน่วย', 'ตัวเลข ลักษณนาม และหน่วย ลักษณนามตามหลังตัวเลขเสมอ (사과 두 개)'),
    ('color', 'noun', '🎨 สี · รูปร่าง', 'ชื่อสีและรูปร่าง ใช้บรรยายสิ่งของและเสื้อผ้า'),
    ('hobby', 'noun', '⚽ งานอดิเรก · กีฬา · ความบันเทิง', 'ชื่อกีฬา งานอดิเรก และความบันเทิง กีฬาบางชนิดใช้ 하다 บางชนิดใช้ 타다 หรือ 치다'),
    ('study', 'noun', '📚 การเรียน · โรงเรียน', 'คำเกี่ยวกับห้องเรียน การบ้าน และการสอบ'),
    ('body', 'noun', '🏥 ร่างกาย · สุขภาพ', 'อวัยวะ อาการป่วย และการรักษา ใช้กับ 이/가 아프다'),
    ('money', 'noun', '💳 งาน · เงิน · การซื้อขาย', 'คำเกี่ยวกับการทำงาน เงิน ราคา และการซื้อขายหรือบริการ'),
    ('event', 'noun', '🎉 กิจกรรม · วันพิเศษ · การนัดหมาย', 'งาน เทศกาล วันหยุด และการนัดหมาย ใช้เล่าแผนและประสบการณ์'),
    ('comm', 'noun', '📱 การสื่อสาร · สื่อ · เทคโนโลยี', 'โทรศัพท์ จดหมาย อินเทอร์เน็ต รูปถ่าย และสื่อต่าง ๆ'),
    ('abstract', 'noun', '🗂️ คำนามอื่น ๆ', 'คำนามนามธรรมที่ไม่เข้าหมวดใด เช่น ความคิด เหตุผล และประสบการณ์'),
    ('v_daily', 'verb', '🛏️ กริยา · ชีวิตประจำวัน', 'กริยาที่ทำทุกวัน เช่น กิน นอน ล้าง แต่งตัว และทำงานบ้าน'),
    ('v_move', 'verb', '🚶 กริยา · การเคลื่อนที่ · เดินทาง', 'กริยาการเคลื่อนที่ ใช้ 에/(으)로 บอกปลายทาง และ 에서 บอกจุดเริ่มต้น'),
    ('v_mind', 'verb', '💬 กริยา · พูด · เรียน · คิด · รู้สึก', 'กริยาเกี่ยวกับภาษา การเรียน ความรู้ และความรู้สึก กริยาเหล่านี้รับกรรมด้วย 을/를'),
    ('v_free', 'verb', '🎳 กริยา · งานอดิเรก · กีฬา · พักผ่อน', 'กริยาเวลาว่าง ระวังคู่ 하다 / 타다 / 치다 (수영을 하다 · 자전거를 타다 · 테니스를 치다)'),
    ('v_act', 'verb', '🛠️ กริยา · ทำงาน · ให้ · ซื้อขาย · ใช้สิ่งของ', 'กริยาที่ทำกับสิ่งของหรือคนอื่น เช่น ซื้อ ขาย ให้ เปิด ปิด และสร้าง'),
    ('a_quality', 'adj', '📏 คุณศัพท์ · ลักษณะของสิ่งของ สถานที่ งาน', 'คุณศัพท์บรรยายสิ่งของ สถานที่ และงาน เวลาขยายคำนามใช้ -(으)ㄴ (큰 가방 · 작은 방) ไม่ใช่ -는'),
    ('a_person', 'adj', '😊 คุณศัพท์ · ความรู้สึก · นิสัย · สภาพร่างกาย', 'คุณศัพท์บอกความรู้สึก นิสัย และสภาพร่างกายของคน'),
    ('a_sense', 'adj', '🌶️ คุณศัพท์ · รสชาติ · อากาศ', 'คุณศัพท์บอกรสชาติและอากาศ หลายคำเป็น ㅂ ไม่ปกติ (맵다 → 매워요 · 덥다 → 더워요)'),
    ('adv', 'other', '✨ คำวิเศษณ์', 'คำขยายกริยาและคุณศัพท์ บอกความถี่ ระดับ และวิธีทำ'),
    ('conj', 'other', '🔗 คำเชื่อมประโยค', 'คำขึ้นต้นประโยคที่เชื่อมกับประโยคก่อนหน้า'),
    ('pron', 'other', '❓ คำถาม · คำชี้ · สรรพนาม', 'คำแสดงคำถาม คำชี้ และสรรพนาม'),
    ('expr', 'other', '🗣️ สำนวน · คำทักทาย · ประโยคสำเร็จรูป', 'ประโยคที่ใช้ทั้งก้อน จำเป็นวลีได้เลยไม่ต้องผัน'),
    ('instr', 'other', '📝 คำในคำสั่งโจทย์', 'คำที่พบในคำสั่งของข้อสอบ อ่านคำสั่งออกก่อนจึงจะตอบถูก'),
]
CAT = {c[0]: c for c in CATS}


def load_words():
    """[(unit, ko, th)] in course order (the examples JSON lists each spelling once, first unit wins)."""
    out = []
    for f in sorted(glob.glob(os.path.join(VOCAB, 'examples', 'unit*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        out += [(d['unit'], w['ko'], w['th']) for w in d['words']]
    return out


def load_map():
    m = {}
    if os.path.exists(MAP):
        for n, ln in enumerate(open(MAP, encoding='utf-8'), 1):
            if not ln.strip() or ln.startswith('#'):
                continue
            p = ln.rstrip('\n').split('\t') + ['']
            m[p[0].strip()] = (p[1].strip(), p[2].strip(), n)
    return m


# ---- -아/어요 conjugation rules (only used to flag forms for a human check) ----
def _dec(ch):
    c = ord(ch) - 0xAC00
    return (c // 588, (c % 588) // 28, c % 28) if 0 <= c < 11172 else None


def _comp(cho, jung, jong=0):
    return chr(0xAC00 + cho * 588 + jung * 28 + jong)


A, YA, EO, YEO, O, U, EU, I, AE, E, OE = 0, 2, 4, 6, 8, 13, 18, 20, 1, 5, 11
J_B, J_D, J_S, J_H, J_L = 17, 7, 19, 27, 8


def haeyo_forms(word):
    """Every -아/어요 form the rules allow for a dictionary form ending in 다 (irregular readings included)."""
    if word in ('이다',):
        return {'이에요', '예요'}
    if word.endswith('아니다'):
        return {word[:-3] + '아니에요'}
    if word == '갖다':                        # short for 가지다
        return {'가져요'}
    if word.endswith('시다'):                 # honorific verbs: 계시다 → 계세요 · 드시다 → 드세요
        return {word[:-2] + '세요', word[:-2] + '셔요'}
    st = word[:-1]
    if not st or not word.endswith('다'):
        return set()
    if st.endswith('하'):
        return {st[:-1] + '해요'}
    head, last = st[:-1], st[-1]
    d = _dec(last)
    if d is None:
        return set()
    cho, jung, jong = d
    bright = jung in (A, YA, O)
    out = set()
    if jong:
        out.add(st + ('아요' if bright else '어요'))
        base = _comp(cho, jung)
        if jong == J_B:
            out.add(head + base + ('와요' if base in '도고' else '워요'))
        if jong == J_D:
            out.add(head + _comp(cho, jung, J_L) + ('아요' if bright else '어요'))
        if jong == J_S:
            out.add(head + base + ('아요' if bright else '어요'))
        if jong == J_H:                       # 빨갛다 → 빨개요 · 그렇다 → 그래요 · 하얗다 → 하얘요
            out.add(head + _comp(cho, {A: AE, EO: AE, YA: 3}.get(jung, jung)) + '요')
        return out
    if jung == EU:                            # ㅡ drop, or 르 irregular
        prev = _dec(head[-1]) if head else None
        pb = prev is not None and prev[1] in (A, YA, O)
        if prev is None:
            out.add(_comp(cho, EO) + '요')
        else:
            out.add(head + _comp(cho, A if pb else EO) + '요')
            if last == '르':
                out.add(head[:-1] + _comp(prev[0], prev[1], J_L) + ('라요' if pb else '러요'))
        return out
    merge = {A: A, EO: EO, YEO: YEO, AE: AE, E: E, O: 9, U: 14, I: YEO, OE: 10}
    if jung in merge:
        out.add(head + _comp(cho, merge[jung]) + '요')
    if jung in (AE, OE, 16, 19):              # 내어요 / 되어요 / 쉬어요 / 띄어요 also exist
        out.add(st + '어요')
    return out


def check(verbose=True):
    words, m = load_words(), load_map()
    known = {ko for _, ko, _ in words}
    hard, soft = [], []
    for u, ko, th in words:
        if ko not in m:
            hard.append(f'no category: {ko} ({u}과 · {th})')
            continue
        cat, hy, n = m[ko]
        if cat not in CAT:
            hard.append(f'91_categories.tsv:{n}: unknown category "{cat}" for {ko}')
            continue
        fam = CAT[cat][1]
        if fam in ('verb', 'adj') and not hy:
            hard.append(f'91_categories.tsv:{n}: {ko} is a {fam} but has no -아/어요 form')
        if hy:
            hy = re.sub(r'\{[A-Za-z]:([^}]*)\}', r'\1', hy)      # explicit colour tags ({v:셔}{e:요}) are allowed
            last_ko, last_hy = ko.split()[-1], hy.split()[-1]
            if ko.split()[:-1] != hy.split()[:-1]:
                soft.append(f'91_categories.tsv:{n}: {ko} → {hy}: the words before the verb differ')
            elif last_ko.endswith('다') and last_hy not in haeyo_forms(last_ko):
                soft.append(f'91_categories.tsv:{n}: {ko} → {hy}: rules give {" / ".join(sorted(haeyo_forms(last_ko))) or "nothing"}')
    for ko, (cat, hy, n) in m.items():
        if ko not in known:
            hard.append(f'91_categories.tsv:{n}: {ko} is not in any examples/unitNN.json (stale row)')
    if verbose:
        for s in hard:
            print('✗', s)
        for s in soft:
            print('⚠️', s)
        print(f'{len(words)} words · {len(m)} map rows · {len(hard)} problems · {len(soft)} warnings')
    return not hard


def _cell(s):
    return s.replace('|', '/').strip()


def render():
    """Markdown for the By-Topic book: one ### section per category, words in course order."""
    words, m = load_words(), load_map()
    by = {c[0]: [] for c in CATS}
    missing = []
    for u, ko, th in words:
        cat = m.get(ko, ('', '', 0))[0]
        if cat in by:
            by[cat].append((u, ko, th, m[ko][1]))
        else:
            missing.append((u, ko, th, ''))
    out = []
    sections = [(c, by[c[0]]) for c in CATS] + ([(('?', 'other', '❔ ยังไม่ได้จัดหมวด', 'คำใหม่ที่ยังไม่ได้ใส่หมวดใน 91_categories.tsv'), missing)]
                                                 if missing else [])
    for (cid, fam, title, lead), ws in sections:
        if not ws:
            continue
        out += [f'### {title}', '', f'{lead} หมวดนี้มี {len(ws)} คำ', '']
        if any(w[3] for w in ws):
            out += ['| 한국어 | -아/어요 | ไทย |', '|:---|:---|:---|']
            out += [f'| {_cell(ko)} *({u}과)* | {_cell(hy) or "—"} | {_cell(th)} |' for u, ko, th, hy in ws]
        else:
            half = (len(ws) + 1) // 2
            left, right = ws[:half], ws[half:] + [None] * (half - len(ws[half:]))
            out += ['| 한국어 | ไทย | 한국어 | ไทย |', '|:---|:---|:---|:---|']
            for a, b in zip(left, right):
                cells = [f'{_cell(a[1])} *({a[0]}과)*', _cell(a[2])]
                cells += [f'{_cell(b[1])} *({b[0]}과)*', _cell(b[2])] if b else ['', '']
                out.append('| ' + ' | '.join(cells) + ' |')
        out.append('')
    return '\n'.join(out).strip()


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(0 if check() else 1)
    print(render())
