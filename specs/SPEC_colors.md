# SPEC_colors — colour-by-function tags (Korean ↔ Thai)

Every Korean sentence in the PDFs is coloured by the **function** of each segment, and the Thai gloss that follows
it (`*(…)*`, a 🇹🇭 line, or a ไทย column) is coloured with the **same classes**, so the reader sees which Thai word
renders which Korean part. Tags are written inline in the Markdown as `{c:text}` and rendered by
`scripts/kotag.py` + `scripts/make_pdf.py`. Korean is tagged automatically at build time; Thai glosses get an
automatic first pass that human/agent review corrects by writing explicit tags into `content/*.md`.

## 1. Classes (one letter)

| tag | class | Korean examples | Thai examples | colour |
|:---|:---|:---|:---|:---|
| `n` | noun · pronoun · demonstrative | 학생 저 학교 이것 이/그/저 책 | นักเรียน ฉัน โรงเรียน นี่ หนังสือ ชื่อคน | blue |
| `p` | particle 조사 and its Thai counterpart | 은/는 이/가 을/를 에 에서 도 만 하고 와/과 한테 한테서 부터 까지 의 | ที่ ใน กับ และ ก็ ด้วย แค่ จาก ถึง ตั้งแต่ ของ ตอน | orange on pale orange |
| `v` | verb / adjective stem | 가 먹 예쁘 공부하(해) 있 | ไป กิน สวย เรียน มี อยู่(=있다) | green |
| `e` | ending · tense · aspect · copula 이다 | 요 어요 이에요 입니다 았어요 ㄹ 거예요 고 있어요 세요(E) 다 | เป็น คือ แล้ว จะ กำลัง เคย ได้(past/able) อยู่(progressive) | purple |
| `q` | question word | 누가 누구 뭐 무엇 어디 언제 왜 몇 얼마 어느 무슨 어떤 어때요 | ใคร อะไร ที่ไหน เมื่อไร ทำไม กี่ เท่าไร ไหน แบบไหน เป็นอย่างไร | teal |
| `x` | negation incl. the negated predicate | 안 못 지 않아요 아니에요 없어요 아니요 마세요 | ไม่ ไม่ใช่ ไม่มี ไม่ได้ อย่า ห้าม | red |
| `m` | number · counter · clock/date unit | 세 개 두 명 9시 30분 55,000원 시월 삼 층 | สามลูก สองคน เก้าโมง 55,000 วอน ชั้นสาม วันที่ 17 | brown |
| `a` | adverb · time word that takes no 에 | 아주 정말 잘 같이 혼자 오늘 어제 내일 지금 매일 요즘 네 | มาก จริง ๆ เก่ง ด้วยกัน คนเดียว วันนี้ เมื่อวาน ตอนนี้ ทุกวัน ใช่ | grey |
| `N P V E` | **uppercase = honorific** form of that class (dotted underline) | 분 님 께서 께 드리 주무 계 세요 십니다 셨어요 | ท่าน คุณ(ปู่) มอบ รับประทาน บรรทม | same colour + dotted underline |

Untagged (plain) = Thai words with no Korean counterpart: ค่ะ ครับ คะ นะ สิ เลย ล่ะ หรือ เหรอ ไหม มั้ย กัน (reciprocal), and
any explanatory remark inside a gloss ("— ให้เหตุผล", "(กาลไม่ตรงคำถาม)").

## 2. The one rule

**A Thai word is tagged with the class of the Korean segment it translates.** Look at the tagged Korean first,
then give each Thai word the same letter. Word order differs (Korean SOV, Thai SVO) — that is exactly what the
colours are for.

| Korean (tagged) | Thai (tagged) |
|:---|:---|
| `{n:저}{p:는} {n:학생}{e:이에요}` | `{n:ฉัน}{e:เป็น}{n:นักเรียน}` |
| `{n:학생}{p:이} {x:아니에요}` | `{x:ไม่ใช่}{n:นักเรียน}` |
| `{n:학교}{p:에서} {n:공부}{v:해}{e:요}` | `{v:เรียน}{p:ที่}{n:โรงเรียน}` |
| `{n:방학}{p:에} {n:태국}{p:에} {v:갈} {e:거예요}` | `{p:ตอน}{n:ปิดเทอม}{e:จะ}{v:ไป}{n:ประเทศไทย}` |
| `{a:어제} {n:친구}{p:하고} {n:영화}{p:를} {x:안} {v:봤}{e:어요}` | `{a:เมื่อวาน}{x:ไม่ได้}{v:ดู}{n:หนัง}{p:กับ}{n:เพื่อน}` |
| `{q:누가} {n:요리}{p:를} {a:잘}{v:해}{e:요}?` | `{q:ใคร}{v:ทำ}{n:อาหาร}{a:เก่ง}` |
| `{n:어머니}{P:께서} {n:신문}{p:을} {v:읽}{E:으세요}` | `{n:คุณแม่}{v:อ่าน}{n:หนังสือพิมพ์}` (no Thai honorific word → nothing uppercase) |
| `{n:할머니}{P:께} {n:선물}{p:을} {V:드렸}{e:어요}` | `{V:มอบ}{n:ของขวัญ}{p:ให้}{n:คุณยาย}` |
| `{n:치마}{p:는} {m:한} {m:벌}{p:에} {m:55,000원}{e:이에요}` | `{n:กระโปรง}{m:ตัว}{p:ละ} {m:55,000 วอน}` |
| `{a:지금} {q:몇} {m:시}{e:예요}?` | `{a:ตอนนี้}{q:กี่โมง}` |
| `{n:밥}{p:을} {v:먹}{e:고} {e:있어요}` | `{e:กำลัง}{v:กิน}{n:ข้าว}` |
| `{n:시간}{p:이} {x:없어요}` | `{x:ไม่มี}{n:เวลา}` |
| `{a:네}, {v:가}{e:요}` | `{a:ค่ะ} {v:ไป}` or `{a:ใช่} {v:ไป}` |

