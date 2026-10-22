---
tieu-de: Tấn công vào FL
phu-de: Trụ 2 FL · module 2.6
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 81
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

Trong ba họ tấn công (suy luận, đầu độc, cửa hậu (backdoor)), họ nào áp được vào hệ của tôi với đúng năng lực kẻ tấn công (attacker capability) mà tôi đã khai?

## Tấn công vào FL
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này không liệt kê tấn công. Nó làm đúng một việc: biến **năng lực kẻ tấn công** thành bốn công tắc có thể bật tắt, rồi đọc ra **tập tấn công còn khả thi**. Bốn năng lực đó là: thấy gradient thô của từng client, biết kiến trúc và hàm mất mát, chọn được client bị kiểm soát, và dự được nhiều vòng liên tiếp.

## Tấn công vào FL (tiếp)
@phut: 1
@che-do: noi

Lý do phải làm theo chiều này: ba họ tấn công đòi ba bộ năng lực khác nhau, và chúng không trùng nhau. **Suy luận** (truy ngược gradient (gradient inversion), suy luận thành viên (membership inference)) đòi thấy gradient thô hoặc mô hình, cộng biết kiến trúc. Không đòi kiểm soát client nào. **Đầu độc và cửa hậu** đòi kiểm soát được client và được chọn trong vòng. Không đòi thấy gradient của ai khác. Hệ quả thực tế:

## Tấn công vào FL (tiếp)
@phut: 1
@che-do: noi

một bài khai mô hình đe doạ (threat model) mạnh ở phần tấn công rồi lặng lẽ dùng mô hình yếu ở phần phòng vệ là bài tự so với chính mình. Reviewer bắt chỗ này bằng cách đặt hai mục cạnh nhau, và đó là một câu hỏi không có cách trả lời bằng thêm thí nghiệm.

## Truy ngược gradient (gradient inversion)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Truy ngược gradient (gradient inversion) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Kẻ tấn công giải `min` theo `(x', y')` của `||grad W(x', y') − grad W||²`, tức tìm đầu vào giả sinh ra đúng gradient đã quan sát.

## Truy ngược gradient (gradient inversion) · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **bốn giả thiết của nó đều là giả thiết về HỆ, không phải về thuật toán tấn công.** Cần biết kiến trúc và hàm mất mát (để tính được vế trong), cần thấy gradient THÔ của một client (không phải tổng), cần lô nhỏ (vì gradient của lô lớn là tổng nhiều mẫu nên bài toán nghịch đảo nhoè đi), và cần không có nhiễu DP đáng kể.

## Truy ngược gradient (gradient inversion) · đáp (tiếp)
@phut: 1
@che-do: noi

Tắt bất kỳ cái nào trong hai cái đầu thì hàm mục tiêu trên KHÔNG CÒN LẬP ĐƯỢC, chứ không phải tấn công yếu đi. Đó là lý do secure aggregation là phòng vệ đúng loại cho họ tấn công này, còn bộ tổng hợp bền thì không liên quan.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Kẻ tấn công nộp `X = gamma·(X_xau − G_t) + G_t` với `gamma = n/eta`. Sau khi server lấy trung bình với bước `eta` trên `n` client, mô hình toàn cục bằng ĐÚNG mô hình xấu, trong một vòng duy nhất.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **điều kiện sống của tấn công này là mô hình đã gần hội tụ, vì lúc đó các cập nhật lành gần triệt tiêu nhau nên chỉ còn số hạng của kẻ xấu.** Và giá của nó là chuẩn: với `n = {{s003}}` và `eta = {{s004}}` thì `gamma = {{s003}}`, nên cập nhật của kẻ xấu lớn hơn cập nhật lành khoảng hai bậc.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Chính vì thế chặn chuẩn ở server (norm clipping) là phòng vệ rẻ nhất cho đúng tấn công này, và cũng chính vì thế kẻ tấn công biết chặn chuẩn sẽ hạ `gamma` xuống rồi đổi lấy nhiều vòng. Hai bên đang đánh đổi cùng một thứ: chuẩn và thời gian.

