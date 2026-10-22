---
tieu-de: Handover trong chòm sao LEO
phu-de: Trụ 3 NTN · module 3.5
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 67
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

Thiết bị của tôi chịu bao nhiêu lần handover mỗi giờ, con số đó suy ra từ hình học thế nào, và tỉ lệ ping-pong tôi báo đo trong mô hình đo nào?

## Hình học cho chặn, mô hình đo cho con số
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này tách hai thứ mà bài báo handover hay trộn. Thứ nhất là **chặn do hình học**: cao độ và góc nâng tối thiểu cho ra cửa sổ nhìn thấy, cửa sổ cho ra chặn trên của thời gian trú, và chặn trên của thời gian trú cho ra **chặn dưới** của tần suất handover. Phần này không cần mô phỏng, tính được bằng giấy, và reviewer kiểm lại được trong một phút.

## Hình học cho chặn, mô hình đo cho con số (tiếp)
@phut: 1
@che-do: noi

Thứ hai là **con số do mô hình đo**: tỉ lệ ping-pong và tỉ lệ thất bại. Hai con số này không phải hàm của `H` và `TTT` mà thôi; chúng còn là hàm của phương sai phép đo, chu kỳ báo cáo và trễ báo cáo. Bài nào không khai mô hình đo thì tỉ lệ ping-pong của bài đó không so được với bài khác, dù hai bài dùng cùng một cặp `H` và `TTT`.

## Hình học cho chặn, mô hình đo cho con số (tiếp)
@phut: 1
@che-do: noi

Và một luật khai báo: **báo ping-pong mà không báo thời gian trú là không khai được**. Ping-pong {{s001}} trên thời gian trú {{s002}} giây là một chuyện, {{s001}} trên thời gian trú {{s003}} phút là chuyện khác hẳn, vì mẫu số đếm số cơ hội ping-pong đã khác tám lần.

## Thời gian trú (dwell time)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Thời gian trú (dwell time) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khoảng thời gian thiết bị được phục vụ liên tục bởi **một ô** (một chùm của một vệ tinh) trước khi chuyển sang ô khác. Nó bị chặn trên bởi cửa sổ nhìn thấy của vệ tinh, và còn ngắn hơn nữa khi vệ tinh chia nhiều chùm hoặc khi bộ điều phối chuyển thiết bị đi vì chia tải.

## Thời gian trú (dwell time) · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **thời gian trú là mẫu số của mọi tỉ lệ trong phần handover**. Tần suất handover là nghịch đảo của nó, tỉ lệ ping-pong và tỉ lệ thất bại đều đếm trên số lần handover, tức đếm trên nó. Nên bỏ thời gian trú ra khỏi bảng kết quả là bỏ mẫu số đi và chỉ còn lại tử số.

## A3 với hysteresis H và thời gian kích hoạt TTT
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s005}} trên bốn.*

## A3 với hysteresis H và thời gian kích hoạt TTT · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Điều kiện kích hoạt: chất lượng ô láng giềng trừ `H` phải vượt chất lượng ô đang phục vụ, và phải giữ liên tục suốt `TTT` mới báo cáo. Hai tham số chống hai thứ khác nhau: `H` chống **nhiễu phép đo** theo trục biên độ, `TTT` chống **biến thiên nhanh** theo trục thời gian.

## A3 với hysteresis H và thời gian kích hoạt TTT · (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: cả hai đều **trì hoãn** handover, nên cả hai đều đổi ping-pong theo một chiều và đổi tỉ lệ thất bại theo chiều ngược lại. Không có cặp giá trị nào tốt cho cả hai; chỉ có cặp nằm trên đường đánh đổi. Bài nào báo ping-pong giảm mà không báo tỉ lệ thất bại tăng là báo một đầu của cùng một cái cân.

## Handover có điều kiện (conditional handover, CHO)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s006}} trên bốn.*

## Handover có điều kiện (conditional handover, CHO) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mạng chuẩn bị trước nhiều ô đích và gửi cấu hình xuống thiết bị; thiết bị tự thực thi khi điều kiện thoả, nên không cần một lượt báo cáo và quyết định trong lúc kênh đang xấu đi.

## Handover có điều kiện (conditional handover, CHO) (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: CHO đổi **xác suất thất bại** và đổi **độ bền với trễ báo hiệu**, nhưng **không đổi tần suất handover**. Tần suất do hình học quyết định: vệ tinh vẫn lặn đúng lúc nó lặn. Câu "CHO giảm số lần handover" là một trong những câu dễ bị reviewer bắt nhất, vì nó lẫn cơ chế thực thi với cơ chế sinh sự kiện.

