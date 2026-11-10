"""Nguồn bài5–8, sửa tên OCR bằng đối chiếu trang32 và giữ hồi quy tập1/2."""
import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n:02}.json').read_text()) for n in range(5,9)]
for n,c in enumerate(a,5):
 assert c['id']==f'TV3_T2_B{n:02}' and c['volume']==2 and c['lesson_no']==n
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
assert a[0]['practice'][3]['correct_answer']=='Cọn nước quay bên suối.'
assert a[1]['practice'][2]['correct_answer']=='Xanh mát, yên tĩnh và trầm tư hơn.'
assert 'toả tia' in a[2]['practice'][2]['explanation']
assert 'cứu một con sa bẫy' in a[3]['practice'][2]['correct_answer']
for f in ['content/system/INDEX.json','data/CHUONG_TRINH_LOP_3_FULL.json']:
 c=json.loads((R/f).read_text());m=next(x for x in c['lessons'] if x['id']=='TV3_T2_B07');assert m['title']=='Mặt trời xanh của tôi'
assert 'Đọc bài thơ “Mặt trời xanh của tôi”' in (R/'index.html').read_text()
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch31:48 câu/4 game, vai trò ngày hội/cây gạo/lá cọ/voi, sửa tên OCR đồng bộ và không trùng đề TV.')
