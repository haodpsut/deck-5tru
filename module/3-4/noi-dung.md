---
tieu-de: Kiến trúc 3GPP NTN
phu-de: Trụ 3 NTN · module 3.4
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 75.5
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: NTN
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Bài của tôi giả định payload trong suốt (transparent) hay tái sinh, và lựa chọn đó đổi những con số nào trong phần kết quả?

## Một lựa chọn kiến trúc, bốn con số đổi theo
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Trong suốt hay tái sinh không phải chuyện phân loại. Nó là một lựa chọn đổi trực tiếp bốn thứ trong phần kết quả: **trễ truy nhập**, **nơi handover xảy ra**, **chặng nào cần bảo mật**, và **cái gì phải chạy trên quỹ đạo**.

## Một lựa chọn kiến trúc, bốn con số đổi theo (tiếp)
@phut: 1
@che-do: noi

Con số gọn nhất để nhớ: với payload trong suốt, gNB ở mặt đất nên mỗi bit của người dùng đi qua CẢ chặng feeder. Ở cao độ {{s001}} km, với thiết bị ở góc nâng 40° và cổng mặt đất ở góc nâng 10°, RTT lan truyền là **{{s002}} ms** cho trong suốt và **{{s003}} ms** cho tái sinh, tức **{{s004}} lần**. Khoảng cách {{s005}} ms đó đúng bằng hai lần trễ chặng feeder.

## Một lựa chọn kiến trúc, bốn con số đổi theo (tiếp)
@phut: 1
@che-do: noi

Và đây là giả thiết ngầm mà nhiều bài báo NTN không khai: **cổng mặt đất luôn nhìn thấy được từ vệ tinh đang phục vụ**. Với chòm sao không có liên kết giữa vệ tinh (ISL), giả thiết đó sai trong phần lớn quỹ đạo trên biển và trên vùng cực.

## Một lựa chọn kiến trúc, bốn con số đổi theo (tiếp)
@phut: 1
@che-do: noi

Lúc đó RTT của kiến trúc trong suốt không phải lớn hơn, mà **không tồn tại**, và con số khả dụng phải tính theo hình học chòm sao chứ không theo một vệ tinh.

## Khái niệm tầng 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s006}} trên bốn.*

## Khái niệm tầng 1 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Trong suốt:** vệ tinh chỉ đổi tần và khuếch đại, không giải mã. gNB nằm ở mặt đất, nên đường từ thiết bị tới gNB gồm cả chặng dịch vụ và chặng feeder.

**Tái sinh:** gNB nằm trên vệ tinh, nên thiết bị kết thúc giao thức ngay tại vệ tinh. Trễ truy nhập ngắn hơn, nhưng phải có xử lý băng gốc trên quỹ đạo.

## Khái niệm tầng 1 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **chọn trong suốt nghĩa là trễ truy nhập của anh gồm cả chặng feeder**. Đó là một phép cộng, không phải một chi tiết triển khai, nên nó phải xuất hiện trong bảng tham số của bài báo cùng với vị trí cổng mặt đất.

## Ba chặng phải tách trong mọi phép tính
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Ba chặng phải tách trong mọi phép tính · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Liên kết **dịch vụ** (service link): thiết bị tới vệ tinh. Liên kết **feeder**: vệ tinh tới cổng mặt đất. Liên kết **giữa vệ tinh** (ISL): vệ tinh tới vệ tinh, nếu chòm sao có.

Ba chặng có góc nâng khác nhau, băng tần khác nhau, và điều kiện mưa khác nhau. Cổng mặt đất thường có anten lớn và chọn được vị trí khí hậu tốt; thiết bị người dùng thì không.

## Ba chặng phải tách trong mọi phép tính · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **gộp ba chặng thành một con số là mất thông tin không khôi phục được**. Một bảng link budget một cột cho hệ trong suốt là bảng sai cấu trúc, vì người đọc không tách lại được chặng nào đóng góp bao nhiêu dB và bao nhiêu ms.

## Phổ tài liệu 3GPP cho NTN
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Phổ tài liệu 3GPP cho NTN · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`TR {{s008}}` nghiên cứu kênh và kịch bản triển khai. `TR {{s009}}` nghiên cứu giải pháp, tức nơi có các phương án kiến trúc và các vấn đề định thời. `TS {{s010}}` mô tả kiến trúc NR tổng thể, `TS {{s011}}` chứa các tham số định thời gồm `K_offset`. Nhánh IoT-NTN phủ NB-IoT và eMTC.

