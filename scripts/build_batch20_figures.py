"""Dựng hình mới từ dữ kiện câu hỏi; không dùng ảnh sách."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'content/toan/tap-2'
OUT.mkdir(parents=True,exist_ok=True)
FIGURES={}
def save(n,q,title,body):
 name=f'TOAN3_T2_B{n}_Q{q:02}.svg'
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" role="img" aria-label="{title}"><title>{title}</title><rect width="640" height="300" rx="12" fill="#f0f9ff"/><g font-family="sans-serif" font-size="20" fill="#12334d">{body}</g></svg>'
 (OUT/name).write_text(svg+'\n')
 FIGURES[f'{n}:{q}']={'path':'content/toan/tap-2/'+name,'caption':title}
def rect(w,h,labelw,labelh):
 return f'<rect x="100" y="70" width="{w}" height="{h}" fill="#d5f5e3" stroke="#145a32" stroke-width="3"/><text x="{100+w/2}" y="55" text-anchor="middle">{labelw}</text><text x="{115+w}" y="{80+h/2}">{labelh}</text>'
for q in [11,12]:save(79,q,'Hình chữ nhật dài 9 cm, rộng 4 cm',rect(360,160,'9 cm','4 cm'))
save(79,7,'Hình vuông cạnh 3 cm',rect(180,180,'3 cm','3 cm'))
save(79,19,'Hình vuông: chu vi 28 cm, cạnh cần tìm',rect(180,180,'cạnh ?','chu vi 28 cm'))
save(79,21,'Vườn rộng 7 m, dài hơn rộng 5 m',rect(360,140,'7 m + 5 m','7 m'))
save(79,23,'Bìa 12 cm × 5 cm; cắt bỏ ô vuông cạnh 3 cm',rect(360,150,'12 cm','5 cm')+'<rect x="100" y="70" width="90" height="90" fill="#f9c3c3" stroke="#9d2929" stroke-dasharray="5 4"/><text x="145" y="120" text-anchor="middle">3 cm</text><text x="100" y="265">Phần hồng bị cắt bỏ.</text>')
save(79,24,'Hai hình vuông cạnh 4 cm ghép trọn một cạnh',rect(320,160,'4 cm + 4 cm','4 cm')+'<path d="M260 70v160" stroke="#a33" stroke-width="3" stroke-dasharray="6 4"/>')
save(79,33,'Hình chữ nhật: dài 11 cm, chu vi 34 cm',rect(330,150,'11 cm','rộng ?')+'<text x="100" y="260">Chu vi: 34 cm</text>')
save(79,38,'Hai tam giác chung cạnh 5 cm; tổng chu vi 32 cm','<path d="M80 220L280 55L470 220Z M280 55V220" fill="#d5f5e3" stroke="#145a32" stroke-width="3"/><path d="M280 55V220" stroke="#a33" stroke-width="4"/><text x="290" y="150">5 cm</text><text x="80" y="270">Tổng hai chu vi: 32 cm; hình không theo tỉ lệ.</text>')
save(79,39,'Đường kính 16 cm đi qua tâm O','<circle cx="310" cy="145" r="100" fill="white" stroke="#145a32" stroke-width="3"/><path d="M210 145H410" stroke="#a33" stroke-width="3"/><circle cx="310" cy="145" r="4"/><text x="300" y="135">O</text><text x="270" y="275">16 cm</text>')
# Bảng đúng dữ kiện Q21; chưa gắn vào bài khác.
body='<text x="60" y="35">Lượt mượn sách trong ba ngày</text>'
for row,cells in enumerate([['Buổi','Hai','Ba','Tư'],['Sáng','16','24','20'],['Chiều','18','21','15']]):
 for col,v in enumerate(cells):
  x=40+col*140;y=55+row*65
  body+=f'<rect x="{x}" y="{y}" width="140" height="65" fill="white" stroke="#456"/><text x="{x+70}" y="{y+40}" text-anchor="middle">{v}</text>'
save(80,21,'Bảng lượt mượn: hàng sáng 16, 24, 20; chiều 18, 21, 15',body)
(ROOT/'content/system/batch20-figures.json').write_text(json.dumps(FIGURES,ensure_ascii=False,indent=2)+'\n')
print('Đã dựng',len(FIGURES),'SVG; chưa tự tăng INDEX.')
