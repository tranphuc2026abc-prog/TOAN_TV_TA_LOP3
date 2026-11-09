"""Hồi quy TV5–8 và chống trùng câu trên toàn bộ TV1–8."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
objects=[json.loads((ROOT/f'content/tieng-viet/tap-1/TV3_T1_B{i:02}.json').read_text()) for i in range(1,9)]
prompts=[q['question'] for c in objects for q in c['practice']]
assert len(prompts)==len(set(prompts))==128
for c in objects[4:]:
 assert len(c['practice'])==16 and c['assessment']['session_size']==10
 assert set(q['skill'] for q in c['practice'])=={'reading','vocabulary','sentences','spelling','expression'}
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert c['examples'] and c['activities'] and c['activities'][0]['check']
 assert 'difficulty' not in c['practice'][0]
def a(n,q):return objects[n-1]['practice'][q-1]['correct_answer']
assert a(5,5)=='Bạn chưa thở dưới nước được và hơi buồn'
assert a(5,6)=='Bơi ếch'
assert a(6,1)=='Trứng đúc thịt'
assert a(6,3)=='Nguyên liệu'
assert a(7,5)=='Thong thả ở chân trời, còn chưa lặn'
assert a(8,6)=='Điều Diệu nghĩ các bạn có thể kể'
assert a(8,4)=='Không nhìn thấy nhưng vẫn tự làm việc trong nhà'
print('PASS batch23: 64 câu TV5–8, trình tự/chi tiết quan trọng và 128 câu TV1–8 không trùng; nói/viết tự đánh giá, không tự duyệt.')
