# Batch 17 đã tích hợp — 08/11/2026

Toán 65–68: 4 JSON/Markdown, 160 câu mới (10/10/20 mỗi bài), 4 trò chơi, 3 SVG tự dựng và 3 hoạt động thực hành giấy/đồng hồ/lịch/thẻ mệnh giá. Đã đọc trực quan trang in 76–87 (PDF 77–88) của chính Toán tập 2 trong repo, blob SHA 1a55eb09c9cf573935fa38911d48a5311575b09c. Nội dung ôn cộng/trừ có ngoặc, xem giờ tới từng phút, tháng/năm, lập lịch, khoảng thời gian, đổi tiền và tiền thừa. Câu hỏi và tình huống mới, không chép hệ thống bài tập sách.

Hình đồng hồ có 60 vạch, kim giờ dịch theo phút; lịch tự dựng là tháng 6/2026, ngày 1 thứ Hai. Đã render và xem cả ba SVG, nhãn không chồng. Mỗi câu phụ thuộc hình đều gắn hình ngay trong câu hỏi. Tiền trong bài là giá giả định, hoạt động dùng thẻ học tập không dùng làm tiền thật.

npm test toàn bộ đạt trên 68 bài/2720 câu: dữ liệu, Markdown, 2143 đẳng thức lời giải, hồi quy cũ và DOM. Hồi quy mới: biểu thức có/không ngoặc, 160 đáp án neo, datetime/calendar, tọa độ 30 ngày và kim giờ/phút, tham chiếu SVG, tiền thừa và hai bước. DOM giữ luyện tập 10 câu 3/3/4, bốn loại trò chơi, lưu/nạp wl3, chống chấm lặp và fallback. Chưa kiểm thử Chromium thật; chưa xác nhận bố cục/cảm ứng/âm thanh thực tế. Không đổi giao diện, bộ tải hay dữ liệu người học.

Tổng 68/168 mục, 2720 câu, 68 trò chơi. Giáo viên duyệt 4 bài Toán 1–4; 64 bài chờ duyệt AI_CHECKED_AWAITING_TEACHER. Còn 100 mục: Toán 69–81 (13), Tiếng Việt 62, Tiếng Anh 25. Tiếp Batch 18 Toán 69–72; đọc nguồn tương ứng trước khi biên soạn. Không làm lại Batch 17. Batch 16 commit 424acbae08840eeb836b0a914bcbfa0a7e124691 đã xác minh hai workflow Pages success và nội dung HTTP của INDEX cùng Toán 61–64 khớp SHA256 với tệp đã kiểm thử. Batch 17 cần xác minh sau ghi.

## Lịch sử

# Checkpoint nguồn Batch 17 — 08/11/2026

Tác vụ tự động đã lưu 40 câu nguồn Bài 65 trong commit cf45406bb5277cfd6574e6e8cf58c8eb69f15181 khi lượt hiện tại đang biên soạn. Đã giữ nguyên và dùng chính 40 câu đó để đóng gói Toán 65, bổ sung Toán 66–68, kiểm thử lại cả batch. Không ghi đè hoặc bỏ nguồn mới; 40 câu Bài 65 là một phần trong tổng 160 câu của batch.

## Lịch sử

# Batch 16 đã tích hợp — 08/11/2026

Toán 61–64: 4 JSON/Markdown, 160 câu phân mức 10/10/20 và 4 trò chơi. Đã đọc trực quan trang in 64–75 (PDF 65–76) của chính PDF Toán tập 2 trong repo; Git blob SHA kiểm tra tại máy là 1a55eb09c9cf573935fa38911d48a5311575b09c, khớp tree GitHub. Nội dung: làm tròn nghìn/chục nghìn, ôn cấu tạo và thứ tự số, cộng/trừ trong 100000. Câu hỏi mới biên soạn riêng, không sao chép hệ thống bài tập sách. Không có câu thiếu dữ kiện hình; các bài này dùng dữ kiện chữ đầy đủ.

Kiểm tra toàn bộ 64 bài/2560 câu: cấu trúc, ID, đáp án, phân mức, Markdown và 2092 đẳng thức lời giải đạt. Hồi quy Batch 16 có 26 phép tính trực tiếp và 119 đáp án neo tính độc lập, biên làm tròn, làm trực tiếp khác nhiều bước, chuyển hàng qua 0 và bài toán hai bước. npm test gồm hồi quy cũ và DOM đạt: luyện tập 10 câu 3/3/4, trò chơi, lời giải, lưu/nạp wl3 và fallback. Chưa kiểm thử Chromium thật do môi trường chưa có trình duyệt; chưa xác nhận bố cục/âm thanh/cảm ứng thực tế. Không thay giao diện hay khóa dữ liệu học sinh.

Tổng tích hợp 64/168 mục: 2560 câu, 64 trò chơi. Giáo viên đã duyệt 4 bài Toán 1–4; 60 bài AI_CHECKED_AWAITING_TEACHER. Còn 104 mục: Toán 65–81 (17), Tiếng Việt 62 và Tiếng Anh 25. Tiếp Batch 17 Toán 65–68; đọc nguồn tương ứng trước biên soạn. Không làm lại Batch 16. Hai workflow Pages của checkpoint trước 8c5ec712a578b3b51588e94df3102b828599cfcf đã success; commit Batch 16 cần xác minh sau khi ghi.

## Lịch sử

# Checkpoint nguồn Batch 16 — 08/11/2026

Đã đọc trực quan trang in 64–75 (PDF 65–76) Toán tập 2 bản sẵn có cho Bài 61–64; chưa đối chiếu hash PDF với repo. Đã soạn 40 câu nguồn riêng Bài 61 trong batch16-source.txt (thứ tự 10/10/20), kiểm tra số dòng, câu không trùng và bốn phương án khác nhau. Chưa đóng gói JSON/Markdown/game hay tích hợp; không tăng INDEX. Tiếp theo soạn Bài 62–64 và hoàn thiện cả batch rồi kiểm thử. Không tạo lại 40 câu nguồn Bài 61.

