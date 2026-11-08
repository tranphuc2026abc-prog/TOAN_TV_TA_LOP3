"""SVG mới: bảng khảo sát, chuyển phiếu và tia số có khoảng 1 000."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'content/toan/tap-2'
def table(title,headers,values):
    out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 170" role="img" aria-label="{title}"><title>{title}</title><rect width="600" height="170" rx="12" fill="#f0f9ff"/><g font-family="sans-serif" font-size="19" text-anchor="middle" fill="#12334d"><text x="300" y="28">{title}</text>'
    for i,(h,v) in enumerate(zip(headers,values)):
        x=15+i*190
        out+=f'<rect x="{x}" y="45" width="190" height="100" fill="white" stroke="#396480"/><path d="M{x} 95h190" stroke="#396480"/><text x="{x+95}" y="77">{h}</text><text x="{x+95}" y="126">{v}</text>'
    return out+'</g></svg>'
figs=[(73,1,'Khảo sát cách đến trường',table('Cách đến trường (số bạn)',['Xe đạp','Đi bộ','Xe buýt'],[8,6,4])),(75,25,'Số phiếu trước khi ba bạn đổi giờ',table('Giờ đi: số phiếu trước khi đổi',['7 giờ','8 giờ','Tổng'],[10,14,24]))]
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 170" role="img" aria-label="Tia số từ 48000 đến 51000; mỗi khoảng 1000"><title>Tia số: mỗi khoảng 1 000</title><rect width="680" height="170" rx="12" fill="#f0f9ff"/><g font-family="sans-serif" text-anchor="middle" fill="#12334d" font-size="19"><text x="340" y="28">Mỗi khoảng: 1 000</text><path d="M45 90H640l-12 -7m12 7l-12 7" fill="none" stroke="#12334d" stroke-width="3"/>'
for i,label in enumerate(['48 000','49 000','50 000','B = ?']):
    x=80+170*i
    svg+=f'<path d="M{x} 80v20" stroke="#12334d" stroke-width="3"/><text x="{x}" y="130">{label}</text>'
svg+='<text x="80" y="65">A</text></g></svg>'
figs.append((76,40,'Tia số: A là 48 000, mỗi khoảng 1 000, B cách A ba khoảng',svg))
for num,qno,caption,svg in figs:
    ident=f'TOAN3_T2_B{num}'
    name=f'{ident}_Q{qno:02}.svg'
    (OUT/name).write_text(svg+'\n')
    p=OUT/(ident+'.json');d=json.loads(p.read_text());fig={'path':'content/toan/tap-2/'+name,'caption':caption}
    d['figures']=[fig];d['practice'][qno-1]['figure']=fig
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    p=OUT/(ident+'.md');s=p.read_text();needle=d['practice'][qno-1]['question'];s=s.replace(needle+'\n\n',needle+'\n\n!['+caption+']('+name+')\n\n');p.write_text(s)
print('Đã tạo 3 SVG và gắn trực tiếp câu hỏi.')
