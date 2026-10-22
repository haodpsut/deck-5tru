---
tieu-de: Số phải dẫn lại được trong *ba mươi giây*
phu-de: Trụ 2 FL · số, công thức, và giả thiết của chúng
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 95
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
@notes: Deck này để đọc to, có đồng hồ. Không để đọc thầm.

## Luật của deck này
@phut: 0.5
@che-do: noi
@notes: Nói luật rồi bắt đầu. Đây là deck duy nhất của bộ mà đọc thầm là vô nghĩa.

{{TAKE_HOME}}

Mỗi slide hỏi một con số hoặc một công thức. Dẫn lại **bằng miệng trong ba mươi giây**, rồi mới lật. Bấm máy tính là tính sai mục đích.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`FedAvg: w^{t+1} = sum_k (n_k/n) w_k^{t,E} · FedProx cục bộ: min F_k(w) + (mu/2)||w - w^t||^2 · SCAFFOLD cục bộ: w_i <- w_i - eta(g_i(w_i) - c_i + c) · FedNova: w^{t+1} = w^t + (sum_j p_j tau_j) · sum_k p_k (d_k / tau_k)`

## Giả thiết
@phut: 0.5
@che-do: so

- FedAvg như viết ở trên giả định mọi client chạy ĐÚNG E epoch và không client nào bị ngắt giữa vòng
- Trọng số n_k/n giả định số mẫu là thước đo đúng của tầm quan trọng, tức mọi mẫu đáng giá như nhau giữa các client
- FedProx giả định bài toán cục bộ được giải xấp xỉ tới một độ chính xác khai được, vì nếu giải quá ít bước thì neo gần chưa phát huy

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- SCAFFOLD giả định client CÓ TRẠNG THÁI giữa các vòng, nên c_i còn dùng được ở vòng sau
- Cả bốn giả định mọi client dùng cùng một hàm mất mát và cùng một kiến trúc

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Tỉ lệ client tham gia mỗi vòng, giá trị điển hình trong cấu hình cross-device. Nhập dưới dạng phân số thập phân.

