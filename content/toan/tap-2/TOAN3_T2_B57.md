# Chia số có bốn chữ số cho số có một chữ số

Nguồn tham khảo: Toán 3 KNTT, tập 2, trang 47-51.

Trạng thái: AI biên soạn và rà soát; chưa có xác nhận của giáo viên.

## Mục tiêu

- Thực hiện chia từ hàng cao nhất, ghi đúng các chữ số của thương.
- Phân biệt chia hết và chia có dư; số dư bé hơn số chia.
- Vận dụng chia đều, một phần của số và số nhóm/đồ chứa cần thiết.

## Khám phá

Chia đều một lượng lớn có thể làm lần lượt từ trái sang phải. Ở mỗi lượt, chia, nhân, trừ rồi hạ chữ số tiếp theo. Nếu đã bắt đầu viết thương mà một lượt chưa đủ chia, vẫn phải ghi chữ số 0 ở hàng đó.

- Lấy đủ chữ số đầu để bắt đầu chia; tiếp tục hạ từng chữ số một.
- Mỗi lượt: chia, nhân, trừ, hạ. Không bỏ lượt có thương 0.
- Số bị chia bằng thương nhân số chia rồi cộng số dư.
- Số dư phải không âm và bé hơn số chia; dư 0 là chia hết.
- Đếm nhóm đầy chỉ lấy thương; muốn chứa hết mà còn dư cần thêm một đồ chứa.

## Hướng dẫn

1. Đặt phép chia, xét một hoặc hai chữ số đầu.
2. Chọn chữ số thương phù hợp; nhân và trừ để biết phần dư tạm.
3. Hạ chữ số tiếp theo; ghi đủ các chữ số thương, kể cả 0.
4. Cuối cùng kiểm tra số dư và nhân ngược.
5. Đọc ngữ cảnh để quyết định chỉ nhóm đầy hay cần thêm một nhóm cho phần dư.

## Lỗi thường gặp

- Bỏ chữ số 0 giữa hoặc cuối thương.
- Dừng khi còn chữ số chưa hạ.
- Ghi số dư bằng hoặc lớn hơn số chia.
- Lấy thương làm số hộp cần thiết dù còn vật chưa đựng.

## Ví dụ

Tính 7248 : 6.

1. 7 chia 6 được 1, dư 1; hạ 2 thành 12.
2. 12 chia 6 được 2, dư 0; hạ 4.
3. 4 chia 6 được 0, viết 0; hạ 8 thành 48.
4. 48 chia 6 được 8, hết dư. Thương là 1208.
5. Kiểm tra 1208 × 6 = 7248.

Có 2227 quả, mỗi hộp tối đa 4 quả. Cần ít nhất bao nhiêu hộp?

1. 556 × 4 + 3 = 2227; có 556 hộp đầy và 3 quả lẻ.
2. Để đựng hết cần thêm một hộp: 557 hộp.

## Ngân hàng câu hỏi

### Câu 1 - nhan_biet

Tính 8424 : 4.

A. 2106; B. 216; C. 2016; D. 2104

Đáp án: 2106. Lời giải: 8424 : 4 = 2106; không bỏ chữ số 0 ở hàng chục của thương.

### Câu 2 - nhan_biet

Nhẩm 6000 : 3.

Đáp án: 2000. Lời giải: Sáu nghìn chia ba phần bằng nhau, mỗi phần hai nghìn.

### Câu 3 - nhan_biet

Tính 4848 : 2.

A. 2424; B. 2244; C. 2404; D. 9696

Đáp án: 2424. Lời giải: Chia lần lượt các hàng từ trái sang phải được 2424.

### Câu 4 - nhan_biet

Trong phép chia đặt dọc, bắt đầu xét từ bên nào? Viết trái hoặc phải.

Đáp án: trái. Lời giải: Bắt đầu từ hàng cao nhất bên trái, khác với cộng và nhân đặt dọc.

### Câu 5 - nhan_biet

Số dư của phép chia cho 5 phải bé hơn số nào?

A. 5; B. 4; C. 6; D. 10

Đáp án: 5. Lời giải: Số dư luôn bé hơn số chia, ở đây là 5.

### Câu 6 - nhan_biet

Tính 3150 : 5.

Đáp án: 630. Lời giải: 31 chia 5 được 6 dư 1, hạ 5 được 15 chia 5 được 3, hạ 0 được 0; thương 630.

### Câu 7 - nhan_biet

Số chia là 4, thương là 502, số dư là 3. Số bị chia là bao nhiêu?

A. 2011; B. 2008; C. 2012; D. 2005

Đáp án: 2011. Lời giải: 502 × 4 + 3 = 2011.

### Câu 8 - nhan_biet

Tính 7070 : 7.

Đáp án: 1010. Lời giải: 7070 : 7 = 1010; phải ghi đủ các chữ số 0 trong thương.

### Câu 9 - nhan_biet

Chia 1000 cho 1 được bao nhiêu?

A. 1000; B. 1; C. 0; D. 100

Đáp án: 1000. Lời giải: Một số chia cho 1 bằng chính số đó.

### Câu 10 - nhan_biet