Tổng tích hợp vẫn 60/168 mục, 2400 câu, 60 trò chơi; giáo viên duyệt 4, chờ duyệt 56, còn 108 mục. Không tự duyệt bài mới. Đây là checkpoint nguồn, không phải batch hoàn chỉnh.

## Lịch sử

# Batch 15 đã tích hợp — 08/11/2026

Toán 57–60: 4 JSON/Markdown, 160 câu mới phân mức 10/10/20, 4 trò chơi, 2 SVG mới đã render và xem. Đã đọc trực quan toàn bộ trang in 47–63 (PDF 48–64) Toán tập 2 bản sẵn có; chưa đối chiếu hash PDF với repo. Nội dung: chia số bốn chữ số, chia có dư và thương có 0; ôn bốn phép tính/ngoặc; số năm chữ số và 100000; so sánh trong phạm vi 100000. Câu hỏi/tình huống/lời giải biên soạn mới.

validate_site.py/validate_content.py, hồi quy Batch 7–9, 12–15 và test_content_dom.cjs toàn bộ 60 bài đạt. Hồi quy mới: 15 câu tính trực tiếp, 117 đáp án neo tính độc lập, chia dài/0 trong thương, số dư bé hơn số chia, nhóm đầy so với chứa hết, mốc 100000, điều kiện biên và tham chiếu SVG. Các bài cũ, lượt 10 câu 3/3/4, bốn trò chơi, lời giải/hình, lưu/nạp wl3 và fallback vẫn đạt. Chưa kiểm thử Chromium thật vì chưa có trình duyệt này; bộ kiểm tra đẳng thức tự động chưa bao quát đầy đủ ngoặc, các biểu thức mới có ngoặc được kiểm tra riêng trong hồi quy. Không sửa giao diện, loader hay dữ liệu tiến độ học sinh.

Tổng đã biên soạn/kiểm tra/tích hợp 60/168 mục, 2400 câu, 60 trò chơi. Giáo viên duyệt 4 (Toán 1–4); 56 mục AI_CHECKED_AWAITING_TEACHER. Còn 108 mục: Toán 61–81 (21), Tiếng Việt 62, Tiếng Anh 25. Checkpoint tiếp Batch 16 Toán 61–64, đọc nguồn tương ứng trước khi biên soạn. Không làm lại nội dung đã tích hợp. Commit Batch 14: 991d15621996b5c6ae26561f9547be6b17164f4c; cả hai workflow Pages đã success. Commit Batch 15 cần xác minh sau khi ghi.

## Lịch sử

# Batch 14 đã tích hợp — 08/11/2026

Toán 53–56: 4 JSON/Markdown, 160 câu (10/10/20 mỗi bài), 4 trò chơi, 3 SVG mới đã render và xem. Đã đọc trực quan toàn bộ trang in 35–46 (PDF 36–47) Toán tập 2 bản đang có; chưa đối chiếu hash với PDF trong repo. Nội dung: ôn chu vi/diện tích; cộng/trừ trong 10000; nhân số bốn chữ số với số một chữ số. Tình huống, phương án nhiễu và lời giải biên soạn mới. INDEX nay ghi ngày cập nhật thực tế UTC khi tái tạo.

validate_site.py/validate_content.py, hồi quy Batch 7–9, 12–14 và test_content_dom.cjs trên toàn bộ 56 bài đều đạt. Kiểm tra mới tính lại 28 câu phép tính trực tiếp, 88 đáp án neo độc lập, số nhớ cộng/nhân, đổi qua hàng 0, ô tô SVG không trùng. Luyện tập 10 câu 3/3/4, bốn chế độ trò chơi, lời giải, hình, lưu/nạp wl3 và fallback đã kiểm tra DOM. Không có Chromium để kiểm thử trình duyệt thật; bộ kiểm tra đẳng thức tự động vẫn chưa bao quát đầy đủ ngoặc. Không đổi index.html, renderer hoặc khóa dữ liệu học sinh.

Tổng AI biên soạn/kiểm tra/tích hợp 56/168 mục, 2240 câu, 56 trò chơi. Giáo viên duyệt 4 (Toán 1–4); 52 mục AI_CHECKED_AWAITING_TEACHER. Còn 112 mục: Toán 57–81 (25), Tiếng Việt 62, Tiếng Anh 25. Checkpoint tiếp Batch 15 Toán 57–60, đọc nguồn tương ứng trước biên soạn. Commit Batch 13 78b60e548265d243fab217747e19ef5fb6e2244f đã có hai workflow Pages success; lượt trước đối chiếu HTTP/SHA256 26 tệp đạt. Commit Batch 14 cần xác minh sau khi ghi.

## Lịch sử

# Batch 13 đã tích hợp — 08/11/2026

Toán 49–52: 4 JSON/Markdown, 160 câu mới theo phân mức 10/10/20, 4 trò chơi, 7 SVG tự dựng đã render và xem. Đã đọc trực quan trang in 17–34 (PDF 18–35) của Toán tập 2 bản sẵn có; chưa đối chiếu hash PDF với repo. Nội dung gồm ôn số/La Mã/làm tròn, chu vi tam giác/tứ giác/chữ nhật/vuông, diện tích và cm², diện tích chữ nhật/vuông. Câu hỏi và tình huống biên soạn mới, không chép hệ thống bài tập sách.

validate_site.py, validate_content.py, hồi quy Batch 7–9, 12–13 và test_content_dom.cjs toàn bộ 52 bài đạt. Kiểm tra mới có 75 đáp án neo tính độc lập, đổi đơn vị, cạnh chung, cắt/ghép, số ô SVG không trùng và diện tích hình đúng tỉ lệ. SVG hiển thị trong các câu cần hình. Chưa có Chromium để kiểm thử trình duyệt thật; kiểm tra đẳng thức tự động chưa bao quát đầy đủ biểu thức có ngoặc. Không đổi giao diện hay dữ liệu wl3.

