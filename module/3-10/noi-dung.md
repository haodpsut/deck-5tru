---
tieu-de: Học liên bang qua liên kết vệ tinh: khi vòng huấn luyện gặp cửa sổ nhìn thấy
phu-de: Trụ 3 NTN · module 3.10
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
@phan: NTN
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Với cửa sổ nhìn thấy (visibility window) {{s001}} phút và mô hình {{s002}} MB, một ngày tôi chạy được bao nhiêu vòng, và con số đó có đủ để hội tụ không?

## Cửa sổ nhìn thấy là một ràng buộc về BYTE
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này là giao điểm của trụ {{s003}} với trụ {{s004}}, và nó chỉ có một ý trung tâm: **cửa sổ nhìn thấy không phải một ràng buộc về thời gian, nó là một ràng buộc về byte**. Một liên kết mở trong `t_vis` giây ở thông lượng `R` chở được đúng `R·t_vis` bit, không hơn. Ở {{s005}} km với góc nâng tối thiểu {{s006}} độ thì `t_vis` là **{{s001}} phút**, nên ở {{s006}} Mbps một lượt qua chở được **{{s007}} MB**.

## Cửa sổ nhìn thấy là một ràng buộc về BYTE (tiếp)
@phut: 1
@che-do: noi

Hệ quả làm đổi cách đọc mọi bài nén trong học liên bang (federated learning). Số lượt qua cần cho một vòng là `ceil(byte một vòng / byte một lượt qua)`, và hàm `ceil` đó biến nén từ **một đánh đổi liên tục** thành **một ngưỡng rời rạc**: nén chỉ đổi được tiến độ khi nó vượt qua một bậc, và khi số lượt qua về {{s008}} thì nén thêm mua được đúng {{s009}}.

## Cửa sổ nhìn thấy là một ràng buộc về BYTE (tiếp)
@phut: 1
@che-do: noi

Hệ quả thứ hai nặng hơn, và nó nằm ở tầng {{s010}}. Ghép với module {{s011}}: ở đây **kẻ chậm (straggler) không phải thiết bị yếu, nó là hình học quỹ đạo**. Số lượt qua mỗi ngày của một client là hàm của vĩ độ, nên trọng số hiệu dụng (effective weight) trong tổng hợp lệch theo vĩ độ. Và vì phân bố dữ liệu cũng lệch theo vĩ độ, hai nguồn lệch **cộng hưởng chứ không triệt tiêu**.

## Cửa sổ nhìn thấy là một ràng buộc về BYTE (tiếp)
@phut: 1
@che-do: noi

Đúng điều kiện làm giả thiết lấy mẫu không chệch sụp.

Một cảnh báo về chính module này: **số lượt qua mỗi ngày là con số tôi KHÔNG khai**. Nó phụ thuộc chòm sao (constellation), độ nghiêng quỹ đạo và vĩ độ client. Trong mô phỏng nó là một thanh kéo mà người học phải tự đặt, chứ không phải một hằng số tôi gài sẵn.

## Ngân sách byte một lượt qua (per-pass byte budget)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Ngân sách byte một lượt qua (per-pass byte budget) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`B_lượt = R · t_vis(h, ε_min)`. Đơn vị phải khớp: {{s006}} Mbps trong {{s012}} giây cho {{s007}} MB.

