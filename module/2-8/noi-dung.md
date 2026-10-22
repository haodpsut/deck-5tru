---
tieu-de: FL cho IDS: dựng bài toán cho đúng
phu-de: Trụ 2 FL · module 2.8
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 84.5
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

Ai là client, nhãn ở đâu ra, và câu sao không gom dữ liệu về một chỗ thì tôi trả lời bằng con số nào?

## Ba câu hỏi dựng bài toán
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này không nói về thuật toán. Nó dựng bài toán, và nó có đúng ba câu hỏi. **Ai là client?** Trả lời bằng cách chọn cross-silo hay cross-device, theo bốn trục: số client, độ tin, tính sẵn sàng, tính trạng thái. Chọn sai thì mọi thí nghiệm sau đó mô phỏng một hệ không tồn tại. **Nhãn ở đâu ra?** Trong IDS liên bang, nhãn thường chỉ có ở nơi có đội SOC.

## Ba câu hỏi dựng bài toán (tiếp)
@phut: 1
@che-do: noi

Nên phân vùng thật là **lệch nhãn cực đoan cộng thiếu nhãn**, không phải một Dirichlet đẹp. **Sao không gom dữ liệu về một chỗ?** Đây là câu phản biện kinh điển, và nó là câu DUY NHẤT trong ba câu có thể trả lời bằng con số: byte nếu gom so với byte nếu liên bang. Hai câu đầu trả lời bằng khai báo, nên chúng rẻ và cũng dễ khai sai mà không ai bắt được.

## Ba câu hỏi dựng bài toán (tiếp)
@phut: 1
@che-do: noi

Câu thứ ba đắt hơn nhưng nó là câu duy nhất reviewer kiểm được, nên nó phải có con số và con số đó phải ở trong bài, không ở trong thư trả lời.

## Ba câu hỏi dựng bài toán (tiếp)
@phut: 1
@che-do: noi

Và một cảnh báo về chính con số đó: tỉ số byte **không phụ thuộc số site và số vòng**, nó chỉ phụ thuộc lưu lượng mỗi site chia cho kích thước mô hình. Nên có vùng tham số mà tỉ số tụt xuống dưới {{s001}}, tức gom RẺ HƠN liên bang.

## Ba câu hỏi dựng bài toán (tiếp)
@phut: 1
@che-do: noi

Nếu hệ của anh nằm trong vùng đó thì lập luận băng thông không dùng được, và bài phải quay về lý do pháp lý hoặc độ nhạy, mỗi lý do kèm số riêng của nó.

## Cross-silo và cross-device, bốn trục phân biệt
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Cross-silo và cross-device, bốn trục phân biệt · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bốn trục: **số client** (cross-silo từ hai tới khoảng một trăm, cross-device tới bậc mười luỹ thừa mười), **độ tin** (silo là tổ chức có hợp đồng, device là bên vô danh), **tính sẵn sàng** (silo gần như luôn có, device tham gia từng phần và biến động), **tính trạng thái** (silo giữ được trạng thái giữa các vòng, device thường không).

## Cross-silo và cross-device, bốn trục phân biệt · (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **FL cho IDS ở biên giới tổ chức gần như luôn là cross-silo, và điều đó đổi cả thiết kế thí nghiệm.** Với cross-silo thì mọi site dự mọi vòng, nên lấy mẫu client không khuếch đại riêng tư; số client nhỏ nên điều kiện tồn tại của bộ tổng hợp bền rất chặt; và độ tin cao nên mô hình đe doạ hợp lý là nửa trung thực chứ không phải Byzantine tuỳ ý.

## Cross-silo và cross-device, bốn trục phân biệt · (tiếp)
@phut: 1
@che-do: noi

Một bài khai cross-silo rồi chạy thí nghiệm với một nghìn client lấy mẫu {{s003}} mỗi vòng là bài đang đánh giá chế độ khác chế độ nó khai.

## Vấn đề nhãn trong IDS liên bang
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Vấn đề nhãn trong IDS liên bang · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Lệch nhãn nghĩa là mỗi site có phân bố nhãn khác nhau, nhưng site nào cũng có nhãn. Thiếu nhãn nghĩa là có site KHÔNG có nhãn nào. Hai thứ này khác hẳn nhau về hệ quả.

