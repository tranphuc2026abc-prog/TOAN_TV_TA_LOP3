"""Hồi quy nghĩa dễ nhầm và tính độc lập câu hỏi TV17–20."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
lessons=[json.loads((R/f'content/tieng-viet/tap-1/TV3_T1_B{n}.json').read_text()) for n in range(17,21)]
for c in lessons:
 assert len(c['practice'])==12
 assert sum(q['skill']=='reading' for q in c['practice'])==4
 assert all(q.get('evidence') for q in c['practice'] if q['skill']=='reading')
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert len(c['games'][0]['question_ids'])==12
 assert c['assessment']['session_size']==10
 assert all(c['language_practice'][s] for s in ['vocabulary','sentences','spelling','expression'])
assert lessons[2]['practice'][1]['correct_answer']=='Chưa thể, bạn nhỏ chỉ đang đặt câu hỏi.'
assert lessons[3]['practice'][0]['correct_answer']=='Mẹ, Thư và Hân.'
assert lessons[3]['practice'][3]['correct_answer']=='Kể về hình dáng của mẹ khi còn bé.'
seen=set()
for p in (R/'content/tieng-viet').glob('tap-*/*.json'):
 for q in json.loads(p.read_text())['practice']:
  key=q['question'].strip().casefold()
  assert key not in seen, (p,key)
  seen.add(key)
print('PASS Batch26: 4 bài, 48 câu; căn cứ đọc hiểu, từ ba, câu hỏi tuổi thơ, 4 trò chơi và không trùng đề TV.')
