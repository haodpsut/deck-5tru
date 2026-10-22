---
tieu-de: Drift và cách chia dữ liệu theo thời gian
phu-de: Trụ 1 NID · module 1.5
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
@phan: NID
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Nếu tôi chia lại dữ liệu theo thời gian thay vì ngẫu nhiên, con số của tôi tụt bao nhiêu, và tôi có dám báo cả hai không?

## Chia ngẫu nhiên không phải một lựa chọn kỹ thuật
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Khi anh chia k-fold ngẫu nhiên trên dữ liệu có mốc thời gian, anh không chỉ chọn một cách đánh giá. Anh đang **khẳng định** rằng phân bố của lưu lượng không đổi theo thời gian, tức mẫu tháng {{s001}} và mẫu tháng {{s002}} đổi chỗ được cho nhau. Reviewer đánh vào đúng chỗ đó, và họ đúng.

## Chia ngẫu nhiên không phải một lựa chọn kỹ thuật (tiếp)
@phut: 1
@che-do: noi

Module này có hai việc. Việc thứ nhất: nhớ được ba ràng buộc thời gian của TESSERACT và nói được tại sao mỗi cái là một ràng buộc riêng. Việc thứ hai, quan trọng hơn: nói được bằng chữ của mình rằng khi phân bố lúc kiểm khác lúc huấn luyện thì **mọi bound tổng quát hoá kiểu i.i.d. mất hiệu lực**, chứ không phải là lỏng hơn.

## Chia ngẫu nhiên không phải một lựa chọn kỹ thuật (tiếp)
@phut: 1
@che-do: noi

Đây là nền của mọi câu trả lời về drift, và nó là câu mà người không nắm sẽ trả lời bằng cách hứa huấn luyện lại.

Một con số một điểm, ví dụ `F1 = {{s003}}`, không chứa thông tin nào về thời gian. `AUT(f, N)` chứa, và đó là lý do nó tồn tại.

## Ba ràng buộc thời gian của TESSERACT
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Ba ràng buộc thời gian của TESSERACT · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ba cái, phải kể được rời nhau: **Nhất quán thời gian khi huấn luyện:** mọi mẫu huấn luyện phải có mốc thời gian trước mọi mẫu kiểm. Vi phạm cái này là huấn luyện trên tương lai. **Cùng kỳ giữa hai lớp:** cửa sổ thời gian (time window) của lớp lành và lớp độc phải trùng nhau. Vi phạm cái này thì bộ phân loại học được chỗ lệch kỳ chứ không học tấn công.

## Ba ràng buộc thời gian của TESSERACT · đáp (tiếp)
@phut: 1
@che-do: noi

**Tỉ lệ lớp lúc kiểm là tỉ lệ thật:** không lấy mẫu lại tập kiểm. **Điểm phải nhớ:** ba ràng buộc này độc lập nhau. Bài báo có thể thoả cái thứ nhất mà vi phạm cái thứ hai, và lúc đó con số vẫn trông hợp lệ. Nên trong phần đánh giá phải khai cả ba, không phải chỉ nói chia theo thời gian.

## AUT(f, N) là gì, và nó mua được gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s005}} trên bốn.*

## AUT(f, N) là gì, và nó mua được gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Diện tích dưới đường hiệu năng theo thời gian, lấy trên `N` đợt liền nhau, chuẩn hoá về đoạn `[{{s006}}]` bằng cách chia cho số đoạn `N − {{s002}}`:

`AUT(f, N) = (1/(N−1)) · Σ_{k=1}^{N−1} ( f(k) + f(k+1) ) / {{s004}}`

Nó mua được một thứ duy nhất, nhưng đúng thứ cần: con số báo cáo không còn phụ thuộc vào việc tác giả chọn cắt ở đợt nào.

## AUT(f, N) là gì, và nó mua được gì · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** `AUT` **không** so sánh được giữa hai bài dùng `N` khác nhau hoặc độ dài đợt khác nhau. Chuẩn hoá chỉ bỏ độ dài của trục, không bỏ tầm thời gian. Hai bài cùng khai AUT {{s007}} trên {{s005}} tháng và trên {{s008}} tháng là hai tuyên bố khác hẳn nhau.

## Drift của dữ liệu khác drift của nhãn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Drift của dữ liệu khác drift của nhãn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Drift dữ liệu:** `p(x)` đổi, lưu lượng lành năm nay khác năm ngoái. Phát hiện được bằng cách so phân bố đặc trưng, không cần nhãn.

