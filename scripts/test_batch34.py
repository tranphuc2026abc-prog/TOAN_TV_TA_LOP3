"""Hồi quy chi tiết quê hương, lời kể tên sông và dấu thanh; giữ mọi hồi quy cũ."""
import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n}.json').read_text()) for n in range(17,21)]
for n,c in enumerate(a,17):
 assert c['id']==f'TV3_T2_B{n}' and c['lesson_no']==n and c['volume']==2
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert '14/11/2026' in c['source']['review'] and len(c['examples'])==2
assert 'bình dị' in a[0]['practice'][3]['correct_answer']
assert a[1]['practice'][2]['correct_answer']=='Chè xanh và khói bếp nhà ai.'
assert 'Theo câu chuyện được kể' in a[2]['practice'][0]['question']
assert 'thạch xương bồ' in a[2]['practice'][0]['correct_answer']
assert 'hoa phượng' in a[2]['practice'][2]['correct_answer']
assert 'thanh ngang' in a[3]['practice'][3]['correct_answer']
assert a[3]['practice'][8]['correct_answer']=='Dấu ngã trong võng.'
cat=json.loads((R/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())['lessons']
assert next(x for x in cat if x['id']=='TV3_T2_B19')['page_end']==90
assert next(x for x in cat if x['id']=='TV3_T2_B20')['page_start']==91
assert a[2]['source']['printed_pages']==[87,90] and a[3]['source']['printed_pages']==[91,94]
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch34:48 câu/4 game; mùi hương/giác quan/sắc phượng/thanh ngang, nguồn19–20 và toàn bộ TV không trùng đề.')