## 3. Ambiguous Thai words — decide from the Korean

| Thai | tag | when |
|:---|:---|:---|
| ให้ | `v` | translates 주다/드리다 (give) — `{v:ให้}{n:เพื่อน}` for 친구한테 줬어요 |
| ให้ / แก่ | `p` | translates 한테/에게/께 after another verb — 친구한테 전화해요 → `{v:โทร}{p:หา}{n:เพื่อน}`, 선생님께 말해요 → `{v:พูด}{p:กับ}{N:อาจารย์}` |
| ที่ | `p` | place 에/에서 (`{p:ที่}{n:โรงเรียน}`) |
| ที่ | `m` | วันที่ + number (`{m:วันที่ 17}`) |
| ที่ | plain | relative "that/which" (คนที่…) |
| อยู่ | `v` | 있다/있어요 (be located) — `{v:อยู่}{p:ที่}{n:บ้าน}` |
| อยู่ | `e` | progressive 고 있어요 — `{e:กำลัง}{v:อ่าน}{e:อยู่}` |
| มี | `v` | 있어요 (have) · `{x:ไม่มี}` for 없어요 |
| ได้ | `e` | past/ability marker (ได้ไป, ไปได้) · `v` inside ได้รับ (받다) · `{x:ไม่ได้}` for 안/못 + past |
| ไม่ | `x` | always; merge with the next word only when the Korean is one red unit (아니에요 → ไม่ใช่, 없어요 → ไม่มี/ไม่อยู่); when the Korean is 안 + green verb keep them apart: `{x:ไม่}{v:ไป}` |
| ก็ / ด้วย | `p` | 도 ("also") · `{a:ด้วยกัน}` = 같이 |
| แค่ / เท่านั้น | `p` | 만 |
| กับ / และ | `p` | 하고 · 와/과 · (이)랑 |
| จาก | `p` | 에서 (from) · 한테서 |
| ตั้งแต่ … ถึง | `p` | 부터 … 까지 |
| ของ | `p` | 의 / possessive (제 책 → `{n:หนังสือ}{p:ของ}{n:ฉัน}`) |
| ตอน / เมื่อ / ใน | `p` | time 에 (토요일에 → `{p:ตอน}{n:วันเสาร์}` or just `{n:วันเสาร์}`) |
| เป็น / คือ | `e` | 이에요/예요/입니다 · `{q:เป็นอย่างไร}` = 어때요 |
| แล้ว | `e` | past 았/었 · `{a:แล้วก็}` = 그리고 |
| จะ | `e` | ㄹ 거예요 / 겠 |
| คน ตัว เล่ม ขวด แก้ว ใบ ชิ้น โมง นาที วอน ปี เดือน ชั้น ห้อง | `m` | only right after a number (สามคน → `{m:สามคน}`); alone they are `n` |
| วันนี้ พรุ่งนี้ เมื่อวาน ตอนนี้ ทุกวัน ช่วงนี้ | `a` | 오늘 내일 어제 지금 매일 요즘 (no 에 in Korean) |
| เช้า บ่าย เย็น เสาร์ อาทิตย์ สุดสัปดาห์ ปิดเทอม | `n` | 아침 오후 저녁 토요일 주말 방학 (take 에 in Korean) |
| ท่าน · คุณ+kin (คุณปู่) | `N` / `n` | ท่าน = 분 → `N`; คุณปู่ for 할아버지 stays `n` unless the Korean is 할아버님/께서 |
| มอบ รับประทาน บรรทม | `V` | 드리다 드시다 주무시다 |
| ใช่ ค่ะ ครับ (as the answer word) | `a` | 네 — but ค่ะ/ครับ as a politeness tail stays plain |

Never tag the whole gloss with one class when the Korean has several classes. Never retranslate or change
Thai wording, spacing or punctuation — only add/fix tags. A gloss that is really an explanation (not a
translation of the Korean) gets **no tags**.

## 4. Review batch format (for agents)

Input `batch_N.tsv`, one item per line: `id<TAB>tagged Korean context<TAB>auto-tagged Thai gloss`.
Output `batch_N_out.tsv`: `id<TAB>corrected Thai gloss` — **only** the lines that needed a change
(fixed tags, or all tags removed for an explanation). Unchanged lines are not written. The Thai text with tags
stripped must be byte-identical to the input text, or the merge step rejects it.
