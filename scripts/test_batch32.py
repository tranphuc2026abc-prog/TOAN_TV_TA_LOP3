"""Bài9–12: hồi quy căn cứ, giới hạn suy luận và sửa trang nguồn theo ảnh sách."""
import json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
a=[json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n:02}.json').read_text()) for n in range(9,13)]
for n,c in enumerate(a,9):
 assert c['id']==f'TV3_T2_B{n:02}' and c['volume']==2 and c['lesson_no']==n
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert Counter(q['skill'] for q in c['practice'])==dict(reading=4,vocabulary=2,sentences=2,spelling=2,expression=2)
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert len(c['examples'])==2
assert a[0]['practice'][2]['correct_answer']=='Bác cho biết mình cũng tập mỗi ngày.'
assert 'đói lả' in a[1]['practice'][1]['correct_answer']
assert 'tiếc' in a[2]['practice'][3]['correct_answer'] and 'chưa kể chim trở lại' in a[2]['knowledge']['rules'][1]
assert 'giữ giấy' in a[3]['practice'][1]['correct_answer']
assert 'không dùng truyện để bắt bạn đổi tay thuận' in a[3]['knowledge']['rules'][2]
cat=json.loads((R/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())['lessons']
assert next(x for x in cat if x['id']=='TV3_T2_B11')['page_end']==50
assert next(x for x in cat if x['id']=='TV3_T2_B12')['page_start']==51
assert a[2]['source']['printed_pages']==[48,50] and a[3]['source']['printed_pages']==[51,54]
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].casefold().strip();assert key not in seen,(p,key);seen.add(key)
print('PASS Batch32: 48 câu/4 game, suy luận không thêm kết truyện, hợp tác/tay thuận, trang11–12 đúng nguồn; TV không trùng đề.')
