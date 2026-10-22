---
tieu-de: Nén và ngân sách truyền
phu-de: Trụ 2 FL · module 2.4
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 64.5
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: FL
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Một vòng của tôi tốn bao nhiêu byte mỗi client, và nén {{s001}} lần có thật sự giảm {{s001}} lần thời gian hội tụ không?

## Byte tới mục tiêu, không phải vòng tới mục tiêu
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Mọi bảng so sánh nén đều có thể viết theo hai tiêu chí, và hai tiêu chí cho hai thứ hạng. Tiêu chí đúng là **byte tới mục tiêu**, tức số vòng nhân byte mỗi vòng, vì đó là đại lượng mà người trả tiền thật sự trả.

## Byte tới mục tiêu, không phải vòng tới mục tiêu (tiếp)
@phut: 1
@che-do: noi

Module này có ba việc. Việc thứ nhất là tính được byte một vòng, kể cả **chi phí chỉ số** mà top-k phải trả và hay bị bỏ. Việc thứ hai là phân biệt nén **không chệch** với nén **chệch**: top-k thuần không phải chậm hơn, nó hội tụ về **điểm khác**, và phản hồi lỗi (error feedback) là thứ mua lại tính đúng chứ không phải thứ tăng tốc.

## Byte tới mục tiêu, không phải vòng tới mục tiêu (tiếp)
@phut: 1
@che-do: noi

Việc thứ ba là chỗ đáng giá nhất: nén thêm **không** luôn luôn giảm byte tới mục tiêu. Khi mỗi vòng có một chi phí cố định, dù là bắt tay (handshake), lịch chọn client, hay thiết lập secure aggregation, thì có một tỉ lệ thưa (sparsity ratio) tối ưu, và nén thưa hơn mức đó làm byte tới mục tiêu **tăng**. Mốc đó có dạng đóng, nên anh tính được nó cho hệ của mình trong một dòng.

## Byte một vòng, và chi phí chỉ số của top-k
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Byte một vòng, và chi phí chỉ số của top-k · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`byte một vòng một chiều = số tham số × số bit mỗi tham số / {{s003}}`, nhân {{s004}} nếu tính cả tải xuống. Với top-k thì chỉ gửi `s·P` toạ độ, nhưng mỗi toạ độ phải kèm **chỉ số** của nó, tốn `ceil(log2 P)` bit.

## Byte một vòng, và chi phí chỉ số của top-k · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** với ResNet-18 thì `ceil(log2(11 {{s005}} {{s006}})) = {{s007}}` bit chỉ số, nên một toạ độ fp32 kèm chỉ số tốn **{{s008}} bit chứ không phải {{s009}}**. Hệ quả: top-1% không giảm {{s010}} lần mà giảm khoảng {{s011}} lần. Một bảng báo giảm {{s010}} lần là bảng quên chỉ số, và đó là con số dễ kiểm nhất mà một phản biện sẽ kiểm trước.

## Không chệch so với chệch
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s012}} trên bốn.*

## Không chệch so với chệch · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Lượng tử hoá ngẫu nhiên không chệch có `E[Q(v)] = v`: nó chỉ thêm phương sai, nên nó nằm trong khuôn SGD nhiễu và các bound cũ vẫn áp với `sigma^2` lớn hơn. Top-k thì **chệch**: `E[topk(v)]` khác `v`, và thiên lệch đó không tự triệt tiêu qua các vòng.

## Không chệch so với chệch · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** phản hồi lỗi (error feedback) giữ phần bị bỏ lại trong một bộ đệm cục bộ rồi cộng vào vòng sau, nên nó **mua lại tính đúng của điểm tới**, không phải mua tốc độ.
Nói cách khác:
thiếu phản hồi lỗi thì top-k không chậm hơn, nó **tới chỗ khác**, và sai lệch đó không hiện ra trên đường cong hội tụ vì đường cong vẫn trông như đã hội tụ.

## Không chệch so với chệch · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là lý do một bài dùng top-k mà không nói phản hồi lỗi là bài có một lỗ hổng im lặng.

## Vì sao có tỉ lệ thưa tối ưu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s013}} trên bốn.*