## Phổ tài liệu 3GPP cho NTN · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **TR là nghiên cứu, TS là đặc tả**. Dẫn một TR để biện hộ cho một tham số triển khai là dẫn sai loại tài liệu, và reviewer biết chuẩn sẽ bắt ngay. Số hiệu và mục của từng tài liệu phải tra lại trước khi vào bài, vì chúng đổi theo Release.

## Giả thiết ngầm: cổng mặt đất luôn nhìn thấy được
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s012}} trên bốn.*

## Giả thiết ngầm: cổng mặt đất luôn nhìn thấy được · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mọi con số trễ của kiến trúc trong suốt đứng trên một điều kiện: vệ tinh đang phục vụ thiết bị đồng thời nhìn thấy một cổng mặt đất. Với chòm sao không có liên kết giữa vệ tinh, điều kiện đó sai trên phần lớn mặt biển và vùng cực.

## Giả thiết ngầm: cổng mặt đất luôn nhìn thấy được (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **khi điều kiện đó sai thì RTT không lớn hơn, nó không tồn tại**, vì không có đường nào từ thiết bị tới gNB. Nên con số khả dụng phải tính theo hình học chòm sao (số vệ tinh, số mặt phẳng, vị trí cổng) chứ không theo một vệ tinh, và bài báo nào im lặng giả định có liên kết giữa vệ tinh thì đang báo một con số của một hệ khác với hệ nó mô tả.

## Trễ theo kiến trúc: trong suốt và tái sinh
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`τ_trong_suốt = (d_dịch_vụ + d_feeder)/c τ_tái_sinh = d_dịch_vụ/c Δτ = d_feeder/c RTT = 2τ`

**Giả thiết nó đứng trên:**

- Chỉ tính trễ lan truyền; trễ xử lý trên quỹ đạo, trễ xếp hàng và trễ mã hoá đều bỏ qua
- Vệ tinh đang phục vụ thiết bị ĐỒNG THỜI nhìn thấy cổng mặt đất, nếu không thì τ_trong_suốt không tồn tại
- Không có liên kết giữa vệ tinh trong đường đi, nếu có thì phải cộng từng chặng ISL

## Trễ theo kiến trúc: trong suốt và tái sinh (tiếp)
@phut: 1
@che-do: so

- d_dịch_vụ và d_feeder đều là khoảng xiên (slant range), tính từ cùng công thức của module {{s013}} với hai góc nâng khác nhau

## Trễ theo kiến trúc: trong suốt và tái sinh · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hệ quả đọc được ngay từ dạng công thức: **trễ thêm của kiến trúc trong suốt đúng bằng trễ chặng feeder**, không phụ thuộc chặng dịch vụ. Nên muốn giảm nó thì đặt cổng mặt đất ở chỗ nhìn vệ tinh với góc nâng cao, chứ không phải cải thiện liên kết người dùng.

## Điều kiện phủ liên tục dọc vệt quỹ đạo
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`N_mặt_phẳng ≥ 360°/(2θ) θ = 90° − ε_min − arcsin( (R_E/(R_E+h))·cos ε_min )`

**Giả thiết nó đứng trên:**

## Điều kiện phủ liên tục dọc vệt quỹ đạo (tiếp)
@phut: 1
@che-do: so

- Chỉ xét phủ dọc vệt quỹ đạo, không xét phủ theo kinh độ, nên đây là điều kiện CẦN chứ không đủ
- Các vệ tinh trên một mặt phẳng cách nhau đều
- Cùng mọi giả thiết hình học của module {{s013}}: quỹ đạo tròn, Trái Đất cầu, đường nhìn thẳng
- ε_min là góc nâng khả dụng, tức đã gồm che chắn địa hình nếu có

## Điều kiện phủ liên tục dọc vệt quỹ đạo · ghi chú
@phut: 1
@che-do: noi

Dùng công thức này để kiểm tính hợp lý của một chòm sao khai trong bài báo: ở h = {{s001}} km với ε_min = 10° thì θ = 14,96°, nên một mặt phẳng cần tối thiểu {{s014}} vệ tinh chỉ để không có khoảng trống dọc vệt. Bài nào khai ít hơn mà vẫn báo phủ liên tục thì đang dựa vào thứ khác, và thứ đó phải được khai.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s015}} | ms | Trễ lan truyền một chiều của chặng feeder
!so {{s016}} | số Release | Bản Release nào của 3GPP đưa NTN vào NR và vào nhánh

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s001}} km, thiết bị ở góc nâng 40°, cổng mặt đất ở góc nâng 10°, payload trong suốt. RTT lan truyền là bao nhiêu ms?

