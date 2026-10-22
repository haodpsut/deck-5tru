---
tieu-de: Cá nhân hoá: khi một mô hình toàn cục là lời giải sai
phu-de: Trụ 2 FL · module 2.9
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 71.5
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

Bài của tôi nên báo độ chính xác toàn cục hay độ chính xác trên từng client, và hai con số đó khác nhau bao nhiêu?

## Hai con số
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module {{s001}} kết thúc ở một kết luận chưa có lối ra: khi `P(y|x)` khác nhau giữa các client thì **một mô hình toàn cục là lời giải sai**, bất kể thuật toán tổng hợp tốt đến đâu. Module này dạy lối ra, và lối ra bắt đầu bằng việc **đổi phép đo** chứ không bằng việc đổi thuật toán.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

Lý do rất gọn. Cá nhân hoá (personalisation) đi tìm một họ `{w_k}`, còn độ chính xác toàn cục là phép đo của một mô hình duy nhất `w⋆`. Hai đối tượng khác nhau, nên so hai phương pháp bằng độ chính xác toàn cục là đo cái mà cá nhân hoá **không nhắm tới**.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

Trong mô hình của module này, phép so đó cho chênh đúng {{s002}} với mọi giá trị của λ, nên nó là một phép thử không thể bác được điều gì.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

Ba đại lượng phải có mặt trong bảng kết quả: trung bình độ chính xác theo client, một **phân vị thấp** theo client, và **dải dò λ**. Thiếu phân vị thấp thì không ai biết client tệ nhất tệ tới đâu; thiếu dải dò λ thì con số báo ra là của một điểm trong một họ một tham số mà không ai kiểm được.

## Ditto, và hệ số co
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Ditto, và hệ số co · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ditto giải `min F_k(w_k) + (λ/2)·||w_k - w⋆||²` cho từng client, với `w⋆` là nghiệm toàn cục. Với `F_k` xấp xỉ bậc hai Hessian đơn vị quanh nghiệm cục bộ `θ̂_k`, nghiệm có dạng đóng `w_k = (θ̂_k + λ·w⋆)/(1+λ)`, tức một phép **co tuyến tính** từ nghiệm cục bộ về nghiệm chung.

## Ditto, và hệ số co · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **λ là hai đầu của một dải, không phải một lựa chọn kỹ thuật**. λ tiến ra vô cùng cho lại đúng FedAvg; λ bằng không cho học cục bộ hoàn toàn, tức không còn liên bang. Nên mọi câu so sánh với FedAvg hay với học cục bộ đều là so sánh ở một điểm của cùng một dải, và phải khai λ.

## Γ_cụm và phân vị thấp theo client
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Γ_cụm và phân vị thấp theo client · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Đặt `Γ_cụm` là trung bình bình phương khoảng cách từ nghiệm của từng cụm tới nghiệm chung `w⋆`. Với C cụm cách nhau đều một khoảng δ, đây đúng là phương sai của phân bố đều rời rạc: `Γ_cụm = δ²·(C²-1)/12`. Client ở cụm biên cách `w⋆` xa nhất, bình phương khoảng cách `δ²·((C-1)/2)²`.

## Γ_cụm và phân vị thấp theo client · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **trung bình theo client và phân vị thấp theo client tách nhau đúng bằng chênh lệch giữa hai đại lượng đó**, nhân hệ số co. Nên trung bình một mình không chỉ là thiếu thông tin, nó là **phép đo bị cụm giữa kéo lên**: cụm giữa gần `w⋆` nhất và cũng đông nhất trong các cấu hình đối xứng.

## Khi nào thì một mô hình là lời giải sai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Khi nào thì một mô hình là lời giải sai · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Nếu client chia thành C cụm có `P(y|x)` khác nhau, thì không tồn tại một `w` nào tối thiểu hoá đồng thời mọi `F_k`: các cực tiểu nằm ở những chỗ khác nhau. Một mô hình duy nhất là **một thoả hiệp**, và C mô hình là lời giải đúng.