Tổng đã biên soạn/kiểm tra/tích hợp: 52/168 mục, 2080 câu, 52 trò chơi. Giáo viên đã duyệt 4 (Toán 1–4), còn 48 AI_CHECKED_AWAITING_TEACHER. Còn 116 mục: Toán 53–81 (29), Tiếng Việt 62, Tiếng Anh 25. Checkpoint tiếp Batch 14 Toán 53–56, phải đọc nguồn tương ứng trước biên soạn. Không làm lại 52 bài đã tích hợp. Commit Batch 12: 376b18d30a3a5e7bcc238ac4db4cddb4db8ea0f1; cả hai workflow Pages của commit đó đã success. Commit Batch 13 cần xác minh sau ghi.

## Lịch sử

# Batch 12 đã tích hợp — 08/11/2026

Toán tập 2 Bài 45–48: 4 JSON, 4 Markdown, 160 câu mới (mỗi bài 10 nhận biết/10 thông hiểu/20 vận dụng), 4 trò chơi, 1 SVG đồng hồ La Mã tự dựng đã render và xem. Đã đọc trực quan trang in 4–16 (PDF 5–17) bản nguồn sẵn có; chưa đối chiếu hash với PDF trong repo. Chủ đề: cấu tạo số có bốn chữ số và 10000; so sánh; La Mã I–XX; làm tròn đến chục/trăm. Không sao chép toàn văn hay hệ thống bài tập sách.

Kiểm tra validate_site.py/validate_content.py, hồi quy Batch 7–9 và Batch 12, test_content_dom.cjs trên 48 bài đều đạt: 1920 câu, lượt 10 câu 3/3/4, bốn chế độ trò chơi, đáp án/lời giải/hình, lưu/nạp wl3 và fallback. Hồi quy mới tính độc lập chuyển hàng, thứ tự, La Mã và biên làm tròn. Chưa kiểm thử Chromium thật; kiểm tra đẳng thức tự động chưa bao quát đầy đủ biểu thức có ngoặc. Không thay đổi index.html, loader hay khóa wl3.

Tổng: AI đã biên soạn/kiểm tra và tích hợp 48/168 mục, 1920 câu, 48 trò chơi. Giáo viên đã duyệt 4 (Toán 1–4); 44 mục AI_CHECKED_AWAITING_TEACHER. Còn 120 mục: Toán 49–81 (33), Tiếng Việt 62, Tiếng Anh 25. Checkpoint tiếp Batch 13 Toán 49–52; đọc nguồn tập 2 tương ứng trước biên soạn, không tạo lại Batch 12. Actions/Pages của commit Batch 11 trước lượt này đã thành công; commit Batch 12 cần xác minh sau khi ghi.

## Lịch sử

# Batch 11 đã tích hợp — 08/11/2026

Đã đóng gói Toán 41–44: 4 JSON/Markdown, 160 câu, 4 trò chơi, 2 SVG tự dựng Bài 43 đã render và xem. Nguồn trang in 113–121 đã đọc trực quan các lượt trước. Kiểm tra dữ liệu/cú pháp, hồi quy và DOM toàn bộ 44 bài đạt. Chưa kiểm thử Chromium thật; tự động kiểm tra đẳng thức chưa bao quát đầy đủ biểu thức ngoặc. Tổng 44/168 mục, 1760 câu, 44 trò chơi; giáo viên duyệt 4, chờ duyệt 40. Còn 124 mục: Toán tập 2 Bài 45–81 (37), Tiếng Việt 62, Tiếng Anh 25. Checkpoint tiếp Toán 45–48; đọc PDF tập 2 trước khi biên soạn. Mọi bài mới AI_CHECKED_AWAITING_TEACHER.

## Lịch sử

## Đủ câu nguồn Batch 11 — 08/11/2026

Đã bổ sung 40 câu Bài 44, batch11-source.txt hiện đủ 160 câu Bài 41–44 (10/10/20 mỗi bài). Chưa đóng gói, chưa tích hợp và chưa kiểm thử đầy đủ câu mới. Tiếp theo hoàn tất kiến thức/ví dụ/game, SVG cần thiết và JSON/Markdown của cả batch, chạy kiểm tra rồi cập nhật INDEX. Không tạo lại 160 câu đã lưu. Tổng đang tích hợp giữ 40/168 mục, 1600 câu, 40 trò chơi; giáo viên duyệt 4, chờ duyệt 36. Đây là checkpoint nguồn, không phải batch học liệu hoàn chỉnh.

## Checkpoint Bài 43 — 08/11/2026

Đã nối 40 câu nguồn Bài 43 vào batch11-source.txt; nguồn Batch 11 hiện 120/160 câu Bài 41–43. Các câu có dữ kiện chữ tường minh về góc, trung điểm, đường tròn, khối và đo lường; hai câu về ghép/sơn khối cần bổ sung SVG minh họa khi đóng gói, chưa tính là sẵn sàng. Kiểm tra số dòng, không trùng trong bài, bốn lựa chọn khác nhau đạt. Chưa kiểm thử tích hợp hay thẩm định hình cho bài mới.

Tiếp Bài 44, nội dung hướng dẫn/ví dụ/game và SVG của Bài 43–44; kiểm thử cả batch trước khi đưa vào INDEX. Tổng tích hợp vẫn 40/168 mục, 1600 câu, 40 game; giáo viên duyệt 4, chờ duyệt 36, còn 128 mục. Không tạo lại 120 câu nguồn Bài 41–43. Nguồn trang 113–121 đã đọc ở các lượt trước.

## Hiển thị trạng thái tải học liệu — 08/11/2026

Đã bổ sung dòng trạng thái trên giao diện ghi số học liệu riêng thực sự tải được /168. Bộ tải INDEX và JSON dùng cache:no-cache để yêu cầu tái xác thực dữ liệu khi tải trang. Không xóa wl3 hay đổi hồ sơ/XP/sao. Mục đích phân biệt bài đã tích hợp với câu nguồn soạn dở; Bài 41–42 vẫn chưa tích hợp. Tổng nội dung giữ 40/168 bài, 1600 câu, 40 trò chơi; giáo viên duyệt 4, chờ duyệt 36. Tiếp tục Batch 11 Bài 43–44 và đóng gói cả batch. Kiểm thử npm test toàn bộ đạt; chưa kiểm thử Chromium thật.

