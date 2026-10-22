---
tieu-de: Giải thích được, và độ ổn định của lời giải thích
phu-de: Trụ 1 NID · module 1.7
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 76.5
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

Nếu tôi chạy lại với hạt khác, {{s001}} đặc trưng quan trọng nhất có còn là {{s001}} cái đó không, và nếu không thì lời giải thích của tôi là gì?

## Giải thích được, và độ ổn định của lời giải thích
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Hình SHAP đẹp nhất trong bài báo thường là hình chưa ai chạy lại. Đổi hạt, huấn luyện lại, vẽ lại: nếu bảy trong mười đặc trưng đầu đổi chỗ thì cái hình kia là một mẫu từ một phân bố, không phải một phát hiện.

## Giải thích được, và độ ổn định của lời giải thích (tiếp)
@phut: 1
@che-do: noi

Module này đòi ba thứ nói được mà không tra. Một: giá trị Shapley (Shapley value) phụ thuộc vào cách chọn nghĩa của **vắng mặt** một đặc trưng, nên hai cài đặt khác nhau cho hai bộ `φ` khác nhau trên cùng một mô hình, và bài báo phải khai mình chọn cách nào. Hai: khi đặc trưng tương quan cao thì công không chia tách được, nên câu *đặc trưng X là nguyên nhân* mất nghĩa, chỉ còn nói được về nhóm. Ba:

## Giải thích được, và độ ổn định của lời giải thích (tiếp)
@phut: 1
@che-do: noi

attribution không phải nhân quả, và chỗ này đổ ngay cả khi mọi giả thiết còn bật.

Và một thứ nữa, rẻ nhưng ít ai làm: báo **độ ổn định (stability) top-k qua các hạt** bằng một con số, rồi chọn `k` theo con số đó chứ không chọn `k` = {{s001}} vì nó tròn.

## Giá trị Shapley
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Giá trị Shapley · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`φ_i = Σ_{S ⊆ F\{i}} ( |S|!·(|F|−|S|−1)! / |F|! )·[ f(S ∪ {i}) − f(S) ]`

Tổng chạy trên mọi tập con `S` không chứa `i`. Bốn tiên đề (hiệu quả, đối xứng, giả thể, cộng tính) xác định `φ` duy nhất, nên **phần toán học không có chỗ cho lựa chọn**.

## Giá trị Shapley · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** chỗ có lựa chọn là `f(S)`.
Mô hình nhận đủ `|F|` đầu vào, nên phải định nghĩa thế nào là mô hình chỉ thấy `S`.
Lấy kỳ vọng biên, lấy kỳ vọng có điều kiện, thay bằng một giá trị nền, lấy trung bình trên một tập nền:
bốn cách này cho bốn bộ `φ` khác nhau trên cùng một mô hình.

## Giá trị Shapley · đáp (tiếp)
@phut: 1
@che-do: noi

Nên câu *chúng tôi dùng SHAP* chưa xác định được phép đo; phải khai thêm cách vắng mặt và tập nền.

## Độ ổn định top-k, đo bằng Jaccard
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Độ ổn định top-k, đo bằng Jaccard · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Hai lần chạy cho hai tập `A` và `B` gồm `k` đặc trưng đầu. Chỉ số Jaccard là `J = |A ∩ B| / |A ∪ B|`, và vì hai tập cùng cỡ `k` nên `|A ∪ B| = 2k − |A ∩ B|`, tức `J = I / (2k − I)` với `I = |A ∩ B|`.

## Độ ổn định top-k, đo bằng Jaccard · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** `J` phạt nặng hơn nhiều so với trực giác. Trùng {{s003}} trên {{s001}} nghe như {{s004}}, nhưng `J = {{s005}}`, tức khoảng {{s006}}. Lý do: hợp của hai tập là {{s007}} phần tử, không phải {{s001}}. Nên một bài báo khai *trùng {{s003}} trên {{s001}}* và một bài khai *Jaccard {{s006}}* đang nói cùng một chuyện, và con số thứ hai mới là con số so được giữa các `k` khác nhau.

