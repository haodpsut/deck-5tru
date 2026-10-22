---
tieu-de: Họ thuật toán và thứ mỗi cái sửa
phu-de: Trụ 2 FL · module 2.1
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
@phan: FL
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

FedProx, SCAFFOLD, FedNova mỗi cái sửa đúng một bệnh nào của FedAvg, và bệnh đó có xuất hiện trong bài của tôi không?

## Bốn thuật toán
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Ba thuật toán hậu FedAvg hay bị xếp cạnh nhau như ba mức độ tốt dần. Chúng không phải thế. Mỗi cái sửa **đúng một bệnh** và không sửa hai bệnh kia: **FedProx** sửa *trôi cục bộ*, bằng cách thêm một neo gần vào hàm mục tiêu cục bộ. **SCAFFOLD** sửa *lệch hướng cập nhật*, bằng cách trừ đi thiên lệch đã ước lượng, và trả giá bằng gấp đôi lượng truyền.

## Bốn thuật toán (tiếp)
@phut: 1
@che-do: noi

**FedNova** sửa *lệch do số bước cục bộ khác nhau*, bằng cách chuẩn hoá theo `tau_i`. Nên câu hỏi trước khi chọn thuật toán không phải là cái nào mạnh nhất, mà là **hệ của tôi mắc bệnh nào trong ba bệnh đó**.

## Bốn thuật toán (tiếp)
@phut: 1
@che-do: noi

Nếu mọi client của anh chạy đúng số bước như nhau thì FedNova không có việc gì làm, và nếu anh báo kết quả theo vòng chứ không theo byte thì SCAFFOLD trông như bữa trưa miễn phí trong khi nó không phải.

Module này có hai việc: nhớ đúng cái mỗi thuật toán sửa, và biết quy mọi so sánh về **byte tới mục tiêu** thay vì vòng tới mục tiêu.

## Trôi cục bộ (client drift)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Trôi cục bộ (client drift) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Sau `E` epoch SGD cục bộ, mỗi client đi về phía cực tiểu của **hàm mục tiêu riêng** `F_k` của nó, không phải của `F`. Càng nhiều bước cục bộ thì các điểm cuối càng tản ra, và trung bình của chúng không phải là một bước tốt cho `F`.

## Trôi cục bộ (client drift) · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** trôi cục bộ tỉ lệ với **số bước cục bộ** và với **độ không đồng nhất giữa các `F_k`**. Dữ liệu IID thì không có trôi dù `E` lớn; `E = {{s001}}` thì không có trôi dù dữ liệu lệch nặng. Hai điều kiện đó phải cùng xảy ra mới sinh bệnh, nên khi phản biện đòi bằng chứng về trôi, anh phải khai cả hai con số chứ không chỉ một.

## Neo gần của FedProx, và việc nó làm với nghiệm
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Neo gần của FedProx, và việc nó làm với nghiệm · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

FedProx đổi bài toán cục bộ thành `min F_k(w) + (mu/2)||w - w^t||^2`. Số hạng thêm vào kéo nghiệm cục bộ về gần mô hình toàn cục của vòng trước, nên biên độ trôi bị chặn.

## Neo gần của FedProx, và việc nó làm với nghiệm · (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** `mu = {{s003}}` cho lại **đúng** FedAvg, không phải gần bằng. Nên FedProx là một họ một tham số **chứa** FedAvg, và mọi so sánh FedProx với FedAvg là so một họ đã dò tham số với một điểm trong chính họ đó. Nếu không dò `mu` và không dò siêu tham số của FedAvg bằng cùng ngân sách thì bảng so sánh không đo được điều nó khai đo.

## Biến điều khiển của SCAFFOLD, và hoá đơn của nó
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Biến điều khiển của SCAFFOLD, và hoá đơn của nó · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