## Khi nào thì một mô hình là lời giải sai · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đây là phát biểu về **bài toán**, không phải về thuật toán, nên nó không sửa được bằng cách chạy thêm vòng, thêm dữ liệu hay đổi bộ tổng hợp. Và nó có một hệ quả sắc hơn cho phần đánh giá: khi `P(y|x)` khác nhau giữa cụm thì **độ chính xác toàn cục không còn là đại lượng cần tối đa**, nên không có một con số duy nhất nào mô tả được chất lượng hệ.

## Khi nào thì một mô hình là lời giải sai · đáp (tiếp)
@phut: 1
@che-do: noi

Lúc đó bảng kết quả phải là một phân bố, không phải một ô.

## Ditto, nghiệm co, và sai số còn lại theo λ
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`min_{w_k} F_k(w_k) + (λ/2)·||w_k - w⋆||² ⇒ w_k = (θ̂_k + λ·w⋆)/(1+λ) ⇒ E||w_k - θ_k||² = (s + λ²·d_k²)/(1+λ)² với λ⋆ = s/d_k²`

**Giả thiết nó đứng trên:**

## Ditto, nghiệm co, và sai số còn lại theo λ (tiếp)
@phut: 1
@che-do: so

- F_k xấp xỉ bậc hai với Hessian đơn vị quanh nghiệm cục bộ, nên nghiệm Ditto có dạng đóng. Mạng neural và KAN không thoả giả thiết này, nên dạng đóng là công cụ lấy trực giác chứ không phải một bảo đảm
- θ̂_k = θ_k + e_k với E[e_k] = {{s002}} và E||e_k||² = s, trong đó s = σ²/n_k là sai số ước lượng cục bộ, nên s lớn khi client ít dữ liệu

## Ditto, nghiệm co, và sai số còn lại theo λ (tiếp)
@phut: 1
@che-do: so

- w⋆ coi như nghiệm toàn cục chính xác: sai số ước lượng của nó nhỏ hơn s khoảng K lần nên bỏ qua được
- λ là siêu tham số do người làm chọn, không do dữ liệu quyết định, nên mọi so sánh phải khai dải dò λ
- d_k² là bình phương khoảng cách từ nghiệm cụm của client k tới w⋆, một tính chất của dữ liệu và cách phân vùng

## Ditto, nghiệm co, và sai số còn lại theo λ · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Sai số còn lại tại λ tối ưu bằng `s·d²/(s + d²)`, tức `1/E⋆ = 1/s + 1/d²`, nên nó bị chặn bởi số hạng **nhỏ hơn** trong hai số hạng. Hệ quả dùng được khi trả phản biện: client ít dữ liệu không cứu được bằng cách chọn λ, chỉ cứu được bằng cách có thêm dữ liệu hoặc bằng cách chia cụm.

## Ditto, nghiệm co, và sai số còn lại theo λ · ghi (tiếp)
@phut: 0.5
@che-do: noi

Và vì `λ⋆ = s/d_k²` khác nhau giữa các cụm, một λ chung cho mọi client là một thoả hiệp đã biết trước, không phải một lựa chọn trung tính.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} |  | Trong Ditto với F_k xấp xỉ bậc hai Hessian đơn vị
!so {{s007}} |  | Client chia thành bốn cụm cách nhau đều
!so {{s008}} | điểm phần trăm | Ở chế độ FedAvg

## Tổng số mẫu trong hệ là 200000
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Tổng số mẫu trong hệ là {{s011}}, chia cho {{s010}} client nên mỗi client có {{s014}} mẫu, và phương sai gradient σ² = {{s009}}. Client chia thành {{s013}} cụm cách nhau δ = {{s015}}. λ tối ưu bằng bao nhiêu?

sig2 = {{s009}}, K = {{s010}}, N = {{s011}}, del = {{s012}}, C = {{s013}}

## Tổng số mẫu trong hệ là 200000 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(sig2⋆K/N) / (del⋆del⋆(C⋆C-1)/12)`

Khoảng {{s016}}, tức λ tối ưu nằm quanh một chứ không ở hai đầu dải, vì s = {{s017}} và Γ_cụm = {{s018}} cùng bậc độ lớn. Nếu anh dò λ trên lưới gồm {{s019}} rồi {{s020}} rồi {{s003}} thì lưới đó không chứa điểm tối ưu, nên con số báo ra là của một λ chưa dò tới. Đó là lý do bảng kết quả phải khai DẢI dò chứ không chỉ khai rằng đã dò.

