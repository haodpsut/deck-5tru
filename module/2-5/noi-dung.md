---
tieu-de: Riêng tư có định nghĩa: DP và kế toán
phu-de: Trụ 2 FL · module 2.5
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 93.5
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

epsilon của tôi là bao nhiêu, ở mức đơn vị kề nào (bản ghi hay người dùng), và đánh đổi độ chính xác là bao nhiêu điểm?

## Riêng tư có định nghĩa: DP và kế toán
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này không dạy định nghĩa DP. Nó làm đúng một việc: tách **con số `epsilon`** ra khỏi **ba thứ phải đi kèm nó**, là `delta`, đơn vị kề, và bộ kế toán đã dùng. Thiếu bất kỳ cái nào thì `epsilon` không phải một bảo đảm, nó chỉ là một chữ số trong bảng.

## Riêng tư có định nghĩa: DP và kế toán (tiếp)
@phut: 1
@che-do: noi

Ba chỗ reviewer đánh, theo đúng thứ tự họ hay đánh: Bài viết *privacy-preserving* mà không có `epsilon`, hoặc có `epsilon` mà không có `delta` và đơn vị kề. Bài dùng công thức Gauss cổ điển `sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon` ở `epsilon = {{s001}}`. Công thức vẫn trả về một số, và không có gì dừng anh lại. Bài khai lấy mẫu Poisson tỉ lệ `q` trong kế toán, rồi cài đặt bằng shuffling theo epoch.

## Riêng tư có định nghĩa: DP và kế toán (tiếp)
@phut: 1
@che-do: noi

Kế toán lúc đó không còn đúng, mà log thì sạch tuyệt đối. Hệ quả thực tế rất gọn: bảng DP của anh phải có bốn cột là `epsilon`, `delta`, đơn vị kề, và tên bộ kế toán. Ba cột là chưa đủ.

