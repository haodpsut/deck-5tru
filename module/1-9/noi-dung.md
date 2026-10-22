---
tieu-de: Hiệu chuẩn: điểm số của mô hình có phải xác suất
phu-de: Trụ 1 NID · module 1.9
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 81.5
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

Khi mô hình của tôi in ra {{s001}}, có đúng {{s002}} các lần như thế là tấn công thật không, và nếu không thì ngưỡng tôi chọn còn nghĩa gì?

## Thứ hạng và xác suất là hai thứ khác nhau
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Một bộ phát hiện in ra một số trong khoảng {{s003}} tới {{s004}}. Số đó dùng được cho hai việc rất khác nhau: **xếp hạng** các luồng, và **định lượng** khả năng một luồng là tấn công. AUROC, AUPRC và mọi phép đo dựa trên đường cong chỉ đọc thứ hạng. Chúng không nhìn thấy việc con số {{s001}} có nghĩa là {{s002}} hay không, và không có bất kỳ giá trị AUROC nào chứng minh được điều đó.

## Thứ hạng và xác suất là hai thứ khác nhau (tiếp)
@phut: 1
@che-do: noi

Module này tách hai việc ra. Hệ quả nối thẳng sang module {{s005}}: ngưỡng tối ưu chỉ đọc được trực tiếp từ tỉ lệ chi phí khi điểm số đã hiệu chuẩn. Chưa hiệu chuẩn thì `ngưỡng {{s001}}` là một nhãn trên thang riêng của mô hình, và nó trỏ tới một điểm làm việc khác với mỗi phép biến đổi đơn điệu mà anh áp lên logit, dù không ai sửa một tham số nào của mô hình.

## Thứ hạng và xác suất là hai thứ khác nhau (tiếp)
@phut: 1
@che-do: noi

Ba thứ anh phải khai được sau module này: định nghĩa hiệu chuẩn hoàn hảo, vì sao ECE không đọc được khi thiếu số ô, và vì sao hiệu chỉnh nhiệt độ không thể đổi AUROC.

## Hiệu chuẩn hoàn hảo
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Hiệu chuẩn hoàn hảo · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bộ phân loại có điểm số `s(x)` hiệu chuẩn hoàn hảo khi `P(y = {{s004}} | s(x) = p) = p` với mọi `p` trong miền giá trị của điểm số.

## Hiệu chuẩn hoàn hảo · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đây là tính chất của **cặp** gồm mô hình và phân bố dữ liệu, không phải tính chất riêng của mô hình. Đổi phân bố lúc chạy thì cùng một mô hình thôi hiệu chuẩn, dù không ai sửa một trọng số nào. Vì vậy mọi tuyên bố hiệu chuẩn phải đi kèm mô tả phân bố đã đo trên đó.

## Hiệu chỉnh nhiệt độ, và vì sao AUROC không thấy nó
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s006}} trên bốn.*

## Hiệu chỉnh nhiệt độ, và vì sao AUROC không thấy nó · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một tham số duy nhất `T > {{s003}}`, học trên một tập hiệu chuẩn tách riêng, cho điểm số mới `s'(x) = sigma(z(x)/T)` với `z` là logit của mô hình.

Điểm phải nhớ: **AUROC không nhìn thấy hiệu chuẩn.** Vì `z > z'` tương đương `sigma(z/T) > sigma(z'/T)` với mọi `T > {{s003}}`, phép này không đổi thứ hạng của bất kỳ cặp luồng nào, nên AUROC, AUPRC và mọi phép đo dựa trên thứ hạng đứng yên tuyệt đối.

## Hiệu chỉnh nhiệt độ, và vì sao AUROC không thấy (tiếp)
@phut: 1
@che-do: noi

Ai báo rằng hiệu chỉnh nhiệt độ nâng AUROC là đang báo một con số không thể xảy ra, và chỗ phải đi tìm là quy trình chia tập hoặc cách xử lý điểm số bằng nhau, không phải phép hiệu chỉnh.

## ECE, số ô M, và sàn do mẫu hữu hạn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s007}} trên bốn.*