SCAFFOLD giữ hai thứ trạng thái: `c_i` ở từng client và `c` ở máy chủ. Bước cục bộ là `w_i ← w_i - eta(g_i(w_i) - c_i + c)`, tức là trừ đi phần thiên lệch đã ước lượng của hướng cục bộ. Đó là lý do nó sửa lệch hướng mà FedProx không sửa: FedProx chỉ **chặn biên độ** trôi, SCAFFOLD **trừ đi hướng** trôi.

## Biến điều khiển của SCAFFOLD, và hoá đơn của nó · (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** mỗi vòng, client gửi lên **hai** vật cùng kích thước mô hình, là cập nhật mô hình và cập nhật biến điều khiển. Lượng truyền mỗi vòng **gấp {{s002}}**, và client phải giữ trạng thái giữa các vòng, nên cross-device với client không trạng thái thì SCAFFOLD không áp được như in trong bài gốc.

## Khi số bước cục bộ khác nhau, FedAvg tối ưu cái gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Khi số bước cục bộ khác nhau, FedAvg tối ưu cái gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Giả sử client `k` chạy `tau_k` bước thay vì đúng `E` bước. Lấy trung bình các cập nhật theo trọng số `p_k` thì điểm bất động của FedAvg là nghiệm của hàm mục tiêu **đã bị đổi trọng số**: `sum_k (p_k tau_k / sum_j p_j tau_j) F_k`, không phải `sum_k p_k F_k`.

## Khi số bước cục bộ khác nhau, FedAvg tối ưu cái (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** đây không phải chậm hơn, đây là **giải sai bài toán**. Client chạy nhiều bước hơn được khuếch đại tiếng nói, và trong cross-device thì `tau_k` gần như luôn khác nhau vì thiết bị khác nhau và vì client bị ngắt giữa vòng. FedNova chuẩn hoá theo `tau_i` để trả trọng số về đúng, và đó là toàn bộ nội dung đóng góp của nó.

## Bốn quy tắc cập nhật, cạnh nhau
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`FedAvg: w^{t+1} = sum_k (n_k/n) w_k^{t,E} · FedProx cục bộ: min F_k(w) + (mu/2)||w - w^t||^2 · SCAFFOLD cục bộ: w_i <- w_i - eta(g_i(w_i) - c_i + c) · FedNova: w^{t+1} = w^t + (sum_j p_j tau_j) · sum_k p_k (d_k / tau_k)`

**Giả thiết nó đứng trên:**

## Bốn quy tắc cập nhật, cạnh nhau (tiếp)
@phut: 1
@che-do: so

- FedAvg như viết ở trên giả định mọi client chạy ĐÚNG E epoch và không client nào bị ngắt giữa vòng
- Trọng số n_k/n giả định số mẫu là thước đo đúng của tầm quan trọng, tức mọi mẫu đáng giá như nhau giữa các client
- FedProx giả định bài toán cục bộ được giải xấp xỉ tới một độ chính xác khai được, vì nếu giải quá ít bước thì neo gần chưa phát huy

## Bốn quy tắc cập nhật, cạnh nhau (tiếp)
@phut: 1
@che-do: so

- SCAFFOLD giả định client CÓ TRẠNG THÁI giữa các vòng, nên c_i còn dùng được ở vòng sau
- Cả bốn giả định mọi client dùng cùng một hàm mất mát và cùng một kiến trúc

## Bốn quy tắc cập nhật, cạnh nhau · ghi chú
@phut: 1
@che-do: noi

Để ý một chuyện thường bị bỏ qua: `mu = {{s003}}` trong FedProx cho lại đúng FedAvg, và `tau_k = E` cho mọi `k` làm FedNova trùng FedAvg. Hai thuật toán đó là **mở rộng** của FedAvg, không phải đối thủ. SCAFFOLD thì không: nó đổi cả không gian trạng thái, nên không có giá trị tham số nào biến nó về FedAvg.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} | tỉ lệ C | Tỉ lệ client tham gia mỗi vòng
!so {{s002}} | lần | Lượng truyền một vòng một chiều của SCAFFOLD

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

FedAvg, ResNet-18 với {{s010}} triệu tham số, fp32, {{s007}} vòng, tính cả tải lên và tải xuống. Mỗi client đi qua bao nhiêu GB?

