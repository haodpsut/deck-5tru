---
tieu-de: Non-IID: đo nó bằng gì
phu-de: Trụ 2 FL · module 2.2
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 67.5
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

Tôi khai dữ liệu của tôi là non-IID bằng con số nào, và con số đó phải xuất hiện ở đâu trong bài?

## Chữ non-IID không phải một phép đo
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Câu *chúng tôi đánh giá trong điều kiện non-IID* không kiểm được. Nó không nói phân vùng được sinh thế nào, không nói lệch bao nhiêu, và quan trọng nhất là không nói lệch theo **kiểu nào**. Bốn kiểu lệch có hậu quả khác nhau tới mức ba kiểu đầu chỉ làm chậm hội tụ, còn kiểu thứ tư làm cho một mô hình toàn cục duy nhất **không còn là lời giải đúng**.

## Chữ non-IID không phải một phép đo (tiếp)
@phut: 1
@che-do: noi

Module này có hai việc. Việc thứ nhất là biết đúng ba con số phải có trong bài: cách phân vùng, tham số của nó, và một khoảng cách phân bố đo được như `TV`. Việc thứ hai, khó hơn, là biết **alpha là tham số của bộ sinh phân vùng chứ không phải tính chất của dữ liệu thật**. Trên dữ liệu IDS liên bang thì ranh giới client là ranh giới tổ chức, và không có alpha nào tồn tại cả.

## Bốn kiểu lệch, và vì sao kiểu thứ tư khác loại
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Bốn kiểu lệch, và vì sao kiểu thứ tư khác loại · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Viết phân bố của client `k` là `P_k(x, y) = P_k(y|x)·P_k(x)`. Bốn kiểu lệch: **lệch nhãn (label skew):** `P_k(y)` khác nhau. **lệch đặc trưng:** `P_k(x)` khác nhau. **lệch số lượng:** `n_k` khác nhau. **lệch quan hệ:** `P_k(y|x)` khác nhau giữa các client. **Điểm phải nhớ:** ba kiểu đầu giữ nguyên **hàm cần học**, chỉ đổi phân bố mà ta lấy mẫu từ đó, nên hậu quả là hội tụ chậm và phương sai lớn.

## Bốn kiểu lệch, và vì sao kiểu thứ tư khác loại · (tiếp)
@phut: 1
@che-do: noi

Kiểu thứ tư đổi chính hàm cần học, nên mô hình toàn cục tốt nhất là một thoả hiệp không tối ưu cho bất kỳ client nào. Đây là lằn ranh giữa FL và FL cá nhân hoá (personalisation), và nó phải được khai trong phần dựng bài toán chứ không phải trong phần kết quả.

## alpha của Dirichlet là tham số của cái gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## alpha của Dirichlet là tham số của cái gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Phân vùng Dirichlet lấy `p_k ~ Dir(alpha·1)` rồi chia một tập dữ liệu tập trung cho các client theo `p_k`. `alpha` nhỏ thì lệch nặng, `alpha` lớn thì tiến về IID.

## alpha của Dirichlet là tham số của cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** `alpha` là tham số của **bộ sinh phân vùng do anh viết**, không phải một đại lượng đo được trên dữ liệu thật.
Trên dữ liệu đã liên bang sẵn, ranh giới client là ranh giới tổ chức và không có `alpha` nào tồn tại; cái đo được là `TV(p_k, p)` của phân bố nhãn thật.

## alpha của Dirichlet là tham số của cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

Nên khai alpha là khai về **thí nghiệm mô phỏng** của anh, và nếu bài của anh nói về IDS liên bang thì câu đó phải đi kèm một câu nhận rằng phân vùng mô phỏng không phản ánh biên giới tổ chức.

## Số lớp hiệu dụng mỗi client
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Số lớp hiệu dụng mỗi client · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Nghịch đảo của chỉ số Simpson: nếu `p_k` là phân bố nhãn của client thì `m_k = {{s001}} / sum_c p_k(c)^2`. Nó bằng đúng số lớp khi phân bố đều trên các lớp đó, và bằng {{s001}} khi client chỉ có một lớp.

Với phân vùng `Dir(alpha·1)` trên `C` lớp, kỳ vọng của chỉ số Simpson có dạng đóng, nên **số lớp hiệu dụng (effective number of classes) kỳ vọng là `(C·alpha + 1)/(alpha + {{s001}})`**.

