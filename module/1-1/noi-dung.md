---
tieu-de: Đặt bài toán phát hiện
phu-de: Trụ 1 NID · module 1.1
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 68.5
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

Đơn vị quan sát của tôi là gói tin, luồng, cửa sổ thời gian hay đồ thị, và lựa chọn đó làm cho tuyên bố nào của tôi không còn kiểm được?

## Đơn vị quan sát là câu đầu tiên của phần đánh giá
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này không dạy định nghĩa. Nó chỉ làm một việc: buộc mọi con số trong bài vào **một đơn vị quan sát đã khai**. Cùng một bộ phát hiện, cùng một ngưỡng, nếu đơn vị báo động là gói thì FPR là một con số, nếu đơn vị là luồng thì nó là một con số khác, và hai con số đó lệch nhau theo đúng số gói trong luồng.

## Đơn vị quan sát là câu đầu tiên của phần đánh giá (tiếp)
@phut: 1
@che-do: noi

Vì sao đây là chỗ reviewer đánh: một bài khai FPR ở mức gói rồi so với baseline đo ở mức luồng là **so hai thước đo khác nhau**, và không có cách nào sửa bằng cách chạy lại thí nghiệm. Phải khai lại đơn vị, rồi đo lại cả hai bên ở cùng đơn vị.

## Đơn vị quan sát là câu đầu tiên của phần đánh giá (tiếp)
@phut: 1
@che-do: noi

Ba thứ phải dẫn lại được trong {{s001}} giây trên giấy: kiểm định tỉ số hợp lẽ và điều nó đòi, AUC là một xác suất so cặp chứ không phải một điểm làm việc, và bài toán tập mở cần một hàm từ chối với ngưỡng riêng.

## Đơn vị quan sát (observation unit)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Đơn vị quan sát (observation unit) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Thực thể mà bộ phát hiện gán một nhãn và một điểm số cho: gói (packet), luồng (flow), cửa sổ thời gian (time window), hay đồ thị kết nối (connection graph).

## Đơn vị quan sát (observation unit) · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** TPR và FPR không phải thuộc tính của mô hình, chúng là thuộc tính của *cặp* mô hình cộng đơn vị quan sát. Đổi đơn vị mà không đo lại thì mọi con số trong bảng kết quả mất hiệu lực, kể cả khi mã nguồn không đổi một dòng nào.

## Bổ đề Neyman-Pearson, và nó đòi những gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Bổ đề Neyman-Pearson, và nó đòi những gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Với mức FPR cho trước là `α`, phép kiểm cực đại hoá TPR là phép kiểm theo tỉ số hợp lẽ: báo động khi `Λ(x) = p(x | tấn công) / p(x | bình thường) ≥ τ`.

## Bổ đề Neyman-Pearson, và nó đòi những gì · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** tính tối ưu này là tối ưu *có điều kiện biết cả hai phân bố*. Một mạng neural không ước lượng `Λ`, nó ước lượng một hàm điểm nào đó trong họ mô hình đã chọn, nên câu đúng để viết trong bài là tối ưu trong họ, không phải tối ưu Neyman-Pearson.

## AUC bằng thống kê Mann-Whitney U
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## AUC bằng thống kê Mann-Whitney U · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`AUC = P(điểm của một mẫu dương lấy ngẫu nhiên > điểm của một mẫu âm lấy ngẫu nhiên)`, bằng `U / (n₊ · n₋)` với `U` là thống kê Mann-Whitney.

## AUC bằng thống kê Mann-Whitney U · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** AUC là một xác suất so cặp, nó **không phụ thuộc tỉ lệ nền** và **không ứng với một điểm làm việc nào**. Chính vì thế AUC {{s004}} không nói được một cảnh báo có đáng đọc hay không, và cũng vì thế nó là con số dễ gây hiểu nhầm nhất trong trụ này.

## Tập mở (open-set) và hàm từ chối
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Tập mở (open-set) và hàm từ chối · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bài toán tập mở: `f(x) ∈ {c₁, …, c_K} ∪ {không biết}`. Cần một hàm từ chối với **ngưỡng riêng**, độc lập với ngưỡng phân lớp giữa K lớp đã biết.

**Điểm phải nhớ:** nếu dữ liệu đánh giá chỉ chứa K lớp đã có nhãn thì hàm từ chối *không bao giờ được kiểm*. Một bài khai mình giải bài toán tập mở nhưng đánh giá trên tập đóng là bài chưa đo thứ nó khai, bất kể độ chính xác bao nhiêu.

