"""English schema and source-specific regression; keep all previous subject tests."""
import json,copy
from pathlib import Path
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
ids=['TA3_T1_START','TA3_T1_U01','TA3_T1_U02','TA3_T1_U03']
seen=set()
for ident in ids:
 c=json.loads((R/f'content/tieng-anh/tap-1/{ident}.json').read_text());validate_subject(c)
 assert len(c['practice'])==12 and len(c['examples'])>=2
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert c['source']['pdf_pages']==[p+1 for p in c['source']['printed_pages']]
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
 for q in c['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
  assert len(q['options'])==4 and len(set(q['options']))==4
 for mutate in [lambda x:x['vocabulary'][0].pop('meaning_vi'),lambda x:x['skills'].update(speaking=[]),lambda x:x['audio'].update(label='Âm thanh sách'),lambda x:x['assessment'].update(session_size=13),lambda x:x['assessment'].update(distribution={'nhan_biet':3}),lambda x:x['source'].update(review='')]:
  bad=copy.deepcopy(c);mutate(bad)
  try:validate_subject(bad)
  except (AssertionError,KeyError):pass
  else:raise AssertionError('Invalid English content accepted')
assert 'How are you?' in json.dumps(json.loads((R/'content/tieng-anh/tap-1/TA3_T1_U01.json').read_text()))
assert 'How old are you?' in json.dumps(json.loads((R/'content/tieng-anh/tap-1/TA3_T1_U02.json').read_text()))
assert 'Is that' in json.dumps(json.loads((R/'content/tieng-anh/tap-1/TA3_T1_U03.json').read_text()))
print('PASS batch38: 4 English banks, 48 distinct questions; schema rejects missing translation, speaking, source, machine label and Math distribution.')