**Drift khái niệm:** `p(y|x)` đổi, tức chính định nghĩa tấn công đổi. Một kiểu quét cổng từng bị gắn nhãn độc giờ là hành vi của một công cụ hợp pháp. Không phát hiện được mà không có nhãn mới.

## Drift của dữ liệu khác drift của nhãn · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** huấn luyện lại định kỳ chỉ chữa được loại thứ nhất. Với loại thứ hai, huấn luyện lại trên nhãn cũ làm mô hình tụt nhanh hơn, vì nó học chắc hơn một quy tắc đã hết đúng. Khi phản biện hỏi về drift mà anh trả lời bằng chu kỳ huấn luyện lại, anh vừa trả lời một nửa câu hỏi.

## Công thức và giả thiết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`AUT(f, N) = (1/(N−1)) · Σ_{k=1}^{N−1} ( f(k) + f(k+1) ) / {{s004}}`

**Giả thiết nó đứng trên:**

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- Mỗi mẫu có mốc thời gian đáng tin, đủ để gán vào đúng một đợt. Dataset không có mốc thời gian thì AUT không tính được, và đó là lý do chính đáng để không dùng dataset đó
- Các đợt dài bằng nhau; nếu không thì phải lấy trọng số theo độ dài đợt, và con số không so được với bài khác
- Nội suy tuyến tính giữa hai đợt liền nhau, tức bỏ qua biến động bên trong một đợt

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- Mô hình KHÔNG được huấn luyện lại trong suốt N đợt; nếu có huấn luyện lại thì phải khai chu kỳ, và AUT lúc đó là của cặp mô hình cộng chu kỳ chứ không phải của mô hình

## Công thức · ghi chú
@phut: 1
@che-do: noi

Hai tính chất kiểm được ngay, dùng để bắt lỗi cài đặt: nếu `f(k) = c` với mọi `k` thì `AUT = c`; nếu `f` giảm tuyến tính từ {{s002}} về {{s009}} thì `AUT = {{s010}}`. Cài đặt nào không ra hai số này là cài đặt sai, thường vì chia cho `N` thay vì `N − {{s002}}`.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s005}} | ràng buộc | TESSERACT đặt ra mấy ràng buộc thời gian riêng biệt cho phần
!so {{s011}} |  | Một bộ phát hiện có F1 giảm tuyến tính từ {{s012}} ở

## Mô hình suy giảm theo cấp số nhân
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình suy giảm theo cấp số nhân, F1 bắt đầu ở {{s003}} và mỗi tháng giữ lại {{s015}} lần tháng trước, đo trên {{s001}} đợt liền nhau, không huấn luyện lại, không khoảng trống. AUT(f, {{s001}}) bằng bao nhiêu?

f0 = {{s013}}, rho = {{s014}}, n = {{s001}}

## Mô hình suy giảm theo cấp số nhân · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`f0⋆(1+rho)/2⋆((1-Math.pow(rho,n-1))/(1-rho))/(n-1)`

Khoảng {{s016}}. Để ý hai chuyện. Thứ nhất, con số này thấp hơn f0 = {{s003}} rất nhiều, tức một bài báo chỉ báo {{s003}} đang báo cái gì đó khác hẳn với điều mà mười hai tháng vận hành sẽ cho. Thứ hai, mất {{s017}} mỗi tháng nghe như là nhỏ, mà sau mười một bước nó kéo F1 cuối kỳ về khoảng {{s018}}, nên AUT tụt xuống quá nửa khoảng cách từ {{s003}} về {{s009}}.

## Mô hình suy giảm theo cấp số nhân · đáp (tiếp)
@phut: 1
@che-do: noi

Cấp số nhân là chỗ trực giác tuyến tính của người đọc sai nhiều nhất.

## Cùng mô hình suy giảm ở trên
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cùng mô hình suy giảm ở trên, f0 = {{s003}}, rho = {{s015}}, {{s001}} đợt. Con số một điểm f0 cao hơn AUT bao nhiêu phần trăm tương đối, tức (f0 − AUT) chia f0 nhân 100?

f0 = {{s013}}, rho = {{s014}}, n = {{s001}}

## Cùng mô hình suy giảm ở trên · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆(f0 - f0⋆(1+rho)/2⋆((1-Math.pow(rho,n-1))/(1-rho))/(n-1))/f0`

