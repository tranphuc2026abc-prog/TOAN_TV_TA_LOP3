"""Hồi quy giờ/lịch bằng datetime-calendar, bài toán tiền và biểu thức có ngoặc."""
import json,re,ast,operator,calendar,datetime,math,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
objects={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(65,69)}
seen=set();direct=0
ops={ast.Add:operator.add,ast.Sub:operator.sub}
def calc(n):
 if isinstance(n,ast.Constant) and type(n.value) is int:return n.value
 if isinstance(n,ast.BinOp) and type(n.op) in ops:return ops[type(n.op)](calc(n.left),calc(n.right))
 raise ValueError('Biểu thức ngoài phạm vi kiểm tra.')
for num,o in objects.items():
 assert o['lesson_no']==num and o['volume']==2 and o['status']=='AI_CHECKED_AWAITING_TEACHER'
 assert not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen,(num,q['question']);seen.add(q['question'])
  m=re.fullmatch(r'Tính ([0-9+() -]+)\.',q['question'])
  if m:assert int(q['correct_answer'])==calc(ast.parse(m[1],mode='eval').body),q['question_id'];direct+=1
 assert len(o['practice'])==40
 assert o['source']['printed_pages']=={65:[76,76],66:[77,80],67:[81,84],68:[85,87]}[num]
def plus(h,m,delta):
 d=datetime.datetime(2026,6,1,h,m)+datetime.timedelta(minutes=delta)
 return f'{d.hour}:{d.minute:02}'
def elapsed(h,m,hh,mm):return (datetime.datetime(2026,6,1,hh,mm)-datetime.datetime(2026,6,1,h,m)).seconds//60
expected={65:{1:24000+5000,2:67000-3000,3:21345+12524,4:76548-32126,5:'trước',6:'đơn vị',7:45987,8:0,9:9999+1,10:100000-1,11:25000+7000-12000,12:90000-(25000+15000),13:60000-(28000-8000),14:32678+4789,15:50003-17865,16:26789+14567,17:(56348+27176)%10,18:(62403-18257)%10,19:17500+2500+30000,20:'có',21:24500+8500-17250,22:18640+3275-4915,23:27450*2-3850,24:12875*2+2250,25:30000-15480-12620,26:75000-38675,27:50000-18500-12500,28:42860-9875+2015,29:64520-23560-17440,30:40000-15785-14315,31:28000-1750+750,32:41000+6000-2000,33:(72000-15000+3000)-(72000-15000-3000),34:45826+37,35:8,36:52780-51870,37:(32560-500)-(31240+500),38:85000-24500-(24500-1500),39:99999-1023,40:12000+18500+9500-27500},
66:{1:60,2:24,3:12,4:calendar.monthrange(2026,4)[1],5:calendar.monthrange(2026,7)[1],6:29,7:30,8:45,9:3,10:'4:25',11:42,12:'7:30',13:'6:40',14:10,15:12,16:5,17:8,18:18+27,19:4*3,20:60-47,21:plus(7,15,30),22:elapsed(19,20,19,55),23:plus(10,50,20),24:plus(8,5,-15),25:35*2+10,26:30,27:9,28:3,29:5,30:'đúng',31:elapsed(6,45,7,10),32:plus(16,35,40),33:'sai',34:sum(calendar.monthrange(2026,m)[1]==30 for m in range(1,13)),35:sum(calendar.monthrange(2026,m)[1]==31 for m in range(1,13)),36:62,37:10,38:plus(11,58,5),39:elapsed(8,0,10,30),40:80-75},
67:{1:'thứ hai',2:7,3:30,4:'thứ sáu',5:3,6:'9:10',7:'thứ bảy',8:7,9:10,10:'thứ hai',11:22,12:'có',13:13-10+1,14:26,15:35//5,16:4,17:'thứ ba',18:'5:05',19:elapsed(10,20,10,55),20:30,21:plus(10,35,40),22:plus(11,48,9),23:elapsed(14,45,15,20),24:28-22+1,25:12,26:15,27:'không',28:elapsed(15,0,15,15),29:plus(7,30,-20-15),30:5,31:29,32:1,33:5,34:plus(9,10,50),35:plus(8,15,20+25+10),36:16+10-1,37:plus(18,40,45),38:2,39:'thứ ba',40:plus(13,25,-15)},
68:{1:2*10000,2:50000//10000,3:100000//50000,4:3*2000,5:20000+5000,6:5000,7:10000-4000,8:1,9:5000+2000,10:20000,11:2,12:12000+3000,13:20000//5000,14:'có',15:6000-5000,16:2*8000,17:(50000-10000)//20000,18:'có',19:30000-28000,20:'sai',21:50000-23500,22:3*5000+12000,23:100000-45000-28000,24:18000+22000+7000,25:80000-47000,26:20000//2000,27:2*20000+10000-46500,28:24000//4,29:18500-17000,30:(50000-12000-8000)//5000,31:5*10000//5000,32:4*10000-20000-3*5000,33:30000//7000,34:30000-4*7000,35:19000-16000,36:36000//2*3,37:100000-38000-47500,38:3,39:15000+20000+25000-48000,40:60000-2*20000-5*2000}}
for num,cases in expected.items():
 for i,value in cases.items():assert objects[num]['practice'][i-1]['correct_answer']==str(value),(num,i,value)
# Kiểm tra các câu tra lịch với calendar chuẩn và kiểm tra vị trí từng ô SVG.
ns={'s':'http://www.w3.org/2000/svg'}
root=ET.parse(R/'content/toan/tap-2/TOAN3_T2_B67_CALENDAR.svg').getroot()
labels={t.text:(float(t.attrib['x']),float(t.attrib['y'])) for t in root.findall('s:text',ns) if (t.text or '').isdigit()}
assert len(labels)==30
for week,row in enumerate(calendar.monthcalendar(2026,6)):
 for col,day in enumerate(row):
  if day:assert labels[str(day)]==(col*90+45,83+week*43+29)
# So sánh tọa độ kim trong SVG với thời gian đề bài, gồm phần dịch kim giờ theo phút.
for filename,centers in [('TOAN3_T2_B66_CLOCKS.svg',[(110,4,25),(320,8,47),(530,11,58)]),('TOAN3_T2_B67_CLOCK.svg',[(120,9,10)])]:
 root=ET.parse(R/'content/toan/tap-2'/filename).getroot()
 lines=root.findall('.//s:line',ns)
 for cx,h,m in centers:
  for color,angle,length in [('#1565c0',m*6,74),('#c62828',(h%12)*30+m/2,47)]:
   line=next(t for t in lines if t.attrib.get('stroke')==color and float(t.attrib['x1'])==cx)
   a=math.radians(angle)
   assert abs(float(line.attrib['x2'])-(cx+length*math.sin(a)))<.02
   assert abs(float(line.attrib['y2'])-(110-length*math.cos(a)))<.02
for q in objects[67]['practice']:
 if 'lịch tháng 6 trong hình' in q['question'] or 'Đồng hồ D trong hình' in q['question']:assert q.get('figure')
for i in [10,20,38]:assert objects[66]['practice'][i-1].get('figure')
assert len(seen)==160
print(f'PASS Batch 17: {direct} biểu thức, {sum(map(len,expected.values()))} đáp án neo; datetime, lịch đủ 30 ô, kim giờ/phút, tham chiếu hình, tiền thừa và hai bước.')
