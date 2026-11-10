"""Hồi quy nội dung và mốc ôn tập sau bài16, giữ đủ môn và các bài cũ."""
import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n}.json').read_text()) for n in range(13,17)]
for n,c in enumerate(a,13):
 assert c['id']==f'TV3_T2_B{n}' and c['lesson_no']==n and c['volume']==2
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
assert 'Cả hai bỏ' in a[0]['practice'][3]['correct_answer']
assert 'Ngạc nhiên nhưng suy nghĩ' in a[1]['practice'][2]['correct_answer']
assert 'được nghỉ ngơi' in a[2]['practice'][2]['correct_answer']
assert 'thì thào' in a[3]['practice'][1]['correct_answer']
assert 'Nhỏ quá' in a[3]['practice'][2]['correct_answer']
assert a[3]['source']['printed_pages']==[66,70]
cat=json.loads((R/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())['lessons'];assert next(x for x in cat if x['id']=='TV3_T2_B16')['page_end']==70
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch33:48 câu/4 game, trách nhiệm hai mèo/học nền tảng/góc nhìn kiến/hai âm lượng; nguồn bài16 dừng trước ôn tập.')