## Bốn cụm cách nhau δ = 0,5
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bốn cụm cách nhau δ = {{s023}}, hai trăm client, tổng mẫu {{s011}}, σ² = {{s009}}. Chuyển từ FedAvg sang Ditto ở λ tối ưu làm TRUNG BÌNH theo client tăng bao nhiêu điểm phần trăm?

del = {{s021}}, C = {{s005}}, sig2 = {{s009}}, K = {{s022}}, N = {{s011}}

## Bốn cụm cách nhau δ = 0,5 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`10⋆Math.pow(del⋆del⋆(C⋆C-1)/12, {{s004}}) / (del⋆del⋆(C⋆C-1)/12 + sig2⋆K/N)`

Khoảng {{s024}} điểm phần trăm, và đó là mức tăng của TRUNG BÌNH theo client. Độ chính xác toàn cục không tăng một điểm nào, vì nó là phép đo của w⋆ và w⋆ không phụ thuộc λ. Công thức là 10·Γ²/(Γ + s), nên mức tăng bằng {{s002}} khi Γ = {{s002}}, tức một cụm, và tiến tới 10·Γ khi s tiến về {{s002}}, tức client nào cũng nhiều dữ liệu.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh so phương pháp cá nhân hoá của mình với FedAvg. Bảng nào trả lời được câu hỏi cá nhân hoá có giúp gì không?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Độ chính xác toàn cục của hai phương pháp, đo trên tập kiểm tra gộp
- Trung bình và phân vị thấp của độ chính xác theo client cho cả hai phương pháp, ở cùng một dải λ đã khai
- AUROC toàn cục của hai phương pháp
- Số vòng truyền tới khi đạt cùng một mức mất mát toàn cục

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Trung bình và phân vị thấp của độ chính xác theo client cho cả hai phương pháp, ở cùng một dải λ đã khai**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Phải là bảng có trung bình cộng phân vị thấp theo client, vì cá nhân hoá đi tìm họ mô hình riêng chứ không tìm một mô hình chung. Mọi phép đo toàn cục, kể cả AUROC toàn cục và số vòng tới một mức mất mát toàn cục, đều là phép đo của w⋆, nên chúng không di chuyển khi đổi λ và không thể bác được điều gì.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Dải λ phải có mặt vì λ tiến ra vô cùng cho lại chính FedAvg, nên thiếu dải dò thì không ai biết đang so hai phương pháp hay so một phương pháp với chính nó ở một điểm khác.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Reviewer hỏi vì sao không dùng một mô hình duy nhất cho mọi client. Lập luận nào đứng được mà không cần chạy thêm thí nghiệm?

- Một mô hình duy nhất hội tụ chậm hơn vì độ không đồng nhất làm bound phình
- Mô hình riêng luôn chính xác hơn vì nó có ít dữ liệu hơn nên dễ khớp hơn
- Một mô hình duy nhất cần nhiều tham số hơn để phủ hết các cụm

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Nếu client chia thành C cụm có P(y|x) khác nhau thì không tồn tại w nào tối thiểu hoá đồng thời mọi F_k, nên một mô hình là thoả hiệp và C mô hình là lời giải đúng

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Nếu client chia thành C cụm có P(y|x) khác nhau thì không tồn tại w nào tối thiểu hoá đồng thời mọi F_k, nên một mô hình là thoả hiệp và C mô hình là lời giải đúng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Lập luận đứng được là lập luận về sự không tồn tại: các cực tiểu của F_k nằm ở những chỗ khác nhau, nên thoả hiệp là bắt buộc chứ không phải hệ quả của thuật toán, và không chạy thêm vòng nào sửa được. Lập luận về hội tụ chậm chỉ nói về tốc độ chứ không nói về chỗ đến, nên nó không trả lời câu hỏi. Câu nói mô hình riêng luôn chính xác hơn thì sai hẳn:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

