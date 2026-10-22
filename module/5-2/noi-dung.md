---
tieu-de: Lattice: bài toán khó và cách ước lượng độ an toàn
phu-de: Trụ 5 PQC · module 5.2
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 76
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: PQC
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Câu an toàn {{s001}} bit của một bộ tham số lattice nghĩa là gì, và tính trong mô hình chi phí nào?

## Con số bit an toàn là con số của một mô hình
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Khi một bài viết bộ tham số này an toàn {{s001}} bit, con số {{s001}} không đo hệ. Nó là đầu ra của một chuỗi: chọn tấn công tốt nhất đã biết, chọn mô hình chi phí cho tấn công đó, chạy bộ ước lượng để ra kích thước khối BKZ cần thiết, rồi nhân số mũ. Đổi một khâu trong chuỗi là đổi con số.

## Con số bit an toàn là con số của một mô hình (tiếp)
@phut: 1
@che-do: noi

Hai điểm phải mang theo. Thứ nhất, **mô hình core-SVP bỏ hết hệ số đa thức**, nên nó là chặn dưới lạc quan cho kẻ tấn công, tức bảo thủ cho người thiết kế; phải nói được chiều này. Thứ hai, **nhiễu trong LWE là thứ làm bài toán khó**, không phải nhược điểm kỹ thuật cần giảm. Nhiễu bằng {{s002}} thì khử Gauss ra ngay bí mật.

## LWE và phiên bản module MLWE
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s003}} trên bốn.*

## LWE và phiên bản module MLWE · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

LWE: cho `(A, b = A·s + e mod q)` với `e` nhỏ, tìm `s`. MLWE thay vô hướng bằng phần tử của một vành đa thức, nên cùng một mức an toàn cần ít byte khoá hơn nhiều.

## LWE và phiên bản module MLWE · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: dùng cấu trúc vành là một **cuộc đổi**, an toàn lấy kích thước. Bài báo phải nói cả hai mặt. Nói mặt khoá nhỏ mà không nói mặt giả định không có tấn công khai thác cấu trúc vành là khai thiếu một giả thiết.

## Nhiễu làm bài toán khó, không làm nó dễ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Nhiễu làm bài toán khó, không làm nó dễ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Không có `e`, hệ `b = A·s mod q` giải được bằng khử Gauss trong thời gian đa thức. Chính `e` biến một bài toán đại số thành bài toán khoảng cách trên lưới, và bài toán khoảng cách mới là bài toán khó.

## Nhiễu làm bài toán khó, không làm nó dễ · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đại lượng quyết định độ khó là **tỉ số độ lớn nhiễu trên q**, không phải độ lớn nhiễu một mình. Nhiễu quá nhỏ so với `q` thì hệ yếu; nhiễu quá lớn thì giải mã sai. Ngân sách nhiễu là chỗ đánh đổi, nên câu giảm nhiễu để an toàn hơn là câu ngược chiều.

## β, kích thước khối BKZ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## β, kích thước khối BKZ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Thu gọn cơ sở lưới làm cơ sở tốt lên, và cơ sở tốt làm bài toán tìm điểm lưới gần nhất dễ. LLL rồi BKZ là hai bậc của việc đó. `β` là kích thước khối mà BKZ cần để thu gọn đủ sâu nhằm giải được bộ tham số đang xét.

## β, kích thước khối BKZ · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: `β` không phải tham số của hệ, nó là **đầu ra của một bộ ước lượng** trên bộ tham số của hệ. Nên con số bit an toàn kế thừa toàn bộ độ bất định của bộ ước lượng đó, kể cả phiên bản của nó.

## Chiều của sự bảo thủ trong core-SVP
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Chiều của sự bảo thủ trong core-SVP · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Core-SVP đếm chi phí bằng đúng một lần gọi lời giải SVP trên khối kích thước `β` và bỏ hết hệ số đa thức. Chi phí thật của một tấn công luôn cao hơn, vì BKZ gọi lời giải SVP rất nhiều lần và mỗi lần còn có phí riêng.

## Chiều của sự bảo thủ trong core-SVP · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: vì thế core-SVP là **chặn dưới lạc quan cho kẻ tấn công**, tức **bảo thủ cho người thiết kế**. Khai được chiều này là khác biệt giữa một câu tự tin và một câu bảo vệ được: nếu con số bị sai, nó sai về phía an toàn.

