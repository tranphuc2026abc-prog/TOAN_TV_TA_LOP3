"""Sơ đồ trung điểm và cây lựa chọn số, tự dựng từ dữ kiện bài mới."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'content/toan/tap-2'
def save(name,body,w,h,label):
 (R/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}"><rect width="{w}" height="{h}" rx="16" fill="#f8fafc"/><g font-family="sans-serif" font-size="18" text-anchor="middle" fill="#0f172a">{body}</g></svg>\n')
def text(x,y,t):return f'<text x="{x}" y="{y}">{t}</text>'
body='<rect x="100" y="80" width="240" height="240" fill="#dbeafe" stroke="#334155" stroke-width="3"/><circle cx="220" cy="80" r="6" fill="#b91c1c"/>'
for x,y,t in [(84,70,'A'),(356,70,'B'),(356,340,'C'),(84,340,'D'),(220,65,'I'),(220,30,'AB = 1840 m'),(220,373,'I là trung điểm AB.')]:body+=text(x,y,t)
save('TOAN3_T2_B58_A.svg',body,440,395,'Khu đất vuông ABCD, cạnh AB dài 1840 m, điểm I nằm chính giữa AB')
body='<path d="M280 285L110 185M280 285L410 185M410 185L320 65M410 185L500 65" fill="none" stroke="#475569" stroke-width="4"/>'
for x,y,t in [(110,185,'71240'),(410,185,'72140'),(320,65,'72500'),(500,65,'72450')]:
 body+=f'<rect x="{x-47}" y="{y-18}" width="94" height="36" rx="10" fill="white" stroke="#334155" stroke-width="2"/>'+text(x,y+6,t)
body+='<circle cx="280" cy="285" r="7" fill="#334155"/>'+text(280,323,'Xuất phát')+text(260,25,'Mỗi chỗ rẽ: chọn số lớn hơn')
save('TOAN3_T2_B60_B.svg',body,560,350,'Từ gốc có hai nhánh 71240 và 72140; nhánh 72140 lại chia thành 72500 và 72450')
print('Đã dựng 2 SVG mới.')