## Đơn vị kề (adjacency unit
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Đơn vị kề (adjacency unit · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Hai tập dữ liệu `D` và `D'` gọi là kề nhau khi chúng khác nhau đúng **một đơn vị**. Định nghĩa DP không nói đơn vị đó là gì: người dùng hệ phải chọn, và lựa chọn đó là một phần của bảo đảm chứ không phải một chi tiết cài đặt.

## Đơn vị kề (adjacency unit · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cùng một con số `epsilon` ở mức bản ghi và ở mức người dùng là hai bảo đảm khác nhau về độ mạnh.** Nếu một người đóng góp `k` bản ghi thì riêng tư nhóm chỉ cho chặn trên `k·epsilon` ở mức người dùng, và muốn giữ nguyên `epsilon` ở mức người dùng thì độ nhạy tăng `k` lần nên `sigma` cũng phải tăng `k` lần.

## Đơn vị kề (adjacency unit · đáp (tiếp)
@phut: 1
@che-do: noi

Một bài FL cho IDS mà mỗi thiết bị sinh hàng nghìn luồng (flow) một ngày thì khai `epsilon` mức bản ghi gần như không nói gì về thiết bị đó.

## Vùng hiệu lực của một chặn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Vùng hiệu lực của một chặn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Chặn Gauss cổ điển `sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon` được chứng minh với `epsilon` trong khoảng ({{s004}}, {{s005}}). Điều kiện đó nằm trong **chứng minh**, không nằm trong biểu thức.

## Vùng hiệu lực của một chặn · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **hàm số vẫn chạy ngoài vùng hiệu lực và vẫn trả về một số nhỏ hơn, nên không có lỗi nào để bắt.** Đây chính là lớp lỗi phép đo có sẵn mà không có ngưỡng: phép tính in ra bình thường, cổng không kêu, và bài báo mang một con số không có bảo đảm.

## Vùng hiệu lực của một chặn · đáp (tiếp)
@phut: 1
@che-do: noi

Muốn dùng `epsilon` lớn thì phải đổi sang chặn giải tích Gauss hoặc sang kế toán RDP, không phải đổi con số trong cùng công thức cũ.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một bước DP-SGD chỉ thấy một lô con. Nếu lô được chọn bằng **lấy mẫu Poisson độc lập từng mẫu với tỉ lệ `q`** thì mỗi mẫu chỉ bị lộ ở các bước nó được chọn, và bảo đảm của một bước được khuếch đại theo `q`. Đó là lý do `epsilon` của `T` bước tăng theo bậc `q·sqrt(T·log(1/delta))/sigma` chứ không tăng tuyến tính theo `T`.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **khuếch đại là một định lý về cách lấy mẫu, không phải một tính chất của nhiễu.** Cài đặt thật của gần hết thư viện là xáo trộn tập rồi cắt thành lô cố định, tức mỗi mẫu xuất hiện đúng một lần mỗi epoch. Đó không phải lấy mẫu Poisson, nên con số khuếch đại đã dùng không áp được. Khoảng cách giữa hai cách này là chỗ trốn im lặng nhất của cả họ bài DP-FL.

## Secure aggregation bảo vệ cái gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Secure aggregation bảo vệ cái gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Secure aggregation làm cho server chỉ thấy **tổng** các cập nhật chứ không thấy từng cập nhật. Nó là một bảo đảm về **ai thấy gì trên đường truyền và tại server**.

## Secure aggregation bảo vệ cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **nó không chặn suy luận từ mô hình đã công bố, nên nó không phải DP và không sinh ra con số `epsilon` nào.** Hai thứ này ghép được và nên ghép, nhưng đổi tên cái này thành cái kia là một lỗi khái niệm mà reviewer bắt rất nhanh. Cách khai đúng là: secure aggregation thu hẹp mô hình đe doạ của server trung thực nhưng tò mò, DP thu hẹp lượng thông tin rò ra qua chính mô hình.

## Định nghĩa (epsilon
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`P[M(D) ∈ S] ≤ e^epsilon · P[M(D') ∈ S] + delta với mọi D, D' kề nhau và mọi S; Delta2 = max ||f(D) − f(D')||₂; sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon`

**Giả thiết nó đứng trên:**

## Định nghĩa (epsilon (tiếp)
@phut: 1
@che-do: so

- Quan hệ kề đã được khai rõ: khác đúng một bản ghi, hay khác đúng một người dùng. Đổi đơn vị là đổi bảo đảm
- Delta2 là độ nhạy L2 trong trường hợp xấu nhất trên MỌI cặp kề, không phải độ nhạy quan sát được trên dữ liệu đang có
- Chặn Gauss cổ điển chỉ được chứng minh với epsilon trong khoảng ({{s004}}, {{s005}}); ngoài khoảng đó công thức vẫn chạy nhưng không còn là một chặn

## Định nghĩa (epsilon (tiếp)
@phut: 1
@che-do: so

- Nhiễu cộng vào là Gauss độc lập từng toạ độ với cùng sigma, và nhiễu được cộng vào ĐẦU RA của f, không cộng vào dữ liệu

## Định nghĩa (epsilon · ghi chú
@phut: 1
@che-do: noi

Chặn giải tích Gauss của Balle và Wang bỏ được ràng buộc `epsilon` nhỏ hơn {{s005}} và cho `sigma` nhỏ hơn ở cùng `(epsilon, delta)`. Nếu bài của anh dùng `epsilon` lớn hơn {{s005}} thì phải đổi sang chặn đó hoặc sang RDP, chứ không được dùng lại công thức cổ điển.

## RDP của cơ chế Gauss
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`cơ chế Gauss là (alpha, alpha/(2·sigma²))-RDP; epsilon(delta) = epsilon_RDP(alpha) + log(1/delta)/(alpha − {{s005}}), lấy min theo alpha; DP-SGD: cắt chuẩn gradient từng mẫu về C, cộng N(0, sigma²C²I), lấy mẫu Poisson tỉ lệ q, ghép T bước`

**Giả thiết nó đứng trên:**

## RDP của cơ chế Gauss (tiếp)
@phut: 1
@che-do: so

- Cắt chuẩn gradient được thực hiện TỪNG MẪU trước khi cộng, nên độ nhạy L2 của tổng trong một lô bị chặn bởi C
- Lô được chọn bằng lấy mẫu Poisson độc lập với tỉ lệ q, không phải bằng xáo trộn rồi cắt lô cố định
- RDP cộng tuyến tính khi ghép T bước, với cùng một alpha cho cả T bước trước khi lấy min

## RDP của cơ chế Gauss (tiếp)
@phut: 1
@che-do: so

- sigma là tỉ số nhiễu trên chuẩn cắt, nên nhiễu thực tế cộng vào có độ lệch chuẩn sigma·C mỗi toạ độ

## RDP của cơ chế Gauss · ghi chú
@phut: 1
@che-do: noi

Hai con số `epsilon` của cùng một lần chạy có thể lệch nhau nhiều lần chỉ vì bộ kế toán khác nhau. Nên tên bộ kế toán và bản của nó là một phần của kết quả, giống như tên dataset. Bảng DP không có cột này là bảng không lặp lại được.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s005}} | chặn trên của epsilon | Chặn Gauss cổ điển sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon chỉ được chứng minh khi
!so {{s006}} | số mũ âm | Luật ngón tay là chọn delta nhỏ hơn nghịch đảo số bản
!so {{s007}} | epsilon mức người dùng | Cơ chế đạt epsilon = {{s008}} ở mức bản ghi. Mỗi người

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một truy vấn có độ nhạy L2 bằng {{s005}}. Muốn (epsilon = {{s008}}, delta = {{s010}} luỹ thừa trừ 5)-DP bằng cơ chế Gauss cổ điển thì sigma nhỏ nhất là bao nhiêu?