## Attribution không phải nhân quả
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Attribution không phải nhân quả · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`φ_i` trả lời: trong mô hình NÀY, đặc trưng `i` góp bao nhiêu vào việc lệch dự đoán khỏi giá trị nền. Nó là một phát biểu về **mô hình**, không phải về **thế giới**.

## Attribution không phải nhân quả · đáp (tiếp)
@phut: 1
@che-do: noi

Hai hệ quả dùng được ngay trong phản biện: Một đặc trưng rò rỉ nhãn sẽ có `φ` rất lớn, và đó là bằng chứng rò rỉ, không phải bằng chứng cơ chế. Hình SHAP đẹp cho một mô hình đang học đúng cái rò rỉ ở module {{s009}} là hình đẹp nhất mà cũng vô dụng nhất. Can thiệp vào đặc trưng có `φ` lớn không bảo đảm đổi được kết quả thật, vì mô hình không phải thế giới.

## Attribution không phải nhân quả · đáp (tiếp)
@phut: 1
@che-do: noi

Muốn nói nhân quả thì phải có can thiệp hoặc một đồ thị nhân quả đã khai, không phải một bảng attribution. **Điểm phải nhớ:** đây là tuyên bố đổ ngay cả khi mọi giả thiết của SHAP đều đúng. Nó không phải một giả thiết bị tắt, nó là một bước suy luận không có.

## Giá trị Shapley, Jaccard top-k, và chi phí TreeSHAP
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`φ_i = Σ_{S ⊆ F\{i}} ( |S|!·(|F|−|S|−1)! / |F|! )·[ f(S ∪ {i}) − f(S) ] · J = |A ∩ B| / |A ∪ B| = I / (2k − I) · chi phí TreeSHAP bậc O(T·L·D²)`

**Giả thiết nó đứng trên:**

## Giá trị Shapley, Jaccard top-k, và chi phí (tiếp)
@phut: 1
@che-do: so

- Hàm giá trị f(S) định nghĩa được khi thiếu đặc trưng, tức phải CHỌN nghĩa của vắng mặt: kỳ vọng biên, kỳ vọng có điều kiện, một giá trị nền, hay trung bình trên một tập nền. Chọn khác nhau cho φ khác nhau trên cùng một mô hình
- Tập nền dùng để lấy kỳ vọng phải khai rõ; đổi tập nền là đổi φ, kể cả khi mô hình không đổi

## Giá trị Shapley, Jaccard top-k, và chi phí (tiếp)
@phut: 1
@che-do: so

- Với Jaccard: hai tập A và B cùng cỡ k, và dùng tập không thứ tự, tức bỏ hẳn thông tin thứ hạng bên trong top-k
- Với công thức Shapley: tổng chạy trên 2^(|F|−1) tập con, nên tính chính xác chỉ khả thi ở |F| nhỏ; mọi cài đặt trên dữ liệu bảng (tabular data) thật đều là xấp xỉ hoặc là thuật toán riêng cho một họ mô hình

## Giá trị Shapley, Jaccard top-k, và chi phí (tiếp)
@phut: 1
@che-do: so

- Với TreeSHAP: mô hình là tập hợp cây, T cây với L lá và độ sâu D; bậc O(T·L·D²) không áp cho mô hình ngoài họ cây

## Giá trị Shapley, Jaccard top-k, và chi phí TreeSHAP ·
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hai tính chất kiểm được ngay. Thứ nhất, tiên đề hiệu quả: `Σ_i φ_i = f(F) − f(∅)`, dùng để bắt lỗi cài đặt vì nó phải đúng tới sai số máy. Thứ hai, với `J`: nếu `k` nhỏ hơn hoặc bằng số đặc trưng lõi thì `J = {{s010}}`, và nếu `k` bằng tổng số đặc trưng thì cũng `J = {{s010}}`, nên `J` theo `k` là một đường đi xuống rồi đi lên chứ không đơn điệu.

