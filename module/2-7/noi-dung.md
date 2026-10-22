---
tieu-de: Phòng vệ và giới hạn cứng của nó
phu-de: Trụ 2 FL · module 2.7
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 83.5
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

Bộ tổng hợp bền của tôi chịu được tỉ lệ kẻ xấu tới đâu, và tôi đã khai con số đó chưa?

## Phòng vệ và giới hạn cứng của nó
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này có hai con số phải nhớ và một điều phải hiểu.

## Phòng vệ và giới hạn cứng của nó (tiếp)
@phut: 1
@che-do: noi

Hai con số: **điều kiện tồn tại của Krum là `n ≥ 2f + {{s001}}`**, và **trần nguyên lý của mọi bộ tổng hợp là `f/n` nhỏ hơn {{s002}}**. Con số thứ hai không phải giới hạn của Krum mà là giới hạn của bài toán: khi nhóm xấu chiếm từ một nửa trở lên thì phân bố của nó không phân biệt được với phân bố thật, nên không có thuật toán nào, kể cả thuật toán chưa được phát minh, làm được.

## Phòng vệ và giới hạn cứng của nó (tiếp)
@phut: 1
@che-do: noi

Điều phải hiểu thì khó hơn: **mọi bộ tổng hợp bền dựa khoảng cách đều giả định các cập nhật lành gần nhau.** Giả thiết đó chính là chỗ non-IID đánh vào. Khi dữ liệu lệch nặng, client hiếm trông y như kẻ xấu, nên Krum loại đúng những client mang lớp tấn công hiếm. Và vì Krum chọn MỘT cập nhật thay vì lấy trung bình, nó bỏ luôn phần giảm phương sai theo `1/sqrt(n)` mà trung bình thường có sẵn.

## Phòng vệ và giới hạn cứng của nó (tiếp)
@phut: 1
@che-do: noi

Hệ quả cho bài báo rất cụ thể: một bài FL bền vững **bắt buộc** phải báo trường hợp **{{s003}} kẻ xấu với non-IID nặng**. Thiếu dòng đó thì bảng kết quả không phân biệt được phòng vệ có ích với phòng vệ đang âm thầm cắt mất dữ liệu quý nhất.

## Điểm Krum và điều kiện tồn tại n ≥ 2f + 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Điểm Krum và điều kiện tồn tại n ≥ 2f + 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Điểm của client `i` là `s(i) = tổng theo j của ||w_i − w_j||²`, lấy trên `n − f − {{s004}}` láng giềng gần nhất của `i`. Server chọn client có điểm nhỏ nhất.

## Điểm Krum và điều kiện tồn tại n ≥ 2f + 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **con số `n − f − {{s004}}` trong định nghĩa là nguồn của điều kiện `n ≥ 2f + {{s001}}`**, và từ đó ra trần `f ≤ (n − 3)/2`, tức `f/n ≤ {{s002}} − 3/(2n)`. Hai hệ quả thực tế. Một, Krum cần BIẾT `f`, hoặc ít nhất một chặn trên của `f`, nên nó không phải phòng vệ không tham số. Hai, với `n` nhỏ thì điều kiện này chặt một cách đáng ngạc nhiên:

## Điểm Krum và điều kiện tồn tại n ≥ 2f + 3 · đáp (tiếp)
@phut: 1
@che-do: noi

muốn chịu đúng một kẻ xấu đã cần tối thiểu {{s005}} client mỗi vòng.

## Giá của tính bền
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Giá của tính bền · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Trung bình của `n` cập nhật độc lập có sai số nhỏ hơn một cập nhật đơn lẻ theo hệ số `1/sqrt(n)`. Krum chọn đúng một cập nhật, nên nó **bỏ hết phần lợi đó**.

