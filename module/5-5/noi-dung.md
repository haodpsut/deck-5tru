---
tieu-de: Ràng buộc thiết bị: nơi lý thuyết gặp MTU
phu-de: Trụ 5 PQC · module 5.5
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 69
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

Trên mạng {{s001}}, một bắt tay hậu lượng tử của tôi tốn bao nhiêu mảnh, và tỉ lệ mất mảnh làm xác suất hoàn tất bắt tay tụt bao nhiêu?

## Byte vào số mũ, vòng thì không
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Trụ này có một trục duy nhất: với người làm mạng, PQC là bài toán **kích thước**, không phải bài toán toán học. Module này là chỗ trục đó thành một con số có thể bị phản biện. Trên {{s001}}, khung chỉ có {{s002}} byte, nên một phần chia khoá hybrid {{s003}} byte không đi được một lần:

## Byte vào số mũ, vòng thì không (tiếp)
@phut: 1
@che-do: noi

nó bị cắt thành **{{s004}} mảnh**, và nếu mỗi mảnh mất độc lập với xác suất {{s005}} phần trăm thì bắt tay một chiều hoàn tất khoảng **{{s006}} phần trăm** số lần.

## Byte vào số mũ, vòng thì không (tiếp)
@phut: 1
@che-do: noi

Hai hệ quả phải mang theo khi viết bài. Thứ nhất, **giảm byte quan trọng hơn giảm số vòng**: số vòng do giao thức khoá (bốn bản tin EDHOC là bốn bản tin, không bỏ được bản nào mà vẫn còn là trao đổi khoá), còn byte thì cắt được, và byte đã cắt được trả công ở mọi vòng vì nó nằm trong số mũ. Thứ hai, con số {{s006}} phần trăm chỉ tồn tại cùng với một **mô hình mất gói**.

## Byte vào số mũ, vòng thì không (tiếp)
@phut: 1
@che-do: noi

Mô hình mất gói không phải chi tiết kỹ thuật của lớp liên kết, nó là một giả thiết phải khai, và reviewer đọc phần đánh giá sẽ đi tìm đúng chỗ đó.

## Ngân sách khung 802.15.4 (frame budget)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Ngân sách khung 802.15.4 (frame budget) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

MTU của {{s001}} là **{{s002}} byte** cho cả khung. Trừ tiêu đề MAC, tiêu đề bảo mật và tiêu đề phân mảnh 6LoWPAN, tải khả dụng cho tầng trên còn **bậc {{s008}} tới {{s009}} byte** mỗi mảnh.

## Ngân sách khung 802.15.4 (frame budget) · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: con số đi vào mọi phép tính của module này không phải {{s002}} mà là **tải khả dụng**, và tải khả dụng phụ thuộc cấu hình bảo mật chứ không phải hằng số của chuẩn. Khai {{s009}} byte thì phải nói rõ là chế độ nào, vì chuyển sang {{s008}} byte làm số mảnh của {{s003}} byte nhảy từ {{s004}} lên {{s010}}.

## Vì sao byte vào số mũ mà vòng thì không
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s011}} trên bốn.*

## Vì sao byte vào số mũ mà vòng thì không · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Xác suất hoàn tất là `(1-p)^(v · ceil(B/W))`, với `v` là số vòng, `B` tổng byte một chiều, `W` tải khả dụng mỗi mảnh. Cả `v` và `B` đều nằm trong số mũ, nên về hình thức hai thứ ngang nhau.

## Vì sao byte vào số mũ mà vòng thì không · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: cái làm chúng khác nhau là **quyền tự do thiết kế**. Số vòng do tính an toàn của giao thức khoá, bỏ một bản tin là đổi giao thức. Byte thì cắt được bằng nén tiêu đề, bằng chứng chỉ gọn hơn, bằng bộ tham số khác, và mỗi byte cắt đi được nhân với `v` trong số mũ. Nên trong một bài báo về PQC cho IoT, trục đóng góp đáng viết là byte.

## Mô hình mất gói là một giả thiết phải khai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s012}} trên bốn.*

