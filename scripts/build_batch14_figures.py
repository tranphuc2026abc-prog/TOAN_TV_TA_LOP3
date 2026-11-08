"""Ba sơ đồ tự dựng cho phần luyện tập chu vi/diện tích."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'content/toan/tap-2'
def save(suffix,body,label):
 (R/f'TOAN3_T2_B53_{suffix}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="310" viewBox="0 0 440 310" role="img" aria-label="{label}"><rect width="440" height="310" rx="16" fill="#f8fafc"/><g font-family="sans-serif" font-size="18" text-anchor="middle" fill="#0f172a">{body}</g></svg>\n')
def text(x,y,t):return f'<text x="{x}" y="{y}">{t}</text>'
save('A','<rect x="85" y="85" width="270" height="90" fill="#bbf7d0" stroke="#166534" stroke-width="3"/><path d="M175 85V175M265 85V175" stroke="#64748b" stroke-width="2" stroke-dasharray="6 4"/>'+''.join(text(x,67,'12 cm') for x in [130,220,310])+text(42,135,'12 cm')+text(220,235,'Ba viên ghép sát; không chồng.'),'Ba viên vuông cạnh 12 cm ghép một hàng, cạnh chung là nét đứt')
save('B','<rect x="55" y="125" width="288" height="120" fill="#bfdbfe" stroke="#334155" stroke-width="2"/><rect x="55" y="53" width="96" height="72" fill="#fde68a" stroke="#334155" stroke-width="2"/>'+text(103,35,'4 cm')+text(25,95,'3 cm')+text(199,275,'12 cm')+text(378,190,'5 cm'),'Chữ nhật 12 nhân 5 cm, thêm chữ nhật 4 nhân 3 cm phía trên bên trái, không chồng diện tích')
body=''
for row in range(4):
 for col in range(5):
  empty=(row,col)==(1,2)
  body+=f'<rect data-unit-cell="1" data-painted="{0 if empty else 1}" x="{130+col*36}" y="{45+row*36}" width="36" height="36" fill="{"white" if empty else "#93c5fd"}" stroke="#334155" stroke-width="1.5"/>'
body+=text(220,235,'Mỗi ô là 1 cm². Ô trắng không tô.')
save('C',body,'Bảng bốn hàng năm cột ô vuông 1 cm², một ô trắng ở hàng thứ hai cột thứ ba; các ô khác tô xanh')
print('Đã dựng ba SVG mới.')