## LWE, MLWE và vai trò của nhiễu
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Tìm s từ (A, b = A·s + e mod q), với e nhỏ. Nhiễu bằng {{s002}} ⇒ khử Gauss ra s ngay. Độ khó điều khiển bởi tỉ số (độ lớn nhiễu / q).`

**Giả thiết nó đứng trên:**

## LWE, MLWE và vai trò của nhiễu (tiếp)
@phut: 1
@che-do: so

- A sinh đều và công khai, nên độ khó không dựa vào việc giấu A
- e lấy từ một phân bố đã khai, thường là phân bố nhị thức tâm hoặc Gauss rời rạc, và phân bố đó phải nằm trong đặc tả chứ không phải trong cài đặt
- kẻ tấn công có nhiều mẫu LWE tuỳ ý trong giới hạn của giao thức, nên số mẫu là một tham số của bài toán

## LWE, MLWE và vai trò của nhiễu (tiếp)
@phut: 1
@che-do: so

- với MLWE: giả định không có tấn công nào khai thác được cấu trúc vành tốt hơn tấn công trên lưới không cấu trúc

## LWE, MLWE và vai trò của nhiễu · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Chỗ hay hiểu sai nhất của cả module nằm ở giả thiết thứ hai. Nhiễu **không** phải nhược điểm kỹ thuật cần giảm; nó là nguồn độ khó. Ngân sách nhiễu bị chia ba phần: phần cho độ khó, phần cho sai số làm tròn khi nén bản mã, và phần lề cho tỉ lệ giải mã sai. Giảm phần đầu để đổi lấy hai phần sau là giảm an toàn, nên phải khai là một cuộc đổi.

## Mô hình chi phí core-SVP
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Chi phí cổ điển ≈ 2^(0,292 · β) Chi phí lượng tử ≈ 2^(0,265 · β) Suy ra: β cần cho λ bit cổ điển = λ / {{s006}}`

**Giả thiết nó đứng trên:**

## Mô hình chi phí core-SVP (tiếp)
@phut: 1
@che-do: so

- bỏ hết hệ số đa thức, nên đây là chặn dưới lạc quan cho kẻ tấn công và bảo thủ cho người thiết kế
- đếm đúng một lần gọi lời giải SVP trên khối kích thước β, trong khi BKZ thật gọi rất nhiều lần
- bộ nhớ của kẻ tấn công không bị tính phí, kể cả phí truy cập ngẫu nhiên vào bộ nhớ lớn

## Mô hình chi phí core-SVP (tiếp)
@phut: 1
@che-do: so

- β lấy từ một bộ ước lượng ở một phiên bản cố định, và phiên bản đó phải khai trong bài

## Mô hình chi phí core-SVP · ghi chú
@phut: 1
@che-do: noi

Hai số mũ {{s006}} và {{s007}} là hai **mô hình chi phí khác nhau cho cùng một tấn công**, không phải hai tấn công. Vì thế câu an toàn {{s001}} bit không có nghĩa khi chưa nói là cổ điển hay lượng tử, và cũng không có nghĩa khi chưa nói phiên bản bộ ước lượng. Hai bài cùng viết {{s001}} bit mà khai hai mô hình khác nhau là hai con số không so được.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s008}} | số mũ trên β | Số mũ chi phí core-SVP cổ điển
!so {{s009}} | số mũ trên β | Cùng tấn công đó nhưng tính trong mô hình chi phí lượng

## Trong mô hình core-SVP cổ điển
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong mô hình core-SVP cổ điển, kích thước khối BKZ cần thiết để đạt {{s001}} bit an toàn là bao nhiêu?

lam = {{s001}}, ec = {{s008}}

## Trong mô hình core-SVP cổ điển · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`lam / ec`

