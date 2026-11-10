import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-1/TV3_T1_B{n}.json').read_text()) for n in range(29,33)]
for c in a:
 assert len(c['practice'])==12 and len(c['games'])==1
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert {s:sum(q['skill']==s for q in c['practice']) for s in ['reading','vocabulary','sentences','spelling','expression']}==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
# Chi tiết nguồn dễ bị lẫn với bản kể khác; kiểm tra vai trò, phương án và lời giải.
assert a[0]['practice'][0]['correct_answer']=='Tập nhảy.'
assert a[1]['practice'][1]['correct_answer']=='Chuyển sang dùng máy phát điện ngay.'
assert a[2]['practice'][3]['correct_answer']=='Vẫn nặn đồ chơi để bán.'
assert a[3]['practice'][3]['correct_answer']=='Chiếc thang em vẽ trên tường.'
for c in a:
 assert len(c['examples'])>=2
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert len({q['options'].index(q['correct_answer']) for q in c['practice']})==4
 assert '10/11/2026' in c['source']['review']
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch29:48 câu,4 game,5 nhóm kỹ năng,4 chi tiết neo và toàn bộ TV không trùng đề.')