ít dữ liệu làm s = σ²/n_k lớn và quá khớp, đó đúng là nhánh λ bằng không của dải. Còn số tham số là chuyện dung lượng, không phải chuyện tồn tại nghiệm chung.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một mệnh đề không thể đúng. Bấm vào mệnh đề đó.

- Chúng tôi huấn luyện Ditto với λ = {{s020}} trên {{s022}} client chia thành {{s005}} cụm,
- và báo độ chính xác toàn cục trên tập kiểm tra gộp cho cả Ditto và FedAvg.
- Hai phương pháp đều đạt {{s025}}, nên cá nhân hoá không mang lại lợi ích trên tập dữ liệu này.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Hai phương pháp đều đạt {{s025}}, nên cá nhân hoá không mang lại lợi ích trên tập dữ liệu này.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai con số bằng nhau ở đây không phải một phát hiện, nó là hệ quả của phép đo đã chọn: độ chính xác toàn cục là phép đo của w⋆, và w⋆ là nghiệm FedAvg trong cả hai cột, nên nó không phụ thuộc λ. Phép thử này không thể cho ra kết quả khác, nên nó không phải một phép thử. Hai mệnh đề đầu đều hợp lệ nếu dừng ở mô tả. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

báo trung bình VÀ phân vị thấp của độ chính xác theo client cho cả hai phương pháp; ở cấu hình này trung bình theo client của Ditto cao hơn khoảng {{s004}} điểm và phân vị {{s026}} cao hơn nhiều hơn thế.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau làm con số phân vị {{s026}} trong bảng kết quả phồng lên. Bấm vào chỗ gây ra chuyện đó.

- Siêu tham số λ được dò bằng tìm kiếm lưới trên dải {{s019}} tới {{s026}} với mười hai giá trị,
- và chúng tôi báo cả trung bình lẫn phân vị {{s026}} của độ chính xác theo client,
- chọn λ theo phân vị {{s026}} cao nhất đo trên chính tập client dùng để báo kết quả.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**chọn λ theo phân vị {{s026}} cao nhất đo trên chính tập client dùng để báo kết quả.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu đúng chuẩn: dải dò được khai, và phép đo có cả trung bình lẫn phân vị thấp. Chỗ đổ là mệnh đề cuối: λ được chọn bằng chính tập client dùng để báo, nên con số in ra là giá trị TỐT NHẤT trên mười hai lần thử chứ không phải một ước lượng không chệch, và nó phồng lên theo số điểm lưới. Đây cùng họ với lỗi chọn ngưỡng cho khớp kết luận đã viết. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

