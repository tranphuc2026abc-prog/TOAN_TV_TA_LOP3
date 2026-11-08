"""Hồi quy số nhớ, đổi qua chữ số 0, hình ghép và bài toán nhiều bước."""
import json,re,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
objects={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(53,57)}
seen=set()
for n,o in objects.items():
 assert o['volume']==2 and o['lesson_no']==n
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
assert len(seen)==160
# Tính lại mọi câu phép tính thuần túy từ dữ kiện trong câu, không dựa vào lời giải.
ops={'+':lambda a,b:a+b,'-':lambda a,b:a-b,'×':lambda a,b:a*b}
checked=0
for o in objects.values():
 for q in o['practice']:
  m=re.fullmatch(r'(?:Tính|Nhẩm) (\d+) ([+×-]) (\d+)\.',q['question'])
  if m:
   assert int(q['correct_answer'])==ops[m[2]](int(m[1]),int(m[3])),q['question_id'];checked+=1
# Tính độc lập bài nhiều bước và điều kiện, tránh chỉ lặp cách diễn đạt của lời giải.
expected={53:{11:'có',12:'bằng nhau',13:'vuông',14:30*7,15:2*(10+3),18:(24//4)**2,21:2*(3*12+12),22:3*12*12,23:(40//4)**2,24:2*32*8,25:12*5+4*3,26:10*10-4*4,27:2*(17+8)-4,28:84//2-12,29:100-3*5*5,30:4*5-1,31:50-2*(16+7),33:35+48-7,34:3*5,36:2*(12+84//12),37:(36//2-4)*4,39:100-8*7,40:2*(8+3)-2*(6+4)},54:{11:0,12:2678+1547,13:3586+2427,15:1,16:3999+2001,18:1250+3750+2000,19:(4812+1369)//1000,21:2356+1789,22:1480+265,23:1825+1760+900,24:1250+(1250+350),27:2500+1500,29:1678+221+1101,31:2480+(2480+120),33:'A',34:(2750+1250)//1000,36:1700,37:5,38:1035+2065+900,39:'có',40:1999+3001+125},55:{11:4321-1567,12:0,13:6002-1548,14:8200-75,15:4282,18:1800+2450,19:5400-2750,20:len(str(7000-6999)),21:8200-2365,23:7500-1850-1650,25:8000-3500-2500,27:9500-1720-2380,28:4135+865,31:3200-1260-(1260-140),32:6000-2450+750,33:4080-1999-1001,35:2500-999,36:5,37:(3105-100)-(2817+100),40:5800-1250+450},56:{11:1427*4,12:3,13:1506*3,15:len(str(2486*2)),16:'có',18:6,19:1760*2*2,20:'không',23:1205*6,24:1325*4,26:4*1125+350,27:3*2100-650,28:10000-5*1500,29:2*1238+1524,31:3*1240+280,32:1256,33:3*1420+740,34:4*2250,35:7*1085,36:3*1320+(1320-120),37:8*1007-56,38:6,39:3*(1450-1200),40:3*2030-4*1500}}
for n,cases in expected.items():
 for ordinal,value in cases.items():assert objects[n]['practice'][ordinal-1]['correct_answer']==str(value),(n,ordinal,value)
# Chuỗi nhớ phép nhân 1427 × 4: cộng số nhớ SAU khi nhân từng chữ số.
carry=0;digits=[];trace=[]
for digit in reversed('1427'):
 value=int(digit)*4+carry;digits.append(str(value%10));carry=value//10;trace.append(carry)
assert ''.join(reversed(digits))=='5708' and carry==0 and trace==[2,1,1,0]
# Phép cộng 2678 + 1547 phải nhớ liên tiếp ba cột đầu.
carry=0;out=[];trace=[]
for a,b in zip(reversed('2678'),reversed('1547')):
 value=int(a)+int(b)+carry;out.append(str(value%10));carry=value//10;trace.append(carry)
assert ''.join(reversed(out))=='4225' and trace==[1,1,1,0]
ns={'s':'http://www.w3.org/2000/svg'}
for figure in objects[53]['figures']:ET.parse(R/figure['path'])
root=ET.parse(R/'content/toan/tap-2/TOAN3_T2_B53_C.svg').getroot()
cells=root.findall('.//s:rect[@data-unit-cell="1"]',ns)
assert len(cells)==20 and len({(c.get('x'),c.get('y')) for c in cells})==20
assert sum(int(c.get('data-painted')) for c in cells)==int(objects[53]['practice'][29]['correct_answer'])==19
for i in [20,21,24,29]:assert objects[53]['practice'][i].get('figure')
print(f'PASS Batch 14: 160 câu riêng; {checked} phép tính trực tiếp, {sum(map(len,expected.values()))} đáp án neo, nhớ cộng/nhân, đổi qua 0 và SVG 19 ô tô.')
