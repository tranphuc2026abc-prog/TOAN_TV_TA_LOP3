"""Đáp án tính độc lập của bài ôn chung cuối năm."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'content/toan/tap-2/TOAN3_T2_B81.json').read_text())
expected={1:60000+3000+8,2:4*1000,3:30000-1,4:min([41205,42105,41025,42015]),5:23000+16000,6:80000-35000,7:1200*5,8:36000//4,9:4*1000,10:6*4,11:50000+700+40+9,12:25000-6000+8000,13:3600*(9-6),14:(4200+1800)//6,15:500*2+100,16:55-15,17:8*5,18:20//4,19:'không',20:19000,21:1450+1450*3,22:6000*5-12500,23:70000-3*18000-9500,24:45000-5*1200,25:12500+12500-1800,26:(36//4)**2,27:(6+6*3)*2,28:2500-850,29:5000-6*500,30:20+25,31:(74+8)//9,32:74//9,33:28046-28000,34:24000+16000,35:(150-65)-65,36:8*12-7,37:72//8,38:35000-2000+2000,39:2350-420,40:(16000-4*2500)//3}
for i,v in expected.items():assert d['practice'][i-1]['correct_answer']==str(v),(i,v)
assert len({q['question'] for q in d['practice']})==40
assert d['status']=='AI_CHECKED_AWAITING_TEACHER' and not d['verification']['teacher_approved']
print('PASS Batch 21: 40 đáp án độc lập, chuyển giờ, phần dư, tiền, đơn vị và hình học.')