## Ngân sách byte một lượt qua (per-pass byte (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **một mẹo đổi đơn vị nên thuộc lòng là {{s013}} Mbps đúng bằng {{s008}} MB mỗi giây**. Nên ở {{s013}} Mbps, số MB chở được trong một lượt qua bằng đúng số GIÂY của cửa sổ, tức {{s012}} MB ở {{s005}} km. Phép kiểm này bắt được mọi lỗi lệch hệ số {{s013}} giữa bit và byte, và lỗi đó là lỗi hay gặp nhất trong bảng ngân sách truyền (communication budget) của bài học liên bang qua vệ tinh.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Số lượt qua cần cho một vòng là `n_lượt = ceil(B_vòng / B_lượt)` với `B_vòng = 2·S/ρ`. Hàm `ceil` làm nó thành hàm bậc thang theo tỉ lệ nén `ρ`.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **nén là một ngưỡng, không phải một đánh đổi liên tục**, và nó có SÀN bằng {{s008}} lượt qua. Ở thông lượng {{s014}} Mbps với ResNet-18 fp32, tỉ số thô là {{s015}} nên cần {{s016}} lượt qua; sàn đạt tại `ρ` bằng {{s015}}. Mọi tỉ lệ nén lớn hơn {{s015}} cho đúng {{s008}} lượt qua và đúng cùng một tiến độ, trong khi vẫn phải trả giá về chất lượng cập nhật.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Nên câu *nén mạnh hơn thì hội tụ nhanh hơn* sai ở hai đầu: dưới ngưỡng nó không đổi gì, trên sàn nó không mua gì.

## Kẻ chậm là hình học, và nó tương quan với dữ liệu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s010}} trên bốn.*

## Kẻ chậm là hình học, và nó tương quan với dữ liệu · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Số lượt qua mỗi ngày của một client là hàm của vĩ độ client và của độ nghiêng quỹ đạo. Client ở vĩ độ cao có nhiều lượt qua hơn client ở xích đạo, nên nó gửi được nhiều vòng hơn trong cùng một khoảng thời gian.

## Kẻ chậm là hình học, và nó tương quan với dữ liệu (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **trọng số HIỆU DỤNG là trọng số khai nhân số lần được tính**. Tổng hợp theo số mẫu vẫn lệch theo vĩ độ nếu số lần tham gia lệch theo vĩ độ. Và vì phân bố dữ liệu của mạng phi mặt đất (non-terrestrial network) cũng lệch theo vĩ độ, hai nguồn lệch cộng hưởng. Hệ quả cho bài báo:

## Kẻ chậm là hình học, và nó tương quan với dữ liệu (tiếp)
@phut: 1
@che-do: noi

lấy mẫu client đều theo diện tích là chưa đủ, và câu *mô hình toàn cục đại diện cho toàn mạng* không phải một con số xấu hơn, nó là một tuyên bố không còn tổng thể nào để quy chiếu.

## Ngân sách byte một lượt qua
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`B_lượt = R·t_vis(h, ε_min) B_vòng = 2·S/ρ n_lượt = ceil( B_vòng / B_lượt ) N_vòng = N_lượt / n_lượt ngày = V_mục tiêu / N_vòng`

**Giả thiết nó đứng trên:**

## Ngân sách byte một lượt qua (tiếp)
@phut: 1
@che-do: so

- Thông lượng R không đổi suốt lượt qua, và toàn bộ cửa sổ nhìn thấy dùng được cho dữ liệu mô hình, tức không trừ thời gian bắt liên kết, báo hiệu và giao thức
- Một vòng gồm đúng hai lần truyền một chiều, mô hình toàn cục xuống và cập nhật lên, cả hai cùng chịu tỉ lệ nén ρ và cùng rút từ một ngân sách byte

## Ngân sách byte một lượt qua (tiếp)
@phut: 1
@che-do: so

- Một vòng được phép TRẢI QUA nhiều lượt qua, tức cập nhật chờ giữa các lượt vẫn được bộ tổng hợp nhận chứ không bị coi là lạc hậu
- N_lượt, số lượt qua mỗi ngày, PHẢI KHAI: nó phụ thuộc chòm sao, độ nghiêng quỹ đạo và vĩ độ client, không dẫn được từ cao độ một mình

## Ngân sách byte một lượt qua (tiếp)
@phut: 1
@che-do: so

- Tốc độ hội tụ khai sẵn qua V_mục tiêu, và nó độc lập với tỉ lệ nén, tức bỏ qua chuyện nén mạnh làm cần nhiều vòng hơn
- t_vis lấy nguyên từ module {{s017}}, tức cửa sổ của lượt qua đúng đỉnh đầu, nên nó là CHẶN TRÊN chứ không phải cửa sổ trung bình