## Giá của tính bền · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **với {{s003}} kẻ xấu, Krum gần như luôn TỆ HƠN trung bình thường, và tệ hơn đúng một hệ số cỡ `sqrt(n)`.** Với `n = {{s006}}` thì đó là {{s007}} lần. Đây không phải lỗi cài đặt, nó là định nghĩa: tính bền được mua bằng cách bỏ thông tin của `n − {{s008}}` client. Trung bình cắt `beta` và trung vị theo toạ độ mất ít hơn vì chúng vẫn tổng hợp nhiều cập nhật, nhưng chúng cũng mất.

## Giá của tính bền · đáp (tiếp)
@phut: 1
@che-do: noi

Nên câu hỏi đúng không phải phòng vệ có bền không, mà là **ở tỉ lệ kẻ xấu nào thì phần bền mua được mới bù nổi phần phương sai mất đi**.

## Khái niệm tầng 4
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s009}} trên bốn.*

## Khái niệm tầng 4 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khi `f/n ≥ {{s002}}`, nhóm xấu có thể dựng một phân bố cập nhật mà server không phân biệt được với phân bố của nhóm lành. Hai thế giới đối xứng, và server không có mẩu thông tin nào để phá đối xứng.

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **đây là kết quả bất khả thi, nên một bài khai chịu được tỉ lệ kẻ xấu từ một nửa trở lên là bài đang khai một thứ không tồn tại, bất kể thí nghiệm cho con số gì.** Nếu thí nghiệm thật cho kết quả tốt ở `f/n = {{s010}}` thì nguyên nhân nằm ở chỗ khác:

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

kẻ tấn công trong mô phỏng quá yếu, hoặc nhóm xấu bị buộc nộp cập nhật giống nhau nên dễ nhận ra, hoặc phép đo đang đo thứ khác. Dấu hiệu nên làm anh đi tìm lỗi, không nên làm anh viết một câu mạnh hơn.

## Ba bộ tổng hợp bền
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Krum: s(i) = tổng trên n−f−2 láng giềng gần nhất của ||w_i − w_j||², chọn i nhỏ nhất, cần n ≥ 2f+3; Trung bình cắt beta: bỏ beta phần cao nhất và thấp nhất theo TỪNG toạ độ, cần beta ≥ f/n; Trung vị theo toạ độ: điểm đổ vỡ {{s002}}; Trần chung: không bộ tổng hợp nào bền khi f/n ≥ {{s002}}`

## Ba bộ tổng hợp bền (tiếp)
@phut: 1
@che-do: so

**Giả thiết nó đứng trên:**

## Ba bộ tổng hợp bền (tiếp)
@phut: 1
@che-do: so

- Các cập nhật của client lành gần nhau trong không gian tham số, nên khoảng cách lớn là dấu hiệu của kẻ xấu. Đây là giả thiết mà non-IID phá
- f được biết, hoặc có một chặn trên của f, vì cả n−f−2 của Krum và beta của trung bình cắt đều cần con số đó
- n ≥ 2f + {{s001}}, nếu không thì số láng giềng n−f−2 không còn đủ để bảo đảm có láng giềng lành trong tập so

## Ba bộ tổng hợp bền (tiếp)
@phut: 1
@che-do: so

- Sai số của trung vị theo toạ độ tăng theo số chiều, nên điểm đổ vỡ {{s002}} không có nghĩa là không mất gì ở mô hình lớn

## Ba bộ tổng hợp bền · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Ba bộ này trả ba loại đầu ra khác nhau: Krum trả một cập nhật CÓ THẬT của một client, trung bình cắt và trung vị trả một vector KHÔNG phải cập nhật của ai. Khác biệt đó đáng để ý khi ghép với DP hoặc với secure aggregation, vì cả hai đòi server thao tác trên tổng chứ không phải trên từng cập nhật.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s011}} | kẻ xấu | Server lấy n = {{s006}} client mỗi vòng và dùng Krum. Theo
!so {{s012}} |  | Trần nguyên lý cho MỌI bộ tổng hợp
!so {{s005}} | client | Điều kiện tồn tại của Krum là n ≥ 2f + {{s001}}.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một hệ cross-silo chỉ có {{s013}} site và site nào cũng dự mỗi vòng. Krum chịu được tối đa bao nhiêu site xấu?

n = {{s013}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.floor((n - {{s001}}) / {{s004}})`

