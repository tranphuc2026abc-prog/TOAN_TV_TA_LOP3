"""Chi tiết văn hoá cộng đồng, thể loại sự tích và hai sự việc qua suối."""
import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n}.json').read_text()) for n in range(21,25)]
for n,c in enumerate(a,21):
 assert c['id']==f'TV3_T2_B{n}' and c['lesson_no']==n and c['volume']==2
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert len(c['examples'])==2 and '14/11/2026' in c['source']['review']
assert 'cùng góp xây' in a[0]['practice'][3]['correct_answer']
assert 'lời giải thích tưởng tượng' in a[1]['practice'][3]['explanation']
assert 'Giỏi võ nghệ' in a[2]['practice'][1]['correct_answer']
assert a[3]['practice'][0]['correct_answer']=='Nhặt lên đặt trên bờ để người sau khỏi trượt.'
assert 'kê không cân' in a[3]['practice'][1]['correct_answer']
assert 'kê đá cho chắc rồi' in a[3]['practice'][6]['correct_answer']
assert a[3]['source']['printed_pages']==[106,109]
cat=json.loads((R/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())['lessons']
assert next(x for x in cat if x['id']=='TV3_T2_B24')['page_end']==109
assert next(x for x in cat if x['id']=='TV3_T2_B25')['page_start']==111
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch35:48 câu/4 game, nhà chung/truyền thuyết/Hai Bà/hai sự việc qua suối, nguồn24–25 và TV không trùng đề.')
