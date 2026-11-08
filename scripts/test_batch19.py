"""Hồi quy có kết quả tính độc lập và liệt kê khả năng lấy thẻ."""
import json
from pathlib import Path
from itertools import combinations,product
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
lessons={n:json.loads((ROOT/f'content/toan/tap-2/TOAN3_T2_B{n}.json').read_text()) for n in range(73,77)}
def check(n,q,expected):
    actual=lessons[n]['practice'][q-1]['correct_answer']
    assert actual==str(expected),(n,q,actual,expected)
# Tính từ dữ kiện, không lấy lời giải làm chuẩn.
for q,v in {13:14-9,18:16+18,21:28-9-8,22:5+9,23:30-23,24:(18+12+15)//3,25:40-11-8-14,26:31+29+32,27:6+3,28:10+9+6-24,29:20-4,30:14+9+7-5,33:8+6,34:17+15-2,35:(24+8)//4,36:12-9,37:18-3+22,38:7+6,39:(16-12)//2,40:3*4}.items():check(73,q,v)
# Les mêmes objets ne peuvent pas être pris deux fois sans remise.
for q,bag,k,predicate in [(14,['R','R','B'],2,lambda xs:xs==('B','B')),(23,['V','V','V','J'],3,lambda xs:'V' in xs),(25,[1,2,3],2,lambda xs:sum(xs)==6),(30,['J']*4+['R'],2,lambda xs:set(xs)=={'J','R'}),(37,['C','S','S','S'],2,lambda xs:xs==('C','C'))]:
    cases=list(combinations(bag,k));flags=[predicate(x) for x in cases]
    expected='có' if (all(flags) if q==23 else any(flags)) else 'không'
    check(74,q,expected)
check(74,31,'có' if any(sum(x)==4 for x in product([1,2],repeat=2)) else 'không')
check(74,34,min(map(sum,combinations([2,4,6],2))))
for q,v in {21:30-12-10,22:13-10,23:4+7,24:16-2,26:11+9+7,27:'có' if 6+4>8 else 'chưa',28:22-20,29:(8+7+9)//6,30:32-19,31:1,32:28-10-9-8,33:6+9,35:15-(25-15),36:(9+8+11)*2,37:12-2}.items():check(75,q,v)
check(75,25,'7 giờ' if 10+3>14-3 else '8 giờ')
check(75,40,'đã đạt' if 12>24/2 else 'chưa')
for q,v in {1:40000+2000+300+5,3:6*1000,4:9999+1,5:50000-1,7:len(str(85000)),9:min([67009,67090,67900,67909]),10:90000+700+2,12:24800+100,13:4,14:sorted([19005,19500,19050])[1],16:round(4728/10)*10,17:len([x for x in range(7001,10000) if x%1000==0]),18:str(40607).count('0'),19:35408-30000-5000-8,24:29998+3,25:9990+10,26:min([25000,20500,25050]),28:len(range(9998,10001)),29:len(range(45001,45006)),30:next(x for x in range(72151,72300) if x%100==0),32:60000+900+30,36:37000,37:min([18240,18420,18042]),39:19998,40:48000+3*1000}.items():check(76,q,v)
from itertools import permutations
check(76,21,min(int(''.join(x)) for x in permutations('0258') if x[0]!='0'))
check(76,22,max(int(''.join(x)) for x in permutations('1369')))
check(76,33,max(int(''.join(x)) for x in permutations('0123456789',4) if x[0]!='0' and x[-1]=='0'))
check(76,34,min(int(''.join(x)) for x in permutations('0123456789',5) if x[0]=='3'))
allqs=[q['question'] for d in lessons.values() for q in d['practice']]
assert len(allqs)==len(set(allqs))==160
for d in lessons.values():
    assert d['status']=='AI_CHECKED_AWAITING_TEACHER' and not d['verification']['teacher_approved']
    for q in d['practice']:
        if 'figure' in q:
            fig=ROOT/q['figure']['path'];root=ET.parse(fig).getroot()
            assert root.attrib.get('viewBox') and root.find('{http://www.w3.org/2000/svg}title') is not None
            assert fig.name in (ROOT/f"content/toan/tap-2/{d['id']}.md").read_text()
assert len([q for d in lessons.values() for q in d['practice'] if 'figure' in q])==3
print('PASS Batch 19: số liệu, khả năng lấy thẻ, cấu tạo số và 3 SVG; 160 câu riêng.')
