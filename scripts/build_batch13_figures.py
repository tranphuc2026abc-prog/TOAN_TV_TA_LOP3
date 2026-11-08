"""SVG mới có số đo và ô đơn vị, không trích hình sách."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'content/toan/tap-2'
def save(name,body,w=430,h=300,label='Hình toán học'):
 (R/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}"><rect width="{w}" height="{h}" rx="16" fill="#f8fafc"/><g font-family="sans-serif" font-size="18" text-anchor="middle" fill="#0f172a">{body}</g></svg>\n')
def text(x,y,s):return f'<text x="{x}" y="{y}">{s}</text>'
save('TOAN3_T2_B50_triangle.svg','<path d="M80 210V90L240 210Z" fill="#cffafe" stroke="#0e7490" stroke-width="3"/>'+text(44,157,'6 cm')+text(160,240,'8 cm')+text(193,142,'10 cm')+text(215,278,'Sơ đồ; không dùng thước đo hình.'),label='Tam giác có cạnh trái 6 cm, cạnh dưới 8 cm, cạnh xiên 10 cm')
save('TOAN3_T2_B50_join.svg','<rect x="95" y="70" width="240" height="120" fill="#dbeafe" stroke="#1d4ed8" stroke-width="3"/><path d="M215 70V190" stroke="#64748b" stroke-width="2" stroke-dasharray="6 5"/>'+text(155,55,'4 cm')+text(275,55,'4 cm')+text(52,137,'4 cm')+text(215,245,'Cạnh chung ở bên trong'),label='Hai hình vuông mỗi cạnh 4 cm ghép sát theo một cạnh, cạnh chung nét đứt')
def cells(coords,x,y,size=34,color='#93c5fd'):
 return ''.join(f'<rect data-unit-cell="1" x="{x+a*size}" y="{y+b*size}" width="{size}" height="{size}" fill="{color}" stroke="#334155" stroke-width="1.5"/>' for a,b in coords)
A=[(0,0),(0,1),(0,2),(1,2),(2,2)];B=[(a,b) for a in range(4) for b in range(2)]
save('TOAN3_T2_B51_A.svg',cells(A,145,55)+text(215,205,'A: mỗi ô là 1 cm²'),label='Hình L có ba ô dọc và hai ô thêm bên phải ở hàng dưới')
save('TOAN3_T2_B51_B.svg',cells(B,145,65)+text(215,195,'B: mỗi ô là 1 cm²'),label='Hình B gồm hai hàng, mỗi hàng bốn ô 1 cm²')
save('TOAN3_T2_B51_AB.svg',cells(A,45,55)+cells(B,235,55,color='#86efac')+text(95,195,'A')+text(300,195,'B')+text(215,250,'Hai hình dùng cùng ô 1 cm²'),label='Hình A năm ô và hình B tám ô, tất cả ô có diện tích 1 cm²')
save('TOAN3_T2_B52_C.svg','<rect x="70" y="100" width="160" height="60" fill="#bfdbfe" stroke="#334155" stroke-width="2"/><rect x="230" y="100" width="100" height="60" fill="#bbf7d0" stroke="#334155" stroke-width="2"/>'+text(150,80,'8 cm')+text(280,80,'5 cm')+text(28,135,'3 cm')+text(215,230,'Ghép sát, không chồng diện tích.'),label='Hai hình chữ nhật 8 nhân 3 cm và 5 nhân 3 cm ghép sát theo cạnh 3 cm')
save('TOAN3_T2_B52_D.svg','<rect x="60" y="130" width="300" height="120" fill="#bfdbfe" stroke="#334155" stroke-width="2"/><rect x="60" y="40" width="90" height="90" fill="#fde68a" stroke="#334155" stroke-width="2"/>'+text(105,28,'3 cm')+text(210,280,'10 cm')+text(392,195,'4 cm')+text(28,91,'3 cm'),label='Chữ nhật dài 10 cm rộng 4 cm, ghép thêm hình vuông cạnh 3 cm ở phía trên bên trái, không chồng')
print('Đã dựng 7 SVG mới.')
