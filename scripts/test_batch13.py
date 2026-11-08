"""Hồi quy chu vi/diện tích: đổi đơn vị, cạnh chung, phần ghép/cắt và SVG."""
import json,re,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
objects={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(49,53)}
seen=set()
for n,o in objects.items():
 assert o['volume']==2 and o['lesson_no']==n
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
 for f in o.get('figures',[]):ET.parse(R/f['path'])
assert len(seen)==160
# Đáp án neo từ cách tính độc lập, gồm cả tìm cạnh rồi mới tính diện tích.
expected={49:{21:sorted([3450,3540,3405])[1],24:2100,25:6998+3,26:6,27:8,28:17-14,29:2800,30:7040-4*10,31:'C',32:9090,33:'XVIII',34:9,35:2700-2680,36:4,37:9042,38:15,39:4100,40:1},50:{13:2*(100+35),15:32//4,16:19-6,17:24-9-8,18:26-5-7-8,19:(6-4)*4,20:3*2,21:2*(14+6)-3,23:70-(18+20+22),26:100//4,28:54//2-9,31:64//2-10,34:20*4-2*2,35:2*(16+16//2),36:(27//3)*4,37:50-sum([11,13,9,15]),38:2*(20+8),39:2*(8+4),40:90-2*(17+13)},51:{17:5,18:8,20:5,26:8-5,27:42-6*5,28:'có',29:10+8-2,30:4+4//2,31:7+11+12,32:50-18-15,33:'sai',36:36+36//2,39:'B',40:24-9-8},52:{12:20*5,14:(20//4)**2,15:42//6,16:2,17:(6*6)//(3*3),19:7*7-2*2,20:8*5//4,23:25*10-10*6,24:9*9-3*5,25:(8+5)*3,26:14*6//2,27:(28//4)**2,28:(30//2-5)*5,29:4*3*3,30:(12//3)*(9//3),31:10*10-4*2*2,33:8*8-24,34:20*12//3,35:10*4+3*3,36:2*(8+56//8),37:11*8-9*6,38:'chữ nhật',39:30*20-2*5*5,40:2*6}}
for n,cases in expected.items():
 for i,value in cases.items():assert objects[n]['practice'][i-1]['correct_answer']==str(value),(n,i,value)
ns={'s':'http://www.w3.org/2000/svg'}
def unit_count(suffix):
 root=ET.parse(R/f'content/toan/tap-2/TOAN3_T2_B51_{suffix}.svg').getroot()
 cells=root.findall('.//s:rect[@data-unit-cell="1"]',ns)
 positions={(c.get('x'),c.get('y')) for c in cells}
 assert len(positions)==len(cells)
 assert all(c.get('width')==c.get('height')=='34' for c in cells)
 return len(cells)
assert unit_count('A')==5 and unit_count('B')==8 and unit_count('AB')==13
# Diện tích từng phần của SVG D phải khớp tỉ lệ 30 pixel/cm; chỉ chung đường biên.
d=ET.parse(R/'content/toan/tap-2/TOAN3_T2_B52_D.svg').getroot()
rects=d.findall('.//s:g/s:rect',ns)
assert [(int(x.get('width'))//30,int(x.get('height'))//30) for x in rects]==[(10,4),(3,3)]
assert int(rects[1].get('y'))+int(rects[1].get('height'))==int(rects[0].get('y'))
assert int(objects[52]['practice'][34]['correct_answer'])==sum(int(x.get('width'))*int(x.get('height'))//900 for x in rects)
# Cạnh ghép 4 cm bị đếm hai lần nếu chỉ cộng chu vi hai hình vuông.
assert int(objects[50]['practice'][38]['correct_answer'])==2*(4*4)-2*4
print(f'PASS Batch 13: 160 câu, {sum(map(len,expected.values()))} đáp án neo, đổi đơn vị/cạnh chung/cắt ghép; SVG ô không trùng và diện tích đúng tỉ lệ.')
