"""Final acceptance: all 168 entries must resolve to real subject-specific content."""
import json
from pathlib import Path
from collections import Counter
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
index=json.loads((R/'content/system/INDEX.json').read_text())
catalog=json.loads((R/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())
meta={c['id']:c for c in catalog['lessons']}
approved={i for c in json.loads((R/'content/system/APPROVALS.json').read_text())['confirmations'] for i in c['lesson_ids']}
assert approved=={f'TOAN3_T1_B{n:02}' for n in range(1,5)}
assert len(index['lessons'])==len(meta)==168
assert index['progress']==dict(ai_authored=168,ai_checked=168,teacher_approved=4,awaiting_teacher=164,remaining=0)
counts=Counter();questions=Counter();games=Counter();teacher=set()
for e in index['lessons']:
 assert e['path'] and e['markdown'] and e['status']!='BAN_NHAP'
 c=json.loads((R/e['path']).read_text());validate_subject(c)
 assert c['id']==e['id'] and c['subject']==e['subject']
 assert meta[c['id']]['content_status']==c['status']
 assert all(c['objectives']) and all(c['knowledge'][k] for k in ['introduction','rules','steps','common_errors'])
 assert len(c['examples'])>=1 and all(x['question'] and x['steps'] for x in c['examples'])
 assert c['feedback'] and c['assessment'] and c['games']
 if c['subject'] in ('tv','ta'):assert c['activities']
 else:assert c['practice'] and c['knowledge']['steps']
 assert c['source']['review'] and c['source']['pdf_pages'] and c['source']['printed_pages']
 if c['verification']['teacher_approved']:teacher.add(c['id']);assert c['status']=='TEACHER_APPROVED'
 else:assert c['status']=='AI_CHECKED_AWAITING_TEACHER'
 counts[c['subject']]+=1;questions[c['subject']]+=len(c['practice']);games[c['subject']]+=len(c['games'])
assert teacher==approved
assert counts==dict(toan=81,tv=62,ta=25)
assert questions==dict(toan=3240,tv=776,ta=300)
assert games==counts
last=json.loads((R/'content/tieng-anh/tap-2/TA3_T2_R04.json').read_text())
assert last['source']['printed_pages']==[70,73] and last['source']['pdf_pages']==[71,74]
assert len(last['practice'])==12 and last['lesson_no']==4
assert any(v['word']=='kitten' for v in last['vocabulary'])
assert any('không chỉ' in x for x in last['patterns'])
print('PASS complete catalog:168 JSON+168 Markdown,4316 questions,168 games;4 teacher-approved and164 awaiting teacher;correct last Review4 source.')
