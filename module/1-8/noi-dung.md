---
tieu-de: Chọn kiến trúc mô hình, và chỗ đứng của KAN với QSVM
phu-de: Trụ 1 NID · module 1.8
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 89
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: NID
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Trên dữ liệu bảng của IDS, tôi có bằng chứng gì để nói mô hình mới của tôi hơn một bộ gradient boosting được tinh chỉnh tử tế?

## Câu hỏi đầu tiên của mọi phản biện về mô hình mới
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Câu đó luôn là: baseline của anh được tinh chỉnh ở ngân sách nào. Không phải baseline là gì, mà baseline được chăm tới mức nào. Nhà đã có một ca mẫu về chuyện này, và nó nằm trong sổ dưới tên baseline cổ điển yếu.

## Câu hỏi đầu tiên của mọi phản biện về mô hình mới (tiếp)
@phut: 1
@che-do: noi

Trên dữ liệu bảng, tập hợp cây thắng vì ba tính chất cụ thể, không vì truyền thống: bất biến với biến đổi đơn điệu từng biến, xử được biên quyết định không trơn, và chịu được đặc trưng vô ích. Ba tính chất đó đúng vào ba chỗ mà dữ liệu bảng của IDS khó.

## Câu hỏi đầu tiên của mọi phản biện về mô hình mới (tiếp)
@phut: 1
@che-do: noi

Nên một mô hình mới muốn thắng phải nói được nó cải thiện cái nào trong ba cái đó, hoặc nó mua được một thứ khác hẳn, ví dụ dễ giải thích hoặc chạy được trên thiết bị nhỏ.

## Câu hỏi đầu tiên của mọi phản biện về mô hình mới (tiếp)
@phut: 1
@che-do: noi

Hai nhánh mà nhà đang đi, KAN và QSVM, có hai loại rủi ro khác nhau. Với KAN, rủi ro là dùng tuyên bố **biểu diễn được** để suy ra **học tốt hơn**: đó là hai chuyện khác nhau và năm tuyên bố của bài KAN gốc đã bị phản bác. Với QSVM, rủi ro là số học:

## Câu hỏi đầu tiên của mọi phản biện về mô hình mới (tiếp)
@phut: 1
@che-do: noi

chi phí dựng ma trận nhân là bậc `n²` nhân với số lần lấy mẫu để ước lượng mỗi phần tử, và khi tính ra giờ máy thì con số không ở cùng bậc với một bộ cây chạy trong vài phút.

## Ba lý do cây thắng trên dữ liệu bảng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Ba lý do cây thắng trên dữ liệu bảng · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ba cái, phải kể rời nhau và gắn được vào dữ liệu IDS: **Bất biến với biến đổi đơn điệu từng biến:** chia theo ngưỡng chỉ dùng thứ tự, nên đổi đơn vị byte sang kilobyte hay lấy log không đổi gì. Mạng neural thì phải chuẩn hoá và kết quả phụ thuộc cách chuẩn hoá. **Xử được biên quyết định không trơn:** nhiều quy tắc thật trong IDS là bậc thang, ví dụ cổng nhỏ hơn {{s002}} hay không.

## Ba lý do cây thắng trên dữ liệu bảng · đáp (tiếp)
@phut: 1
@che-do: noi

Hàm trơn phải tiêu nhiều dung lượng để xấp xỉ một bậc thang. **Chịu được đặc trưng vô ích:** cây bỏ qua đặc trưng không giảm được độ bất thuần, còn mạng toàn kết nối vẫn gán trọng số cho chúng và phải học cách triệt tiêu. **Điểm phải nhớ:** ba tính chất này là tính chất của dữ liệu, không phải của ngành.

## Ba lý do cây thắng trên dữ liệu bảng · đáp (tiếp)
@phut: 1
@che-do: noi

Nên lập luận đúng cho một mô hình mới không phải là nó mới, mà là chỉ ra bộ dữ liệu của mình thiếu một trong ba đặc điểm đó, hoặc mô hình mới mua được một thứ khác mà cây không có.