## Vấn đề nhãn trong IDS liên bang · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **Dirichlet mô hình được lệch nhãn, nhưng không mô hình được thiếu nhãn, nên một bài dùng Dirichlet để biện minh tính thực tế của phân vùng đang bỏ qua đúng phần khó.** Thực tế của IDS: nhãn đến từ đội SOC, và chỉ tổ chức lớn mới có SOC. Nên phân vùng thật là vài site có nhãn tốt, một số site có nhãn thưa và trễ, và phần còn lại không có nhãn.

## Vấn đề nhãn trong IDS liên bang · đáp (tiếp)
@phut: 1
@che-do: noi

Bài toán đúng của trường hợp đó là liên bang bán giám sát hoặc phát hiện bất thường thuần, và quan trọng nhất: **không có nhãn thì không có F1 nào để báo**, kể cả khi mô hình vẫn huấn luyện được.

## Ba lý do chính đáng để không gom
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Ba lý do chính đáng để không gom · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Chỉ có ba lý do chịu được phản biện, và mỗi lý do đòi một loại số khác nhau. **Pháp lý:** đòi một điều khoản cụ thể, có số điều và phạm vi áp dụng. Câu dữ liệu nhạy cảm nên không chia sẻ được là chưa phải lý do. **Khối lượng:** đòi byte mỗi ngày nếu gom so với byte của mô hình nhân số vòng. Đây là lý do duy nhất tính được từ chính bảng tham số của bài.

## Ba lý do chính đáng để không gom · đáp (tiếp)
@phut: 1
@che-do: noi

**Độ nhạy:** đòi loại dữ liệu cụ thể, ví dụ tải nội dung gói (packet) so với siêu dữ liệu luồng (flow), vì hai loại này có mức nhạy khác nhau hẳn. Điểm phải nhớ: **lý do khối lượng là lý do có thể ĐẢO CHIỀU, và nó đảo theo một phân số đơn giản.** Tỉ số byte bằng lưu lượng mỗi site chia hai lần kích thước mô hình, nên mô hình lớn với lưu lượng nhỏ làm liên bang tốn hơn gom.

## Ba lý do chính đáng để không gom · đáp (tiếp)
@phut: 1
@che-do: noi

Một bài dùng lập luận băng thông mà không kiểm phân số đó đang dùng một lý do có thể bị reviewer tính ngược lại trong ba mươi giây.

## Tỉ số byte gom trên byte liên bang
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`byte gom trong D ngày = S·V·D ; byte liên bang trong R vòng = 2·S·R·M ; lấy D = R thì tỉ số = V/(2·M), KHÔNG phụ thuộc S và R`

**Giả thiết nó đứng trên:**

## Tỉ số byte gom trên byte liên bang (tiếp)
@phut: 1
@che-do: so

- S là số site, V là lưu lượng mỗi site mỗi ngày, M là kích thước mô hình, R là số vòng, và một vòng ứng với một ngày
- Không nén, không lọc trước khi gửi, và cập nhật có cùng kích thước với mô hình; nén hoặc lượng tử hoá làm tỉ số tăng, lọc tại nguồn làm tỉ số giảm

## Tỉ số byte gom trên byte liên bang (tiếp)
@phut: 1
@che-do: so

- Mọi site dự mọi vòng, tức chế độ cross-silo; với cross-device lấy mẫu tỉ lệ C thì vế liên bang nhân thêm C
- Hệ số {{s002}} là vì mỗi vòng mỗi site tải mô hình XUỐNG rồi tải cập nhật LÊN; bỏ một chiều là tự cho mình lợi thế gấp đôi

## Tỉ số byte gom trên byte liên bang · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Chỗ đáng chú ý nhất của công thức này là nó rút gọn mất `S` và `R`. Nghĩa là lập luận băng thông KHÔNG mạnh thêm khi có nhiều site hơn hay huấn luyện lâu hơn, và nó chỉ phụ thuộc một phân số duy nhất. Nên nó cũng có thể đảo chiều: với `V` nhỏ và `M` lớn thì liên bang tốn hơn gom.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} | client | Theo bảng phân biệt hai chế độ FL
!so {{s007}} | số mũ của mười | Chế độ cross-device có số client lên tới bậc mười luỹ thừa

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mười site, mỗi site sinh {{s007}} GB mỗi ngày, mô hình {{s008}} MB, huấn luyện {{s006}} vòng với một vòng mỗi ngày. Gom tốn gấp mấy lần liên bang?

