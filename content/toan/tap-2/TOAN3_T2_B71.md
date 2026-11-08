# Chia số có năm chữ số cho số có một chữ số

Nguồn tham khảo: Toán 3 KNTT, tập 2, trang 97-100.

Trạng thái: AI biên soạn và rà soát; chưa có xác nhận của giáo viên.

## Mục tiêu

- Chia hết và chia có dư trong phạm vi 100000.
- Ghi đủ các chữ số 0 của thương.
- Kiểm tra ngược và giải bài chia nhiều tầng.

## Khám phá

Chia từ trái sang phải. Mỗi lượt gồm chia, nhân, trừ, hạ chữ số tiếp theo. Đã bắt đầu viết thương thì phải giữ vị trí hàng có thương 0.

- Số dư bé hơn số chia.
- Thương nhân số chia cộng số dư bằng số bị chia.
- Chỉ nhóm đầy thì lấy thương; chứa hết khi còn dư cần thêm một nhóm.

## Hướng dẫn

1. Lấy đủ chữ số đầu để bắt đầu chia.
2. Chia, nhân, trừ rồi hạ từng chữ số.
3. Kiểm tra số dư và nhân ngược.
4. Đọc ngữ cảnh trước khi chọn số nhóm.

## Lỗi thường gặp

- Bỏ 0 ở giữa hoặc cuối thương.
- Ghi số dư bằng hoặc lớn hơn số chia.
- Chưa chứa hết mà chỉ lấy số nhóm đầy.

## Ví dụ

Tính 60024 : 6.

1. 6 chia 6 được 1.
2. Hai lượt hạ 0 tiếp theo đều phải viết 0 trong thương.
3. Hạ 2 chưa đủ chia, viết 0; hạ 4 thành 24, chia được 4.
4. Thương 10004; kiểm tra 10004 × 6 = 60024.

Có 20003 thẻ, mỗi hộp tối đa 4 thẻ.

1. 5000 × 4 + 3 = 20003.
2. Cần 5000 hộp đầy và một hộp cho 3 thẻ lẻ: 5001 hộp.

## Ngân hàng câu hỏi

### Câu 1 - nhan_biet

Tính 24630 : 3.

A. 8210; B. 821; C. 8201; D. 8310

Đáp án: 8210. Lời giải: 24630 : 3 = 8210; giữ chữ số 0 cuối thương.

### Câu 2 - nhan_biet

Chia 36000 cho 4, thương là bao nhiêu?

Đáp án: 9000. Lời giải: 36 nghìn chia bốn bằng chín nghìn.

### Câu 3 - nhan_biet

Tính 50505 : 5.

A. 10101; B. 111; C. 1101; D. 1011

Đáp án: 10101. Lời giải: 50505 : 5 = 10101; không bỏ hai chữ số 0 trong thương.

### Câu 4 - nhan_biet

Khi hạ chữ số trong phép chia đặt dọc, hạ từ trái sang phải hay ngược lại?

Đáp án: trái sang phải. Lời giải: Chia từ hàng cao nhất và hạ từng chữ số còn lại theo thứ tự.

### Câu 5 - nhan_biet

Trong phép chia cho 6, số dư lớn nhất có thể là mấy?

A. 5; B. 6; C. 7; D. 0

Đáp án: 5. Lời giải: Số dư phải bé hơn 6 nên lớn nhất là 5.

### Câu 6 - nhan_biet

Số bị chia 14000, số chia 7. Thương là gì?

Đáp án: 2000. Lời giải: 14000 : 7 = 2000.

### Câu 7 - nhan_biet

Tính 12345 : 1.

A. 12345; B. 1; C. 0; D. 12344

Đáp án: 12345. Lời giải: Chia một số cho 1 giữ nguyên số đó.

### Câu 8 - nhan_biet

Phép chia có thương 7000, số chia 3, không dư. Số bị chia là gì?

Đáp án: 21000. Lời giải: 7000 × 3 = 21000.

### Câu 9 - nhan_biet

Trong phép chia có dư, số dư có được bằng số chia không?

A. không; B. có; C. chỉ khi chia 5; D. luôn bằng

Đáp án: không. Lời giải: Nếu dư bằng số chia thì còn đủ thêm một nhóm, phải tăng thương.

### Câu 10 - nhan_biet

Tính 80808 : 8.

Đáp án: 10101. Lời giải: 80808 : 8 = 10101; mỗi vị trí thương phải được giữ.

### Câu 11 - thong_hieu

Một bạn chia 32016 cho 4 được 804. Bạn đã bỏ sót chữ số nào trong thương đúng?

A. 0; B. 1; C. 2; D. 4

Đáp án: 0. Lời giải: Thương đúng 8004; bạn bỏ một chữ số 0.

### Câu 12 - thong_hieu

Chia 27431 cho 3, biết thương 9143. Số dư là bao nhiêu?

Đáp án: 2. Lời giải: 9143 × 3 = 27429; còn 2.

### Câu 13 - thong_hieu