h = {{s001}}, es = {{s017}}, ef = {{s018}}, c = {{s019}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`2⋆((6378⋆(Math.sqrt(Math.pow((6378+h)/6378,2)-Math.pow(Math.cos(es⋆Math.PI/180),2))-Math.sin(es⋆Math.PI/180)))+(6378⋆(Math.sqrt(Math.pow((6378+h)/6378,2)-Math.pow(Math.cos(ef⋆Math.PI/180),2))-Math.sin(ef⋆Math.PI/180))))/c`

Khoảng {{s002}} ms, tức {{s004}} lần RTT {{s003}} ms của kiến trúc tái sinh ở cùng góc nâng dịch vụ. Phần chênh {{s020}} ms đúng bằng hai lần trễ chặng feeder. Con số này mới là con số đi vào ngân sách định thời và vào cấu hình HARQ, chứ không phải {{s003}} ms.

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s001}} km, góc nâng khả dụng tối thiểu 10°. Một mặt phẳng quỹ đạo cần tối thiểu bao nhiêu vệ tinh để không có khoảng trống dọc vệt quỹ đạo?

h = {{s001}}, em = {{s018}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.ceil(360/(2⋆(90-em-180/Math.PI⋆Math.asin(6378/(6378+h)⋆Math.cos(em⋆Math.PI/180)))))`

Đúng {{s014}} vệ tinh, vì {{s021}} chia cho cung nhìn thấy 29,91° cho {{s022}} và phải làm tròn lên. Và đây chỉ là điều kiện CẦN cho một mặt phẳng: nó không nói gì về phủ theo kinh độ, nên tổng số vệ tinh của chòm sao còn nhân thêm số mặt phẳng. Dùng con số này để kiểm nhanh tính hợp lý của một chòm sao khai trong bài báo.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài báo khai payload trong suốt và báo RTT truy nhập {{s023}} ms ở cao độ {{s001}} km. Vấn đề ở đâu?

- Con số chỉ gồm chặng dịch vụ, trong khi trong suốt còn phải cộng chặng feeder
- Thiếu trễ xử lý trên quỹ đạo
- Thiếu suy hao mưa trong phép tính trễ
- Con số quá lớn, trễ ở {{s001}} km phải nhỏ hơn

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Con số chỉ gồm chặng dịch vụ, trong khi trong suốt còn phải cộng chặng feeder**

{{s023}} ms là RTT của chặng dịch vụ ở góc nâng 40°, tức con số của kiến trúc TÁI SINH. Với trong suốt thì gNB ở mặt đất nên còn cộng hai lần trễ feeder, ở góc nâng cổng 10° là {{s005}} ms nữa, thành {{s024}} ms. Trễ xử lý trên quỹ đạo thuộc nhánh tái sinh, còn mưa đổi khả dụng chứ không đổi trễ lan truyền.

## Chòm sao KHÔNG có liên kết giữa vệ tinh
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Chòm sao KHÔNG có liên kết giữa vệ tinh, payload trong suốt, và bài báo báo khả dụng {{s025}} cho dịch vụ trên biển. Dữ kiện nào bắt buộc phải có để kiểm câu đó?

- Số tiến trình HARQ
- Băng thông của chặng feeder
- Vị trí của các cổng mặt đất cùng số vệ tinh và số mặt phẳng quỹ đạo
- Mô hình kênh Rice hay Loo

## Chòm sao KHÔNG có liên kết giữa vệ tinh · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Vị trí của các cổng mặt đất cùng số vệ tinh và số mặt phẳng quỹ đạo**

## Chòm sao KHÔNG có liên kết giữa vệ tinh · đáp (tiếp)
@phut: 1
@che-do: noi

Không có liên kết giữa vệ tinh thì dịch vụ chỉ tồn tại khi một vệ tinh đồng thời thấy thiết bị VÀ thấy một cổng. Điều kiện đó là một bài toán hình học chòm sao: nó cần vị trí cổng, số vệ tinh, số mặt phẳng. Ba phương án kia đều cần cho các con số khác, nhưng không cái nào quyết định được dịch vụ có tồn tại hay không trong một khoảng thời gian.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài so trong suốt với tái sinh và kết luận tái sinh tốt hơn {{s005}} ms. Số hạng nào đang bị bỏ trống khiến kết luận có thể đảo chiều?

- Góc nâng tối thiểu của thiết bị
- Hệ số tái dùng tần số
- Suy hao không gian tự do của chặng feeder
- Trễ xử lý băng gốc trên quỹ đạo của kiến trúc tái sinh

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Trễ xử lý băng gốc trên quỹ đạo của kiến trúc tái sinh**

Lợi thế {{s005}} ms là phép trừ thuần hình học, và nó là lợi thế GỘP chưa trừ chi phí. Tái sinh phải giải mã, định tuyến, mã hoá lại trên quỹ đạo, nên nếu trễ xử lý vượt {{s005}} ms thì kết luận đảo chiều. Ba phương án kia đổi các con số khác nhưng không nằm trong phép trừ này.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả hệ sau có một câu không khớp với kiến trúc đã khai. Bấm vào câu đó.

- Hệ dùng payload trong suốt, gNB đặt tại cổng mặt đất.
- Chòm sao ở cao độ {{s001}} km, thiết bị phục vụ từ góc nâng 40° trở lên.
- Trễ truy nhập một chiều do đó là {{s026}} ms, lấy từ khoảng xiên {{s027}} km ở góc nâng 40°.
- Bảng tham số khai băng tần feeder và băng tần dịch vụ riêng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Trễ truy nhập một chiều do đó là {{s026}} ms, lấy từ khoảng xiên {{s027}} km ở góc nâng 40°.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai dòng đầu khai đúng và đủ. Dòng thứ ba lấy trễ của CHẶNG DỊCH VỤ làm trễ truy nhập, nhưng với payload trong suốt thì gNB ở mặt đất nên đường từ thiết bị tới gNB còn đi tiếp qua chặng feeder. Ở cao độ {{s001}} km với cổng nhìn vệ tinh ở góc nâng 10°, trễ feeder là {{s028}} ms, nên trễ truy nhập một chiều là {{s029}} ms và RTT là {{s002}} ms chứ không phải {{s003}} ms. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

tách hai chặng thành hai dòng, khai góc nâng của cổng mặt đất, rồi cộng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đánh giá sau có một câu dựa trên một giả thiết không được khai ở đâu trong bài. Bấm vào câu đó.

- Chòm sao mô phỏng gồm {{s007}} mặt phẳng, mỗi mặt {{s030}} vệ tinh ở cao độ {{s001}} km, không có liên kết giữa vệ tinh.
- Có hai cổng mặt đất, cả hai ở châu Âu.
- Kết quả cho khả dụng {{s025}} cho thiết bị trên Thái Bình Dương, với RTT trung bình {{s024}} ms.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Kết quả cho khả dụng {{s025}} cho thiết bị trên Thái Bình Dương, với RTT trung bình {{s024}} ms.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai dòng đầu là dữ kiện, và chính chúng làm dòng thứ ba không thể đúng. Không có liên kết giữa vệ tinh thì dịch vụ chỉ tồn tại khi một vệ tinh ĐỒNG THỜI thấy thiết bị và thấy một cổng; với cả hai cổng ở châu Âu thì vệ tinh trên Thái Bình Dương không thấy cổng nào, nên trong khoảng đó RTT không phải lớn hơn mà KHÔNG TỒN TẠI.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Khả dụng {{s025}} ở đó chỉ dựng lại được nếu ngầm giả định có liên kết giữa vệ tinh, và giả thiết đó không khai ở đâu. Cách sửa: hoặc khai liên kết giữa vệ tinh thành một thành phần của hệ cùng số chặng và trễ từng chặng, hoặc báo khả dụng theo vùng địa lý và nói rõ vùng nào không có dịch vụ.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Tính khoảng xiên chặng dịch vụ d_s = d(h, ε_s) bằng công thức khoảng xiên của module {{s013}}
- Tính khoảng xiên chặng feeder d_f = d(h, ε_f) bằng CÙNG công thức, với góc nâng của cổng mặt đất
- Đường từ thiết bị tới gNB đi qua cả hai chặng, vì gNB ở mặt đất: τ = (d_s + d_f)/c
- Nhân hai để ra trễ vòng: RTT = 2(d_s + d_f)/c

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- So với kiến trúc tái sinh RTT = 2d_s/c, phần chênh là 2d_f/c, tức đúng hai lần trễ chặng feeder

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: h {{s001}} km · ε_s 40° · ε_f 10° → trễ dịch vụ {{s031}} ms · trễ feeder {{s032}} ms · RTT tái sinh {{s033}} ms · RTT trong suốt {{s034}} ms · tỉ lệ feeder {{s035}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Cổng mặt đất luôn nhìn thấy được từ vệ tinh đang phục vụ** tắt đi: Chòm sao không có liên kết giữa vệ tinh, và vệ tinh đang phục vụ thiết bị không đồng thời thấy cổng nào. Trường hợp này xảy ra trên phần lớn mặt biển và vùng cực.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Trễ xử lý trên vệ tinh bỏ qua được** tắt đi: Kiến trúc tái sinh phải giải mã, định tuyến và mã hoá lại trên quỹ đạo, nên cộng thêm trễ xử lý.
- **Một cổng mặt đất duy nhất và cố định** tắt đi: Nhiều cổng mặt đất, và vệ tinh chuyển cổng theo quỹ đạo, nên góc nâng feeder đổi liên tục.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Chặng feeder và chặng dịch vụ cùng điều kiện truyền** tắt đi: Hai chặng khác băng tần (feeder thường Ka hoặc cao hơn, dịch vụ có thể S hoặc Ka) và khác điều kiện mưa, vì cổng chọn được vị trí khí hậu còn thiết bị thì không.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Hai chặng, hai kiến trúc, một bảng. Kéo cao độ, góc nâng thiết bị và góc nâng cổng mặt đất, rồi đọc RTT của cả hai kiến trúc cạnh nhau cùng tỉ lệ mà chặng feeder chiếm.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.4` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III declares a transparent payload, yet Table III reports a one-way access delay of {{s037}} ms, which corresponds to the service link alone. Please state where the gNB is located, report the feeder link separately, and give the elevation assumed for the gateway.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The gNB is located at the gateway, so the payload is transparent and the access path traverses both the service and the feeder link. Table III has been split accordingly. For h = {{s001}} km, a service elevation of {{s017}} degrees and a gateway elevation of {{s018}} degrees, the one-way propagation delays are {{s038}} ms on the service link and {{s039}} ms on the feeder link, giving {{s040}} ms one way and an access RTT of {{s041}} ms.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The previously reported {{s042}} ms RTT is the regenerative figure and we have corrected every place in the paper that used it, including the HARQ configuration of Section VI, where the number of processes was sized for the shorter value. Because the constellation uses several gateways, the feeder delay is a distribution rather than a constant; Table III now reports the median and the worst served case, and states which one each later figure uses.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, the architecture comparison of Section VII no longer presents the {{s043}} ms difference as a net gain for the regenerative option: that figure is the geometric gross gain, and the on-board baseband processing delay subtracts from it directly, so we now give that delay with its source and state the threshold at which the conclusion reverses.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s006}}: trả lời rằng {{s026}} ms là trễ lan truyền ở góc nâng 40° và cao độ {{s001}} km. Đúng về số học của một chặng, không trả lời được điều reviewer hỏi.
- Mức {{s007}}: thêm trễ chặng feeder dạng một con số gộp vào tổng, nhưng không khai góc nâng của cổng mặt đất nên con số không dựng lại được.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s036}}: tách bảng thành hai chặng, khai góc nâng của cổng, báo cả trễ một chiều và RTT cho cả hai kiến trúc, và sửa mọi chỗ trong bài dùng con số cũ.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The constellation in Section V has no inter-satellite links and two gateways, both in Europe, yet Table VI reports {{s044}} percent availability for maritime users in the Pacific. Please explain how service is maintained when the serving satellite sees no gateway.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We thank the reviewer, this exposed an unstated assumption. With no inter-satellite links the service condition is not one of visibility but two simultaneous ones: the serving satellite must see the user and must also see a gateway. With both gateways in Europe this condition fails over the Pacific, so in those intervals there is no path from the user to the gNB at all.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The reported availability was therefore computed on the service link alone, which is the wrong condition for a transparent architecture. Section V has been recomputed from the constellation geometry with the real gateway locations, and Table VI now reports availability per region rather than as a single global number, naming explicitly the longitude bands where the service does not exist. We also corrected a second defect that followed from the first:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the intervals without a path were previously entering the delay average as large values, whereas an undefined RTT must be excluded from the average and reported separately as outage, not as latency. Where the intended system does rely on inter-satellite links, as the Pacific scenario does, the model now includes them with the number of hops and the per hop propagation delay, and the resulting RTT is reported as a distribution over hop counts.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s006}}: trả lời rằng chòm sao có đủ vệ tinh để luôn có một vệ tinh trên đầu người dùng. Đúng về chặng dịch vụ, bỏ mất chặng feeder nên không trả lời được điều reviewer hỏi.
- Mức {{s007}}: thừa nhận cần cổng mặt đất và thêm một cổng giả định ở Thái Bình Dương, nhưng không tính lại con số khả dụng theo hình học mới.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s036}}: khai rõ điều kiện dịch vụ là một vệ tinh đồng thời thấy thiết bị VÀ thấy một cổng, rồi tính lại khả dụng theo hình học chòm sao và vị trí cổng thật, báo theo vùng địa lý.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.4` bấm thẻ.