## Lợi thế của bộ phân biệt thành viên
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Lợi thế của bộ phân biệt thành viên · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Suy luận thành viên không đo bằng accuracy. Nó đo bằng `Adv = TPR − FPR`, tức lợi thế so với tung đồng xu, vì một bộ phân biệt luôn trả lời có thành viên đã có TPR bằng {{s004}}.

## Lợi thế của bộ phân biệt thành viên · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **trên tập cân bằng thì `Adv = 2·accuracy − {{s004}}`, nên accuracy {{s005}} tương ứng lợi thế {{s006}}, còn accuracy {{s007}} tương ứng lợi thế {{s008}}.** Và cũng như mọi phép đo phụ thuộc tỉ lệ nền (base rate), accuracy của tấn công suy luận trên tập cân bằng là con số dễ nhất:

## Lợi thế của bộ phân biệt thành viên · đáp (tiếp)
@phut: 1
@che-do: noi

tỉ lệ thành viên thật trong một hệ thật nhỏ hơn {{s009}} rất nhiều, nên phải báo TPR ở FPR thấp (ví dụ TPR tại FPR bằng {{s010}}) thay vì báo accuracy. Đây là cùng một lớp lỗi với module {{s011}}, chỉ đổi vai.

## Khái niệm tầng 4
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s012}} trên bốn.*

## Khái niệm tầng 4 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mỗi tuyên bố về tấn công tiêu thụ một bộ năng lực, và mỗi tuyên bố về phòng vệ cũng tiêu thụ một bộ năng lực. Nếu hai bộ đó khác nhau thì bài đang kể hai câu chuyện về hai hệ khác nhau.

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **dấu hiệu hay gặp nhất là phần tấn công giả định kẻ xấu biết phân bố dữ liệu toàn cục để dựng cập nhật xấu, còn phần phòng vệ giả định kẻ xấu không biết ngưỡng chặn chuẩn của server.** Không có lý do nào cho kẻ tấn công mạnh ở chỗ này mà yếu ở chỗ kia.

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

Cách sửa rẻ nhất là viết một bảng năng lực duy nhất ở đầu phần đánh giá, rồi mọi thí nghiệm đều trỏ về bảng đó; cách sửa đắt hơn nhưng đáng là báo cả kết quả với kẻ tấn công thích nghi, tức kẻ biết phòng vệ.

## Ba họ tấn công
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`truy ngược gradient: min theo (x', y') của ||grad W(x', y') − grad W||² ; thay thế mô hình: X = gamma·(X_xau − G_t) + G_t, gamma = n/eta ; suy luận thành viên: Adv = TPR − FPR`

**Giả thiết nó đứng trên:**

## Ba họ tấn công (tiếp)
@phut: 1
@che-do: so

- Truy ngược gradient cần bốn thứ cùng lúc: biết kiến trúc và hàm mất mát, thấy gradient THÔ của một client, lô nhỏ, và không có nhiễu DP đáng kể
- Thay thế mô hình (model replacement) cần ba thứ: kẻ xấu được chọn trong vòng đó, mô hình đã gần hội tụ nên cập nhật lành gần triệt tiêu, và server không chặn chuẩn cập nhật

## Ba họ tấn công (tiếp)
@phut: 1
@che-do: so

- Adv đo ở CÙNG một ngưỡng cho cả hai lớp, và tập thành viên với tập không thành viên chỉ khác nhau ở yếu tố thành viên, không khác ở phân bố
- Cả ba con số đều là hàm của năng lực kẻ tấn công đã khai, nên đổi mô hình đe doạ là đổi kết quả, không phải đổi cách trình bày

## Ba họ tấn công · ghi chú
@phut: 1
@che-do: noi