## Ngân sách byte một lượt qua · ghi chú
@phut: 1
@che-do: noi

Hai phép kiểm bắt buộc. Một, đổi đơn vị: {{s013}} Mbps đúng bằng {{s008}} MB mỗi giây, nên ở {{s013}} Mbps số MB chở được bằng đúng số giây của cửa sổ, {{s012}} MB ở {{s005}} km. Hai, biên: cho thông lượng rất lớn thì `B_vòng/B_lượt` về {{s009}} nhưng `ceil` chặn ở {{s008}}, nên một vòng vẫn cần đúng {{s008}} lượt qua. Chính cái sàn đó là chỗ nén hết tác dụng, và nó phải nằm trong bài báo chứ không nằm ngoài.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s018}} | phút | Cửa sổ nhìn thấy lớn nhất của một lượt qua ở cao
!so {{s019}} | MB | Kích thước một chiều của ResNet-18 ở độ chính xác fp32
!so {{s007}} | MB | Byte chuyển được trong một lượt qua dài {{s001}} phút ở thông

## Cao độ 1200 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s020}} km, góc nâng tối thiểu {{s006}} độ, thông lượng liên kết {{s003}} Mbps. Byte chuyển được trong một lượt qua đỉnh đầu là bao nhiêu MB?

mbps = {{s003}}, h = {{s020}}, em = {{s006}}

## Cao độ 1200 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`mbps⋆(2⋆(90-em-180/Math.PI⋆Math.asin(6378/(6378+h)⋆Math.cos(em⋆Math.PI/180)))/360)⋆2⋆Math.PI⋆Math.sqrt(Math.pow((6378+h)⋆1e3,3)/3.986e14)/60⋆60/8`

Khoảng {{s021}} MB. Ở {{s005}} km với cùng {{s003}} Mbps chỉ được {{s022}} MB, nên lên cao {{s023}} lần theo cao độ mua được {{s024}} lần ngân sách byte, đúng bằng tỉ số cửa sổ {{s025}} phút trên {{s001}} phút. Ngân sách byte tỉ lệ TUYẾN TÍNH với cửa sổ, còn cửa sổ tăng dưới tuyến tính theo cao độ. Và đây là một đánh đổi phải khai, không phải một món quà:

## Cao độ 1200 km · đáp (tiếp)
@phut: 1
@che-do: noi

module {{s017}} cho thấy lên {{s020}} km làm trễ ở đỉnh đầu đi từ {{s026}} ms lên {{s027}} ms, nên mua byte bằng cao độ là bán trễ.

## Thông lượng 0,2 Mbps
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Thông lượng {{s029}} Mbps, cửa sổ ở cao độ {{s005}} km với góc nâng tối thiểu {{s006}} độ, mô hình {{s002}} MB một chiều, không nén. Một vòng cần bao nhiêu lượt qua?

mbps = {{s028}}, sz = {{s019}}, nen = {{s008}}, h = {{s005}}, em = {{s006}}

## Thông lượng 0,2 Mbps · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.ceil(2⋆sz/nen/(mbps⋆(2⋆(90-em-180/Math.PI⋆Math.asin(6378/(6378+h)⋆Math.cos(em⋆Math.PI/180)))/360)⋆2⋆Math.PI⋆Math.sqrt(Math.pow((6378+h)⋆1e3,3)/3.986e14)/60⋆60/8))`

Đúng {{s013}} lượt qua. Tỉ số thô là {{s030}}, tức {{s031}} MB một vòng chia {{s032}} MB một lượt qua, và phần dư kéo lên {{s013}} vì không có lượt qua lẻ. Chính hàm trần đó là chỗ sinh ra toàn bộ tính RỜI RẠC của bài toán: giữa hai bậc, giảm byte một vòng không đổi được tiến độ một chút nào, còn ngay tại một bậc thì nó đổi hẳn một đơn vị.

## Thông lượng 0,2 Mbps · đáp (tiếp)
@phut: 1
@che-do: noi

Nên câu nói nén cho một đánh đổi liên tục giữa băng thông và tiến độ là câu nói sai về cấu trúc, không phải sai về độ lớn.