## Từ hình học ra chặn cho tần suất handover
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`t_vis(h, ε_min) = (2θ/360°)·T, θ = 90° − ε_min − arcsin[(R_E/(R_E+h))·cos ε_min], T = 2π·sqrt(a³/μ); t_tru ≤ t_vis nên f_HO ≥ 1/t_vis`

**Giả thiết nó đứng trên:**

## Từ hình học ra chặn cho tần suất handover (tiếp)
@phut: 1
@che-do: so

- Quỹ đạo tròn, Trái Đất cầu, hai vật, nên h là một số chứ không phải hàm của thời gian
- Lượt qua đi qua đỉnh đầu, đây là lượt dài nhất có thể, nên t_vis là chặn TRÊN cho mọi lượt qua
- Vùng phủ liên tục: thiết bị luôn có ít nhất một ô dùng được, nên hết phục vụ là có handover chứ không phải mất liên lạc

## Từ hình học ra chặn cho tần suất handover (tiếp)
@phut: 1
@che-do: so

- Thiết bị không được phục vụ sau khi vệ tinh xuống dưới ε_min

## Từ hình học ra chặn cho tần suất handover · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Chiều của bất đẳng thức là chỗ dễ viết ngược. `t_vis` là chặn TRÊN của thời gian trú, nên nó là chặn TRÊN của khoảng cách giữa hai lần handover, và là chặn DƯỚI của tần suất handover. Ở `h = {{s007}} km` và `ε_min = 10°` thì `t_vis = {{s008}} phút`, nên thiết bị chịu **tối thiểu** khoảng {{s009}} lần handover mỗi giờ, chưa tính chia chùm và chia tải.

## Từ hình học ra chặn cho tần suất handover · ghi (tiếp)
@phut: 0.5
@che-do: noi

Đặc tả `thiet-ke/tru3-ntn.md` gọi {{s003}} phút là chặn dưới của khoảng cách giữa hai handover; đó là chiều ngược, xem phần báo lại của lô này.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s010}} | phút | Ở h = {{s007}} km với ε_min = 10°
!so {{s011}} | lần mỗi giờ | Vẫn h = {{s007}} km và ε_min = 10°
!so {{s012}} | ms | Chu kỳ đo và báo cáo mặc định của NR cho các

## Chòm sao đổi sang cao độ 1200 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Chòm sao đổi sang cao độ {{s013}} km, vẫn ε_min = 10°. Cửa sổ nhìn thấy dài nhất là bao nhiêu phút?

h = {{s013}}, eps = {{s014}}, Re = {{s015}}, mu = {{s016}}

## Chòm sao đổi sang cao độ 1200 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(2⋆(90 - eps - Math.asin((Re/(Re+h))⋆Math.cos(eps⋆Math.PI/180))⋆180/Math.PI)/360)⋆(2⋆Math.PI⋆Math.sqrt(Math.pow((Re+h)⋆1e3,3)/mu)/60)`

Khoảng {{s017}} phút, tức khoảng {{s018}} lần cửa sổ ở {{s007}} km. Hai thứ cùng tăng: chu kỳ tăng từ {{s019}} lên {{s020}} phút, và góc tâm θ tăng từ 14,96° lên 24,04°. Chặn dưới tần suất handover do đó tụt từ khoảng {{s009}} xuống khoảng {{s021}} lần mỗi giờ. Đây là lý do mọi so sánh tần suất handover phải khai cao độ trước khi khai thuật toán.

## Cửa sổ 7,9477 phút
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cửa sổ {{s023}} phút, thiết bị đi qua {{s003}} chùm trong một lượt, mỗi chùm phục vụ một khoảng bằng nhau. Chặn dưới tần suất handover là bao nhiêu lần mỗi giờ?

nchum = {{s003}}, tvis = {{s022}}

## Cửa sổ 7,9477 phút · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`60⋆nchum/tvis`

Khoảng {{s024}} lần mỗi giờ, tức khoảng một lần mỗi phút. Chia chùm nhân tần suất lên đúng bằng số chùm, nên một bài báo khai 'vài lần mỗi giờ' và một bài khai 'hàng chục lần mỗi giờ' có thể đang nói về cùng một chòm sao mà khác nhau ở chỗ một bên đếm handover giữa vệ tinh, một bên đếm cả handover giữa chùm. Khai số chùm trước, rồi mới so.

