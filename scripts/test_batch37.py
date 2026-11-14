"""Regression: full Vietnamese catalog and the last two source-specific banks."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
for n,anchor in [(29,'nước Pháp'),(30,'Bầu trời')]:
 c=json.loads((R/f'content/tieng-viet/tap-2/TV3_T2_B{n}.json').read_text())
 assert len(c['practice'])==12 and c['assessment']['session_size']==10
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert anchor in json.dumps(c,ensure_ascii=False)
 assert sum(q['skill']=='reading' and bool(q.get('evidence')) for q in c['practice'])==4
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert all(c['language_practice'][s] for s in ['vocabulary','sentences','spelling','expression'])
# Do not silently count a Vietnamese draft as finished when crossing to English.
index=json.loads((R/'content/system/INDEX.json').read_text())
files=list((R/'content/tieng-viet').glob('tap-*/*.json'))
assert len(files)==62
prompts=[q['question'] for f in files for q in json.loads(f.read_text())['practice']]
assert len(prompts)==len(set(prompts))
print('PASS batch37: 62 Vietnamese banks; source anchors, 24 new questions, evidence, language groups and games.')
