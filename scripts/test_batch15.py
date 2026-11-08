"""Hồi quy phép chia, chứa hết/nhóm đầy, năm chữ số và so sánh giới hạn."""
import json,re,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
objects={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(57,61)}
seen=set();direct=0
for n,o in objects.items():
 assert o['volume']==2 and o['lesson_no']==n
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
  m=re.fullmatch(r'(?:Tính|Nhẩm) (\d+) ([+:×-]) (\d+)\.',q['question'])
  if m:
   a=int(m[1]);b=int(m[3]);op=m[2]
   if op==':':assert a%b==0;v=a//b
   elif op=='+':v=a+b
   elif op=='-':v=a-b
   else:v=a*b
   assert q['correct_answer']==str(v),q['question_id'];direct+=1
assert len(seen)==160
expected={57:{7:502*4+3,12:f'{4703//5} dư {4703%5}',13:6030//3,14:3210%8,15:2080//6,16:5004//6,17:8245%4,19:len(str(4080//4)),20:1867%3,21:3608//4,22:4523//6,23:(4523+5)//6,24:7400//8,25:6284//4,26:5290//5,27:5290-5290//5,28:1825//7,29:4872//6,30:2050%4,31:4500//3//5,32:6408//8-200,33:3225%4,34:5607//7,35:1980//9*2,36:3120//4+120,37:(9015+7)//8,38:(305*7+6+1)//7,39:1736//7-48,40:2825//5+35},58:{8:5501%5,11:(1500+2500)//4,12:1305*(7-3),13:2754//3,14:725*4,15:max(1240*3,7500//2),16:1620//3*2,17:4800-600*3,19:1000+2000//5,21:1450+1450*3,22:4*1250-875,23:4836//6+194,24:8400-8400//4,25:'B',26:1680//5,27:1200+840//4*3,28:8*30,29:1840//2,30:1840*4,31:1025*4-3900,32:4200//6,33:(7150-1150)//5,34:(3085+3)//4,35:9500-3*1250,36:(1500+2200+2300)//6,37:(3*2100-900)//3,38:(2016//8-152)*8,39:(1200*3-600)//5,40:3600//4//3},59:{3:8000,4:34027,7:29999+1,8:60000-1,9:10000//1000,10:len(str(100000)),16:6*10000+12*100,18:70000+2*10000,19:43680,20:58200,21:49998+3,22:20579,23:86410,24:8*10000+2*1000+9,25:48031,26:9,27:2*10000+30*100+4*10+6,28:79990+3*10,29:65424,31:69830,32:len(range(89998,90001)),33:50700,34:60950,35:95000-2*5000,36:10*10000,37:200,38:99999,39:10008,40:40000+5*1000},60:{11:max(72019,72100),12:4,13:8,14:sorted([39018,39108,38918])[1],15:min(65430,65340,65403),16:len(range(59999,60002)),17:10234,18:98765,19:71890,20:60000+100,21:max(45280,45820,45082),22:min(20805,20580,20850),23:sorted([78120,78021,78210])[1],24:max(x for x in [34999,35000,35001] if x<=35000),25:62045,26:87420,27:10569,28:max(d for d in range(10) if int(f'38{d}7{d}')<38575),29:max(56308,56083,56803),30:'không có',31:sorted([47320,47230,47302],reverse=True)[1],32:len([d for d in range(10) if 54010+100*d>54610]),33:min(d for d in range(10) if 52609+10*d>52688),34:49980,35:max(60815,68105,61085),36:min(80008,80800,88000),37:len(range(99999,100000)),38:72500,39:max(d for d in range(10) if 49990+d<49995),40:38000}}
for n,cases in expected.items():
 for i,value in cases.items():assert objects[n]['practice'][i-1]['correct_answer']==str(value),(n,i,value)
# Mô phỏng chia dài độc lập để bắt lỗi bỏ 0 ở trong/cuối thương.
def long_division(a,b):
 rem=0;out=''
 for c in str(a):
  current=rem*10+int(c);digit,rem=divmod(current,b)
  if out or digit:out+=str(digit)
 return int(out or '0'),rem
for a,b in [(8424,4),(7070,7),(6030,3),(4703,5),(4080,4),(5004,6),(9015,8)]:
 q,rem=long_division(a,b);assert (q,rem)==divmod(a,b) and q*b+rem==a and 0<=rem<b
for n in [58,60]:
 o=objects[n]
 for f in o['figures']:ET.parse(R/f['path'])
 assert o['practice'][28 if n==58 else 37]['figure']==o['figures'][0]
print(f'PASS Batch 15: 160 câu riêng; {direct} phép tính trực tiếp; {sum(map(len,expected.values()))} đáp án neo, thương có 0/số dư, chứa hết, mốc 100000, giới hạn và SVG.')