## Bảng kết quả handover khai: tần suất handover
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bảng kết quả handover khai: tần suất handover, tỉ lệ thất bại, tỉ lệ ping-pong. Thiếu đúng một cột để ba con số kia đọc được. Cột nào?

- Thời gian trú trung bình
- Độ nghiêng quỹ đạo
- Số lượng thiết bị mô phỏng
- Số vệ tinh của chòm sao

## Bảng kết quả handover khai: tần suất handover · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Thời gian trú trung bình**

Ba con số kia đều là tỉ lệ hoặc tần suất đếm trên số lần handover, tức đếm trên thời gian trú. Không có thời gian trú thì ping-pong {{s001}} không biết là {{s001}} trên {{s002}} giây hay trên {{s003}} phút, và hai thứ đó khác nhau tám lần về số cơ hội. Số vệ tinh và độ nghiêng đều cần cho tái lập nhưng không phải cái thiếu để ĐỌC ba con số này.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai bài báo cùng khai H = {{s005}} dB và TTT = {{s025}} ms trên cùng cao độ {{s007}} km, một bài báo ping-pong {{s026}}, bài kia {{s027}}. Giải thích nào có khả năng nhất?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Cao độ {{s007}} km không đủ để xác định hình học
- Một bài có lỗi cài đặt, vì cùng tham số thì phải cùng kết quả
- Hai bài dùng mô hình phép đo khác nhau, nên hai con số không nằm trên cùng một thước
- Một bài dùng CHO nên tần suất handover thấp hơn

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hai bài dùng mô hình phép đo khác nhau, nên hai con số không nằm trên cùng một thước**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Chặn trên của ping-pong tỉ lệ với p₁ luỹ thừa số mẫu trong TTT, mà p₁ phụ thuộc H chia độ lệch chuẩn phép đo. Chỉ cần độ lệch chuẩn đổi từ {{s004}} dB sang {{s028}} dB là chặn trên nhảy từ khoảng {{s029}} lên khoảng {{s030}}, tức hơn ba bậc độ lớn, với H và TTT y nguyên. CHO không đổi tần suất nên không giải thích được, và {{s007}} km đã đủ cho phần hình học.

## Chòm sao chuyển từ 550 km lên 1200 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Chòm sao chuyển từ {{s007}} km lên {{s013}} km, giữ ε_min = 10° và giữ số chùm. Chặn dưới của tần suất handover đổi thế nào?

- Không đổi, vì tần suất do H và TTT quyết định
- Giảm khoảng {{s031}} lần, đúng bằng tỉ số cao độ
- Tăng, vì vệ tinh ở xa hơn nên phủ kém hơn
- Giảm khoảng {{s032}} lần, vì cửa sổ nhìn thấy dài hơn

## Chòm sao chuyển từ 550 km lên 1200 km · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Giảm khoảng {{s032}} lần, vì cửa sổ nhìn thấy dài hơn**

## Chòm sao chuyển từ 550 km lên 1200 km · đáp (tiếp)
@phut: 1
@che-do: noi

Cửa sổ dài nhất đi từ {{s008}} lên {{s033}} phút, tức {{s018}} lần, nên chặn dưới của tần suất chia cho đúng {{s018}} lần. Tỉ số cao độ {{s013}} chia {{s007}} bằng {{s034}} nhưng cửa sổ không tỉ lệ với cao độ: nó là tích của chu kỳ với góc tâm, hai thứ tăng theo hai luật khác nhau. Còn H và TTT không sinh ra sự kiện handover, chúng chỉ quyết định thời điểm báo cáo.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bảng kết quả handover dưới đây có một dòng làm cả bảng không so được với bài khác. Bấm vào dòng đó.

- Cao độ {{s007}} km, ε_min = 10°, {{s003}} chùm trên mỗi vệ tinh.
- Tần suất handover: {{s035}} lần mỗi giờ.
- Thời gian trú trung bình: {{s036}} giây.
- Tỉ lệ thất bại handover: {{s037}}.
- Tỉ lệ ping-pong: {{s038}}, với H = {{s005}} dB và TTT = {{s025}} ms.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Tỉ lệ ping-pong: {{s038}}, với H = {{s005}} dB và TTT = {{s025}} ms.**

Ba dòng trên đều khai đủ: tần suất và thời gian trú khớp nhau ({{s002}} chia {{s036}} giây ra {{s035}} lần mỗi giờ), và tỉ lệ thất bại có mẫu số rõ. Dòng ping-pong thì khai H và TTT mà không khai mô hình đo, trong khi chặn trên của ping-pong là hàm của H chia độ lệch chuẩn phép đo:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

