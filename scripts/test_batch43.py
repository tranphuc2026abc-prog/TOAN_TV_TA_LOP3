"""Specific regressions for third-person possession and ongoing actions."""
import json
from pathlib import Path
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
for n,pg,anchor in [(17,[46,51],'They have'),(18,[52,57],'listening to music'),(19,[58,63],'flying a kite'),(20,[64,69],'an elephant')]:
 p=R/f'content/tieng-anh/tap-2/TA3_T2_U{n}.json';c=json.loads(p.read_text());validate_subject(c)
 assert c['volume']==2 and c['source']['printed_pages']==pg and c['source']['pdf_pages']==[x+1 for x in pg]
 assert len(c['practice'])==12 and len(c['examples'])>=2 and anchor in json.dumps(c,ensure_ascii=False)
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert p.with_suffix('.md').exists()
c=json.loads((R/'content/tieng-anh/tap-2/TA3_T2_U20.json').read_text())
assert any('minh hoạ' in rule for rule in c['knowledge']['rules'])
qs=[q['question'] for p in (R/'content/tieng-anh').glob('tap-*/*.json') for q in json.loads(p.read_text())['practice']]
assert len(qs)==len(set(qs))
print('PASS batch43: four source-specific banks,48 new questions,game scopes,has/have and story/observation distinction.')