## Thông lượng 0,05 Mbps
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Thông lượng {{s014}} Mbps, cửa sổ ở cao độ {{s005}} km với góc nâng tối thiểu {{s006}} độ, mô hình {{s002}} MB một chiều, không nén, và {{s034}} lượt qua mỗi ngày khai sẵn. Cần bao nhiêu ngày để chạy xong {{s035}} vòng?

mbps = {{s033}}, sz = {{s019}}, nen = {{s008}}, h = {{s005}}, em = {{s006}}, luot = {{s034}}, vong = {{s035}}

## Thông lượng 0,05 Mbps · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`vong⋆Math.ceil(2⋆sz/nen/(mbps⋆(2⋆(90-em-180/Math.PI⋆Math.asin(6378/(6378+h)⋆Math.cos(em⋆Math.PI/180)))/360)⋆2⋆Math.PI⋆Math.sqrt(Math.pow((6378+h)⋆1e3,3)/3.986e14)/60⋆60/8))/luot`

Đúng {{s036}} ngày, tức {{s037}} năm cho một lần huấn luyện {{s035}} vòng. Đây là con số phải nằm trong bài báo, và nó là con số mà một bảng kết quả chỉ báo độ chính xác theo số vòng không hề cho thấy. Nén {{s015}} lần đưa số lượt qua cho một vòng từ {{s016}} về {{s008}}, nên {{s036}} ngày thành {{s038}} ngày; nén thêm nữa không bớt được một ngày nào vì sàn của hàm trần là {{s008}} lượt qua.

## Thông lượng 0,05 Mbps · đáp (tiếp)
@phut: 1
@che-do: noi

Cách khai đúng trong bài: trục hoành của hình hội tụ ghi thêm THỜI GIAN THẬT cạnh số vòng, với ngân sách truyền và số lượt qua mỗi ngày khai rõ.

## Ở cấu hình mặc định của mô phỏng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Ở cấu hình mặc định của mô phỏng, tăng tỉ lệ nén từ {{s016}} lên {{s040}} làm số vòng mỗi ngày (mean motion) đổi thế nào?

- Tăng khoảng {{s039}} lần
- Không đổi, vì một vòng đã vừa khít một lượt qua từ tỉ lệ nén {{s015}}
- Tăng đúng {{s040}} lần
- Giảm, vì nén mạnh làm cập nhật kém giá trị hơn

## Ở cấu hình mặc định của mô phỏng · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Không đổi, vì một vòng đã vừa khít một lượt qua từ tỉ lệ nén {{s015}}**

## Ở cấu hình mặc định của mô phỏng · đáp (tiếp)
@phut: 1
@che-do: noi

Số lượt qua cần cho một vòng là ceil(2S/ρ chia byte một lượt qua), và nó có SÀN bằng {{s008}}. Ở cấu hình mặc định sàn đó đạt tại tỉ lệ nén {{s015}}, nên mọi giá trị lớn hơn cho đúng {{s008}} lượt qua và đúng {{s034}} vòng mỗi ngày. Nén thêm không mua được gì về tiến độ. Chuyện cập nhật kém giá trị hơn là thật nhưng nó nằm ngoài mô phỏng này:

## Ở cấu hình mặc định của mô phỏng · đáp (tiếp)
@phut: 1
@che-do: noi

mô phỏng chỉ đo ngân sách truyền, nên nó không bao giờ cho số vòng mỗi ngày giảm, và đó chính là giới hạn phải tự khai khi dùng nó.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bỏ giả thiết mọi client có cùng số lượt qua mỗi ngày. Phát biểu nào MẤT NGHĨA, chứ không chỉ đổi số?

