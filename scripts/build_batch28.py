import json
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=R/'content/system/drafts'
def rd(n):return json.loads((D/n).read_text())
b=[rd('BATCH28_B25_SOURCE.json'),rd('BATCH28_B25_B26_SOURCE.json')['b26'],rd('BATCH28_B26_B27_SOURCE.json')['b27'],rd('BATCH28_B27_B28_SOURCE.json')['b28']]
# Câu mới: kỹ năng|đề|đúng|ba nhiễu|giải thích.
rows=[
[
'vocabulary|Đảm đương việc khó nghĩa là gì?|Nhận trách nhiệm và gánh vác việc ấy.|Chỉ đứng nhìn;Đẩy hết việc cho người khác;Bỏ đi khi việc chưa xong|Tên cố Đương gắn với tinh thần sẵn sàng gánh vác.',
'vocabulary|Sờn lòng trước việc nặng nhọc là trạng thái nào?|Nản chí, muốn thôi cố gắng.|Vui vì hoàn thành;Tự nguyện giúp đỡ;Bàn cách hợp tác|Cố Đương không sờn lòng nghĩa là ông vẫn kiên trì.',
'sentences|Câu nào nêu việc làm giúp dân xóm đi lại?|Cố Đương ghép đá thành bậc lên núi.|Núi rất cao.;Xóm nằm dưới núi.;Bão thật dữ dội!|Ghép đá là hành động tạo lối đi, khác câu tả cảnh.',
'sentences|Câu nào giải thích đúng sự thay đổi của dân xóm?|Thấy ông kiên trì, nhiều người đến cùng làm.|Dân xóm luôn làm đường từ đầu.;Ông bỏ việc nên dân bỏ theo.;Ai cũng chỉ muốn đi đánh cá.|Câu gắn nguyên nhân với việc người dân tự nguyện giúp.',
'spelling|Điền tiếng đúng: Mọi người cùng ... đá làm đường.|chuyển|truyển;chuyễn;truyễn|Chuyển viết ch và dấu hỏi, chỉ đưa từ nơi này tới nơi khác.',
'spelling|Chọn từ viết đúng để tả sườn núi cao dốc.|Dựng đứng.|Dựng đứn.;Dựng đướng.;Dựng đưng.|Đứng có vần ưng; cụm từ gợi độ dốc lớn.',
'expression|Kể lại việc làm đường nên sắp xếp ý nào trước?|Bão làm dân mất thuyền nên phải lên núi kiếm củi.|Cả xóm đặt tên mới cho ông.;Con đường đã hoàn thành.;Mọi người đi lại dễ dàng.|Nêu hoàn cảnh trước giúp hiểu vì sao cần con đường.',
'expression|Muốn giới thiệu cố Đương thuyết phục, em nên nêu gì?|Việc ông kiên trì làm và lợi ích cho dân xóm.|Chỉ nói ông tốt rất nhiều lần.;Bịa ông xây cả thành phố.;Chỉ đọc tên mọi ngọn núi.|Chi tiết cụ thể giúp nhận xét có căn cứ.'
],
[
'vocabulary|Cặp từ nào trái nghĩa khi nói về ánh sáng khu rừng?|Tối tăm – sáng sủa.|Ẩm ướt – ướt át.;Lạnh – rét.;Cao – cao vút.|Hai từ chỉ hai đặc điểm đối lập về ánh sáng.',
'vocabulary|Từ nào trái nghĩa với dũng cảm trong tình huống nhận việc khó?|Nhút nhát.|Can đảm.;Mạnh dạn.;Gan dạ.|Nhút nhát đối lập với sự mạnh dạn trước khó khăn.',
'sentences|Đóng vai gõ kiến, lời nào là đề nghị lịch sự?|Bạn cùng chúng tôi tìm ánh sáng cho rừng nhé!|Rừng đang rất tối.;Ai đã tới đây?;Tôi là gõ kiến.|Lời nhờ dùng nhé và nêu rõ việc mong bạn làm.',
'sentences|Câu nào động viên gà trống cố gắng?|Bạn hãy bám chắc, chúng tôi tin bạn!|Gà trống có đôi chân.;Mặt trời ở đâu?;Khu rừng có cây chò.|Câu khiến có hãy nhằm động viên thực hiện hành động.',
'spelling|Tên riêng nào viết đúng theo phần luyện chữ L?|Lam Sơn|lam Sơn;Lam sơn;lam sơn|Tên riêng viết hoa chữ đầu mỗi tiếng.',
'spelling|Chọn tiếng đúng: Gà trống ... chặt ngón chân vào thân cây.|quặp|quạp;quập;quắp|Quặp chỉ động tác co, móc chặt để bám trong ngữ cảnh này.',
'expression|Nhận xét thích gà trống nào có lí do rõ?|Em thích gà vì gà vượt gió lạnh để giúp các bạn.|Em thích vì rất thích.;Gà là gà nên em thích.;Em thích công vì công đã đi tìm nắng.|Lí do dựa đúng việc gà làm cho cộng đồng.',
'expression|Khi kể chuyện rồi nói về mặt trời ngoài đời, em cần phân biệt gì?|Chi tiết tưởng tượng với hiện tượng thật.|Mọi chi tiết truyện đều là khoa học.;Gà quyết định giờ mặt trời mọc.;Chim biết điều khiển các vì sao.|Câu chuyện dùng tưởng tượng để ca ngợi tinh thần giúp mọi người.'
],
[
'vocabulary|Xe chỉ nghĩa là làm gì?|Xoắn các sợi nhỏ thành sợi lớn hơn.|Cắt tấm vải thành áo.;Trải vải trên bàn.;Vạch đường lên vải.|Xe chỉ là phần việc của tằm trong truyện.',
'vocabulary|Từ nào hợp với việc các bạn góp sức làm áo?|Hợp tác.|Tranh giành.;Xa lánh.;Phá phách.|Các bạn chia việc và phối hợp để cùng đạt kết quả.',
'sentences|Câu nào nêu đúng hai việc theo trình tự làm áo?|Ốc sên kẻ vạch rồi bọ ngựa cắt theo vạch.|Bọ ngựa may còn chim cắt.;Tằm trải vải rồi thỏ xe chỉ.;Nhím cắt vải trước khi có vạch.|Có vạch kích thước trước giúp cắt phù hợp.',
'sentences|Muốn hỏi bạn đã làm phần việc nào trong nhóm, em nói thế nào?|Bạn phụ trách việc gì trong nhóm?|Nhóm mình rất vui!;Bạn làm tốt lắm.;Chúng ta cùng làm nhé!|Câu hỏi tìm thông tin về trách nhiệm, không chỉ bộc lộ cảm xúc.',
'spelling|Điền tiếng đúng: Các bạn ... nghe nhím bàn cách may áo.|lắng|nắng;lắn;nắn|Lắng nghe viết l, chỉ chú ý nghe người khác.',
'spelling|Câu nào phân biệt đúng đỗ và đổ?|Tằm nghỉ cạnh rổ đỗ, nhím đổ nước ra chậu.|Tằm nghỉ cạnh rổ đổ, nhím đỗ nước.;Rổ đổ còn nước đỗ.;Hai tiếng luôn thay được nhau.|Đỗ là hạt cây; đổ là làm chất chứa chảy ra, cần giữ dấu đúng.',
'expression|Kể hoạt động tập thể rõ nhất cần có phần nào?|Việc chung, phần việc của em và kết quả.|Chỉ kể tên nhóm.;Chỉ nói vui quá.;Chỉ kể việc của nhóm khác.|Người nghe cần hiểu em tham gia như thế nào và đạt điều gì.',
'expression|Bạn nói ý tưởng chưa rõ, cách phản hồi nào giúp hợp tác?|Hỏi lại điều chưa hiểu rồi cùng bàn cách làm.|Cắt lời để chê ngay.;Im lặng bỏ phần việc.;Tự đổi việc của bạn không báo.|Hỏi và lắng nghe giúp hiểu đúng, phối hợp tốt hơn.'
],
[
'vocabulary|Nhóm nào ghép đúng người làm nghề và công việc?|Điều dưỡng – chăm sóc bệnh nhân.|Phi công – trồng lúa.;Nông dân – lái máy bay.;Bác sĩ – lái tàu hoả.|Công việc chăm sóc người bệnh gắn với điều dưỡng.',
'vocabulary|Song hành trong hình ảnh đường sắt nghĩa là gì?|Đi song song bên nhau.|Cắt nhau ở mọi điểm.;Chỉ có một đường.;Uốn thành vòng tròn kín.|Hai đường ray được gợi bằng nét song song kéo dài.',
'sentences|Câu nào hỏi lí do bé yêu việc học?|Vì sao bé thích khám phá qua sách?|Bé thích đọc sách.;Bé đang đi học à?;Bé đến trường lúc mấy giờ?|Vì sao dùng hỏi nguyên nhân, khác hỏi thời gian hoặc xác nhận.',
'sentences|Chuyển câu Bố làm nghề xây dựng thành câu hỏi về nghề, chọn câu nào?|Bố làm nghề gì?|Bố làm ở đâu?;Bố đi làm lúc nào?;Bố có khoẻ không?|Gì thay cho thông tin tên nghề cần tìm.',
'spelling|Cách viết nào đúng tên một nghề trong bài thơ?|Hải quân.|Hãi quân.;Hải quâng.;Hãi quâng.|Hải có dấu hỏi, quân có vần uân.',
'spelling|Điền từ đúng: Bố làm việc trên ... cao.|giàn giáo|dàn dáo;ràn ráo;giàng giáo|Giàn giáo là kết cấu hỗ trợ thợ xây làm việc trên cao.',
'expression|Nói về con đường học tập, ý nào phù hợp nhất?|Em tới trường, đọc sách để biết thêm nhiều điều.|Em chỉ tìm đường ô tô trong sách.;Em không cần học nghề nào.;Em cho rằng chỉ một nghề có ích.|Con đường của bé gợi hành trình khám phá kiến thức.',
'expression|Viết về nhân vật mình yêu thích cần chọn chi tiết thế nào?|Một hành động đúng truyện và điều em cảm phục.|Một thành tích tự bịa.;Tên nhân vật lặp nhiều lần.;Một chuyện không liên quan.|Nhận xét có căn cứ giúp người đọc hiểu lí do của em.'
]]
wr=[
[['Dân thích đổi nghề cho vui.','Không còn cây trong rừng.','Biển không có cá từ trước.'],['Từ cùng làm đến bỏ hết việc.','Từ quý ông đến ghét ông.','Ai cũng làm ngay từ đầu.'],['Chỉ một ngày.','Sau một buổi sáng.','Sau năm mươi năm.'],['Chê ông quá chậm.','Vì ông bỏ dở công việc.','Vì ông thích nhận quà.']],
[['Gà bỏ về vì sợ.','Gà ngủ dưới bụi cây.','Gà nhờ công thay mình.'],['Công đã dẫn cả đoàn đi.','Công là người gọi được nắng.','Gõ kiến không gặp công.'],['Mặt trời lặn.','Mưa kéo dài.','Cả rừng chìm trong nước.'],['Một vết thương do gió.','Một chiếc mũ mua ở chợ.','Đốm màu do gõ kiến vẽ.']],
[['Đã có đủ mọi người và dụng cụ.','Thỏ không muốn có áo.','Vải không thể cắt được.'],['Vì bọ ngựa định cắt cây.','Vì nhím muốn giấu vải.','Vì cả rừng không cần áo.'],['Thỏ xe chỉ, tằm cắt vải.','Chim kẻ vạch, nhím trải vải.','Bọ ngựa luồn kim, ốc sên cắt.'],['Chỉ một người làm được hết.','Mỗi người nên giữ tài riêng.','Không cần bàn bạc khi làm chung.']],
[['Nghề phi công.','Nghề nông.','Nghề xây dựng.'],['Cánh đồng và ruộng dâu.','Mây cao và sao trời.','Biển cả và đảo xa.'],['Sân bay có nhiều máy bay.','Đường sắt có hai đường ray.','Giàn giáo và nhà mới.'],['Bé chỉ muốn vẽ đường ô tô.','Bé không muốn tới trường.','Bé tìm cách bỏ hết sách.']]]
meta=[('Những bậc đá chạm mây',112,115,['Cố Đương','Dân xóm']),('Đi tìm mặt trời',116,119,['Gõ kiến','Gà trống','Mặt trời']),('Những chiếc áo ấm',120,123,['Thỏ','Nhím','Tằm','Bọ ngựa','Ốc sên','Chim ổ dộc']),('Con đường của bé',124,128,['Bé','Bố','Mẹ','Những người lao động'])]
rules=[['Kiên trì làm việc có ích có thể thuyết phục mọi người cùng góp sức.','Kể chuyện theo nguyên nhân, hành động, kết quả; không bỏ hoàn cảnh mất thuyền.'],['Gà trống dũng cảm vì nghĩ tới các bạn trong rừng.','Truyện tưởng tượng không thay thế giải thích khoa học về mặt trời mọc.'],['Mỗi bạn góp thế mạnh riêng để cả rừng có áo ấm.','Cần phối hợp theo thứ tự: trải, vạch, cắt rồi may.'],['Mỗi nghề có công việc và môi trường riêng, đều góp ích cho cuộc sống.','Con đường qua trang sách là hành trình khám phá kiến thức.']]
tasks=['Kể lại công việc làm đường bằng4 ý, rồi nói điều em cảm phục ở cố Đương.','Viết3 câu nêu lí do em thích gà trống, có một hành động làm căn cứ.','Kể một hoạt động nhóm thật: việc chung, phần em làm, kết quả và cảm nghĩ.','Viết đoạn nêu lí do em thích một nhân vật đã đọc, dẫn một chi tiết đúng truyện.']
for j,(src,m) in enumerate(zip(b,meta)):
 title,start,end,chars=m;ident=f'TV3_T1_B{25+j}';c=json.loads((R/'content/tieng-viet/tap-1/TV3_T1_B24.json').read_text())
 c.update(id=ident,title=title,lesson_no=25+j,topic='Cộng đồng gắn bó',objectives=['Kể và giải thích đúng chi tiết của '+title+'.','Dùng chi tiết nguồn làm căn cứ cho nhận xét.','Luyện từ, câu, chính tả và diễn đạt theo bài.'])
 c['source'].update(printed_pages=[start,end],pdf_pages=[start+1,end+1],review='Đã đọc trực quan nguồn qua các lượt trước; đối chiếu các ghi chú BATCH28 đã lưu. Lượt xuất bản dùng ghi chú, không nhận là đọc lại ảnh.')
 c['reading']=dict(summary=src['summary'],characters_or_images=chars,message=rules[j][0]);c['knowledge']=dict(introduction=src['summary'],rules=rules[j],steps=['Đọc bài trong sách.','Tìm chi tiết rồi mới kết luận.','Thực hành và đọc lại để sửa.'],common_errors=[['Nhầm nguyên nhân dân bỏ nghề cá.','Nói con đường xong ngay một ngày.'],['Đổi thứ tự ba tiếng kêu.','Coi tiếng gà là nguyên nhân khoa học tạo bình minh.'],['Đổi phần việc của các con vật.','Nói một bạn làm hết mọi công đoạn.'],['Nhầm đường sắt với đường bộ.','Hiểu con đường trong sách chỉ là lối đi thật.']][j])
 c['practice']=[]
 for n,q in enumerate(src['questions']):
  c['practice'].append(dict(question_id=f'{ident}_Q{n+1:02}',type='mcq',skill='reading',question=q['question'],correct_answer=q['answer'],options=[q['answer']]+wr[j][n],explanation=q['explanation'],evidence=q['evidence']))
 for row in rows[j]:
  s,q,a,w,e=row.split('|');n=len(c['practice'])+1;c['practice'].append(dict(question_id=f'{ident}_Q{n:02}',type='mcq',skill=s,question=q,correct_answer=a,options=[a]+w.split(';'),explanation=e))
 c['examples']=[dict(question=c['practice'][0]['question'],steps=[c['practice'][0]['evidence'],c['practice'][0]['explanation'],'Trả lời: '+c['practice'][0]['correct_answer']])]
 c['language_practice']={s:[q['question']+' Đáp án: '+q['correct_answer']+' '+q['explanation'] for q in c['practice'] if q['skill']==s] for s in ['vocabulary','sentences','spelling','expression']}
 c['activities']=[dict(title='Thực hành theo bài',materials=['Vở','Bút'],steps=[tasks[j],'Nói hoặc đọc cho người thân nghe, sửa một chỗ chưa rõ.'],check=['Đúng người, đúng việc.','Có lí do và chi tiết.','Câu rõ ý, đúng dấu kết câu.'])]
 c['games'][0].update(id=ident+'_GAME',title='Kho báu: '+title,question_ids=[q['question_id'] for q in c['practice']]);c['verification']['teacher_approved']=False;c['status']='AI_CHECKED_AWAITING_TEACHER'
 p=R/f'content/tieng-viet/tap-1/{ident}.json';p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 lines=['# '+title,c['status'],str(c['source']),*c['objectives'],src['summary'],*rules[j],*c['knowledge']['steps'],*c['knowledge']['common_errors']]
 for e in c['examples']:lines +=[e['question'],*e['steps']]
 lines+=c['activities'][0]['steps']+c['activities'][0]['check']
 for q in c['practice']:lines +=[q['question'],*q['options'],'Đáp án: '+q['correct_answer'],q['explanation'],q.get('evidence','')]
 lines +=[c['games'][0]['title'],*c['games'][0]['rules'],*map(str,c['assessment'].values()),*map(str,c['feedback'].values())]
 p.with_suffix('.md').write_text('\n\n'.join(lines)+'\n')
print('Batch28:4 bài,48 câu,4 game')
