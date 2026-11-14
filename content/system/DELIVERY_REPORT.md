# Bàn giao học liệu tự học lớp 3 — Nguyễn Thế Khanh

Ngày bàn giao: 15/11/2026 (giờ Việt Nam). Repository duy nhất: [TOAN_TV_TA_LOP3](https://github.com/tranphuc2026abc-prog/TOAN_TV_TA_LOP3), nhánh `main`.

[Mở website học tập](https://tranphuc2026abc-prog.github.io/TOAN_TV_TA_LOP3/).

## Phạm vi đã hoàn thành

| Môn | Học liệu riêng | Câu hỏi có đáp án/giải thích | Trò chơi | Giáo viên đã duyệt | Chờ giáo viên |
| --- | ---: | ---: | ---: | ---: | ---: |
| Toán 3 Kết nối tri thức | 81/81 | 3240 | 81 | 4 | 77 |
| Tiếng Việt 3 Kết nối tri thức | 62/62 | 776 | 62 | 0 | 62 |
| Tiếng Anh 3 Global Success | 25/25 | 300 | 25 | 0 | 25 |
| **Tổng** | **168/168** | **4316** | **168** | **4** | **164** |

Tiếng Anh gồm Starter, Unit 1–20 và Review 1–4. Có 168 tệp JSON và 168 bản Markdown riêng, được tích hợp theo INDEX.json. Mỗi gói có mục tiêu, kiến thức, cách học, lỗi thường gặp, ví dụ có lời giải, luyện tập, phản hồi, đánh giá và trò chơi. Đây là số học liệu đã biên soạn và kiểm tra bằng AI, không phải số bài học sinh đã hoàn thành.

AI đã biên soạn 168/168 và kiểm tra 168/168; không còn mục chỉ có danh mục mà thiếu kho học liệu. Trạng thái chờ thẩm định của 164 mục vẫn là `AI_CHECKED_AWAITING_TEACHER`. Chỉ `TOAN3_T1_B01` đến `TOAN3_T1_B04` được ghi giáo viên duyệt theo xác nhận ngày 07/11/2026 trong APPROVALS.json. Không nâng trạng thái giáo viên duyệt cho các bài còn lại.

## Học liệu và nguồn

Sáu PDF ảnh quét trong nguồn dự án là căn cứ biên soạn. Các batch lưu trang nguồn và dấu vết đối chiếu trong gói bài, scripts và lịch sử PROGRESS.md/AUDIT_REPORT.md. Học liệu diễn giải, câu hỏi và hoạt động được biên soạn cho website; không đăng lại toàn văn SGK. Batch cuối Review 4 được đọc trực quan lại PDF Tiếng Anh tập 2, trang PDF 71–74 tương ứng trang in 70–73, ngày 15/11/2026.

Toán có 40 câu/bài theo 10 nhận biết, 10 thông hiểu, 20 vận dụng; mỗi lượt 10 câu theo 3/3/4. Hình cần thiết được gắn trong câu hỏi bằng tài nguyên SVG. Tiếng Việt luyện chi tiết bài đọc, từ/câu/chính tả/diễn đạt cùng nhiệm vụ nói và viết. Tiếng Anh có từ vựng, nghĩa Việt, ví dụ, mẫu câu, phát âm và hoạt động đọc/viết/nói; âm tổng hợp luôn được ghi là giọng máy, không phải âm thanh của sách.

## Tích hợp và kiểm thử

- Giữ giao diện, khóa dữ liệu `wl3:*`, hồ sơ, XP, sao, huy hiệu và sao lưu/khôi phục. Bộ tải theo INDEX.json có fallback từng file; renderer và validator phân biệt yêu cầu từng môn.
- Sửa điều hướng bị lặp khi mở trò chơi. Khi tải đủ, website hiển thị 168/168 cùng số 4 đã duyệt/164 chờ thẩm định; khi thiếu/tải lỗi vẫn báo đúng trạng thái.
- `npm test` kết thúc mã 0: validate_site.py, validate_content.py được gọi trong luồng kiểm tra, các hồi quy từng batch, test_complete_catalog.py và ba bộ DOM dùng jsdom đều đạt. Xem [nhật ký kiểm thử](FINAL_TEST_RESULTS.txt).
- DOM kiểm tra toàn bộ 168 kho: chọn lượt, đáp án/lời giải, chống cộng điểm lặp, trò chơi, hình, trạng thái thẩm định, lưu/nạp và fallback. Kiểm tra thêm cấu trúc ngôn ngữ và các nhánh giọng máy. Validator tính lại 2222 đẳng thức số trong lời giải.
- Trên Chrome của website đã triển khai: kiểm tra trang chủ đủ ba môn; mở Toán bài 1 (40 câu, lượt 3/3/4, trạng thái đã duyệt), Tiếng Việt “Một mái nhà chung” (nội dung theo bài, 12 câu và trò chơi), Review 4 (12 câu, từ vựng, các kỹ năng). Trò chơi Review 4 trả lời đúng tăng 10 điểm và hiện giải thích; chỉ có một thanh điều hướng. SVG thẻ màu Unit 9 đã được xem trên Chrome trong đợt kiểm tra trước.

Giới hạn kiểm thử: Chromium cục bộ bị môi trường chặn socket/ptrace nên đã dùng Chrome đám mây kiểm tra các mẫu nêu trên. Không tuyên bố đã kiểm tra thủ công giao diện của cả 168 bài trên mọi điện thoại. Nút nghe đã vào trạng thái “Đang đọc bằng giọng máy tiếng Anh”; chưa kiểm chứng chất lượng âm thanh thực nghe trên từng thiết bị. Kiểm tra tự động không thay thế thẩm định ngữ nghĩa và tính phù hợp sư phạm của giáo viên.

## Xác minh triển khai

Commit nội dung cuối: [6e744e2 — batch 44](https://github.com/tranphuc2026abc-prog/TOAN_TV_TA_LOP3/commit/6e744e2f6efe997ad774ffc0004a97a5675b8c7d).

Cả hai workflow tại commit này đã hoàn tất thành công: [43627754561](https://github.com/tranphuc2026abc-prog/TOAN_TV_TA_LOP3/actions/runs/43627754561) và [43627754157](https://github.com/tranphuc2026abc-prog/TOAN_TV_TA_LOP3/actions/runs/43627754157).

Đã đối chiếu toàn bộ 402 tệp công khai (168 JSON, 168 Markdown, các hình được tham chiếu và 5 tệp tích hợp): 402/402 trả HTTP 200 và SHA-256 khớp bản đã kiểm thử; không có lỗi tải hoặc sai khác.

Biên nhận [PAGES_VERIFICATION.json](PAGES_VERIFICATION.json) ghi đường dẫn, mã HTTP và SHA-256 thực nhận so với bản kiểm thử. Biên nhận xác minh commit nội dung trên; commit bàn giao chỉ bổ sung báo cáo, nhật ký và biên nhận. Lịch sử batch và kiểm tra trước được giữ trong [PROGRESS.md](PROGRESS.md) và [AUDIT_REPORT.md](AUDIT_REPORT.md).

## Sử dụng và thẩm định tiếp theo

Mở website, chọn môn và bài; đọc kiến thức rồi luyện tập hoặc chơi. Hồ sơ và tiến độ lưu trên trình duyệt hiện tại; dùng “Hồ sơ & sao lưu tiến độ” để xuất JSON và khôi phục trên thiết bị khác. Hệ thống không cung cấp đồng bộ tài khoản qua máy chủ.

Giáo viên có thể rà soát từng cặp JSON/Markdown: đối chiếu trang nguồn, kiểm tra câu hỏi, phương án nhiễu, đáp án, lời giải, hình và nhiệm vụ thực hành; thử bài trên website. Chỉ sau xác nhận rõ của thầy mới cập nhật APPROVALS.json và trạng thái duyệt tương ứng, rồi chạy lại validator và hồi quy. Nhiệm vụ nói/viết có tiêu chí tự đánh giá, không coi một câu mẫu là đáp án duy nhất.

Phần bàn giao còn chờ: thầy thẩm định 77 bài Toán, 62 bài Tiếng Việt và 25 mục Tiếng Anh. Không có yêu cầu duyệt từng batch để tiếp tục biên soạn. Khi xác minh bản bàn giao trên Pages xong, tạm dừng tác vụ tự động hoàn thiện học liệu lớp 3 theo yêu cầu; không dừng các tác vụ dự án khác.