Một phép chia cho 4 được ghi thương 2750 dư 5. Thương sau khi sửa là gì?

A. 2751; B. 2750; C. 2752; D. 2749

Đáp án: 2751. Lời giải: Dư 5 còn đủ một nhóm 4; thương tăng 1, dư mới 1.

### Câu 14 - thong_hieu

Để kiểm tra 17402 chia 5 được 3480 dư 2, phải cộng gì vào tích 3480 × 5?

Đáp án: 2. Lời giải: Thương nhân số chia rồi cộng số dư để được số bị chia.

### Câu 15 - thong_hieu

Một số năm chữ số bắt đầu bằng 8 chia cho 2. Thương có mấy chữ số?

A. 5; B. 4; C. 3; D. 6

Đáp án: 5. Lời giải: Chữ số đầu 8 chia được 2 ngay nên thương có đủ năm vị trí.

### Câu 16 - thong_hieu

Một số năm chữ số bắt đầu bằng 1 chia cho 8. Thương có mấy chữ số?

Đáp án: 4. Lời giải: Cần dùng hai chữ số đầu để bắt đầu chia, nên thương có bốn chữ số.

### Câu 17 - thong_hieu

Chia 70004 cho 7, chỉ ghi số dư.

A. 4; B. 0; C. 1; D. 7

Đáp án: 4. Lời giải: 10000 × 7 + 4 = 70004.

### Câu 18 - thong_hieu

Trong phép chia 45000 : 9, có thể bỏ các số 0 cuối thương không?

Đáp án: không. Lời giải: Thương là 5000; bỏ số 0 làm thay đổi giá trị.

### Câu 19 - thong_hieu

Nếu chia 19200 cho 3 được 6400 thì 19200 chia cho 6 được bao nhiêu?

A. 3200; B. 6400; C. 12800; D. 6300

Đáp án: 3200. Lời giải: Chia thành sáu phần thì mỗi phần bằng nửa khi chia thành ba phần: 3200.

### Câu 20 - thong_hieu

Một số chia 5 dư 4. Muốn chia hết cho 5 bằng cách thêm ít nhất, cần thêm mấy đơn vị?

Đáp án: 1. Lời giải: Dư 4 thêm 1 đủ một nhóm 5.

### Câu 21 - van_dung

Có 18006 trang được in đều trong 6 ngày. Máy in hỏng một ngày nên chỉ làm được đúng 5 ngày theo năng suất ấy. Đã in bao nhiêu trang?

A. 15005; B. 18001; C. 15000; D. 3001

Đáp án: 15005. Lời giải: Mỗi ngày 3001 trang; 3001 × 5 = 15005 trang.

### Câu 22 - van_dung

Xưởng chia 23456 nhãn cho 8 người bằng nhau. Một người trả lại 432 nhãn chưa dùng. Người đó đã dùng bao nhiêu nhãn?

Đáp án: 2500. Lời giải: Mỗi người nhận 2932 nhãn; 2932 - 432 = 2500.

### Câu 23 - van_dung

Một cuốn sách mô hình có 12024 trang, chia đều vào 3 tập. Mỗi tập có 8 trang mục lục nằm trong tổng đó. Mỗi tập có bao nhiêu trang khác mục lục?

A. 4000; B. 4008; C. 4016; D. 12000

Đáp án: 4000. Lời giải: Một tập 4008 trang; bớt 8 trang mục lục còn 4000.

### Câu 24 - van_dung

Kho có 25001 chi tiết, đóng hộp đúng 5 chi tiết. Một hộp chưa đầy có bao nhiêu chi tiết?

Đáp án: 1. Lời giải: 5000 hộp đầy dùng 25000 chi tiết, còn 1.

### Câu 25 - van_dung

Một máy báo 42005 chia 6 được 7000 dư 5. Chỉ cần thêm ít nhất bao nhiêu chi tiết để đóng thêm một nhóm 6?

A. 1; B. 5; C. 6; D. 0

Đáp án: 1. Lời giải: Phần lẻ có 5 chi tiết, thêm 1 đủ nhóm 6.

### Câu 26 - van_dung

Tổng chiều dài 4 đoạn dây bằng nhau là 30300 cm. Một đoạn được cắt ngắn 75 cm. Đoạn bị cắt còn bao nhiêu xăng-ti-mét?

Đáp án: 7500. Lời giải: Ban đầu mỗi đoạn 7575 cm; 7575 - 75 = 7500.

### Câu 27 - van_dung

Một xe cần 7 chuyến đều nhau để chở 21014 kg. Sau 2 chuyến, đã chở bao nhiêu ki-lô-gam?

A. 6004; B. 3002; C. 6000; D. 42028

Đáp án: 6004. Lời giải: Mỗi chuyến 3002 kg; hai chuyến 6004 kg.

### Câu 28 - van_dung

Có 16500 hạt chia đều cho 5 nhóm. Nhóm thứ nhất chia tiếp đều cho 3 bạn. Mỗi bạn nhóm đó nhận bao nhiêu hạt?