## Số lớp hiệu dụng mỗi client · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** công thức này cho ngay ba con số đáng nhớ với `C = {{s004}}`:
`alpha = {{s005}}` cho khoảng {{s006}} lớp, `alpha = {{s007}}` cho đúng {{s008}} lớp, `alpha = {{s009}}` cho khoảng {{s010}} lớp.
Nó cũng cho hai trường hợp biên kiểm được bằng tay:
`alpha` về {{s011}} cho {{s001}} lớp, `alpha` ra vô cùng cho `C` lớp.

## Số lớp hiệu dụng mỗi client · đáp (tiếp)
@phut: 1
@che-do: noi

Dùng nó thay cho câu *mỗi client giữ một hai lớp* thì phần thiết lập của anh có một con số chứ không có một cảm giác.

## Phân vùng Dirichlet
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`p_k ~ Dir(alpha·1_C) · TV(p_k, p) = (1/2)·sum_c |p_k(c) - p(c)| · E[sum_c p_k(c)^2] = (alpha+1)/(C·alpha+1) · m = 1/E[sum_c p_k(c)^2] = (C·alpha+1)/(alpha+1) · TV tương đương = (C-1)/(C·(alpha+1))`

**Giả thiết nó đứng trên:**

## Phân vùng Dirichlet (tiếp)
@phut: 1
@che-do: so

- Dirichlet ĐỐI XỨNG, tức cùng một alpha cho mọi lớp; nếu dùng alpha khác nhau theo lớp thì mọi công thức dưới đây sai
- Phân bố nhãn toàn cục p là đều trên C lớp; nếu tập gốc đã lệch lớp thì p không đều và TV phải tính với p thật
- Số lớp C biết trước và mọi client dùng CÙNG tập lớp

## Phân vùng Dirichlet (tiếp)
@phut: 1
@che-do: so

- Dòng TV tương đương là TV của một client giữ ĐỀU m lớp, với m là số lớp hiệu dụng ở trên. Nó KHÔNG phải kỳ vọng của TV dưới Dirichlet, mà là TV của một client đại diện có cùng chỉ số Simpson. Dùng nó để đọc bậc độ lớn thì được, dùng nó làm con số báo cáo thì phải khai đúng định nghĩa này

## Phân vùng Dirichlet · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hai trường hợp biên kiểm được bằng tay và nên dùng để bắt lỗi cài đặt bộ phân vùng: `alpha` về {{s011}} cho `m = {{s001}}` và `TV = (C-1)/C`, tức mỗi client đúng một lớp; `alpha` ra vô cùng cho `m = C` và `TV = {{s011}}`, tức IID. Nếu bộ phân vùng của anh không cho hai giới hạn đó thì nó sai, và đây là phép thử rẻ nhất mà hầu như không ai chạy.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s012}} | lớp | Dirichlet đối xứng với alpha = {{s005}} trên C = {{s004}} lớp.
!so {{s008}} | lớp | Cùng công thức, alpha = {{s007}} và C = {{s004}}. Số lớp
!so {{s013}} | TV | C = {{s004}} lớp

## Phân vùng Dirichlet đối xứng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phân vùng Dirichlet đối xứng, C = {{s004}} lớp, alpha = {{s007}}. Số lớp hiệu dụng kỳ vọng mỗi client bằng bao nhiêu?

C = {{s004}}, a = {{s014}}

## Phân vùng Dirichlet đối xứng · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(C⋆a+1)/(a+1)`

Đúng {{s015}} lớp trên {{s004}}, một con số tròn đáng nhớ. Nó khớp với câu lệch mạnh nhưng mọi lớp còn hiện diện: mọi lớp có xác suất dương, nhưng khối lượng tập trung vào bốn lớp. Để ý alpha = {{s005}} cho {{s016}} lớp, tức hai mức alpha này là hai chế độ khác nhau, không phải hai cách nói cùng một chuyện.

## C = 10 lớp
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

C = {{s004}} lớp, alpha = {{s018}}. TV tương đương so với phân bố nhãn đều bằng bao nhiêu?

C = {{s004}}, a = {{s017}}

## C = 10 lớp · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(C-1)/(C⋆(a+1))`