## Biểu diễn được khác học được
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Biểu diễn được khác học được · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Dạng Kolmogorov-Arnold: `f(x) = Σ_q Φ_q( Σ_p φ_{q,p}(x_p) )`, tức thay trọng số bằng hàm một biến học được trên cạnh. Định lý nền là một định lý **tồn tại**: nó nói có một biểu diễn như thế, nó không nói tìm được bằng cách nào, không nói cần bao nhiêu mẫu, và không nói các hàm một biến đó có trơn hay không.

## Biểu diễn được khác học được · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** mạng neural một lớp ẩn đủ rộng cũng xấp xỉ được mọi hàm liên tục trên tập compact, và không ai dùng kết quả đó để tuyên bố nó thắng mô hình khác.
Ba cầu nối thiếu giữa biểu diễn được và học được là:
thuật toán tối ưu có tìm tới được hay không, cần bao nhiêu mẫu, và chi phí mỗi bước.

## Biểu diễn được khác học được · đáp (tiếp)
@phut: 1
@che-do: noi

Một bài báo lấy tính biểu diễn làm lý do cho hiệu năng là bài đang bỏ qua cả ba, và đó đúng là chỗ năm tuyên bố của bài KAN gốc đã bị phản bác.

## Ngân sách tinh chỉnh là một phần của kết quả
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Ngân sách tinh chỉnh là một phần của kết quả · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khi so hai mô hình, con số so được chỉ xuất hiện khi hai bên dùng cùng một ngân sách tìm siêu tham số: cùng số lần thử, cùng không gian tìm, cùng tiêu chí chọn, cùng tập dùng để chọn. Thiếu điều đó thì bảng xếp hạng đo tổng của hai thứ: chất lượng mô hình và công sức tác giả.

## Ngân sách tinh chỉnh là một phần của kết quả · (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** cách khai rẻ nhất và khó bác nhất là báo **đường hiệu năng theo ngân sách** cho cả hai bên, tức trục hoành là số lần thử siêu tham số và trục tung là hiệu năng tốt nhất tới lúc đó.
Nếu hai đường cắt nhau thì nói rõ chúng cắt ở đâu.

## Ngân sách tinh chỉnh là một phần của kết quả · (tiếp)
@phut: 1
@che-do: noi

Nếu baseline vẫn đang đi lên ở cuối trục thì bài báo chưa có bằng chứng thắng, và câu đó phải tự viết ra trước khi phản biện viết nó.

## Dạng KAN, và chi phí dựng ma trận nhân lượng tử
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`KAN: f(x) = Σ_q Φ_q( Σ_p φ_{q,p}(x_p) ) · QSVM: số phần tử phải ước lượng = n(n−1)/2 · số lần chạy mạch mỗi phần tử bậc 1/ε² · tổng số lần chạy mạch = n(n−1)/2 · 1/ε²`

**Giả thiết nó đứng trên:**

## Dạng KAN, và chi phí dựng ma trận nhân lượng tử (tiếp)
@phut: 1
@che-do: so

- Với KAN: định lý Kolmogorov-Arnold là định lý TỒN TẠI của một biểu diễn, không kèm thuật toán tìm, không kèm số mẫu cần, và không bảo đảm các hàm một biến trơn. Biểu diễn được không kéo theo học được
- Với KAN: so sánh số tham số chỉ có nghĩa khi khai cùng lúc thời gian huấn luyện và thời gian suy luận, vì một tham số của KAN là một hàm trên cạnh chứ không phải một số vô hướng

## Dạng KAN, và chi phí dựng ma trận nhân lượng tử (tiếp)
@phut: 1
@che-do: so

