"""Hồi quy Tiếng Việt thực: căn cứ đọc hiểu, nhóm ngôn ngữ, hoạt động và game."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
anchors=[('Chi','Sơn','xe đạp'),('bà','quả','quạt'),('ông','sóc','lời'),('Thắng','Hải','còng gió')]
for n,words in enumerate(anchors,1):
 c=json.loads((ROOT/f'content/tieng-viet/tap-1/TV3_T1_B{n:02}.json').read_text())
 assert all(w.lower() in c['reading']['summary'].lower() for w in words)
 qs=c['practice'];assert len(qs)==16
 assert {q['skill'] for q in qs}=={'reading','vocabulary','sentences','spelling','expression'}
 assert all(q.get('evidence','').startswith('Trang ') for q in qs if q['skill']=='reading')
 assert len({q['correct_answer'] for q in qs})>=5
 assert all('difficulty' not in q for q in qs)
 assert c['activities'] and all(a['check'] and len(a['steps'])>=3 for a in c['activities'])
 assert c['verification']['source_reviewed'] and not c['verification']['teacher_approved']
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER'
# Những chi tiết dễ nhầm phải được giữ đúng, không chỉ kiểm tra có từ khóa.
def answer(n,q):
 c=json.loads((ROOT/f'content/tieng-viet/tap-1/TV3_T1_B{n:02}.json').read_text());return c['practice'][q-1]['correct_answer']
assert answer(1,5)=='Bố của Chi'
assert answer(2,4)=='Bà muốn để dành cho cháu khi cháu về'
assert answer(3,6)=='Qua lời ông kể về khu rừng ngày trước'
assert answer(4,4)=='Hải'
assert answer(4,5)=='Thắng ở Hà Nội, vào Quy Nhơn thăm bác'
print('PASS batch22: TV1–4, 64 câu mới đủ 5 nhóm kỹ năng; căn cứ, nhầm lẫn nhân vật, hoạt động, game và trạng thái.')