Đúng {{s019}}. Vậy mốc TV tương đương bằng một nửa ứng với alpha = (C-2)/C, bằng {{s018}} khi C = {{s004}}. Con số này đáng để trong đầu vì nó cho ngay một cách đọc: alpha dưới {{s018}} là vùng TV tương đương vượt {{s019}}, còn alpha = {{s009}} cho TV tương đương chỉ khoảng {{s020}}, tức gần IID.

## Bốn kiểu lệch dưới đây
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bốn kiểu lệch dưới đây, cái nào làm một mô hình toàn cục duy nhất KHÔNG còn là lời giải đúng, dù hội tụ hoàn hảo?

- Lệch quan hệ, P_k(y|x) khác nhau
- Lệch nhãn, P_k(y) khác nhau
- Lệch đặc trưng, P_k(x) khác nhau
- Lệch số lượng, n_k khác nhau

## Bốn kiểu lệch dưới đây · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Lệch quan hệ, P_k(y|x) khác nhau**

Ba kiểu đầu đổi phân bố lấy mẫu nhưng giữ nguyên hàm cần học, nên hậu quả là chậm và phương sai lớn. Lệch quan hệ đổi chính hàm cần học, nên bộ dự báo tối ưu khác nhau theo client và mô hình toàn cục tốt nhất là một thoả hiệp. Đây là lý do phần dựng bài toán phải khai kiểu lệch, không chỉ mức lệch.

## Dữ liệu IDS của anh đã liên bang sẵn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Dữ liệu IDS của anh đã liên bang sẵn: mỗi client là một tổ chức thật. Con số nào khai được về độ non-IID?

## Dữ liệu IDS của anh đã liên bang sẵn (tiếp)
@phut: 0.5
@che-do: hoi

- alpha của Dirichlet, bằng cách khớp phân vùng quan sát được với Dir(alpha·1)
- TV(p_k, p) và số lớp hiệu dụng, đo trực tiếp trên phân bố nhãn thật
- Không khai được gì, vì non-IID chỉ định nghĩa được cho phân vùng mô phỏng
- Độ chính xác của mô hình cục bộ so với mô hình toàn cục

## Dữ liệu IDS của anh đã liên bang sẵn · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**TV(p_k, p) và số lớp hiệu dụng, đo trực tiếp trên phân bố nhãn thật**

## Dữ liệu IDS của anh đã liên bang sẵn · đáp (tiếp)
@phut: 1
@che-do: noi

TV và chỉ số Simpson là đại lượng của phân bố, đo được trên bất kỳ phân vùng nào kể cả phân vùng không do bộ sinh nào tạo ra. alpha thì ngược lại: nó là tham số của bộ sinh, và khớp một alpha vào phân vùng tổ chức là áp một họ mô hình không có cơ sở. Phương án cuối là một phép đo hệ quả, không phải phép đo lệch:

## Dữ liệu IDS của anh đã liên bang sẵn · đáp (tiếp)
@phut: 1
@che-do: noi

nó trộn độ lệch với dung lượng mô hình và với số mẫu.

## Anh giữ alpha = 0,5 và C = 10
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh giữ alpha = {{s007}} và C = {{s004}}, tăng số client từ {{s021}} lên {{s022}}. Đại lượng nào đổi?

- Số lớp hiệu dụng mỗi client, giảm khoảng {{s004}} lần
- TV tương đương, tăng khoảng {{s004}} lần
- Chỉ số mẫu mỗi client, giảm {{s004}} lần; hai đại lượng kia không đổi
- Cả ba đại lượng đều đổi, vì Dirichlet phụ thuộc số client

## Anh giữ alpha = 0,5 và C = 10 · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chỉ số mẫu mỗi client, giảm {{s004}} lần; hai đại lượng kia không đổi**

Biên duyên của Dir(alpha·1_C) là Beta(alpha, (C-1)alpha), không chứa số client, nên cả số lớp hiệu dụng và TV tương đương giữ nguyên. Cái đổi là số mẫu mỗi client. Đây chính là lý do non-IID cần tối thiểu ba con số: mức lệch nhãn, số mẫu mỗi client, và kiểu lệch. Một bài chỉ khai alpha đã bỏ hai trục.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết lập sau có một câu không kiểm được. Bấm vào câu đó.

- Chúng tôi dùng CIC-IDS2017 với {{s004}} lớp tấn công và một lớp lành,
- chia cho {{s021}} client để mô phỏng điều kiện non-IID thực tế,
- mỗi client chạy {{s023}} epoch cục bộ, batch {{s024}},
- và chúng tôi chạy {{s025}} vòng với tỉ lệ tham gia {{s026}}.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**chia cho {{s021}} client để mô phỏng điều kiện non-IID thực tế,**