- Byte chuyển được trong một lượt qua
- Số lượt qua cần cho một vòng của một client
- Số ngày để một client cụ thể chạy xong {{s035}} vòng
- Mô hình toàn cục đại diện cho toàn mạng

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Mô hình toàn cục đại diện cho toàn mạng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ba đại lượng kia vẫn tính được cho từng client nếu khai số lượt qua của chính client đó, nên chúng chỉ đổi số. Cái mất nghĩa là tuyên bố về tính đại diện: số lượt qua lệch theo vĩ độ nên trọng số hiệu dụng trong tổng hợp lệch theo vĩ độ, và vì phân bố dữ liệu cũng lệch theo vĩ độ thì không còn tổng thể nào để mô hình quy chiếu tới.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là chỗ giả thiết lấy mẫu không chệch của học liên bang sụp vì HÌNH HỌC QUỸ ĐẠO, không vì thiết bị yếu, nên nó không sửa được bằng cách chờ thiết bị chậm.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn ngân sách truyền sau có một dòng làm mất đúng tính chất quan trọng nhất của bài toán. Bấm vào dòng đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Mỗi client có cửa sổ nhìn thấy {{s001}} phút ở cao độ {{s005}} km với góc nâng tối thiểu {{s006}} độ.
- Ở thông lượng {{s014}} Mbps, một lượt qua chuyển được {{s041}} MB.
- ResNet-18 fp32 một chiều là {{s002}} MB, nên một vòng gồm mô hình xuống và cập nhật lên tốn {{s031}} MB.
- Vậy một vòng cần {{s015}} lượt qua, và với {{s034}} lượt qua mỗi ngày thì được {{s042}} vòng mỗi ngày.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vậy một vòng cần {{s015}} lượt qua, và với {{s034}} lượt qua mỗi ngày thì được {{s042}} vòng mỗi ngày.**

Số lượt qua là số nguyên, nên phải lấy TRẦN: {{s015}} kéo lên {{s016}}, và số vòng mỗi ngày là {{s034}} chia {{s016}} bằng {{s043}} chứ không phải {{s042}}. Sai số {{s044}} nghe nhỏ, nhưng thứ bị mất không phải {{s044}}: bỏ hàm trần là bỏ toàn bộ tính RỜI RẠC của bài toán.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Có hàm trần thì giảm byte một vòng chỉ đổi được tiến độ khi nó vượt qua một bậc, và khi số lượt qua về {{s008}} thì nén thêm mua được đúng {{s009}}. Không có hàm trần thì nén thành một đánh đổi liên tục và mọi kết luận về ngưỡng nén biến mất. Ba mệnh đề đầu đều đúng. Cách sửa: viết ceil, rồi vẽ số vòng mỗi ngày theo tỉ lệ nén để các bậc hiện ra.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết lập thí nghiệm sau có một câu không dẫn ra được từ hai câu trước. Bấm vào câu đó.

- Chúng tôi lấy mẫu {{s040}} client phân bố đều theo diện tích trên mặt cầu.
- Mỗi vòng, bộ tổng hợp nhận mọi cập nhật đến trong {{s045}} giờ và lấy trung bình có trọng số theo số mẫu của client.
- Vì client được lấy mẫu đều theo diện tích, mô hình toàn cục không chệch theo vùng địa lý.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì client được lấy mẫu đều theo diện tích, mô hình toàn cục không chệch theo vùng địa lý.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Lấy mẫu client đều không đủ. Số lượt qua mỗi ngày của một client là hàm của vĩ độ client và của độ nghiêng quỹ đạo, nên client ở vĩ độ cao gửi được nhiều cập nhật hơn client ở xích đạo trong cùng {{s045}} giờ. Trọng số HIỆU DỤNG là trọng số khai nhân số lần được tính, nên nó lệch theo vĩ độ dù trọng số khai chỉ theo số mẫu.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Và vì phân bố dữ liệu của mạng phi mặt đất cũng lệch theo vĩ độ, hai nguồn lệch cộng hưởng chứ không triệt tiêu. Hai mệnh đề đầu là mô tả thiết lập và hoàn toàn hợp lệ. Cách sửa: đo và khai số lượt qua theo dải vĩ độ, rồi hoặc chuẩn hoá trọng số theo số lần tham gia, hoặc báo kết quả theo dải vĩ độ thay cho một con số toàn mạng. Lưu ý:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

