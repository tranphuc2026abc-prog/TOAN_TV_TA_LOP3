"""Hồi quy độc lập: chuyển tập, chuyển hàng, La Mã và biên làm tròn."""
import json,re,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def lesson(n): return json.loads((ROOT/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text())
objects={n:lesson(n) for n in range(45,49)}
questions=[q['question'] for o in objects.values() for q in o['practice']]
assert len(questions)==len(set(questions))==160
for n,o in objects.items():
 assert o['volume']==2 and o['lesson_no']==n
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 assert o['source']['pdf_pages']==[o['source']['printed_pages'][0]+1,o['source']['printed_pages'][1]+1]
# Các giá trị được tính độc lập từ cấu tạo/dãy và giới hạn.
expected={45:{3:6*100,9:9300//10,21:2997+3,22:248+1,25:8998+2,26:6*1000+4*100+3,28:9+1,30:10000-9*1000,31:4000-3*100,38:9997+3,40:3000+15*10},46:{21:max(2405,2450,2045),22:min(3180,3081,3108),23:sorted([5070,5700,5007])[1],30:min(4512,4521,4152,4251),31:len(range(4998,5001)),37:max(v for v in [1498,1500,1502] if v<=1500)}}
for n,cases in expected.items():
 for i,v in cases.items(): assert objects[n]['practice'][i-1]['correct_answer']==str(v),(n,i)
roman=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
for q in objects[47]['practice']:
 m=re.fullmatch(r'Số ([IVX]+) (?:biểu thị|được đọc là) số mấy\?',q['question'])
 if m: assert int(q['correct_answer'])==roman.index(m[1])+1
for i,v in {5:4,6:6,12:'XV',13:'XVIII',15:'VII',16:'XIV',17:4,18:5,26:'XIV',28:'XIX',29:'XV',30:6,31:0,33:7,34:'VI',38:'XV',39:'XVII',40:3}.items():
 assert objects[47]['practice'][i-1]['correct_answer']==str(v),i
# Dùng khoảng cách tới hai mốc thay vì chép quy tắc so chữ số.
def rounded(x,unit):
 lo=x//unit*unit;hi=lo+unit
 return lo if x-lo < hi-x else hi
for q in objects[48]['practice']:
 m=re.fullmatch(r'Làm tròn (\d+) đến hàng (chục|trăm)(?: được số nào\?|\.)',q['question'])
 if m: assert int(q['correct_answer'])==rounded(int(m[1]),10 if m[2]=='chục' else 100)
for i,target,unit,which in [(25,270,10,min),(26,480,10,max),(27,3600,100,min),(28,9100,100,max)]:
 candidates=[x for x in range(10001) if rounded(x,unit)==target]
 assert int(objects[48]['practice'][i-1]['correct_answer'])==which(candidates)
for i,v in {29:470,30:1400,32:7400,33:5000,34:6501,36:5,37:4,38:7250,39:200,40:28}.items():
 assert objects[48]['practice'][i-1]['correct_answer']==str(v),i
f=objects[47]['practice'][32]['figure']
assert f==objects[47]['figures'][0]
ET.parse(ROOT/f['path'])
print('PASS Batch 12: 160 câu riêng; tập 2, chuyển hàng, La Mã, khoảng biên làm tròn và SVG đồng hồ.')