Câu này nói chia theo cách nào thì không, nói lệch bao nhiêu thì không, nói lệch kiểu nào thì không. Ba câu còn lại đều kiểm được: số lớp, số vòng, cấu hình huấn luyện. Cách sửa rẻ nhất là thêm cách phân vùng và tham số của nó, ví dụ Dirichlet đối xứng alpha = {{s007}}.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Cách sửa tốt hơn là thêm một con số ĐO ĐƯỢC trên phân vùng đã sinh, ví dụ TV trung bình hoặc số lớp hiệu dụng trung bình, vì con số đó còn đúng kể cả khi người đọc không tin bộ sinh của anh. Và nếu bài nói về IDS liên bang thật thì phải thêm một câu nhận rằng phân vùng mô phỏng này không phản ánh biên giới tổ chức.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết luận sau có một chỗ mở rộng một phép đo ra ngoài tầm của nó. Bấm vào chỗ đó.

- Ở alpha = {{s007}}, phương pháp của chúng tôi giữ được {{s027}} macro F1,
- so với {{s028}} của FedAvg,
- chứng tỏ phương pháp của chúng tôi bền với non-IID.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**chứng tỏ phương pháp của chúng tôi bền với non-IID.**

Hai câu đầu là phép đo tại MỘT điểm của MỘT kiểu lệch. Câu thứ ba suy ra một tính chất trên toàn trục, và trên cả những kiểu lệch chưa đo. Non-IID có ít nhất bốn kiểu và một trục cường độ, nên một alpha là một điểm trong không gian đó. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

