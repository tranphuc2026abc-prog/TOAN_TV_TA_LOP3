"""Hồi quy tập2: ID không đụng tập1, chi tiết nguồn và loại câu theo nghĩa."""
import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n:02}.json').read_text()) for n in range(1,5)]
for n,c in enumerate(a,1):
 assert c['id']==f'TV3_T2_B{n:02}' and c['volume']==2 and c['lesson_no']==n
 assert 'tap-hai' in c['source']['pdf']
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert len(c['examples'])==2
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert all(q['question_id'].startswith(c['id']) for q in c['practice'])
 assert 'luôn một màu' in a[0]['knowledge']['rules'][1]
assert a[1]['practice'][2]['correct_answer']=='Chị.'
assert 'Cua giơ' in a[2]['practice'][2]['correct_answer']
assert 'bật cười' in a[3]['practice'][3]['correct_answer']
assert 'Dấu chấm than có thể đi với cả hai' in a[1]['knowledge']['rules'][2]
idx=json.loads((R/'content/system/INDEX.json').read_text())['lessons']
for n in range(1,5):
 for v in (1,2):
  ident=f'TV3_T{v}_B{n:02}';item=next(x for x in idx if x['id']==ident)
  assert f'/tap-{v}/' in item['path']
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch30: tập2 đúng ID/nguồn/đường dẫn,48 câu,4 game,5 nhóm kỹ năng; nguồn và không trùng đề TV.')
