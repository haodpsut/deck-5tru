---
tieu-de: Hội tụ: đọc được bound chứ không chỉ trích nó
phu-de: Trụ 2 FL · module 2.3
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 80
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

Trong bound của FedAvg, tăng E làm số hạng nào phình, và bound đó có áp được cho mô hình của tôi không?

## Hội tụ: đọc được bound chứ không chỉ trích nó
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Bound hội tụ của FedAvg trên dữ liệu non-IID gần như luôn được trích từ cùng một chỗ, và gần như luôn bị trích sai cùng một kiểu: lấy kết luận mà bỏ bốn giả thiết, rồi dán nó lên một mạng neural.

## Hội tụ: đọc được bound chứ không chỉ trích nó (tiếp)
@phut: 1
@che-do: noi

Module này không dạy chứng minh bound. Nó dạy ba việc mà một phản biện sẽ hỏi: **Đọc được `B` theo số hạng:** số hạng nào mua được bằng batch lớn hơn, số hạng nào mua được bằng thuật toán, và số hạng nào **không mua được bằng gì** vì nó là tính chất của dữ liệu. **Đọc đúng biến đếm:** `T` trong bound là **tổng số bước SGD cục bộ**, không phải số vòng truyền. Số vòng truyền là `T/E`.

## Hội tụ: đọc được bound chứ không chỉ trích nó (tiếp)
@phut: 1
@che-do: noi

Đọc nhầm chỗ này làm cả câu chuyện về epoch cục bộ đảo chiều. **Biết bound chết ở đâu:** tắt lồi mạnh thì `kappa = L/mu` không tồn tại và bound **không còn định nghĩa được**, không phải xấu hơn. Đây là ca mẫu đúng cho lớp lỗi hằng số sai thuộc. Phần đáng giá nhất của module là khối công tắc.

## Hội tụ: đọc được bound chứ không chỉ trích nó (tiếp)
@phut: 1
@che-do: noi

Nếu anh chỉ nhớ một thứ từ đây, hãy nhớ rằng câu *chúng tôi bảo đảm hội tụ cho mạng neural vì chúng tôi trích bound này* là một phát biểu sai thẩm quyền, và nó sai kể cả khi mọi con số trong bài đều đúng.

## Ba số hạng của B, xếp theo thứ mua được
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Ba số hạng của B, xếp theo thứ mua được · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`B = sum_k p_k^2 sigma_k^2 + 6·L·Gamma + 8(E-1)^2·G^2`. Ba số hạng, ba cách xử khác nhau: `sum_k p_k^2 sigma_k^2` là phương sai gradient ngẫu nhiên. **Mua được bằng batch lớn hơn**, vì sigma_k^2 giảm theo cỡ batch. Để ý nó có p_k^2, nên lệch số lượng làm nó tăng ngay cả khi mọi sigma_k bằng nhau. `6·L·Gamma` với `Gamma = F⋆ - sum_k p_k F_k⋆` là độ không đồng nhất. **Không mua được bằng thuật toán**:

## Ba số hạng của B, xếp theo thứ mua được · đáp (tiếp)
@phut: 1
@che-do: noi

nó là tính chất của dữ liệu và của phân vùng. `8(E-1)^2·G^2` là giá của bước cục bộ. Phình **bậc hai theo E**. **Điểm phải nhớ:** chỉ số hạng thứ nhất là thứ anh mua được bằng tiền tính toán, và chỉ số hạng thứ ba là thứ anh mua được bằng cách đổi cấu hình. Số hạng giữa thì không:

## Ba số hạng của B, xếp theo thứ mua được · đáp (tiếp)
@phut: 1
@che-do: noi

một thuật toán tổng hợp tốt hơn không làm `Gamma` nhỏ đi, vì `Gamma` đã được định nghĩa qua các giá trị tối ưu chứ không qua đường đi của thuật toán. Câu *phương pháp của chúng tôi giảm độ không đồng nhất* là một câu cần kiểm rất kỹ.

## T trong bound đếm cái gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s002}} trên bốn.*

## T trong bound đếm cái gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`T` là **tổng số bước SGD cục bộ** đã chạy, và truyền thông xảy ra mỗi `E` bước, nên **số vòng truyền là `T/E`**.

