"""Hình tự dựng: kim giờ dịch theo phút, lịch tháng 6/2026 từ calendar chuẩn."""
import math,calendar
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'content/toan/tap-2'
def clock(cx,cy,h,m,label):
 s=f'<g><circle cx="{cx}" cy="{cy}" r="88" fill="white" stroke="#253b61" stroke-width="3"/>'
 for i in range(60):
  a=math.radians(i*6);rr=78 if i%5==0 else 83
  s+=f'<line x1="{cx+rr*math.sin(a):.2f}" y1="{cy-rr*math.cos(a):.2f}" x2="{cx+87*math.sin(a):.2f}" y2="{cy-87*math.cos(a):.2f}" stroke="#253b61" stroke-width="{2 if i%5==0 else 1}"/>'
 for i in range(1,13):
  a=math.radians(i*30);s+=f'<text x="{cx+65*math.sin(a):.2f}" y="{cy-65*math.cos(a)+5:.2f}" text-anchor="middle" font-size="17">{i}</text>'
 for angle,length,color,width in [(m*6,74,'#1565c0',4),((h%12)*30+m/2,47,'#c62828',6)]:
  a=math.radians(angle);s+=f'<line x1="{cx}" y1="{cy}" x2="{cx+length*math.sin(a):.2f}" y2="{cy-length*math.cos(a):.2f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
 return s+f'<circle cx="{cx}" cy="{cy}" r="5" fill="#253b61"/><text x="{cx}" y="{cy+114}" text-anchor="middle" font-size="20" font-weight="bold">{label}</text></g>'
def svg(w,h,s):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="DejaVu Sans, sans-serif"><rect width="{w}" height="{h}" fill="#f3f7ff"/>{s}</svg>\n'
(R/'TOAN3_T2_B66_CLOCKS.svg').write_text(svg(640,260,''.join(clock(x,110,h,m,label) for x,h,m,label in [(110,4,25,'A'),(320,8,47,'B'),(530,11,58,'C')])))
(R/'TOAN3_T2_B67_CLOCK.svg').write_text(svg(240,260,clock(120,110,9,10,'D')))
s='<text x="315" y="32" text-anchor="middle" font-size="23" font-weight="bold">THÁNG 6 NĂM 2026</text>'
for i,t in enumerate(['T2','T3','T4','T5','T6','T7','CN']):s+=f'<text x="{45+i*90}" y="68" text-anchor="middle" font-size="20">{t}</text>'
for week,row in enumerate(calendar.monthcalendar(2026,6)):
 for col,day in enumerate(row):
  x=col*90;y=83+week*43
  s+=f'<rect x="{x}" y="{y}" width="90" height="43" fill="white" stroke="#b6c9e0"/>'
  if day:s+=f'<text x="{x+45}" y="{y+29}" text-anchor="middle" font-size="21" fill="{"#b71c1c" if col==6 else "#253b61"}">{day}</text>'
(R/'TOAN3_T2_B67_CALENDAR.svg').write_text(svg(630,310,s))
