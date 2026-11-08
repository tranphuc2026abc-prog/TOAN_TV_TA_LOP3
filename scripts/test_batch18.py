"""Hồi quy mốc giờ, số nhớ/0 trong thương và thứ tự biểu thức."""
import json,re,ast,operator
from pathlib import Path
R=Path(__file__).resolve().parents[1]
objects={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(69,73)}
anchors={69:{12:25,14:105,15:12,16:27,17:32,21:35,22:30,23:55,24:'Chủ nhật',25:4,26:3,27:4,28:6,29:6,30:5000,31:18000,33:1,34:'thứ Sáu',35:11,36:5,37:15,38:5500,39:1500,40:'thứ Năm'},70:{11:64992,12:4,13:39021,16:5,18:5,21:50000,23:29500,24:40000,26:40000,27:60000,28:49800,29:1500,31:59500,32:70000,34:67500,35:6,36:7500,37:14520,38:56500,39:81000,40:80000},71:{5:5,11:0,12:2,13:2751,15:5,16:4,17:4,19:3200,20:1,21:15005,22:2500,23:4000,24:1,25:1,26:7500,27:6004,28:1100,29:1000,30:1,31:1,32:3000,33:5000,34:16402,35:6000,36:6000,37:7,38:33750,39:8001,40:'có'},72:{11:4000,12:64000,13:15000,16:20000,17:4200,18:35000,19:13000,20:75000,21:5000,22:21000,23:11600,24:24016,25:15000,26:8001,27:48000,28:45000,29:21000,30:15000,31:19500,32:64004,33:1965,34:7,35:9000,36:54000,37:55000,38:60000,39:7002,40:9250}}
# Bài 71 câu 11 hỏi chữ số bỏ sót, không phải giá trị thương.
ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def calc(n):
 if isinstance(n,ast.Constant):return n.value
 return ops[type(n.op)](calc(n.left),calc(n.right))
seen=set();checked=0
for n,o in objects.items():
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
  m=re.fullmatch(r'(?:Tính|Nhẩm) ([\d +×:()]+)\.',q['question'])
  if m:
   v=calc(ast.parse(m[1].replace('×','*').replace(':','/'),mode='eval').body)
   assert float(q['correct_answer'])==v,q['question_id'];checked+=1
 for i,v in anchors[n].items():assert o['practice'][i-1]['correct_answer']==str(v),(n,i,v)
assert len(seen)==160
print('PASS Batch 18:',checked,'biểu thức độc lập;',sum(map(len,anchors.values())),'đáp án neo; 160 câu riêng.')