## T trong bound đếm cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** vì bound chỉ phạt `E` qua `B`, đọc `T` là số vòng cho kết luận *tăng E luôn luôn tệ*.
Đọc đúng `T` là số bước thì số vòng cần tỉ lệ với `B(E)/E`, và vì `B` có hằng số không phụ thuộc `E`, đại lượng đó **có cực tiểu**.
Tối thiểu hoá cho `E⋆ = sqrt(1 + (sum_k p_k^2 sigma_k^2 + 6L·Gamma)/(8G^2))`.

## T trong bound đếm cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

Đó chính là lời giải thích định lượng cho câu quen tai *tăng epoch cục bộ giúp giảm số vòng nhưng tới một mức thì hỏng*, và nó nói thêm một điều ít ai nói:
**mức đó lớn khi dữ liệu lệch nặng**, vì `Gamma` nằm ở tử số.

## Bốn giả thiết
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Bốn giả thiết · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bốn giả thiết phải nhớ cả bốn: **mu-lồi mạnh**, **L-trơn**, **phương sai gradient bị chặn**, **chuẩn gradient bị chặn bởi G**. Cộng thêm hai điều kiện khung hay bị bỏ: client tham gia đầy đủ, và trọng số `p_k` cố định.

## Bốn giả thiết · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** giả thiết loại mạng neural ra là **lồi mạnh**, và cách nó loại không phải là làm bound rộng hơn mà là làm bound **không còn phát biểu được**:
`mu = {{s004}}` thì `kappa = L/mu` không tồn tại, `gamma = max{8kappa, E}` không tồn tại, và cả hai vế của bất đẳng thức mất nghĩa.
Nên với một CNN, bound này không phải là một bảo đảm yếu, nó **không phải một bảo đảm**.

## Bốn giả thiết · đáp (tiếp)
@phut: 1
@che-do: noi

Thêm một chuyện đáng biết để trả phản biện:
lồi mạnh cộng chuẩn gradient bị chặn trên toàn miền là hai giả thiết **chỏi nhau** trên miền không bị chặn, vì gradient của hàm lồi mạnh lớn tuỳ ý khi ra xa nghiệm.
Nên bound này còn chịu một phê phán nội bộ ngay cả trong lớp hàm của chính nó.

## Công thức và giả thiết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`E[F(w_T)] - F⋆ ≤ (kappa/(gamma + T - 1))·( 2B/mu + (mu·gamma/2)·||w_1 - w⋆||^2 ), kappa = L/mu, gamma = max{8·kappa, E}`

**Giả thiết nó đứng trên:**

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- F là mu-LỒI MẠNH. Đây là giả thiết loại mạng neural ra khỏi tầm, và khi nó tắt thì kappa cùng cả bound KHÔNG CÒN ĐỊNH NGHĨA ĐƯỢC
- F là L-TRƠN, tức gradient Lipschitz với hằng số L; không có L thì cả kappa và số hạng 6L·Gamma mất nghĩa
- Phương sai gradient ngẫu nhiên của client k bị chặn bởi sigma_k^2

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- Chuẩn gradient ngẫu nhiên bị chặn bởi G trên toàn miền; lưu ý giả thiết này chỏi với lồi mạnh trên miền không bị chặn
- T đếm TỔNG SỐ BƯỚC SGD cục bộ, không phải số vòng truyền; số vòng truyền là T/E
- Mọi client tham gia MỌI vòng, và trọng số p_k cố định. Lấy mẫu một phần client thêm số hạng riêng, không nằm trong B này

## Công thức · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Để ý vế phải có hai cục: cục `2B/mu` là giá của ngẫu nhiên cộng non-IID cộng bước cục bộ, còn cục `(mu·gamma/2)||w_1 - w⋆||^2` là giá của điểm khởi tạo. Khi `T` lớn thì cả hai chia cho `T`, nên tốc độ là `O(1/T)`. Điều đó cũng nói rằng bound này **không** cho hội tụ hàm mũ: nó là bound `O(1/T)` cho bước học giảm dần, không phải bound tuyến tính của gradient descent toàn phần trên hàm lồi mạnh.

## Ba số hạng của B, và định nghĩa của Gamma
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`B = sum_k p_k^2·sigma_k^2 + 6·L·Gamma + 8(E-1)^2·G^2, Gamma = F⋆ - sum_k p_k·F_k⋆`