tách tập client dò λ khỏi tập client báo kết quả, hoặc khai rõ rằng con số là cực đại trên lưới và báo thêm giá trị tại một λ chọn trước.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Viết mục tiêu của client k: F_k(w_k) + (λ/2)·||w_k - w⋆||², với F_k xấp xỉ bậc hai quanh θ̂_k
- Đặt gradient bằng {{s002}}: (w_k - θ̂_k) + λ(w_k - w⋆) = {{s002}}
- Giải ra w_k = (θ̂_k + λ·w⋆)/(1+λ)
- Trừ θ_k rồi lấy kỳ vọng: E||w_k - θ_k||² = (s + λ²·d_k²)/(1+λ)²
- Đạo hàm theo λ cho 2(λ·d_k² - s)/(1+λ)³, nên λ⋆ = s/d_k²

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Vì d_k² khác nhau giữa các cụm, λ⋆ khác nhau giữa các cụm, nên C mô hình là lời giải đúng và một λ chung là một thoả hiệp

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: toàn cục {{s027}} · trung bình theo client {{s028}} · phân vị {{s026}} theo client {{s029}} · chênh {{s030}} điểm phần trăm, ở λ = {{s003}}, C = {{s005}}, δ = {{s023}}, K = {{s022}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi client cùng một bài toán, tức P(y|x) như nhau** tắt đi: P(y|x) khác nhau giữa các cụm: cùng một luồng (flow) mạng được gán nhãn tấn công ở cụm này và lành ở cụm kia, vì chính sách và nền lưu lượng của hai mạng khác nhau.
- **Client nào cũng đủ dữ liệu để học riêng** tắt đi: n_k nhỏ, nên s = σ²/n_k lớn: mô hình riêng khớp vào nhiễu của chính client đó.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **F_k xấp xỉ bậc hai với Hessian đơn vị quanh nghiệm cục bộ** tắt đi: Mô hình là CNN, KAN hay transformer, nên F_k phi lồi và nghiệm Ditto không có dạng đóng.
- **Số client đủ lớn để phân vị {{s026}} ước lượng được** tắt đi: K bằng {{s026}}, nên phân vị {{s026}} là đúng một client.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bốn con số của cùng một hệ. Trần độ chính xác đặt ở {{s031}} và mỗi đơn vị sai số còn lại trừ {{s026}} điểm. Tổng số mẫu giữ nguyên {{s011}}, nên kéo số client lên là làm mỗi client ít dữ liệu đi. Kéo λ trước, và để ý rằng con số TOÀN CỤC không hề nhúc nhích.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.9` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table III compares your personalized method against FedAvg using global test accuracy. Personalized federated learning does not optimize that quantity, so the comparison does not support the claim in the abstract. Please report the per client accuracy distribution for both methods, including a low percentile, and state the range of lambda you searched.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree and have changed the reported quantity. Table III now leads with the per client accuracy distribution for both methods: mean, 10th percentile, and the worst client, over the same {{s022}} clients. Global accuracy is retained in one column only, and we now state explicitly in Section V-A that it is a property of the shared model and is therefore identical for both methods by construction, so it cannot separate them.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Lambda was searched over {{s032}} values on a log grid from {{s033}} to {{s026}}, and the grid is now reported in Table II together with the selected value; the selection used a held out set of {{s034}} clients that is disjoint from the {{s022}} reporting clients.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also added Figure {{s035}}, the per cluster accuracy, because a symmetric cluster layout can give a zero gap between the mean and the 10th percentile while the data is still far from identically distributed, so the gap alone is not sufficient evidence.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng độ chính xác toàn cục là phép đo phổ biến và dễ so với các bài khác. Đúng về thực hành, không trả lời được phản bác.
- Mức {{s004}}: thêm trung bình độ chính xác theo client, nhưng vẫn giữ độ chính xác toàn cục làm con số dẫn và không báo phân vị thấp.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s013}}: đổi con số dẫn thành trung bình cộng phân vị thấp theo client cho cả hai phương pháp, khai dải dò λ, và nói rõ rằng độ chính xác toàn cục là phép đo của mô hình chung nên nó không di chuyển theo λ.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Your ablation fixes lambda at a single value and concludes that personalization helps. Since lambda to infinity recovers FedAvg and lambda equal to zero recovers purely local training, the reported gain is a statement about one point of a one parameter family. Please report the sweep, and explain why the gain should not be attributed to the amount of local data rather than to the clustering structure.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Section V-C now reports the full sweep rather than a single point. For {{s032}} values of lambda on a log grid we plot the mean and the 10th percentile of per client accuracy, and we mark both ends of the family: the largest lambda reproduces FedAvg to within {{s036}} accuracy points, and the smallest reproduces purely local training. To separate the two explanations we added a two factor experiment in Section V-D.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Holding the cluster layout fixed and reducing the local sample size by a factor of four moves the optimal lambda up, from {{s037}} to about {{s038}}, while holding the sample size fixed and doubling the inter cluster offset moves it down. This is the signed prediction of the shrinkage analysis, where the optimal lambda equals the local estimation error divided by the cluster dispersion, and the two factors therefore act in opposite directions.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The observed direction matches in both arms, which is evidence that the gain is not merely a consequence of the amount of local data.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng λ được chọn theo thực hành thường gặp trong các bài trước. Không trả lời được chuyện một điểm của một họ.
- Mức {{s004}}: thêm bảng quét λ, nhưng vẫn kết luận bằng con số ở λ tốt nhất và không tách được hai nguyên nhân.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s013}}: báo đường cong theo λ cho cả trung bình và phân vị thấp, chỉ ra hai đầu dải là FedAvg và học cục bộ, và khai λ được chọn trên tập client tách riêng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.9` bấm thẻ.