số lượt qua mỗi ngày là con số module này cố tình KHÔNG khai, vì nó phụ thuộc chòm sao cụ thể.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Ngân sách byte một lượt qua (per-pass byte budget): B_lượt = R·t_vis, với t_vis lấy từ hình học quỹ đạo theo cao độ và góc nâng tối thiểu
- Byte một vòng: B_vòng = 2·S/ρ, mô hình xuống và cập nhật lên, cùng tỉ lệ nén
- Số lượt qua cần cho một vòng: n_lượt = ceil(B_vòng/B_lượt), lấy trần vì không có lượt qua lẻ

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Số vòng mỗi ngày: N_vòng = N_lượt/n_lượt, với N_lượt PHẢI KHAI vì nó phụ thuộc chòm sao và vĩ độ client
- Số ngày: ngày = V_mục tiêu/N_vòng, với V_mục tiêu là số vòng khai sẵn để đạt mục tiêu chất lượng

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: R {{s014}} Mbps · cửa sổ {{s001}} phút · S {{s002}} MB một chiều · ρ {{s008}} · {{s034}} lượt qua mỗi ngày khai sẵn → byte một lượt qua {{s041}} MB · {{s016}} lượt qua cho một vòng · {{s043}} vòng mỗi ngày · {{s036}} ngày cho {{s035}} vòng

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi client có cùng số lượt qua mỗi ngày** tắt đi: Số lượt qua mỗi ngày là hàm của vĩ độ client và độ nghiêng quỹ đạo, nên client ở vĩ độ cao có nhiều lượt qua hơn hẳn client ở xích đạo.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Một vòng dùng đúng hai lần truyền, lên và xuống, cùng ngân sách byte** tắt đi: Mô hình toàn cục đi xuống bằng quảng bá nên không rút từ ngân sách của client, hoặc ngược lại đường xuống nghẽn hơn đường lên.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Toàn bộ cửa sổ nhìn thấy dùng được cho dữ liệu mô hình** tắt đi: Phải trừ thời gian bắt liên kết, đồng bộ, báo hiệu và truyền lại, nên phần cửa sổ chở được dữ liệu nhỏ hơn cửa sổ hình học.
- **Một vòng được phép trải qua nhiều lượt qua** tắt đi: Cập nhật phải hoàn tất trong một lượt qua, vì bộ tổng hợp coi cập nhật chờ qua nhiều lượt là lạc hậu và loại nó.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bảng trọng số của torchvision niêm yết ResNet-18 ở {{s046}} MB, nên lượng truyền một chiều mỗi vòng cũng là {{s046}} MB.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỔ**

ĐỔ ở nửa sau, dù nửa đầu trích đúng. Bảng thật in File size {{s046}} MB, và con số đó là kích thước tệp .pth tính theo MiB, tức một đại lượng khác với lượng truyền tham số. Bảng cũng in num_params {{s047}}; ở fp32 thì {{s047}} × {{s010}} = {{s048}} byte, tức {{s002}} MB theo MB thập phân. Hai con số lệch nhau vì MB và MiB, và vì tệp .pth còn nén cùng siêu dữ liệu.

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