## Kiểm định tỉ số hợp lẽ, và bốn giả thiết của nó
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Báo động khi Λ(x) = p(x | tấn công) / p(x | bình thường) ≥ τ`

**Giả thiết nó đứng trên:**

## Kiểm định tỉ số hợp lẽ, và bốn giả thiết của nó (tiếp)
@phut: 1
@che-do: so

- biết cả hai phân bố điều kiện p(x | tấn công) và p(x | bình thường)
- chi phí của hai loại lỗi cố định, nên tỉ số chi phí chọn được một τ duy nhất
- một ngưỡng duy nhất, áp cho mọi mẫu và mọi thời điểm
- đơn vị quan sát x cố định, cùng một x cho cả bộ phát hiện và cho baseline

## Kiểm định tỉ số hợp lẽ, và bốn giả thiết của nó · ghi
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Quan hệ giữa τ và chi phí: nếu chi phí bỏ sót là `c₁₀`, chi phí báo động sai là `c₀₁` và tỉ lệ nền là `p`, thì ngưỡng Bayes là `τ = c₀₁(1 − p) / (c₁₀ p)`. Hai thứ τ phụ thuộc vào đều **không nằm trong dữ liệu**, chúng do bên vận hành cung cấp.

## AUC là một xác suất so cặp
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`AUC = P(s(x₊) > s(x₋)) = U / (n₊ · n₋)`

**Giả thiết nó đứng trên:**

- không có hoà điểm, hoặc hoà điểm được tính một nửa
- mọi mẫu dùng cùng một hàm điểm s và cùng một thang điểm
- hai mẫu lấy độc lập từ hai phân bố điều kiện, nên tỉ lệ nền không vào công thức

## AUC là một xác suất so cặp · ghi chú
@phut: 1
@che-do: noi

Bài toán tập mở viết là `f(x) ∈ {c₁, …, c_K} ∪ {không biết}`, cần một hàm từ chối với ngưỡng riêng. AUC tính trên K lớp đã biết **không chấm** hàm từ chối, nên hai con số này không thay thế nhau được.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} | triệu gói mỗi giây | Liên kết {{s007}} Gbps
!so {{s008}} | nano giây | Cùng liên kết {{s007}} Gbps và khung {{s009}} byte. Ngân sách thời
!so {{s010}} | byte | Trên Ethernet, mỗi khung còn kéo theo bao nhiêu byte phí nằm

## Liên kết 10 Gbps
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Liên kết {{s007}} Gbps, khung {{s009}} byte, phí ngoài khung {{s010}} byte. Tốc độ gói tối đa là bao nhiêu gói mỗi giây?

bit = {{s011}}, khung = {{s009}}, phi = {{s010}}

## Liên kết 10 Gbps · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`bit / ((khung + phi) × {{s012}})`

Khoảng {{s013}} triệu gói mỗi giây, phân số đúng là {{s014}}. Nghịch đảo của nó là {{s015}} nano giây cho mỗi gói. Đó là lý do mọi bộ phát hiện đặt ở mức gói đều phải là mô hình nhỏ hoặc phần cứng: {{s016}} nano giây không đủ cho một lượt suy diễn mạng neural trên CPU.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

FPR mức gói là 10⁻⁴. Gộp {{s010}} gói thành một luồng theo luật báo động nếu có ít nhất một gói vượt ngưỡng. FPR mức luồng là bao nhiêu phần trăm?

f = {{s017}}, n = {{s010}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s018}} × ({{s002}} - Math.pow(1 - f, n))`

Khoảng {{s019}}, trong khi FPR mức gói là {{s020}}. Con số mức luồng lớn hơn khoảng {{s021}} lần, tức gần đúng bằng n lần. Hệ quả cho bài báo: nếu bảng của anh khai FPR 10⁻⁴ ở mức gói mà baseline khai FPR ở mức luồng, thì anh đang so với một con số bị quy đổi lệch gần {{s010}} lần, và không có cách nào sửa bằng cách huấn luyện lại.

## Cùng một mô hình
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cùng một mô hình, cùng một ngưỡng. Đổi đơn vị báo động từ gói sang luồng gộp {{s010}} gói theo luật OR. Đại lượng nào KHÔNG đổi?

- AUC tính trên điểm mức gói
- Số cảnh báo sai mỗi ngày
- Cả FPR và TPR, vì cả hai tính trong từng lớp
- FPR, vì nó là tỉ lệ nên không phụ thuộc cách gộp

## Cùng một mô hình · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**AUC tính trên điểm mức gói**

## Cùng một mô hình · đáp (tiếp)
@phut: 1
@che-do: noi

AUC mức gói là xác suất so cặp giữa hai mẫu gói, nó là thuộc tính của hàm điểm trên đơn vị gói, nên luật gộp ở tầng trên không chạm vào. FPR và TPR đều đổi vì luật gộp đổi: FPR mức luồng = {{s002}} − ({{s002}} − FPR gói)^20. Số cảnh báo mỗi ngày đổi theo cả FPR mới lẫn số luồng mỗi ngày. Lưu ý thêm: AUC mức luồng là một con số KHÁC, phải tính lại trên điểm mức luồng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai mình giải bài toán phát hiện tập mở và báo macro F1 {{s022}} trên {{s023}} họ tấn công của UNSW-NB15. Thiếu đúng một thứ để kiểm câu khai tập mở. Thứ gì?