## Mô hình mất gói là một giả thiết phải khai · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Công thức `(1-p)^n` đứng trên giả thiết mất **độc lập**. Trên liên kết vô tuyến thật, mất thường theo chùm (burst loss): một lần nhiễu ăn vài mảnh liền nhau. Với cùng tỉ lệ mất trung bình, mất theo chùm cho xác suất hoàn tất **cao hơn** công thức độc lập, vì các lần mất dồn vào ít lần thử hơn.

## Mô hình mất gói là một giả thiết phải khai · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: như thế `(1-p)^n` là con số **bi quan**, nên nó an toàn để dùng làm chặn dưới nhưng không an toàn để dùng làm kết quả đo. Bài báo khai nó mà không khai mô hình mất gói là bài báo in một con số không kiểm được, và đó là điểm reviewer đánh.

## Số mảnh và xác suất hoàn tất bắt tay
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`n_mảnh = ceil(B / W) P_hoàn_tất = ({{s007}} − p)^(v · n_mảnh) số lần thử trung bình = {{s007}} / P_hoàn_tất`

**Giả thiết nó đứng trên:**

## Số mảnh và xác suất hoàn tất bắt tay (tiếp)
@phut: 1
@che-do: so

- W là tải khả dụng cho tầng trên sau mọi tiêu đề, và là hằng số với mọi mảnh của cùng một bản tin
- mỗi mảnh mất độc lập với xác suất p, không có tương quan thời gian và không có mất theo chùm
- không có truyền lại ở lớp liên kết, nên mất một mảnh là mất cả bản tin
- v vòng trao đổi đều phải hoàn tất, và mỗi vòng mang đúng B byte

## Số mảnh và xác suất hoàn tất bắt tay · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Nghịch đảo `{{s007}} / P_hoàn_tất` là số lần thử trung bình chỉ khi các lần thử độc lập với nhau, tức giả thiết mất độc lập phải đúng cả giữa các lần thử. Trên liên kết có nhiễu kéo dài thì số lần thử trung bình này cũng bi quan theo cùng một lý do.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s002}} | B | Gói lớn nhất ở TẦNG VẬT LÝ của {{s001}} (aMaxPHYPacketSize) là bao
!so {{s004}} | mảnh | Phần chia khoá hybrid phía khách là {{s003}} byte
!so {{s013}} | % | {{s004}} mảnh, mỗi mảnh mất độc lập với xác suất {{s014}}, không

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s015}} | % | Cũng p = {{s014}}

## Cùng 1216 byte
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cùng {{s003}} byte, nhưng cấu hình bảo mật nặng hơn nên tải khả dụng chỉ còn {{s008}} byte mỗi mảnh. Số mảnh là bao nhiêu?

byte = {{s003}}, tai = {{s008}}

## Cùng 1216 byte · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.ceil(byte/tai)`

{{s010}} mảnh. Tải khả dụng tụt {{s016}} phần trăm mà số mảnh tăng từ {{s004}} lên {{s010}}, tức thêm đúng {{s012}} mảnh. Ba mảnh đó không là thêm {{s017}} phần trăm chi phí: chúng vào số mũ, nên xác suất hoàn tất bị nhân thêm {{s018}} ba lần nữa, tức nhân {{s019}}.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

{{s010}} mảnh, p = {{s014}}, không truyền lại. Xác suất bản tin tới đủ là bao nhiêu phần trăm?