## Batch 11 — đã thêm nguồn Bài 42, 08/11/2026

Đã render và đọc trực quan trang in 116–121 (PDF 117–122) Toán tập 1 cho Bài 42–44. Chưa đối chiếu hash bản PDF đang dùng với bản trong repo. Bài 42 ôn thứ tự tính, dấu ngoặc, nhóm số tính thuận tiện và đóng gói nhiều cấp. Bài 43 ôn góc, trung điểm, vẽ hình, bán kính/đường kính, khối và đơn vị đo; Bài 44 tổng hợp phép tính, trung điểm/góc, đường gấp khúc và đo lường. Câu phụ thuộc hình của Bài 43–44 phải có SVG tự dựng khi biên soạn.

Đã nối 40 câu mới Bài 42 sau 40 câu Bài 41 trong batch11-source.txt, theo thứ tự phân mức 10/10/20; kiểm tra không trùng trong bài, bốn lựa chọn khác nhau, tính lại 73 đẳng thức đạt. Nguồn Batch 11 hiện 80/160 câu, chưa tích hợp, chưa tạo JSON/Markdown/game bài mới. Cần soạn Bài 43–44, hình SVG, nội dung hướng dẫn/ví dụ/game cả batch; bổ sung kiểm tra đầy đủ biểu thức có ngoặc trước khi đóng gói. Không tạo lại nguồn Bài 41–42 hoặc đọc lại trang nguồn nếu không thay đổi.

Tổng đang tích hợp vẫn 40/168 mục, 1600 câu, 40 trò chơi; giáo viên duyệt 4, chờ duyệt 36, còn 128 mục nháp. Không thay INDEX hoặc dữ liệu wl3 trong checkpoint nguồn này. Chưa kiểm thử Chromium thật.

## Batch 11 đang biên soạn — 08/11/2026

Đã render và đọc trực quan trang PDF 114–116 / trang in 113–115 bản Toán tập 1 đang truy cập được; chưa đối chiếu hash với bản trong repo. Đã biên soạn 40 câu nguồn riêng Bài 41 tại batch11-source.txt, theo thứ tự 10 nhận biết/10 thông hiểu/20 vận dụng, có đáp án, lời giải và ba phương án nhiễu. Có ôn phân số đơn vị, tìm thừa số/số chia/số bị chia, chữ số thiếu, số nhớ, thương có 0, phần dư, số can chứa hết và bài thực tế. Kiểm tra không trùng trong bài, bốn lựa chọn khác nhau và tính lại 54 đẳng thức đạt.

Chưa đóng gói JSON/Markdown hay trò chơi Bài 41; chưa kiểm thử tích hợp bài mới. Tổng đang tích hợp vẫn 40/168 mục, 1600 câu, 40 trò chơi; giáo viên duyệt 4, chờ duyệt 36; còn 128 mục. Tiếp đọc nguồn Bài 42–44 trang 116–121, biên soạn 120 câu và nội dung hướng dẫn/ví dụ/game cả batch, rồi kiểm thử và commit batch hoàn chỉnh. Không tạo lại 40 câu Bài 41 đã lưu. Chưa kiểm thử Chromium thật.

# Batch 10 hoàn tất — 08/11/2026

Đã tích hợp Toán 37–40: 4 JSON, 4 Markdown, 160 câu (10/10/20 mỗi bài), 4 trò chơi; lượt 10 câu 3/3/4. Nguồn trang 99–112 đã đọc trực quan ở lượt trước. Các câu đủ dữ kiện chữ, không phụ thuộc hình. npm test đạt trên 40 bài, 1600 câu, 1581 đẳng thức; DOM và hồi quy cũ đạt. Chưa kiểm thử Chromium thật; kiểm tra tự động chưa bao quát mọi biểu thức có ngoặc. Giáo viên duyệt 4 bài, 36 chờ duyệt; mọi bài mới AI_CHECKED_AWAITING_TEACHER. Tổng 40/168; còn 128 mục (Toán 41, Tiếng Việt 62, Tiếng Anh 25). Tiếp Toán 41–44; đọc nguồn trước khi biên soạn.

## Lịch sử

## Checkpoint đủ câu nguồn Batch 10 — 08/11/2026

Đã bổ sung 40 câu Bài 40; batch10-source.txt hiện đủ 160 câu nguồn Bài 37–40, mỗi bài theo thứ tự 10 nhận biết/10 thông hiểu/20 vận dụng. Chưa đóng gói JSON/Markdown, phần kiến thức và trò chơi, chưa kiểm thử tích hợp bài mới. Không tăng tiến độ: vẫn 36/168 mục đang tích hợp, 1440 câu, 36 trò chơi, 4 bài giáo viên duyệt và 32 chờ duyệt. Bước tiếp theo phải hoàn tất batch10-details.json, build_batch10.py, kiểm tra đáp án/biểu thức ngoặc và hồi quy toàn bộ, rồi commit batch hoàn chỉnh. Không tạo lại 160 câu nguồn đã có.

## Checkpoint Bài 39 — 08/11/2026

Đã nối thêm 40 câu Bài 39 vào batch10-source.txt: phân biệt hiệu với số lần, đổi cùng đơn vị, tình huống thay đổi hai nhóm. Kiểm tra 40 câu không trùng trong bài, lựa chọn khác nhau và tính lại 48 đẳng thức đạt. Nguồn Batch 10 hiện 120/160 câu (Bài 37–39), chưa tích hợp vào website. Tiếp tục Bài 40 và phần kiến thức/ví dụ/game/JSON/Markdown cả batch; chưa tăng số hoàn thiện. Tổng tích hợp giữ 36/168 mục, 1440 câu, 36 game; giáo viên duyệt 4, chờ duyệt 32. Không tạo lại 120 câu đã lưu.

## Checkpoint Bài 38 — 08/11/2026