**Giả thiết nó đứng trên:**

## Ba số hạng của B, và định nghĩa của Gamma (tiếp)
@phut: 1
@che-do: so

- Gamma định nghĩa qua các GIÁ TRỊ TỐI ƯU F⋆ và F_k⋆, nên nó không phụ thuộc thuật toán, không phụ thuộc khởi tạo và không phụ thuộc E
- Gamma ≥ {{s004}} luôn đúng, vì F⋆ là cực tiểu của tổ hợp lồi của các F_k nên không nhỏ hơn tổ hợp các cực tiểu riêng
- Gamma = {{s004}} khi mọi F_k có cùng tập cực tiểu, mà trường hợp quen nhất của điều đó là dữ liệu IID

## Ba số hạng của B, và định nghĩa của Gamma (tiếp)
@phut: 1
@che-do: so

- Trọng số p_k là hằng số, tổng bằng {{s005}}; với p_k = 1/K đồng đều thì số hạng thứ nhất bằng sigma^2/K

## Ba số hạng của B, và định nghĩa của Gamma · ghi chú
@phut: 1
@che-do: noi

Hai trường hợp biên nên dùng để kiểm mọi cài đặt tính `B`: dữ liệu IID với gradient đầy đủ và `E = {{s005}}` cho `B = {{s004}}` đúng bằng {{s004}}, còn `E = {{s005}}` một mình đã triệt tiêu số hạng thứ ba vì `(E-1)^2 = {{s004}}`. Nếu bộ tính của anh không cho hai số đó thì nó sai, và đây là phép thử rẻ nhất.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s001}} | bậc | Trong B, số hạng chứa số bước cục bộ phình theo nó
!so {{s005}} |  | Bốn client, trọng số tổng hợp đồng đều, mỗi client có sigma_k
!so {{s006}} |  | Lấy L = {{s005}} và mu = {{s007}} nên kappa = L/mu.

## Lấy L = 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Lấy L = {{s005}}, {{s008}} client trọng số đồng đều, sigma_k = {{s005}}, Gamma = {{s005}}, G = {{s005}}, E = {{s009}}. B bằng bao nhiêu?

sig = {{s005}}, K = {{s008}}, L = {{s005}}, Gam = {{s005}}, E = {{s009}}, G = {{s005}}

## Lấy L = 1 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`sig⋆sig/K + 6⋆L⋆Gam + 8⋆Math.pow(E-1,2)⋆G⋆G`

B = {{s010}}, tách ra thành {{s011}} cộng {{s012}} cộng {{s013}}. Số hạng epoch một mình là {{s013}}, tức {{s014}} của B, nên ở cấu hình này bound nói về giá của bước cục bộ chứ không nói về non-IID. Đổi E về {{s005}} thì B tụt xuống {{s015}}, tức giảm {{s016}} lần, trong khi mọi tham số dữ liệu giữ nguyên.

## Giữ nguyên mọi thứ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Giữ nguyên mọi thứ, tăng số bước cục bộ từ {{s001}} lên {{s017}}. Số hạng 8(E-1)^2 G^2 nhân lên bao nhiêu lần?

E1 = {{s001}}, E2 = {{s017}}

## Giữ nguyên mọi thứ · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.pow((E2-1)/(E1-1), {{s001}})`

{{s018}} lần, vì tỉ số là ((6-1)/(2-1))^2 = 5^2. Đây là nội dung thực tế của chữ bậc hai: nhân số bước cục bộ lên {{s002}} lần thì số hạng đó nhân lên {{s018}} lần, không phải {{s002}} lần. Hai số hạng kia không đổi một chút nào, nên toàn bộ phần phình của B đến từ đúng một chỗ.

## Trong bound này
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong bound này, T đếm cái gì, và số vòng truyền bằng gì?

- T đếm số epoch trên toàn bộ dữ liệu, nên số vòng truyền bằng T·E
- T đếm số client đã tham gia tích luỹ qua các vòng
- T đếm số vòng truyền, nên số vòng truyền bằng T
- T đếm tổng số bước SGD cục bộ, nên số vòng truyền bằng T/E

## Trong bound này · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**T đếm tổng số bước SGD cục bộ, nên số vòng truyền bằng T/E**

## Trong bound này · đáp (tiếp)
@phut: 1
@che-do: noi