Đặc tả của module này còn một dòng số nữa, là cỡ lô tối đa mà truy ngược gradient còn dựng lại được ảnh rõ. Dòng đó đang ở trạng thái chưa chắc trong bản thiết kế, nên nó **đã bị bỏ** khỏi module theo luật về số: thà thiếu một thẻ còn hơn dạy sai một con số. Nếu cần con số đó thì phải tra bài gốc và các bài theo sau, rồi mới thêm thẻ.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s003}} | lần | FedAvg lấy một trăm client mỗi vòng và dùng bước server eta
!so {{s004}} | vòng | Với mô hình đã gần hội tụ và không có chặn chuẩn

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Server lấy {{s013}} client mỗi vòng và dùng bước eta = {{s015}}. Hệ số nhân gamma của tấn công thay thế mô hình là bao nhiêu?

n = {{s013}}, eta = {{s014}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`n / eta`

Bằng {{s016}}, tức gấp bốn lần trường hợp n = {{s003}} với eta = {{s004}}. Hai cách làm tấn công khó hơn nằm trong cùng một phân số: tăng số client mỗi vòng, hoặc hạ bước server. Cả hai đều buộc kẻ xấu nộp cập nhật có chuẩn lớn hơn, nên cả hai đều làm chặn chuẩn ở server hiệu quả hơn. Nhưng đừng đọc đây là tin tốt một chiều:

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

thẻ mô phỏng cho thấy cùng lúc đó cửa hậu đã cài vào lại sống dai hơn.

## Một cửa hậu đã cài xong
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một cửa hậu đã cài xong, rồi kẻ xấu không được chọn nữa. Với mô hình co tuyến tính hệ số ({{s004}} − eta/n) mỗi vòng, n = {{s003}} và eta = {{s004}}, cần bao nhiêu vòng để hiệu lực cửa hậu phai xuống dưới 10%?

eta = {{s004}}, n = {{s003}}

## Một cửa hậu đã cài xong · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.log(0.1) / Math.log(1 - eta / n)`

Khoảng {{s017}} vòng, tức hơn hai trăm vòng huấn luyện lành mới xoá được tới mức một phần mười. Con số này chỉ để đọc BẬC ĐỘ LỚN, vì mô hình co tuyến tính là một mô hình quy ước, không phải phép đo. Điều đáng dùng là hệ quả thực nghiệm:

## Một cửa hậu đã cài xong · đáp (tiếp)
@phut: 1
@che-do: noi

một bài báo khai cửa hậu bị xoá sau vài vòng thì phải nói nó đo trên bao nhiêu vòng, vì đo trên {{s018}} vòng và đo trên {{s019}} vòng cho hai kết luận trái nhau với cùng một hệ.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hệ dùng secure aggregation nên server chỉ thấy tổng các cập nhật. Họ tấn công nào vẫn khả thi NGUYÊN VẸN?

- Cả hai đều bị chặn
- Cả hai đều không bị ảnh hưởng
- Truy ngược gradient ở mức một client
- Đầu độc và cài cửa hậu

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Đầu độc và cài cửa hậu**

Đầu độc và cửa hậu không cần ĐỌC gì của ai, chúng chỉ cần GHI một cập nhật vào tổng. Secure aggregation thu hẹp thứ server thấy, nên nó đánh đúng vào họ suy luận mức client và không làm gì cho họ đầu độc. Tệ hơn một chút: secure aggregation còn làm phòng vệ bền khó hơn, vì server không còn thấy từng cập nhật để so khoảng cách.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Server chặn chuẩn mọi cập nhật về tối đa {{s020}}. Với n = {{s003}} và eta = {{s004}}, phát biểu nào về tấn công thay thế mô hình là đúng?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Tấn công bị chặn hoàn toàn, vì nó cần chuẩn gấp {{s003}} lần
- Tấn công một phát bị chặn, nhưng kẻ xấu đổi sang nhiều vòng với gamma nhỏ, hoặc đổi sang khai sai số mẫu để tăng trọng số
- Chặn chuẩn không ảnh hưởng gì, vì kẻ xấu chỉ cần chuẩn hoá lại cập nhật
- Tấn công mạnh hơn, vì chặn chuẩn làm cập nhật lành nhỏ đi

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tấn công một phát bị chặn, nhưng kẻ xấu đổi sang nhiều vòng với gamma nhỏ, hoặc đổi sang khai sai số mẫu để tăng trọng số**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Chặn chuẩn đánh đúng vào dấu vết của gamma = {{s003}}, nên tấn công MỘT PHÁT không qua được. Nhưng kẻ tấn công thích nghi có hai đường rẽ: hạ gamma và cộng dồn qua nhiều vòng, hoặc đi trục không dùng chuẩn lớn, ví dụ khai số mẫu lớn để chiếm trọng số trong FedAvg có trọng số.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Phương án A sai vì nó giả định kẻ tấn công không thích nghi, tức giả định một mô hình đe doạ yếu hơn mô hình đã khai ở phần tấn công.

## Một bài báo khai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai: tấn công của chúng tôi giả định kẻ xấu biết phân bố dữ liệu toàn cục; phòng vệ của chúng tôi giả định kẻ xấu không biết ngưỡng chặn chuẩn của server. Vấn đề nghiêm trọng nhất ở đây là gì?

## Một bài báo khai (tiếp)
@phut: 0.5
@che-do: hoi

- Hai mục dùng hai mô hình đe doạ khác nhau, nên kết quả phòng vệ không nói gì về kẻ tấn công mà chính bài đã dựng
- Ngưỡng chặn chuẩn nên được học thay vì đặt cố định
- Phân bố dữ liệu toàn cục là giả thiết quá mạnh cho phần tấn công
- Thiếu thí nghiệm với nhiều mức ngưỡng chặn chuẩn

## Một bài báo khai · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hai mục dùng hai mô hình đe doạ khác nhau, nên kết quả phòng vệ không nói gì về kẻ tấn công mà chính bài đã dựng**

## Một bài báo khai · đáp (tiếp)
@phut: 1
@che-do: noi

Đây không phải lỗ hổng thí nghiệm mà là lỗ hổng logic, nên thêm thí nghiệm không sửa được. Kẻ tấn công biết được phân bố toàn cục thì không có lý do gì không biết một siêu tham số của server. Hai mục đang nói về hai hệ khác nhau, nên bảng kết quả phòng vệ không trả lời câu hỏi mà phần tấn công đặt ra.

## Một bài báo khai · đáp (tiếp)
@phut: 1
@che-do: noi

Cách sửa là một bảng năng lực duy nhất, cộng một thí nghiệm với kẻ tấn công thích nghi.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả mô hình đe doạ sau có một câu không đứng được. Bấm vào câu đó.

- Kẻ tấn công kiểm soát tối đa {{s021}} client và nộp cập nhật tuỳ ý.
- Server trung thực, thực hiện đúng FedAvg và công bố mô hình toàn cục mỗi vòng.
- Vì dữ liệu thô không rời khỏi client, dữ liệu huấn luyện của client được bảo vệ khỏi kẻ tấn công.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì dữ liệu thô không rời khỏi client, dữ liệu huấn luyện của client được bảo vệ khỏi kẻ tấn công.**

Hai câu đầu là mô tả mô hình đe doạ hợp lệ, và chúng chưa khai tuyên bố riêng tư nào. Câu thứ ba mới là lỗi: nó suy một tuyên bố về RIÊNG TƯ từ một tuyên bố về VẬN CHUYỂN.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Chính câu thứ hai đã nói mô hình toàn cục được công bố mỗi vòng, nên kẻ tấn công có đủ thứ để làm suy luận thành viên, và nếu thấy được cập nhật từng client thì còn làm được truy ngược gradient. Cách sửa: bỏ câu suy luận này, và thay bằng một tuyên bố có cặp (epsilon, delta) cùng đơn vị kề, hoặc thay bằng một câu khai thẳng rằng bài không đưa ra bảo đảm riêng tư nào.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phần thí nghiệm sau có một dòng làm kết luận về cửa hậu không kiểm được, trong khi mọi dòng khác đều hợp lệ. Bấm vào dòng đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Kẻ xấu kiểm soát {{s004}} trong {{s003}} client và cài cửa hậu bằng thay thế mô hình với gamma = {{s003}}.
- Sau khi cài, kẻ xấu rút và không dự vòng nào nữa.
- Chúng tôi đo tỉ lệ kích hoạt cửa hậu sau {{s018}} vòng lành tiếp theo và thấy nó còn {{s022}}, nên kết luận cửa hậu bền.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Chúng tôi đo tỉ lệ kích hoạt cửa hậu sau {{s018}} vòng lành tiếp theo và thấy nó còn {{s022}}, nên kết luận cửa hậu bền.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai dòng đầu là thiết kế thí nghiệm hợp lệ và khai đủ tham số. Dòng thứ ba là lỗi vì cửa sổ đo {{s018}} vòng quá ngắn so với thang thời gian của chính hệ: với n = {{s003}} và eta = {{s004}}, thang phai là khoảng {{s017}} vòng để xuống dưới {{s021}}, nên sau {{s018}} vòng con số còn cao là điều phải xảy ra bất kể cửa hậu bền hay không.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Phép đo này không phân biệt được hai giả thuyết, nên nó không chống được kết luận nào. Cách sửa: báo đường cong tỉ lệ kích hoạt theo vòng tới ít nhất vài trăm vòng, và khai luôn cả thang thời gian lý thuyết để người đọc biết cửa sổ đo đã đủ dài chưa.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Viết luật cập nhật của server: G_{t+1} = G_t + (eta/n)·tổng theo i của (L_i − G_t)
- Giả mô hình đã gần hội tụ, nên với mọi client lành thì L_i − G_t gần bằng {{s008}} và các số hạng đó gần triệt tiêu nhau
- Còn lại G_{t+1} gần bằng G_t + (eta/n)·(X − G_t), với X là thứ kẻ xấu nộp lên
- Đòi G_{t+1} = X_xau rồi giải theo X: X = (n/eta)·(X_xau − G_t) + G_t

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Đọc ra gamma = n/eta, và đọc ra dấu vết: chuẩn của cập nhật kẻ xấu lớn gấp gamma lần cập nhật lành

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Kẻ tấn công thấy gradient thô từng client · biết kiến trúc và hàm mất mát · chọn được client bị kiểm soát · dự được nhiều vòng liên tiếp. Cả ba họ tấn công đều khả thi, hệ số thay thế mô hình gamma = n/eta = {{s003}}, và cửa hậu phai sau khoảng {{s017}} vòng nếu kẻ xấu rút.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Thấy gradient thô của TỪNG client** tắt đi: Hệ có secure aggregation, nên server chỉ nhận được tổng các cập nhật, không nhận được cập nhật nào riêng lẻ.
- **Biết kiến trúc và hàm mất mát** tắt đi: Mô hình và hàm mất mát là bí mật của bên triển khai, client chỉ nhận một đặc tả giao diện.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Chọn được client bị kiểm soát, tức chắc chắn được dự vòng mục tiêu** tắt đi: Server chọn client ngẫu nhiên với tỉ lệ C mỗi vòng, và kẻ tấn công không ảnh hưởng được phép chọn.
- **Dự được nhiều vòng liên tiếp** tắt đi: Kẻ xấu chỉ dự đúng một vòng rồi bị loại, ví dụ do luân phiên bắt buộc hoặc do phát hiện sau một vòng.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Năng lực kẻ tấn công thành con số. Kéo số client mỗi vòng, bước server, số mẫu kẻ xấu KHAI, và số mẫu mỗi client lành. Hai cột đầu nói kẻ xấu phải nộp cập nhật lớn cỡ nào; hai cột sau nói nó có thể đạt cùng mục tiêu mà KHÔNG cần cập nhật lớn, chỉ bằng cách khai sai số mẫu.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.6` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III assumes an attacker who knows the global data distribution and can craft arbitrary updates, while Section V evaluates the defence against an attacker who does not know the server-side clipping threshold and does not adapt to it. These are different adversaries. Please evaluate the defence against the adversary defined in Section III, or weaken the attack model in Section III to match.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right that the two sections described two different adversaries, and we have resolved this by fixing one adversary rather than by adding a case. Table I of the revised manuscript is now a single capability table (knows architecture and loss: yes; observes per-client updates: no, secure aggregation is assumed; controls a fraction f/n of clients: yes; is selected in a chosen round: no, selection is random at rate C; knows all server-side hyperparameters including the clipping threshold:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

yes), and every experiment in Sections IV and V now refers to that table. Under this adversary, two of our previous conclusions do not survive and we have rewritten them. First, single-shot model replacement is blocked by norm clipping at tau = {{s023}}, as before. Second, and new, the adaptive attacker that lowers gamma to stay under tau and accumulates the backdoor over {{s024}} rounds still reaches {{s025}} activation, which our defence does not detect; Table VII reports this.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Third, we now also report the trust axis we cannot defend: because the server cannot verify the sample count a client declares, an attacker claiming {{s026}} samples against {{s027}} honest clients of {{s028}} samples each obtains half of the aggregation weight while submitting an update of entirely normal norm. No distance-based or norm-based defence sees this, and we state it as a limitation in Section VI rather than as a result.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: nói rằng kẻ tấn công thích nghi nằm ngoài phạm vi bài và dẫn vài bài cùng đánh giá với kẻ tấn công không thích nghi. Không trả lời được: phản bác không hỏi về tiền lệ, nó hỏi về tính nhất quán nội bộ của chính bài này.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: thêm một thí nghiệm với kẻ tấn công biết ngưỡng chặn chuẩn, nhưng vẫn giữ mọi kết luận cũ và chỉ coi kết quả mới là một ca bổ sung. Trả lời đúng yêu cầu bề mặt, chưa sửa chỗ hai mục nói về hai hệ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: hợp nhất thành một bảng năng lực kẻ tấn công duy nhất ở đầu phần đánh giá, chạy lại toàn bộ phần phòng vệ dưới đúng bộ năng lực đó, và sửa những kết luận nào không còn đứng.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table VI reports a membership inference accuracy of {{s005}} on a balanced member/non-member split and concludes that the system leaks membership. In deployment the prior probability of membership is far below one half, so balanced accuracy overstates the operational risk. Please report an advantage measure and the true positive rate at a low false positive rate.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree that balanced accuracy is the wrong summary and we have replaced it. Table VI now reports the advantage, Adv = TPR − FPR = {{s031}} on the balanced split, and, more importantly, the low-FPR regime: TPR = {{s032}} at FPR = 1e-2, TPR = {{s033}} at FPR = 1e-3, and TPR = {{s034}} at FPR = 1e-4, each with {{s035}} bootstrap intervals over {{s018}} seeds. We also translate this into the operational statement the reviewer is asking for:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

at FPR = 1e-3 on a population of 1e6 non-members, the attacker correctly identifies {{s036}} of members while producing about {{s028}} false identifications, so the attack is informative at the population level but weak as an accusation about any single individual. Finally, we put this next to our privacy accounting:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

at the record-level epsilon = {{s037}} we report in Section IV-C, the theoretical upper bound on the advantage is not tight enough to predict the measured {{s031}}, and we now say so explicitly rather than presenting the two numbers as mutually confirming.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: giữ accuracy {{s005}} và nói rằng tập cân bằng là quy ước phổ biến của các bài suy luận thành viên. Đúng về thực hành, không trả lời được: phản bác hỏi về khả chuyển sang vận hành, không hỏi về quy ước.
- Mức {{s001}}: thêm lợi thế Adv = TPR − FPR, tức {{s006}} trên tập cân bằng, nhưng vẫn chỉ báo ở một điểm làm việc nên vẫn chưa nói gì về vùng FPR thấp.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: báo Adv cộng TPR tại vài mức FPR thấp (ví dụ {{s029}}, {{s010}} và {{s030}}), và nói rõ các số đó đo trên phân bố nào.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.6` bấm thẻ.