Một phép chia cho 3 có dư 0. Phép chia đó có phải chia hết không?

Đáp án: có. Lời giải: Số dư bằng 0 nghĩa là chia hết.

### Câu 11 - thong_hieu

Tính 2564 : 4.

A. 641; B. 640; C. 614; D. 651

Đáp án: 641. Lời giải: 25 chia 4 được 6 dư 1; hạ 6 được 16, chia được 4; hạ 4 chia được 1. Thương 641.

### Câu 12 - thong_hieu

Tính 4703 : 5; viết theo mẫu “thương dư số dư”.

Đáp án: 940 dư 3. Lời giải: 940 × 5 + 3 = 4703; số dư 3 bé hơn 5.

### Câu 13 - thong_hieu

Bạn viết 6030 : 3 = 21 vì bỏ các chữ số 0. Thương đúng là bao nhiêu?

A. 2010; B. 210; C. 2001; D. 2030

Đáp án: 2010. Lời giải: 6030 : 3 = 2010; các hàng có thương 0 vẫn cần ghi.

### Câu 14 - thong_hieu

Chia 3210 cho 8 được thương 401. Số dư bao nhiêu?

Đáp án: 2. Lời giải: 401 × 8 = 3208; 3210 - 3208 = 2, bé hơn 8.

### Câu 15 - thong_hieu

Một bạn ghi 2080 chia 6 được 345 dư 10. Sau điều chỉnh, thương đúng là bao nhiêu?

A. 346; B. 345; C. 347; D. 344

Đáp án: 346. Lời giải: Dư 10 còn đủ thêm một nhóm 6; 346 × 6 + 4 = 2080.

### Câu 16 - thong_hieu

Tính 5004 : 6.

Đáp án: 834. Lời giải: 50 chia 6 được 8 dư 2; hạ 0 được 20, chia được 3 dư 2; hạ 4 được 24, chia được 4.

### Câu 17 - thong_hieu

Muốn kiểm tra 8245 chia 4 được 2061 dư 1, tính 2061 × 4 rồi cộng số nào?

A. 1; B. 4; C. 2061; D. 8245

Đáp án: 1. Lời giải: Thương nhân số chia cộng số dư bằng số bị chia; cộng 1.

### Câu 18 - thong_hieu

Một số có bốn chữ số chia 9, số đầu bên trái là 1. Lần chia đầu có cần lấy hai chữ số đầu không?

Đáp án: có. Lời giải: Một nghìn chia 9 chưa đủ một nghìn trong thương nên xét hai chữ số đầu để bắt đầu.

### Câu 19 - thong_hieu

Trong phép chia 4080 : 4, thương có mấy chữ số?

A. 4; B. 2; C. 3; D. 5

Đáp án: 4. Lời giải: 4080 : 4 = 1020, gồm bốn chữ số, kể cả hai chữ số 0.

### Câu 20 - thong_hieu

Chia 1867 cho 3. Chỉ ghi số dư.

Đáp án: 1. Lời giải: 622 × 3 + 1 = 1867, số dư là 1.

### Câu 21 - van_dung

Có 3608 chiếc cúc chia đều vào 4 túi. Mỗi túi bao nhiêu chiếc?

A. 902; B. 92; C. 920; D. 904

Đáp án: 902. Lời giải: 3608 : 4 = 902 chiếc mỗi túi.

### Câu 22 - van_dung

Có 4523 quả cam, mỗi hộp 6 quả. Đóng được nhiều nhất bao nhiêu hộp đầy?

Đáp án: 753. Lời giải: 753 × 6 + 5 = 4523; đóng 753 hộp đầy, còn 5 quả.

### Câu 23 - van_dung

Có 4523 quả cam, mỗi hộp tối đa 6 quả. Cần ít nhất bao nhiêu hộp để đựng hết?

A. 754; B. 753; C. 752; D. 755

Đáp án: 754. Lời giải: 753 hộp đầy còn 5 quả, cần thêm một hộp; tổng 754 hộp.

### Câu 24 - van_dung

Một sợi dây 7400 cm chia thành 8 đoạn bằng nhau. Mỗi đoạn bao nhiêu xăng-ti-mét?

Đáp án: 925. Lời giải: 7400 : 8 = 925 cm.

### Câu 25 - van_dung

Bốn đội trồng tổng 6284 cây, số cây mỗi đội bằng nhau. Một đội trồng bao nhiêu cây?

A. 1571; B. 1561; C. 1570; D. 1671

Đáp án: 1571. Lời giải: 6284 : 4 = 1571 cây.

### Câu 26 - van_dung

Kho có 5290 kg thóc, xuất một phần năm số đó. Đã xuất bao nhiêu ki-lô-gam?

Đáp án: 1058. Lời giải: Một phần năm của 5290 là 5290 : 5 = 1058 kg.

### Câu 27 - van_dung

Kho có 5290 kg thóc, xuất một phần năm số đó. Còn bao nhiêu ki-lô-gam?

A. 4232; B. 1058; C. 4242; D. 5295

Đáp án: 4232. Lời giải: Đã xuất 1058 kg; 5290 - 1058 = 4232 kg.