## Vì sao có tỉ lệ thưa tối ưu · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Gọi `c = P(b + idx)/8` là byte tải trọng khi gửi hết, `H` là chi phí cố định mỗi vòng mỗi client, và `R(s) = R0(rho/s + {{s002}} - rho)` là số vòng tới mục tiêu khi giữ tỉ lệ `s`. Byte tới mục tiêu là `R(s)·(c·s + H)`, nhân ra thành `R0[rho·c + rho·H/s + (1-rho)c·s + (1-rho)H]`.

## Vì sao có tỉ lệ thưa tối ưu · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** trong tổng đó có một số hạng tăng theo `s` và một số hạng tăng theo `1/s`, nên nó **có cực tiểu nội** tại `s⋆ = sqrt(rho·H/((1-rho)·c))`.
Nén thưa hơn `s⋆` làm byte tới mục tiêu **tăng**, vì chi phí cố định `H` bị nhân với số vòng đang phình theo `1/s`.

## Vì sao có tỉ lệ thưa tối ưu · đáp (tiếp)
@phut: 1
@che-do: noi

Và nếu `rho = {{s002}}`, tức anh phải trả đủ trần lý thuyết `1/s` của bộ nén co, thì tải trọng triệt tiêu hoàn toàn và nén thưa **không mua được byte nào**, chỉ còn mua thêm chi phí chỉ số và chi phí cố định.

## Byte một vòng
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`byte một vòng một chiều = s·P·(b + idx)/8 + H, idx = ceil(log2 P) · E[Q(v)] = v cho lượng tử không chệch · R(s) = R0·(rho/s + {{s002}} - rho) · byte tới mục tiêu = R(s)·(s·P·(b+idx)/8 + H) · s⋆ = sqrt(rho·H/((1-rho)·P·(b+idx)/8))`

**Giả thiết nó đứng trên:**

## Byte một vòng (tiếp)
@phut: 1
@che-do: so

- Mỗi toạ độ giữ lại tốn b bit giá trị CỘNG idx bit chỉ số; khi gửi dày đủ thì không cần chỉ số nên idx = {{s014}}
- H là chi phí cố định mỗi vòng mỗi client, gồm bắt tay, tiêu đề, lịch chọn client và thiết lập secure aggregation; H phải ĐO ĐƯỢC trên hệ thật, không đoán

## Byte một vòng (tiếp)
@phut: 1
@che-do: so

- rho là hệ số phình vòng do nén, trong đoạn từ {{s014}} tới {{s002}}, ĐO ĐƯỢC từ ablation của chính anh: rho = {{s014}} là nén miễn phí, rho = {{s002}} là trả đủ trần lý thuyết 1/delta của bộ nén delta-co với delta = s
- R0 là số vòng tới mục tiêu khi KHÔNG nén, đo trên cùng một mức mục tiêu

## Byte một vòng (tiếp)
@phut: 1
@che-do: so

- Mọi công thức trên giả định nén còn giữ được ĐIỂM TỚI, tức không chệch hoặc có phản hồi lỗi; nếu không thì không có mục tiêu nào để đếm byte tới
- Mô hình chi phí là tuyến tính theo byte, tức băng thông là cổ chai; nếu độ trễ là cổ chai thì phải thay bằng mô hình theo số vòng

## Byte một vòng · ghi chú
@phut: 1
@che-do: noi

Dạng `R(s) = R0(rho/s + {{s002}} - rho)` là một **nội suy khai ra** giữa hai đầu kiểm được, không phải một định lý: tại `rho = {{s014}}` nó cho `R0`, tại `rho = {{s002}}` nó cho `R0/s` đúng bằng trần lý thuyết của bộ nén co. Giá trị `rho` ở giữa là thứ anh phải đo, và nếu bài của anh không đo nó thì mọi tuyên bố về thời gian hội tụ của phần nén là chưa có cơ sở.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s015}} | MB | ResNet-18 có {{s016}} triệu tham số
!so {{s017}} | MB | Cùng mô hình ResNet-18 đó
!so {{s018}} | MB | Cùng mô hình đó

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

So dense fp32 với top-1% có chỉ số {{s007}} bit mỗi toạ độ. Payload nhỏ đi bao nhiêu lần?