hoặc quét alpha qua vài giá trị và báo đường cong rồi nói bền trong khoảng đã quét, hoặc giữ nguyên một điểm nhưng đổi câu kết luận thành ở mức lệch nhãn này, với kiểu lệch này. Để ý thêm: nếu lệch của hệ thật là lệch quan hệ thì không alpha nào chạm tới nó, nên câu bền với non-IID vẫn không mua được bằng cách quét alpha.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Biên duyên của Dirichlet đối xứng: p_k(c) ~ Beta(alpha, (C-1)·alpha), nên kỳ vọng là 1/C với mọi lớp c
- Phương sai của Beta(a, b) là a·b/((a+b)^2·(a+b+1)), nên Var[p_k(c)] = (C-1)/(C^2·(C·alpha+1))
- E[p_k(c)^2] = Var + bình phương kỳ vọng = (C-1)/(C^2·(C·alpha+1)) + 1/C^2
- Cộng C lớp: E[sum_c p_k(c)^2] = (alpha+1)/(C·alpha+1), nên số lớp hiệu dụng là (C·alpha+1)/(alpha+1)
- Kiểm hai biên: alpha về {{s011}} cho đúng {{s001}} lớp, alpha ra vô cùng cho đúng C lớp

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: C = {{s004}} · alpha = {{s007}} · {{s015}} lớp hiệu dụng mỗi client · TV tương đương {{s030}} · {{s004}} {{s031}} mẫu mỗi client

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **P(y|x) giống nhau giữa các client, chỉ P(x) và P(y) khác nhau** tắt đi: Có lệch quan hệ: cùng một luồng (flow) mạng được gán nhãn khác nhau ở hai site, vì chính sách của SOC khác nhau hoặc vì ngữ cảnh mạng khác nhau.
- **Phân vùng được sinh bằng Dirichlet đối xứng Dir(alpha·1)** tắt đi: Dữ liệu đã liên bang sẵn: ranh giới client là ranh giới tổ chức, chứ không do bộ sinh nào tạo ra.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi client dùng cùng một tập lớp** tắt đi: Site A chưa bao giờ thấy lớp tấn công thứ {{s029}}, và không chỉ là thấy ít mà là không có nhãn đó trong lược đồ.
- **Số mẫu mỗi client bằng nhau** tắt đi: Có lệch số lượng: n_k lệch nhau hàng chục lần, như lưu lượng giữa một trung tâm dữ liệu và một chi nhánh.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Phân vùng Dirichlet, đọc bằng số thay vì bằng cảm giác. Kéo alpha, số lớp, số client và tổng số mẫu. Để ý một chuyện sẽ dùng cho câu gãy: hai trong bốn thanh KHÔNG đổi được độ lệch nhãn của một client.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.2` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV states that the dataset is partitioned across {{s021}} clients to simulate a realistic non-IID setting, but the partition mechanism and its parameters are not given, and no distributional distance is reported. Please state the partition procedure, its parameter, and a measured statistic of the resulting label skew, so that the setting can be reproduced and compared against other papers.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Section IV-A now specifies the partition completely. We draw client label proportions from a symmetric Dirichlet with alpha equal to {{s014}} over the {{s004}} classes, with the partition seed fixed and the generating script released. Table II reports statistics measured on the generated partition rather than only the generator setting: mean total variation distance to the global label distribution, mean effective number of classes per client computed as the inverse Simpson index, and samples per client.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The measured effective class count is {{s032}} of {{s004}}, which matches the closed form (C alpha + 1)/(alpha + {{s001}}) for our C and alpha, and we report this agreement as a check that the partitioner behaves as intended. We also added the two boundary checks the closed form predicts: alpha approaching zero yields one effective class and total variation (C-1)/C, and large alpha yields C effective classes and total variation approaching zero. Finally we narrowed the claim. Our experiments vary label skew only.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Feature skew, quantity skew and concept shift, that is client-dependent P(y|x), are not covered, and we now say so in Section VI, together with the observation that a Dirichlet partition of a centralized corpus does not reproduce the organizational boundaries of a real federated intrusion detection deployment.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: thêm câu phân vùng theo Dirichlet với alpha = {{s007}}. Trả lời đúng phần cơ chế nhưng vẫn không có con số đo được trên phân vùng đã sinh, nên người đọc vẫn phải tin bộ sinh.
- Mức {{s002}}: thêm alpha, cộng thêm hạt ngẫu nhiên của bộ phân vùng và mã sinh phân vùng. Đã tái lập được, nhưng vẫn chưa có đại lượng so sánh giữa các bài.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: làm mức {{s002}}, cộng báo TV trung bình và số lớp hiệu dụng trung bình ĐO ĐƯỢC trên phân vùng đã sinh, cộng số mẫu mỗi client, và đối chiếu số đo được với giá trị kỳ vọng của dạng đóng để chứng tỏ bộ phân vùng chạy đúng.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The paper reports a single global model and a single aggregate accuracy figure. If labelling policy differs across the participating organizations, then P(y|x) differs across clients, and a single global model is not the Bayes-optimal predictor for any of them. What evidence do you have that concept shift is absent in your deployment, and if it is present, why is a single global objective the right formulation?

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree that a shared label schema is not evidence of a shared conditional distribution, so we measured it. Section V-F adds a pairwise transfer test: for each ordered pair of sites we train locally on one and evaluate on the other, and we report the drop relative to in-site evaluation.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We separate the part of that drop explained by label skew alone, estimated by repeating the same test on a Dirichlet partition of each site's own data at the measured skew level, from the residual, which we attribute to conditional shift. On our data the residual is {{s033}} points of macro F1, which is small relative to the {{s034}} points explained by label skew, so we keep the single global objective and now justify it with that measurement instead of with the shared schema.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also replaced the single aggregate figure: Table V reports the per-client distribution of accuracy with minimum, median and maximum, because an aggregate figure hides exactly the clients that a global compromise hurts. Finally we state the consequence of the alternative explicitly: if the residual had been large, the distance to a single global optimum would not be a defined quantity, since the optimal predictor differs per client, and the reporting unit itself would have to change rather than the numbers in it.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: trả lời rằng mọi client dùng cùng một lược đồ nhãn nên P(y|x) giống nhau. Lược đồ chung không phải bằng chứng về quan hệ nhãn và đặc trưng, nên câu này chưa trả lời được phản bác.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: công nhận có thể có lệch quan hệ, và báo thêm phân bố độ chính xác theo client thay vì chỉ một con số gộp. Đã trung thực hơn nhưng vẫn chưa đo được lệch quan hệ, cũng chưa biện hộ được cho mục tiêu toàn cục.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: làm mức {{s002}}, cộng một phép đo trực tiếp của lệch quan hệ, ví dụ huấn luyện cục bộ ở site A rồi đo mức tụt khi đánh giá ở site B theo hai chiều, cộng so mức tụt đó với mức tụt chỉ do lệch nhãn mô phỏng được.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.2` bấm thẻ.
