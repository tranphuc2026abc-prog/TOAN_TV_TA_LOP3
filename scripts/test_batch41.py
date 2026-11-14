"""Regression crossing from book1 to book2 without relabelling source or volume."""
import json
from pathlib import Path
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
for ident,vol,pg,anchor in [('TA3_T1_R02',1,[74,77],'Yes, you can'),('TA3_T2_U11',2,[6,11],'nineteen'),('TA3_T2_U12',2,[12,17],'nurse'),('TA3_T2_U13',2,[18,23],'on the table')]:
 p=R/f'content/tieng-anh/tap-{vol}/{ident}.json';c=json.loads(p.read_text());validate_subject(c)
 assert c['volume']==vol and c['source']['pdf']==f'03-sgk-tieng-anh-3-tap-{vol}-global-success.pdf'
 assert c['source']['printed_pages']==pg and c['source']['pdf_pages']==[x+1 for x in pg]
 assert len(c['practice'])==12 and len(c['examples'])>=2
 assert anchor in json.dumps(c,ensure_ascii=False)
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert p.with_suffix('.md').exists()
qs=[q['question'] for p in (R/'content/tieng-anh').glob('tap-*/*.json') for q in json.loads(p.read_text())['practice']]
assert len(qs)==len(set(qs))
print('PASS batch41: 4 banks/48 new questions, correct volume/source/path/page mapping and no repeated English prompts.')
