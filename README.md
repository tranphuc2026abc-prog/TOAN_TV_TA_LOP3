# Hành trình tri thức – Lớp 3

Website tự học Toán, Tiếng Việt và Tiếng Anh cho học sinh lớp 3.

[Mở website](https://tranphuc2026abc-prog.github.io/TOAN_TV_TA_LOP3/) · [Lịch sử học liệu](content/system/PROGRESS.md)

| Môn | Mục học | Câu luyện tập | Trò chơi theo bài |
| --- | ---: | ---: | ---: |
| Toán | 81 | 3.240 | 81 |
| Tiếng Việt | 62 | 776 | 62 |
| Tiếng Anh | 25 | 300 | 25 |
| Tổng | 168 | 4.316 | 168 |

Học liệu theo Toán và Tiếng Việt Kết nối tri thức với cuộc sống, Tiếng Anh Global Success. 25 mục Tiếng Anh gồm Starter, 20 Unit và 4 Review. Tiến độ lưu theo hồ sơ trên trình duyệt. Có thể xuất và nhập bản sao lưu trong mục Hồ sơ.

## Rà soát học liệu

Đối chiếu ở mức danh mục với [Chương trình GDPT ban hành theo Thông tư 32/2018/TT-BGDĐT](https://moet.gov.vn/content/vanban/Lists/VBPQ/Attachments/1483/vbhn-ttu-322018-202021-132022-ttbgddt.pdf). [Thông tư 17/2025/TT-BGDĐT](https://vanban.chinhphu.vn/?docid=215347&pageid=27160) điều chỉnh nội dung ở các môn khác với phạm vi ba môn của dự án.

| Môn | Mạch nội dung thể hiện trong danh mục và học liệu |
| --- | --- |
| Toán | Số và phép tính đến 100.000, hình học và đo lường, bảng số liệu và khả năng xảy ra của sự kiện |
| Tiếng Việt | Đọc hiểu, luyện từ và câu, chính tả, viết, nói và nghe |
| Tiếng Anh | Từ vựng, mẫu câu, phát âm và thực hành nghe, nói, đọc, viết theo chủ đề gần gũi |

Kiểm tra trực tiếp 168 tệp JSON theo chỉ mục: mỗi câu có ID riêng, nội dung, đáp án và lời giải. Mỗi câu trắc nghiệm có đúng một lựa chọn khớp đáp án lưu trong dữ liệu. Tính lại 234 phép tính một bước có đề và đáp án xác định được bằng mẫu văn bản, tất cả khớp. Bốn bài Toán đầu đã được giáo viên duyệt, 164 mục còn chờ giáo viên duyệt theo [APPROVALS.json](content/system/APPROVALS.json). Việc đối chiếu từng yêu cầu cần đạt và kiểm định từng câu ngôn ngữ cần rà soát chuyên môn riêng.

## Chạy kiểm thử

Cài Node.js và Python 3, sau đó chạy `npm ci` và `npm test`. Bộ kiểm thử bao gồm kiểm tra dữ liệu, hồi quy và các luồng DOM. Website dùng HTML, CSS và JavaScript thuần.