- Với QSVM: ma trận nhân đối xứng và đường chéo bằng {{s005}}, tức dùng nhân fidelity giữa hai trạng thái đã mã hoá; nếu nhân khác thì số phần tử khác
- Với QSVM: mỗi phần tử nhân là một XÁC SUẤT, chỉ đọc được bằng cách chạy mạch nhiều lần rồi đếm tần suất; không có cách đọc biên độ trực tiếp

## Dạng KAN, và chi phí dựng ma trận nhân lượng tử (tiếp)
@phut: 1
@che-do: so

- Với QSVM: bậc 1/ε² là chặn DƯỚI, vì nó chỉ tính nhiễu lấy mẫu. Nhiễu phần cứng, lỗi đọc và trôi hiệu chuẩn đều làm số lần chạy thật lớn hơn
- Với QSVM: giả thiết có phần cứng chạy được số lần chạy mạch đó; nếu con số chạy trên bộ mô phỏng cổ điển thì mọi tuyên bố về thời gian là tuyên bố về bộ mô phỏng

## Dạng KAN, và chi phí dựng ma trận nhân lượng tử · ghi
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hai chỗ số học phải nhớ. Thứ nhất, số phần tử đi theo `n²` nên nhân đôi số mẫu là gấp bốn chi phí, trong khi một bộ cây gần như tuyến tính theo số mẫu. Thứ hai, ở lúc suy luận một mẫu mới vẫn cần `n` phần tử nhân, mỗi cái lại cần `1/ε²` lần chạy, nên QSVM đắt ở cả hai đầu chứ không chỉ ở huấn luyện.

## Dạng KAN, và chi phí dựng ma trận nhân lượng tử · (tiếp)
@phut: 0.5
@che-do: noi

Đây là chỗ một tuyên bố tăng tốc dễ chết nhất, và nó chết bằng phép nhân chứ không bằng tranh luận.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s003}} | tính chất | Theo Grinsztajn và cộng sự
!so {{s006}} | tuyên bố | Trong sổ lỗi của nhà

## QSVM trên 2000 mẫu huấn luyện
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

QSVM trên {{s007}} mẫu huấn luyện, muốn sai số cộng tính {{s009}} cho mỗi phần tử ma trận nhân. Tổng số lần chạy mạch cho MỘT lần huấn luyện là bao nhiêu?

n = {{s007}}, eps = {{s008}}

## QSVM trên 2000 mẫu huấn luyện · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`n⋆(n-1)/2/(eps⋆eps)`

Khoảng {{s010}} × 10⁹ lần chạy mạch, tức gần năm tỉ. Hai chuyện phải đọc ra. Thứ nhất, nới sai số từ {{s011}} lên {{s009}} chỉ bớt được bốn lần số lần chạy, trong khi nhân đôi số mẫu từ {{s012}} lên {{s007}} lại nhân bốn, nên hai hiệu ứng triệt tiêu nhau và tổng vẫn ở cùng bậc năm tỉ. Thứ hai, con số này là CHẶN DƯỚI:

## QSVM trên 2000 mẫu huấn luyện · đáp (tiếp)
@phut: 1
@che-do: noi

nó chỉ tính nhiễu lấy mẫu, chưa tính lỗi đọc, nhiễu phần cứng, trôi hiệu chuẩn, và chưa tính tinh chỉnh siêu tham số hay kiểm chéo.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cùng QSVM, nay trên {{s013}} mẫu với sai số cộng tính {{s011}}, và mỗi lần chạy mạch mất {{s016}} giây. Một lần huấn luyện tiêu bao nhiêu ngày máy lượng tử liên tục?