## ECE, số ô M, và sàn do mẫu hữu hạn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`ECE = sum_m (|B_m|/n) · |acc(B_m) − conf(B_m)|`, với `B_m` là ô thứ `m` trong `M` ô chia theo điểm số, và `n` là số mẫu.

## ECE, số ô M, và sàn do mẫu hữu hạn · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **ECE phụ thuộc M**, nên báo ECE mà không báo `M` là không khai được. Thêm một chuyện ít ai viết: với số mẫu hữu hạn, ECE ước lượng có một **sàn dương**. Ngay cả mô hình hiệu chuẩn hoàn hảo cũng cho ECE lớn hơn {{s003}}, vì trong mỗi ô thì tần suất quan sát lệch khỏi tần suất thật theo cỡ nghịch với căn số mẫu trong ô. Hệ quả:

## ECE, số ô M, và sàn do mẫu hữu hạn · đáp (tiếp)
@phut: 1
@che-do: noi

một con số ECE nhỏ ở M nhỏ không chứng minh gì, và so hai bài ở hai giá trị M là so hai thước đo khác nhau.

## Công thức và giả thiết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Hiệu chuẩn hoàn hảo: P(y = {{s004}} | s(x) = p) = p ECE = sum_m (|B_m|/n) · |acc(B_m) − conf(B_m)| Hiệu chỉnh nhiệt độ: s'(x) = sigma(z(x)/T) Ngưỡng theo chi phí: q⋆ = c_FP/(c_FP + c_FN)`

**Giả thiết nó đứng trên:**

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- ECE: mỗi ô có đủ mẫu để tần suất trong ô là một ước lượng dùng được; thiếu điều này thì con số đo cái sàn chứ không đo sai lệch
- ECE: số ô M chốt TRƯỚC khi xem kết quả, nếu không thì giá trị nhỏ nhất trên một họ M là một đại lượng khác hẳn
- Hiệu chỉnh nhiệt độ: T học trên một tập hiệu chuẩn tách khỏi tập kiểm, và T lớn hơn {{s003}}

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- Ngưỡng theo chi phí: chi phí mỗi loại lỗi là một hằng số, quyết định từng luồng độc lập, và điểm số đã hiệu chuẩn nên dùng được thay cho xác suất hậu nghiệm

## Công thức · ghi chú
@phut: 1
@che-do: noi

Ba công thức này là ba tầng khác nhau. Dòng một là **định nghĩa**, nên nó không có số. Dòng hai là **ước lượng**, nên nó có hai tham số tự do là M và n, và cả hai phải khai. Dòng ba là **phép biến đổi**, nên nó chỉ đổi thang điểm, không đổi thông tin. Dòng bốn là **quyết định**, và nó là dòng duy nhất dùng được cho vận hành, nhưng nó đứng trên dòng một.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s003}} |  | Một bộ phân loại hiệu chuẩn hoàn hảo
!so {{s003}} |  | Anh áp hiệu chỉnh nhiệt độ với một T khác {{s004}} lên
!so {{s008}} | ô | Khi báo ECE, công trình nền của chủ đề này chia điểm

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bảng tin cậy chia ba ô trên {{s015}} mẫu kiểm. Ô một có {{s009}} mẫu và lệch tin cậy {{s016}}; ô hai có {{s011}} mẫu và lệch {{s017}}; ô ba có {{s013}} mẫu và lệch {{s018}}. ECE bằng bao nhiêu?

