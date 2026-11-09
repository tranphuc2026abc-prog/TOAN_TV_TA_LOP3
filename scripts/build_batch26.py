import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
# Nội dung mới biên soạn từ trang quét, không sao chép bài đọc.
data=[
('Ngưỡng cửa',82,85,['Bạn nhỏ','Bà và mẹ','Bố mẹ','Bạn bè'],
'Ngưỡng cửa gắn với những bước đi đầu đời, cuộc sống gia đình, tình bạn và ngày đi học. Từ nơi thân thuộc ấy, bạn nhỏ sẽ bước tới những hành trình mới.',
['Ngưỡng cửa là thanh dưới khung cửa ra vào; trong thơ còn gợi mái ấm và sự lớn lên.','Hình ảnh con đường xa gợi tương lai rộng mở, không chỉ một đoạn đường đo được.','Đọc chậm ở những hình ảnh bà, mẹ; giữ giọng trìu mến khi nói về mái nhà.'],
['Nhầm ngưỡng cửa với mái nhà.','Hiểu con đường xa chỉ là khoảng cách đến trường.','Kể thêm sự việc không có trong bài như bạn nhỏ bỏ nhà đi.'],
'Viết 3–4 câu về một góc nhà gắn với kỉ niệm của em. Nêu vị trí, một việc đã diễn ra và cảm xúc.',
[
('reading','Vì sao ngưỡng cửa gợi bước đầu trưởng thành của bạn nhỏ?','Nơi ấy gắn với lúc tập đi rồi bước tới trường.',['Vì đó là phần cao nhất ngôi nhà.','Vì nó tự đưa bạn đi xa.','Vì bạn chỉ đứng đó mà không lớn lên.'],'Các giai đoạn tập đi và đi học cho thấy bạn lớn dần.','Trang 82–83: hình ảnh tập đi và đường tới lớp.'),
('reading','Những ai giúp bạn nhỏ vượt qua bước đi đầu đời?','Bà và mẹ.',['Thủ thư và người đọc.','Cô bán hàng và khách.','Chỉ các bạn ở lớp.'],'Tình chăm sóc của bà, mẹ gắn với việc tập đi.','Trang 82: bà và mẹ giúp em tập đi.'),
('reading','Khi bạn bè tới chơi, ngưỡng cửa gắn với điều gì?','Niềm vui gặp gỡ.',['Một cuộc chia tay buồn.','Việc làm bài kiểm tra.','Một chuyến tàu ra biển.'],'Cảnh bạn bè tới vui chơi khiến mái nhà thêm gần gũi.','Trang 82: bạn bè tới và niềm vui nơi cửa.'),
('reading','Cách hiểu nào hợp với hình ảnh con đường còn xa?','Nhiều điều mới chờ bạn nhỏ khám phá khi lớn lên.',['Bạn không bao giờ được đến lớp.','Gia đình không còn yêu bạn.','Bài thơ đang tính số ki-lô-mét.'],'Đây là hình ảnh gợi hành trình tương lai.','Trang 82–83: từ đường đi học đến con đường xa.'),
('vocabulary','Đi men khi tập đi là thế nào?','Bám vào vật để bước đi từng chút.',['Chạy thật nhanh ngoài sân.','Ngồi yên không cử động.','Nhảy qua nhiều bậc thang.'],'Đi men giúp em bé giữ thăng bằng.'),
('vocabulary','Từ nào hợp để tả tình cảm của bạn với ngưỡng cửa?','Thân thuộc.',['Xa lạ.','Lạnh nhạt.','Thù ghét.'],'Nơi gắn với nhiều kỉ niệm thường tạo cảm giác thân thuộc.'),
('sentences','Câu nào gắn hoạt động với một người trong gia đình?','Bà dìu em bước qua cửa.',['Ngưỡng cửa rất thấp.','Cửa gỗ màu nâu.','Sân nhà rộng.'],'Bà là người thực hiện hoạt động dìu em.'),
('sentences','Muốn hỏi mẹ về lần đầu tập đi, em nói câu nào?','Mẹ ơi, hồi bé con tập đi thế nào ạ?',['Hồi bé con tập đi rất nhanh.','Mẹ đang mở cửa.','Ngưỡng cửa thấp quá!'],'Câu hỏi có mục đích xin mẹ kể lại kỉ niệm.'),
('spelling','Từ nào có vần ươu và gọi một con vật?','Hươu.',['Hiếu.','Diều.','Yêu.'],'Hươu có vần ươu; các tiếng kia không có vần này.'),
('spelling','Chọn cách viết đúng trong câu: Bà bật ngọn ... nhỏ bên cửa.','đèn',['đèng','đền','đềng'],'Đèn viết vần en, dấu huyền, chỉ đồ dùng chiếu sáng.'),
('expression','Muốn kể kỉ niệm ở cửa nhà rõ hơn, cần chi tiết nào?','Ai ở đó và việc gì đã xảy ra.',['Chỉ nói rất hay nhiều lần.','Chép tên tác giả thay câu chuyện.','Liệt kê đồ vật không liên quan.'],'Người và sự việc giúp người nghe hình dung kỉ niệm.'),
('expression','Câu kết nào thể hiện tình cảm với góc nhà?','Mỗi lần nhìn nơi ấy, em nhớ bàn tay bà dìu mình.',['Ngưỡng cửa là một danh từ.','Em có ba bút chì trong cặp.','Trên lớp có nhiều bạn.'],'Câu kết gắn cảm xúc với kỉ niệm cụ thể.')]),
('Món quà đặc biệt',86,89,['Bố','Người chị','Người em'],
'Hai chị em làm thiệp sinh nhật ghi những nét đáng nhớ của bố. Chị quên bỏ nhận xét bố nấu ăn chưa ngon nên lo lắng, nhưng bố vui vẻ đón nhận, ôm hai con và nhắc tình yêu dành cho các con.',
['Tấm thiệp đặc biệt nhờ sự quan tâm và tình cảm chân thành của hai chị em.','Cảm xúc của chị và bố khác nhau: chị lo vì dòng nhận xét còn sót, bố vui vì món quà của con.','Câu khiến dùng để đề nghị, nhờ, khuyên hoặc yêu cầu; cần nói lễ phép với người thân.'],
['Cho rằng bố nổi giận vì bị chê.','Nhầm chị rơm rớm vì không được tặng quà.','Dùng lời yêu cầu cộc lốc khi nhờ người thân.'],
'Quan sát một đồ vật trong nhà rồi viết 3–4 câu tả màu sắc, hình dáng, công dụng và điều em thích.',
[
('reading','Điều gì khiến người chị lo khi bố đọc thiệp?','Chị quên bỏ nhận xét về việc bố nấu ăn chưa ngon.',['Chị làm mất toàn bộ thiệp.','Bố không có ở nhà.','Em đã giấu quà đi.'],'Dòng nhận xét còn lại khiến chị sợ bố buồn.','Trang 87: chị nhớ mình chưa xoá dòng nhận xét.'),
('reading','Hành động nào cho thấy bố trân trọng món quà?','Bố ôm hai con và cảm ơn.',['Bố xé thiệp ngay.','Bố bắt con mua quà khác.','Bố bỏ đi không nói gì.'],'Cử chỉ gần gũi và lời cảm ơn thể hiện sự yêu thương.','Trang 87: bố dang tay ôm hai chị em.'),
('reading','Ý bố muốn bổ sung vào thiệp nói về điều gì?','Tình yêu của bố dành cho các con.',['Giá của chiếc máy tính.','Một món ăn bố muốn mua.','Lịch làm việc tuần sau.'],'Bố nhắc điều quan trọng hai con chưa ghi: bố yêu các con.','Trang 87: lời bố sau khi cảm ơn.'),
('reading','Vì sao món quà có ý nghĩa dù không đắt tiền?','Hai con dành thời gian quan sát và bày tỏ tình cảm với bố.',['Vì thiệp tự làm luôn bán được nhiều tiền.','Vì bố chỉ thích được khen đẹp trai.','Vì lời nhận xét nào cũng phải hoàn hảo.'],'Ý nghĩa của quà nằm ở tình cảm chứ không chỉ giá tiền.','Trang 86–87: hai chị em tự chuẩn bị thiệp, bố vui khi nhận.'),
('vocabulary','Rơm rớm nước mắt diễn tả trạng thái nào?','Nước mắt vừa ứa lên.',['Cười thành tiếng rất lớn.','Ngủ say ngay lập tức.','Mắt hoàn toàn khô vì vui.'],'Rơm rớm là nước mắt chực trào, chưa nhất thiết khóc thành tiếng.'),
('vocabulary','Đăm chiêu tả vẻ mặt thế nào?','Đang suy nghĩ, có điều băn khoăn.',['Đang cười đùa náo nhiệt.','Đang ngủ không hay biết.','Đang chạy vội.'],'Đăm chiêu liên quan tới nét suy tư trên gương mặt.'),
('sentences','Lời nào nhờ bố hướng dẫn làm thiệp lễ phép?','Bố chỉ con cách gấp thiệp nhé!',['Bố đang gấp thiệp.','Bố có tờ giấy nào?','Thiệp của bố đẹp quá!'],'Câu dùng để nhờ bố làm một việc, có từ nhé tạo sắc thái nhẹ nhàng.'),
('sentences','Câu nào chỉ kể việc làm, không yêu cầu người khác làm?','Em tô thêm một bông hoa lên thiệp.',['Em tô hoa giúp chị nhé!','Hãy đưa chị bút màu!','Đừng gấp góc thiệp!'],'Câu kể thuật lại hoạt động; các câu còn lại có mục đích yêu cầu.'),
('spelling','Tên địa danh nào viết hoa đúng?','Hà Giang',['hà Giang','Hà giang','hà giang'],'Tên địa lí hai tiếng này viết hoa đầu mỗi tiếng.'),
('spelling','Cách viết nào đúng trong lời tả người mẹ hiền?','Dịu dàng.',['Dịu giàng.','Dịu ràng.','Dịu dà ng.'],'Dịu dàng là từ chỉ tính cách, tiếng dàng viết d.'),
('expression','Để tả chiếc đèn bàn, chi tiết nào hữu ích nhất?','Chao màu vàng, thân cong và ánh sáng giúp em đọc.',['Bố có một người bạn.','Ngày mai em đi học.','Thư viện mở cửa sáng thứ hai.'],'Màu, hình dáng và công dụng là những nét cần quan sát đồ vật.'),
('expression','Khi góp ý thiệp của em nhỏ, cách nào thể hiện quan tâm?','Khen phần em làm tốt rồi nhẹ nhàng gợi ý sửa chữ khó đọc.',['Chê em không làm được gì.','Xé thiệp để em làm lại.','Đổi tên mình vào thiệp của em.'],'Góp ý cụ thể, nhẹ nhàng giúp em tiến bộ và giữ tình cảm.')]),
('Khi cả nhà bé tí',90,92,['Bạn nhỏ','Bà','Ông','Bố','Mẹ'],
'Bạn nhỏ tò mò không biết người thân hồi còn bé có giống mình hay không. Những câu hỏi về việc bà, ông, bố, mẹ thường làm cho thấy sự quan sát gần gũi và tình yêu gia đình.',
['Nhiều dòng thơ là câu hỏi, chưa khẳng định ông bà, bố mẹ hồi bé đã làm những việc ấy.','Bạn nhỏ tự nhận mình hồi bé chủ yếu nô đùa, chưa làm được nhiều việc như người lớn.','Hỏi chuyện tuổi thơ giúp em hiểu thêm người thân; lắng nghe rồi kể đúng lời được nghe.'],
['Biến thắc mắc thành sự thật đã xác nhận.','Cho rằng bạn nhỏ chê cả nhà.','Ngắt lời người thân hoặc kể thay khi chưa nghe rõ.'],
'Hỏi một người thân về trò chơi hoặc công việc yêu thích khi còn nhỏ. Ghi lại ba ý rồi kể trong một phút.',
[
('reading','Bạn nhỏ muốn tìm hiểu điều gì về cả nhà?','Khi còn nhỏ mọi người có giống bạn không.',['Ai có nhiều tiền nhất.','Ai sẽ đi xa ngày mai.','Nhà mình xây năm nào.'],'Các câu hỏi đều hướng tới tuổi thơ người thân.','Trang 90–91: chuỗi câu hỏi về lúc cả nhà còn bé.'),
('reading','Có thể kết luận ông hồi bé chắc chắn đã chơi cờ giỏi không?','Chưa thể, bạn nhỏ chỉ đang đặt câu hỏi.',['Có, vì mọi người sinh ra đều biết chơi cờ.','Có, vì bài ghi kết quả một ván cờ.','Không, vì bài nói ông ghét cờ.'],'Không đổi một câu hỏi thành lời khẳng định về quá khứ.','Trang 90: bạn hỏi về dáng ông khi chơi cờ.'),
('reading','Những câu hỏi về bố gắn với nhóm việc nào?','Lái xe, sửa đồ và xem bóng đá.',['May áo, trồng lúa và chèo thuyền.','Dạy múa, bán vé và đánh trống.','Làm thiệp, đọc văn và trực thư viện.'],'Những việc ấy là các hình ảnh bạn nhỏ quan sát ở bố.','Trang 90: khổ thơ hỏi về bố.'),
('reading','Bạn nhỏ nói gì về bản thân khi còn bé?','Thích nô đùa và chưa làm được nhiều việc.',['Đã sửa mọi đồ dùng trong nhà.','Đã đọc sách thâu đêm mỗi ngày.','Đã chơi cờ thắng ông.'],'Lời cuối thơ đặt cái bé nhỏ của mình cạnh hình ảnh người lớn.','Trang 90: khổ cuối tự nói về mình.'),
('vocabulary','Từ nào gần nghĩa với nô đùa?','Chơi đùa vui vẻ.',['Ngồi im buồn bã.','Làm bài thật lặng lẽ.','Mệt đến thiếp đi.'],'Nô đùa gợi hoạt động vui chơi, thường có sự tinh nghịch.'),
('vocabulary','Cụm từ bé tí nhấn mạnh điều gì trong tên bài?','Tuổi còn rất nhỏ.',['Chiều cao ngôi nhà.','Số lượng thành viên.','Giá tiền món quà.'],'Trong nhan đề, bé tí nói về thời thơ ấu của mọi người.'),
('sentences','Câu nào hỏi về sở thích tuổi thơ của bà?','Hồi nhỏ bà thích chơi trò gì ạ?',['Bà đang đọc báo.','Bà thích uống trà.','Cháu đem sách giúp bà nhé!'],'Câu hỏi nêu rõ mốc hồi nhỏ và điều muốn biết.'),
('sentences','Sau khi nghe bố kể, câu nào tránh tự khẳng định quá mức?','Bố kể hồi nhỏ bố thích thả diều.',['Ai hồi nhỏ cũng chỉ thích thả diều.','Bố chắc chắn chưa từng chơi trò khác.','Bố không bao giờ làm việc gì.'],'Câu giới hạn thông tin trong điều bố đã kể, không suy rộng tuỳ tiện.'),
('spelling','Chọn tiếng hợp nghĩa: Mẹ ... em bé trên lưng.','địu',['đựu','điệu','đượu'],'Địu là mang em bé trên lưng hoặc trước ngực bằng vật đỡ phù hợp.'),
('spelling','Cặp từ nào viết đúng để khuyên bạn chăm chỉ?','Đừng lười biếng.',['Đừng lười biến.','Đừng lười biên.','Đừng lười biễn.'],'Biếng có vần iêng, chỉ thái độ ngại làm việc.'),
('expression','Khi người thân đang kể tuổi thơ, em nên làm gì?','Lắng nghe hết ý rồi hỏi thêm điều chưa rõ.',['Cắt lời liên tục.','Tự thêm thành tích cho người kể.','Đổi sang chuyện khác ngay.'],'Lắng nghe giúp ghi nhớ đúng và thể hiện sự tôn trọng.'),
('expression','Cách mở đầu nào phù hợp khi kể điều đã hỏi được?','Hôm qua em nghe bà kể về trò chơi chuyền hồi nhỏ.',['Em sẽ bịa tuổi thơ cho bà.','Tất cả người lớn đều giống nhau.','Không cần nghe cũng biết mọi chuyện.'],'Câu mở nêu người kể, thời điểm nghe và nội dung chính.')]),
('Trò chuyện cùng mẹ',93,96,['Mẹ','Thư','Hân'],
'Thư và Hân thích được đọc sách, trò chuyện với mẹ trước khi ngủ. Mẹ kể chuyện của mình, hai con kể chuyện trường lớp; những câu chuyện nối nhau và tiếng cười khiến ba mẹ con thêm gần gũi.',
['Ba mẹ con ở đây là mẹ cùng hai con Thư, Hân; từ ba chỉ số lượng.','Hân kể chuyện lớp mẫu giáo, trò chơi và quà chiều; Thư kể chuyện đọc văn và đố toán.','Dấu hai chấm có thể báo phần liệt kê hoặc giải thích; cần đọc phần sau để xác định.'],
['Hiểu ba mẹ con là bố, mẹ và một con.','Đổi chuyện của Hân thành chuyện của Thư.','Cho rằng mọi dấu hai chấm đều báo lời nói trực tiếp.'],
'Viết một đoạn tả ngôi nhà em: giới thiệu, tả một nét bên ngoài, một góc bên trong và tình cảm. Không cần ghi địa chỉ riêng tư.',
[
('reading','Ai cùng trò chuyện trước giờ ngủ trong bài?','Mẹ, Thư và Hân.',['Bố, mẹ và Thư.','Ông, bà và Hân.','Cô giáo và cả lớp.'],'Ba trong ba mẹ con là số ba, gồm mẹ và hai chị em.','Trang 93–94: tên Thư, Hân và người mẹ.'),
('reading','Vì sao thời gian trò chuyện thường kéo dài thêm?','Các câu chuyện nối tiếp nhau và ai cũng thích nghe kể.',['Vì mẹ bắt hai con làm bài phạt.','Vì cả nhà đang chờ tàu.','Vì đồng hồ đã ngừng chạy.'],'Sự hào hứng khiến lời hẹn thêm vài phút chưa kết thúc được cuộc trò chuyện.','Trang 93: mẹ hẹn thêm năm phút nhưng vẫn tiếp tục lắng nghe.'),
('reading','Nội dung nào thuộc chuyện Hân thường kể?','Bạn ở lớp mẫu giáo và trò chơi được cô dạy.',['Một bài văn được đọc trước cả lớp.','Những bài toán đố giờ ra chơi của Thư.','Cuộc họp ở nơi làm việc của mẹ.'],'Hân kể những điều gần gũi với em ở lớp mẫu giáo.','Trang 94: đoạn phân biệt chuyện Hân và chuyện Thư.'),
('reading','Mẹ làm điều gì khiến hai con bật cười?','Kể về hình dáng của mẹ khi còn bé.',['Bắt hai con ngủ ngay mà không nói.','Đọc bảng điểm thật nghiêm khắc.','Giấu hết sách trong phòng.'],'Hình dáng của mẹ lúc nhỏ khiến hai con thấy buồn cười.','Trang 93: mẹ kể chuyện ngày bé; hình dáng mẹ hồi bé khiến con cười.'),
('vocabulary','Líu lo kể chuyện gợi cách kể thế nào?','Vui vẻ, ríu rít.',['Cáu kỉnh, quát mắng.','Im lặng hoàn toàn.','Chậm vì đang ngủ.'],'Líu lo gợi tiếng nói vui, liên tiếp như tiếng chim.'),
('vocabulary','Ai là bà ngoại của một bạn nhỏ?','Mẹ của mẹ bạn ấy.',['Mẹ của bố bạn ấy.','Chị của bố bạn ấy.','Em gái của bạn ấy.'],'Bên ngoại là phía gia đình mẹ; mẹ của mẹ là bà ngoại.'),
('sentences','Trong câu Mẹ mang ra hai thứ: sách và bút, dấu hai chấm báo gì?','Phần liệt kê.',['Một câu hỏi.','Lời của người đang nói trực tiếp.','Kết thúc toàn bộ đoạn văn.'],'Phía sau kể tên hai đồ vật đã được giới thiệu.'),
('sentences','Trong câu Em thích góc này: nơi ấy có cửa sổ nhìn ra vườn, dấu hai chấm báo gì?','Phần giải thích lí do thích.',['Danh sách nhiều người.','Một lời gọi đáp.','Chỗ kết thúc câu hỏi.'],'Vế sau làm rõ vì sao em thích góc nhà.'),
('spelling','Tên hai chị em được viết đúng là gì?','Thư và Hân',['thư và Hân','Thư và hân','thư và hân'],'Tên riêng của mỗi người phải viết hoa đầu tên.'),
('spelling','Chọn cách viết đúng: Ba mẹ con cười ... khi nghe chuyện vui.','rúc rích',['dúc dích','rút rích','rúc rít'],'Rúc rích tả tiếng cười nhỏ, vui vẻ; hai tiếng viết r.'),
('expression','Để tả ngôi nhà rõ hơn, câu nào hữu ích?','Cửa sổ cạnh bàn học nhìn ra một cây xoài.',['Nhà em rất rất rất rất nhà.','Thư là tên một nhân vật.','Hai chị em trò chuyện cùng mẹ.'],'Chi tiết vị trí và cảnh nhìn thấy giúp hình dung ngôi nhà.'),
('expression','Cuối buổi trò chuyện, cách nào thể hiện vừa yêu mẹ vừa giữ giờ ngủ?','Cảm ơn mẹ, hẹn mai kể tiếp rồi đi ngủ.',['Đòi kể đến sáng mỗi ngày.','Giận mẹ vì cần nghỉ ngơi.','Nói mẹ không được đi làm.'],'Tình cảm đi cùng sự quan tâm thời gian nghỉ của cả nhà.')])]
for i,(title,start,end,chars,summary,rules,errors,task,rows) in enumerate(data,17):
 c=json.loads((R/'content/tieng-viet/tap-1/TV3_T1_B16.json').read_text()); ident=f'TV3_T1_B{i:02}'
 c.update(id=ident,lesson_no=i,title=title,topic='Mái nhà yêu thương',status='AI_CHECKED_AWAITING_TEACHER')
 c['source'].update(printed_pages=[start,end],pdf_pages=[start+1,end+1],review='Đọc trực quan các trang nguồn PDF tương ứng; ghi chú BATCH26_SOURCE_NOTES.md. Nội dung luyện tập mới biên soạn, không chép toàn văn SGK.')
 c['objectives']=['Hiểu nội dung và chi tiết chính của '+title+'.','Giải thích ý nghĩa bằng căn cứ trong bài.','Luyện từ, câu, chính tả và diễn đạt theo chủ đề gia đình.']
 c['reading']=dict(summary=summary,characters_or_images=chars,message=rules[0] if i in [18,20] else rules[1])
 c['knowledge']=dict(introduction=summary,rules=rules,steps=['Đọc bài trong sách ở trang nguồn.','Đối chiếu người, sự việc với phần tóm tắt.','Làm bài tập, xem lời giải rồi thực hành nói hoặc viết.'],common_errors=errors)
 c['practice']=[]
 for n,row in enumerate(rows,1):
  skill,q,a,wrong,ex,*e=row
  x=dict(question_id=f'{ident}_Q{n:02}',type='mcq',skill=skill,question=q,options=[a]+wrong,correct_answer=a,explanation=ex)
  if e:x['evidence']=e[0]
  c['practice'].append(x)
 c['examples']=[dict(question=rows[0][1],steps=[rows[0][-1],rows[0][4],'Trả lời: '+rows[0][2]]),dict(question=rows[6][1],steps=[rows[6][4],'Đáp án: '+rows[6][2]])]
 c['language_practice']={s:[q['question']+' Đáp án: '+q['correct_answer']+' '+q['explanation'] for q in c['practice'] if q['skill']==s] for s in ['vocabulary','sentences','spelling','expression']}
 checks=['Có chi tiết cụ thể, đúng điều quan sát hoặc được nghe.','Các ý nối nhau rõ, câu đủ ý và có dấu kết câu.','Thể hiện tình cảm phù hợp, không chép đoạn mẫu.']
 c['activities']=[dict(title='Nói và viết về mái ấm',materials=['Vở','Bút'],steps=[task,'Đọc hoặc kể cho người thân nghe.','Dựa vào tiêu chí để sửa một chỗ chưa rõ.'],check=checks)]
 c['games'][0].update(id=ident+'_GAME',title=['Bước qua ngưỡng cửa','Tấm thiệp yêu thương','Hỏi chuyện tuổi thơ','Chuyện trước giờ ngủ'][i-17],question_ids=[q['question_id'] for q in c['practice']])
 c['verification']['teacher_approved']=False
 p=R/f'content/tieng-viet/tap-1/{ident}.json';p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 lines=['# '+title,'Trạng thái: AI_CHECKED_AWAITING_TEACHER','Nguồn: '+str(c['source']),'## Mục tiêu',*c['objectives'],'## Kiến thức',summary,*rules,*c['knowledge']['steps'],'## Lỗi thường gặp',*errors,'## Ví dụ có lời giải']
 for e in c['examples']:lines +=[e['question'],*e['steps']]
 lines+=['## Thực hành nói và viết',task,*checks,'## Bài tập và đáp án']
 for q in c['practice']:lines +=[q['question'],*q['options'],'Đáp án: '+q['correct_answer'],q['explanation'],q.get('evidence','')]
 lines+=['## Trò chơi',c['games'][0]['title'],*c['games'][0]['rules'],'## Đánh giá và phản hồi',*[str(v) for v in c['assessment'].values()],*[str(v) for v in c['feedback'].values()]]
 p.with_suffix('.md').write_text('\n\n'.join(lines)+'\n')
print('Created TV17–20: 48 questions, 4 games')