Đã thêm 40 câu nguồn Bài 38 nối sau 40 câu Bài 37 trong batch10-source.txt. Tổng nguồn Batch 10 hiện 80/160 câu; chưa tích hợp bài mới. Bài 38 có thứ tự cùng mức từ trái sang phải, nhân/chia trước, ngoặc trước, lỗi sai và tình huống thực tế. Đã kiểm tra số dòng, không trùng trong bài, bốn lựa chọn khác nhau; chưa kiểm thử DOM hay validator biểu thức đầy đủ. Tiếp tục 80 câu Bài 39–40 cùng phần kiến thức/ví dụ/game, rồi đóng gói cả batch. Tiến độ đang tích hợp vẫn 36/168, 1440 câu, 36 game; giáo viên duyệt 4, chờ duyệt 32. Không tạo lại nguồn Bài 37–38.

## Checkpoint biên soạn Batch 10 — 08/11/2026

Đã biên soạn và lưu 40 câu nguồn Toán 37 trong batch10-source.txt, kèm đáp án, lời giải, ba phương án nhiễu; phân mức theo thứ tự 10/10/20. Đã kiểm tra không trùng nguyên câu trong bài, bốn lựa chọn khác nhau, tính lại 39 đẳng thức. Đây là nguồn soạn dở, chưa có JSON/Markdown bài, chưa tích hợp hoặc kiểm thử DOM cho bài mới. Không tăng số bài hoàn thiện: vẫn 36/168, 1440 câu đang tích hợp, 36 trò chơi; giáo viên duyệt 4, chờ duyệt 32. Cần tiếp tục 120 câu Bài 38–40, phần hướng dẫn/ví dụ/trò chơi của cả bốn bài rồi đóng gói, kiểm thử và commit Batch 10. Không tạo lại 40 câu Bài 37 đã lưu.

## Đối chiếu nguồn kế tiếp — 08/11/2026

Đã đọc trực quan nguồn Toán 37–40, trang in 99–112 (PDF 100–113); ghi chú tại BATCH10_SOURCE_REVIEW.md. Chưa biên soạn đủ 160 câu nên chưa tạo batch học liệu và không tăng tiến độ. Tổng giữ 36/168 mục, 1440 câu, 36 trò chơi; 4 bài giáo viên duyệt, 32 chờ duyệt, 132 mục nháp. Nối tiếp biên soạn Toán 37–40, không cần đọc lại trừ khi nguồn thay đổi.

## Kiểm thử tổng hợp — 08/11/2026

Đã đưa kiểm tra dữ liệu/cú pháp và các hồi quy Batch 7–9 vào `npm test`, trước bước DOM, để tránh bỏ sót khi chạy một lệnh. Toàn bộ kiểm tra đạt trên 36 bài/1440 câu. Lượt này chưa bổ sung bài mới; checkpoint vẫn Toán 37–40 (trang in 99–112). Chỉ Toán 1–4 được giáo viên duyệt; 32 bài chờ duyệt, còn 132 mục nháp. Chưa kiểm thử Chromium thật.

## Batch 9 — Toán 33–36, 07/11/2026

- Đã render và đọc trực quan toàn bộ trang PDF 92–99 (trang in 91–98) bản Toán tập 1 có sẵn trong môi trường. Chưa xác minh hash với PDF trong repo.
- 4 JSON, 4 Markdown, 160 câu và phương án nhiễu mới, 4 trò chơi. Hai SVG tự dựng: nhiệt kế P/Q có mỗi khoảng 2 °C, thẻ dài 35 mm trên thước chia mm. Mọi câu cần hình đều tham chiếu hình ngay trong câu; đã render và xem cả hai hình, sửa chỗ nhãn đơn vị nhiệt kế bị chạm số trước khi lưu.
- Bài 33–34 có hoạt động thực hành với dụng cụ, ghi số/đơn vị và tự kiểm tra. Thiếu dụng cụ thì ghi chưa thực hiện, không đoán kết quả. Số liệu nhiệt độ dùng luyện toán là mô phỏng, không phải thời tiết hiện tại hay tư vấn sức khỏe.
- validate_site.py/validate_content.py đạt: 36 bài/1440 câu, 1366 đẳng thức số được tính lại; ID, phân mức 10/10/20, lựa chọn, đáp án, lời giải, Markdown, hình, game và trạng thái đồng bộ.
- test_batch9.py: 160 câu trong batch không trùng nguyên văn, 32 đáp án trọng yếu; tính độc lập các phép nhân thuần túy, chênh nhiệt độ, vạch thước, đong bằng hai cốc và số nhớ qua chữ số 0. test_batch7.py và test_batch8.py vẫn đạt.
- test_content_dom.cjs đạt toàn bộ 36 bài: lấy 10 câu 3/3/4, đổi bộ, chấm điểm, game đúng bài, hình/bảng/vẽ cũ, lưu/nạp tiến độ và fallback file lỗi. Renderer và wl3 không đổi.
- Chưa có Chromium để kiểm thử bố cục, cảm ứng, âm thanh thực tế. Tổng 36/168 có học liệu riêng; 1440 câu, 36 trò chơi; giáo viên duyệt 4, chờ duyệt 32, còn 132 mục nháp. Checkpoint tiếp Toán 37–40.

## Batch 8 — Toán 29–32, 07/11/2026