n = {{s013}}, eps = {{s014}}, tq = {{s015}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`n⋆(n-1)/2/(eps⋆eps)⋆tq/86400`

Khoảng {{s017}} ngày máy lượng tử liên tục, cho MỘT ma trận nhân ở MỘT bộ siêu tham số. Đây là con số dùng được ngay trong phản biện, theo hai chiều. Chiều thứ nhất, nếu bài báo khai chạy QSVM trên {{s013}} mẫu thật thì phải khai luôn đã chạy ở đâu và trong bao lâu, vì {{s017}} ngày là một dữ kiện kiểm được.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Chiều thứ hai, nếu con số thời gian trong bài nhỏ hơn thế nhiều thì nó là thời gian của bộ mô phỏng cổ điển, và lúc đó tuyên bố về tăng tốc lượng tử không có đại lượng nào đỡ. Đối chiếu: {{s013}} mẫu là một mẫu con rất nhỏ so với {{s018}} bản ghi huấn luyện của NSL-KDD.

## Bài báo khai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài báo khai: mô hình mới của chúng tôi đạt F1 {{s019}} so với {{s020}} của XGBoost. Thiếu đúng một dữ kiện để kiểm câu đó. Dữ kiện nào?

- Thời gian huấn luyện của mô hình mới
- Số tham số của hai mô hình
- Ngân sách tìm siêu tham số của mỗi bên: số lần thử, không gian tìm, tiêu chí chọn, tập dùng để chọn
- Phiên bản thư viện XGBoost

## Bài báo khai · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Ngân sách tìm siêu tham số của mỗi bên: số lần thử, không gian tìm, tiêu chí chọn, tập dùng để chọn**

## Bài báo khai · đáp (tiếp)
@phut: 1
@che-do: noi

Hiệu {{s021}} điểm trên dữ liệu bảng nằm trong khoảng mà ngân sách tinh chỉnh một mình có thể tạo ra. Không biết ngân sách của hai bên thì không phân biệt được chất lượng mô hình với công sức tác giả, nên tuyên bố không kiểm được. Phiên bản thư viện là chi tiết tái lập, có ích nhưng không gỡ được chỗ này. Số tham số và thời gian huấn luyện đo hai thứ khác.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài QSVM khai thời gian suy luận {{s022}} mili giây một mẫu, chạy trên bộ mô phỏng cổ điển, rồi kết luận có tăng tốc so với SVM cổ điển. Chỗ sai nặng nhất là gì?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Mô phỏng chậm hơn phần cứng thật nên con số là bi quan
- Tỉ số tăng tốc không còn đại lượng nào để đo: cả hai con số đều là thời gian chạy trên CPU, nên phép so không nói gì về lượng tử
- Thiếu kiểm chéo
- Chưa khai số qubit

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tỉ số tăng tốc không còn đại lượng nào để đo: cả hai con số đều là thời gian chạy trên CPU, nên phép so không nói gì về lượng tử**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

So thời gian của một bộ mô phỏng lượng tử trên CPU với thời gian của một thuật toán cổ điển trên CPU là so hai chương trình trên cùng một loại máy, nên nó không chứa thông tin về lượng tử. Đáp án thứ nhất là một suy đoán theo chiều có lợi và cũng không cứu được phép so. Số qubit và kiểm chéo đều nên khai, nhưng chúng không phải chỗ làm kết luận sụp. Cách sửa:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

báo SỐ LẦN CHẠY MẠCH thay cho thời gian, vì đó là đại lượng của thuật toán và kiểm được mà không cần thiết bị.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Dataset nào trong bốn thứ dưới đây làm cho lập luận cây thắng trên dữ liệu bảng YẾU đi, tức mở ra chỗ chính đáng cho một kiến trúc khác?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Luồng đã trích {{s023}} đặc trưng số bằng CICFlowMeter
- Byte thô của gói tin, tức dữ liệu chuỗi có cấu trúc cục bộ và thứ tự quan trọng
- Bảng luồng có nhiều đặc trưng vô ích
- Bảng luồng mà một số đặc trưng bị đổi đơn vị từ byte sang kilobyte

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Byte thô của gói tin, tức dữ liệu chuỗi có cấu trúc cục bộ và thứ tự quan trọng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ba lý do cây thắng đều là lý do về dữ liệu BẢNG: bất biến đơn điệu, biên không trơn, chịu đặc trưng vô ích. Byte thô không phải dữ liệu bảng: thứ tự và cấu trúc cục bộ mang thông tin, và cây không khai thác được quan hệ đó. Đáp án thứ ba và thứ tư lại đúng là hai chỗ cây MẠNH, nên chúng củng cố lập luận chứ không làm yếu. Hệ quả:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

muốn đề một kiến trúc mới thì chọn đơn vị quan sát nơi dữ liệu không còn là bảng, đó là lập luận bền hơn nhiều so với việc đua điểm trên cùng một bảng.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn so sánh sau có một chỗ làm toàn bộ bảng xếp hạng mất hiệu lực. Bấm vào chỗ đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi rà {{s024}} cấu hình siêu tham số cho mô hình đề xuất bằng tìm kiếm Bayes,
- và dùng tham số mặc định của thư viện cho XGBoost, LightGBM và Random Forest,
- rồi báo F1 trên cùng một cách chia theo thời gian cho cả bốn mô hình.
- Mọi con số đều là trung bình của {{s025}} hạt, kèm độ lệch chuẩn.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và dùng tham số mặc định của thư viện cho XGBoost, LightGBM và Random Forest,**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là so mô hình đã tinh chỉnh kỹ với baseline để mặc định, và nó là câu hỏi đầu tiên của mọi phản biện về mô hình mới. Trên dữ liệu bảng, hiệu một tới hai điểm nằm hoàn toàn trong khoảng mà ngân sách tinh chỉnh một mình tạo ra, nên bảng xếp hạng đang đo tổng của chất lượng mô hình và công sức tác giả. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

rà cùng ngân sách cho cả hai bên trong không gian tìm hợp lý của từng họ mô hình, rồi báo đường hiệu năng theo số lần thử cho cả hai, và nói rõ hai đường có cắt nhau hay không. Ba câu còn lại đều hợp lệ.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn lập luận về KAN sau có một câu không đứng được. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- KAN thay trọng số vô hướng bằng hàm một biến học được trên cạnh, theo dạng Kolmogorov-Arnold.
- Vì dạng này biểu diễn được mọi hàm liên tục nhiều biến, KAN có dung lượng biểu diễn cao hơn MLP cùng số tham số, nên nó học tốt hơn trên dữ liệu bảng của IDS.
- Chúng tôi báo thời gian huấn luyện và thời gian suy luận cạnh số tham số, vì một tham số của KAN là một hàm trên cạnh.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Baseline MLP được rà cùng {{s024}} cấu hình như KAN, trong không gian tìm riêng của nó.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì dạng này biểu diễn được mọi hàm liên tục nhiều biến, KAN có dung lượng biểu diễn cao hơn MLP cùng số tham số, nên nó học tốt hơn trên dữ liệu bảng của IDS.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Bước nhảy từ biểu diễn được sang học tốt hơn không có cầu nối. Định lý Kolmogorov-Arnold là định lý TỒN TẠI: nó không nói thuật toán gradient tìm tới được biểu diễn đó, không nói cần bao nhiêu mẫu, không bảo đảm các hàm một biến trơn. Đối chiếu dứt điểm: mạng một lớp ẩn đủ rộng cũng xấp xỉ được mọi hàm liên tục trên tập compact, và không ai lấy đó làm bằng chứng thắng.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Đây đúng là chỗ năm tuyên bố của bài KAN gốc đã bị phản bác. Cách sửa: bỏ chữ nên, giữ phần biểu diễn như một động cơ thiết kế, rồi đưa bằng chứng thực nghiệm ở cùng ngân sách tinh chỉnh; hoặc đổi sang một tuyên bố kiểm được khác, ví dụ hàm trên cạnh đọc ra được dạng đóng nên dễ giải thích hơn. Câu đầu và hai câu cuối đều hợp lệ.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bảng chi phí QSVM sau có một dòng làm dòng cuối không đọc được. Bấm vào dòng đó.

- Số mẫu huấn luyện sau khi lấy mẫu con: {{s026}}
- Sai số cộng tính đặt cho mỗi phần tử ma trận nhân: {{s011}}
- Số lần chạy mạch để dựng ma trận nhân: {{s027}} tỉ
- Nền chạy: không khai
- Thời gian báo trong bài: {{s028}} giây

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Nền chạy: không khai**

Dòng cuối báo thời gian, mà thời gian chỉ có nghĩa khi biết nó chạy trên đâu: thiết bị lượng tử thật, hay bộ mô phỏng cổ điển trên CPU. Thiếu dòng này thì {{s028}} giây không đối chiếu được với bất cứ cái gì, và đặc biệt không đối chiếu được với {{s029}} ngày máy mà chính ba dòng trên đã hàm ý ở 10⁻⁴ giây một lần chạy.

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Chênh lệch giữa {{s028}} giây và {{s029}} ngày là dấu hiệu gần như chắc chắn rằng con số là của bộ mô phỏng. Chú ý ba dòng trên đều hợp lệ và đều là những dòng nên có. Cách sửa: khai nền chạy, và nếu là mô phỏng thì bỏ cột thời gian, chỉ giữ cột số lần chạy mạch, vì đó là đại lượng của thuật toán.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Ma trận nhân đối xứng và đường chéo bằng {{s005}}, nên chỉ phải ước lượng n(n−1)/2 phần tử
- Mỗi phần tử là một xác suất, đọc được bằng cách chạy mạch R lần rồi đếm tần suất của một biến cố
- Sai số của một tần suất giảm theo {{s005}} chia căn R, nên để đạt sai số cộng tính ε cần R bậc 1/ε²
- Tổng số lần chạy mạch cho cả ma trận là n(n−1)/2 nhân 1/ε²

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Thời gian tường bằng tổng số lần chạy nhân thời gian một lần chạy, gồm nạp, chạy, đọc và đặt lại, rồi chia cho {{s030}} để ra ngày

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: mô hình mới xếp nhất · QSVM: {{s031}} phần tử nhân, {{s027}} tỉ lần chạy mạch, {{s029}} ngày máy, {{s025}} triệu lần chạy mỗi mẫu suy luận

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Baseline được tinh chỉnh ở ngân sách tương đương** tắt đi: Baseline chạy tham số mặc định của thư viện, hoặc được rà {{s006}} cấu hình trong khi mô hình mới được rà {{s024}}.
- **Hai bên đo trên cùng cách chia, cùng tỉ lệ nền, cùng đơn vị quan sát** tắt đi: Mô hình mới đo trên mẫu con cân bằng {{s013}} luồng, còn baseline lấy số từ một bài khác đo trên toàn bộ dataset theo đơn vị cửa sổ.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Có phần cứng lượng tử chạy được số lần chạy mạch đã tính** tắt đi: Thí nghiệm chạy trên bộ mô phỏng cổ điển, hoặc chạy trên thiết bị thật nhưng chỉ cho một mẫu con rất nhỏ rồi ngoại suy.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biểu diễn được kéo theo học được trong ngân sách tối ưu hoá đang dùng** tắt đi: Định lý biểu diễn chỉ nói có một biểu diễn tồn tại, không nói thuật toán gradient tìm tới được, không nói cần bao nhiêu mẫu, không nói các hàm một biến đó trơn.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Chi phí dựng ma trận nhân của QSVM. Kéo số mẫu huấn luyện, sai số cộng tính muốn đạt cho mỗi phần tử nhân, và thời gian một lần chạy mạch. Xem con số giờ máy, rồi so với một bộ gradient boosting chạy trong vài phút trên một máy để bàn.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.8` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table V compares the proposed architecture against XGBoost, LightGBM and Random Forest, but Section IV-C states that {{s024}} hyperparameter configurations were searched for the proposed model while the baselines use library defaults. On tabular data a gap of one to two F1 points is within the range that tuning budget alone produces. Please equalise the tuning budget or withdraw the ranking claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have equalised the budget. Section IV-C now gives every model the same number of trials under the same search protocol, each within a search space appropriate to its own family, with the same selection criterion and the same selection split, and Table V reports the mean and spread over ten seeds.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also added Figure {{s033}}, which plots best-so-far performance against the number of trials for each model, so the reader can see the effect of the budget directly rather than trusting a single endpoint. Under equal budgets the gap against the strongest tree baseline narrows and the two curves overlap within their spread, so we have withdrawn the ranking claim from the abstract and the conclusion and state instead that the proposed model is competitive with a tuned gradient boosting baseline on this data.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The contribution has been restated on the axis where the measurement does separate the two: parameter count and inference latency at a fixed operating point, which we now report as the headline comparison, with the accuracy table kept as a parity check rather than as evidence of superiority. We also report the tuning cost itself in Table VI, since a model that needs {{s024}} trials to match a baseline that needs {{s032}} is more expensive to deploy, and that is part of the result.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: trả lời rằng tham số mặc định của các thư viện này đã được cộng đồng chọn kỹ nên là baseline hợp lý. Sai, và nó còn tránh câu hỏi: vấn đề không phải mặc định có tốt hay không mà là hai bên không cùng ngân sách.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: rà thêm vài cấu hình cho baseline, ví dụ {{s032}} so với {{s024}} của mô hình mới, rồi báo lại bảng. Đã đúng hướng nhưng ngân sách vẫn lệch một bậc, nên phản bác vẫn đứng nguyên.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: rà cùng ngân sách cho mọi mô hình, mỗi họ trong không gian tìm hợp lý của nó, cùng tiêu chí chọn và cùng tập dùng để chọn, rồi báo lại bảng kèm trung bình và độ phân tán qua nhiều hạt. Và khai rõ ngân sách đó trong phần phương pháp.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V claims a quantum speedup for the proposed QSVM kernel. The experiments were executed on a statevector simulator, and the paper reports wall clock time of the simulator against wall clock time of a classical SVM on the same workstation. Please justify the speedup claim or remove it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The speedup claim has been removed from the abstract, Section V and the conclusion, and the wall clock column has been deleted rather than renamed, because comparing a statevector simulator on a CPU against a classical solver on the same CPU carries no information about quantum execution. Section V now reports the cost of the kernel in the unit that belongs to the algorithm:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the number of circuit executions, n(n-1)/2 kernel entries times order 1/epsilon squared executions each, with the figure for our subsample size, and we state that this is a lower bound since it accounts only for sampling noise and not for readout error, hardware noise or calibration drift. We report the inference cost separately, because it scales linearly in n rather than quadratically and it is where deployability is decided.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The execution platform is stated explicitly as a simulator, including the version and the noise model, and we no longer place simulator timings beside classical timings anywhere in the paper. Finally we restated the contribution:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

rather than claiming an advantage over classical methods, we measure the reduction in circuit executions and in qubit count against a published QSVM implementation at matched kernel accuracy, which is a quantity that can be checked without access to hardware, and we report the accuracy of the resulting kernel matrix against the exactly computed one so the reader can see what the reduction costs.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: lập luận rằng mô phỏng chậm hơn phần cứng thật nên con số đang bi quan, tức tăng tốc thật sẽ lớn hơn. Đây là suy đoán theo chiều có lợi, và nó không cứu được phép so vì cả hai con số vẫn chạy trên cùng một loại máy.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: bỏ chữ speedup khỏi tóm tắt nhưng giữ bảng thời gian và giữ đoạn thảo luận nói về tiềm năng tăng tốc. Đổi từ mà không đổi tuyên bố, nên bảng vẫn mời người đọc đến đúng kết luận đã rút.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: bỏ hẳn cột thời gian, chuyển sang báo số lần chạy mạch và số qubit, khai rõ nền chạy là mô phỏng, và phát biểu lại đóng góp theo đơn vị của thuật toán chứ không theo giây.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.8` bấm thẻ.