đổi độ lệch chuẩn từ {{s004}} sang {{s028}} dB là chặn trên nhảy hơn ba bậc độ lớn, từ khoảng {{s029}} lên khoảng {{s030}}, với H và TTT y nguyên. Cách sửa: thêm phương sai phép đo, hằng số bộ lọc L3, chu kỳ đo và trễ báo cáo ngay cạnh con số, hoặc báo ping-pong như một đường theo độ lệch chuẩn phép đo thay vì một điểm.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp dưới đây có một chỗ làm phần so sánh mất hiệu lực. Bấm vào chỗ đó.

- Chúng tôi mô phỏng {{s039}} lượt qua ở {{s007}} km với ε_min = 10°, mỗi lượt lấy mẫu RSRP mỗi {{s012}} ms.
- Phép đo được giả định lý tưởng và tức thời, tức không nhiễu đo và không trễ báo cáo.
- Với H = {{s005}} dB và TTT = {{s025}} ms, tỉ lệ ping-pong đo được là {{s040}}.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Con số này thấp hơn {{s041}} mà [{{s042}}] báo ở cùng cặp tham số, nên cơ chế của chúng tôi bền hơn với ping-pong.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Con số này thấp hơn {{s041}} mà [{{s042}}] báo ở cùng cặp tham số, nên cơ chế của chúng tôi bền hơn với ping-pong.**

Ba câu đầu đều hợp lệ nếu khai rõ, và câu thứ hai chính là chỗ khai trung thực giả thiết. Câu cuối mới là chỗ sai: dưới phép đo lý tưởng, A3 với H dương KHÔNG THỂ sinh ping-pong, nên {{s040}} không phải thành tích của cơ chế mà là hệ quả tất yếu của giả thiết đo.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