bit = {{s009}}, s = {{s019}}, idx = {{s007}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`bit/(s⋆(bit + idx))`

{{s020}} lần, không phải {{s010}} lần. Chênh lệch đến từ chỉ số: mỗi toạ độ giữ lại tốn {{s009}} bit giá trị cộng {{s007}} bit chỉ số, tức {{s008}} bit, nên tải trọng mỗi toạ độ tăng {{s021}} lần so với dense. Một bảng báo giảm {{s010}} lần là bảng quên chi phí chỉ số, và đây là con số mà phản biện kiểm trước tiên vì nó kiểm được bằng một phép chia.

## ResNet-18 với 11,69 triệu tham số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

ResNet-18 với {{s016}} triệu tham số, {{s009}} bit giá trị và {{s007}} bit chỉ số, chi phí cố định {{s023}} B mỗi vòng mỗi client, hệ số phình vòng rho = {{s025}}. Tỉ lệ thưa tối ưu s⋆ bằng bao nhiêu?

rho = {{s022}}, H = {{s023}}, P = {{s024}}, bit = {{s009}}, idx = {{s007}}

## ResNet-18 với 11,69 triệu tham số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.sqrt(rho⋆H/((1-rho)⋆P⋆(bit+idx)/8))`

{{s026}}, tức giữ khoảng {{s027}} toạ độ là đáy của byte tới mục tiêu. Nén thưa hơn mức này làm byte tới mục tiêu TĂNG, vì số hạng rho·H/s phình theo 1/s trong khi tải trọng đã nhỏ tới mức không bù lại được. Để ý s⋆ phụ thuộc H: với H = {{s014}} thì s⋆ về {{s014}} và không có vùng đảo chiều, nên vùng đó là tính chất của chi phí cố định mỗi vòng, không phải của bộ nén.

## Hai bộ nén dưới đây
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai bộ nén dưới đây, cái nào cần phản hồi lỗi để giữ được điểm tới, và vì sao?

- Lượng tử hoá ngẫu nhiên không chệch, vì nó thêm phương sai
- Top-k, vì nó chệch nên thiên lệch tích luỹ qua các vòng
- Cả hai, vì cả hai đều làm mất thông tin
- Không cái nào, phản hồi lỗi chỉ để tăng tốc

## Hai bộ nén dưới đây · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Top-k, vì nó chệch nên thiên lệch tích luỹ qua các vòng**

## Hai bộ nén dưới đây · đáp (tiếp)
@phut: 1
@che-do: noi

Lượng tử không chệch có E[Q(v)] = v nên nó chỉ thêm phương sai, và phương sai nằm trong khuôn SGD nhiễu có sẵn. Top-k thì chệch, và thiên lệch không tự triệt tiêu, nên không có phản hồi lỗi thì thuật toán tới một điểm khác. Phương án đầu lẫn phương sai với thiên lệch; phương án cuối gán sai công lao cho phản hồi lỗi, vì nó mua lại tính đúng chứ không mua tốc độ.

## Mô hình 11,69 triệu tham số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình {{s016}} triệu tham số, chuyển từ fp32 dày sang top-1% có mã hoá chỉ số tường minh. Payload mỗi vòng nhỏ đi bao nhiêu lần?

- {{s010}} lần, đúng bằng tỉ lệ nén
- Khoảng {{s011}} lần, vì mỗi toạ độ phải kèm {{s007}} bit chỉ số
- Khoảng {{s009}} lần, vì mất hết độ chính xác fp32
- Không xác định được nếu chưa biết số client

## Mô hình 11,69 triệu tham số · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khoảng {{s011}} lần, vì mỗi toạ độ phải kèm {{s007}} bit chỉ số**

Mỗi toạ độ giữ lại tốn {{s009}} bit giá trị cộng ceil(log2(11 {{s005}} {{s006}})) = {{s007}} bit chỉ số, tức {{s008}} bit, nên tỉ số là {{s009}} chia cho {{s028}} nhân {{s008}}, bằng {{s020}}. Phương án đầu là con số hay bị báo trong bảng và là chỗ phản biện kiểm trước. Phương án cuối sai vì payload mỗi vòng mỗi client không phụ thuộc số client.

## Trong vùng nén rất thưa
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong vùng nén rất thưa, byte tới mục tiêu TĂNG khi nén thêm. Đại lượng nào tạo ra vùng đó?

- Chi phí cố định H mỗi vòng mỗi client, vì số vòng phình theo 1/s
- Phương sai của bộ lượng tử, vì nó tăng khi số mức giảm
- Số tham số của mô hình, vì nó quyết định số bit chỉ số
- Chi phí chỉ số, vì mỗi toạ độ phải kèm chỉ số của nó

## Trong vùng nén rất thưa · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chi phí cố định H mỗi vòng mỗi client, vì số vòng phình theo 1/s**

Byte tới mục tiêu chứa số hạng rho·H/s, tăng không giới hạn khi s về {{s014}}, nên đáy ở s⋆ = sqrt(rho·H/((1-rho)c)). Đặt H = {{s014}} thì s⋆ về {{s014}} và vùng đảo chiều biến mất, nên vùng đó là tính chất của chi phí cố định mỗi vòng. Chi phí chỉ số chỉ dịch hệ số c, tức dịch chỗ của đáy, chứ không tạo ra đáy.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một câu đổi đơn vị mà không nhân đủ. Bấm vào câu đó.

- Chúng tôi áp top-1% cho các cập nhật, giữ {{s029}} toạ độ có trị tuyệt đối lớn nhất,
- nên lượng truyền mỗi vòng giảm {{s010}} lần,
- và số vòng tới mục tiêu tăng từ {{s010}} lên {{s030}} trong Bảng V,
- nên chúng tôi báo thêm cột byte tới mục tiêu ngay cạnh cột số vòng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên lượng truyền mỗi vòng giảm {{s010}} lần,**

Mỗi toạ độ giữ lại phải kèm chỉ số của nó, tốn ceil(log2 P) bit, với ResNet-18 là {{s007}} bit. Một toạ độ fp32 kèm chỉ số tốn {{s008}} bit chứ không phải {{s009}}, nên payload giảm khoảng {{s011}} lần, không phải {{s010}}. Câu đầu và hai câu sau đều hợp lệ về phát biểu. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

đổi {{s010}} lần thành {{s011}} lần và thêm một dòng khai số bit chỉ số; nếu anh thật sự đạt gần {{s010}} lần thì phải khai cơ chế làm được điều đó, ví dụ mẫu thưa cố định dùng lại nhiều vòng hoặc nén chỉ số bằng mã hoá entropy, và cơ chế đó là một đóng góp riêng phải trình bày.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thảo luận sau có một câu gán sai cơ chế. Bấm vào câu đó.

- Top-k là bộ nén chệch, nên cập nhật tích luỹ không còn là một ước lượng không chệch của gradient,
- do đó chúng tôi thêm phản hồi lỗi với một bộ đệm phần dư ở mỗi client,
- và chính nhờ phản hồi lỗi mà phương pháp của chúng tôi hội tụ nhanh hơn baseline nén {{s031}} lần.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và chính nhờ phản hồi lỗi mà phương pháp của chúng tôi hội tụ nhanh hơn baseline nén {{s031}} lần.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Phản hồi lỗi sửa THIÊN LỆCH, tức mua lại điểm tới đúng, chứ không mua tốc độ. Nó giữ lại phần bị bỏ nên không bỏ đi nhiễu nào, và ở những vòng đầu nó có thể còn chậm hơn top-k thuần. Hai câu đầu đều phát biểu đúng. Cách sửa: tách hai tuyên bố ra. Thứ nhất, phản hồi lỗi giữ điểm tới, và bằng chứng là độ chính xác cuối cùng so với bản không nén, không phải số vòng.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Thứ hai, nếu thật sự có nhanh hơn {{s031}} lần thì phải quy cho một nguyên nhân khác và khai nguyên nhân đó, ví dụ đã dò lại bước học, vì so với baseline nén nào và ở cùng ngân sách dò nào cũng là một câu phải khai.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Byte một vòng một client = c·s + H, với c = P(b + idx)/8 và idx = ceil(log2 P)
- Số vòng tới mục tiêu R(s) = R0(rho/s + {{s002}} - rho)
- Byte tới mục tiêu = R(s)(c·s + H) = R0[rho·c + rho·H/s + (1-rho)c·s + (1-rho)H]
- Lấy đạo hàm theo s rồi cho bằng {{s014}}: trừ rho·H/s^2 cộng (1-rho)c bằng {{s014}}
- s⋆ = sqrt(rho·H/((1-rho)·c)), và nén thưa hơn s⋆ làm byte tới mục tiêu TĂNG

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: ResNet-18 fp32 dày · {{s032}} MB một vòng một chiều · {{s010}} vòng · {{s033}} MB tới mục tiêu · tỉ số byte {{s034}} · s⋆ tối ưu {{s026}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Nén không chệch, hoặc có phản hồi lỗi** tắt đi: Dùng top-k thuần, không giữ bộ đệm phần dư, nên E[Q(v)] khác v và thiên lệch tích luỹ qua các vòng.
- **Chi phí chỉ số đáng kể và đã được đếm** tắt đi: Bỏ qua chỉ số, ví dụ giả định một mẫu thưa cố định dùng lại nhiều vòng, hoặc nén chỉ số bằng mã hoá entropy.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Có chi phí cố định H mỗi vòng mỗi client** tắt đi: Đặt H = {{s014}}, tức coi một vòng chỉ tốn đúng tải trọng của nó.
- **Băng thông lên là cổ chai** tắt đi: Cổ chai là độ trễ vòng, thời gian tính cục bộ, hoặc thời gian chờ client chậm nhất.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ngân sách truyền (communication budget), đọc theo byte tới mục tiêu chứ không theo vòng tới mục tiêu. Mặc định là ResNet-18 fp32 không nén. Kéo tỉ lệ thưa và để ý rằng đường byte tới mục tiêu KHÔNG đơn điệu.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.4` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V claims a {{s010}} times reduction in communication from top-1 percent sparsification and concludes a proportional reduction in training time. Two issues. First, explicit index coding costs ceil(log2 P) bits per retained coordinate, so the payload reduction is closer to {{s011}} times for your model. Second, Table V shows the round count rising from {{s010}} to {{s030}} under compression, so bytes to target accuracy, not bytes per round, is the quantity that supports a time claim.

## Phản biện hỏi (tiếp)
@phut: 1
@che-do: hoi

Please report bytes to target and state the per-round fixed overhead of your protocol.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept both points and have rewritten Section V-B. First, we now count index cost. With {{s017}} million parameters an index needs {{s007}} bits, so a retained fp32 coordinate costs {{s008}} bits rather than {{s009}}, and top-1 percent reduces the per-round payload by {{s011}} times, not {{s010}}. Table V reports the corrected figure and adds the index bit width as an explicit row. Second, we replaced the time claim with a bytes-to-target column.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Measured on our setting, the uncompressed run reaches the target in {{s010}} rounds at {{s015}} MB per round per client, that is {{s035}} MB, while top-1 percent needs {{s030}} rounds at {{s036}} MB, that is {{s037}} MB, a reduction of {{s038}} percent rather than two orders of magnitude. Third, we measured the per-round fixed overhead of our protocol, which is {{s039}} kB per client per round covering handshake, headers and client scheduling, and we now report it.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

With that overhead the bytes-to-target curve has an interior minimum, and the model gives its location in closed form as the square root of rho H over one minus rho times c, where c is the full payload in bytes and rho is the measured round inflation coefficient. For our values that is a retained fraction near {{s040}}, and Section V-C reports the sweep that confirms the minimum lies between {{s041}} and {{s019}}. We also report the adverse half of that finding:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

compressing below {{s042}} makes bytes to target exceed the uncompressed baseline, so more compression is not uniformly better in our protocol. Finally we corrected the attribution of error feedback. It restores the fixed point of the compressed iteration rather than accelerating it, and the evidence we give for it is the final accuracy gap against the uncompressed run, not the round count.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: sửa {{s010}} lần thành {{s011}} lần và giữ nguyên câu về thời gian. Đã trả lời nửa thứ nhất, nhưng câu thời gian vẫn dựa trên byte mỗi vòng chứ không trên byte tới mục tiêu, nên phản bác chính vẫn còn.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: sửa cả hai con số và báo thêm cột byte tới mục tiêu. Đã đúng, nhưng chưa khai chi phí cố định mỗi vòng, nên vẫn chưa nói được mức nén nào là đáy, và câu về thời gian vẫn chưa khai cổ chai.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s012}}: làm mức {{s004}}, cộng đo và khai chi phí cố định H mỗi vòng mỗi client, cộng khai cổ chai thật của hệ, cộng chỉ rõ cấu hình nén nào tối ưu theo byte tới mục tiêu chứ không theo tỉ lệ nén.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.4` bấm thẻ.