vong = {{s007}}, P = {{s008}}, bit = {{s009}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`2⋆vong⋆P⋆bit/8/1e9`

{{s011}} GB mỗi client cho {{s007}} vòng. Con số này đáng nhớ vì nó biến một câu định tính thành một ràng buộc: với client dùng gói dữ liệu di động, gần {{s012}} GB cho một lần huấn luyện là không chạy được, và đó là lý do thật của mọi phần nén trong các bài FL cross-device.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Để ý nó tuyến tính theo số vòng, nên giảm {{s007}} vòng xuống {{s013}} vòng chỉ cứu được một nửa, trong khi lượng tử {{s009}} bit xuống {{s014}} bit cứu được ba phần tư.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Thí nghiệm của anh cho SCAFFOLD cần {{s016}} lần số vòng của FedAvg để tới cùng mục tiêu. Byte lên của SCAFFOLD bằng bao nhiêu lần byte lên của FedAvg?

r = {{s015}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`2⋆r`

{{s017}} lần, tức SCAFFOLD tốn NHIỀU HƠN {{s018}} byte trong khi tiết kiệm {{s019}} vòng. Điểm hoà vốn là r = {{s020}} đúng. Đây là lý do một bảng chỉ có cột số vòng không trả lời được câu hỏi reviewer sẽ hỏi, và cũng là lý do nên để cột byte tới mục tiêu ngay cạnh cột vòng tới mục tiêu.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Đặt mu = {{s003}} trong FedProx thì thu được thuật toán nào?

- FedNova, vì không còn ràng buộc nào về bước cục bộ
- Một thuật toán mới không trùng cái nào trong ba cái kia
- SCAFFOLD, vì mất neo gần thì phải bù bằng biến điều khiển
- Đúng FedAvg, không phải gần bằng

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Đúng FedAvg, không phải gần bằng**

Số hạng thêm vào của FedProx là (mu/2)||w - w^t||^2, bằng {{s003}} với mọi w khi mu = {{s003}}, nên bài toán cục bộ trở lại đúng min F_k(w) và thuật toán trùng FedAvg từng bước một. Hệ quả cho phần đánh giá: FedProx là một họ một tham số CHỨA FedAvg, nên dò mu rồi lấy cái tốt nhất để so với FedAvg mặc định là so một cực đại với một điểm trong cùng họ.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

SCAFFOLD giảm số vòng tới mục tiêu xuống còn {{s021}} lần so với FedAvg. Byte lên tới mục tiêu đổi thế nào?

- Giảm còn {{s021}} lần
- Không đổi, vì byte không phụ thuộc thuật toán
- Tăng lên {{s022}} lần
- Không kết luận được nếu chưa biết số tham số của mô hình

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tăng lên {{s022}} lần**

Tỉ số byte bằng 2r, với r = {{s021}} cho {{s022}}. Phương án cuối là bẫy dễ chọn nhất: số tham số triệt tiêu giữa tử và mẫu, nên tỉ số byte không phụ thuộc cỡ mô hình, số bit hay số vòng. Chỉ r quyết định, và điểm hoà vốn là r = {{s020}}.

## Trong hệ của anh
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong hệ của anh, client bị ngắt giữa vòng và vẫn gửi phần đã chạy, nên tau_k khác nhau. Điều gì xảy ra với FedAvg?

- Nó hội tụ chậm hơn tới cùng nghiệm
- Nó hội tụ tới nghiệm của một hàm mục tiêu đã bị đổi trọng số theo tau_k
- Nó không hội tụ, nghiệm dao động quanh trung bình các F_k
- Nó vẫn đúng nếu trọng số tổng hợp là n_k/n

## Trong hệ của anh · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Nó hội tụ tới nghiệm của một hàm mục tiêu đã bị đổi trọng số theo tau_k**

## Trong hệ của anh · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm bất động là nghiệm của sum_k (p_k tau_k / sum_j p_j tau_j) F_k. Phân biệt chậm hơn với giải sai bài toán là toàn bộ nội dung của FedNova, và đây cũng là lằn ranh giữa một kết quả thực nghiệm kém và một phần phương pháp chưa xác định được hàm mục tiêu. Phương án cuối sai vì trọng số n_k/n chính là p_k, tức là chỗ sinh bệnh chứ không phải chỗ chữa.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết lập thí nghiệm sau có một câu làm toàn bộ phần so sánh FedProx với FedAvg mất hiệu lực. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi chia CIC-IDS2017 cho {{s013}} client theo Dirichlet với alpha = {{s020}},
- mỗi client chạy E = {{s023}} epoch cục bộ với batch {{s009}} và bước học {{s024}},
- dò mu của FedProx trên {0,001; {{s024}}; {{s025}}; 1} và báo giá trị tốt nhất, còn FedAvg dùng cấu hình mặc định,
- và báo độ chính xác toàn cục trung bình trên {{s004}} hạt cùng độ lệch chuẩn.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**dò mu của FedProx trên {0,001; {{s024}}; {{s025}}; 1} và báo giá trị tốt nhất, còn FedAvg dùng cấu hình mặc định,**

Vì mu = {{s003}} cho lại đúng FedAvg, họ FedProx CHỨA FedAvg. Lấy cực đại trên bốn giá trị của một họ rồi so với một điểm trong chính họ đó thì chênh lệch dương là chuyện bắt buộc, không phải bằng chứng cho neo gần. Hai câu đầu và câu cuối đều hợp lệ. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

dò bước học và E cho FedAvg bằng đúng bốn lần chạy, hoặc báo cả đường cong theo mu kèm giá trị tại mu = {{s003}} để người đọc thấy FedAvg nằm đâu trên đường đó.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một chỗ biến một hoá đơn thành một lợi thế. Bấm vào chỗ đó.

- SCAFFOLD đạt mục tiêu {{s026}} sau {{s027}} vòng, còn FedAvg cần {{s007}} vòng,
- tức giảm {{s019}} số vòng truyền,
- nên phương pháp của chúng tôi tiết kiệm {{s019}} chi phí truyền thông.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên phương pháp của chúng tôi tiết kiệm {{s019}} chi phí truyền thông.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu đầu là phép đo đúng và phát biểu đúng. Câu thứ ba đổi đơn vị mà không nhân payload: SCAFFOLD gửi mô hình cộng biến điều khiển, tức gấp đôi mỗi vòng, nên byte lên bằng {{s016}} × {{s002}} = {{s017}} lần FedAvg, tức TỐN THÊM {{s018}}. Cách sửa: giữ hai câu đầu, bỏ câu ba, và thêm một dòng byte tới mục tiêu trong bảng. Nếu muốn giữ tuyên bố tiết kiệm thì phải đo được r nhỏ hơn {{s020}}.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt c = số byte một chiều của một mô hình, c = P·b/8 với P tham số và b bit mỗi tham số
- Byte lên tới mục tiêu của FedAvg = R·c, với R là số vòng FedAvg cần
- Byte lên tới mục tiêu của SCAFFOLD = (r·R)·2c, vì mỗi vòng gửi mô hình cộng biến điều khiển
- Tỉ số byte = 2r, nên SCAFFOLD chỉ rẻ hơn theo byte khi r nhỏ hơn {{s028}}

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Client k chạy tau_k bước SGD, cập nhật tích luỹ d_k = -eta·sum_{j=1..tau_k} g_k(w_k^j)
- Xấp xỉ d_k ≈ -eta·tau_k·grad F_k(w^t) khi tau_k bước còn nằm trong lân cận của w^t
- FedAvg lấy w^{t+1} = w^t + sum_k p_k d_k ≈ w^t - eta·sum_k p_k tau_k grad F_k(w^t)
- Hướng đi là gradient của sum_k (p_k tau_k) F_k, tức hàm mục tiêu đã bị đổi trọng số

## Dẫn lại từng bước · ca hai (tiếp)
@phut: 1
@che-do: so

- Chuẩn hoá lại bằng cách thay d_k bởi d_k/tau_k rồi nhân sum_j p_j tau_j: điểm bất động về lại nghiệm của sum_k p_k F_k

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: FedAvg {{s007}} vòng · SCAFFOLD {{s027}} vòng · byte SCAFFOLD trên FedAvg = {{s029}} · điểm bất động của cả bốn là nghiệm của sum_k p_k F_k

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi client chạy đúng E bước cục bộ, không ai bị ngắt giữa vòng** tắt đi: tau_k khác nhau giữa client, vì thiết bị khác nhau, vì số mẫu khác nhau, hoặc vì client bị ngắt và vẫn gửi phần đã chạy.
- **Mọi client tham gia mọi vòng, C = {{s001}}** tắt đi: Mỗi vòng lấy mẫu một phần client, như cross-device thật, C khoảng {{s025}} hoặc nhỏ hơn.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **FedProx và FedAvg được dò siêu tham số bằng cùng ngân sách** tắt đi: mu của FedProx dò trên năm giá trị, còn FedAvg lấy cấu hình mặc định.
- **Trục so sánh là số vòng truyền** tắt đi: So theo byte lên tới mục tiêu, tức nhân số vòng với payload mỗi vòng.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Hoá đơn băng thông của SCAFFOLD. Kéo số tham số, số bit, số vòng FedAvg cần, và tỉ số vòng r mà anh ĐO ĐƯỢC cho SCAFFOLD. Để ý một chuyện: tỉ số byte không phụ thuộc mô hình to hay nhỏ.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.1` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table III compares FedProx, whose proximal coefficient mu was tuned over four values, against FedAvg in its default configuration, and Figure {{s005}} plots accuracy against communication rounds only. Since FedProx with mu equal to zero reduces exactly to FedAvg, the reported gap is a search over a family that contains the baseline rather than evidence for the proximal term. Furthermore, SCAFFOLD transmits two model-sized objects per round, so a round-indexed x axis understates its communication cost.

## Phản biện hỏi (tiếp)
@phut: 1
@che-do: hoi

Please equalize the tuning budget across methods and report bytes to target accuracy.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have equalized the tuning budget. FedAvg now receives the same four-run budget over local epochs and learning rate that FedProx receives over mu, and Table III reports the best configuration for every method under that identical budget. Figure {{s005}} additionally plots accuracy against uplink bytes per client, and Table III gains a payload column: FedAvg, FedProx and FedNova each send one model per round, while SCAFFOLD sends two.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

With our measured round ratio of {{s030}}, SCAFFOLD uses {{s031}} times the uplink bytes of FedAvg despite {{s032}} percent fewer rounds, so its rank inverts between the two axes and we now state this inversion explicitly in Section V-C. We also report the break-even condition as a testable prediction: SCAFFOLD is cheaper in bytes only when its round ratio falls below {{s033}}, which our setting does not reach.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, Figure {{s023}} plots accuracy against mu with the mu equal to zero point marked, so the reader can see where FedAvg sits inside the FedProx family. Appendix B reports the measured distribution of local step counts and our handling of clients dropped mid-round, since the aggregation weights in Table III assume equal local work.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: trả lời rằng mu = {{s024}} là giá trị thường dùng trong tài liệu và rằng FedAvg không có siêu tham số tương ứng để dò. Đúng một phần về thực hành, nhưng không trả lời được phản bác: nó công nhận bảng vẫn so một cực đại với một điểm.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: chạy lại với cùng ngân sách dò cho cả hai, ví dụ dò bước học và E cho FedAvg bằng đúng bốn lần chạy, và báo lại bảng. Vẫn còn nợ trục byte, nên phần SCAFFOLD vẫn chưa trả lời.
- Mức {{s004}}: làm mức {{s002}}, cộng thêm cột byte lên tới mục tiêu cho cả bốn thuật toán, cộng khai payload mỗi vòng của từng cái, cộng chỉ rõ thứ hạng đổi ở đâu giữa hai trục.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.1` bấm thẻ.