So nó với {{s041}} của một bài có mô hình đo nhiễu là so hai thước khác nhau, và câu 'bền hơn với ping-pong' không có nội dung. Cách sửa: chạy lại với cùng mô hình đo nhiễu như [{{s042}}], hoặc bỏ phép so và chỉ khai {{s040}} kèm câu nói rõ nó là hệ quả của giả thiết.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Tính góc tâm Trái Đất θ = 90° − ε_min − arcsin[(R_E/(R_E+h))·cos ε_min]
- Tính chu kỳ T = 2π·sqrt(a³/μ) với a = R_E + h
- Cửa sổ nhìn thấy dài nhất t_vis = (2θ/360°)·T
- Thời gian trú t_tru ≤ t_vis, vì còn chia chùm và chia tải
- Nghịch đảo và đổi chiều: f_HO = 1/t_tru ≥ 1/t_vis, tức {{s009}} lần mỗi giờ ở {{s007}} km với ε_min = 10°

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: cửa sổ {{s008}} phút · {{s003}} chùm nên thời gian trú {{s043}} phút · chặn dưới {{s024}} lần mỗi giờ · ping-pong {{s044}} (chặn trên với H = {{s005}} dB, TTT = {{s025}} ms, phép đo lệch chuẩn {{s005}} dB) · thất bại {{s045}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Chỉ số chất lượng đo được tức thời và không nhiễu** tắt đi: Phép đo có nhiễu lệch chuẩn vài dB, đi qua bộ lọc L3, có chu kỳ đo và trễ báo cáo.
- **Thiết bị chỉ có một ô đích, quyết định xong mới thực thi** tắt đi: Mạng chuẩn bị trước nhiều ô theo kiểu CHO, thiết bị tự thực thi khi điều kiện thoả.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi handover do hình học, không do chia tải** tắt đi: Bộ điều phối chuyển thiết bị sang ô khác vì tải hoặc vì công bằng, trước khi vệ tinh lặn.
- **Lượt qua được đo khi vệ tinh đi qua đỉnh đầu** tắt đi: Lượt qua thường lệch khỏi đỉnh đầu, góc nâng cực đại nhỏ hơn 90°.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Phần ba của S7. Hai nhóm thanh kéo cố tình đặt cạnh nhau: nhóm hình học (cao độ, góc nâng, số chùm) quyết định các chặn, nhóm tham số và mô hình đo (H, TTT, độ lệch chuẩn phép đo) quyết định ping-pong và thất bại. Mô hình ping-pong ở đây là chặn trên Chernoff của xác suất một mẫu đo báo láng giềng tốt hơn quá H khi hai ô thật ra bằng nhau, lấy luỹ thừa theo số mẫu trong TTT.

## Chỗ này phải tự kéo, không xem được (tiếp)
@phut: 1
@che-do: demo

Nó cho thấy CHIỀU của đánh đổi, không phải để báo số trong bài.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.5` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table V reports a ping-pong rate of {{s046}} and a handover failure rate of {{s047}}, but the measurement model is never specified. Under ideal instantaneous measurements an A3 rule with positive hysteresis cannot produce ping-pong at all, so the reported value is a property of your measurement assumptions rather than of your algorithm. Please state the measurement error model, the L3 filter coefficient, the measurement period and the reporting delay, and explain how the comparison against [{{s042}}] remains meaningful.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree and have restructured Section V-C. Table V is now split into two groups. The geometric group (mean dwell time {{s048}} s, handover rate {{s049}} per hour) follows from altitude, minimum elevation and beam count alone, and we give the closed-form bound: at {{s007}} km with a {{s014}} degree minimum elevation the longest pass is {{s010}} minutes, so a single-beam device sees at least {{s011}} handovers per hour, and with {{s003}} beams at least {{s050}} per hour.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The measurement-dependent group is now reported with its model: log-normal measurement error with standard deviation {{s005}} dB, L3 filter coefficient {{s028}}, measurement period {{s012}} ms, reporting delay {{s051}} ms. Figure {{s052}} reports ping-pong as a curve over measurement standard deviation from {{s053}} to {{s054}} dB rather than as a single number, because the value moves by about fourteen orders of magnitude across that range while H and TTT are unchanged.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

As a negative control, the ideal-measurement run gives exactly {{s055}} ping-pong, which confirms the reviewer's point that a nonzero value is a property of the measurement model. The comparison with [{{s042}}] has been restricted to the single operating point where we reproduce their declared measurement model, and we state the residual difference there.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: trả lời rằng H và TTT đã được khai đầy đủ nên cấu hình handover là tái lập được. Đúng về tham số, không trả lời được rằng con số ping-pong còn phụ thuộc thứ khác.
- Mức {{s005}}: thêm một câu nói mô phỏng có nhiễu đo, nhưng không cho giá trị phương sai, không cho hằng số bộ lọc, và vẫn giữ nguyên phép so với [{{s042}}].

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: khai đủ bốn thứ (phương sai phép đo, hằng số L3, chu kỳ đo, trễ báo cáo), chạy lại và báo ping-pong như một đường theo phương sai phép đo thay vì một điểm, và nói rõ phép so với [{{s042}}] chỉ hợp lệ ở điểm mà hai bên cùng mô hình đo.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV claims that the proposed conditional handover scheme reduces the number of handovers per device by {{s056}}. Handover events in a LEO constellation are generated by orbital geometry: a device loses its serving beam when the satellite descends below the minimum elevation, regardless of how the handover is executed. Please either justify how execution timing changes the event rate, or restate the contribution.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is correct and we have corrected the claim. Handover event rate is set by geometry: at {{s007}} km with a {{s014}} degree minimum elevation and {{s003}} beams per satellite, a continuously served device experiences at least {{s050}} handovers per hour, and no scheduling or execution scheme can reduce that floor. The {{s056}} figure was measured on the total number of executed handover procedures, which includes repeated attempts after failure and ping-pong pairs. We now report the two quantities separately in Table VI:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the geometric event rate, identical for all compared schemes by construction, and the number of executed procedures per event, where our scheme reduces the overhead from {{s057}} to {{s058}} procedures per event. The abstract and Section I now claim a reduction in handover failure rate from {{s047}} to {{s059}} and in procedure overhead, not in handover frequency. We also added a baseline in which the reference scheme is given the same multi-cell preparation, and the remaining improvement there is {{s060}}, which we state explicitly.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: nói rằng số liệu {{s056}} là đo được từ mô phỏng nên nó đúng. Không phân biệt sự kiện sinh ra với sự kiện được đếm.
- Mức {{s005}}: nhận ra vấn đề và hạ câu xuống 'giảm số lần handover không cần thiết', nhưng vẫn không định nghĩa 'không cần thiết' và vẫn để con số {{s056}} ở abstract.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: tách rõ hai đại lượng: tần suất sự kiện do hình học, và số lần thực thi bị tính thêm do ping-pong hoặc do thất bại rồi thử lại; khai lại {{s056}} là giảm ở nhóm thứ hai, và sửa abstract theo.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.5` bấm thẻ.
