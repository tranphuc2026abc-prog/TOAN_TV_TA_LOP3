# Đối chiếu nguồn Batch 10 — 08/11/2026

Trạng thái: SOURCE_REVIEWED_NOT_AUTHORED. Chưa có đủ học liệu hoặc ngân hàng 40 câu/bài; không cộng vào số bài hoàn thiện.

Đã render và đọc trực quan toàn bộ trang PDF 100–113 của bản Toán tập 1 đang truy cập được trong môi trường, tương ứng trang in 99–112. Chưa đối chiếu hash bản này với PDF trong repo.

## Bài 37 — trang 99–103

Chia từ trái sang phải; lượt đầu có thể lấy hai chữ số khi hàng trăm nhỏ hơn số chia. Mỗi lượt chia, nhân, trừ, hạ chữ số tiếp. Phải ghi chữ số 0 trong thương ở lượt chưa chia đủ. Có chia hết và chia có dư; số dư cuối nhỏ hơn số chia. Phạm vi gồm vận dụng giảm số lần, nhóm bằng nhau và các tình huống hai bước.

Ví dụ mới để phát triển: 816 chia 4 có thương 204. Sau 8 chia 4, hạ 1 chưa đủ chia 4 nên ghi 0; hạ 6 thành 16 rồi chia được 4. Kiểm tra 204 × 4 = 816. Với 827 chia 4, thương 206 dư 3; kiểm tra 206 × 4 + 3 = 827. Tránh bỏ 0 làm thương thành 24 hoặc 26.

## Bài 38 — trang 104–108

Phân biệt biểu thức với giá trị. Chỉ cộng/trừ hoặc chỉ nhân/chia: làm từ trái sang phải. Có cả hai nhóm phép tính: nhân/chia trước, cộng/trừ sau. Có ngoặc: trong ngoặc trước. Có nhận xét nhóm số cộng để tính thuận tiện; không tự đổi thứ tự phép trừ/chia.

Ví dụ mới: 54 - 18 : 3 có giá trị 48 vì chia trước. (54 - 18) : 3 có giá trị 12 vì ngoặc trước. 48 : 6 × 2 có giá trị 16 vì nhân/chia cùng mức, làm từ trái sang phải. Phải kiểm tra validator với biểu thức có ngoặc, không chỉ regex lấy một đoạn biểu thức.

## Bài 39 — trang 109–110

Tìm số lớn gấp mấy lần số bé bằng chia số lớn cho số bé; trả lời đơn vị lần. Phân biệt hơn bao nhiêu đơn vị dùng trừ. Số đo cần cùng đơn vị trước khi chia. Phạm vi có đọc bảng, độ dài, hàng/cột và tình huống vận chuyển.

Ví dụ mới: 45 thẻ so với 9 thẻ là gấp 5 lần, nhưng hơn 36 thẻ. Dây 8 cm so với dây 20 mm: đổi 8 cm thành 80 mm rồi chia 20 được 4 lần. Cần SVG mới nếu dùng câu phụ thuộc sơ đồ hoặc hàng/cột.

## Bài 40 — trang 111–112

Ôn nhân/chia ba chữ số, gấp/giảm, tìm số lần, tính biểu thức có ngoặc và hai bước. Có cách nhóm phép nhân để tính thuận tiện. Không sao chép trò chơi, toàn văn hay hệ thống câu hỏi SGK.

Ví dụ mới: (7 × 4) × 5 và 7 × (4 × 5) cùng bằng 140. Nhóm 4 × 5 trước giúp tính nhẩm. Nhóm A có 135 hạt, nhóm B gấp 3 lần: B có 405 hạt, cả hai có 540 hạt.

## Việc cần làm tiếp

Biên soạn riêng 160 câu cùng phương án nhiễu, lời giải và 4 trò chơi; bổ sung mục tiêu, hướng dẫn, lỗi thường gặp, ví dụ, đánh giá và JSON/Markdown từng bài. Chưa tạo các tệp bài để bộ tải không hiểu nhầm bản nháp là học liệu đủ. Kiểm thử toàn bộ hồi quy trước khi commit batch nội dung. Chỉ bài 1–4 được giáo viên duyệt.
