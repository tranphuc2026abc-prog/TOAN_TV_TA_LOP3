import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n}.json').read_text()) for n in range(25,29)]
for n,c in enumerate(a,25):
 assert c['id']==f'TV3_T2_B{n}' and c['lesson_no']==n and c['volume']==2
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
assert 'giờ khai mạc' in a[0]['practice'][3]['correct_answer']
assert 'Nhân vật người máy' in a[1]['practice'][0]['correct_answer']
assert 'nhân hoá' in a[2]['knowledge']['rules'][0]
assert 'Người làm ra thức ăn' in a[3]['practice'][3]['correct_answer']
assert 'không có nghĩa ép mình ăn quá sức' in a[3]['knowledge']['rules'][1]
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch36: 48 câu/4 game; ngọn lửa, nhân vật kịch, thư nhân hoá và ba việc nhỏ; TV không trùng đề.')