## Giá trị Shapley, Jaccard top-k, và chi phí (tiếp)
@phut: 0.5
@che-do: noi

Một bài báo chọn `k` rồi khai `J` cao mà không vẽ cả đường là đang báo một điểm trên một đường có hai nhánh.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s011}} | số mũ | Chi phí TreeSHAP có bậc O(T·L·D^x) với T cây
!so {{s012}} | tập con | Mô hình có |F| = {{s013}} đặc trưng. Để tính CHÍNH XÁC

## Một rừng gradient boosting có 100 cây
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một rừng gradient boosting có {{s014}} cây, mỗi cây {{s015}} lá và độ sâu {{s003}}. Theo bậc O(T·L·D²), số đơn vị công việc để giải thích MỘT mẫu bằng TreeSHAP là bao nhiêu?

t = {{s014}}, l = {{s015}}, dd = {{s003}}

## Một rừng gradient boosting có 100 cây · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`t⋆l⋆Math.pow(dd,2)`

{{s016}} đơn vị công việc cho MỘT mẫu. Chỗ phải đọc ra: nhân với số mẫu cần giải thích thì con số nổ rất nhanh. Giải thích {{s017}} mẫu của tập kiểm là bậc {{s018}} tỉ đơn vị, nên phần giải thích của bài báo thường đắt hơn phần huấn luyện. Và nếu muốn đo độ ổn định top-k qua {{s013}} hạt thì nhân thêm {{s013}} lần nữa; đó là lý do thật mà nhiều bài bỏ phép đo độ ổn định:

## Một rừng gradient boosting có 100 cây · đáp (tiếp)
@phut: 1
@che-do: noi

nó đắt, không phải vì nó khó.

## Hai lần chạy
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai lần chạy, mỗi lần báo top {{s001}} đặc trưng, và {{s003}} đặc trưng xuất hiện ở cả hai lần. Chỉ số Jaccard bằng bao nhiêu?

i = {{s003}}, k = {{s001}}

## Hai lần chạy · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`i/(2⋆k-i)`

Khoảng {{s019}}, tức đúng phân số {{s005}}. Đây là chỗ trực giác lệch: trùng {{s003}} trên {{s001}} nghe như {{s004}}, mà Jaccard chỉ khoảng {{s006}}, vì mẫu số là HỢP của hai tập, tức {{s007}} đặc trưng, không phải {{s001}}. Hệ quả thực hành:

## Hai lần chạy · đáp (tiếp)
@phut: 1
@che-do: noi

khi phản biện đòi con số độ ổn định thì báo Jaccard kèm cả k và tổng số đặc trưng, vì tỉ lệ trùng trên k phụ thuộc k theo cách khác và không so được giữa hai bài dùng k khác nhau.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai bài báo dùng cùng mô hình gradient boosting đã huấn luyện, cùng mã SHAP, mà cho hai hình attribution khác nhau. Lời giải thích hợp lý nhất là gì?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Một trong hai bài có lỗi cài đặt, vì giá trị Shapley là duy nhất
- Hai bài chọn nghĩa của vắng mặt hoặc tập nền khác nhau, nên chúng tính hai hàm giá trị f(S) khác nhau và cả hai đều đúng
- Một trong hai bài không chuẩn hoá đặc trưng (feature normalisation)
- Hiệu ứng của hạt ngẫu nhiên khi vẽ hình

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hai bài chọn nghĩa của vắng mặt hoặc tập nền khác nhau, nên chúng tính hai hàm giá trị f(S) khác nhau và cả hai đều đúng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Bốn tiên đề xác định φ duy nhất KHI ĐÃ CÓ hàm giá trị f(S). Nhưng f(S) không có sẵn: mô hình đòi đủ đầu vào, nên phải chọn nghĩa của vắng mặt, và kỳ vọng biên với kỳ vọng có điều kiện cho hai bộ φ khác nhau trên cùng một mô hình. Đáp án thứ nhất nhầm tính duy nhất của φ với tính duy nhất của f.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Đáp án thứ tư sai vì mô hình đã huấn luyện xong, không còn hạt nào trong bước giải thích nếu f(S) tính chính xác.

