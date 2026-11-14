"""Meaningful regression for permission, possession, singular/plural colours and break activities."""
import json,xml.etree.ElementTree as ET
from pathlib import Path
from content_policy import validate_subject
R=Path(__file__).resolve().parents[1]
for n,pg,anchor in [(7,[50,55],'May I'),(8,[56,61],'Do you have'),(9,[62,67],'They\'re'),(10,[68,73],'word puzzles')]:
 c=json.loads((R/f'content/tieng-anh/tap-1/TA3_T1_U{n:02}.json').read_text());validate_subject(c)
 assert c['source']['printed_pages']==pg
 assert anchor in json.dumps(c,ensure_ascii=False)
 assert len(c['practice'])==12 and len(c['examples'])>=2
 assert c['status']=='AI_CHECKED_AWAITING_TEACHER' and not c['verification']['teacher_approved']
 assert set(c['games'][0]['question_ids'])=={q['question_id'] for q in c['practice']}
c=json.loads((R/'content/tieng-anh/tap-1/TA3_T1_U09.json').read_text());q=c['practice'][4]
assert q['correct_answer']=='B.' and q['figure']['path']==c['figures'][0]['path']
svg=ET.parse(R/q['figure']['path']).getroot();ns={'s':'http://www.w3.org/2000/svg'}
assert len(svg.findall('s:rect',ns))==3
assert svg.findall('s:rect',ns)[1].attrib['fill']=='#df2525'
assert [e.text for e in svg.findall('s:g/s:text',ns)]==['A','B','C']
qs=[q['question'] for p in (R/'content/tieng-anh').glob('tap-*/*.json') for q in json.loads(p.read_text())['practice']]
assert len(qs)==len(set(qs))
print('PASS batch40: 4 banks/48 distinct new questions, correct source ranges, game scope, teacher status and new SVG answer B.')
