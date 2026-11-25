# BRIEF — put each vocabulary word into one meaning category (By-Topic book, ส่วนที่ 4 · 📂 คำศัพท์แยกหมวด)

The By-Topic guide prints the whole course vocabulary (5–37과, 1,366 words) grouped by meaning. `scripts/vocab_categories.py`
builds that section from `content/guide/04_vocabulary/91_categories.tsv`, which gives every word one category id and, for
verbs/adjectives, its polite present form (-아/어요). Your job: produce those TSV rows for a batch of words.

## Input
A TSV file, one word per line: `ko <TAB> unit <TAB> Thai gloss <TAB> English gloss`. Do not read any other file.

## Output
A TSV file, **exactly one line per input line, same order**, three tab-separated columns:

```
ko<TAB>category_id<TAB>해요-form
```

- `ko` copied byte-for-byte from the input (spaces, brackets and all).
- `category_id` = one id from the table below. Decide the **word class first** (noun / verb / adjective / other), then the topic.
- `해요-form` = the -아/어요 polite present form, **only** when the category is a verb (`v_*`) or adjective (`a_*`) id;
  otherwise leave the third column empty (the line still ends with a tab). For a phrase, conjugate only the last word and keep
  the rest unchanged: `감기에 걸리다 → 감기에 걸려요`, `길이 막히다 → 길이 막혀요`. Mind the irregulars: ㅂ (덥다 → 더워요, 돕다 → 도와요,
  but 입다 → 입어요, 좁다 → 좁아요), ㄷ (듣다 → 들어요, but 닫다 → 닫아요, 받다 → 받아요), 르 (부르다 → 불러요, 모르다 → 몰라요), ㅡ (쓰다 → 써요,
  바쁘다 → 바빠요), ㅎ (빨갛다 → 빨개요, 어떻다 → 어때요), ㅅ (낫다 → 나아요). 있다/없다 compounds: 재미있다 → 재미있어요.
- A Korean word ending in 다 is not always a verb: 바다 (sea) is a noun, 다 (all) is an adverb, 감사합니다 is a set expression (`expr`).
- 하다-verbs vs their nouns: 운동 = noun (`hobby`), 운동하다 = verb (`v_free`).
- Homonym lines (gloss lists several meanings, e.g. 쓰다 · 배 · 개 · 반 · 일): categorise by the **first** meaning.

## Category ids