soSite = {{s007}}, luuLuong = {{s007}}, soVong = {{s006}}, moHinh = {{s008}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`soSite × luuLuong × soVong / ((soSite × soVong × moHinh + soSite × soVong × moHinh) / {{s009}})`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

{{s010}} lần: gom tốn {{s011}} GB còn liên bang tốn {{s012}} GB. Đây là con số phải có trong bài để trả lời câu phản biện kinh điển. Nhưng phải đọc kèm phép rút gọn: tỉ số bằng lưu lượng chia hai lần kích thước mô hình, nên nó không phụ thuộc số site và không phụ thuộc số vòng. Câu nhiều site thì liên bang càng đáng giá là một câu không có cơ sở trong công thức này.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mỗi site sinh {{s007}} GB mỗi ngày. Mô hình phải lớn tới bao nhiêu MB thì liên bang tốn bằng đúng gom, tức tỉ số byte bằng 1?

luuLuong = {{s007}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`luuLuong × {{s009}} / {{s002}}`

{{s013}} MB, tức một mô hình {{s014}} GB. Con số này là điểm đảo chiều của cả lập luận băng thông: mô hình lớn hơn thế thì gom RẺ HƠN liên bang, và câu trả lời quen thuộc cho câu phản biện không dùng được nữa. Điều kiện tổng quát là lưu lượng mỗi site mỗi ngày nhỏ hơn hai lần kích thước mô hình.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Với mô hình thị giác hay mô hình ngôn ngữ cỡ vài trăm MB tới vài GB đặt cạnh các site chỉ sinh siêu dữ liệu luồng, hệ rơi vào vùng đảo chiều dễ hơn nhiều người tưởng, nên phải kiểm phân số này trước khi viết phần biện minh.

## Một bài khai chế độ cross-silo giữa 8 bệnh viện
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài khai chế độ cross-silo giữa {{s015}} bệnh viện, rồi chạy thí nghiệm với {{s009}} client lấy mẫu {{s003}} mỗi vòng. Hệ quả nghiêm trọng nhất là gì?

## Một bài khai chế độ cross-silo giữa 8 bệnh viện (tiếp)
@phut: 0.5
@che-do: hoi

- Thời gian huấn luyện trong thí nghiệm không khớp thực tế
- Thí nghiệm đánh giá một chế độ khác chế độ đã khai, nên mọi kết luận về bộ tổng hợp bền, về kế toán riêng tư và về tính sẵn sàng đều không chuyển sang được
- Nên dùng FedProx thay vì FedAvg cho cross-silo
- {{s009}} client là quá nhiều để mô phỏng trên một máy

## Một bài khai chế độ cross-silo giữa 8 bệnh viện · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Thí nghiệm đánh giá một chế độ khác chế độ đã khai, nên mọi kết luận về bộ tổng hợp bền, về kế toán riêng tư và về tính sẵn sàng đều không chuyển sang được**

## Một bài khai chế độ cross-silo giữa 8 bệnh viện · (tiếp)
@phut: 1
@che-do: noi

Ba thứ đổi cùng lúc khi đổi chế độ. Điều kiện tồn tại của bộ tổng hợp bền phụ thuộc n, và n bằng {{s015}} chặt hơn n bằng {{s006}} rất nhiều. Kế toán riêng tư phụ thuộc lấy mẫu, mà cross-silo thì mọi site dự mọi vòng nên không có khuếch đại. Và tính sẵn sàng khác hẳn. Phương án A có thật nhưng nhẹ nhất trong các hệ quả.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài khai phân vùng non-IID bằng Dirichlet với alpha = {{s016}} để phản ánh thực tế của IDS liên bang. Phần nào của thực tế mà Dirichlet KHÔNG mô hình được?

- Lệch phân bố nhãn giữa các site
- Lệch số lượng mẫu giữa các site
- Việc có site hoàn toàn KHÔNG có nhãn, vì nhãn đến từ đội SOC mà không site nào cũng có
- Việc các site có kích thước mô hình khác nhau

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Việc có site hoàn toàn KHÔNG có nhãn, vì nhãn đến từ đội SOC mà không site nào cũng có**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Dirichlet sinh ra một phân bố nhãn cho mỗi site, nên nó mô hình được lệch nhãn và lệch số lượng, tức hai phương án đầu. Nó không sinh ra được trạng thái không có nhãn, vì nó luôn gán nhãn cho mọi mẫu. Và đó đúng là phần khó của FL-IDS: thiếu nhãn làm mọi phép đo dựa nhãn mất định nghĩa, còn lệch nhãn chỉ làm chúng khó hơn.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Reviewer hỏi sao không gom dữ liệu về một chỗ. Bài có {{s017}} site, mỗi site sinh {{s012}} MB siêu dữ liệu luồng mỗi ngày, mô hình {{s018}} MB, huấn luyện {{s019}} vòng. Câu trả lời nào đứng được?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Liên bang tiết kiệm băng thông, vì có tới {{s017}} site nên lợi thế càng lớn
- Lập luận băng thông KHÔNG dùng được ở đây vì lưu lượng mỗi site nhỏ hơn hai lần kích thước mô hình, nên phải dùng lý do pháp lý hoặc độ nhạy kèm số riêng
- Liên bang tiết kiệm băng thông, vì chỉ gửi tham số mô hình chứ không gửi dữ liệu thô

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Không cần trả lời, vì FL vốn được chấp nhận trong lĩnh vực này

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Lập luận băng thông KHÔNG dùng được ở đây vì lưu lượng mỗi site nhỏ hơn hai lần kích thước mô hình, nên phải dùng lý do pháp lý hoặc độ nhạy kèm số riêng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Tính nhanh: gom tốn {{s017}} × {{s012}} MB × {{s019}} ngày, tức {{s020}} MB. Liên bang tốn {{s002}} × {{s017}} × {{s019}} × {{s018}} MB, tức {{s021}} MB, gấp {{s022}} lần. Nên lập luận băng thông đang nói NGƯỢC điều bài muốn. Phương án A sai hai lần: tỉ số không phụ thuộc số site, và ở đây nó dưới {{s001}}.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Phương án C mô tả đúng kiến trúc nhưng không trả lời câu hỏi, vì câu hỏi là vì sao chọn kiến trúc đắt hơn về phối hợp.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả thiết lập thí nghiệm sau có một câu khai thiếu đúng một điều, và vì thiếu nó mà cả phần đánh giá không chuyển được sang hệ thật. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi dùng CIC-IDS2017 và chia thành {{s007}} phân vùng theo Dirichlet với alpha = {{s016}}.
- Mỗi phân vùng được coi là một client, và mỗi client giữ {{s023}} dữ liệu của mình để huấn luyện.
- Thiết lập này phản ánh môi trường liên bang thực tế giữa các tổ chức.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Thiết lập này phản ánh môi trường liên bang thực tế giữa các tổ chức.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu đầu là mô tả thiết lập hợp lệ và đầy đủ tham số: cách chia, alpha, số client, tỉ lệ tách. Câu thứ ba là chỗ lỗi, vì nó khai một tính chất mà thiết lập không có. Chia một dataset tập trung theo Dirichlet không sinh ra biên giới tổ chức: nó cho mọi client cùng tập nhãn, cho mọi client nhãn đầy đủ, và cho mọi client cùng phân bố điều kiện.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Ba thứ đó đều sai trong một liên bang IDS thật. Cách sửa rẻ nhất là một câu khai thẳng rằng phân vùng này là mô phỏng chứ không phản ánh biên giới tổ chức, cộng một dòng nói hệ quả nào trong bài phụ thuộc điều đó.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn biện minh sau có một câu sẽ bị reviewer tính ngược lại. Bấm vào câu đó.

- Mười hai site, mỗi site sinh khoảng {{s012}} MB siêu dữ liệu luồng mỗi ngày.
- Mô hình của chúng tôi có {{s018}} MB tham số và huấn luyện trong {{s019}} vòng.
- Do đó học liên bang là lựa chọn phù hợp vì nó giảm đáng kể băng thông so với gom dữ liệu về trung tâm.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Do đó học liên bang là lựa chọn phù hợp vì nó giảm đáng kể băng thông so với gom dữ liệu về trung tâm.**

Hai câu đầu là các con số của chính bài, và chúng đúng. Câu thứ ba là kết luận sai chiều, và nó sai bằng chính hai câu trên: gom tốn {{s017}} × {{s012}} × {{s019}} tức {{s020}} MB, còn liên bang tốn {{s002}} × {{s017}} × {{s019}} × {{s018}} tức {{s021}} MB, gấp {{s022}} lần.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Lưu lượng mỗi site mỗi ngày là {{s012}} MB, nhỏ hơn hai lần kích thước mô hình là {{s024}} MB, nên tỉ số byte nằm dưới {{s001}} và lập luận băng thông đảo chiều. Đây đúng là lớp lỗi kết luận định tính viết trước, còn con số bên cạnh nói ngược. Cách sửa: bỏ lý do băng thông ở trường hợp này và dùng lý do pháp lý hoặc độ nhạy, mỗi lý do kèm số riêng của nó.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Nếu gom: mỗi ngày S site gửi V GB, nên trong D ngày tổng là S·V·D GB
- Nếu liên bang: mỗi vòng mỗi site tải mô hình xuống rồi tải cập nhật lên, nên một vòng tốn 2·S·M
- Trong R vòng, tổng liên bang là 2·S·R·M
- Lấy D = R, tức một vòng mỗi ngày, rồi lập tỉ số: (S·V·R)/(2·S·R·M)
- Rút gọn: tỉ số = V/(2·M), không còn S và không còn R

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: {{s007}} site · {{s007}} GB mỗi site mỗi ngày · mô hình {{s008}} MB · {{s006}} vòng · tỉ số byte gom trên byte liên bang {{s010}} lần · macro-F1 đo được ở từng site vì site nào cũng có nhãn · biên giới client trùng biên giới tổ chức

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mỗi site có nhãn** tắt đi: Chỉ các site có đội SOC mới có nhãn, các site còn lại hoàn toàn không có nhãn nào.
- **Mọi site có cùng tập nhãn tấn công** tắt đi: Mỗi site chỉ thấy một phần các lớp tấn công, ví dụ site nhỏ chưa từng gặp lớp tấn công hiếm nhất.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biên giới client trùng biên giới tổ chức thật** tắt đi: Phân vùng được tạo bằng cách chia một dataset tập trung cho N client theo Dirichlet, không theo tổ chức nào.
- **Lưu lượng thô mỗi ngày lớn hơn hai lần kích thước mô hình** tắt đi: Site nhỏ chỉ sinh vài chục MB siêu dữ liệu luồng mỗi ngày, trong khi mô hình là {{s025}} MB.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Câu trả lời định lượng cho câu phản biện kinh điển. Kéo số site, lưu lượng mỗi site, kích thước mô hình và số vòng, rồi đọc tỉ số byte gom trên byte liên bang. Việc khó của thẻ này không phải đọc con số, mà là tìm vùng tham số nơi câu trả lời quen thuộc ĐẢO CHIỀU.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.8` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section I motivates the federated design by stating that it avoids transferring raw traffic to a central collector. However, Section IV reports {{s017}} sites generating about {{s012}} MB of flow metadata per day each, a {{s018}} MB model, and {{s019}} training rounds. Under these numbers the federated protocol moves roughly fifteen times more data than centralising the logs would. Please justify the architecture with numbers that actually hold for your setting.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer's arithmetic is correct and we have removed the bandwidth argument rather than rewording it. With {{s017}} sites at {{s012}} MB per day, a {{s018}} MB model and {{s019}} rounds, centralising moves {{s026}} GB while our federated protocol moves {{s027}} TB, so bandwidth is an argument against our design, not for it.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Section I now states this explicitly and gives the general condition, namely that the federated protocol is cheaper only when the per-site daily volume exceeds twice the model size, which our setting does not satisfy. The architecture is instead justified on two grounds that do hold. First, legal: the participating sites are governed by data-sharing restrictions that we now cite by article rather than describing in general terms, and we state what those articles do and do not permit for flow metadata. Second, sensitivity:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

flow metadata in our setting contains internal addressing and service topology that the participating organisations treat as confidential even in aggregate, and Section II-B now distinguishes this from packet payload, which is a different sensitivity class and which we never collect. We also state what would make the bandwidth argument valid again: compressing updates by an order of magnitude, or cutting rounds from {{s019}} to {{s008}}, would bring the ratio above one, and we report both as future directions rather than as current properties.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: nhắc lại rằng FL chỉ gửi tham số chứ không gửi dữ liệu thô. Không trả lời được: reviewer không hỏi gửi gì, reviewer đã tính byte và ra con số ngược.
- Mức {{s002}}: thừa nhận tính toán của reviewer và bỏ câu nói FL tiết kiệm băng thông, nhưng không đưa lý do nào khác vào chỗ trống, nên phần động cơ của bài rỗng.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: bỏ lý do băng thông, thay bằng lý do pháp lý hoặc độ nhạy có số cụ thể (điều khoản nào, loại dữ liệu nào), và báo luôn tỉ số byte thật để người đọc thấy bài đã tự kiểm.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The partition is created by splitting CIC-IDS2017 across ten clients with a Dirichlet concentration of {{s028}}, and Section IV calls this representative of a real federation. A Dirichlet split gives every client the full label set with complete labels, whereas in operational intrusion detection labels originate from a security operations team that most sites do not have. Please state what your partition does and does not represent.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced the representativeness claim with an explicit statement of scope, and we have added the experiment that tests it. Section IV-A now says that our Dirichlet partition models label distribution skew and quantity skew only, and that it does not model three properties of an operational federation: sites with no labels at all, sites whose label sets differ, and sites whose conditional distribution differs.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We then added a second partition in which four of the ten sites hold no labels, which matches the situation where only larger organisations run a security operations team. Two findings. First, macro-F1 on the six labelled sites falls from {{s029}} to {{s030}}, so the supervised part degrades but survives. Second, and more important for how the paper reports results, for the four unlabelled sites F1 is not low, it is undefined, because there is no ground truth to score against.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We therefore report a different quantity for those sites, namely the agreement rate between the global model and a local unsupervised detector, and we state clearly that this is a weaker form of evidence rather than an F1 by another name. Section VI now limits our contribution accordingly: the aggregation method we propose is evaluated under label skew, and we do not claim it addresses the missing-label regime, which we identify as the harder open problem.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: nói rằng Dirichlet là quy ước chuẩn của lĩnh vực FL. Đúng về thực hành, không trả lời được: phản biện không hỏi về quy ước mà hỏi về điều bài đã khai, là tính đại diện.
- Mức {{s002}}: sửa câu khai tính đại diện thành một câu thận trọng hơn, nhưng vẫn giữ nguyên mọi con số và mọi kết luận.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai rõ ba thứ phân vùng KHÔNG mô hình được (thiếu nhãn, tập nhãn khác nhau giữa các site, phân bố điều kiện khác nhau), và chỉ ra kết luận nào trong bài phụ thuộc vào ba thứ đó.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table VII averages macro-F1 across the ten clients. Several clients do not contain all attack classes, so per-class recall is undefined for the missing classes at those clients. The paper does not state how such cases enter the macro average. Please specify the convention and report how much the headline number depends on it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We specify the convention and we report its effect, because it turned out to be larger than our reported improvement. Our previous number used the library default, which skips classes absent at a client, so clients that had never seen the rarest attack classes were scored only on the classes they did have. Under the alternative convention, which scores an absent class as zero recall, macro-F1 falls from {{s029}} to {{s032}}, a gap of {{s033}} points.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Since our claimed improvement over the strongest baseline was {{s034}} points, the convention matters more than the contribution, and we now say so in Section V-B. To make the headline number independent of the choice, Table VII now reports per-class precision and recall pooled over the global test set rather than averaged per client, and we keep the two per-client conventions in Appendix D for comparability with prior work.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also re-ran the three baselines under the pooled metric, since comparing our pooled number against their per-client number would be a unit mismatch; under the pooled metric our improvement is {{s035}} points, which we now report as the headline result.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: trả lời rằng macro-F1 được tính bằng hàm có sẵn của thư viện. Không trả lời được: chính thư viện cũng có nhiều cách xử lý lớp vắng mặt, và cách được chọn là một lựa chọn của tác giả.
- Mức {{s002}}: khai quy ước đã dùng, ví dụ coi lớp vắng mặt là {{s031}} hoặc bỏ qua. Trả lời đúng câu đầu nhưng chưa trả lời câu thứ hai, là con số headline phụ thuộc quy ước bao nhiêu.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai quy ước, cộng báo con số dưới CẢ HAI quy ước để người đọc thấy khoảng cách giữa chúng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.8` bấm thẻ.