Khoảng {{s010}}, tức β khoảng {{s011}}. Phép chia này là toàn bộ nội dung của câu an toàn {{s001}} bit trong mô hình core-SVP cổ điển: lấy mức mục tiêu chia cho số mũ. Vì nó chỉ là một phép chia, mọi độ bất định của con số {{s001}} bit nằm ở hai chỗ khác: ở việc số mũ {{s006}} có đúng không, và ở việc bộ ước lượng trả về β nào cho bộ tham số của anh.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Lấy đúng bộ tham số vừa chọn để đạt {{s001}} bit cổ điển, tức β bằng {{s001}} chia {{s006}}. Trong mô hình core-SVP lượng tử, bộ tham số đó đạt bao nhiêu bit?

eq = {{s009}}, lam = {{s001}}, ec = {{s008}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`eq × (lam / ec)`

Khoảng {{s012}} bit, tức THẤP HƠN {{s001}} bit chứ không bằng. Cùng một bộ tham số, hai con số khác nhau, và khoảng cách gần {{s013}} bit. Đây là lý do một bảng bộ tham số phải có hai cột chứ không một cột, và là lý do câu bộ tham số của chúng tôi an toàn {{s001}} bit phải nói rõ {{s001}} bit trong mô hình nào.

## Trong mô hình core-SVP, β là gì?
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong mô hình core-SVP, β là gì?

- Số mẫu LWE mà kẻ tấn công thu được
- Chiều của lưới
- Kích thước khối mà BKZ cần dùng để thu gọn đủ sâu nhằm giải bộ tham số đang xét
- Số bit của module q

## Trong mô hình core-SVP, β là gì? · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Kích thước khối mà BKZ cần dùng để thu gọn đủ sâu nhằm giải bộ tham số đang xét**

## Trong mô hình core-SVP, β là gì? · đáp (tiếp)
@phut: 1
@che-do: noi

β là tham số của thuật toán tấn công, không phải tham số của hệ. Nó là đầu ra của một bộ ước lượng chạy trên bộ tham số của hệ, nên nó kế thừa toàn bộ độ bất định của bộ ước lượng đó, kể cả phiên bản. Chiều lưới và module q là tham số của hệ, còn số mẫu là một phần của mô hình tấn công.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Core-SVP bỏ hết hệ số đa thức. Điều đó làm nó thành ước lượng theo chiều nào?

- Ước lượng không chệch, vì các hệ số bị bỏ triệt tiêu nhau
- Không nói được chiều nào, vì hệ số đa thức có thể âm
- Chặn trên lạc quan cho người thiết kế, tức con số in ra cao hơn mức thật
- Chặn dưới lạc quan cho kẻ tấn công, tức bảo thủ cho người thiết kế

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chặn dưới lạc quan cho kẻ tấn công, tức bảo thủ cho người thiết kế**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

BKZ thật gọi lời giải SVP rất nhiều lần, còn core-SVP đếm đúng một lần và bỏ phí mỗi lần. Nên chi phí thật của kẻ tấn công luôn CAO hơn con số của core-SVP. Người thiết kế dùng con số thấp đó để chọn tham số, nên bộ tham số ra to hơn mức cần: sai về phía an toàn. Khai được chiều này là khác biệt giữa một câu tự tin và một câu bảo vệ được.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai bài đều báo bộ tham số của mình an toàn {{s001}} bit. Thiếu đúng một nhóm dữ kiện để so hai con số đó. Nhóm nào?

- Mô hình chi phí (cổ điển hay lượng tử, có tính hệ số đa thức hay không) và phiên bản bộ ước lượng
- Thời gian sinh khoá đo trên cùng một máy
- Ngôn ngữ và trình biên dịch của hai cài đặt
- Chiều lưới và module q của từng bộ

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Mô hình chi phí (cổ điển hay lượng tử, có tính hệ số đa thức hay không) và phiên bản bộ ước lượng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Cùng một bộ tham số cho {{s014}} bit trong mô hình {{s006}} và {{s015}} bit trong mô hình {{s007}}, và đổi lại con số lần nữa nếu đếm hệ số đa thức. Nên con số {{s001}} bit không xác định được bộ tham số, và hai con số {{s001}} bit từ hai mô hình khác nhau là hai thước đo khác nhau. Chiều lưới và q thì suy ra được sau khi đã cố định mô hình, nên chúng không phải dữ kiện thiếu.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả bộ tham số sau có một câu không kiểm được. Bấm vào câu đó.

- Bộ tham số của chúng tôi dùng chiều lưới và module q như trong Bảng II.
- Chúng tôi chạy bộ ước lượng lattice để lấy kích thước khối BKZ cần thiết cho bộ tham số đó.
- Bộ tham số đạt an toàn {{s001}} bit, nên nó mạnh hơn bộ tham số của công trình trước.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Bộ tham số đạt an toàn {{s001}} bit, nên nó mạnh hơn bộ tham số của công trình trước.**

Câu này thiếu hai thứ và vì thế nó không kiểm được, cũng không so được. Thứ nhất, {{s001}} bit trong mô hình chi phí nào: cùng một bộ tham số cho {{s014}} bit với số mũ {{s006}} và {{s015}} bit với số mũ {{s007}}, và đổi lần nữa nếu đếm hệ số đa thức. Thứ hai, phiên bản của bộ ước lượng:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

β là đầu ra của một công cụ đang được cập nhật, nên không có phiên bản thì con số không tái lập được. Và chữ mạnh hơn là chỗ nặng nhất: khi hai bên chưa cùng mô hình chi phí thì thứ hạng có thể đảo, nên so sánh này không có nội dung. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

trong chính bảng, thêm cột mô hình chi phí và cột phiên bản bộ ước lượng, rồi chạy lại con số của công trình trước bằng cùng một mô hình.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả thiết kế sau có một câu đi ngược bản chất bài toán. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- LWE đặt bài toán tìm s từ cặp (A, b = A·s + e mod q) với e nhỏ.
- Chúng tôi giảm độ lớn nhiễu e để giảm tỉ lệ giải mã sai, và điều này đồng thời làm hệ an toàn hơn vì bản mã sạch hơn.
- Phần còn lại của ngân sách nhiễu dành cho sai số làm tròn khi nén bản mã.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Chúng tôi giảm độ lớn nhiễu e để giảm tỉ lệ giải mã sai, và điều này đồng thời làm hệ an toàn hơn vì bản mã sạch hơn.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Nửa đầu câu đúng và nửa sau ngược chiều. Nhiễu là NGUỒN độ khó: không có e thì b = A·s mod q giải được bằng khử Gauss trong thời gian đa thức, tức hệ sập hẳn. Đại lượng quyết định độ khó là tỉ số độ lớn nhiễu trên q, nên giảm nhiễu là đi về phía dễ. Giảm tỉ lệ giải mã sai và giữ độ khó là một cuộc đổi, phải khai là cuộc đổi. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

tách ngân sách nhiễu thành ba phần (phần cho độ khó, phần cho sai số làm tròn khi nén, phần lề cho giải mã sai), rồi nói rõ anh lấy từ phần nào và chạy lại bộ ước lượng trên tham số mới.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Chọn mức an toàn mục tiêu λ bit, ví dụ λ = {{s001}} cổ điển
- Chọn mô hình chi phí: core-SVP cổ điển, chi phí bậc {{s004}} luỹ thừa ({{s006}} β)
- Đặt {{s006}} · β = λ, tức chỉ so số mũ
- β = λ / {{s006}}, với λ = {{s001}} cho β khoảng {{s011}}
- Chọn chiều lưới và tỉ số nhiễu trên q sao cho bộ ước lượng trả về đúng β đó

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: β = {{s016}} · số mũ cổ điển {{s006}} · hệ số đa thức góp {{s002}} bit · {{s014}} bit cổ điển · {{s015}} bit lượng tử · β cần cho {{s001}} bit là {{s010}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Bỏ hết hệ số đa thức, tức core-SVP thuần** tắt đi: Đếm cả số lần BKZ gọi lời giải SVP và phí mỗi lần gọi, nên có một lượng bit cộng thêm phụ thuộc chiều lưới và phụ thuộc cài đặt.
- **Có một phiên bản bộ ước lượng cố định để lấy β** tắt đi: β đổi theo phiên bản bộ ước lượng và theo mỗi lần có tấn công mới được thêm vào nó.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Bộ nhớ của kẻ tấn công không bị tính phí** tắt đi: Tính phí dung lượng và phí truy cập ngẫu nhiên vào bộ nhớ rất lớn mà sieving đòi.
- **Cấu trúc vành của MLWE không cho tấn công nào tốt hơn lưới không cấu trúc** tắt đi: Có một tấn công khai thác được cấu trúc vành.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Mô hình chi phí, không phải hệ. Kéo số mũ và kéo lượng bit do hệ số đa thức đóng góp, rồi xem con số bit an toàn và β cần thiết đổi theo. Để ý thanh cuối cùng: nó là thứ core-SVP đặt bằng {{s002}}.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.2` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table III claims 128-bit security for the proposed parameter set and compares it with two prior parameter sets on the same scale. The paper does not state which cost model produced these numbers, nor which estimator version was used. As it stands the ordering in Table III is not reproducible. Please justify the comparison.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Table III has been rebuilt so that all three parameter sets are evaluated under one declared cost model. The caption now states the model explicitly: core-SVP, classical exponent {{s008}} and quantum exponent {{s009}} on the BKZ block size, with polynomial factors omitted, and it names the estimator and the exact commit we ran. We no longer quote security levels from the original papers, because those were produced under different models; instead we re-ran all three parameter sets ourselves, and Appendix C gives the script.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The table now carries two columns, classical and quantum, since the same parameter set yields different numbers in the two models. We also state the direction of the approximation: core-SVP counts a single SVP call and omits per-call cost, so it is a lower bound on attack cost and therefore conservative for the designer, which means an error in this number makes our parameters larger than necessary rather than weaker than claimed. Finally, Section V-C reports a robustness check:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

we recomputed the ordering with polynomial factors included, and the ordering of the three sets is unchanged, so none of our conclusions depends on the choice of model. Where the ordering had changed we would have said so.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: dẫn thêm một bài dùng cùng con số {{s001}} bit và nói đó là thông lệ của lĩnh vực. Đúng về thực hành, nhưng không làm bảng tái lập được và không trả lời được chuyện thứ hạng.
- Mức {{s004}}: khai mô hình core-SVP và nói rõ cổ điển hay lượng tử, nhưng vẫn giữ nguyên con số của hai công trình trước lấy từ bài gốc của họ, tức bảng vẫn trộn hai mô hình.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s005}}: khai mô hình chi phí và phiên bản bộ ước lượng ngay trong bảng, chạy lại con số của cả ba bộ tham số bằng đúng một mô hình, và in cả hai cột cổ điển và lượng tử.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

In Section IV-B the authors reduce the noise magnitude relative to the modulus in order to lower the decryption failure rate, and describe this as improving both reliability and security. This is backwards: the noise is what makes the underlying problem hard. Please explain the actual effect on the hardness of the instance.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We thank the reviewer and have corrected both the claim and the analysis. The noise is the source of hardness: with e set to zero, recovering s from b = A s mod q is a linear system solvable by Gaussian elimination in polynomial time, so the hardness is monotone in the noise-to-modulus ratio, not in the noise magnitude alone. Section IV-B now states that reducing the noise reduces the hardness of the instance, and we quantify it rather than assert it:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table V reports the estimator output before and after the change, giving the BKZ block size and the resulting classical and quantum core-SVP levels for both parameter sets, under the model and estimator commit declared in Table III. We have also replaced the single operating point with a trade-off curve, Figure {{s017}}, which plots the classical security level against the decryption failure rate across the noise budget, so the reader can see the exchange rate rather than one chosen point.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The noise budget itself is now decomposed into three parts in Section IV-A: the part that carries hardness, the rounding error introduced by ciphertext compression, and the margin reserved for the decryption failure target. The reduction in Section IV-B is taken from the margin only, and the hardness part is held fixed, which is why the re-estimated security level is unchanged to within one bit.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: sửa câu văn thành chỉ nói về độ tin cậy và bỏ chữ an toàn hơn. Đã hết sai, nhưng chưa nói được tác động thật lên độ khó, nên vẫn chưa trả lời câu hỏi.
- Mức {{s004}}: nói rằng nhiễu là nguồn độ khó và giảm nhiễu làm độ khó giảm, nhưng không định lượng và không chạy lại bộ ước lượng.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s005}}: nêu rằng đại lượng quyết định độ khó là tỉ số nhiễu trên q, chạy lại bộ ước lượng trên tham số mới, và in con số bit an toàn trước và sau khi giảm nhiễu.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.2` bấm thẻ.
