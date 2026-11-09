"""Xuất bản TV13–16 từ các phần biên soạn đã lưu; không sửa bài trước."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
knowledge=json.loads((R/'content/system/drafts/BATCH25_KNOWLEDGE.json').read_text())['lessons']
reading=json.loads((R/'content/system/drafts/BATCH25_READING_QUESTIONS.json').read_text())['lessons']
# Mỗi dòng: kỹ năng, đề, đáp án, ba nhiễu, giải thích.
extra=[
[
('vocabulary','Mặt nước dập dềnh chuyển động thế nào?','Lên xuống nhịp nhàng','Bất động','Chạy trên bờ','Bay vào lớp','Dập dềnh gợi chuyển động lên xuống của nước.'),
('vocabulary','Từ rì rào gợi điều gì trong cảnh biển?','Âm thanh sóng nhỏ và đều','Màu đỏ của giấy','Kích thước thuyền','Độ dày sách','Đây là từ gợi âm thanh, khác từ tả màu hoặc kích thước.'),
('sentences','Câu nào nói rõ sự khéo léo của cô?','Cô cắt giấy nhanh và tạo hình rất đẹp.','Cô và rồi.','Giấy của nhưng.','Đẹp vì.','Câu đầy đủ nêu người và việc làm, kèm đặc điểm.'),
('sentences','Câu nào nói cảm xúc có lí do khi xem cô làm thủ công?','Em thích thú vì giấy màu thành một bức tranh biển.','Em có một bút chì.','Lớp em có cửa.','Tờ giấy ở trên bàn.','Câu nêu cảm xúc và chi tiết tạo nên cảm xúc.'),
('spelling','Điền l hoặc n: Cô ...àm một chiếc thuyền giấy.','l','n','r','d','Làm viết l; không viết nàm.'),
('spelling','Cặp tiếng nào đều đúng trong cảnh mặt trời buổi sớm?','nắng lên','lắng nên','nắng nên','lắng lên','Nắng chỉ ánh sáng mặt trời; lên chỉ hướng xuất hiện cao hơn.'),
('expression','Kể giờ thủ công rõ nhất nên thêm điều nào?','Việc em đã tự làm và cảm xúc khi hoàn thành','Chỉ lặp vui quá nhiều lần','Tên mọi đồ vật trong nhà','Một chuyện đi chợ không liên quan','Hoạt động và cảm xúc cụ thể giúp người nghe hiểu trải nghiệm.'),
('expression','Em chưa làm được sản phẩm đẹp. Cách kể nào phù hợp?','Kể điều còn khó và điều em muốn luyện thêm','Nhận sản phẩm của cô là mình làm','Bịa đã làm hoàn hảo','Chê bạn để tránh nói việc mình','Trung thực về khó khăn vẫn tạo câu chuyện có ý nghĩa.')],
[
('vocabulary','Giọng dõng dạc là giọng thế nào?','Rõ ràng, mạnh mẽ và chững chạc','Nhỏ đến không nghe được','Ngắt quãng vì ngủ','Lẫn mọi tiếng vào nhau','Dõng dạc tả cách nói rõ, có sự vững vàng.'),
('vocabulary','Mồ hôi lấm tấm nghĩa là gì?','Nhiều giọt nhỏ trên da','Da hoàn toàn khô','Một vũng nước trên sàn','Màu giấy đổi đỏ','Lấm tấm chỉ nhiều hạt hoặc giọt nhỏ trên bề mặt.'),
('sentences','Câu nào nêu hoạt động của Hoàng?','Hoàng đọc lại câu vừa viết.','Hoàng là học sinh.','Vở của Hoàng mới.','Chữ trên vở nhỏ.','Đọc lại là hoạt động; các câu kia giới thiệu hoặc tả đặc điểm.'),
('sentences','Đặt dấu nào sau câu Bạn đã đọc lại bài chưa','?','.',';',':','Câu nhằm hỏi thông tin nên kết thúc bằng dấu hỏi.'),
('spelling','Tên riêng nào viết đúng theo nội dung ôn chữ Ê?','Ê-đê','ê-đê','ê-Đê','Ê-ĐÊ','Tên trong bài viết hoa chữ đầu, các cách kia không theo dạng tên đã cho.'),
('spelling','Cách viết nào đúng đầu một câu kể?','Em đọc lại bài.','em đọc lại bài.','eM đọc lại bài.','em đọc lại bài','Câu cần viết hoa đầu và có dấu kết câu.'),
('expression','Khi giới thiệu sở thích, câu nào rõ ý?','Tớ thích đọc truyện về động vật.','Tớ thích vì và.','Sở thích của.','Tớ nhưng rồi.','Câu nêu người và sở thích cụ thể.'),
('expression','Sau khi viết thẻ giới thiệu, việc nào giúp bài rõ hơn?','Đọc lại, sửa từ chưa rõ và dấu câu','Chấm bất cứ nơi nào mỏi tay','Bỏ mọi dấu câu','Viết thêm thông tin riêng của bạn khác','Đọc lại nội dung là cách tránh lỗi giống Hoàng.')],
[
('vocabulary','Từ nào gọi người làm việc quản lí sách ở thư viện?','Thủ thư','Giá sách','Phiếu mượn','Đọc sách','Thủ thư là người; giá và phiếu là đồ vật, đọc là hoạt động.'),
('vocabulary','Từ nào chỉ hoạt động liên quan tới sách?','Mượn','Người đọc','Bàn','Thẻ','Mượn là việc làm, ba từ còn lại gọi người hoặc đồ vật.'),
('sentences','Câu nào nhắc trách nhiệm người mượn?','Em đọc xong rồi trả sách đúng hẹn.','Sách là của em mãi mãi.','Em xé trang mình thích.','Em giấu sách để bạn khỏi đọc.','Trả sách giúp người khác tiếp tục được sử dụng.'),
('sentences','Câu nào là câu hỏi về cuốn sách?','Bạn muốn mượn cuốn nào?','Em đang đọc.','Sách có tranh.','Thư viện mới đẹp.','Câu muốn biết lựa chọn của bạn là câu hỏi.'),
('spelling','Chọn từ đúng nghĩa quý trọng: ... trọng.','trân','chân','trăng','chăng','Trân trọng mang nghĩa quý trọng; không viết chân trọng.'),
('spelling','Từ nào viết đúng để gọi một quốc gia theo nghĩa đất nước?','đất nước','đất lước','đấc nước','đấc lước','Tiếng nước có n và đất có t; cần giữ đúng cấu tạo tiếng.'),
('expression','Gợi ý nào làm ước muốn về thư viện cụ thể hơn?','Em muốn có góc yên tĩnh và sách tranh dễ tìm.','Em muốn tốt và tốt.','Thư viện là thư viện.','Em không nói thêm gì.','Đặc điểm rõ ràng giúp người nghe hình dung thư viện mong muốn.'),
('expression','Bạn hỏi vì sao cần góp sách dùng chung. Em trả lời thế nào?','Để nhiều bạn có thêm sách lựa chọn và cùng đọc','Để không ai khác được đọc','Để sách biến thành ghế','Để khỏi phải trả sách đã mượn','Chia sẻ sách làm nguồn đọc phong phú hơn.')],
[
('vocabulary','Khao khát là mong muốn ở mức nào?','Tha thiết','Thờ ơ','Miễn cưỡng','Hoàn toàn không muốn','Khao khát chỉ mong muốn mạnh mẽ, tha thiết.'),
('vocabulary','Nhóm nào gồm những người gắn với thư viện?','Thủ thư, người đọc','Giá sách, bàn','Mượn, trả','Thẻ, phiếu','Thủ thư và người đọc gọi người, khác đồ vật và hoạt động.'),
('sentences','Câu nào bộc lộ sự vui mừng?','Buổi sinh hoạt vui quá!','Buổi sinh hoạt bắt đầu lúc ba giờ.','Em có một tờ giấy.','Ai đang nói?','Từ quá cùng dấu chấm than giúp bộc lộ cảm xúc.'),
('sentences','Chuyển câu Thư viện rộng thành câu cảm phù hợp.','Thư viện rộng biết bao!','Thư viện rộng lúc nào?','Thư viện là phòng đọc.','Thư viện có sách.','Biết bao diễn tả cảm xúc trước độ rộng, không chỉ cung cấp thông tin.'),
('spelling','Chọn cách viết đúng tên tổ chức được nhắc trong bài.','Đội Thiếu niên Tiền phong Hồ Chí Minh','đội thiếu niên tiền phong hồ chí minh','Đội thiếu niên tiền phong hồ chí minh','đội Thiếu niên tiền phong Hồ chí minh','Tên tổ chức và tên riêng cần viết hoa đúng dạng tên đã nêu.'),
('spelling','Câu nào viết hoa đầu câu và kết câu đúng?','Em vui khi được vào Đội.','em vui khi được vào Đội.','Em vui khi được vào Đội','em vui khi được vào đội','Câu kể cần viết hoa đầu và có dấu chấm; Đội là tên gọi tổ chức trong ngữ cảnh này.'),
('expression','Thông báo buổi chia sẻ sách còn thiếu gì nếu chỉ nêu tên hoạt động?','Thời gian, nơi, người tham gia và cách đăng kí','Một bài thơ dài bất kì','Thông tin riêng của tất cả bạn','Tên món ăn em thích','Người đọc cần thông tin để biết có thể tham gia thế nào.'),
('expression','Để nói ước mơ sau ngày vào Đội rõ hơn, em nên làm gì?','Nêu điều muốn cố gắng và việc cụ thể sẽ làm','Chỉ bảo khăn làm mọi việc thay em','Khẳng định không cần học nữa','Chép nguyên bài thơ thay ý mình','Ước mơ gắn hành động giúp lời nói thiết thực hơn.')]
]
for j,(k,r) in enumerate(zip(knowledge,reading)):
 c=json.loads((R/'content/tieng-viet/tap-1/TV3_T1_B12.json').read_text());id=k['id'];c.update(id=id,lesson_no=13+j,title=k['title'],objectives=k['objectives'])
 c['source'].update(printed_pages=k['source_pages'],pdf_pages=[p+1 for p in k['source_pages']],review='Đọc trực quan nguồn ở lượt trước; đối chiếu BATCH25_SOURCE_NOTES.md ngày10/11/2026. B16 chỉ trang70–73; không chép toàn văn.')
 c['knowledge']=dict(introduction=k['introduction'],rules=k['rules'],steps=['Đọc bài ở trang nguồn, đối chiếu phần tóm tắt.','Trả lời câu hỏi rồi xem căn cứ trong lời giải.','Làm nhiệm vụ viết và sửa theo tiêu chí.'],common_errors=k['common_errors']);c['examples']=k['examples']
 c['reading']=dict(summary=k['introduction'],characters_or_images=[['Cô giáo','Học trò và cảnh thủ công'],['Bác chữ A','Hoàng','Các dấu câu'],['Thầy hiệu trưởng','Các bạn học sinh'],['Người chị','Người em vào Đội','Khăn quàng đỏ']][j],message=k['rules'][1])
 c['practice']=[]
 for z,a in enumerate(r['questions']):c['practice'].append(dict(question_id=f'{id}_Q{z+1:02}',type='mcq',skill='reading',question=a['question'],correct_answer=a['answer'],options=[a['answer']]+a['wrong'],explanation=a['explanation'],evidence=a['evidence']))
 for row in extra[j]:
  skill,p,a,*rest=row;c['practice'].append(dict(question_id=f'{id}_Q{len(c["practice"])+1:02}',type='mcq',skill=skill,question=p,correct_answer=a,options=[a]+rest[:3],explanation=rest[3]))
 c['language_practice']={name:[q['question']+' Đáp án: '+q['correct_answer']+'. '+q['explanation'] for q in c['practice'] if q['skill']==skill] for name,skill in [('vocabulary','vocabulary'),('sentences','sentences'),('spelling','spelling'),('expression','expression')]}
 task=k['writing_task'];c['activities']=[dict(title='Thực hành theo bài',materials=['Vở','Bút'],steps=[task['prompt'],'Viết bằng lời và trải nghiệm của em.','Đọc lại, sửa ít nhất một điểm chưa rõ.'],check=task['check'])]
 c['games'][0].update(id=id+'_GAME',title=['Bức tranh giấy','Giúp Hoàng sửa câu','Góc đọc vui','Khăn đỏ và ước mơ'][j],question_ids=[q['question_id'] for q in c['practice']]);c['verification']['teacher_approved']=False;c['status']='AI_CHECKED_AWAITING_TEACHER'
 p=R/f'content/tieng-viet/tap-1/{id}.json';p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 lines=[c['title'],'Trạng thái: AI biên soạn và rà soát; chưa có xác nhận của giáo viên.',str(c['source']),*c['objectives'],k['introduction'],*k['rules'],*c['knowledge']['steps'],*k['common_errors']]
 for e in c['examples']:lines +=[e['question'],*e['steps']]
 for values in c['language_practice'].values():lines+=values
 lines +=c['activities'][0]['steps']+task['check']
 for q in c['practice']:lines +=[q['question'],*q['options'],'Đáp án: '+q['correct_answer'],q['explanation'],q.get('evidence','')]
 lines +=[c['games'][0]['title'],*c['games'][0]['rules'],*c['assessment'].values(),*c['feedback'].values()]
 p.with_suffix('.md').write_text('\n\n'.join(str(v) for v in lines)+'\n')
 print(id,len(c['practice']))