## Trên dữ liệu bảng của IDS
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trên dữ liệu bảng của IDS, phép đo nào cho biết bảng top-10 đặc trưng của anh có đáng tin hay không, và rẻ nhất để thêm vào bài?

- Độ chính xác của mô hình trên tập kiểm
- Jaccard trung bình của top-k qua nhiều hạt, báo kèm k và tổng số đặc trưng, cộng đường Jaccard theo k
- Thời gian tính SHAP cho toàn tập kiểm
- Tổng công của mọi đặc trưng, so với f(F) trừ f(∅)

## Trên dữ liệu bảng của IDS · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Jaccard trung bình của top-k qua nhiều hạt, báo kèm k và tổng số đặc trưng, cộng đường Jaccard theo k**

## Trên dữ liệu bảng của IDS · đáp (tiếp)
@phut: 1
@che-do: noi

Đáp án thứ tư là một phép kiểm cài đặt rất nên có, nhưng nó chỉ chứng minh mã chạy đúng tiên đề hiệu quả, tức nó là kiểm nội bộ và không nói gì về độ ổn định. Đáp án thứ nhất và thứ ba đo hai thứ khác. Chỉ Jaccard qua các hạt đo đúng điều mà phản biện đang hỏi, và nó đòi đúng một thứ: chạy lại vài lần rồi so tập, nên nó rẻ.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phân tích giải thích sau có một câu không đứng được. Bấm vào câu đó.

- Hình {{s020}} cho thấy cổng đích chiếm {{s021}} tổng công SHAP, cao hơn hẳn mọi đặc trưng khác.
- Điều này xác nhận cơ chế mà chúng tôi đề xuất: dịch vụ đích là tín hiệu phân biệt chính của họ tấn công này.
- Chúng tôi lặp lại phân tích trên {{s013}} hạt và báo Jaccard trung bình của top-10 kèm độ phân tán.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Vì nhóm đặc trưng byte có tương quan cao, chúng tôi gộp chúng và báo công ở mức nhóm.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Điều này xác nhận cơ chế mà chúng tôi đề xuất: dịch vụ đích là tín hiệu phân biệt chính của họ tấn công này.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Một đặc trưng đơn lẻ chiếm phần công áp đảo là DẤU HIỆU RÒ RỈ, không phải bằng chứng cơ chế. Trong CIC-IDS2017, cổng đích trùng khít với cách sinh từng họ tấn công, nên mô hình học được bảng tra chứ không học hành vi. Phép kiểm đúng và rẻ là thông tin tương hỗ một biến giữa cổng đích và nhãn: nếu nó gần entropy của nhãn thì đặc trưng đó mã hoá gần hết nhãn. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

chạy lại mô hình khi bỏ nhóm đặc trưng nghi rò rỉ, báo cả hai con số, và chỉ viết câu về cơ chế nếu mô hình không rò rỉ vẫn giữ được hiệu năng. Câu đầu và hai câu cuối đều hợp lệ.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn trả lời phản biện sau có một câu không đứng được. Bấm vào câu đó.

