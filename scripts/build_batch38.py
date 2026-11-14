"""Starter + Units1–3: visually reviewed printed7–27 / PDF8–28 on14/11/2026."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
rows=[[
'vocabulary|Thẻ có chữ eight. Em cần đặt thẻ cạnh số nào?|8|3;5;10|Eight là số tám; không nhầm với cách viết three hoặc ten.',
'reading|Đọc thẻ: A — B — C. Thẻ này đang luyện nội dung nào?|Các chữ cái tiếng Anh.|Tên ba ngày.;Ba lời chào.;Tên ba màu.|A, B, C là ba chữ đầu bảng chữ cái, không phải các từ chỉ màu hay ngày.',
'writing|Một bạn viết số chín là nien. Cách sửa đúng là gì?|nine|nien;nein;nineh|Nine gồm n-i-n-e. Quan sát vị trí i và n trước khi chép.',
'vocabulary|Trong trò gọi số, bạn nói ten. Em hiểu là bao nhiêu?|Mười.|Một.;Bốn.;Bảy.|Ten là mười, điểm cuối dãy số từ một đến mười của Starter.',
'alphabet|Trong dãy chữ cái L, M, N, chữ đứng ngay sau M là gì?|N|L;W;H|M đứng trước N. Khi đọc bảng chữ cái, theo thứ tự thay vì đoán theo hình dáng.',
'writing|Chọn cách viết đúng số bốn bằng tiếng Anh.|four|forr;fuor;frou|Four có thứ tự f-o-u-r; từ for không phải số bốn.',
'reading|Trên bảng Bingo của em đã đánh dấu seven. Ô nào tương ứng với từ ấy?|Ô số 7.|Ô chữ S.;Ô số 6.;Ô chữ V.|Bảng đang chơi là bảng số; seven tương ứng với 7, không phải chỉ chữ đầu của từ.',
'alphabet|Chữ hoa Q ghép với chữ thường nào?|q|p;g;o|Q và q là hai kiểu viết của cùng một chữ; phân biệt đuôi của q với o.',
'pronunciation|Khi luyện chữ B và từ bắt đầu bằng b, cần nhớ điều gì?|Tên chữ B khác với âm b trong từ.|Tên chữ và âm luôn giống hệt.;Mọi chữ đều đọc như tiếng Việt.;Chỉ nhìn hình mà không cần đọc.|Tên chữ dùng khi đánh vần; âm trong từ dùng khi phát âm từ. Starter luyện tên chữ cái.',
'speaking|Bạn mới bắt đầu tập đếm. Cách luyện nào giúp em tự kiểm tra tốt?|Chỉ từng đồ vật, đọc một số cho mỗi vật rồi kiểm tra lại.|Đọc số thật nhanh mà không đếm.;Bỏ vật khó nhìn khỏi nhóm.;Đọc cùng một số cho mọi vật.|Ghép mỗi vật với một số giúp kiểm tra đọc và đếm; có thể dùng một đến mười vật.',
'writing|Tên LAN có bao nhiêu chữ cái để em đọc lần lượt?|Ba chữ cái: L, A, N.|Hai chữ cái: L, N.;Bốn chữ cái: L, A, A, N.;Một chữ cái: LAN.|Tên này gồm ba kí tự riêng; không coi cả tên là một chữ cái.',
'alphabet|Khi thẻ chữ bị lẫn, nhóm nào đã đúng thứ tự gần cuối bảng chữ cái?|W, X, Y, Z.|Z, Y, X, W.;W, Y, X, Z.;X, W, Z, Y.|Cuối bảng chữ cái lần lượt là W rồi X, Y, Z. Đọc chậm để nhận thứ tự.'
],[
'communication|Gặp bạn An lần đầu, em muốn chào và giới thiệu mình là Hoa. Câu nào phù hợp?|Hello, An. I\'m Hoa.|Goodbye, An.;I Hoa am.;Bye, Hoa.|Hello dùng lúc chào gặp; I am hoặc I\'m đứng trước tên người nói.',
'grammar|Trong lời tự giới thiệu, I\'m là dạng ngắn của cụm nào?|I am.|I is.;I are.;I name.|Dấu nháy thay chữ a của am; không đổi sang is hoặc are.',
'communication|Bạn hỏi How are you? Em đang khoẻ và muốn cảm ơn. Em đáp thế nào?|Fine, thank you.|Goodbye, teacher.;My friend.;Hello is fine.|Câu hỏi thăm tình trạng, câu đáp cho biết khoẻ và cảm ơn người hỏi.',
'vocabulary|Cặp từ nào đều dùng để chào khi gặp nhau?|Hello và Hi.|Bye và ten.;Goodbye và eight.;Fine và nine.|Hello và Hi cùng dùng để chào gặp; Goodbye hoặc Bye dùng khi tạm biệt.',
'reading|Đọc: Hello. I\'m Lan. Hi, Lan. I\'m Phuc. Người thứ hai tên gì?|Phuc.|Lan.;Hello.;Hi.|Sau lời chào Lan, người thứ hai tự giới thiệu bằng I\'m Phuc. Đây là hội thoại biên soạn mới.',
'writing|Chọn câu tự giới thiệu đã viết hoa và có dấu kết câu.|I\'m Huy.|i\'m huy;I m Huy;Huy I\'m|I và tên riêng viết hoa; I\'m có dấu nháy và cuối câu dùng dấu chấm.',
'communication|Cuối buổi học, bạn vẫy tay ra về. Em nên nói gì?|Goodbye!|I\'m here hello.;Fine name.;How goodbye?|Goodbye là lời tạm biệt phù hợp lúc chia tay; có thể dùng Bye.',
'pronunciation|Âm đầu trong hello được luyện ở Unit1 là âm nào?|/h/|/b/;/m/;/n/|Hello mở đầu bằng /h/: thở nhẹ qua miệng, không khép hai môi như /b/.',
'pronunciation|Muốn luyện âm đầu bye, động tác nào phù hợp?|Khép hai môi rồi bật nhẹ, có rung giọng.|Cắn môi dưới và thổi.;Đặt đầu lưỡi giữa răng.;Chỉ kéo dài nguyên âm.|Âm /b/ là âm bật hai môi có rung; không đọc tên chữ bee thay toàn từ bye.',
'reading|Phiếu có lời Hi, I\'m Nga. Thông tin chắc chắn biết từ phiếu là gì?|Tên người nói là Nga.|Nga chín tuổi.;Nga học lớp 3B.;Nga đang tạm biệt.|Phiếu chỉ cho biết tên và lời chào; không suy thêm tuổi hay lớp.',
'writing|Đáp lại Hello, Nam! bằng lời chào gặp, em chọn câu nào?|Hi!|Bye!;Goodbye!;Ten!|Hi đáp lời chào gặp. Bye và Goodbye chuyển sang tạm biệt nên không phù hợp yêu cầu.',
'speaking|Đóng vai gặp rồi chia tay bạn, trình tự nào hợp lí?|Chào, tự giới thiệu, hỏi thăm, tạm biệt.|Tạm biệt rồi hỏi tên trong im lặng.;Chỉ lặp số đếm.;Nói tên người khác như tên mình.|Tình huống cần dùng lời chào, tên người nói, hỏi thăm rồi lời chia tay đúng lúc.'
],[
'communication|Em chưa biết tên bạn mới. Nên hỏi câu nào?|What\'s your name?|How old are you?;How are you?;Goodbye, name.|What\'s your name hỏi tên; không nhầm với câu hỏi tuổi hoặc hỏi thăm.',
'grammar|Bạn hỏi tên em. Em tên Thao. Câu trả lời nào đúng mẫu?|My name\'s Thao.|Your name\'s Thao.;My Thao name.;Name my Thao.|My name\'s dùng để giới thiệu tên của chính người nói; your chỉ người nghe.',
'communication|Một bạn hỏi How old are you? Em cần cung cấp thông tin gì?|Tuổi của mình.|Tên trường.;Màu áo.;Tên bạn thân.|How old hỏi tuổi, khác What\'s your name hỏi tên.',
'writing|Em 9 tuổi. Chọn câu viết đầy đủ theo mẫu Unit2.|I\'m nine years old.|I nine years.;I\'m nine name.;My age name nine.|Sau I\'m là số tuổi; years old làm rõ ý tuổi trong câu đầy đủ.',
'reading|Đọc: My name\'s Bao. I\'m seven years old. Bao bao nhiêu tuổi?|Bảy tuổi.|Tám tuổi.;Chín tuổi.;Mười tuổi.|Seven chỉ bảy, là số tuổi Bao tự giới thiệu trong đoạn mới này.',
'vocabulary|Trong câu My name\'s Vy, name có nghĩa là gì?|Tên.|Tuổi.;Lớp học.;Lời tạm biệt.|Name chỉ tên gọi; không dùng nó thay cho số tuổi.',
'grammar|Đổi My name is Quynh sang dạng ngắn đúng.|My name\'s Quynh.|My names Quynh.;My name\' Quynh.;My name Quynh\'s.|Name\'s là name is; dấu nháy đứng trước s.',
'pronunciation|Khi luyện âm m ở đầu Mary, môi em nên thế nào?|Khép hai môi, cho tiếng vang qua mũi.|Mở to miệng và thổi mạnh.;Đặt răng lên môi dưới.;Bật âm như t.|/m/ là âm mũi hai môi; luyện âm đầu rồi đọc cả tên.',
'pronunciation|Âm đầu /n/ trong Nam khác /m/ ở điểm nào?|Đầu lưỡi chạm vùng lợi trên thay vì khép hai môi.|Luôn cần cắn môi dưới.;Không dùng giọng.;Chỉ có trong tiếng Việt.|/n/ dùng đầu lưỡi, /m/ dùng hai môi; cả hai có tiếng vang qua mũi.',
'reading|Hai thẻ ghi Yen: eight; Khoa: ten. Ai ghi tuổi mười?|Khoa.|Yen.;Cả hai.;Không ai.|Ten là mười, eight là tám; đọc đúng mỗi dòng của thẻ biên soạn mới.',
'writing|Điền câu hỏi phù hợp trước lời đáp My name\'s Long.|What\'s your name?|How old are you?;How are you?;Is this a number?|Lời đáp cho biết tên nên cần câu hỏi tên, không hỏi tuổi hay sức khoẻ.',
'speaking|Làm thẻ sinh nhật để giới thiệu, em nên chuẩn bị điều gì?|Tên và số tuổi muốn giới thiệu, rồi tập hỏi đáp theo cặp.|Chỉ màu bánh, không nói tên tuổi.;Ghi tuổi người khác thành của mình.;Chép một lời tạm biệt duy nhất.|Hoạt động giúp nói tên và tuổi; có thể đóng vai và nói rõ thông tin nhân vật khi không dùng tuổi thật.'
],[
'communication|Bạn đứng ngay cạnh em. Em giới thiệu bạn ấy tên Thu thế nào?|This is Thu.|That are Thu.;This Thu am.;How Thu is?|This is dùng giới thiệu người ở gần; is cần đứng trước tên.',
'communication|Cô Mai đứng ở phía xa. Em muốn chỉ và giới thiệu cô. Câu nào phù hợp?|That\'s Ms Mai.|This are Mai.;I\'m Ms Mai.;My name teacher.|That\'s là That is, dùng người ở xa người nói trong tình huống này.',
'grammar|Cụm That\'s viết đầy đủ là gì?|That is.|That am.;That are.;That has name.|Trong mẫu giới thiệu của Unit3, dấu nháy thay i của is.',
'communication|Bạn chỉ đúng vào Binh và hỏi Is this Binh? Em đáp ngắn thế nào?|Yes, it is.|Yes, I am.;No, it is.;Yes, this are.|Mẫu xác nhận người được chỉ là Yes, it is; không dùng I am để nói về người khác.',
'communication|Người ở xa là Hà, bạn lại hỏi Is that Nga? Em sửa lịch sự thế nào?|No, it isn\'t. It\'s Ha.|Yes, it is. It\'s Nga.;No, I\'m Ha.;That are not.|Phủ định nhận diện sai rồi cung cấp tên đúng của người được chỉ.',
'vocabulary|Trong câu This is my friend, friend có nghĩa là gì?|Bạn.|Cái bàn.;Màu sắc.;Chín.|Friend là bạn; teacher mới chỉ giáo viên.',
'reading|Đọc: This is my teacher, Ms Thuy. Ms Thuy là ai của người nói?|Cô giáo.|Bạn cùng tuổi.;Em gái.;Người nói.|My teacher cho biết quan hệ; Ms là cách gọi phụ nữ, không tự suy đoán tình trạng hôn nhân.',
'writing|Chọn câu đã đủ thành phần để giới thiệu bạn Nam.|This is my friend, Nam.|This my friend Nam.;This are friend Nam.;Is my Nam this.|Mẫu cần This is, rồi my friend và tên người được giới thiệu.',
'pronunciation|Âm th trong that khác th trong thank ở điểm nào?|That có rung giọng, thank không rung giọng ở âm đầu.|Cả hai đều đọc /t/.;Chỉ that cần lưỡi giữa răng, thank không.;Cả hai đều đọc tên chữ T.|/ð/ trong that và /θ/ trong thank đều để đầu lưỡi nhẹ giữa răng, khác độ rung giọng.',
'pronunciation|Để luyện /θ/ trong thank, cách nào gần đúng nhất?|Đầu lưỡi nhẹ giữa răng và thổi khí, không bật thành /t/.|Khép môi bật âm /b/.;Đọc thành sờ thật mạnh.;Chỉ đọc tên chữ H.|Luyện luồng hơi qua đầu lưỡi; không thêm âm tắc /t/ hoặc đổi thành /s/.',
'reading|Đọc: That\'s Duc. Duc is my friend. Người ở xa được giới thiệu tên gì?|Duc.|My.;Friend.;That.|That\'s giới thiệu Duc; câu sau cho biết quan hệ bạn bè, không phải tên mới.',
'speaking|Làm tấm giới thiệu bạn thân, cách dùng lời nào đúng bài?|Nói This is my friend rồi tên, cùng bạn luyện câu hỏi nhận diện.|Đọc tuổi mà không giới thiệu ai.;Dùng I\'m để gọi mọi người.;Chỉ nói Yes cho mọi câu hỏi.|Hoạt động cần giới thiệu bạn và luyện Is this/that, trả lời theo đúng người được nêu.'
]]
meta=[
('TA3_T1_START','Starter',7,9, 'Làm quen các số từ1 đến10, tên chữ cái A–Z, ghép chữ hoa với chữ thường và chơi Bingo.',
 [('one','một','One card.'),('two','hai','Two cards.'),('three','ba','Three cards.'),('four','bốn','Four cards.'),('five','năm','Five cards.'),('six','sáu','Six cards.'),('seven','bảy','Seven cards.'),('eight','tám','Eight cards.'),('nine','chín','Nine cards.'),('ten','mười','Ten cards.')],
 ['Đọc số: one, two, three, four, five, six, seven, eight, nine, ten.','Đọc tên chữ A–Z theo thứ tự; dùng để đánh vần từng chữ của tên.'],
 ['Tên chữ cái khác âm của chữ trong từ. Đọc A /eɪ/, B /biː/, C /siː/ khi đánh vần.','Nghe four /fɔː/ và five /faɪv/; four kết thúc bằng âm nguyên âm dài trong giọng Anh, five có /v/.'],
 ['Đọc các thẻ biên soạn mới: six — 6; ten — 10; LAN — L, A, N.','Nhiệm vụ: từ ten ghép với6 hay10? Đáp án10 vì ten là mười.'],
 ['Viết số2,4,9 bằng tiếng Anh rồi tự soát: two, four, nine.','Viết tên nhân vật do em chọn, tách từng chữ và đếm số chữ. Mẫu: AN có2 chữ A, N.'],
 ['Đọc các số một đến mười khi chỉ từng thẻ tự làm.','Đánh vần tên LAN theo từng chữ L, A, N; nhờ bạn chỉ đúng thẻ em đọc.'],
 ['Đảo hai thẻ four và five, nghe giọng máy rồi chỉ đúng thẻ; kiểm tra bằng chữ trên thẻ.','Giọng máy chỉ hỗ trợ luyện; em đọc lại chậm và nhờ người lớn nghe nếu chưa chắc.'],
 ['Đọc tên chữ như âm tiếng Việt hoặc nhầm tên chữ với âm trong từ.','Đảo vị trí chữ trong four/nine hoặc đọc số mà không chỉ từng vật.'],
 'Làm bảng Bingo3×3 với9 số tự chọn từ1–10. Người thân gọi số ngẫu nhiên, em đánh dấu và đọc lại các số tạo hàng thắng.'),
('TA3_T1_U01','Unit 1: Hello',10,15,'Chào gặp, tự giới thiệu tên, hỏi thăm tình trạng và tạm biệt đúng lúc.',
 [('hello','xin chào','Hello, Lan.'),('hi','chào','Hi, Khoa.'),('goodbye','tạm biệt','Goodbye, An.'),('bye','tạm biệt','Bye, Nam.'),('fine','khoẻ, ổn','I\'m fine.'),('thank you','cảm ơn','Fine, thank you.')],
 ['Hello. / Hi. I\'m Hoa. → Xin chào. Mình là Hoa. I\'m = I am.','How are you? — Fine, thank you. → Bạn có khoẻ không? — Mình khoẻ, cảm ơn.','Goodbye. / Bye. → Tạm biệt.'],
 ['/h/ trong hello: mở miệng, thở nhẹ rồi đọc cả hello; không thêm âm khờ.','/b/ trong bye: khép hai môi rồi bật nhẹ có rung giọng; đừng đọc tên chữ bee thay cho từ.'],
 ['Hội thoại mới: Lan: Hi. I\'m Lan. Phuc: Hello, Lan. I\'m Phuc. Lan: How are you? Phuc: Fine, thank you.','Ai trả lời lời hỏi thăm? Đáp án: Phuc. Tìm lượt nói sau câu How are you.'],
 ['Viết ba lời của em khi gặp bạn: Hello. I\'m Hoa. How are you?','Thêm lời chia tay: Goodbye. Thay tên Hoa bằng tên em hoặc tên nhân vật đóng vai, viết hoa tên và I.'],
 ['Đóng vai gặp nhau ở sân trường, chào và giới thiệu; đổi vai hỏi thăm rồi chia tay.','Tự kiểm: mỗi người có một lời chào, một thông tin tên và lời đáp hỏi thăm phù hợp.'],
 ['Bấm nghe hello và bye; chỉ thẻ gặp nhau hoặc chia tay phù hợp.','Nghe fine rồi đọc cả câu Fine, thank you; đây là giọng máy, không phải bản thu của sách.'],
 ['Dùng Goodbye lúc mới gặp theo yêu cầu chào hỏi.','Viết I m thiếu dấu nháy hoặc dùng I is thay I am.'],
 'Tạo thẻ học sinh tưởng tượng có tên và lớp, rồi đóng vai chào bạn bằng tên trên thẻ; không cần đưa thông tin riêng lên mạng.'),
('TA3_T1_U02','Unit 2: Our names',16,21,'Hỏi đáp tên và tuổi, phân biệt câu hỏi tên với câu hỏi tuổi, luyện âm m và n.',
 [('name','tên','My name\'s Bao.'),('my','của tôi','My name\'s Thao.'),('your','của bạn','What\'s your name?'),('old','tuổi (trong years old)','I\'m eight years old.'),('seven','bảy','I\'m seven.'),('eight','tám','I\'m eight.'),('nine','chín','I\'m nine.'),('ten','mười','I\'m ten.')],
 ['What\'s your name? — My name\'s Bao. → Bạn tên gì? — Mình tên Bảo.','How old are you? — I\'m eight years old. → Bạn bao nhiêu tuổi? — Mình tám tuổi.','What\'s = What is; name\'s = name is. Dùng my khi nói tên mình, your khi hỏi bạn.'],
 ['/m/ trong Mary: hai môi khép, có tiếng vang qua mũi.','/n/ trong Nam: đầu lưỡi chạm vùng lợi trên, môi không cần khép; so sánh /m/ và /n/.'],
 ['Đoạn mới: My name\'s Bao. I\'m seven years old. My friend is Khoa.','Bảo bao nhiêu tuổi? Đáp án: seven, bảy tuổi. Không suy rằng Khoa cùng tuổi vì đoạn không nêu.'],
 ['Viết một lượt hỏi tên và một lượt trả lời; mẫu mới: What\'s your name? My name\'s Thao.','Thêm câu tuổi nhân vật: I\'m nine years old. Giữ dấu nháy, viết hoa và dấu kết câu.'],
 ['Vẽ bánh sinh nhật có số tuổi nhân vật7–10, hỏi bạn How old are you và đáp theo thẻ.','Đổi vai hỏi tên trước hỏi tuổi; người nghe nhắc lại xem đã hiểu đúng tên và số chưa.'],
 ['Nghe các từ seven/eight/nine/ten từ nút giọng máy, chỉ số trên thẻ bánh.','Luyện Mary và Nam bằng hướng dẫn âm trong bài; giọng máy hỗ trợ, không thay phản hồi phát âm của người lớn.'],
 ['Trả lời tên khi được hỏi How old.','Dùng your name để nói tên mình; quên is trong name is hoặc dấu nháy trong name\'s.'],
 'Làm thẻ bánh sinh nhật cho nhân vật tự đặt tên, ghi số tuổi7–10; dùng thẻ để hỏi đáp tên và tuổi theo cặp.'),
('TA3_T1_U03','Unit 3: Our friends',22,27,'Giới thiệu bạn và giáo viên; dùng this/that theo khoảng cách, hỏi và xác nhận người được giới thiệu.',
 [('this','đây, người ở gần','This is Thu.'),('that','kia, người ở xa','That is Duc.'),('friend','bạn','This is my friend, An.'),('teacher','giáo viên','That\'s my teacher.'),('yes','vâng, đúng','Yes, it is.'),('no','không','No, it isn\'t.'),('Mr','cách gọi ông/thầy kèm tên','That\'s Mr Hai.'),('Ms','cách gọi cô/bà kèm tên','This is Ms Thuy.')],
 ['This is Thu. / That\'s Duc. → Đây là Thu. / Kia là Đức. That\'s = That is.','Is this Binh? — Yes, it is. → Đây là Bình phải không? — Đúng rồi.','Is that Nga? — No, it isn\'t. It\'s Ha. → Kia là Nga phải không? — Không. Đó là Hà.','This is my friend, Nam. / That\'s my teacher, Ms Thuy. → Giới thiệu bạn / cô giáo.'],
 ['/ð/ trong that: đầu lưỡi nhẹ giữa răng, thổi khí có rung giọng.','/θ/ trong thank: vị trí lưỡi tương tự nhưng không rung giọng; không bật thành /t/ hay đổi thành /s/.'],
 ['Đoạn mới: This is my friend, Thu. That\'s my teacher, Mr Hai.','Ai là giáo viên? Đáp án: Mr Hai. Ai ở gần người nói theo câu giới thiệu? Thu, vì dùng This is.'],
 ['Viết hai câu giới thiệu nhân vật trên hai thẻ: This is my friend, An. That\'s my teacher, Ms Yen.','Thêm câu nhận diện sai và sửa: Is that Nga? No, it isn\'t. It\'s Ha. Nhớ dấu nháy trong isn\'t và It\'s.'],
 ['Đặt một thẻ gần, một thẻ xa; giới thiệu lần lượt bằng This is/That\'s, bạn hỏi lại Is this/that.','Khi tên bị hỏi sai, nói No, it isn\'t rồi cung cấp tên đúng; đổi vị trí thẻ và đổi vai.'],
 ['Nghe this/that từ nút giọng máy và chỉ thẻ gần/xa theo ngữ cảnh em đặt.','Đọc chậm thank và that theo hướng dẫn, đặt tay nhẹ lên cổ để nhận độ rung, không dùng vật chạm miệng.'],
 ['Dùng I\'m để giới thiệu người khác.','Dùng This are hoặc That am; trả lời Yes, I am cho câu hỏi về người được chỉ.'],
 'Vẽ hai người bạn tưởng tượng, đặt thẻ gần/xa, viết một câu giới thiệu mỗi người rồi hỏi bạn nhận diện. Có thể dùng tranh tự vẽ, không cần ảnh cá nhân.')]
for j,(ident,title,start,end,intro,vocab,patterns,pronunciation,reading,writing,speaking,listening,errors,task) in enumerate(meta):
 c=json.loads((R/'content/tieng-viet/tap-2/TV3_T2_B30.json').read_text())
 for key in ['reading','language_practice']:c.pop(key,None)
 c.update(id=ident,title=title,subject='ta',volume=1,lesson_no=j,topic='English Global Success',objectives=['Hiểu và dùng đúng: '+intro,'Đọc, viết và thực hành nói theo tình huống mới.','Nhận biết trọng tâm phát âm và luyện nghe bằng giọng máy có ghi nhãn.'])
 c['source'].update(pdf='03-sgk-tieng-anh-3-tap-1-global-success.pdf',printed_pages=[start,end],pdf_pages=[start+1,end+1],review='Đã đọc trực quan đầy đủ trang nguồn PDF ảnh quét ngày14/11/2026. Biên soạn tình huống, ví dụ và câu hỏi mới; không đăng toàn văn hay sao chép hệ thống bài tập SGK; không có bản thu âm sách.')
 c['vocabulary']=[dict(word=w,meaning_vi=m,example=e) for w,m,e in vocab]
 c['patterns']=patterns;c['pronunciation']=pronunciation;c['skills']=dict(reading=reading,writing=writing,speaking=speaking,listening=listening)
 c['audio']=dict(type='speechSynthesis',label='Giọng máy tiếng Anh của thiết bị, không phải âm thanh sách. Có thể khác theo thiết bị; nếu không phát, đọc theo mẫu và nhờ người lớn hỗ trợ.')
 c['knowledge']=dict(introduction=intro,rules=patterns,steps=['Đọc từ và nghĩa, quan sát tình huống trước khi chọn cách nói.','Nghe từ bằng giọng máy nếu thiết bị hỗ trợ, đọc lại chậm theo hướng dẫn phát âm.','Làm câu hỏi, xem giải thích rồi thực hành nói và viết theo nhiệm vụ.'],common_errors=errors)
 c['practice']=[]
 for n,row in enumerate(rows[j],1):
  skill,q,a,w,e=row.split('|');opts=[a]+w.split(';');opts=opts[n%4:]+opts[:n%4]
  c['practice'].append(dict(question_id=f'{ident}_Q{n:02}',type='mcq',skill=skill,question=q,correct_answer=a,options=opts,explanation=e))
 c['examples']=[dict(question=c['practice'][k]['question'],steps=['Nhận diện yêu cầu: '+c['practice'][k]['skill'],c['practice'][k]['explanation'],'Đáp án: '+c['practice'][k]['correct_answer']]) for k in [0,4]]
 c['activities']=[dict(title='Thực hành theo cặp: '+title,materials=['Giấy','Bút','Thẻ tự làm'],steps=[task,'Đổi vai và nhờ bạn nhắc lại thông tin đã nghe.','Sửa một lỗi sau khi đọc phần giải thích trong bài.'],check=['Đúng nội dung giao tiếp hoặc chữ/số yêu cầu.','Phát âm chậm, đủ nghe; nhờ người lớn hỗ trợ chỗ chưa chắc.','Viết đúng từ, tên riêng, dấu nháy và dấu câu.'])]
 c['assessment'].pop('distribution',None);c['assessment']['session_size']=10;c['assessment']['review_advice']='Xem lại câu sai theo nhóm từ, mẫu câu, phát âm; thực hiện cả nhiệm vụ nói và viết. Điểm trắc nghiệm không thay thế nhận xét phát âm.'
 c['games'][0].update(id=ident+'_GAME',title='Kho báu tiếng Anh: '+title,question_ids=[q['question_id'] for q in c['practice']],objective='Chọn từ và lời nói phù hợp để mở kho báu.',rules=['Mỗi lượt10 câu thuộc bài, không áp phân mức Toán.','Chọn đáp án rồi đọc giải thích. Trả lời đúng tiến thêm một bước.','Kết thúc, ôn câu sai và thử lại.'])
 c['feedback']=dict(correct='Đúng rồi! Em đọc lại từ hoặc lời nói vừa chọn.',incorrect='Đọc lời giải, chú ý tình huống rồi thử dùng mẫu câu.',teacher_note='AI_CHECKED_AWAITING_TEACHER; phần nói và phát âm cần người lớn nghe và góp ý.')
 c['status']='AI_CHECKED_AWAITING_TEACHER';c['verification']['teacher_approved']=False
 p=R/f'content/tieng-anh/tap-1/{ident}.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 lines=['# '+title,'Trạng thái: '+c['status'],'## Nguồn',str(c['source']),'## Mục tiêu',*c['objectives'],'## Kiến thức',intro,*patterns,'## Hướng dẫn',*c['knowledge']['steps'],'## Lỗi thường gặp',*errors,'## Từ vựng']
 for v in c['vocabulary']:lines.append(v['word']+' — '+v['meaning_vi']+' — '+v['example'])
 lines+=['## Phát âm',*pronunciation,c['audio']['label']]
 for skill,items in c['skills'].items():lines+=['## '+skill,*items]
 lines+=['## Ví dụ có lời giải']
 for ex in c['examples']:lines +=[ex['question'],*ex['steps']]
 lines+=['## Hoạt động',*c['activities'][0]['steps'],*c['activities'][0]['check'],'## Luyện tập và đáp án']
 for q in c['practice']:lines +=[q['question_id']+' — '+q['question'],*q['options'],'Đáp án: '+q['correct_answer'],q['explanation']]
 lines+=['## Trò chơi',c['games'][0]['title'],*c['games'][0]['rules'],'## Đánh giá',*map(str,c['assessment'].values()),'## Phản hồi',*c['feedback'].values()]
 p.with_suffix('.md').write_text('\n\n'.join(lines)+'\n')
print('Batch38: Starter + Unit1–3, 48 câu mới,4 game,8 ví dụ; đã đọc PDF8–28.')