p = {{s020}}, n = {{s010}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆Math.pow(1-p, n)`

Khoảng {{s021}} phần trăm, tức dưới một nửa. So với {{s006}} phần trăm ở {{s004}} mảnh thì ba mảnh thêm lấy đi hơn {{s022}} điểm phần trăm. Đây là lý do con số tải khả dụng phải khai trong bài: đổi một dòng cấu hình bảo mật là đổi kết quả đánh giá.

## Giao thức có 2 vòng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Giao thức có {{s011}} vòng, mỗi chiều {{s003}} byte, tải khả dụng {{s009}} byte, p = {{s014}}. Nén được {{s023}} byte khỏi mỗi chiều mà giữ nguyên số vòng thì xác suất hoàn tất cả bắt tay tăng bao nhiêu điểm phần trăm?

p = {{s020}}, v = {{s011}}, byte = {{s003}}, tai = {{s009}}, giam = {{s023}}

## Giao thức có 2 vòng · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆(Math.pow(1-p, v⋆Math.ceil((byte-giam)/tai)) - Math.pow(1-p, v⋆Math.ceil(byte/tai)))`

Khoảng {{s024}} điểm phần trăm, từ {{s025}} lên {{s026}} phần trăm. Cùng phép nén {{s023}} byte đó, nếu giao thức chỉ có một vòng thì chỉ được khoảng {{s027}} điểm. Đây là nội dung thật của câu bài học: byte được nhân với số vòng trong số mũ, nên mỗi byte cắt đi được trả công ở MỌI vòng, trong khi số vòng thì giao thức đã khoá và anh không có quyền cắt.

## Giao thức khoá cứng 2 vòng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Giao thức khoá cứng {{s011}} vòng, không bỏ được bản tin nào. Anh có ba cách tiết kiệm, mỗi cách cắt được đúng {{s028}} byte mỗi chiều. Cách nào làm xác suất hoàn tất cả bắt tay tăng nhiều nhất?

## Giao thức khoá cứng 2 vòng (tiếp)
@phut: 0.5
@che-do: hoi

- Cắt {{s028}} byte ở vòng một, giữ nguyên vòng hai
- Cắt {{s029}} byte ở mỗi vòng
- Cắt {{s028}} byte ở cả hai vòng, nếu phần dư thừa có ở cả hai
- Ba cách tương đương, vì tổng byte cắt được như nhau

## Giao thức khoá cứng 2 vòng · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cắt {{s028}} byte ở cả hai vòng, nếu phần dư thừa có ở cả hai**

## Giao thức khoá cứng 2 vòng · đáp (tiếp)
@phut: 1
@che-do: noi

Số mũ là tổng số mảnh của cả bắt tay, nên cái quyết định là tổng số mảnh cắt được, không phải tổng byte cắt được. Cắt {{s028}} byte ở CẢ HAI vòng lấy đi {{s012}} mảnh mỗi vòng, tức {{s030}} mảnh khỏi số mũ. Cắt {{s028}} byte ở một vòng lấy đi {{s012}} mảnh. Cắt {{s029}} byte mỗi vòng lấy đi {{s011}} mảnh mỗi vòng, tức {{s031}} mảnh, vì ceil làm phần cắt lẻ không được tính.

## Giao thức khoá cứng 2 vòng · đáp (tiếp)
@phut: 1
@che-do: noi

Đáp án thứ tư sai vì nó bỏ qua ceil và bỏ qua chuyện byte được nhân với số vòng.

## Bài báo in
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài báo in: xác suất hoàn tất bắt tay {{s006}} phần trăm trên testbed {{s001}}. Thiếu đúng một dữ kiện để con số này kiểm được. Dữ kiện nào?

- Mức an toàn NIST của bộ tham số
- Số chu kỳ CPU của ML-KEM-768 trên vi điều khiển
- Mô hình mất gói dùng để tính, và tải khả dụng mỗi mảnh
- Phiên bản thư viện mật mã

## Bài báo in · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Mô hình mất gói dùng để tính, và tải khả dụng mỗi mảnh**

{{s006}} phần trăm là {{s018}} luỹ thừa {{s004}}, nên nó mang theo hai giả thiết: mất độc lập với p = {{s014}}, và số mảnh bằng {{s004}} tức tải khả dụng {{s009}} byte. Thiếu hai dữ kiện đó thì không ai dựng lại được con số, và với mất theo chùm cùng tỉ lệ trung bình thì con số thật khác hẳn.

## Bài báo in · đáp (tiếp)
@phut: 1
@che-do: noi

Ba đáp án kia đều là thông tin nên có trong bài nhưng không đứng giữa con số này và việc kiểm nó.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đánh giá sau có một dòng làm cả con số không kiểm được. Bấm vào dòng đó.

- Chúng tôi đo tỉ lệ mất mảnh {{s005}} phần trăm trên testbed {{s001}} gồm {{s032}} nút,
- tải khả dụng sau tiêu đề là {{s009}} byte mỗi mảnh, nên phần chia khoá {{s003}} byte đi thành {{s004}} mảnh,
- và bắt tay một chiều hoàn tất {{s006}} phần trăm số lần.
- Mô hình mất gói: không khai trong bài.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Mô hình mất gói: không khai trong bài.**

Ba dòng đầu đều hợp lệ và đủ để dựng lại con số VỚI ĐIỀU KIỆN biết mô hình mất. {{s006}} phần trăm chính là {{s018}} luỹ thừa {{s004}}, tức công thức độc lập. Nhưng trên liên kết vô tuyến thật, mất theo chùm là thường gặp, và với cùng tỉ lệ trung bình {{s005}} phần trăm thì xác suất hoàn tất CAO HƠN con số này.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Nên con số {{s006}} phần trăm vừa không dựng lại được vừa bi quan theo một chiều mà người đọc không biết. Cách sửa rẻ nhất: thêm một câu khai mất độc lập và nói rõ đó là chặn dưới. Cách sửa tốt hơn: báo xác suất hoàn tất ĐO ĐƯỢC cạnh con số mô hình, và nếu hai số lệch thì đó chính là kết quả đáng viết.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau có một chỗ số học sai dù mọi con số trước đó đều đúng. Bấm vào chỗ đó.

- Nhờ nén tiêu đề, bản tin của chúng tôi giảm từ {{s003}} còn {{s033}} byte, tức {{s016}} phần trăm,
- nên số mảnh giảm từ {{s004}} còn {{s034}} với tải khả dụng {{s009}} byte,
- và xác suất hoàn tất một chiều tăng {{s016}} phần trăm, từ {{s006}} lên {{s035}} phần trăm.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và xác suất hoàn tất một chiều tăng {{s016}} phần trăm, từ {{s006}} lên {{s035}} phần trăm.**

Hai dòng đầu đúng: ceil(972/100) = {{s034}}. Dòng này lấy mức giảm byte {{s016}} phần trăm và áp thẳng lên xác suất, tức coi một quan hệ hàm mũ như quan hệ tuyến tính. Con số đúng là {{s018}} luỹ thừa {{s034}}, bằng {{s036}} phần trăm, tức tăng {{s037}} ĐIỂM phần trăm chứ không phải tăng {{s016}} phần trăm. Đáng chú ý là hướng của lỗi:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

nó làm kết quả NGHE KÊU HƠN thực tế, kiểu lỗi mà nhà đã đếm được, và nó lọt qua mọi cổng chỉ kiểm cấu trúc vì cả ba con số đều có mặt và đều có dạng hợp lệ.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Cộng byte hai thành phần của phần chia khoá hybrid: {{s038}} byte X25519 cộng {{s039}} byte khoá công khai ML-KEM-768, ra B = {{s003}} byte phía khách
- Lấy tải khả dụng W sau mọi tiêu đề, ở đây W = {{s009}} byte
- Số mảnh n = ceil(B / W) = ceil(1216 / {{s009}}) = {{s004}}
- Xác suất một bản tin tới đủ là ({{s007}} − p)^n, vì cần cả {{s004}} mảnh tới

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Nhân số mũ với số vòng v để ra xác suất cả bắt tay: P = ({{s007}} − p)^(v·n)

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: {{s003}} byte mỗi chiều · tải khả dụng {{s009}} byte · {{s004}} mảnh · {{s011}} vòng · p = {{s014}} · hoàn tất cả bắt tay {{s040}} · số lần thử trung bình {{s041}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mất mảnh độc lập** tắt đi: Mất theo chùm: một lần nhiễu ăn vài mảnh liền nhau, nên các biến cố mất tương quan theo thời gian.
- **Không có truyền lại ở lớp liên kết** tắt đi: Lớp liên kết có ARQ cho từng mảnh, nên mảnh mất được gửi lại.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Tải khả dụng là hằng số {{s009}} byte cho mọi mảnh** tắt đi: Nén tiêu đề 6LoWPAN phụ thuộc ngữ cảnh, và mảnh đầu mang tiêu đề khác mảnh sau, nên tải khả dụng đổi theo từng mảnh.
- **Biết p, và p cố định** tắt đi: Tỉ lệ mất đổi theo liên kết, theo khoảng cách, theo giờ, và chỉ biết trong một dải.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ngân sách bắt tay trên {{s001}}. Kéo tổng byte, tải khả dụng, tỉ lệ mất mảnh và số vòng. Để ý thứ đổi nhanh nhất không phải xác suất mà là SỐ MŨ, vì số mảnh nhảy theo bậc thang.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.5` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The handshake completion probabilities in Table V are obtained from (1-p)^n under an independent fragment loss model. Loss on {{s001}} links is strongly correlated in time, so this model is not justified, and the reported figures are neither reproducible nor clearly conservative. Please either justify the loss model or report measured completion rates.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree that independence is an assumption rather than a property of the link, and we have made it explicit. Section V-B now states the model in the same sentence as the number, and proves the direction of the bias: for a fixed mean loss rate, correlated loss concentrates losses into fewer transmission attempts, so the independent model is a lower bound on completion probability.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table V therefore reports (1-p)^n as a conservative bound and adds a new column with the measured completion rate over {{s042}} handshakes on the 12-node testbed. For the hybrid X25519 plus ML-KEM-768 client share ({{s003}} bytes, 100-byte usable payload, {{s004}} fragments, p = {{s020}}), the model gives {{s043}} percent per direction while the measurement gives {{s044}} percent, and we report the measured mean burst length of {{s045}} fragments that explains the gap.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The design conclusion is unchanged and now rests on the measurement rather than on the model: at two round trips the handshake needs several attempts, so byte reduction and not round reduction is the lever.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s007}}: trả lời rằng mất độc lập là giả thiết chuẩn trong tài liệu. Đúng về thực hành, không trả lời được phản bác, vì reviewer đang hỏi vì sao nó đúng Ở ĐÂY.
- Mức {{s011}}: khai thêm trong bài rằng mô hình là mất độc lập, nhưng vẫn giữ bảng cũ và không nói chiều của sai lệch.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s012}}: khai mô hình, chứng minh rằng với cùng tỉ lệ mất trung bình thì mất theo chùm cho xác suất hoàn tất CAO HƠN, nên con số in ra là chặn dưới, và viết lại mọi câu kết luận ở dạng chặn dưới.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section VI reports that the post-quantum handshake does not complete within the energy budget at {{s034}} percent fragment loss. It is unclear whether this is a property of post-quantum key exchange on {{s001}} or an artifact of the authors' fragmentation and compression configuration.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have reframed the result as a conditional negative result and stated its conditions. First, the configuration is at the best available operating point rather than a default: 6LoWPAN header compression is enabled, raw public keys replace X.509 certificates, and we use the smallest parameter set that meets the target security level, so the byte count cannot be reduced further without changing the security target. Second, we now report the boundary rather than a single verdict.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Figure {{s046}} plots the (usable payload, loss rate) region in which the handshake completes within the {{s007}} joule budget: at 100-byte usable payload the handshake is feasible up to about {{s031}} percent loss, and at 80-byte payload only up to about {{s012}} percent. Third, we state the direction in which our conclusion reverses: with link-layer ARQ per fragment the feasible region widens substantially, and the binding constraint moves from completion probability to latency and energy per handshake, which we quantify in Table VII.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s007}}: nhắc lại rằng con số đo đúng như đã chạy. Không trả lời được, vì reviewer không hỏi con số có đúng mà hỏi nó là tính chất của ai.
- Mức {{s011}}: thêm một cấu hình thứ hai cho thấy kết quả tương tự, nhưng không khai rằng đã dùng hết các cách nén có sẵn.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s012}}: chứng minh cấu hình đã ở biên tốt nhất có thể (nén tiêu đề 6LoWPAN bật, chứng chỉ thô thay vì X.509, bộ tham số nhỏ nhất đủ mức an toàn mục tiêu), rồi khai rõ kết luận là kết quả âm có điều kiện, kèm đúng điều kiện nào.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.5` bấm thẻ.