- Chúng tôi đã thêm phép đo độ ổn định: Jaccard trung bình của top-10 qua {{s013}} hạt là {{s022}}.
- Vì con số này thấp, chúng tôi hạ xuống báo top-3, nơi Jaccard đạt {{s023}}, và khai cả đường Jaccard theo k.
- Chúng tôi cũng gộp các đặc trưng tương quan trên {{s024}} thành nhóm và báo công ở mức nhóm.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Vì giá trị Shapley là duy nhất theo bốn tiên đề, kết quả của chúng tôi so sánh được trực tiếp với attribution báo trong các bài trước.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì giá trị Shapley là duy nhất theo bốn tiên đề, kết quả của chúng tôi so sánh được trực tiếp với attribution báo trong các bài trước.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Tính duy nhất của φ chỉ đúng KHI ĐÃ CỐ ĐỊNH hàm giá trị f(S). Mà f(S) là lựa chọn của người làm: kỳ vọng biên, kỳ vọng có điều kiện, một giá trị nền, hay trung bình trên một tập nền. Hai bài khác tập nền cho hai bộ φ khác nhau trên cùng một mô hình, và không bài nào sai. Nên câu này so hai thước đo khác nhau. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

khai cách vắng mặt và tập nền của mình, rồi chỉ so với bài nào trùng cả hai, hoặc chạy lại attribution của bài trước dưới cùng lựa chọn. Ba câu trên đều hợp lệ và đều là việc đúng nên làm.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Hai lần chạy cho hai tập A và B, mỗi tập gồm đúng k đặc trưng đầu
- Vì |A| = |B| = k, ta có |A ∪ B| = 2k − |A ∩ B|
- Đặt I = |A ∩ B|, suy ra J = I / (2k − I), tức J chỉ phụ thuộc I và k

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Mô hình lõi: c đặc trưng luôn vào top-k ở mọi lần chạy, còn k − c chỗ trống rút đều từ d − c đặc trưng còn lại
- Kỳ vọng số trùng của phần ngẫu nhiên là (k − c)² chia (d − c), nên I = c + (k − c)² / (d − c)

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Kiểm lại bằng hai trường hợp biên: c = k cho I = k và J = {{s010}}; k = d cho I = d và J = {{s010}}

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Jaccard trung bình {{s025}} · kỳ vọng {{s026}} trên {{s001}} đặc trưng lặp lại · {{s027}} chỗ đổi khi đổi hạt · tỉ lệ chỗ ổn định {{s028}}