| id | word class | covers | examples |
|:---|:---|:---|:---|
| country | noun | countries, cities, languages, nationalities | 한국 · 서울 · 한국어 · 외국인 |
| people | noun | people, family, relationships, pronoun-like people nouns | 친구 · 어머니 · 손님 · 분 · 남자 |
| job | noun | occupations and positions | 의사 · 회사원 · 가수 |
| place | noun | places, buildings, shops, institutions (not rooms of a home) | 학교 · 은행 · 공원 · 백화점 · 경찰서 |
| home | noun | rooms, furniture, home appliances, things fixed in a house | 방 · 침대 · 냉장고 · 창문 · 부엌 |
| things | noun | portable objects, clothes, shoes, accessories, stationery | 가방 · 시계 · 옷 · 우산 · 연필 |
| food | noun | dishes, drinks, fruit, ingredients, taste nouns | 김치찌개 · 커피 · 사과 · 맛 |
| travel | noun | vehicles, roads, directions, position words, travel nouns | 버스 · 사거리 · 왼쪽 · 출구 · 위 · 앞 |
| nature | noun | nature, animals, plants, weather, seasons | 산 · 바다 · 고양이 · 날씨 · 봄 · 비 |
| time | noun | time nouns: days, months, parts of the day, 지난/다음 phrases | 어제 · 주말 · 아침 · 작년 · 방학 기간 |
| number | noun | numbers, counters, units, amounts | 하나 · 개 · 원 · 층 · 번 · 시간 |
| color | noun | colours and shapes | 빨간색 · 색깔 |
| hobby | noun | sports, hobbies, music, films, entertainment | 축구 · 영화 · 노래 · 여행 · 취미 |
| study | noun | school, class, homework, exams, learning | 수업 · 숙제 · 시험 · 단어 · 문법 |
| body | noun | body parts, illness, medicine, health | 머리 · 감기 · 약 · 병 |
| money | noun | work, money, prices, buying/selling, services, receipts | 회사 · 돈 · 가격 · 영수증 · 주문 |
| event | noun | events, festivals, holidays, parties, appointments | 생일 · 파티 · 약속 · 휴가 · 축제 |
| comm | noun | phone, mail, internet, photos, media | 전화 · 이메일 · 사진 · 편지 |
| abstract | noun | any other noun (abstract: thought, reason, experience, feeling) | 생각 · 이유 · 경험 · 기분 · 이름 |
| v_daily | verb | daily life: eat, sleep, wash, dress, cook, clean, live | 먹다 · 자다 · 씻다 · 입다 · 청소하다 |
| v_move | verb | moving, going, riding, getting off, crossing, travelling, moving house | 가다 · 타다 · 내리다 · 걷다 · 건너다 · 이사하다 |
| v_mind | verb | speaking, listening, reading, writing, studying, knowing, thinking, liking, feelings | 말하다 · 듣다 · 알다 · 모르다 · 좋아하다 · 외우다 |
| v_free | verb | free time: sports, hobbies, playing, resting, sightseeing | 운동하다 · 치다 · 놀다 · 쉬다 · 구경하다 |
| v_act | verb | any other verb: work, give, buy/sell, make, use, open/close, switch on/off | 사다 · 주다 · 만들다 · 켜다 · 일하다 |
| a_quality | adjective | qualities of things, places, tasks: size, price, distance, difficulty, fun, cleanliness | 크다 · 비싸다 · 멀다 · 어렵다 · 재미있다 |
| a_person | adjective | a person's feelings, personality, physical state | 기쁘다 · 친절하다 · 바쁘다 · 피곤하다 · 아프다 |
| a_sense | adjective | taste and weather | 맵다 · 달다 · 느끼하다 · 덥다 · 시원하다 |
| adv | other | adverbs (frequency, degree, manner) | 자주 · 너무 · 빨리 · 같이 · 다 |
| conj | other | sentence connectors | 그리고 · 그렇지만 · 그래서 · 그런데 |
| pron | other | question words, demonstratives, pronouns | 뭐 · 어디 · 이것 · 저 · 우리 · 무슨 |
| expr | other | set phrases and greetings used as a whole | 안녕하세요 · 감사합니다 · 실례합니다 |
| instr | other | words from exam instructions (보기, 고르다, 완성하다 …) — nouns get no 해요-form; verbs here may have one | 보기 · 고르다 · 대화 |

## Check before you finish
Run this (replace the two paths) and fix every ✗ line; ⚠️ lines are -아/어요 forms the rules did not predict — double-check
each one and keep it only if you are sure it is right:

```bash
cd /home/beamkeerati/Documents/KMU_Korean && python3 - IN.tsv OUT.tsv <<'EOF'
import sys; sys.path.insert(0, 'scripts')
from vocab_categories import CAT, haeyo_forms
inp = [l.split('\t')[0] for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
out = [l.rstrip('\n').split('\t') for l in open(sys.argv[2], encoding='utf-8') if l.strip()]
if [o[0] for o in out] != inp: print('✗ ko column differs from the input (order/spelling/count)', len(inp), len(out))
for o in out:
    if len(o) != 3: print('✗ not 3 columns:', o); continue
    ko, cat, hy = o
    if cat not in CAT: print('✗ unknown id:', o); continue
    fam = CAT[cat][1]
    if fam in ('verb', 'adj') and not hy: print('✗ verb/adj without 해요-form:', ko)
    if fam not in ('verb', 'adj') and hy and cat != 'instr': print('✗ 해요-form on a non-verb:', ko)
    if hy and ko.split()[-1].endswith('다') and hy.split()[-1] not in haeyo_forms(ko.split()[-1]): print('⚠️', ko, '→', hy)
print('checked', len(out))
EOF
```

Do not edit any repo file, do not run build scripts, do not publish. Report: the count per category id and every ⚠️ you kept.