Bằng {{s014}}, vì ({{s013}} − 3)/2 = {{s014}} đúng. Hai điều phải đọc. Một, tỉ lệ chịu được là {{s014}} trên {{s013}}, tức khoảng {{s015}}, chưa tới một nửa đúng như trần nguyên lý đòi. Hai, và đây là chỗ hay sai: con số {{s014}} là chặn TỒN TẠI của thuật toán, không phải tỉ lệ kẻ xấu mà bài của anh đo được.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Dùng nó làm tuyên bố thực nghiệm là nhầm một chặn lý thuyết với một kết quả, vì ở gần chặn đó độ chính xác đã tụt từ lâu trước khi thuật toán ngừng chạy.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Krum chạy với {{s006}} client mỗi vòng và chặn trên của số kẻ xấu đặt là {{s016}}. Điểm Krum của mỗi client lấy tổng trên bao nhiêu láng giềng?

n = {{s006}}, f = {{s016}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`n - f - {{s004}}`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Bằng {{s017}} láng giềng. Để ý con số này giảm khi anh khai f bi quan hơn: khai f = {{s011}} thì chỉ còn {{s018}} láng giềng, và khai f = {{s019}} với n = {{s006}} thì điều kiện n ≥ 2f+3 vỡ. Nên chặn trên của f không phải một tham số an toàn miễn phí: khai cao cho chắc là tự thu hẹp tập so sánh, và tới một mức thì thuật toán không còn định nghĩa được.

## Một bài khai dùng Krum với 7 site
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài khai dùng Krum với {{s020}} site, chặn trên của số site xấu là {{s001}}. Vấn đề là gì?

- Chặn trên quá bi quan, nên độ chính xác tụt
- Điều kiện n ≥ 2f + {{s001}} không thoả, vì {{s020}} nhỏ hơn {{s021}}, nên Krum không có bảo đảm nào ở cấu hình này
- Số site quá ít để chạy FL
- Phải dùng trung bình cắt thay vì Krum khi số site là số lẻ

## Một bài khai dùng Krum với 7 site · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Điều kiện n ≥ 2f + {{s001}} không thoả, vì {{s020}} nhỏ hơn {{s021}}, nên Krum không có bảo đảm nào ở cấu hình này**

## Một bài khai dùng Krum với 7 site · đáp (tiếp)
@phut: 1
@che-do: noi

Với f = {{s001}} thì điều kiện đòi n tối thiểu bằng {{s021}}, còn hệ chỉ có {{s020}}. Thuật toán vẫn chạy và vẫn trả về một client, nhưng không có định lý nào gắn kết quả đó với cập nhật lành, nên đây không phải chuyện độ chính xác mà là chuyện bảo đảm không tồn tại. Phương án A mô tả một hệ quả có thật nhưng ở cấu hình khác, cấu hình mà điều kiện còn thoả.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bảng kết quả cho thấy Krum tệ hơn FedAvg ở cột {{s003}} kẻ xấu với alpha = {{s022}}, và tốt hơn ở cột {{s023}} kẻ xấu với alpha = {{s008}}. Cách đọc nào đúng?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Cài đặt Krum có lỗi, vì bộ bền không thể tệ hơn khi không có kẻ xấu
- Cả hai ô đều là hành vi đúng: tính bền được mua bằng cách bỏ thông tin của n − {{s008}} client, nên lợi hay lỗ phụ thuộc cặp tỉ lệ kẻ xấu và độ lệch dữ liệu
- alpha = {{s022}} là cấu hình không thực tế nên bỏ ô đó đi

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Phải báo giá trị trung bình của hai ô để kết luận công bằng

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cả hai ô đều là hành vi đúng: tính bền được mua bằng cách bỏ thông tin của n − {{s008}} client, nên lợi hay lỗ phụ thuộc cặp tỉ lệ kẻ xấu và độ lệch dữ liệu**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Krum chọn một cập nhật nên nó không có phần giảm phương sai 1/sqrt(n), và nó loại các client xa trung tâm, tức đúng các client hiếm khi dữ liệu lệch. Hai ô đó không mâu thuẫn, chúng là hai điểm của cùng một mặt đánh đổi. Phương án D là cách nhanh nhất để xoá mất thông tin có ích nhất của bảng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai phương pháp của họ giữ được độ chính xác ở tỉ lệ kẻ xấu {{s025}}. Việc đầu tiên nên làm là gì?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chấp nhận kết quả, vì đó là số đo thực nghiệm chứ không phải lý thuyết
- Đi tìm lỗi, vì f/n từ một nửa trở lên là vùng bất khả thi, nên con số tốt là dấu hiệu kẻ tấn công trong mô phỏng quá yếu hoặc phép đo sai
- Yêu cầu họ chạy thêm với {{s024}} để xem có bền tới đó không
- Kết luận họ đã vượt được trần nguyên lý nhờ một giả thiết mới

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Đi tìm lỗi, vì f/n từ một nửa trở lên là vùng bất khả thi, nên con số tốt là dấu hiệu kẻ tấn công trong mô phỏng quá yếu hoặc phép đo sai**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Kết quả bất khả thi không phải một chặn lỏng có thể vượt bằng thuật toán tốt hơn: nó nói server không có thông tin để phá đối xứng. Một số đo nằm trong vùng bất khả thi chỉ có hai cách giải thích, là mô hình đe doạ trong mô phỏng yếu hơn mô hình đã khai, hoặc phép đo đang đo thứ khác.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Phương án D chỉ đứng được nếu bài đã khai thêm một giả thiết phá đối xứng, ví dụ một tập xác thực sạch ở server, và lúc đó bài phải khai tập đó như một thành phần tin cậy.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả phòng vệ sau có một câu không đứng được. Bấm vào câu đó.

- Server tổng hợp bằng Krum với n = {{s006}} client mỗi vòng và chặn trên f = {{s016}}.
- Điểm Krum của mỗi client lấy tổng bình phương khoảng cách tới {{s017}} láng giềng gần nhất.
- Vì Krum không dùng trung bình, phương pháp không bị ảnh hưởng bởi độ lệch dữ liệu giữa các client.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì Krum không dùng trung bình, phương pháp không bị ảnh hưởng bởi độ lệch dữ liệu giữa các client.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu đầu đúng và khớp nhau: n − f − {{s004}} = {{s017}}. Câu thứ ba là lỗi, và nó sai ngược hẳn chiều: Krum phụ thuộc độ lệch dữ liệu NHIỀU HƠN trung bình thường, không ít hơn. Toàn bộ cơ sở của nó là giả thiết cập nhật lành gần nhau, nên khi dữ liệu lệch thì client hiếm trông như kẻ xấu và bị loại. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

thay câu đó bằng một câu khai đúng chiều, rằng Krum dựa trên giả thiết các cập nhật lành gần nhau nên hiệu lực của nó giảm khi dữ liệu lệch, kèm một dòng bảng ở {{s003}} kẻ xấu với non-IID nặng để đo chính chuyện đó.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phần kết quả sau có một dòng làm cả bảng không trả lời được câu hỏi của chính nó. Bấm vào dòng đó.

- Bảng V so bốn bộ tổng hợp ở các tỉ lệ kẻ xấu {{s026}}, {{s023}} và {{s027}}.
- Mỗi ô là trung bình trên {{s005}} hạt giống, kèm độ lệch chuẩn.
- Phân vùng dữ liệu dùng Dirichlet với alpha = {{s028}}, và mọi cột đều có tấn công nên bảng không có cột {{s003}} kẻ xấu.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Phân vùng dữ liệu dùng Dirichlet với alpha = {{s028}}, và mọi cột đều có tấn công nên bảng không có cột {{s003}} kẻ xấu.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai dòng đầu là thiết kế thí nghiệm tốt: nhiều tỉ lệ kẻ xấu, nhiều hạt giống, có độ lệch chuẩn. Dòng thứ ba mới là chỗ bảng mất hiệu lực. Bài dùng alpha = {{s028}}, tức non-IID nặng, mà lại không có cột {{s003}} kẻ xấu, nên không có cách nào tách phần độ chính xác mất do TẤN CÔNG ra khỏi phần mất do bộ tổng hợp bền LOẠI OAN client hiếm.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai nguyên nhân này cho cùng một dấu hiệu trong bảng. Cách sửa rẻ nhất là thêm đúng một cột {{s003}} kẻ xấu ở cùng alpha, không cần thí nghiệm mới nào ngoài cột đó.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Ghi điều kiện tồn tại của Krum: n ≥ 2f + {{s001}}
- Giải theo f: f ≤ (n − 3)/2
- Lấy phần nguyên dưới vì f là số nguyên không âm; với n = {{s006}} thì f ≤ {{s029}} nên f tối đa là {{s011}}
- Chia hai vế cho n: f/n ≤ (n − 3)/(2n) = {{s002}} − 3/(2n)

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Cho n lớn thì chặn trên tiến về {{s002}} từ bên dưới, và {{s002}} cũng đúng là trần nguyên lý của MỌI bộ tổng hợp

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: n = {{s006}} client mỗi vòng · f = {{s016}} kẻ xấu · alpha = {{s008}} · độ mạnh tấn công {{s007}} · điều kiện n ≥ 2f+3 thoả vì f tối đa là {{s011}} · điểm Krum lấy trên {{s017}} láng giềng · sai số trung bình thường {{s031}} · sai số Krum {{s032}} · lợi thế của Krum cộng {{s033}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Các cập nhật của client lành gần nhau trong không gian tham số** tắt đi: Dữ liệu lệch nặng, ví dụ alpha của Dirichlet bằng {{s030}}, nên client lành nằm rải rác và client hiếm xa hẳn phần còn lại.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Số client mỗi vòng thoả điều kiện n ≥ 2f + {{s001}}** tắt đi: Triển khai thật chỉ có {{s020}} site mà chặn trên của số site xấu được khai là {{s001}}, nên n = {{s020}} nhỏ hơn 2·3 + {{s001}} = {{s021}}.
- **Tỉ lệ kẻ xấu nhỏ hơn một nửa** tắt đi: f/n bằng {{s010}}, ví dụ một liên minh chiếm phần lớn client trong các vòng mà nó chọn.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biết f, hoặc có một chặn trên đáng tin của f** tắt đi: Số kẻ xấu không biết và không có cách ước lượng, nên server phải tự chọn một con số.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Server lấy {{s006}} client mỗi vòng và dùng Krum, nên nó chịu được tới {{s018}} client độc hại, tức một nửa.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỔ**

ĐỔ, và lệch đúng hai đơn vị, tức kiểu lệch không ai thấy khi đọc nhanh. Điều kiện trong nguồn là n > 2f + {{s004}}, chứ không phải n > 2f. Với n = {{s006}} thì 2f < {{s034}}, nên f < {{s019}}, và f nguyên cho f tối đa là {{s011}}. Krum KHÔNG chịu được một nửa. Nhầm sang {{s018}} là nhầm sang giả thiết của phép lấy trung vị theo toạ độ, một cơ chế khác.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Hai bộ tổng hợp cạnh nhau trên cùng một mô hình sai số quy ước: trung bình thường được lợi 1/sqrt(n) nhưng bị kẻ xấu kéo đi, còn Krum chọn một cập nhật nên miễn nhiễm với kẻ xấu mà phải trả cả phần phương sai. Nhiệm vụ của anh là tìm vùng tham số mà bộ BỀN lại TỆ HƠN.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.7` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table V reports robust aggregation only under attack, at malicious fractions of {{s026}}, {{s023}} and {{s027}}, with Dirichlet alpha = {{s035}}. Without a zero-attacker column at the same alpha, the reported accuracy drop cannot be attributed to the attack rather than to the aggregator discarding legitimate minority clients. Please add that control and discuss it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have added the control and it changed two of our conclusions. Table V now carries a zero-attacker column at the same alpha = {{s035}}. Under FedAvg with no attacker, macro-F1 is {{s036}}; under Krum with no attacker it is {{s037}}, a loss of {{s038}} points that is caused entirely by the aggregator, since there is no attack to resist.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

At {{s023}} malicious clients, FedAvg falls to {{s039}} and Krum holds at {{s040}}, so the honest accounting is that Krum buys {{s041}} points of attack resistance at a standing cost of {{s038}} points, not that Krum preserves accuracy. We also report the mechanism rather than only the numbers: Krum selects a single update, so it forgoes the 1/sqrt(n) variance reduction that averaging provides, and its distance-based selection systematically rejects the clients furthest from the centroid.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table VIII makes the second effect visible by reporting per-class recall: under Krum with no attacker, recall on the three rarest attack classes drops from {{s042}}, {{s043}} and {{s044}} to {{s045}}, {{s046}} and {{s047}}, while recall on the two most common classes is unchanged. For an intrusion detector this is the cost that matters, because the rare classes are the ones the system exists to catch. Section VI now states the operating condition explicitly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

our defence is worth its cost above roughly {{s048}} malicious clients at this alpha, and below that threshold plain averaging is the better choice.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s008}}: trả lời rằng mục tiêu của bài là đánh giá dưới tấn công nên cột {{s003}} kẻ xấu không liên quan. Không trả lời được: thiếu cột đó thì chính con số dưới tấn công không gán được nguyên nhân.
- Mức {{s004}}: thêm cột {{s003}} kẻ xấu và báo con số, nhưng để nó ở phụ lục và không sửa kết luận nào trong phần chính.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: thêm cột {{s003}} kẻ xấu vào bảng chính, tách rõ phần mất do tấn công và phần mất do bộ tổng hợp, và sửa những câu kết luận nào không còn đứng.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V-D claims that the proposed aggregator maintains accuracy at a malicious fraction of {{s025}}. This exceeds the information-theoretic limit for Byzantine-robust aggregation, where the malicious distribution becomes indistinguishable from the honest one. Please either identify the additional assumption that breaks the symmetry, or withdraw the claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is correct and we have traced the number to its cause rather than softening the wording. Our malicious clients were implemented as a single shared perturbation applied by all of them, so at {{s025}} they formed a tight cluster that the aggregator separated easily. That is an artefact of the attack implementation, not robustness: a colluding group that instead mimics the honest update distribution removes the separation entirely, and we verified this.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

With the corrected attacker, accuracy collapses at {{s049}} as the impossibility result predicts, and we now report the full sweep from {{s026}} to {{s025}} in Figure {{s020}} with the {{s049}} boundary marked. All claims above {{s049}} have been withdrawn from the abstract, Section I and Section V-D. We also note what would have been required to make such a claim legitimately: a symmetry-breaking assumption such as a small clean validation set held by the server, which our deployment does not have.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Section VI now states this as a limitation and names it, so that a future version adding such a component reports it as a trusted element rather than as an improvement to the aggregator.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s008}}: khẳng định lại con số và nói rằng đó là số đo thực nghiệm chứ không phải chặn lý thuyết. Không trả lời được: kết quả bất khả thi nói chính chuyện số đo đó phải có nguyên nhân khác.
- Mức {{s004}}: rút tuyên bố và sửa về vùng dưới một nửa. Trả lời đúng nhưng chưa nói vì sao thí nghiệm lại cho con số đó, nên lỗi vẫn còn trong mã.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: rút tuyên bố, cộng truy ra nguyên nhân thật trong thiết lập thí nghiệm (ví dụ nhóm xấu bị buộc nộp cập nhật giống nhau nên dễ tách, hoặc kẻ tấn công không thích nghi với phòng vệ), cộng chạy lại với kẻ tấn công đã sửa.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.7` bấm thẻ.