Khoảng {{s019}}, tức hơn hai phần năm. Quan trọng: con số này KHÔNG phải mức thổi của chia ngẫu nhiên so với chia theo thời gian trên một dataset thật. Nó là hệ quả thuần của mô hình suy giảm cấp số nhân với rho = {{s015}} mà ta vừa đặt ra, và nó chỉ phụ thuộc rho với N, không phụ thuộc f0.

## Cùng mô hình suy giảm ở trên · đáp (tiếp)
@phut: 1
@che-do: noi

Mức thổi thật phải đo trên dataset thật, và đó là con số bài báo phải báo chứ không được suy ra từ một mô hình suy giảm.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài dùng 10-fold ngẫu nhiên có phân tầng trên CIC-IDS2017, là bộ dữ liệu có mốc thời gian theo từng luồng (flow), trải năm ngày. Ràng buộc TESSERACT nào bị vi phạm TRƯỚC NHẤT?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Tỉ lệ lớp lúc kiểm là tỉ lệ thật
- Nhất quán thời gian khi huấn luyện: fold huấn luyện chứa mẫu có mốc sau mẫu kiểm
- Cửa sổ thời gian của lớp lành và lớp độc phải cùng kỳ
- Không ràng buộc nào, vì phân tầng đã giữ tỉ lệ lớp

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Nhất quán thời gian khi huấn luyện: fold huấn luyện chứa mẫu có mốc sau mẫu kiểm**

Chia ngẫu nhiên trộn mọi mốc thời gian vào cả hai phía, nên trong mỗi fold gần như chắc chắn có mẫu huấn luyện muộn hơn mẫu kiểm. Đó là huấn luyện trên tương lai. Phân tầng giữ được tỉ lệ lớp, tức nó có thể giữ ràng buộc thứ ba, nhưng nó không nói gì về thời gian nên không cứu được ràng buộc thứ nhất.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Đáp án thứ ba cũng có thể bị vi phạm, nhưng nó là tính chất của dataset chứ không phải của cách chia.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Reviewer nói: phân bố lúc chạy khác lúc huấn luyện nên bound tổng quát hoá của anh không áp dụng được. Câu trả lời nào đúng về mặt kỹ thuật?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Bound vẫn áp dụng được, chỉ lỏng hơn, và ta bù bằng cách huấn luyện lại hàng tháng
- Bound mất hiệu lực vì risk thật không còn định nghĩa được khi chưa khai lấy kỳ vọng trên phân bố của thời điểm nào; muốn có phát biểu định lượng phải chuyển sang khung thích ứng miền
- Bound vẫn đúng vì nó không giả thiết gì về phân bố

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Bound không quan trọng, vì AUT đã đo trực tiếp hiệu năng theo thời gian

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Bound mất hiệu lực vì risk thật không còn định nghĩa được khi chưa khai lấy kỳ vọng trên phân bố của thời điểm nào; muốn có phát biểu định lượng phải chuyển sang khung thích ứng miền**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Đáp án thứ nhất là cái bẫy hay gặp nhất: nó đổi một phát biểu không còn định nghĩa được thành một phát biểu lỏng hơn, rồi dùng một biện pháp vận hành để lấp. Đáp án thứ ba sai vì bound dạng đó đòi mẫu i.i.d. từ một phân bố. Đáp án thứ tư đúng một nửa và vì thế nguy hiểm:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

AUT là phép đo mô tả, nó không thay được một chặn, và nó cũng không nói gì về đợt thứ N cộng một.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình được huấn luyện lại mỗi tháng trong suốt mười hai đợt kiểm. AUT(f, {{s001}}) đo được lúc đó là đại lượng của cái gì?

- Của cặp gồm mô hình và chu kỳ huấn luyện lại, nên phải khai cả chu kỳ mới so được
- Của cách chia dữ liệu
- Của mô hình
- Của dataset

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Của cặp gồm mô hình và chu kỳ huấn luyện lại, nên phải khai cả chu kỳ mới so được**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Công thức AUT giả thiết f(k) đo trên MỘT mô hình giữ nguyên. Khi có huấn luyện lại, mỗi f(k) thuộc một mô hình khác, nên con số là hiệu năng của cả quy trình vận hành. Hệ quả thực tế: bài báo so AUT của mình, có huấn luyện lại hàng tháng, với AUT của baseline không huấn luyện lại là một kiểu so mô hình đã tinh chỉnh với baseline để mặc định, chỉ chuyển sang trục thời gian.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau có một chỗ làm toàn bộ phần đánh giá theo thời gian mất giá trị. Bấm vào chỗ đó.