- Nguồn thực đọc: bản PDF Toán tập 1 sẵn trong môi trường, trang PDF 84–91 (trang in 83–90), đã render và đọc trực quan cả 8 trang. Chưa xác minh hash bản đính kèm với bản trong repo.
- Biên soạn 4 JSON/Markdown, 160 câu riêng, 4 trò chơi (kho báu, ghép cặp, đúng/sai), 3 SVG mới: thước chia từng mm với đầu A lệch 0; cân thăng bằng có ba quả cân; ca nước chia vạch 100 ml. Hình hiển thị ngay trong mọi câu phụ thuộc hình. Đã render và xem cả 3 hình, không dùng ảnh SGK.
- Có hướng dẫn, mục tiêu, lỗi thường gặp, ví dụ giải, phản hồi, đánh giá, hoạt động dụng cụ cho bài 30–32. Dữ kiện và bài tập mới, không chép hệ thống bài tập SGK.
- validate_site.py/validate_content.py: 32 bài, 1280 câu, 1193 đẳng thức số được tính lại; ID, lựa chọn, đáp án, phân mức 10/10/20, Markdown, hình, game và trạng thái đạt.
- test_batch8.py: 160 câu không trùng nguyên văn giữa batch; 27 đáp án trọng yếu và các phép tính độc lập về chia lấy số hộp, thước lệch 0, tổng quả cân, khối lượng trừ khay, nước tràn. test_batch7.py vẫn đạt.
- test_content_dom.cjs: toàn bộ 32 bài đạt, 10 câu/lượt 3/3/4, thay bộ, chấm điểm, chống chấm lặp, 4 loại game, hình/bảng/lưới vẽ cũ, lưu nạp wl3, fallback khi một JSON lỗi. Không đổi renderer hay khóa lưu trữ.
- Chưa có Chromium: chưa kiểm thử bố cục, cảm ứng và âm thanh bằng trình duyệt thật. AI kiểm tra không thay thẩm định giáo viên.
- Tổng 32/168 mục có học liệu riêng, 1280 câu, 32 trò chơi; giáo viên duyệt 4, chờ duyệt 28; còn 136 mục nháp. Checkpoint Toán 33–36 trang 91–98.

## Batch 7 — Toán 25–28, 07/11/2026

- Nguồn đã đọc trực quan: PDF Toán tập 1 sẵn trong môi trường, trang PDF 73–83 / trang in 72–82. Chưa xác minh hash với bản PDF trong repo.
- 4 JSON và 4 Markdown riêng; 160 câu và phương án nhiễu biên soạn riêng; 4 trò chơi theo bài. Các câu mới đủ dữ kiện chữ, không phụ thuộc hình ngầm, không cần hình hình học. Không sao chép hệ thống bài tập SGK.
- Rà soát số dư bé hơn số chia, phép kiểm tra bằng nhân cộng phần dư; phân biệt số nhóm đầy với số chỗ chứa hết; hạ chục dư; lượng còn lại với lượng đem dùng; trung gian với đáp số cuối.
- Kiểm tra toàn bộ 28 bài/1120 câu: JSON, ID, trùng câu trong bài, lựa chọn, đáp án, lời giải, Markdown, hình cũ, game và trạng thái đạt. Tính lại 1017 đẳng thức số. test_batch7.py kiểm tra 22 đáp án trọng yếu và hai cặp tình huống số dư/giảm số lần.
- DOM toàn bộ đạt: 10 câu 3/3/4, thay bộ, chấm điểm, 4 chế độ chơi, hồi quy hình/bảng/vẽ, lưu/nạp wl3 và fallback file lỗi. npm ci thành công.
- Chưa có Chromium: chưa kiểm thử bố cục, cảm ứng, âm thanh bằng trình duyệt thật. AI kiểm tra không thay giáo viên thẩm định.
- Tổng 28/168 có học liệu riêng; 1120 câu, 28 trò chơi; giáo viên duyệt 4, chờ duyệt 24; còn 140 mục nháp. Tiếp Toán 29–32.

# Rà soát học liệu — 07/11/2026

## Bằng chứng và phạm vi

- Đã đọc README.md, KIEM_KE_DU_LIEU_LOP_3.md, danh mục JSON, index.html và cây thư mục main.
- Kho có sáu PDF; bản đính kèm được dùng để đọc Batch 1. Chưa kiểm tra hash đối chiếu từng PDF đính kèm với kho.
- Không có tệp OCR toàn văn trong cây kho hiện tại. Báo cáo cũ nói OCR 716 trang được giữ trong artifact tạm; chưa truy cập được artifact đó.
- Danh mục JSON chứa 81 + 62 + 20 + 5 = 168 mục. Báo cáo cũ ghi “6 mục” Tiếng Anh bổ sung nhưng Starter + Review 1–4 chỉ là 5; đã sửa lỗi đếm đó. Chưa đối chiếu lại toàn bộ mục lục sáu PDF.

## Hiện trạng

- Các bài cũ có mẫu hoặc nội dung tự động; không đủ cơ sở công nhận hoàn thiện từng bài.
- INDEX.json phân loại 164 mục BẢN NHÁP và 4 mục CẦN RÀ SOÁT (AI đã kiểm tra, chờ giáo viên).
- question_count=null cho bài chưa kiểm kê ngân hàng riêng, không có nghĩa website không có câu hỏi.
- Website cũ tái sử dụng seed để tạo 12 nhiệm vụ; Batch 1 thay bằng 40 câu riêng/bài.
- Đường dẫn danh mục trên giao diện còn trỏ kho tên cũ; đã sửa về TOAN_TV_TA_LOP3.

## Batch 1: Toán tập 1, Bài 1–4

- Đọc trực quan tất cả trang in 6–15 (PDF 7–16); không đăng nguyên văn SGK.
- 160 câu mới, mỗi bài phân mức 10 nhận biết, 10 thông hiểu, 20 vận dụng.
- Có trắc nghiệm và điền đáp án; không tự tuyên bố có câu đúng/sai trong kho mới.
- Mỗi bài có mục tiêu, khám phá, quy tắc, cách học, ví dụ, lỗi thường gặp, trò chơi và đánh giá.
- Đáp án được AI rà soát; các phép tính và cách giải đã đọc lại. Kiểm tra tự động cấu trúc không thay thế thẩm định sư phạm.
- Không có xác nhận của giáo viên cho nội dung mới.

## Kết quả kỹ thuật