*Module {{s001}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s002}} | tỉ lệ C | module {{s001}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Lượng truyền một vòng một chiều của SCAFFOLD, tính theo lần so với FedAvg trên cùng mô hình.

*Module {{s001}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s003}} | lần | module {{s001}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

FedAvg, ResNet-18 với {{s007}} triệu tham số, fp32, {{s004}} vòng, tính cả tải lên và tải xuống. Mỗi client đi qua bao nhiêu GB?

vong = {{s004}}, P = {{s005}}, bit = {{s006}}

## Đáp
@phut: 0.5
@che-do: so

`2⋆vong⋆P⋆bit/8/1e9`

{{s008}} GB mỗi client cho {{s004}} vòng. Con số này đáng nhớ vì nó biến một câu định tính thành một ràng buộc: với client dùng gói dữ liệu di động, gần {{s009}} GB cho một lần huấn luyện là không chạy được, và đó là lý do thật của mọi phần nén trong các bài FL cross-device.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Để ý nó tuyến tính theo số vòng, nên giảm {{s004}} vòng xuống {{s010}} vòng chỉ cứu được một nửa, trong khi lượng tử {{s006}} bit xuống {{s011}} bit cứu được ba phần tư.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Thí nghiệm của anh cho SCAFFOLD cần {{s013}} lần số vòng của FedAvg để tới cùng mục tiêu. Byte lên của SCAFFOLD bằng bao nhiêu lần byte lên của FedAvg?

r = {{s012}}

## Đáp
@phut: 0.5
@che-do: so

`2⋆r`

{{s014}} lần, tức SCAFFOLD tốn NHIỀU HƠN {{s015}} byte trong khi tiết kiệm {{s016}} vòng. Điểm hoà vốn là r = {{s017}} đúng. Đây là lý do một bảng chỉ có cột số vòng không trả lời được câu hỏi reviewer sẽ hỏi, và cũng là lý do nên để cột byte tới mục tiêu ngay cạnh cột vòng tới mục tiêu.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`p_k ~ Dir(alpha·1_C) · TV(p_k, p) = (1/2)·sum_c |p_k(c) - p(c)| · E[sum_c p_k(c)^2] = (alpha+1)/(C·alpha+1) · m = 1/E[sum_c p_k(c)^2] = (C·alpha+1)/(alpha+1) · TV tương đương = (C-1)/(C·(alpha+1))`

## Giả thiết
@phut: 0.5
@che-do: so

- Dirichlet ĐỐI XỨNG, tức cùng một alpha cho mọi lớp; nếu dùng alpha khác nhau theo lớp thì mọi công thức dưới đây sai
- Phân bố nhãn toàn cục p là đều trên C lớp; nếu tập gốc đã lệch lớp thì p không đều và TV phải tính với p thật
- Số lớp C biết trước và mọi client dùng CÙNG tập lớp

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Dòng TV tương đương là TV của một client giữ ĐỀU m lớp, với m là số lớp hiệu dụng ở trên. Nó KHÔNG phải kỳ vọng của TV dưới Dirichlet, mà là TV của một client đại diện có cùng chỉ số Simpson. Dùng nó để đọc bậc độ lớn thì được, dùng nó làm con số báo cáo thì phải khai đúng định nghĩa này

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Dirichlet đối xứng với alpha = {{s018}} trên C = {{s009}} lớp. Số lớp hiệu dụng kỳ vọng mỗi client là bao nhiêu?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s020}} | lớp | module {{s019}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng công thức, alpha = {{s017}} và C = {{s009}}. Số lớp hiệu dụng kỳ vọng mỗi client là bao nhiêu?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s021}} | lớp | module {{s019}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

C = {{s009}} lớp, mỗi client chỉ giữ đúng một lớp. TV giữa phân bố nhãn của client và phân bố đều toàn cục bằng bao nhiêu?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s022}} | TV | module {{s019}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Phân vùng Dirichlet đối xứng, C = {{s009}} lớp, alpha = {{s017}}. Số lớp hiệu dụng kỳ vọng mỗi client bằng bao nhiêu?

C = {{s009}}, a = {{s023}}

## Đáp
@phut: 0.5
@che-do: so

`(C⋆a+1)/(a+1)`

Đúng {{s024}} lớp trên {{s009}}, một con số tròn đáng nhớ. Nó khớp với câu lệch mạnh nhưng mọi lớp còn hiện diện: mọi lớp có xác suất dương, nhưng khối lượng tập trung vào bốn lớp. Để ý alpha = {{s018}} cho {{s025}} lớp, tức hai mức alpha này là hai chế độ khác nhau, không phải hai cách nói cùng một chuyện.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

C = {{s009}} lớp, alpha = {{s027}}. TV tương đương so với phân bố nhãn đều bằng bao nhiêu?

C = {{s009}}, a = {{s026}}

## Đáp
@phut: 0.5
@che-do: so

`(C-1)/(C⋆(a+1))`

Đúng {{s028}}. Vậy mốc TV tương đương bằng một nửa ứng với alpha = (C-2)/C, bằng {{s027}} khi C = {{s009}}. Con số này đáng để trong đầu vì nó cho ngay một cách đọc: alpha dưới {{s027}} là vùng TV tương đương vượt {{s028}}, còn alpha = {{s004}} cho TV tương đương chỉ khoảng {{s029}}, tức gần IID.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`E[F(w_T)] - F⋆ ≤ (kappa/(gamma + T - 1))·( 2B/mu + (mu·gamma/2)·||w_1 - w⋆||^2 ), kappa = L/mu, gamma = max{8·kappa, E}`

## Giả thiết
@phut: 0.5
@che-do: so

- F là mu-LỒI MẠNH. Đây là giả thiết loại mạng neural ra khỏi tầm, và khi nó tắt thì kappa cùng cả bound KHÔNG CÒN ĐỊNH NGHĨA ĐƯỢC
- F là L-TRƠN, tức gradient Lipschitz với hằng số L; không có L thì cả kappa và số hạng 6L·Gamma mất nghĩa
- Phương sai gradient ngẫu nhiên của client k bị chặn bởi sigma_k^2

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Chuẩn gradient ngẫu nhiên bị chặn bởi G trên toàn miền; lưu ý giả thiết này chỏi với lồi mạnh trên miền không bị chặn
- T đếm TỔNG SỐ BƯỚC SGD cục bộ, không phải số vòng truyền; số vòng truyền là T/E
- Mọi client tham gia MỌI vòng, và trọng số p_k cố định. Lấy mẫu một phần client thêm số hạng riêng, không nằm trong B này

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`B = sum_k p_k^2·sigma_k^2 + 6·L·Gamma + 8(E-1)^2·G^2, Gamma = F⋆ - sum_k p_k·F_k⋆`

## Giả thiết
@phut: 0.5
@che-do: so

- Gamma định nghĩa qua các GIÁ TRỊ TỐI ƯU F⋆ và F_k⋆, nên nó không phụ thuộc thuật toán, không phụ thuộc khởi tạo và không phụ thuộc E
- Gamma ≥ {{s030}} luôn đúng, vì F⋆ là cực tiểu của tổ hợp lồi của các F_k nên không nhỏ hơn tổ hợp các cực tiểu riêng
- Gamma = {{s030}} khi mọi F_k có cùng tập cực tiểu, mà trường hợp quen nhất của điều đó là dữ liệu IID

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Trọng số p_k là hằng số, tổng bằng {{s031}}; với p_k = 1/K đồng đều thì số hạng thứ nhất bằng sigma^2/K

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trong B, số hạng chứa số bước cục bộ phình theo nó với bậc nào? Nhập bậc đó.

*Module {{s032}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s003}} | bậc | module {{s032}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Bốn client, trọng số tổng hợp đồng đều, mỗi client có sigma_k = {{s003}}. Số hạng phương sai sum_k p_k^2 sigma_k^2 bằng bao nhiêu?

*Module {{s032}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s031}} |  | module {{s032}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Lấy L = {{s031}} và mu = {{s018}} nên kappa = L/mu. Bound dùng gamma = max{8·kappa, E}. Với E = {{s033}} thì gamma bằng bao nhiêu?

*Module {{s032}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s034}} |  | module {{s032}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Lấy L = {{s031}}, {{s009}} client trọng số đồng đều, sigma_k = {{s031}}, Gamma = {{s031}}, G = {{s031}}, E = {{s033}}. B bằng bao nhiêu?

sig = {{s031}}, K = {{s009}}, L = {{s031}}, Gam = {{s031}}, E = {{s033}}, G = {{s031}}

## Đáp
@phut: 0.5
@che-do: so

`sig⋆sig/K + 6⋆L⋆Gam + 8⋆Math.pow(E-1,2)⋆G⋆G`

B = {{s035}}, tách ra thành {{s036}} cộng {{s037}} cộng {{s038}}. Số hạng epoch một mình là {{s038}}, tức {{s039}} của B, nên ở cấu hình này bound nói về giá của bước cục bộ chứ không nói về non-IID. Đổi E về {{s031}} thì B tụt xuống {{s040}}, tức giảm {{s041}} lần, trong khi mọi tham số dữ liệu giữ nguyên.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Giữ nguyên mọi thứ, tăng số bước cục bộ từ {{s003}} lên {{s042}}. Số hạng 8(E-1)^2 G^2 nhân lên bao nhiêu lần?

E1 = {{s003}}, E2 = {{s042}}

## Đáp
@phut: 0.5
@che-do: so

`Math.pow((E2-1)/(E1-1), {{s003}})`

{{s043}} lần, vì tỉ số là ((6-1)/(2-1))^2 = 5^2. Đây là nội dung thực tế của chữ bậc hai: nhân số bước cục bộ lên {{s044}} lần thì số hạng đó nhân lên {{s043}} lần, không phải {{s044}} lần. Hai số hạng kia không đổi một chút nào, nên toàn bộ phần phình của B đến từ đúng một chỗ.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`byte một vòng một chiều = s·P·(b + idx)/8 + H, idx = ceil(log2 P) · E[Q(v)] = v cho lượng tử không chệch · R(s) = R0·(rho/s + {{s031}} - rho) · byte tới mục tiêu = R(s)·(s·P·(b+idx)/8 + H) · s⋆ = sqrt(rho·H/((1-rho)·P·(b+idx)/8))`

## Giả thiết
@phut: 0.5
@che-do: so

- Mỗi toạ độ giữ lại tốn b bit giá trị CỘNG idx bit chỉ số; khi gửi dày đủ thì không cần chỉ số nên idx = {{s030}}
- H là chi phí cố định mỗi vòng mỗi client, gồm bắt tay, tiêu đề, lịch chọn client và thiết lập secure aggregation; H phải ĐO ĐƯỢC trên hệ thật, không đoán

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- rho là hệ số phình vòng do nén, trong đoạn từ {{s030}} tới {{s031}}, ĐO ĐƯỢC từ ablation của chính anh: rho = {{s030}} là nén miễn phí, rho = {{s031}} là trả đủ trần lý thuyết 1/delta của bộ nén delta-co với delta = s
- R0 là số vòng tới mục tiêu khi KHÔNG nén, đo trên cùng một mức mục tiêu

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Mọi công thức trên giả định nén còn giữ được ĐIỂM TỚI, tức không chệch hoặc có phản hồi lỗi; nếu không thì không có mục tiêu nào để đếm byte tới
- Mô hình chi phí là tuyến tính theo byte, tức băng thông là cổ chai; nếu độ trễ là cổ chai thì phải thay bằng mô hình theo số vòng

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

ResNet-18 có {{s007}} triệu tham số, lưu ở fp32. Lượng truyền một chiều một vòng một client là bao nhiêu MB?

*Module {{s045}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s046}} | MB | module {{s045}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng mô hình ResNet-18 đó, lượng tử hoá về {{s011}} bit mỗi tham số. Lượng truyền một chiều một vòng là bao nhiêu MB?

*Module {{s045}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s047}} | MB | module {{s045}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng mô hình đó, giữ top {{s048}} toạ độ, mỗi giá trị {{s006}} bit và mỗi chỉ số {{s049}} bit. Lượng truyền một chiều một vòng là bao nhiêu MB?

*Module {{s045}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s050}} | MB | module {{s045}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

So dense fp32 với top-1% có chỉ số {{s049}} bit mỗi toạ độ. Payload nhỏ đi bao nhiêu lần?

bit = {{s006}}, s = {{s051}}, idx = {{s049}}

## Đáp
@phut: 0.5
@che-do: so

`bit/(s⋆(bit + idx))`

{{s052}} lần, không phải {{s004}} lần. Chênh lệch đến từ chỉ số: mỗi toạ độ giữ lại tốn {{s006}} bit giá trị cộng {{s049}} bit chỉ số, tức {{s053}} bit, nên tải trọng mỗi toạ độ tăng {{s054}} lần so với dense. Một bảng báo giảm {{s004}} lần là bảng quên chi phí chỉ số, và đây là con số mà phản biện kiểm trước tiên vì nó kiểm được bằng một phép chia.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

ResNet-18 với {{s007}} triệu tham số, {{s006}} bit giá trị và {{s049}} bit chỉ số, chi phí cố định {{s055}} B mỗi vòng mỗi client, hệ số phình vòng rho = {{s017}}. Tỉ lệ thưa tối ưu s⋆ bằng bao nhiêu?

rho = {{s023}}, H = {{s055}}, P = {{s005}}, bit = {{s006}}, idx = {{s049}}

## Đáp
@phut: 0.5
@che-do: so
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

`Math.sqrt(rho⋆H/((1-rho)⋆P⋆(bit+idx)/8))`

{{s056}}, tức giữ khoảng {{s057}} toạ độ là đáy của byte tới mục tiêu. Nén thưa hơn mức này làm byte tới mục tiêu TĂNG, vì số hạng rho·H/s phình theo 1/s trong khi tải trọng đã nhỏ tới mức không bù lại được. Để ý s⋆ phụ thuộc H: với H = {{s030}} thì s⋆ về {{s030}} và không có vùng đảo chiều, nên vùng đó là tính chất của chi phí cố định mỗi vòng, không phải của bộ nén.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`P[M(D) ∈ S] ≤ e^epsilon · P[M(D') ∈ S] + delta với mọi D, D' kề nhau và mọi S; Delta2 = max ||f(D) − f(D')||₂; sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon`

## Giả thiết
@phut: 0.5
@che-do: so

- Quan hệ kề đã được khai rõ: khác đúng một bản ghi, hay khác đúng một người dùng. Đổi đơn vị là đổi bảo đảm
- Delta2 là độ nhạy L2 trong trường hợp xấu nhất trên MỌI cặp kề, không phải độ nhạy quan sát được trên dữ liệu đang có
- Chặn Gauss cổ điển chỉ được chứng minh với epsilon trong khoảng ({{s030}}, {{s031}}); ngoài khoảng đó công thức vẫn chạy nhưng không còn là một chặn

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Nhiễu cộng vào là Gauss độc lập từng toạ độ với cùng sigma, và nhiễu được cộng vào ĐẦU RA của f, không cộng vào dữ liệu

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`cơ chế Gauss là (alpha, alpha/(2·sigma²))-RDP; epsilon(delta) = epsilon_RDP(alpha) + log(1/delta)/(alpha − {{s031}}), lấy min theo alpha; DP-SGD: cắt chuẩn gradient từng mẫu về C, cộng N(0, sigma²C²I), lấy mẫu Poisson tỉ lệ q, ghép T bước`

## Giả thiết
@phut: 0.5
@che-do: so

- Cắt chuẩn gradient được thực hiện TỪNG MẪU trước khi cộng, nên độ nhạy L2 của tổng trong một lô bị chặn bởi C
- Lô được chọn bằng lấy mẫu Poisson độc lập với tỉ lệ q, không phải bằng xáo trộn rồi cắt lô cố định
- RDP cộng tuyến tính khi ghép T bước, với cùng một alpha cho cả T bước trước khi lấy min

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- sigma là tỉ số nhiễu trên chuẩn cắt, nên nhiễu thực tế cộng vào có độ lệch chuẩn sigma·C mỗi toạ độ

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Chặn Gauss cổ điển sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon chỉ được chứng minh khi epsilon nhỏ hơn một ngưỡng. Ngưỡng đó là bao nhiêu?

*Module {{s058}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s031}} | chặn trên của epsilon | module {{s058}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Luật ngón tay là chọn delta nhỏ hơn nghịch đảo số bản ghi. Với một triệu bản ghi thì delta phải nhỏ hơn {{s009}} luỹ thừa âm bao nhiêu? Nhập số mũ.

*Module {{s058}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s042}} | số mũ âm | module {{s058}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cơ chế đạt epsilon = {{s017}} ở mức bản ghi. Mỗi người dùng đóng góp {{s009}} bản ghi. Chặn riêng tư nhóm cho epsilon ở mức người dùng là bao nhiêu?

*Module {{s058}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s033}} | epsilon mức người dùng | module {{s058}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một truy vấn có độ nhạy L2 bằng {{s031}}. Muốn (epsilon = {{s017}}, delta = {{s009}} luỹ thừa trừ 5)-DP bằng cơ chế Gauss cổ điển thì sigma nhỏ nhất là bao nhiêu?

sens = {{s031}}, d = {{s033}}, eps = {{s023}}

## Đáp
@phut: 1
@che-do: so

`sens × Math.sqrt(2 × (Math.log(1.25) + d × Math.LN10)) / eps`

Khoảng {{s059}}. Để ý epsilon = {{s017}} nằm TRONG vùng hiệu lực, nên con số này là một chặn thật. Nhiễu phải có độ lệch chuẩn gần {{s009}} lần độ nhạy của một bản ghi, và đó là lý do DP ở epsilon nhỏ hơn {{s031}} đắt tới mức nhiều bài lặng lẽ đẩy epsilon lên {{s011}} rồi giữ nguyên công thức.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một bước Gauss với sigma = {{s021}} là (alpha, alpha/(2·sigma²))-RDP. Chuyển về DP tại alpha = {{s009}} và delta = {{s009}} luỹ thừa trừ {{s033}} cho epsilon bằng bao nhiêu?

alpha = {{s009}}, sigma = {{s021}}, delta = {{s060}}

## Đáp
@phut: 1
@che-do: so

`alpha / ({{s003}} × sigma × sigma) + Math.log(1 / delta) / (alpha - {{s031}})`

Khoảng {{s061}}. Hai điều phải đọc ra. Một, con số này LỚN hơn {{s031}}, nên ở đúng điểm này công thức Gauss cổ điển không áp được: muốn dùng nó anh phải tụt epsilon xuống dưới {{s031}}, tức tăng sigma.

## Đáp (tiếp)
@phut: 1
@che-do: so

Hai, epsilon thật là min theo alpha nên nó nhỏ hơn hoặc bằng {{s061}}; lấy một alpha bất kỳ rồi báo kết quả là báo một chặn lỏng hơn mức cần thiết, và nếu lưới alpha quá hẹp thì min rơi vào biên lưới mà không ai thấy.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`truy ngược gradient: min theo (x', y') của ||grad W(x', y') − grad W||² ; thay thế mô hình: X = gamma·(X_xau − G_t) + G_t, gamma = n/eta ; suy luận thành viên: Adv = TPR − FPR`

## Giả thiết
@phut: 1
@che-do: so

- Truy ngược gradient cần bốn thứ cùng lúc: biết kiến trúc và hàm mất mát, thấy gradient THÔ của một client, lô nhỏ, và không có nhiễu DP đáng kể
- Thay thế mô hình cần ba thứ: kẻ xấu được chọn trong vòng đó, mô hình đã gần hội tụ nên cập nhật lành gần triệt tiêu, và server không chặn chuẩn cập nhật

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Adv đo ở CÙNG một ngưỡng cho cả hai lớp, và tập thành viên với tập không thành viên chỉ khác nhau ở yếu tố thành viên, không khác ở phân bố
- Cả ba con số đều là hàm của năng lực kẻ tấn công đã khai, nên đổi mô hình đe doạ là đổi kết quả, không phải đổi cách trình bày

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

FedAvg lấy một trăm client mỗi vòng và dùng bước server eta = {{s031}}. Hệ số nhân gamma mà tấn công thay thế mô hình phải dùng là bao nhiêu?

*Module {{s062}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s004}} | lần | module {{s062}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Với mô hình đã gần hội tụ và không có chặn chuẩn ở server, tấn công thay thế mô hình cần kẻ xấu được chọn trong bao nhiêu vòng để mô hình toàn cục bằng đúng mô hình xấu?

*Module {{s062}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s031}} | vòng | module {{s062}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Server lấy {{s063}} client mỗi vòng và dùng bước eta = {{s017}}. Hệ số nhân gamma của tấn công thay thế mô hình là bao nhiêu?

n = {{s063}}, eta = {{s023}}

## Đáp
@phut: 1
@che-do: so

`n / eta`

Bằng {{s064}}, tức gấp bốn lần trường hợp n = {{s004}} với eta = {{s031}}. Hai cách làm tấn công khó hơn nằm trong cùng một phân số: tăng số client mỗi vòng, hoặc hạ bước server. Cả hai đều buộc kẻ xấu nộp cập nhật có chuẩn lớn hơn, nên cả hai đều làm chặn chuẩn ở server hiệu quả hơn. Nhưng đừng đọc đây là tin tốt một chiều:

## Đáp (tiếp)
@phut: 1
@che-do: so

thẻ mô phỏng cho thấy cùng lúc đó cửa hậu đã cài vào lại sống dai hơn.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một cửa hậu đã cài xong, rồi kẻ xấu không được chọn nữa. Với mô hình co tuyến tính hệ số ({{s031}} − eta/n) mỗi vòng, n = {{s004}} và eta = {{s031}}, cần bao nhiêu vòng để hiệu lực cửa hậu phai xuống dưới 10%?

eta = {{s031}}, n = {{s004}}

## Đáp
@phut: 1
@che-do: so

`Math.log(0.1) / Math.log(1 - eta / n)`

Khoảng {{s065}} vòng, tức hơn hai trăm vòng huấn luyện lành mới xoá được tới mức một phần mười. Con số này chỉ để đọc BẬC ĐỘ LỚN, vì mô hình co tuyến tính là một mô hình quy ước, không phải phép đo. Điều đáng dùng là hệ quả thực nghiệm:

## Đáp (tiếp)
@phut: 1
@che-do: so

một bài báo khai cửa hậu bị xoá sau vài vòng thì phải nói nó đo trên bao nhiêu vòng, vì đo trên {{s066}} vòng và đo trên {{s067}} vòng cho hai kết luận trái nhau với cùng một hệ.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Krum: s(i) = tổng trên n−f−2 láng giềng gần nhất của ||w_i − w_j||², chọn i nhỏ nhất, cần n ≥ 2f+3; Trung bình cắt beta: bỏ beta phần cao nhất và thấp nhất theo TỪNG toạ độ, cần beta ≥ f/n; Trung vị theo toạ độ: điểm đổ vỡ {{s068}}; Trần chung: không bộ tổng hợp nào bền khi f/n ≥ {{s068}}`

## Giả thiết
@phut: 1
@che-do: so

- Các cập nhật của client lành gần nhau trong không gian tham số, nên khoảng cách lớn là dấu hiệu của kẻ xấu. Đây là giả thiết mà non-IID phá
- f được biết, hoặc có một chặn trên của f, vì cả n−f−2 của Krum và beta của trung bình cắt đều cần con số đó
- n ≥ 2f + {{s044}}, nếu không thì số láng giềng n−f−2 không còn đủ để bảo đảm có láng giềng lành trong tập so

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Sai số của trung vị theo toạ độ tăng theo số chiều, nên điểm đổ vỡ {{s068}} không có nghĩa là không mất gì ở mô hình lớn

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Server lấy n = {{s004}} client mỗi vòng và dùng Krum. Theo điều kiện tồn tại của Krum, số kẻ xấu tối đa chịu được là bao nhiêu?

*Module {{s069}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s070}} | kẻ xấu | module {{s069}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trần nguyên lý cho MỌI bộ tổng hợp, kể cả bộ chưa được phát minh: tỉ lệ kẻ xấu f/n phải nhỏ hơn giá trị nào thì mới còn hy vọng bền?

*Module {{s069}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s023}} |  | module {{s069}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Điều kiện tồn tại của Krum là n ≥ 2f + {{s044}}. Muốn chịu được đúng một kẻ xấu thì cần tối thiểu bao nhiêu client mỗi vòng?

*Module {{s069}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s033}} | client | module {{s069}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một hệ cross-silo chỉ có {{s071}} site và site nào cũng dự mỗi vòng. Krum chịu được tối đa bao nhiêu site xấu?

n = {{s071}}

## Đáp
@phut: 1
@che-do: so

`Math.floor((n - {{s044}}) / {{s003}})`

Bằng {{s072}}, vì ({{s071}} − 3)/2 = {{s072}} đúng. Hai điều phải đọc. Một, tỉ lệ chịu được là {{s072}} trên {{s071}}, tức khoảng {{s073}}, chưa tới một nửa đúng như trần nguyên lý đòi. Hai, và đây là chỗ hay sai: con số {{s072}} là chặn TỒN TẠI của thuật toán, không phải tỉ lệ kẻ xấu mà bài của anh đo được.

## Đáp (tiếp)
@phut: 1
@che-do: so

Dùng nó làm tuyên bố thực nghiệm là nhầm một chặn lý thuyết với một kết quả, vì ở gần chặn đó độ chính xác đã tụt từ lâu trước khi thuật toán ngừng chạy.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Krum chạy với {{s004}} client mỗi vòng và chặn trên của số kẻ xấu đặt là {{s066}}. Điểm Krum của mỗi client lấy tổng trên bao nhiêu láng giềng?

n = {{s004}}, f = {{s066}}

## Đáp
@phut: 1
@che-do: so

`n - f - {{s003}}`

## Đáp (tiếp)
@phut: 1
@che-do: so

Bằng {{s074}} láng giềng. Để ý con số này giảm khi anh khai f bi quan hơn: khai f = {{s070}} thì chỉ còn {{s010}} láng giềng, và khai f = {{s075}} với n = {{s004}} thì điều kiện n ≥ 2f+3 vỡ. Nên chặn trên của f không phải một tham số an toàn miễn phí: khai cao cho chắc là tự thu hẹp tập so sánh, và tới một mức thì thuật toán không còn định nghĩa được.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`byte gom trong D ngày = S·V·D ; byte liên bang trong R vòng = 2·S·R·M ; lấy D = R thì tỉ số = V/(2·M), KHÔNG phụ thuộc S và R`

## Giả thiết
@phut: 1
@che-do: so

- S là số site, V là lưu lượng mỗi site mỗi ngày, M là kích thước mô hình, R là số vòng, và một vòng ứng với một ngày
- Không nén, không lọc trước khi gửi, và cập nhật có cùng kích thước với mô hình; nén hoặc lượng tử hoá làm tỉ số tăng, lọc tại nguồn làm tỉ số giảm

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Mọi site dự mọi vòng, tức chế độ cross-silo; với cross-device lấy mẫu tỉ lệ C thì vế liên bang nhân thêm C
- Hệ số {{s003}} là vì mỗi vòng mỗi site tải mô hình XUỐNG rồi tải cập nhật LÊN; bỏ một chiều là tự cho mình lợi thế gấp đôi

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Theo bảng phân biệt hai chế độ FL, số client của chế độ cross-silo nằm trong khoảng từ hai tới khoảng bao nhiêu?

*Module {{s076}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s004}} | client | module {{s076}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Chế độ cross-device có số client lên tới bậc mười luỹ thừa bao nhiêu? Nhập số mũ.

*Module {{s076}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s009}} | số mũ của mười | module {{s076}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mười site, mỗi site sinh {{s009}} GB mỗi ngày, mô hình {{s066}} MB, huấn luyện {{s004}} vòng với một vòng mỗi ngày. Gom tốn gấp mấy lần liên bang?

soSite = {{s009}}, luuLuong = {{s009}}, soVong = {{s004}}, moHinh = {{s066}}

## Đáp
@phut: 1
@che-do: so

`soSite × luuLuong × soVong / ((soSite × soVong × moHinh + soSite × soVong × moHinh) / {{s077}})`

## Đáp (tiếp)
@phut: 1
@che-do: so

{{s078}} lần: gom tốn {{s079}} GB còn liên bang tốn {{s080}} GB. Đây là con số phải có trong bài để trả lời câu phản biện kinh điển. Nhưng phải đọc kèm phép rút gọn: tỉ số bằng lưu lượng chia hai lần kích thước mô hình, nên nó không phụ thuộc số site và không phụ thuộc số vòng. Câu nhiều site thì liên bang càng đáng giá là một câu không có cơ sở trong công thức này.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mỗi site sinh {{s009}} GB mỗi ngày. Mô hình phải lớn tới bao nhiêu MB thì liên bang tốn bằng đúng gom, tức tỉ số byte bằng 1?

luuLuong = {{s009}}

## Đáp
@phut: 1
@che-do: so

`luuLuong × {{s077}} / {{s003}}`

{{s081}} MB, tức một mô hình {{s033}} GB. Con số này là điểm đảo chiều của cả lập luận băng thông: mô hình lớn hơn thế thì gom RẺ HƠN liên bang, và câu trả lời quen thuộc cho câu phản biện không dùng được nữa. Điều kiện tổng quát là lưu lượng mỗi site mỗi ngày nhỏ hơn hai lần kích thước mô hình.

## Đáp (tiếp)
@phut: 1
@che-do: so

Với mô hình thị giác hay mô hình ngôn ngữ cỡ vài trăm MB tới vài GB đặt cạnh các site chỉ sinh siêu dữ liệu luồng, hệ rơi vào vùng đảo chiều dễ hơn nhiều người tưởng, nên phải kiểm phân số này trước khi viết phần biện minh.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`min_{w_k} F_k(w_k) + (λ/2)·||w_k - w⋆||² ⇒ w_k = (θ̂_k + λ·w⋆)/(1+λ) ⇒ E||w_k - θ_k||² = (s + λ²·d_k²)/(1+λ)² với λ⋆ = s/d_k²`

## Giả thiết
@phut: 1
@che-do: so

- F_k xấp xỉ bậc hai với Hessian đơn vị quanh nghiệm cục bộ, nên nghiệm Ditto có dạng đóng. Mạng neural và KAN không thoả giả thiết này, nên dạng đóng là công cụ lấy trực giác chứ không phải một bảo đảm
- θ̂_k = θ_k + e_k với E[e_k] = {{s030}} và E||e_k||² = s, trong đó s = σ²/n_k là sai số ước lượng cục bộ, nên s lớn khi client ít dữ liệu

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- w⋆ coi như nghiệm toàn cục chính xác: sai số ước lượng của nó nhỏ hơn s khoảng K lần nên bỏ qua được
- λ là siêu tham số do người làm chọn, không do dữ liệu quyết định, nên mọi so sánh phải khai dải dò λ
- d_k² là bình phương khoảng cách từ nghiệm cụm của client k tới w⋆, một tính chất của dữ liệu và cách phân vùng

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trong Ditto với F_k xấp xỉ bậc hai Hessian đơn vị, đặt λ bằng một. Hệ số co của số hạng không đồng nhất, tức (λ/(1+λ))², bằng bao nhiêu?

*Module {{s082}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s083}} |  | module {{s082}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Client chia thành bốn cụm cách nhau đều, khoảng cách giữa hai cụm liền nhau bằng một đơn vị. Γ_cụm, tức phương sai của phân bố đều rời rạc trên bốn điểm đó, bằng bao nhiêu?

*Module {{s082}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s084}} |  | module {{s082}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Ở chế độ FedAvg, tức λ rất lớn, với bốn cụm cách nhau δ = {{s017}} và hai trăm client. Khoảng cách giữa trung bình theo client và phân vị {{s009}} theo client bằng bao nhiêu điểm phần trăm?

*Module {{s082}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s058}} | điểm phần trăm | module {{s082}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Tổng số mẫu trong hệ là {{s085}}, chia cho {{s064}} client nên mỗi client có {{s087}} mẫu, và phương sai gradient σ² = {{s004}}. Client chia thành {{s044}} cụm cách nhau δ = {{s088}}. λ tối ưu bằng bao nhiêu?

sig2 = {{s004}}, K = {{s064}}, N = {{s085}}, del = {{s086}}, C = {{s044}}

## Đáp
@phut: 1
@che-do: so

`(sig2⋆K/N) / (del⋆del⋆(C⋆C-1)/12)`

Khoảng {{s089}}, tức λ tối ưu nằm quanh một chứ không ở hai đầu dải, vì s = {{s090}} và Γ_cụm = {{s091}} cùng bậc độ lớn. Nếu anh dò λ trên lưới gồm {{s092}} rồi {{s018}} rồi {{s031}} thì lưới đó không chứa điểm tối ưu, nên con số báo ra là của một λ chưa dò tới. Đó là lý do bảng kết quả phải khai DẢI dò chứ không chỉ khai rằng đã dò.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Bốn cụm cách nhau δ = {{s017}}, hai trăm client, tổng mẫu {{s085}}, σ² = {{s004}}. Chuyển từ FedAvg sang Ditto ở λ tối ưu làm TRUNG BÌNH theo client tăng bao nhiêu điểm phần trăm?

del = {{s023}}, C = {{s021}}, sig2 = {{s004}}, K = {{s063}}, N = {{s085}}

## Đáp
@phut: 1
@che-do: so

`10⋆Math.pow(del⋆del⋆(C⋆C-1)/12, {{s003}}) / (del⋆del⋆(C⋆C-1)/12 + sig2⋆K/N)`

Khoảng {{s093}} điểm phần trăm, và đó là mức tăng của TRUNG BÌNH theo client. Độ chính xác toàn cục không tăng một điểm nào, vì nó là phép đo của w⋆ và w⋆ không phụ thuộc λ. Công thức là 10·Γ²/(Γ + s), nên mức tăng bằng {{s030}} khi Γ = {{s030}}, tức một cụm, và tiến tới 10·Γ khi s tiến về {{s030}}, tức client nào cũng nhiều dữ liệu.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`T_vòng = max_{k∈S}(t_tính,k + t_truyền,k) · q_k = P(t_k ≤ D) · p̃_k = p_k·q_k / Σ_j p_j·q_j · cập nhật cũ τ vòng nhân 1/(1+τ)`

## Giả thiết
@phut: 1
@che-do: so

- Vòng là đồng bộ: server chờ tới khi mọi client trong S báo về hoặc tới hạn chờ D, rồi mới tổng hợp, nên thời gian vòng là max chứ không phải trung bình
- Server chuẩn hoá lại trọng số theo tập người về kịp, tức chia cho tổng trọng số của những client có mặt; đây là điều cài đặt thật làm và cũng là chỗ sinh ra thiên lệch

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- q_k chỉ phụ thuộc thiết bị và đường truyền, không phụ thuộc nội dung cập nhật; đây chính là giả thiết bị tắt ở công tắc thứ nhất
- Số client mỗi vòng đủ lớn để mẫu số tập trung quanh kỳ vọng, nên xấp xỉ bậc một của tỉ số kỳ vọng dùng được
- Hệ số hạ trọng số 1/(1+τ) chọn trước chứ không học, nên nó là một giả thiết thiết kế phải khai, không phải một kết quả

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Một vòng chọn {{s066}} client, thời gian mỗi client phân bố đều độc lập trên khoảng từ {{s080}} tới {{s034}} giây. Kỳ vọng của thời gian vòng, tức kỳ vọng của cực đại, bằng bao nhiêu giây?

*Module {{s094}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s095}} | giây | module {{s094}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Nhóm chậm chiếm tỉ lệ danh nghĩa {{s096}} của dữ liệu và chỉ về kịp hạn chờ với xác suất {{s097}}, còn nhóm nhanh về kịp chắc chắn. Sau khi server chuẩn hoá lại, trọng số hiệu dụng của nhóm chậm bằng bao nhiêu?

*Module {{s094}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s098}} |  | module {{s094}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Số client mỗi vòng tăng từ {{s009}} lên {{s004}}, thời gian mỗi client vẫn phân bố đều độc lập trên khoảng từ {{s080}} tới {{s034}} giây. Thời gian vòng kỳ vọng tăng thêm bao nhiêu giây?

*Module {{s094}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s099}} | giây | module {{s094}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Nhóm chậm có trọng số danh nghĩa {{s097}} và về kịp với xác suất {{s096}}; nhóm nhanh về kịp với xác suất {{s102}}. Trọng số hiệu dụng của nhóm chậm bằng bao nhiêu phần trăm trọng số danh nghĩa của nó?

pc = {{s083}}, qc = {{s100}}, qn = {{s101}}

## Đáp
@phut: 1
@che-do: so

`100⋆qc/((1-pc)⋆qn + pc⋆qc)`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s103}} trọng số danh nghĩa. Nhóm chậm khai {{s104}} dữ liệu nhưng chỉ còn {{s105}} sức nặng trong tổng hợp, nên hệ đang tối thiểu hoá một tổng khác với tổng viết trong phần phương pháp. Con số phải vào bài là tỉ số này chứ không phải tỉ lệ client bị bỏ: ở cấu hình mặc định của mô phỏng, tỉ lệ bỏ là {{s015}} trong khi tỉ số này bằng {{s106}}, nên hai con số đo hai thứ khác nhau.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Hạn chờ {{s107}} giây là cái chặn thời gian vòng, và server mất thêm {{s108}} giây tổng hợp mỗi vòng. Bao nhiêu vòng mỗi giờ?

han = {{s107}}, tth = {{s108}}

## Đáp
@phut: 1
@che-do: so

`3600/(han + tth)`

Khoảng {{s109}} vòng mỗi giờ, nên một thí nghiệm {{s055}} vòng cần khoảng {{s110}} giờ đồng hồ treo tường. Bảng cấu hình ghi {{s055}} vòng không nói gì về chi phí đó, vì số vòng là đại lượng không có đơn vị thời gian. Hai đại lượng phải khai cạnh nó là hạn chờ và thời gian tổng hợp của server, và cả hai đều là lựa chọn của người làm chứ không phải tính chất của thuật toán.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: tiêu chí là thời gian dẫn, không phải đáp đúng.

Số nào dẫn lại quá ba mươi giây thì nó chưa thuộc, dù đáp đúng.