- Chúng tôi sắp xếp toàn bộ luồng theo mốc thời gian,
- lấy {{s020}} đầu làm tập huấn luyện và {{s021}} sau làm tập kiểm,
- rồi lấy mẫu lại tập kiểm về tỉ lệ {{s022}} giữa lành và độc để tránh lệch lớp,
- và báo F1 theo từng tháng cùng AUT trên mười hai đợt.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**rồi lấy mẫu lại tập kiểm về tỉ lệ {{s022}} giữa lành và độc để tránh lệch lớp,**

Hai câu đầu thoả ràng buộc nhất quán thời gian. Câu này phá ràng buộc thứ ba của TESSERACT: tỉ lệ lớp lúc kiểm phải là tỉ lệ thật. Hậu quả không phải là một con số kém chính xác hơn, mà là precision, F1 và mọi AUT dựng trên chúng không còn chuyển được sang vận hành. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

giữ tỉ lệ thật ở tập kiểm, chỉ dùng lấy mẫu lại cho tập huấn luyện, và nếu vẫn muốn có một bảng cân bằng thì khai nó là bảng phụ với tỉ lệ nền (base rate) được ghi rõ.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn trả lời phản biện sau có một câu không đứng được. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi đồng ý rằng chia ngẫu nhiên là quá lạc quan, nên đã thêm một bảng chia theo thời gian.
- Vì phân bố đổi theo thời gian, bound tổng quát hoá ở Mệnh đề {{s002}} trở nên lỏng hơn nhưng vẫn áp dụng được.
- Bảng mới báo F1 theo từng tháng và AUT trên mười hai đợt, giữ nguyên tỉ lệ lớp thật ở tập kiểm.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi cũng khai rằng mô hình không được huấn luyện lại trong suốt mười hai đợt này.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì phân bố đổi theo thời gian, bound tổng quát hoá ở Mệnh đề {{s002}} trở nên lỏng hơn nhưng vẫn áp dụng được.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Đây đúng chỗ cần tránh. Khi mẫu kiểm không rút từ cùng phân bố với mẫu huấn luyện, risk thật ở vế trái của bound không còn định nghĩa được, vì chưa khai lấy kỳ vọng trên phân bố của thời điểm nào. Mất hiệu lực không phải lỏng hơn. Cách sửa: hạ Mệnh đề {{s002}} xuống thành phát biểu trong giả thiết i.i.d.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

