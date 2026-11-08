"""Hồi quy làm tròn trực tiếp, cấu tạo số, nhớ/đổi qua 0 và bài toán hai bước."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
objects={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(61,65)}
def rounded(n,unit):return (n+unit//2)//unit*unit
seen=set();direct=0
for n,o in objects.items():
 assert o['lesson_no']==n and o['volume']==2
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
  m=re.fullmatch(r'Tính (\d+) ([+-]) (\d+)\.',q['question'])
  if m:
   a,b=int(m[1]),int(m[3]);v=a+b if m[2]=='+' else a-b
   assert q['correct_answer']==str(v),q['question_id'];direct+=1
  m=re.fullmatch(r'Làm tròn(?: trực tiếp)? (\d+) đến hàng (nghìn|chục nghìn)\.',q['question'])
  if m:assert int(q['correct_answer'])==rounded(int(m[1]),1000 if m[2]=='nghìn' else 10000)
expected={
61:{12:100000,14:40000,21:rounded(24681,1000),22:rounded(83129,10000),25:41500,26:42499,27:55000,28:64999,29:5,30:4,31:rounded(19450,1000),32:rounded(12480,1000)+rounded(12520,1000),33:rounded(45999,10000)-45999,34:rounded(75612,1000),35:31500,36:95000,37:rounded(61500,1000)-61500,38:25000,39:rounded(64900,10000),40:rounded(22840,1000)},
62:{1:42631,2:0,3:5000,4:80006,5:89999+1,6:60000-1,7:43400+100,8:max(71908,71890),9:rounded(67280,1000),10:rounded(76400,10000),11:45070,12:5,13:38990+10,14:min(52049,52094,52904),15:rounded(58210,1000),16:90480,17:40000,18:'<',19:28416-5000,20:34500,21:'A',22:60000+2000+10+5,23:97520,24:20579,25:39800+3*100,26:rounded(58460,1000),27:min(d for d in range(10) if 73102+10*d>73162),28:max(d for d in range(10) if 40980+1000*d<45000),29:65090,30:sorted([37240,37024,37402])[1],31:(56000+57000)//2,32:80000+12*100+4,33:30608,34:rounded(45949,10000),35:23510,36:10000,37:11111,38:97500+2*1000,39:sum(rounded(x,1000)==82000 for x in [82501,82499,83000,81999]),40:'B'},
63:{11:28976+11358,12:47508+92,13:39500+500,14:'không',15:20000+3000+400,17:99990+10,18:1,19:18400+2600,20:32140+75,21:12460+8315,22:16400+2500,23:12500+8900+3600,24:18350+12680,25:14800*2+1200,26:50000+20000+15000,27:5,28:9,29:4*5000+1850,30:24575+425,31:36000+1200,32:rounded(28400+19600,10000),33:15860+17240,34:12050+13950+8000,35:17500+8250+2250,36:23680+17450,37:1,38:12480*2+1520,39:100000-1,40:min(21400,24100)+min(18500,15800)},
64:{11:50302-17856,12:42000-6000,13:70000-25001,14:41111+17321,15:63040-95,16:1,17:56120-48,18:45300-2800,19:60005-29999,20:0,21:45280-18750,22:35820-32480,23:24000-8500-6700,24:18640-2350,25:12500-7800,26:100000-36500-12500,27:6,28:35000+1200+800,29:18000+500,30:24000-600,31:38200-17450-8650,32:13200-4600,33:65000-42750,34:50000-17890,35:(80000-12500)-(70000-3500),36:30000-12450-9875,37:16700,38:99999-1000,39:45000-28000-9400,40:rounded(70400-25600,1000)}}
for n,cases in expected.items():
 for i,v in cases.items():assert objects[n]['practice'][i-1]['correct_answer']==str(v),(n,i,v)
# Kiểm tra biên khoảng làm tròn và trường hợp làm tròn trực tiếp khác nhiều bước.
for a,b,middle,target in [(41500,42499,42000,42000),(55000,64999,60000,60000)]:
 unit=1000 if target==42000 else 10000
 assert rounded(a-1,unit)!=target and rounded(a,unit)==target
 assert rounded(b,unit)==target and rounded(b+1,unit)!=target
assert rounded(44999,10000)==40000 and rounded(rounded(44999,1000),10000)==50000
assert len(seen)==160
print(f'PASS Batch 16: 160 câu, {direct} phép tính trực tiếp, {sum(map(len,expected.values()))} đáp án neo; làm tròn trực tiếp/biên, cấu tạo số, có nhớ/đổi qua 0, bài toán hai bước.')
