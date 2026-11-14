"""Check source boundaries and nonrepeated English questions across all ready banks."""
import json
from pathlib import Path
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
for ident,pages,anchor in [('TA3_T1_U04',[28,33],'Open your mouth'),('TA3_T1_U05',[34,39],'running'),('TA3_T1_R01',[40,43],'smell'),('TA3_T1_U06',[44,49],'classroom')]:
 c=json.loads((R/f'content/tieng-anh/tap-1/{ident}.json').read_text());validate_subject(c)
 assert c['source']['printed_pages']==pages
 assert c['source']['pdf_pages']==[x+1 for x in pages]
 assert anchor in json.dumps(c,ensure_ascii=False)
 assert len(c['practice'])==12 and len(c['examples'])>=2
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
catalog=json.loads((R/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())
byid={e['id']:e for e in catalog['lessons']}
assert byid['TA3_T1_R01']['page_end']==43
assert (byid['TA3_T1_U06']['page_start'],byid['TA3_T1_U06']['page_end'])==(44,49)
assert byid['TA3_T1_U07']['page_start']==50
prompts=[q['question'] for p in (R/'content/tieng-anh').glob('tap-*/*.json') for q in json.loads(p.read_text())['practice']]
assert len(prompts)==len(set(prompts))
print('PASS batch39: 48 new questions, source boundaries, English schema, 4 games and all-English prompt uniqueness.')