và nói rõ nó không phủ chế độ drift, rồi để phần thời gian cho AUT với một đại lượng mô tả chứ không cho một chặn. Nếu thật muốn một chặn thì phải viết nó trong khung thích ứng miền, và khung đó đòi thêm một đại lượng đo khoảng cách hai phân bố.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt f(k) là hiệu năng đo trên đợt thời gian thứ k, với k chạy từ {{s002}} tới N, mô hình giữ nguyên suốt N đợt
- Nối hai điểm liền nhau bằng một đoạn thẳng. Diện tích hình thang thứ k là ( f(k) + f(k+1) ) / {{s004}}
- Cộng N − {{s002}} hình thang để lấy diện tích thô: Σ_{k=1}^{N−1} ( f(k) + f(k+1) ) / {{s004}}

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Chia cho N − {{s002}}, vì N điểm chỉ tạo ra N − {{s002}} đoạn. Được AUT(f, N) nằm trong [{{s006}}] khi f nằm trong [{{s006}}]
- Kiểm lại bằng hai trường hợp biên: f hằng bằng c cho AUT = c, và f giảm tuyến tính từ {{s002}} về {{s009}} cho AUT = {{s010}}

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: f0 {{s003}} · AUT(f, {{s001}}) {{s023}} · F1 đợt cuối {{s024}} · mọi bound i.i.d. còn áp dụng được

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Phân bố lúc kiểm giống lúc huấn luyện, tức i.i.d.** tắt đi: Lưu lượng và tập tấn công đổi theo thời gian, nên mẫu kiểm rút từ một phân bố khác mẫu huấn luyện.
- **Mỗi mẫu có mốc thời gian đáng tin** tắt đi: Dataset không ghi mốc thời gian cho từng mẫu, hoặc mốc đó là thời điểm thu thập chứ không phải thời điểm xuất hiện.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Định nghĩa tấn công giữ nguyên trong suốt N đợt** tắt đi: Nhãn đổi theo thời gian, tức p(y|x) đổi. Một hành vi từng là độc giờ là hành vi của công cụ hợp pháp, hoặc ngược lại.
- **Tỉ lệ lớp lúc kiểm là tỉ lệ thật** tắt đi: Tập kiểm bị lấy mẫu lại hoặc cân bằng, nên tỉ lệ nền lúc đo khác lúc chạy.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Mô hình suy giảm theo cấp số nhân: f(k) = f0 · rho^(g + k − {{s002}}). Kéo hệ số giữ lại mỗi đợt, số đợt, và độ dài khoảng trống thời gian giữa huấn luyện và đợt kiểm đầu. Xem con số một điểm và AUT tách nhau ra.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.5` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The evaluation in Section V uses stratified 10-fold cross-validation over the entire capture. Since every flow in this dataset carries a timestamp, the folds train on traffic that is chronologically later than the traffic they are tested on. The reported F1 is therefore an upper bound under an assumption the deployment setting violates. Please provide a time-aware split, report performance per test period, and state what the reported single number now means.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced the cross-validation protocol. Section V-A now states the three temporal constraints separately and how each is enforced: training flows strictly precede test flows; the benign and malicious windows coincide; and the test split keeps the native class ratio, with resampling confined to training.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table VI reports F1, TPR and FPR for each of the twelve monthly test periods, with bootstrap intervals, together with AUT over those periods, and it states explicitly that the model is not retrained during the evaluation window, so the figure characterises the model alone rather than a model plus a retraining policy. The random-split row is retained but relabelled as an optimistic upper bound and is no longer used to support any deployment claim.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also report AUT computed on TPR in addition to AUT computed on F1, because only the former is comparable against work evaluated at a different class prior. Finally, Proposition {{s002}} has been restated under an explicit i.i.d. assumption and we no longer describe the bound as looser under distribution shift:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

once train and test are drawn from different distributions the true risk on the left hand side is not defined until the reference distribution is named, so the bound does not apply at all. Section V-E gives a descriptive drift analysis in its place, and the discussion separates covariate drift from label drift rather than treating retraining as an answer to both.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: nhận là chia ngẫu nhiên có hạn chế, rồi lập luận rằng đây là thực hành phổ biến trong lĩnh vực và các bài trước cũng làm thế. Đúng về thực hành, không trả lời được phản bác, và mời reviewer đi tìm ba bài khác đã làm đúng.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: thêm một bảng chia theo thời gian với một con số F1 duy nhất cho toàn kỳ kiểm, và báo cả hai bảng. Đã đúng hướng nhưng vẫn là một con số một điểm, nên chưa trả lời được việc nó có suy giảm hay không, và vẫn chưa nói mô hình có được huấn luyện lại hay không.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s005}}: chia theo thời gian với cả ba ràng buộc TESSERACT được khai rời nhau, báo hiệu năng theo từng đợt kèm AUT, giữ nguyên tỉ lệ lớp thật ở tập kiểm, khai rõ mô hình không được huấn luyện lại trong kỳ, và giữ bảng chia ngẫu nhiên nhưng dán nhãn lại là chặn trên chứ không phải ước lượng vận hành.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

You report AUT of {{s025}} and compare it with {{s026}} reported by prior work to claim an improvement. The two evaluations use different numbers of test periods and different period lengths. Please justify the comparison or withdraw it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The comparison has been withdrawn from the abstract, the results section and the conclusion. We now report AUT only within our own setting and we state the setting next to the number: twelve consecutive monthly periods, a total horizon of twelve months, no retraining, AUT computed on F1 and also on TPR. We make the limitation explicit:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the normalisation in AUT divides by the number of intervals, so it removes the length of the axis but not the horizon or the period length, and a longer horizon systematically lowers AUT for the same detector. A lower published AUT therefore does not imply a weaker model.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Where the prior implementation is available we reran it over our own period grid and report that co-designed pair in Table VII; for the two systems whose code is not available we keep the numbers separate and say so rather than placing them in one column.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: lập luận rằng AUT đã được chuẩn hoá về đoạn không đơn vị nên so sánh được. Sai, và đây đúng là chỗ reviewer đang chỉ vào.
- Mức {{s004}}: nhận rằng hai thiết lập khác nhau, rồi thêm một câu cảnh báo trong phần thảo luận mà vẫn giữ nguyên câu so sánh ở phần kết quả và trong tóm tắt. Mặt tiền vẫn hứa cái mà thân bài đã rút lại.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s005}}: rút câu so sánh trực tiếp, chỉ giữ AUT của mình kèm khai rõ số đợt, độ dài một đợt, tầm thời gian tổng, và đại lượng được lấy tích phân. Nói rõ AUT là con số trong một thiết lập chứ không phải một thang chung.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.5` bấm thẻ.
