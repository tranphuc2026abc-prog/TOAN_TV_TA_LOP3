"""Source-specific regressions for room descriptions, polite food offers and pets."""
import json
from pathlib import Path
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
for ident,pg,anchor in [('U14',[24,29],'There are'),('U15',[30,35],'Would you like'),('R03',[36,39],'on the desk'),('U16',[40,45],'goldfish')]:
 p=R/f'content/tieng-anh/tap-2/TA3_T2_{ident}.json';c=json.loads(p.read_text());validate_subject(c)
 assert c['volume']==2 and c['source']['pdf']=='03-sgk-tieng-anh-3-tap-2-global-success.pdf'
 assert c['source']['printed_pages']==pg and c['source']['pdf_pages']==[x+1 for x in pg]
 assert len(c['practice'])==12 and len(c['examples'])>=2 and anchor in json.dumps(c,ensure_ascii=False)
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert p.with_suffix('.md').exists()
c=json.loads((R/'content/tieng-anh/tap-2/TA3_T2_U16.json').read_text())
assert 'Số cá vàng cụ thể.' in {q['correct_answer'] for q in c['practice']}
assert 'I have two goldfish.' in {q['correct_answer'] for q in c['practice']}
qs=[q['question'] for p in (R/'content/tieng-anh').glob('tap-*/*.json') for q in json.loads(p.read_text())['practice']]
assert len(qs)==len(set(qs))
print('PASS batch42: 48 new questions, correct sources, scopes and pets quantifier/non-count precision checks.')
