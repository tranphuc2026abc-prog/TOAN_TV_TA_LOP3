"""Kiểm tra độc lập tình huống nhiều bước, đơn vị, thời gian và lấy thẻ."""
import json
from pathlib import Path
from itertools import combinations,product
from datetime import datetime,timedelta
R=Path(__file__).resolve().parents[1]
D={n:json.loads((R/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(77,81)}
def check(n,q,v):
 a=D[n]['practice'][q-1]['correct_answer'];assert a==str(v),(n,q,a,v)
for q,v in {21:15240+1260-850,22:50000-18500-12500,23:12650+12650-2350,24:60000-18750-16450,25:45000-16800-19200,26:5800+7200-12400,27:24860+17540,28:70500-2500,29:50000-28675,30:27000+27000+6000,31:3250+3250+750,32:30000+7600-18500,33:2026-2014,34:24500-9800-8700,35:99999-45678,36:7650-3280,37:18000-(40000-27500),38:3,39:(21800-1800)-(18200+1800),40:35000-12500-8700}.items():check(77,q,v)
for q,v in {11:12000//3*2,12:24000//(3*2),13:(3500+1500)*4,14:2106*4,15:42035//5,16:1250*8+3,21:36000//4*2,22:50000-12500*3,23:(43+7)//8,24:43//8,25:1850*4,26:7200-7200//3,27:36//9,28:95000//5*3,29:1000-6*125,30:8400*3//6,31:15000//5//3,32:28000//7*2,33:12400*3+6800,34:2304*4+2,35:7-5,36:1860//6//5,37:245*8+1040,38:5,39:18000-24000//4,40:90000-4*12000-3*9000}.items():check(78,q,v)
for q,v in {11:(9+4)*2,12:9*4,13:18//2,14:1000+250,15:3000+80,16:200-35,19:28//4,21:(7+7+5)*2,22:8*4-2,23:12*5-3*3,24:(8+4)*2,25:18+27,26:3000-4*250,27:2000//5,28:(85+75+40)//100,30:60-10,31:50000-28000-2*8500,32:3,33:34//2-11,34:6*4-8,35:1000+350-875,36:500+2*200,37:(1800-300)//3,38:32-2*5,39:16}.items():check(79,q,v)
def timecheck(q,start,mins):
 t=datetime.strptime(start,'%H:%M')+timedelta(minutes=mins);check(79,q,f'{t.hour} giờ {t.minute} phút')
timecheck(17,'08:20',30);timecheck(29,'09:45',35);timecheck(40,'07:50',25+10+15)
for q,v in {11:18+22,12:14+26,13:12-7,14:2*5000+3*2000,17:30-11-10-8,19:2,21:16+24+20,23:4*2000+10000-13000,24:12500+2*12500+15000,25:3,26:max(map(sum,combinations([2,5,8],2))),29:(16+12+20)*2,30:34+28-9,35:19-12,36:(32-11)-(50-32),38:(7+9+8)//4}.items():check(80,q,v)
check(80,15,'có' if any(x==('P','P') for x in combinations(['P','W','W'],2)) else 'không')
check(80,27,'có' if all('G' in x for x in combinations(['G','G','O'],2)) else 'không')
check(80,28,'có' if any(sum(x)==6 for x in product([1,3],repeat=2)) else 'không')
qs=[q['question'].strip().casefold() for d in D.values() for q in d['practice']];assert len(set(qs))==160
for d in D.values():assert not d['verification']['teacher_approved'] and d['status']=='AI_CHECKED_AWAITING_TEACHER'
print('PASS Batch 20: phép tính độc lập, thời gian, đo lường, tiền và tổ hợp lấy thẻ; 160 câu riêng.')