- Một bảng so sánh thời gian suy diễn
- Thêm vài kiến trúc baseline nữa
- Khai tỉ lệ nền của tập đánh giá
- Một tập mẫu thuộc lớp chưa từng thấy lúc huấn luyện, cộng ngưỡng của hàm từ chối

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Một tập mẫu thuộc lớp chưa từng thấy lúc huấn luyện, cộng ngưỡng của hàm từ chối**

Macro F1 trên {{s023}} họ đã có nhãn chỉ chấm phần phân lớp tập đóng. Hàm từ chối chỉ được chấm khi có mẫu không thuộc {{s023}} họ đó, và chỉ so được khi ngưỡng từ chối được khai riêng. Khai tỉ lệ nền là việc cần cho precision, nhưng nó không cứu được chuyện hàm từ chối chưa bao giờ bị thử.

## FPR mức gói là 10⁻⁵
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

FPR mức gói là 10⁻⁵, luồng gộp {{s024}} gói theo luật OR. Cách ước FPR mức luồng nào vừa nhanh vừa an toàn khi trả lời phản biện tại chỗ?

- Lấy {{s024}} · 10⁻⁵ = 2·10⁻³, và nói rõ đây là chặn trên
- Lấy 10⁻⁵ chia {{s024}}, vì gộp làm giảm cảnh báo
- Không ước được nếu chưa chạy lại thí nghiệm
- Giữ nguyên 10⁻⁵, vì tỉ lệ không đổi khi gộp

## FPR mức gói là 10⁻⁵ · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Lấy {{s024}} · 10⁻⁵ = 2·10⁻³, và nói rõ đây là chặn trên**

## FPR mức gói là 10⁻⁵ · đáp (tiếp)
@phut: 1
@che-do: noi

Bất đẳng thức Bernoulli cho {{s002}} − ({{s002}} − f)^N ≤ N·f, nên N·f luôn là chặn trên, và nó rất sát khi N·f nhỏ: giá trị đúng ở đây là 1,998·10⁻³ so với chặn trên 2·10⁻³, lệch khoảng một phần nghìn. Nói rõ đây là chặn trên thì câu trả lời vừa nhanh vừa không nói quá. Gộp theo luật OR làm FPR mức luồng TĂNG, không giảm, nên phương án chia là sai dấu.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết luận sau có một câu không được chống đỡ bởi bất cứ số nào trong bài. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Mô hình đề xuất đạt AUC {{s025}} trên tập kiểm tra, cao hơn baseline mạnh nhất {{s026}}.
- Đường ROC của mô hình nằm trên đường của mọi baseline ở mọi ngưỡng.
- AUC {{s025}} cho thấy mô hình đã sẵn sàng triển khai trong một trung tâm điều hành an ninh.
- Thời gian suy diễn trung bình là {{s027}} mili giây mỗi luồng trên một GPU RTX {{s028}}.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**AUC {{s025}} cho thấy mô hình đã sẵn sàng triển khai trong một trung tâm điều hành an ninh.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu trước là phát biểu về AUC và về ROC, cả hai đều kiểm được từ dữ liệu. Câu này nhảy từ một xác suất so cặp sang một kết luận vận hành, mà AUC thì không ứng với điểm làm việc nào và không nhìn tỉ lệ nền, nên không có đường nào đi từ {{s025}} tới chữ sẵn sàng triển khai. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

chọn một điểm làm việc, khai TPR và FPR tại đó, khai lưu lượng và đơn vị báo động, rồi quy ra số cảnh báo mỗi ngày và so với ngân sách người đọc.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết lập thực nghiệm sau có một chỗ làm phần so sánh mất hiệu lực. Bấm vào chỗ đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Mô hình của chúng tôi chấm điểm từng gói, và một luồng được báo động nếu có ít nhất một gói vượt ngưỡng.
- Chúng tôi báo FPR của mô hình ở mức gói để so sánh được với tài liệu về phát hiện mức gói.
- Ba baseline được dùng theo cài đặt gốc của chúng, tức chấm điểm ở mức luồng, và FPR của chúng lấy nguyên từ bài gốc.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Mọi phương pháp dùng cùng một lần chia dữ liệu và cùng một hạt giống ngẫu nhiên.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Ba baseline được dùng theo cài đặt gốc của chúng, tức chấm điểm ở mức luồng, và FPR của chúng lấy nguyên từ bài gốc.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu trước đều hợp lệ nếu đứng riêng: khai luật gộp, và khai rằng FPR của mình ở mức gói. Câu này đặt FPR mức gói của mình cạnh FPR mức luồng của baseline, hai con số lệch nhau tới n lần vì {{s002}} − ({{s002}} − f)^n ≤ n·f. Với n khoảng {{s010}} thì phần so sánh đang cho mình lợi gần {{s010}} lần, và đây là lỗi không sửa được bằng cách huấn luyện lại. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