- **Đặc trưng độc lập, không tương quan cao theo nhóm** tắt đi: Dữ liệu bảng của IDS có nhiều nhóm gần như trùng nhau: tổng byte và byte trung bình mỗi gói (packet), thời lượng luồng (flow) và khoảng cách gói trung bình, cổng đích và tên dịch vụ.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Hàm giá trị f(S) định nghĩa được khi thiếu đặc trưng** tắt đi: Mô hình đòi đủ |F| đầu vào và không có chế độ đánh dấu thiếu, trong khi tập nền để lấy kỳ vọng không khai được, ví dụ vì mỗi triển khai có phân bố lưu lượng riêng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Tập huấn luyện và hạt cố định giữa các lần chạy** tắt đi: Huấn luyện lại với hạt khác, hoặc hoán vị thứ tự dữ liệu, hoặc lấy mẫu lại tập huấn luyện bằng bootstrap.
- **Đặc trưng có công lớn không rò rỉ nhãn** tắt đi: Một đặc trưng mã hoá gián tiếp nhãn, ví dụ cổng đích trùng khít với họ tấn công trong cách sinh lưu lượng của dataset.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Mô hình lõi cộng phần ngẫu nhiên: c đặc trưng luôn vào top-k, phần còn lại rút đều. Kéo k, cỡ lõi, và tổng số đặc trưng. Tìm k nhỏ nhất mà Jaccard còn trên {{s029}}, rồi tự trả lời: bài báo nên báo top mấy?

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.7` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Figure {{s020}} presents SHAP values from a single training run and the paper draws mechanistic conclusions from the top ten features. Tree ensembles on tabular data are known to produce unstable attributions across seeds, and several of your features are strongly correlated. Please quantify the stability of the ranking and justify reporting ten features rather than some other number.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Section VII has been rewritten around a stability measurement rather than a single run. We retrain with {{s013}} seeds, compute SHAP under a stated absence convention and a stated background set, and report the mean pairwise Jaccard of the top-k sets with its spread.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also plot Jaccard against k, which shows that the ranking is reproducible only up to a small stable core, and we therefore report that core rather than a round ten; the figure now shows the aggregate attribution across seeds with dispersion bars, and the former single-run figure is described as one draw.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Because several features are strongly correlated we group features above a stated correlation threshold and report attribution at the group level, since the split of credit inside a correlated group is determined by the absence convention rather than by the data, so per-feature statements inside a group are not well defined. We separate two sources of variation and report both: fixed training set with varying seed, and bootstrap resampling of the training set, the latter being closer to the deployment setting.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, for every feature that is both high in attribution and highly stable we report single-variable mutual information with the label and the performance of the model retrained without that feature group, because leakage raises stability rather than lowering it and would otherwise hide behind the very measurement we just added.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s010}}: trả lời rằng SHAP có nền tảng lý thuyết vững với bốn tiên đề và giá trị là duy nhất. Đúng về toán, không trả lời được phản bác: tính duy nhất là của φ khi đã cố định f(S), nó không nói gì về độ ổn định của thứ hạng qua các lần huấn luyện.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s011}}: chạy lại với vài hạt và báo rằng thứ hạng nhìn chung ổn định, hoặc báo một con số Jaccard duy nhất ở k bằng {{s001}}. Đã là một phép đo nhưng chưa trả lời vì sao chọn k bằng {{s001}}, và chưa xử lý chuyện đặc trưng tương quan làm các thành viên trong nhóm thay nhau chiếm chỗ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: báo Jaccard trung bình của top-k qua {{s013}} hạt kèm độ phân tán, vẽ đường Jaccard theo k, chọn k theo đường đó chứ không chọn tròn, gộp đặc trưng tương quan trên một ngưỡng đã khai thành nhóm và báo công ở mức nhóm, và khai cách vắng mặt cùng tập nền dùng để tính φ.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The paper states that destination port is the causal driver of the detection decision, based on its SHAP contribution. Attribution is not causal identification. Please either provide an intervention or restate the claim as a statement about the model.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have removed the causal wording. The claim is now stated as a property of the model: under the absence convention and background set given in Section VII-A, the destination port group accounts for the stated share of the deviation of the model output from its baseline value. We also note explicitly that this is a statement about the model, not about the phenomenon. Two interventions are now reported in the scope we can actually run.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

First, we retrain without the destination port group and report the resulting performance, which drops substantially, showing the model depends on it but not why. Second, we build a permuted variant of the evaluation traffic in which destination port is reassigned independently of the attack family and report performance there, which collapses; we interpret this as evidence that the association is a property of how this dataset was generated rather than of operational traffic.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We additionally report single-variable mutual information between destination port and the label alongside the label entropy, so the reader can judge how much of the label this one feature encodes. The discussion now separates what is a property of the dataset from what we claim about the phenomenon, and the mechanistic paragraph has been removed rather than reworded.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s010}}: lập luận rằng SHAP đo đóng góp nên đóng góp lớn nghĩa là nguyên nhân. Đây đúng là chỗ reviewer đang chỉ vào, và nó còn trộn hai nghĩa của chữ nguyên nhân.
- Mức {{s011}}: đổi chữ causal thành important nhưng giữ nguyên đoạn diễn giải cơ chế ở phần thảo luận và trong tóm tắt. Đổi từ mà không đổi tuyên bố, nên mặt tiền vẫn hứa cái cũ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: phát biểu lại thành một câu về mô hình, nói rõ rằng trong mô hình này đặc trưng đó góp bao nhiêu vào việc lệch dự đoán khỏi giá trị nền, kèm cách vắng mặt và tập nền, và bỏ mọi câu suy ra cơ chế của thế giới từ bảng attribution.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.7` bấm thẻ.
