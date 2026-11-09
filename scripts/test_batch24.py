"""Hồi quy chi tiết nguồn TV9–12 và ngân hàng Tiếng Việt đã xuất bản."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
all_tv=[json.loads(p.read_text()) for p in sorted((ROOT/'content/tieng-viet/tap-1').glob('TV3_T1_B*.json'))]
questions=[q['question'] for c in all_tv for q in c['practice']]
assert len(questions)==len(set(questions)), 'Trùng nguyên văn câu hỏi Tiếng Việt'
for n in range(9,13):
 c=json.loads((ROOT/f'content/tieng-viet/tap-1/TV3_T1_B{n:02}.json').read_text())
 assert len(c['practice'])==12
 assert {q['skill'] for q in c['practice']}=={'reading','vocabulary','sentences','spelling','expression'}
 assert c['assessment']['session_size']==10
 assert c['activities'] and all(a['check'] for a in c['activities'])
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert len(set(q['correct_answer'] for q in c['practice']))>=5
 answers=[q['correct_answer'] for q in c['practice']]
 if n==9:assert answers[1]=='Lật những trang sách mới' and answers[3]=='Bước chân hòa với lời hát'
 if n==10:assert answers[2]=='Lầy và trơn, có đoạn ngập' and answers[3]=='Đợi ở đoạn khó để đưa các bạn đi'
 if n==11:assert answers[2]=='Mười lăm phút' and answers[3]=='Lời giải đúng được trình bày bằng thơ'
 if n==12:assert answers[1]=='Cậu ít khi giúp mẹ làm việc nhà' and answers[2]=='Viết thêm cả việc chưa làm'
print('PASS Batch24: 48 câu, các chi tiết dễ nhầm, 5 nhóm kỹ năng, game và trạng thái; toàn bộ câu TV không trùng nguyên văn.')
