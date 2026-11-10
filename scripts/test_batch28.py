import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-1/TV3_T1_B{n}.json').read_text()) for n in range(25,29)]
for c in a:
 assert len(c['practice'])==12 and len(c['games'])==1
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert {s:sum(q['skill']==s for q in c['practice']) for s in ['reading','vocabulary','sentences','spelling','expression']}==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
assert a[0]['practice'][2]['correct_answer']=='Sau năm năm.'
assert a[1]['practice'][2]['correct_answer']=='Sao lặn.'
assert a[2]['practice'][2]['correct_answer']=='Ốc sên kẻ vạch, bọ ngựa cắt theo vạch.'
assert a[3]['practice'][0]['correct_answer']=='Nghề lái tàu.'
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch28:48 câu,4 game,5 nhóm kỹ năng,4 chi tiết neo và toàn bộ TV không trùng đề.')