- JSON hợp lệ; 160 mã câu duy nhất, không trùng nguyên văn câu trong từng bài, không thiếu đáp án/lời giải.
- Mỗi MCQ có bốn phương án khác nhau và có đáp án trong phương án.
- Node kiểm tra cú pháp bộ tải: đạt.
- test_batch1_dom.cjs: đạt luồng 168 bài, bốn kho câu hỏi, lượt 10 câu phân mức 3/3/4, tám lượt xáo trộn khác bộ, trả lời/chấm điểm/lời giải, chặn chấm lại câu đã xong, bốn trò chơi theo bài, lưu/nạp hồ sơ, một tệp JSON lỗi 404 vẫn giữ bài cũ.
- Chưa chạy được test_batch1.cjs bằng Chromium do thiếu executable và tải Chromium không thành công. Chưa xác nhận bố cục, thao tác cảm ứng, âm thanh, tải tệp sao lưu/khôi phục bằng giao diện thực tế và trạng thái Pages sau commit.
- Bộ tải có lỗi độc lập từng tệp; dữ liệu cũ vẫn dùng được khi tệp mới không tải được. Không thay khóa lưu tiến độ.

## Cần theo dõi

1. Giáo viên rà soát nội dung, độ khó và phương án nhiễu của Batch 1.
2. Kiểm thử trình duyệt sau triển khai, gồm hồ sơ, sao lưu/khôi phục và màn hình điện thoại.
3. Đối chiếu lại mục lục và khoảng trang cho các bài sau; một số khoảng đang bao gồm phần ôn tập xen giữa.
4. Hoàn thiện 164 mục còn lại theo batch; không đánh dấu hoàn thành dựa vào tên bài có trên giao diện.

## Cập nhật Batch 2 — 07/11/2026

- Ghi nhận xác nhận thực tế của giáo viên cho Batch 1. Chỉ 4 bài 1–4 được gắn TEACHER_APPROVED; 4 bài mới chưa được duyệt.
- Toán 5–8: đọc toàn bộ trang in 16–27, biên soạn 160 câu mới có phương án nhiễu riêng, lời giải; 4 kiểu trò chơi theo đúng phạm vi từng bài.
- Bài 7: 2 sơ đồ SVG có mô tả tiếp cận và chú thích; dữ kiện câu hỏi đủ, không dựa vào hình SGK không được đính kèm.
- Đã loại bỏ bộ tải cứng 4 tệp, chuyển sang chỉ mục. Bộ tải kiểm tra ID, câu hỏi, đáp án, lựa chọn trước khi dùng; khi lỗi giữ bài cũ.
- Sửa nút làm lại để vẫn lấy 10 câu thay vì toàn bộ 40 câu. Chơi lại mini game giữ phạm vi bài. Ghép đôi dùng 5 đáp án khác nhau để tránh ghép mơ hồ.
- Kiểm thử DOM cho 8 bài: phân mức 3/3/4, xáo trộn 8 lần, đáp án/lời giải, chặn chấm lặp, cả bốn kiểu chơi, hình ngay trong câu hỏi, trạng thái thẩm định, lưu/nạp hồ sơ, fallback khi 404: đạt.
- Tính lại độc lập 291 đẳng thức số trong lời giải của 8 bài: đạt. Các khẳng định bằng chữ và độ phù hợp sư phạm vẫn cần giáo viên kiểm tra.
- Tích hợp kiểm tra JSON, chỉ mục, hình, cú pháp JavaScript ngoài HTML và đẳng thức vào validate_site.py, là bước kiểm tra của workflow Pages hiện có.
- Hạn chế còn giữ: chưa kiểm thử bố cục/âm thanh/tải sao lưu/khôi phục trên trình duyệt thật; không tự tuyên bố đã hoàn thành toàn bộ 168 mục.

## Cập nhật Batch 3 — 07/11/2026

- Đọc trực quan trang in 28–38 (PDF 29–39), đối chiếu nội dung bảng nhân/chia 6, 7, 8, 9 và bảng tra chung.
- Thêm 160 câu mới, mỗi bài phân mức 10/10/20, có lời giải và phương án nhiễu riêng; đã rà soát phép tính và ngữ nghĩa của đề. Không sao chép hệ thống bài tập SGK.
- Bài 12 có bảng nhân/chia HTML chính xác; các câu hỏi tham chiếu bảng tự hiển thị bảng trong bài kiểm tra và trò chơi. Bảng được lưu cùng JSON và Markdown.
- Chỉ mục hiện có 12 bài riêng: 4 bài đã thẩm định, 8 bài chờ thẩm định, 156 bản nháp.
- Toàn bộ 480 câu qua kiểm tra JSON, ID, phân mức, đáp án, lựa chọn, lời giải, tài liệu Markdown và trạng thái duyệt. Tính lại 495 đẳng thức số trong lời giải: đạt.
- Bộ kiểm thử DOM mở rộng theo chỉ mục thay vì số bài cố định: 12 bài, 8 lượt xáo trộn/bài, phân mức 3/3/4, làm lại giữ 10 câu, bốn kiểu trò chơi và phạm vi bài, hình và bảng tham chiếu, lưu/nạp hồ sơ, một file 404: đạt. Đã kiểm tra đúng sau một lần sai được nửa điểm và hiện lời giải sau hai lần sai.
- Tên bộ kiểm thử hiện hành: scripts/test_content_dom.cjs; tên cũ gọi lại bộ hiện hành. Không tuyên bố đã kiểm thử trình duyệt thật.
- Workflow Publish class 3 website to GitHub Pages của Batch 2 đã hoàn tất thành công (run 42376240072). Kiểm tra triển khai Batch 3 sau khi commit.

## Cập nhật Batch 4 — 07/11/2026

- Nguồn: đọc trực quan toàn bộ trang in 39–51, gồm tìm thành phần trong nhân/chia, một phần mấy, ôn tập và điểm ở giữa/trung điểm.
- Biên soạn 160 câu có lời giải và phương án nhiễu riêng, 4 trò chơi; thêm 5 SVG có mô tả tiếp cận, render và xem cả 5 PNG để kiểm tra nhãn và dữ kiện.
- Đã rà soát phạm vi kiến thức: bỏ phép nhân hai chữ số chưa học trong tháp tích, giữ phép tính trong các bảng đã học; các bài tính nửa đoạn dùng số phù hợp bảng chia 2 đã học.
- Hai câu Bài 14 và năm câu Bài 16 có tham chiếu SVG, được kiểm tra hiện đúng tệp hình trong luồng làm bài.
- Tổng 16 bài, 640 câu qua validator; 633 đẳng thức số trong lời giải được tính lại. Kiểm thử DOM theo chỉ mục, gồm các hình mới: đạt.
- Giáo viên chỉ xác nhận Batch 1; không mở rộng xác nhận đó cho các batch khác. Hiện 4 bài đã thẩm định, 12 bài chờ thẩm định, 152 mục bản nháp.
- Đã thiết lập tác vụ tiếp tục tự động theo thứ tự Toán, Tiếng Việt, Tiếng Anh; mỗi lượt phải đọc checkpoint và xác minh commit thực tế, không giả báo hoàn thành.
- Giữ giới hạn: kiểm thử DOM không xác nhận thao tác cảm ứng, bố cục toàn trang, giọng đọc và tải tệp sao lưu/khôi phục bằng trình duyệt thật.