sens = {{s005}}, d = {{s007}}, eps = {{s009}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`sens × Math.sqrt(2 × (Math.log(1.25) + d × Math.LN10)) / eps`

Khoảng {{s011}}. Để ý epsilon = {{s008}} nằm TRONG vùng hiệu lực, nên con số này là một chặn thật. Nhiễu phải có độ lệch chuẩn gần {{s010}} lần độ nhạy của một bản ghi, và đó là lý do DP ở epsilon nhỏ hơn {{s005}} đắt tới mức nhiều bài lặng lẽ đẩy epsilon lên {{s001}} rồi giữ nguyên công thức.

## Một bước Gauss với sigma = 4 là (alpha
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bước Gauss với sigma = {{s012}} là (alpha, alpha/(2·sigma²))-RDP. Chuyển về DP tại alpha = {{s010}} và delta = {{s010}} luỹ thừa trừ {{s007}} cho epsilon bằng bao nhiêu?

alpha = {{s010}}, sigma = {{s012}}, delta = {{s013}}

## Một bước Gauss với sigma = 4 là (alpha · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`alpha / ({{s002}} × sigma × sigma) + Math.log(1 / delta) / (alpha - {{s005}})`

Khoảng {{s014}}. Hai điều phải đọc ra. Một, con số này LỚN hơn {{s005}}, nên ở đúng điểm này công thức Gauss cổ điển không áp được: muốn dùng nó anh phải tụt epsilon xuống dưới {{s005}}, tức tăng sigma.

## Một bước Gauss với sigma = 4 là (alpha · đáp (tiếp)
@phut: 1
@che-do: noi

Hai, epsilon thật là min theo alpha nên nó nhỏ hơn hoặc bằng {{s014}}; lấy một alpha bất kỳ rồi báo kết quả là báo một chặn lỏng hơn mức cần thiết, và nếu lưới alpha quá hẹp thì min rơi vào biên lưới mà không ai thấy.

## Một bài khai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài khai: hệ dùng secure aggregation nên server không thấy cập nhật của từng client, do đó dữ liệu người dùng được bảo vệ. Thiếu đúng một thứ để câu đó thành một tuyên bố riêng tư kiểm được. Thiếu gì?

## Một bài khai (tiếp)
@phut: 0.5
@che-do: hoi

- Giao thức mã hoá dùng trong secure aggregation
- Kiến trúc mô hình và số tham số
- Một cặp (epsilon, delta) kèm đơn vị kề, vì secure aggregation không chặn suy luận từ mô hình đã công bố
- Số client tham gia mỗi vòng

## Một bài khai · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Một cặp (epsilon, delta) kèm đơn vị kề, vì secure aggregation không chặn suy luận từ mô hình đã công bố**

Secure aggregation là bảo đảm về ai thấy gì trên đường truyền và tại server. Mô hình toàn cục vẫn được công bố, và suy luận thành viên hay truy ngược vẫn làm được từ chính mô hình đó. Chỉ DP mới chặn được kênh ấy, và chặn đó phải hiện ra thành một cặp số cộng một đơn vị kề.

## Hai bài cùng chạy DP-SGD trên cùng dữ liệu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai bài cùng chạy DP-SGD trên cùng dữ liệu, cùng sigma, cùng q, cùng T, và cùng delta. Bài A báo epsilon = {{s015}}, bài B báo epsilon = {{s016}}. Giải thích nào KHÔNG cần thêm giả thiết nào để đứng được?

## Hai bài cùng chạy DP-SGD trên cùng dữ liệu (tiếp)
@phut: 0.5
@che-do: hoi

- Một trong hai bài tính sai, vì cùng cấu hình thì epsilon phải bằng nhau
- Hai bài dùng hai bộ kế toán khác nhau, hoặc hai đơn vị kề khác nhau, nên hai con số trả lời hai câu khác nhau
- Bài B huấn luyện lâu hơn nên epsilon lớn hơn
- Bài A dùng secure aggregation còn bài B thì không

## Hai bài cùng chạy DP-SGD trên cùng dữ liệu · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hai bài dùng hai bộ kế toán khác nhau, hoặc hai đơn vị kề khác nhau, nên hai con số trả lời hai câu khác nhau**

## Hai bài cùng chạy DP-SGD trên cùng dữ liệu · đáp (tiếp)
@phut: 1
@che-do: noi

Với cùng sigma, q, T, delta thì epsilon vẫn phụ thuộc bộ kế toán (moments accountant, RDP, hay PLD cho ba chặn khác nhau, chặt dần) và phụ thuộc đơn vị kề. Phương án C trái dữ kiện vì T đã khai bằng nhau. Phương án A sai vì nó giả định có một con số epsilon duy nhất cho một cấu hình, điều chỉ đúng khi cố định cả bộ kế toán và đơn vị kề.

## Hai bài cùng chạy DP-SGD trên cùng dữ liệu · đáp (tiếp)
@phut: 1
@che-do: noi

Đó là lý do bảng DP phải có cột tên bộ kế toán.

## Trong một cài đặt DP-SGD
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong một cài đặt DP-SGD, dòng nào bị viết sai thì bảo đảm DP mất HẲN thay vì chỉ xấu đi?

## Trong một cài đặt DP-SGD (tiếp)
@phut: 0.5
@che-do: hoi

- Dùng xáo trộn rồi cắt lô cố định thay vì lấy mẫu Poisson tỉ lệ q
- Cắt chuẩn gradient trung bình của lô thay vì cắt chuẩn gradient từng mẫu
- Chọn delta bằng {{s010}} luỹ thừa trừ {{s012}} thay vì {{s010}} luỹ thừa trừ {{s007}}
- Lấy min của epsilon(alpha) trên một lưới alpha gồm {{s017}} giá trị thay vì {{s018}} giá trị

## Trong một cài đặt DP-SGD · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cắt chuẩn gradient trung bình của lô thay vì cắt chuẩn gradient từng mẫu**

## Trong một cài đặt DP-SGD · đáp (tiếp)
@phut: 1
@che-do: noi

Cắt theo lô không chặn được độ nhạy của một mẫu, nên Delta2 không còn hữu hạn và không có sigma nào cho bất kỳ (epsilon, delta). Phương án A làm kế toán không còn đúng, tức con số đã báo mất bảo đảm, nhưng cơ chế vẫn có một bảo đảm nào đó nếu tính bằng kế toán cho shuffling. Phương án C và D chỉ đổi con số hoặc làm chặn lỏng hơn.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả riêng tư sau có một câu làm toàn bộ phần DP của bài không kiểm được. Bấm vào câu đó.

- Chúng tôi cắt chuẩn L2 của gradient từng mẫu về C = {{s019}},
- cộng nhiễu Gauss với sigma = {{s020}} vào tổng của mỗi lô,
- lấy mẫu Poisson với tỉ lệ q = {{s021}} và chạy T = {{s010}} nghìn bước,
- và đạt riêng tư mạnh với delta = {{s010}} luỹ thừa trừ {{s007}}.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và đạt riêng tư mạnh với delta = {{s010}} luỹ thừa trừ {{s007}}.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu đầu khai đủ mọi tham số của CƠ CHẾ, và đều hợp lệ. Câu cuối là chỗ phải có con số epsilon cùng tên bộ kế toán và đơn vị kề, nhưng nó thay bằng tính từ riêng tư mạnh. Không có epsilon thì không có gì để kiểm, không có gì để so với bài khác, và cũng không có gì để đặt cạnh cột độ chính xác. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

thay cụm riêng tư mạnh bằng epsilon tính ra, tên và bản của bộ kế toán, và một câu nói đơn vị kề là bản ghi hay người dùng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau có một chỗ dùng công thức ngoài vùng hiệu lực của nó. Bấm vào chỗ đó.

- Độ nhạy L2 của truy vấn sau khi cắt là Delta2 = C = {{s019}},
- chúng tôi chọn delta = {{s010}} luỹ thừa trừ {{s007}} theo luật delta nhỏ hơn nghịch đảo số bản ghi,
- và đặt epsilon = {{s001}} để giữ độ chính xác ở mức dùng được,
- nên theo cơ chế Gauss sigma = Delta2·sqrt(2·ln(1,25/delta))/epsilon = {{s022}}.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên theo cơ chế Gauss sigma = Delta2·sqrt(2·ln(1,25/delta))/epsilon = {{s022}}.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu đầu đều đúng, kể cả việc chọn epsilon = {{s001}}: đó là một lựa chọn thiết kế hợp lệ. Câu cuối mới là lỗi, vì chặn Gauss cổ điển chỉ được chứng minh với epsilon trong khoảng ({{s004}}, {{s005}}), và ở epsilon = {{s001}} nó không còn là một chặn. Nguy hiểm của chỗ này là giá trị {{s022}} không có gì bất thường, nên không cổng số học nào bắt được. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

dùng chặn giải tích Gauss của Balle và Wang, hoặc tính sigma từ kế toán RDP, rồi khai tên bộ kế toán.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phần phương pháp sau có một dòng làm con số epsilon của cả bài mất bảo đảm, trong khi mọi dòng khác đều đúng. Bấm vào dòng đó.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Mỗi vòng, server chọn {{s023}} client bằng lấy mẫu độc lập và kế toán dùng tỉ lệ q = {{s021}}.
- Mỗi client cắt chuẩn gradient từng mẫu về C rồi cộng phần nhiễu của mình.
- Client nạp dữ liệu cục bộ bằng bộ nạp mặc định: xáo trộn tập một lần mỗi epoch rồi cắt thành lô cố định cỡ {{s024}}.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Client nạp dữ liệu cục bộ bằng bộ nạp mặc định: xáo trộn tập một lần mỗi epoch rồi cắt thành lô cố định cỡ {{s024}}.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Kế toán ở mức client đang dùng khuếch đại do lấy mẫu Poisson cho từng BƯỚC cục bộ, nhưng dòng này nói lô cục bộ được tạo bằng xáo trộn rồi cắt, tức mỗi mẫu đi qua đúng một lần mỗi epoch. Đó không phải lấy mẫu Poisson, nên định lý khuếch đại không áp được và epsilon báo ra không còn là chặn. Hai dòng đầu đều đúng và không liên quan:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

lấy mẫu client ở mức server là một chuyện, lấy mẫu mẫu ở mức client là chuyện khác, và bài phải khai cả hai. Cách sửa: đổi bộ nạp cục bộ sang lấy mẫu Poisson, hoặc dùng bộ kế toán cho shuffling, và nói rõ trong bài là đã chọn cái nào.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Chọn và khai quan hệ kề, rồi đặt Delta2 = max trên mọi cặp kề của ||f(D) − f(D')||₂
- Công bố M(D) = f(D) + N(0, sigma²I), nhiễu Gauss độc lập từng toạ độ
- Viết lỗ riêng tư ln(p_D(x)/p_D'(x)); với nhiễu Gauss nó là một biến Gauss có trung bình Delta2²/(2·sigma²) và độ lệch chuẩn Delta2/sigma
- Đòi xác suất lỗ riêng tư vượt epsilon nhỏ hơn delta, rồi chặn đuôi Gauss đó

## Dẫn lại từng bước · ca một (tiếp)
@phut: 1
@che-do: so

- Giải ra sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon, và ghi kèm vùng hiệu lực epsilon trong khoảng ({{s004}}, {{s005}})

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Cắt chuẩn L2 của gradient TỪNG MẪU về C, rồi mới cộng các gradient đã cắt lại
- Kết luận độ nhạy L2 của tổng trong một lô bị chặn bởi C, vì thêm hay bỏ một mẫu đổi tổng tối đa C
- Cộng N(0, sigma²C²I) vào tổng, nên một bước là (alpha, alpha/(2·sigma²))-RDP
- Áp khuếch đại do lấy mẫu Poisson tỉ lệ q cho một bước, rồi cộng RDP của T bước lại

## Dẫn lại từng bước · ca hai (tiếp)
@phut: 1
@che-do: so

- Chuyển về DP bằng epsilon(delta) = epsilon_RDP(alpha) + log(1/delta)/(alpha − {{s005}}), rồi lấy min trên một lưới alpha

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Delta2 = {{s005}} · epsilon = {{s008}} · delta = {{s010}} luỹ thừa trừ {{s007}} · đơn vị kề là một bản ghi · sigma nhỏ nhất {{s025}} · lấy mẫu Poisson tỉ lệ q · cắt chuẩn gradient từng mẫu về C

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Lô được chọn bằng lấy mẫu Poisson độc lập đúng tỉ lệ q** tắt đi: Cài đặt thật xáo trộn tập rồi cắt thành lô cố định, tức mỗi mẫu đi qua đúng một lần mỗi epoch. Đây là hành vi mặc định của gần hết bộ nạp dữ liệu.
- **Cắt chuẩn L2 của gradient TỪNG MẪU về C** tắt đi: Cắt theo lô, tức tính gradient trung bình của lô rồi mới cắt chuẩn của nó về C.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Đơn vị kề là một bản ghi** tắt đi: Đơn vị kề đổi sang một người dùng, và một người dùng đóng góp tới k bản ghi.
- **epsilon nằm trong vùng hiệu lực của chặn Gauss cổ điển, tức nhỏ hơn {{s005}}** tắt đi: Bài đặt epsilon = {{s001}} để giữ độ chính xác, nhưng vẫn dùng lại đúng công thức sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Chúng tôi dùng cơ chế Gauss với epsilon bằng {{s001}}, và trích chặn sigma ≥ Delta2·sqrt(2·ln(1,25/delta))/epsilon của Dwork và Roth làm cơ sở.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỔ**

ĐỔ, không vì epsilon {{s001}} là sai, mà vì CHẶN ĐƯỢC TRÍCH không phủ tới đó. Theorem A.1 mở đầu bằng đúng một câu ràng buộc: "Let epsilon in ({{s004}}, {{s005}}) be arbitrary". Phép chứng minh cổ điển đó chỉ phủ epsilon nhỏ hơn {{s005}}, nên dẫn nó cho epsilon bằng {{s001}} là dẫn ra ngoài vùng hiệu lực.

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

Muốn dùng epsilon lớn thì phải đổi công cụ, ví dụ phân tích Gauss giải tích hay kế toán theo Rényi, và phải khai rõ công cụ nào.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Chỉ một công thức duy nhất, công thức Gauss cổ điển. Kéo epsilon qua biên vùng hiệu lực và xem nó vẫn trả về số như không có gì xảy ra. Rồi kéo k để thấy cùng một cơ chế được đọc ở hai đơn vị kề cho hai câu trả lời khác nhau.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.5` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV-C states that the system is privacy-preserving and reports epsilon = {{s001}} with delta = 1e-5, citing the Gaussian mechanism of Dwork and Roth for the noise multiplier. That bound is stated for epsilon in ({{s026}}), so the reported noise multiplier does not establish the claimed guarantee. In addition, the adjacency unit is never specified, and each device in Table II contributes thousands of flows. Please clarify what exactly is being guaranteed and at which granularity.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We thank the reviewer for both points, and we have corrected the accounting rather than the wording. First, we no longer use the classical Gaussian bound. The noise multiplier is now obtained from an RDP accountant (Opacus {{s027}}, RDP orders {{s028}} to {{s024}}), and we also report the analytic Gaussian mechanism of Balle and Wang as a cross-check; the two agree within {{s029}} at our operating point.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Second, we now state the adjacency unit explicitly in Section IV-C and in the caption of Table V. Our deployment unit of interest is the device, not the flow, so we report both: record-level epsilon = {{s030}} and device-level epsilon = {{s031}} at delta = 1e-5, where the device-level figure is obtained by running the accountant with device-level sampling rather than by applying a group-privacy factor, since the latter is loose.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The accuracy column of Table V is now reported at the device-level setting, which costs {{s032}} macro-F1 points relative to the non-private baseline rather than the {{s033}} points we previously reported at record level. Finally, we verified that the local data loader performs Poisson subsampling at the rate the accountant assumes; the previous version used shuffle-and-batch, which invalidated the amplification step, and Appendix C now reports the unit test that checks the realized batch size distribution against the Poisson expectation.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: trả lời rằng epsilon = {{s001}} là giá trị thường dùng trong các bài DP-FL và dẫn vài bài cùng dùng. Đúng về thực hành, không trả lời được phản bác: tiền lệ không sửa được một chặn áp ngoài vùng hiệu lực.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: nhận lỗi vùng hiệu lực và đổi sang chặn giải tích Gauss hoặc kế toán RDP, báo lại sigma và epsilon. Vẫn chưa trả lời phần đơn vị kề, nên nửa sau của phản biện còn nguyên.
- Mức {{s003}}: làm mức {{s002}}, cộng khai đơn vị kề rõ ràng, cộng báo epsilon ở CẢ hai mức bản ghi và người dùng, cộng tên và bản của bộ kế toán.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The paper reports that differential privacy costs only {{s033}} macro-F1 points at epsilon = {{s001}}. Given the per-example clipping norm C = {{s035}} and the noise multiplier in Table III, this seems implausibly cheap for the model size reported in Section III. Please confirm that the clipping is applied per example rather than per batch, and report the non-private baseline trained under the identical data pipeline.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right to read a cheap privacy cost as a symptom rather than a result. Three changes. ({{s005}}) Clipping: we confirm per-example clipping and we now cite the exact call site (Appendix B, Listing {{s002}}); we have also added a unit test that injects a single large-gradient example and asserts that the per-example norm after clipping never exceeds C, which fails under per-batch clipping. ({{s002}}) Baseline:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the non-private baseline in the previous submission was trained with a different loader and a larger effective batch. Retrained under the identical pipeline, it reaches {{s036}} macro-F1 rather than {{s037}}, so the measured privacy cost at record-level epsilon = {{s030}} is {{s032}} points, not {{s033}}. ({{s003}}) Negative control: we deliberately ran the per-batch clipping variant and report it in Table VI.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

It loses only {{s038}} macro-F1 points while providing no DP guarantee at all, which is exactly the configuration a small reported privacy cost should make a reader suspect. We state this explicitly in Section V-F so that the number is read as a guarantee, not as a tuning result.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: khẳng định lại con số {{s034}} điểm và nói rằng cấu hình đã được dò cẩn thận. Không có bằng chứng nào mới, nên phản bác vẫn đứng.
- Mức {{s002}}: xác nhận cắt từng mẫu bằng cách dẫn tên hàm trong mã, và báo lại baseline không riêng tư. Trả lời đúng hai câu được hỏi nhưng chưa giải thích vì sao chi phí lại nhỏ bất thường.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: làm mức {{s002}}, cộng chỉ ra nguồn gốc thật của chi phí nhỏ (ví dụ baseline cũ chạy trên một đường ống dữ liệu khác, hoặc epsilon tính ở mức bản ghi trong khi mô hình đe doạ đòi mức thiết bị), cộng báo lại bảng với cả hai bên cùng một đường ống.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.5` bấm thẻ.