gộp điểm của mô hình mình về mức luồng rồi đo lại FPR ở đó, hoặc lấy điểm mức luồng của baseline tách về mức gói, và nói rõ đơn vị trong mọi dòng của bảng.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt đơn vị báo động là luồng gồm N gói, bộ phát hiện chấm từng gói riêng rẽ
- Một luồng lành bị gắn cờ khi có ít nhất một gói của nó vượt ngưỡng
- Xác suất một gói lành không vượt ngưỡng là {{s002}} − f
- Xác suất cả N gói đều không vượt ngưỡng là ({{s002}} − f)^N
- FPR mức luồng = {{s002}} − ({{s002}} − f)^N

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Khi N·f ≪ {{s002}} thì FPR mức luồng ≈ N·f, và luôn có FPR mức luồng ≤ N·f

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Một ngưỡng τ duy nhất trên Λ(x) · TPR mức luồng {{s029}} và FPR mức luồng {{s030}} khi gộp {{s010}} gói · AUC {{s031}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biết cả hai phân bố p(x | tấn công) và p(x | bình thường)** tắt đi: Chỉ có một hàm điểm học từ dữ liệu, trong một họ mô hình đã chọn trước.
- **Chi phí hai loại lỗi cố định** tắt đi: Chi phí bỏ sót và chi phí báo động sai phụ thuộc bối cảnh: giờ cao điểm, loại tài sản bị nhắm, giai đoạn của chiến dịch tấn công.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Một ngưỡng duy nhất, áp cho mọi đơn vị quan sát** tắt đi: Gói được gộp thành luồng hoặc cửa sổ trước khi báo động, nên có một luật gộp nằm giữa ngưỡng và cảnh báo.
- **Tập nhãn đóng, mọi mẫu thuộc một trong K lớp đã biết** tắt đi: Bài toán thật là tập mở: có họ tấn công chưa từng thấy, và có lưu lượng lành chưa từng thấy.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Một bộ phát hiện duy nhất, một ngưỡng duy nhất. Kéo số gói trong luồng và xem cùng một mô hình sinh ra hai bảng kết quả khác nhau, chỉ vì đơn vị báo động khác nhau.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.1` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV reports a false positive rate of 1e-4 and claims this is acceptable for operational deployment. However, Section III states that the detector scores individual packets, while the baselines in Table V operate on flows. Under the stated OR aggregation rule, a per packet FPR of 1e-4 over flows of about {{s010}} packets corresponds to a flow level FPR close to 2e-3, which is an order of magnitude above the figure you compare against.

## Phản biện hỏi (tiếp)
@phut: 1
@che-do: hoi

Please state the observation unit for every number in Table V, and justify the deployability claim at the unit the operators actually see.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is correct and we have reworked Table V so that every row carries its observation unit. Our detector scores packets, and flow level decisions use the OR rule stated in Section III, so the correct conversion is FPR_flow = {{s002}} - ({{s002}} - FPR_packet)^N, with the Bernoulli bound FPR_flow <= N × FPR_packet. At N = {{s010}} and FPR_packet = 1e-4 this gives FPR_flow = 1.998e-3, within one part in a thousand of the 2e-3 the reviewer quotes.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table V now reports both units for our method and for the three baselines, with the per packet columns marked as not comparable across rows. Two consequences are now stated explicitly. First, aggregation also raises the true positive rate: at a per packet TPR of {{s032}} and five malicious packets per attack flow, flow level TPR is {{s033}} percent, so the honest comparison is the pair ({{s033}} percent, 1.998e-3) against the baseline pair, not a one sided FPR comparison.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Second, at the traffic volume of Section II, FPR_flow = 1.998e-3 implies about {{s034}} false alerts per day per million benign flows, and we have replaced the phrase acceptable for operational deployment with that number plus the alert budget it has to fit into.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng FPR là một tỉ lệ nên không phụ thuộc cách gộp. Sai thẳng, và reviewer đã đưa sẵn công thức phản bác.
- Mức {{s003}}: nhận là hai đơn vị khác nhau, thêm một câu khai đơn vị vào chú thích bảng, nhưng vẫn giữ nguyên con số và giữ nguyên phần so sánh.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s005}}: đo lại điểm của mô hình mình ở mức luồng, báo lại cả TPR và FPR ở mức luồng cạnh baseline, khai luật gộp và số gói mỗi luồng, và sửa câu kết luận về khả năng triển khai cho khớp con số mới.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.1` bấm thẻ.
