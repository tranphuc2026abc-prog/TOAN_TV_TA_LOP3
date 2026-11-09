"""Thử nhánh ngôn ngữ bằng fixture, không tính là học liệu xuất bản."""
from copy import deepcopy
from content_policy import validate_subject

def rejects(obj):
    try:validate_subject(obj)
    except (AssertionError,KeyError):return
    raise AssertionError('Dữ liệu thiếu phải bị từ chối')

# Fixture giả lập cấu trúc, không dùng làm nội dung bài đọc.
tv={'subject':'tv','reading':{'summary':'Tóm tắt thử','characters_or_images':['Nhân vật thử'],'message':'Thông điệp thử'},'source':{'printed_pages':[1,2],'review':'Dữ liệu thử'},'language_practice':{'vocabulary':['từ thử'],'sentences':['câu thử'],'spelling':['âm thử'],'expression':['nói thử']},'practice':[{'skill':'reading','evidence':'Chi tiết thử'}],'assessment':{'session_size':1}}
validate_subject(tv) # Không bắt có 40 câu hoặc difficulty của Toán.
for key in ['vocabulary','sentences','spelling','expression']:
    bad=deepcopy(tv);bad['language_practice'][key]=[];rejects(bad)
for key in ['summary','characters_or_images','message']:
    bad=deepcopy(tv);bad['reading'][key]=[];rejects(bad)
bad=deepcopy(tv);bad['practice'][0].pop('evidence');rejects(bad)
bad=deepcopy(tv);bad['assessment']['session_size']=2;rejects(bad)
math={'subject':'toan','practice':[{'difficulty':level} for level,count in [('nhan_biet',10),('thong_hieu',10),('van_dung',20)] for _ in range(count)],'assessment':{'session_size':10,'distribution':{'nhan_biet':3,'thong_hieu':3,'van_dung':4}}}
validate_subject(math)
bad=deepcopy(math);bad['practice'].pop();rejects(bad)
bad=deepcopy(math);bad['assessment']['distribution']['nhan_biet']=4;rejects(bad)
print('PASS policy: Tiếng Việt không ép 40 câu; thiếu căn cứ/nhóm luyện tập bị từ chối; Toán giữ 10/10/20 và 3/3/4.')

# Một câu có căn cứ không được che khuất câu đọc hiểu khác thiếu căn cứ.
bad=deepcopy(tv);bad['practice'].append({'skill':'reading','evidence':'  '});rejects(bad)
for size in [0,-1,True,0.5]:
    bad=deepcopy(tv);bad['assessment']['session_size']=size;rejects(bad)
print('PASS: mọi câu đọc hiểu cần căn cứ; số câu/lượt là số nguyên dương, không chấp nhận bool.')