Truyền thông xảy ra mỗi E bước cục bộ, nên số vòng là T/E. Đọc sai chỗ này đổi hẳn kết luận: với T là số bước thì số vòng tỉ lệ với B(E)/E và có cực tiểu tại E⋆ = sqrt(1 + A/(8G^2)); với T hiểu là số vòng thì phép chia cho E mất và kết luận thành tăng E luôn luôn tệ, tức xoá mất đúng cái hiện tượng mà thực nghiệm quan sát được.

## Tắt giả thiết lồi mạnh. Điều gì xảy ra với bound?
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Tắt giả thiết lồi mạnh. Điều gì xảy ra với bound?

- Bound vẫn đúng nhưng lỏng hơn, hằng số xấu đi theo bậc
- Bound vẫn đúng với mu thay bằng {{s004}}, cho một bound O(1/sqrt(T))
- kappa = L/mu và cả bound không còn định nghĩa được, nên không còn bảo đảm nào
- Bound chỉ còn đúng cho E = {{s005}}

## Tắt giả thiết lồi mạnh. Điều gì xảy ra với bound? · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**kappa = L/mu và cả bound không còn định nghĩa được, nên không còn bảo đảm nào**

mu = {{s004}} làm kappa = L/mu và gamma = max{8kappa, E} không tồn tại, và vế phải có 2B/mu, nên cả bất đẳng thức mất nghĩa. Phương án đầu là cách hiểu sai phổ biến nhất và cũng là cách hiểu làm người ta viết bảo đảm hội tụ cho CNN. Phương án thứ hai trộn hai định lý khác nhau:

## Tắt giả thiết lồi mạnh. Điều gì xảy ra với bound? (tiếp)
@phut: 1
@che-do: noi

bound O(1/sqrt(T)) cho trường hợp lồi hoặc phi lồi là một kết quả riêng với giả thiết riêng, không thu được bằng cách đặt mu = {{s004}} vào bound này. Phương án cuối là hệ quả của việc tắt chặn gradient, không phải của việc tắt lồi mạnh.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phân tích sau có một câu là phát biểu sai thẩm quyền. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Theo Li và cộng sự, bound hội tụ của FedAvg có dạng O(1/T) với B = sum_k p_k^2 sigma_k^2 + 6L·Gamma + 8(E-1)^2 G^2,
- trong đó số hạng cuối phình bậc hai theo số bước cục bộ,
- do đó mô hình CNN của chúng tôi được bảo đảm hội tụ tới nghiệm toàn cục với E = {{s009}}.
- Chúng tôi chọn E = {{s009}} và báo đường cong hội tụ trên {{s002}} hạt trong Hình {{s017}}.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**do đó mô hình CNN của chúng tôi được bảo đảm hội tụ tới nghiệm toàn cục với E = {{s009}}.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu đầu trích đúng và phát biểu đúng. Câu thứ ba mượn thẩm quyền của một định lý mà tiền đề không áp: bound đòi hàm mục tiêu mu-lồi mạnh, còn CNN thì không, nên kappa = L/mu không tồn tại và bound không phải là một phát biểu về mô hình này. Để ý thêm là câu đó còn nói tới nghiệm toàn cục, thứ mà cả bài toán phi lồi cũng không bảo đảm được. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

giữ hai câu đầu, đổi câu ba thành một câu về trực giác, ví dụ bound trong trường hợp lồi mạnh cho thấy giá của bước cục bộ là bậc hai theo E, và chúng tôi dùng điều đó để chọn E, rồi kiểm bằng thực nghiệm; nếu cần một bảo đảm thật thì phải dẫn bound phi lồi và nhận rằng nó chỉ nói về điểm dừng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thảo luận sau có một câu gán cho thuật toán một thứ nó không với tới. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Số hạng 6L·Gamma với Gamma = F⋆ - sum_k p_k F_k⋆ đo độ không đồng nhất giữa các client,
- và nó bằng {{s004}} khi mọi client có cùng tập cực tiểu, trường hợp quen nhất là dữ liệu IID,
- nên bộ tổng hợp có trọng số thích ứng của chúng tôi làm giảm Gamma và do đó làm bound chặt hơn.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên bộ tổng hợp có trọng số thích ứng của chúng tôi làm giảm Gamma và do đó làm bound chặt hơn.**