Khai lượng truyền thì phải nói rõ đang dùng đơn vị nào.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bảy thanh kéo, năm con số. Kéo thông lượng, kích thước mô hình, tỉ lệ nén, cao độ, góc nâng tối thiểu, số lượt qua mỗi ngày và số vòng mục tiêu. Đồ thị là số vòng mỗi ngày theo tỉ lệ nén, và nó là một bậc thang chứ không phải một đường trơn.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.10` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Fig. {{s013}} shows accuracy against communication rounds and Section VI states convergence at {{s035}} rounds. Over the satellite link described in Section III, please state how long {{s035}} rounds actually take in wall clock time, state the per pass byte budget that follows from your visibility window and link rate, and state whether a single round fits inside one pass.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have added the wall clock budget, which was indeed missing. With h = {{s005}} km and a {{s006}} degree minimum elevation, the zenith pass visibility window is {{s018}} minutes, that is {{s049}} seconds, and we now state in Table I that this is an upper bound for a zenith pass, not a mean over passes. At the {{s033}} Mbps uplink of Section III, and noting that {{s013}} Mbps equals {{s008}} MB per second, one pass carries {{s050}} MB.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

One uncompressed round of ResNet-18 at fp32 costs {{s019}} MB in each direction, so {{s051}} MB per round, which requires ceil(93.52 / {{s050}}) = {{s016}} passes. At the {{s034}} passes per day we assume for the client latitudes in Section III, and we now state that assumption explicitly because the pass count depends on the constellation and on client latitude, this gives {{s052}} rounds per day and {{s036}} days, about {{s053}} years, for {{s035}} rounds. Fig.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

{{s013}} now carries a second horizontal axis in days alongside the round axis. Section VI-C adds the point this exposes: compression here is not a continuous cost accuracy tradeoff but a discrete threshold, because the pass count is a ceiling function with a floor of one. At this configuration the floor is reached at a compression ratio of {{s054}}, which brings {{s035}} rounds down to {{s038}} days, and any ratio beyond {{s054}} buys exactly nothing in schedule while still costing update quality.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also now report the protocol efficiency we assume, and show that removing {{s055}} percent of the window for acquisition and signalling moves the figure from {{s036}} to {{s056}} days.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s008}}: trả lời rằng số vòng là trục tiêu chuẩn trong tài liệu học liên bang và chi phí truyền đã được bàn định tính. Đúng về thực hành, không trả lời được điều reviewer hỏi.
- Mức {{s003}}: tính ra tổng byte phải truyền cho {{s035}} vòng, nhưng vẫn không chuyển nó thành thời gian thật và vẫn không nói một vòng có vừa một lượt qua hay không.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai ngân sách byte một lượt qua từ cửa sổ nhìn thấy và thông lượng, khai số lượt qua cần cho một vòng bằng hàm trần, khai số lượt qua mỗi ngày đã dùng, và báo số ngày thật cho {{s035}} vòng.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V states that clients are sampled uniformly by surface area and concludes that the global model is not biased towards any geographic region. Over a LEO constellation the number of contact opportunities per day depends on client latitude and on orbital inclination. Please justify the unbiased sampling claim, or report results per latitude band.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We withdraw the unbiased claim as stated and have replaced it with a measurement. Section V-B now reports, for the constellation and inclination of Table I, the number of contact opportunities per day in six latitude bands, and the counts differ by a factor of about two between the equatorial band and the highest band in our setup. The consequence is stated explicitly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the effective aggregation weight of a client is the declared weight multiplied by the number of times the client is counted, so weighting by sample count alone does not remove the imbalance when participation frequency itself depends on latitude. Because the data distribution in our scenario is also latitude dependent, the two sources of skew are correlated and reinforce rather than cancel, so this is not a slow client problem that disappears with waiting.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table VIII now reports accuracy per latitude band instead of a single network wide figure. To separate the two effects we added a negative control in Section V-C in which the client data is made identically distributed while the orbital geometry is left unchanged: the residual gap in that run isolates the geometric contribution.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, Section V-D reports a participation normalized aggregation rule, in which the weight is divided by the measured participation count, together with its cost, namely a higher variance in the aggregate for the low latitude clients that participate least.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s008}}: trả lời rằng lấy mẫu client đều theo diện tích là thực hành tiêu chuẩn và trọng số theo số mẫu đã xử lý chuyện không đồng nhất. Đúng về thực hành, không trả lời được phản bác.
- Mức {{s003}}: thừa nhận số lượt qua khác nhau giữa các client, nhưng coi đó là chuyện tốc độ hội tụ chứ không phải chuyện chệch, và vẫn giữ một con số toàn mạng.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai số lượt qua mỗi ngày theo dải vĩ độ, chỉ ra rằng trọng số hiệu dụng là trọng số khai nhân số lần được tính, và báo lại kết quả theo dải vĩ độ thay cho một con số toàn mạng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.10` bấm thẻ.