Đáp án: 1100. Lời giải: Mỗi nhóm 3300 hạt; 3300 : 3 = 1100 hạt.

### Câu 29 - van_dung

Đội A chia 24000 nhãn cho 6 tổ, đội B chia 24000 nhãn cho 8 tổ. Mỗi tổ đội A nhận hơn mỗi tổ đội B bao nhiêu nhãn?

A. 1000; B. 3000; C. 4000; D. 2000

Đáp án: 1000. Lời giải: A mỗi tổ 4000 nhãn, B mỗi tổ 3000 nhãn; hơn 1000.

### Câu 30 - van_dung

Một túi chứa tối đa 9 hạt giống đặc biệt. Có 18001 hạt. Sau khi dùng đủ 2000 túi đầy còn cần mấy túi nữa để chứa hết?

Đáp án: 1. Lời giải: 2000 túi đầy chứa 18000 hạt; còn 1 hạt cần một túi nữa.

### Câu 31 - van_dung

Mỗi hộp chứa đúng 8 thẻ. Trong 32007 thẻ, phần không đóng đủ hộp ít hơn 8 thẻ bao nhiêu thẻ?

A. 1; B. 7; C. 8; D. 0

Đáp án: 1. Lời giải: Dư 7 thẻ; từ 7 đến 8 còn thiếu 1.

### Câu 32 - van_dung

Một đoàn có 27018 người chia đều thành 9 nhóm. Mỗi nhóm có 2 người hướng dẫn. Mỗi nhóm còn bao nhiêu người không làm hướng dẫn?

Đáp án: 3000. Lời giải: Mỗi nhóm 3002 người; bớt 2 người hướng dẫn còn 3000.

### Câu 33 - van_dung

Một kho có 56000 nhãn. Mỗi gói 7 nhãn. Đã phát 3000 gói đầy, còn bao nhiêu gói đầy?

A. 5000; B. 8000; C. 53000; D. 21000

Đáp án: 5000. Lời giải: Có 8000 gói; phát 3000 còn 5000 gói.

### Câu 34 - van_dung

Dây 41005 cm được cắt thành 5 đoạn bằng nhau. Hai đoạn ghép lại, không hao hụt, dài bao nhiêu xăng-ti-mét?

Đáp án: 16402. Lời giải: Một đoạn 8201 cm; hai đoạn 16402 cm.

### Câu 35 - van_dung

Một số chia 4 có thương 6000 dư 3. Bớt số đó 3 rồi chia 4, thương là gì?

A. 6000; B. 5999; C. 6001; D. 24000

Đáp án: 6000. Lời giải: Bớt đúng phần dư thì còn 24000; chia 4 vẫn được 6000.

### Câu 36 - van_dung

Nhóm có 36018 viên sỏi. Sau khi bỏ 18 viên, chia đều vào 6 rổ. Mỗi rổ bao nhiêu viên?

Đáp án: 6000. Lời giải: Còn 36000 viên; 36000 : 6 = 6000.

### Câu 37 - van_dung

Một số chia 8 được 1500 dư 7. Bớt 8 khỏi số ban đầu rồi chia lại, số dư là mấy?

A. 7; B. 6; C. 0; D. 8

Đáp án: 7. Lời giải: Bớt đúng một nhóm 8 làm thương giảm 1; số dư vẫn 7.

### Câu 38 - van_dung

Chia 40000 tấm bìa đều vào 5 thùng. Sau đó lấy 1250 tấm từ mỗi thùng. Tổng số bìa còn trong 5 thùng là bao nhiêu?

Đáp án: 33750. Lời giải: Mỗi thùng 8000 tấm, còn 6750 tấm; 6750 × 5 = 33750.

### Câu 39 - van_dung

Máy chia 54006 thành 6 phần bằng nhau, rồi bớt 1000 ở mỗi phần. Mỗi phần mới là bao nhiêu?

A. 8001; B. 9001; C. 8000; D. 53006

Đáp án: 8001. Lời giải: 54006 : 6 = 9001; bớt 1000 còn 8001.

### Câu 40 - van_dung

Có 24010 hạt chia đều vào 7 túi, chỉ dùng số hạt nguyên. Mỗi túi nhận 3430 hạt. Số hạt còn lại có phải bằng 0 không?

Đáp án: có. Lời giải: 3430 × 7 = 24010, chia hết.

## Trò chơi

Ghép thương và phần dư: Trả lời các nhiệm vụ trong bài, xem lời giải và thử lại để củng cố cách làm.

- Mỗi lượt chọn 5 câu có 5 đáp án khác nhau.
- Chọn câu hỏi bên trái rồi đáp án bên phải. Sai thì thử lại.
- Mỗi cặp đúng 10 điểm; tối đa 50 điểm.

## Đánh giá

Đúng lần đầu: 1 điểm; đúng sau một gợi ý: 0,5 điểm. Từ 90%: 3 sao; từ 60%: 2 sao; còn lại: 1 sao.

Xem lời giải các câu sai, đọc lại quy tắc, rồi làm một lượt mới.