Gamma được định nghĩa qua các GIÁ TRỊ TỐI ƯU F⋆ và F_k⋆, nên nó không phụ thuộc thuật toán, không phụ thuộc khởi tạo, không phụ thuộc E. Một bộ tổng hợp mới không chạm tới nó được. Hai câu đầu đều đúng. Có một lối thoát hẹp mà nếu dùng thì phải khai thẳng:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

đổi trọng số p_k thì đổi chính hàm F mà ta tối ưu, nên F⋆ đổi và Gamma đổi theo, nhưng lúc đó bài toán đã khác bài toán đã phát biểu, nên không được gọi đó là bound chặt hơn cho cùng một bài toán. Cách sửa: nói bộ tổng hợp giảm ảnh hưởng của trôi cục bộ, một đại lượng về đường đi, và đừng nói nó giảm Gamma.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Số hạng thứ nhất sum_k p_k^2 sigma_k^2 không chứa E, nên tăng E không đổi nó
- Số hạng thứ hai 6·L·Gamma không chứa E, và cũng không chứa gì của thuật toán
- Số hạng thứ ba 8(E-1)^2·G^2 là số hạng DUY NHẤT chứa E, và nó bậc hai theo E-1
- Vậy tăng E từ E_1 lên E_2 nhân số hạng thứ ba lên ((E_2-1)/(E_1-1))^2 lần, hai số hạng kia giữ nguyên

## Dẫn lại từng bước · ca một (tiếp)
@phut: 1
@che-do: so

- Mốc đổi chế độ: số hạng thứ ba vượt hai số hạng kia cộng lại khi E vượt {{s005}} + sqrt((sum_k p_k^2 sigma_k^2 + 6L·Gamma)/(8G^2))

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt epsilon là mức mục tiêu. Giải (kappa/(gamma+T-1))·(2B/mu + (mu·gamma/2)·D) = epsilon ra T, với D = ||w_1 - w⋆||^2
- T tỉ lệ với B khi epsilon nhỏ, vì số hạng 2B/mu chi phối cục khởi tạo
- T đếm BƯỚC SGD, nên số vòng truyền là R = T/E, tỉ lệ với B(E)/E
- Viết A = sum_k p_k^2 sigma_k^2 + 6L·Gamma, thì B(E)/E = (A + 8(E-1)^2 G^2)/E, lấy đạo hàm theo E và cho bằng {{s004}}

## Dẫn lại từng bước · ca hai (tiếp)
@phut: 1
@che-do: so