### Câu 28 - van_dung

Một trường có 1825 chiếc ghế, xếp mỗi hàng 7 chiếc. Xếp được nhiều nhất bao nhiêu hàng đủ 7 chiếc?

Đáp án: 260. Lời giải: 260 × 7 + 5 = 1825; có 260 hàng đủ và 5 ghế lẻ.

### Câu 29 - van_dung

Một xe đi 4872 m trong 6 phút, mỗi phút đi đều nhau. Mỗi phút đi bao nhiêu mét?

A. 812; B. 82; C. 821; D. 802

Đáp án: 812. Lời giải: 4872 : 6 = 812 m.

### Câu 30 - van_dung

Có 2050 hạt chia đều vào 4 hộp, chỉ chia số hạt nguyên. Sau khi mỗi hộp nhận nhiều nhất bằng nhau, còn mấy hạt?

Đáp án: 2. Lời giải: 512 × 4 + 2 = 2050; còn 2 hạt.

### Câu 31 - van_dung

Ba bao gạo nặng bằng nhau có tổng 4500 kg. Một bao được chia thành 5 phần bằng nhau. Mỗi phần bao nhiêu ki-lô-gam?

A. 300; B. 900; C. 1500; D. 100

Đáp án: 300. Lời giải: Một bao 1500 kg; 1500 : 5 = 300 kg.

### Câu 32 - van_dung

Có 6408 tờ giấy chia đều cho 8 lớp. Mỗi lớp dùng 200 tờ. Mỗi lớp còn bao nhiêu tờ?

Đáp án: 601. Lời giải: Mỗi lớp nhận 801 tờ; 801 - 200 = 601 tờ.

### Câu 33 - van_dung

Tấm vải 3225 cm cắt các đoạn 4 cm. Phần vải thừa không đủ một đoạn dài bao nhiêu xăng-ti-mét?

A. 1; B. 0; C. 2; D. 4

Đáp án: 1. Lời giải: 806 × 4 + 1 = 3225; còn 1 cm.

### Câu 34 - van_dung

Một máy làm 5607 sản phẩm trong 7 ngày, mỗi ngày bằng nhau. Mỗi ngày làm bao nhiêu sản phẩm?

Đáp án: 801. Lời giải: 5607 : 7 = 801; không bỏ chữ số 0 hàng chục.

### Câu 35 - van_dung

Có 1980 viên bi chia đều vào 9 hộp. Hai hộp chứa tổng bao nhiêu viên?

A. 440; B. 220; C. 990; D. 396

Đáp án: 440. Lời giải: Mỗi hộp 220 viên; hai hộp 220 × 2 = 440 viên.

### Câu 36 - van_dung

Một vườn có 3120 cây, chia đều thành 4 khu. Khu A có thêm 120 cây mới. Lúc này khu A có bao nhiêu cây?

Đáp án: 900. Lời giải: Ban đầu mỗi khu 780 cây; thêm 120 được 900 cây.

### Câu 37 - van_dung

Nhà máy có 9015 viên gạch, mỗi xe chở tối đa 8 viên trong mô hình đồ chơi. Cần ít nhất bao nhiêu chuyến để chở hết?

A. 1127; B. 1126; C. 1125; D. 1128

Đáp án: 1127. Lời giải: 1126 × 8 + 7 = 9015; còn 7 viên nên cần thêm một chuyến.

### Câu 38 - van_dung

Một số chia 7 được 305 dư 6. Nếu thêm 1 vào số đó rồi chia 7 thì thương mới là bao nhiêu?

Đáp án: 306. Lời giải: Số ban đầu 2141; thêm 1 được 2142, gồm 306 nhóm 7.

### Câu 39 - van_dung

Lớp có 1736 nhãn chia đều cho 7 tổ. Mỗi tổ tặng 48 nhãn cho thư viện. Mỗi tổ còn bao nhiêu nhãn?

A. 200; B. 248; C. 1688; D. 240

Đáp án: 200. Lời giải: Mỗi tổ nhận 248 nhãn; 248 - 48 = 200 nhãn.

### Câu 40 - van_dung

Một đội chia 2825 cây giống vào 5 luống bằng nhau. Sau đó mỗi luống thêm 35 cây. Mỗi luống lúc này có bao nhiêu cây?

Đáp án: 600. Lời giải: 2825 : 5 = 565; 565 + 35 = 600 cây.

## Trò chơi

Ghép thương và số dư: Ghép năm nhiệm vụ với các kết quả khác nhau; ghi đủ chữ số 0 trong thương.

- Mỗi lượt chọn 5 câu có 5 đáp án khác nhau.
- Chọn câu hỏi bên trái rồi đáp án bên phải. Sai thì thử lại.
- Mỗi cặp đúng 10 điểm; tối đa 50 điểm.

## Đánh giá

Đúng lần đầu: 1 điểm; đúng sau một gợi ý: 0,5 điểm. Từ 90%: 3 sao; từ 60%: 2 sao; còn lại: 1 sao.

Xem lời giải các câu sai, đọc lại quy tắc, rồi làm một lượt mới.