## Cập nhật Batch 5 — 07/11/2026

- Đã đọc toàn bộ trang in 52–62; xác định OCR lệch ranh giới Bài 18/19: Bài 18 kết thúc ở 55, Bài 19 bắt đầu ở 56. Sửa danh mục CHUONG_TRINH_LOP_3_FULL.json và dẫn trang; không sửa số lượng danh mục.
- Toán 17–20 có 160 câu mới (10/10/20 mỗi bài), 4 trò chơi, kiến thức, ví dụ, lỗi thường gặp và lời giải. Bài 20 có ba hoạt động thực hành bằng dụng cụ, tiêu chí tự kiểm tra và lưới vẽ tương tác.
- Sáu SVG mới được dựng bằng tọa độ, render và xem trực quan: hình tròn với đường kính/bán kính/đoạn không qua tâm; ba góc; góc vuông xoay nghiêng; tam giác/chữ nhật/vuông; tứ giác cạnh bằng nhưng không vuông; lưới hình chữ nhật/vuông. Đã chỉnh nhãn nhóm góc để không lẫn với tên điểm.
- Kiểm tra toàn bộ 800 câu, ID, lựa chọn, lời giải, Markdown, hình và trạng thái duyệt: đạt. Tính lại 671 đẳng thức số trong lời giải: đạt.
- DOM hồi quy 20 bài và bốn loại game: đạt. Kiểm tra lưới vẽ có tám trường hợp đúng/sai cho bốn kiểu hình, góc vuông xoay nghiêng, đường tròn vượt lưới, chọn trùng điểm, xóa nét và chọn bằng phím/chuột: đạt. Vùng chọn chấm được mở rộng để dễ thao tác.
- Sửa thiếu dữ kiện ở trò ghép đôi: câu cần hình/bảng có phần tham chiếu chung hiển thị ngay trên màn chơi; đã kiểm thử với Bài 19 và bảng của Bài 12.
- Giới hạn: DOM và render SVG không thay thế kiểm thử bố cục toàn website, thao tác cảm ứng hay âm thanh bằng trình duyệt thật. Chỉ Bài 1–4 đã được giáo viên xác nhận.

## Cập nhật Batch 6 — 07/11/2026

- Đã đọc trực quan toàn bộ trang in 63–71 (PDF 64–72) cho Bài 21–24. Không thay đổi số lượng danh mục; các mốc nguồn của bốn bài khớp PDF.
- Biên soạn 160 câu, phân mức 10/10/20 mỗi bài, đáp án/lời giải và phương án nhiễu riêng; thêm 4 trò chơi. Nhân hai chữ số có hướng dẫn thẳng hàng, tính đơn vị trước, nhớ sang chục và ví dụ không vượt phạm vi bài.
- Câu gấp số lần có phân biệt thêm đơn vị, xác định số ban đầu, số phần trên sơ đồ, kiểm tra cách lập phép tính, tìm tổng và chênh lệch; không chỉ đổi số trong cùng một mẫu.
- Năm SVG mới: mô hình lập phương và hộp chữ nhật đủ cạnh/đỉnh khuất; trung điểm bốn cạnh hình vuông; đường tròn vừa khít hình vuông; sơ đồ số thẻ gấp ba. Đã render và xem cả năm hình; nhãn rõ, không cắt chữ.
- Validator đạt cho toàn bộ 24 bài, 960 câu. Tính lại 824 đẳng thức số trong lời giải: đạt. Bài 21 dùng phép cộng đã học nếu cần cộng 12 cạnh của hai khung, không yêu cầu thuật toán nhân hai chữ số trước Bài 23.
- DOM hồi quy 24 bài, 10 câu phân mức 3/3/4, chấm điểm/lời giải, bốn kiểu trò chơi, hình trong câu hỏi và ghép đôi, lưới vẽ, lưu/nạp tiến độ, fallback 404: đạt. Bổ sung kiểm thử ghép đôi với sơ đồ của Bài 24.
- Kiểm thử Chromium chưa thực hiện vì môi trường chưa có executable. Bộ kiểm thử trình duyệt đã sửa để lấy số học liệu từ chỉ mục thay vì hằng số cũ.
- Workflow Pages Batch 5 thành công (run 42379465425). Batch 6 cần xác minh theo commit thực tế sau khi ghi.
- Trạng thái duyệt giữ nguyên: 4 bài đã được giáo viên thẩm định; 20 bài mới chờ thẩm định; 144 mục còn bản nháp.

## Kiểm tra khả năng tái lập — 07/11/2026

- Kiểm tra lại main và các tệp tiến độ/chỉ mục/duyệt/mã ứng dụng trước khi thao tác.
- validate_site.py đạt: 168 mục, 24 bài riêng, 960 câu, 824 đẳng thức số.
- Phát hiện thư mục jsdom tạm không còn. Đã bổ sung package.json, package-lock.json với phiên bản jsdom thực tế đã kiểm tra và .gitignore cho node_modules.
- Đã chạy npm ci và npm test từ bộ phụ thuộc được khóa: DOM hồi quy 24 bài đạt. Không thay đổi số bài hoặc gán thêm xác nhận giáo viên. Chưa biên soạn Batch 7; tiếp tục Toán 25–28.
- Chưa kiểm thử Chromium; không suy diễn DOM thành kiểm thử trình duyệt thật.