- Nghiệm là E⋆ = sqrt(1 + A/(8G^2)), tức số epoch tối ưu TĂNG khi dữ liệu lệch nặng hơn

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: B = {{s010}} · kappa = {{s008}} · gamma = {{s006}} · T = {{s001}} {{s019}} {{s020}} bước SGD · {{s021}} {{s022}} vòng truyền ở E = {{s009}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **F là mu-lồi mạnh** tắt đi: Mô hình là CNN, hoặc KAN, hoặc transformer, tức hàm mục tiêu không lồi và không có mu dương nào.
- **F là L-trơn** tắt đi: Hàm mất mát có chỗ gradient không Lipschitz, ví dụ có ReLU trên miền không bị chặn, hoặc có chuẩn hoá làm Hessian nổ ở một vùng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Phương sai gradient ngẫu nhiên bị chặn bởi sigma_k^2** tắt đi: Nhiễu gradient đuôi nặng, hoặc batch quá nhỏ trên dữ liệu rất lệch nên phương sai không chặn được đều.
- **Chuẩn gradient bị chặn bởi G** tắt đi: Không có chặn đều trên toàn miền, điều này gần như luôn đúng trên miền không bị chặn.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Chính bound đó, ở dạng kéo được. L đã chuẩn hoá về {{s005}} nên kappa = 1/mu, và mục tiêu đặt ở epsilon = {{s023}} với ||w_1 - w⋆||^2 = {{s005}}. Kéo E và Gamma trước, rồi để ý rằng số vòng truyền KHÔNG đi cùng chiều với B.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.3` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III cites the FedAvg convergence bound of Li et al. (ICLR {{s024}}) and concludes that the proposed method inherits a convergence guarantee. That bound assumes a mu-strongly convex and L-smooth objective, while the model in Section IV is a convolutional network. Since kappa equals L over mu, the bound is not merely loose in this setting, it is undefined. Please either remove the guarantee claim or provide an analysis valid for your function class.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept the point and have removed the guarantee claim. Section III now states explicitly that the Li et al. bound assumes a mu-strongly convex and L-smooth objective, that our model does not belong to that class, and that under mu equal to zero the condition number kappa is undefined, so the bound is not a statement about our setting. We keep the bound in a clearly labelled role, as the source of two structural readings that we then test rather than assume:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

that the cost of local work enters as 8(E-1)^2 G^2, hence quadratically in E, and that the heterogeneity term {{s017}} L Gamma is a property of the data partition that no aggregation rule changes, since Gamma is defined through optimal values.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

For a statement valid in our function class we now cite a nonconvex smooth analysis and state its weaker conclusion, convergence to an approximate stationary point, together with its own assumptions including the participation condition, which the strongly convex theorem we previously cited also required and which our experiments at participation rate {{s025}} did not satisfy. Finally we turned the borrowed intuition into a falsifiable prediction.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The bound implies an optimal number of local steps E⋆ equal to the square root of one plus A over {{s026}} G squared, with A the sum of the variance and heterogeneity terms, so E⋆ should increase with heterogeneity.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Section V-D sweeps E over eight values at two Dirichlet levels and reports that the empirical optimum moves from {{s003}} to {{s027}} as alpha falls from {{s028}} to {{s025}}, which is consistent in direction with the prediction, and we also report that the magnitude is not predicted correctly, since the bound is not valid for our class.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: trả lời rằng bound được trích chỉ để tham khảo và rằng thực nghiệm cho thấy hội tụ. Không trả lời được phản bác, vì câu bảo đảm vẫn còn trong bài và vì quan sát thực nghiệm không phải một bảo đảm.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: bỏ chữ bảo đảm, giữ phần trích bound như động lực. Đã hết phát biểu sai thẩm quyền nhưng còn nợ: bài vẫn chưa nói gì được về hội tụ cho lớp hàm thật của nó.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: làm mức {{s001}}, cộng dẫn một kết quả hội tụ cho trường hợp phi lồi và trơn, nói rõ nó chỉ bảo đảm tới điểm dừng xấp xỉ chứ không tới cực tiểu toàn cục, và khai rõ giả thiết mà kết quả đó cần, gồm cả điều kiện khung về tham gia đầy đủ hoặc lấy mẫu.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table VI reports the number of communication rounds to reach the target accuracy for several values of local epochs E, and the text explains the non-monotone shape by referring to the cited bound. However, in that bound T counts local SGD iterations rather than communication rounds, and the bound is monotone increasing in E. Please clarify which quantity your table reports and which quantity the bound constrains.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Table VI reports communication rounds, and we have corrected the accompanying text. In the cited bound T counts local SGD iterations, so the quantity the bound constrains is total local work, and the number of communication rounds is T divided by E. The bound is indeed monotone increasing in E through B, so it alone does not predict a minimum; the minimum appears in the ratio B(E) over E, because B contains a part that does not depend on E.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Writing A for the sum of the variance and heterogeneity terms, minimizing that ratio gives E⋆ equal to the square root of one plus A over {{s026}} G squared, which is the shape our table shows. We state in Section V-D that this reading stays inside the strongly convex class and therefore serves as intuition for our nonconvex model rather than as a bound on it.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table VI now reports both axes, communication rounds and total local SGD steps, because the two rank configurations differently: a cross-device deployment pays for rounds while an on-device energy budget pays for local steps, and a reader with the second cost model would draw the opposite conclusion from the first axis alone.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: trả lời rằng bảng báo số vòng truyền và bound cũng nói về số vòng. Sai về biến đếm, nên lời giải thích trong bài vẫn không khớp với công thức được trích.
- Mức {{s001}}: nhận rằng T là số bước SGD, sửa câu giải thích, nhưng chưa nói được vì sao đường cong có cực tiểu.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: làm mức {{s001}}, cộng chỉ rõ số vòng tỉ lệ với B(E)/E, cộng dẫn E⋆ = sqrt(1 + A/(8G^2)) và nói rõ cực tiểu tồn tại vì B có một phần không phụ thuộc E.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.3` bấm thẻ.