n1 = {{s009}}, d1 = {{s010}}, n2 = {{s011}}, d2 = {{s012}}, n3 = {{s013}}, d3 = {{s014}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(n1⋆d1 + n2⋆d2 + n3⋆d3)/(n1 + n2 + n3)`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s019}}. Con số này chỉ đọc được khi khai kèm số ô, ở đây là ba ô: cùng bộ điểm số đó chia {{s008}} ô sẽ cho một giá trị khác, thường cao hơn, vì ô hẹp hơn thì ít sai lệch trong ô bị làm phẳng. Để ý thêm là ô ba chỉ có {{s013}} mẫu mà lại mang lệch lớn nhất, nên phải kiểm xem {{s018}} là sai lệch thật hay là sàn do ít mẫu.

## Bỏ sót một tấn công tốn 100 đơn vị
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bỏ sót một tấn công tốn {{s020}} đơn vị, một cảnh báo sai tốn {{s004}} đơn vị. Ngưỡng tối ưu trên xác suất hậu nghiệm bằng bao nhiêu?

cfp = {{s004}}, cfn = {{s020}}

## Bỏ sót một tấn công tốn 100 đơn vị · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`cfp/(cfp + cfn)`

Khoảng {{s021}}, tức đúng {{s022}}. Để ý biểu thức không chứa tỉ lệ nền: tỉ lệ nền đã nằm trong xác suất hậu nghiệm, nên ngưỡng Bayes trên xác suất là cùng một con số ở mọi mạng. Và đây là chỗ hiệu chuẩn đi vào: con số này áp trực tiếp lên điểm số của mô hình chỉ khi điểm số đã hiệu chuẩn.

## Bỏ sót một tấn công tốn 100 đơn vị · đáp (tiếp)
@phut: 1
@che-do: noi

Chưa hiệu chuẩn thì phải quét đường ROC với tỉ lệ nền khai rõ, và lúc đó ngưỡng trên thang điểm số không còn đọc được từ tỉ lệ chi phí.

## Theo mô hình khai trong mô phỏng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Theo mô hình khai trong mô phỏng, logit lớp lành là Logistic(0, {{s004}}) nên ngưỡng điểm số {{s001}} trên thang đã chia nhiệt độ T cho FPR bằng 1/(1 + 9^T). Ở T = {{s006}}, FPR là bao nhiêu phần trăm?

T = {{s006}}

## Theo mô hình khai trong mô phỏng · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100/(1 + Math.pow(9, T))`

Khoảng {{s023}}. Cùng ba chữ ngưỡng {{s001}} mà ở T = {{s004}} thì FPR là {{s024}}, còn ở T = {{s006}} chỉ còn {{s023}}: tám lần chênh lệch cho một nhãn ngưỡng không đổi. Đó là nội dung đầy đủ của câu ngưỡng trên điểm số chưa hiệu chuẩn là một nhãn, không phải một điểm làm việc. Hệ quả cho bài báo: phải khai điểm làm việc bằng cặp TPR với FPR, chứ không khai bằng giá trị ngưỡng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh áp hiệu chỉnh nhiệt độ với T = {{s025}} lên cùng bộ logit, trên cùng tập đánh giá. Đại lượng nào KHÔNG đổi?

- AUROC và AUPRC
- ECE ở {{s008}} ô
- Precision tại ngưỡng điểm số {{s001}}
- Chi phí kỳ vọng tại ngưỡng điểm số {{s001}}

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**AUROC và AUPRC**

AUROC và AUPRC chỉ đọc thứ hạng, và chia logit cho một số dương là phép đơn điệu tăng nên không đổi thứ hạng của bất kỳ cặp nào. Ba đại lượng còn lại đều neo vào một giá trị tuyệt đối trên thang điểm số:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

ECE đo khoảng cách giữa điểm số và xác suất nên nó là mục tiêu của phép hiệu chỉnh, còn precision và chi phí đo tại ngưỡng {{s001}} nên chúng đổi vì cùng nhãn ngưỡng ứng với một logit khác sau khi chia nhiệt độ.

## Một bài báo khai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai: ECE sau hiệu chỉnh nhiệt độ là {{s026}}. Thiếu đúng một dữ kiện để kiểm con số đó. Dữ kiện nào?

- Kiến trúc mô hình
- Giá trị T học được
- Số ô M và số mẫu của tập đo
- AUROC trước và sau hiệu chỉnh

## Một bài báo khai · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Số ô M và số mẫu của tập đo**

ECE là ước lượng theo ô, nên giá trị của nó là hàm của số ô và của số mẫu. Không có hai con số đó thì {{s026}} không so được với bài nào khác, và cũng không phân biệt được với sàn do mẫu hữu hạn.

## Một bài báo khai · đáp (tiếp)
@phut: 1
@che-do: noi

Giá trị T học được thì hữu ích để tái lập nhưng tự nó không làm con số ECE đọc được; AUROC trước và sau thì theo định nghĩa phải bằng nhau nên nó không mang thông tin về hiệu chuẩn; kiến trúc thì không vào biểu thức ECE.

## Anh học T trên chính tập kiểm
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh học T trên chính tập kiểm, rồi báo ECE trên tập kiểm đó. Chuyện gì xảy ra với con số báo ra?

- Nó không đổi, vì một tham số thì không thể quá khớp
- Nó chệch lên, nên con số báo ra bi quan
- Nó không còn tính được
- Nó chệch xuống, nên con số báo ra lạc quan có hệ thống

## Anh học T trên chính tập kiểm · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Nó chệch xuống, nên con số báo ra lạc quan có hệ thống**

## Anh học T trên chính tập kiểm · đáp (tiếp)
@phut: 1
@che-do: noi

T được chọn để tối thiểu hoá chính hàm mất mát đo trên tập đó, nên giá trị tối thiểu quan sát được thấp hơn giá trị kỳ vọng lúc chạy, tức con số nghe hay hơn thực tế. Một tham số vẫn đủ để sinh chệch: cỡ của chệch nhỏ hơn so với mô hình nhiều tham số, nhưng dấu của nó cố định. Chiều bi quan là chiều ngược, không xảy ra ở đây.

## Anh học T trên chính tập kiểm · đáp (tiếp)
@phut: 1
@che-do: noi

Và con số vẫn tính ra được, nên nói nó không tính được là sai: cái mất không phải khả năng tính, mà là ý nghĩa.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một dòng không kiểm được. Bấm vào dòng đó.

- Chúng tôi áp hiệu chỉnh nhiệt độ trên một tập hiệu chuẩn tách riêng, học được T = {{s027}}.
- ECE giảm từ {{s028}} xuống {{s026}}.
- AUROC giữ nguyên ở {{s029}} trước và sau, đúng như dự đoán vì phép hiệu chỉnh là đơn điệu tăng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**ECE giảm từ {{s028}} xuống {{s026}}.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

ECE là ước lượng theo ô, nên hai con số này là hàm của số ô M và của số mẫu mỗi ô, mà cả hai đều không khai. Ở M = {{s030}} và ở M = {{s031}} thì cùng một bộ điểm số cho hai cặp giá trị khác nhau, nên dòng này không so được với bài khác, và cũng không tách được phần giảm thật khỏi phần sàn do mẫu hữu hạn. Cách sửa rẻ nhất:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

thêm M và số mẫu tập đo. Cách sửa tốt hơn: báo ECE ở hai ba giá trị M, kèm sàn tính từ chính n đó, và kèm một đường tin cậy để người đọc thấy sai lệch nằm ở vùng điểm nào.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau trộn hai đại lượng khác nhau. Bấm vào chỗ trộn.

- Tại ngưỡng điểm số {{s001}}, bộ phát hiện đạt precision {{s032}} trên tập đánh giá.
- Nói cách khác, khi mô hình in ra {{s001}} thì khoảng {{s033}} các lần như thế là tấn công thật, nên mô hình đã hiệu chuẩn tốt ở vùng điểm cao.
- Chúng tôi chọn ngưỡng {{s001}} vì nó cân bằng cảnh báo sai với bỏ sót ở tỉ lệ nền của tập đánh giá.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Nói cách khác, khi mô hình in ra {{s001}} thì khoảng {{s033}} các lần như thế là tấn công thật, nên mô hình đã hiệu chuẩn tốt ở vùng điểm cao.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Precision tại ngưỡng là P(y = {{s004}} khi s lớn hơn hoặc bằng {{s001}}), một đại lượng tính trên cả ĐUÔI điểm số từ {{s001}} lên tới {{s004}}. Hiệu chuẩn tại {{s001}} là P(y = {{s004}} khi s bằng {{s001}}), một đại lượng tính trên MỘT Ô quanh {{s001}}. Hai cái hiếm khi bằng nhau: khi điểm số tăng theo khả năng là tấn công, đuôi chứa những điểm cao hơn {{s001}} nên precision của đuôi lớn hơn giá trị hiệu chuẩn tại biên.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Suy từ cái đầu ra cái sau là bước không có cơ sở, và nó luôn suy theo chiều làm mô hình trông hiệu chuẩn hơn thực tế. Hai dòng kia hợp lệ: một là phép đo, một là khai lý do chọn ngưỡng.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Với một luồng có xác suất hậu nghiệm q, chi phí khi báo động là ({{s004}} − q)·c_FP, chi phí khi im lặng là q·c_FN
- Báo động rẻ hơn khi ({{s004}} − q)·c_FP < q·c_FN
- Sắp lại: q > c_FP/(c_FP + c_FN). Đây là ngưỡng trên XÁC SUẤT HẬU NGHIỆM, và nó không chứa tỉ lệ nền vì tỉ lệ nền đã nằm trong q

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Điểm số s(x) thay được cho q chỉ khi P(y = {{s004}} | s(x) = v) = v, tức khi điểm số đã hiệu chuẩn trên phân bố đang chạy
- Với c_FP = {{s004}} và c_FN = {{s020}}, ngưỡng là {{s022}}. Chưa hiệu chuẩn thì bước {{s034}} hỏng, và ngưỡng phải tìm bằng cách quét đường ROC với tỉ lệ nền khai rõ, chứ không đọc được từ tỉ lệ chi phí

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: ECE {{s036}} ở M = {{s008}} ô · AUROC {{s037}} · precision tại ngưỡng {{s001}} là {{s038}} · chi phí kỳ vọng {{s039}} đơn vị mỗi sự kiện

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Tập hiệu chuẩn tách khỏi tập kiểm** tắt đi: T học trên chính tập kiểm, rồi ECE báo ngay trên tập đó.
- **Phân bố lúc chạy giống lúc hiệu chuẩn** tắt đi: Mạng đích có cấu hình lưu lượng khác tập hiệu chuẩn.
- **Số ô M và số mẫu khai cùng ECE, và M chốt trước khi xem kết quả** tắt đi: M chọn sau khi xem kết quả, lấy giá trị cho ECE nhỏ nhất, và số mẫu không khai.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mỗi ô có đủ mẫu** tắt đi: Chia {{s031}} ô trên {{s035}} mẫu kiểm, nên nhiều ô chỉ còn vài mẫu.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Công trình nền về hiệu chuẩn mạng neural báo ECE với {{s030}} ô, nên {{s030}} là số ô quy ước của lĩnh vực.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỔ**

ĐỔ, và đổ ở chỗ kiểm được trong ba mươi giây. Bài của Guo và cộng sự định nghĩa ECE bằng cách chia dự đoán vào M ô rộng 1/M, rồi mọi bảng kết quả của bài đều ghi rõ M = {{s008}}. Không có con số {{s030}} nào trong đó. Quan trọng hơn con số:

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

ECE không có số ô quy ước, vì nó là ƯỚC LƯỢNG theo ô, nên cùng một bộ điểm số cho giá trị khác nhau ở M khác nhau. Một bảng báo ECE mà không khai M và không khai số mẫu là bảng không so được với bài khác.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bốn con số, một mô hình. Mô phỏng này khai bằng DỮ LIỆU ba mảnh giải tích, không phải số đo trên một mô hình thật, và ba mảnh đó là:

## Chỗ này phải tự kéo, không xem được (tiếp)
@phut: 1
@che-do: demo

độ phân biệt theo họ ROC `TPR = FPR^(1/k)` nên `AUROC = k/(k+1)`; đường tin cậy theo luật nhiệt độ nên ECE dân số bằng `|T0 − T| / (2(T0 + T))` với T0 là nhiệt độ thật; và sàn ước lượng do mẫu hữu hạn bằng `sqrt(M / (2·pi·n))` với `n = {{s040}}` khai cố định. Logit của lớp lành khai là Logistic(0, {{s004}}), nên ngưỡng điểm số {{s001}} trên thang đã chia nhiệt độ T ứng với `FPR = 1/(1 + 9^T)`.

## Chỗ này phải tự kéo, không xem được (tiếp)
@phut: 1
@che-do: demo

Việc phải làm: kéo T và nhìn ô AUROC đứng yên.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.9` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V reports that temperature scaling improves the detector, giving AUROC {{s042}} after calibration against {{s043}} before. Temperature scaling divides the logits by a positive scalar, which is strictly monotone and therefore cannot change the ranking of any pair of samples. AUROC is a function of that ranking alone. Please explain the reported difference and state precisely what your calibration step changed.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right and the two numbers must be identical. Temperature scaling is strictly monotone, so AUROC is invariant by construction. We traced the discrepancy to our evaluation script, which computed the pre calibration AUROC on the full validation split and the post calibration AUROC on the held out calibration subset. Table V now reports AUROC {{s043}} before and after, on the same split, to four decimals, and we added that identity as an assertion in the evaluation code.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The calibration step changed only the score scale: at {{s008}} bins on {{s044}} test samples, ECE fell from {{s045}} to {{s046}}, against a finite sample floor of {{s047}} for a perfectly calibrated model at the same bin count and sample size. Because the measured value is at that floor, we also report ECE at {{s030}} and at {{s048}} bins, and we added the reliability diagram as Figure {{s049}}. We have likewise restated the threshold claim:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the operating point is now given as a TPR and FPR pair rather than as a score value, since the score value is not comparable across calibration maps.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: nói rằng khác biệt {{s041}} nằm trong nhiễu nên không quan trọng. Đúng về cỡ, nhưng vẫn khai một con số không thể xảy ra, và phản biện hỏi về CƠ CHẾ chứ không về cỡ.
- Mức {{s006}}: thừa nhận AUROC phải bất biến, rồi sửa bảng cho hai con số bằng nhau, nhưng không nói nguồn của chênh lệch nên không ai biết còn chỗ nào trong bài bị cùng lỗi đó.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: thừa nhận bất biến, truy ra nguồn thật của chênh lệch, ví dụ hai số đo trên hai lần chia tập khác nhau hoặc cách xử lý điểm số bằng nhau khác nhau sau khi làm tròn, rồi sửa bảng và khai lại rằng phép hiệu chỉnh chỉ đổi hiệu chuẩn.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

You report an ECE of {{s046}} and conclude that the detector outputs usable probabilities, which Section VI then uses to set the alarm threshold from the cost ratio. ECE is a binned estimator and the manuscript does not state the bin count, the binning scheme, or the size of the split it was measured on. In addition, the threshold argument needs calibration under the deployment distribution, not under the evaluation distribution. Please report the missing quantities and justify the threshold transfer.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We now report calibration fully. ECE is measured with {{s008}} equal mass bins on the {{s044}} sample test split, with the temperature fitted on a disjoint {{s050}} sample calibration split, and Table VI adds the values at {{s030}} and {{s048}} bins. For a perfectly calibrated reference at the same bin count and sample size, the expected ECE floor is {{s047}}, so we report our value against that floor rather than against zero, and Figure {{s049}} gives the reliability diagram.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

On the threshold argument, the reviewer is correct that the Bayes threshold at the cost ratio, {{s004}} over {{s051}} for our {{s020}} to {{s004}} costs, applies to a posterior probability, not to a raw score, and only under the distribution the calibration was fitted on. Section VI now gives both routes. Route one assumes calibration transfers and is stated as conditional, with a recalibration schedule for deployment.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Route two makes no calibration assumption and selects the operating point by scanning the ROC curve at three stated class priors. The main result is reported on route two, so the headline number does not depend on calibration transfer.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: thêm số ô vào bản thảo và coi như xong. Trả lời một nửa câu hỏi, bỏ hẳn phần chuyển ngưỡng sang phân bố triển khai.
- Mức {{s006}}: thêm số ô, số mẫu và cách chia ô, nhưng vẫn lập luận ngưỡng từ ECE đo trên tập đánh giá, tức vẫn giả định ngầm hai phân bố giống nhau.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: thêm đủ số ô, số mẫu, cách chia ô, cộng sàn do mẫu hữu hạn tính ở chính n đó, rồi khai thẳng rằng việc chuyển ngưỡng cần hiệu chuẩn trên phân bố triển khai và báo cách hiệu chuẩn lại tại nơi triển khai.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.9` bấm thẻ.
