---
tieu-de: An ninh lớp vật lý: dùng được tới đâu
phu-de: Trụ 4 6G Sec · module 4.5
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 74
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: 6G SEC
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Dung lượng bí mật của tôi dựa trên việc biết kênh của kẻ nghe, và tôi biết nó bằng cách nào?

## Một công thức đúng
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Dung lượng bí mật là một định lý, và định lý đó đúng. Vấn đề không nằm ở toán. Vấn đề nằm ở **đầu vào**: công thức cần `γ_E`, tức tỉ số tín hiệu trên nhiễu tại kẻ nghe. Trong vận hành thật, kẻ nghe thụ động không phát gì, nên gần như không bao giờ biết `γ_E`.

## Một công thức đúng (tiếp)
@phut: 1
@che-do: noi

Hệ quả là một câu rất gọn mà người học phải nói được thành tiếng: **mọi bài báo báo C_s như một kết quả vận hành đang ngầm giả định điều không có**. Đó không phải lỗi tính toán, nên không cổng nào trong quy trình bắt được; nó chỉ lộ ra khi có người hỏi đầu vào đến từ đâu, và reviewer của IEEE hỏi đúng câu đó.

## Một công thức đúng (tiếp)
@phut: 1
@che-do: noi

Module này có hai việc. Một, tách rõ ba đại lượng: `C_s` tức thời (cần biết `γ_E`), xác suất mất bí mật `P_out` (cần biết **phân bố** của `γ_E`, không cần giá trị), và tỉ lệ thời gian `C_s` bằng {{s001}} (hệ quả của toán tử cắt). Hai, cho thấy bằng số rằng **giữ C_s trung bình không đổi mà làm P_out xấu đi hẳn** là việc làm được, nên báo trung bình là không đủ.

## Dung lượng bí mật, và đầu vào mà nó đòi
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Dung lượng bí mật, và đầu vào mà nó đòi · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`C_s = [log₂(1+γ_B) − log₂(1+γ_E)]⁺`, đơn vị bit mỗi ký hiệu. Nó là tốc độ mà người nhận hợp pháp giải được trong khi kẻ nghe không lấy được thông tin nào theo nghĩa lý thuyết thông tin.

## Dung lượng bí mật, và đầu vào mà nó đòi · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: công thức này đòi **hai** đầu vào, và hai đầu vào đó có địa vị hoàn toàn khác nhau. `γ_B` đo được, vì người nhận hợp pháp có phản hồi. `γ_E` **không đo được**, vì kẻ nghe thụ động không phát gì. Nên `C_s` là đại lượng của mô hình, và nó chỉ thành đại lượng vận hành khi anh nói được `γ_E` lấy từ đâu:

## Dung lượng bí mật, và đầu vào mà nó đòi · đáp (tiếp)
@phut: 1
@che-do: noi

từ một giới hạn hình học (kẻ nghe không vào gần hơn một bán kính), từ một ràng buộc phần cứng, hoặc từ một phân bố mà anh khai.

## Vì sao toán tử cắt về phần dương đổi cách báo số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Vì sao toán tử cắt về phần dương đổi cách báo số · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Nếu kẻ nghe gần hơn, tức `γ_E ≥ γ_B`, thì `C_s` bằng **{{s001}}**, không âm. Không có khái niệm tốc độ bí mật âm: hệ chỉ đơn giản không truyền được gì có bí mật.

## Vì sao toán tử cắt về phần dương đổi cách báo số (tiếp)
@phut: 1
@che-do: noi

Hệ quả về cách báo số, và đây là chỗ bị bắt: trung bình của `C_s` trên một vùng là trung bình của một biến có **khối lượng xác suất dồn tại {{s001}}**. Một hệ có `C_s` bằng {{s001}} trong {{s004}} thời gian và bằng {{s005}} bit trong {{s006}} thời gian cũng cho trung bình {{s007}} bit, giống một hệ luôn cho {{s007}} bit. Hai hệ đó khác nhau hoàn toàn về an ninh.

## Vì sao toán tử cắt về phần dương đổi cách báo số (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **mỗi con số trung bình của C_s phải đi kèm tỉ lệ thời gian nó bằng {{s001}}**, và nếu có tốc độ mục tiêu thì kèm cả `P_out` tại tốc độ đó. Thiếu hai con số đó thì trung bình không khai được, giống hệt cách precision không khai được khi thiếu tỉ lệ nền.

## Xác suất mất bí mật: cái gì được mua
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Xác suất mất bí mật: cái gì được mua · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`P_out = P(C_s` không đạt `R_s)`. Cái được mua: **không cần biết giá trị γ_E nữa**, nên đại lượng này sống qua đúng giả thiết nặng nhất của module.

Cái phải trả: phải khai **phân bố** của kênh kẻ nghe và **phân bố vị trí** của nó. Hai thứ đó không ai kiểm được từ bên ngoài, nên mọi tranh luận trong phản biện diễn ra ở đúng đây, chứ không ở phép tính.

## Xác suất mất bí mật: cái gì được mua · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: `P_out` là **hệ quả của giả thiết, không phải kết quả của phép đo**. Cách viết đứng được là nêu phân bố ngay trong câu kết luận, cộng một phép thử độ bền: con số đổi bao nhiêu khi đổi giả thiết phân bố, chẳng hạn khi cho trung bình `γ̄_E` tăng {{s008}} dB. Nếu kết luận đảo chiều trong khoảng đó thì kết luận đó là kết luận về giả thiết của anh.

## Dung lượng bí mật của kênh Gauss suy giảm
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`C_s = [ log₂(1 + γ_B) − log₂(1 + γ_E) ]⁺`

**Giả thiết nó đứng trên:**

## Dung lượng bí mật của kênh Gauss suy giảm (tiếp)
@phut: 1
@che-do: so

- biết γ_E, tức biết kênh của kẻ nghe; đây là giả thiết nặng nhất và cả module nói về nó
- kênh của kẻ nghe là bản suy giảm của kênh hợp pháp (kênh wiretap suy giảm), nên tốc độ bí mật đạt được là hiệu hai dung lượng
- độ dài khối vô hạn và mã đạt dung lượng; với khối hữu hạn thì tốc độ bí mật đạt được thấp hơn

## Dung lượng bí mật của kênh Gauss suy giảm (tiếp)
@phut: 1
@che-do: so

- đúng MỘT kẻ nghe, một ăng ten, không hợp tác với kẻ nghe khác
- nhiễu Gauss trắng cộng tính, công suất phát cố định, không có ăng ten nhiễu chủ động

## Dung lượng bí mật của kênh Gauss suy giảm · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Toán tử `[·]⁺` nghĩa là lấy phần dương: nếu `γ_E ≥ γ_B` thì `C_s` bằng {{s001}}, **không âm**. Vì vậy mọi con số trung bình của `C_s` là trung bình của một biến có khối lượng xác suất dồn ở {{s001}}, nên **phải khai kèm tỉ lệ thời gian nó bằng {{s001}}**. Thiếu con số đó thì một trung bình dương vẫn tương thích với việc hệ mất bí mật phần lớn thời gian.

## Xác suất mất bí mật, dùng khi không biết γ_E
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`P_out = P( C_s nhỏ hơn R_s ), với γ_E ~ phân bố khai trước, γ_B cho trước`

**Giả thiết nó đứng trên:**

## Xác suất mất bí mật, dùng khi không biết γ_E (tiếp)
@phut: 1
@che-do: so

- khai được PHÂN BỐ của kênh kẻ nghe, thường là phân bố mũ cho γ_E tức pha đinh Rayleigh, cộng một phân bố cho vị trí của kẻ nghe
- pha đinh tựa tĩnh theo khối: trong một khối thì kênh không đổi, giữa các khối thì độc lập
- R_s là tốc độ bí mật mục tiêu, do thiết kế chọn trước chứ không chọn sau khi thấy kết quả

## Xác suất mất bí mật, dùng khi không biết γ_E (tiếp)
@phut: 1
@che-do: so

- γ_B coi như biết và cố định, vì người nhận hợp pháp có phản hồi

## Xác suất mất bí mật, dùng khi không biết γ_E · ghi chú
@phut: 1
@che-do: noi

Với `γ_E` mũ trung bình `γ̄_E` và `γ_B` cố định, điều kiện mất bí mật là `γ_E` vượt ngưỡng `(1+γ_B)/2^R_s − {{s002}}`, nên `P_out = exp( −((1+γ_B)/2^R_s − {{s002}}) / γ̄_E )`. Chỗ phải thấy: **P_out là hệ quả của phân bố anh khai**, không phải của một phép đo. Đổi giả thiết phân bố là đổi con số, và không ai bên ngoài kiểm được giả thiết đó.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s001}} | bit mỗi ký hiệu | Kẻ nghe ở gần hơn
!so {{s009}} | bit mỗi ký hiệu | Người nhận hợp pháp ở {{s010}} dB

## Người nhận hợp pháp ở 15 dB
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Người nhận hợp pháp ở {{s011}} dB, kẻ nghe ở {{s005}} dB. Dung lượng bí mật bằng bao nhiêu bit mỗi ký hiệu?

gbdB = {{s011}}, gedB = {{s005}}

## Người nhận hợp pháp ở 15 dB · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.max(0, Math.log2(1+Math.pow(10,gbdB/10)) - Math.log2(1+Math.pow(10,gedB/10)))`

Khoảng {{s012}} bit mỗi ký hiệu. Để ý: cách biệt vẫn đúng {{s008}} dB như ca {{s010}} dB với {{s008}} dB, mà kết quả nhỏ hơn {{s013}} bit của ca đó. Cách biệt dB không ánh xạ thành số bit, vì số {{s002}} cộng thêm trong mỗi log đè nặng hơn khi tỉ số tín hiệu trên nhiễu thấp. Ai lấy hiệu dB chia cho {{s014}} sẽ ra {{s015}} bit cho cả hai ca, tức sai cả hai.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Người nhận hợp pháp cố định ở {{s010}} dB. Kẻ nghe có tỉ số tín hiệu trên nhiễu phân bố mũ với trung bình {{s008}} dB. Tốc độ bí mật mục tiêu là {{s003}} bit mỗi ký hiệu. Xác suất mất bí mật bằng bao nhiêu phần trăm?

gbdB = {{s010}}, rs = {{s003}}, gebardB = {{s008}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆Math.exp(-((1+Math.pow(10,gbdB/10))/Math.pow(2,rs) - 1)/Math.pow(10,gebardB/10))`

Khoảng {{s016}}, tức cỡ một phần mười khối tin không đạt mục tiêu bí mật, trong khi dung lượng bí mật tức thời ở cùng cặp {{s010}} dB với {{s008}} dB vẫn là {{s013}} bit, nghe như thừa sức cho mục tiêu {{s003}} bit. Hai con số không mâu thuẫn: một cái nói về MỘT thực hiện kênh, cái kia nói về cả phân bố.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Và chỉ cần đổi trung bình của phân bố lên {{s010}} dB là con số này lên khoảng {{s017}}, trong khi dung lượng tức thời đứng yên.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Tắt giả thiết biết kênh của kẻ nghe. Đại lượng nào còn khai được?

- C_s tức thời, chỉ cần thay γ_E bằng giá trị trung bình
- C_s trung bình, vì trung bình không cần biết giá trị tức thời
- P_out, với một phân bố khai trước cho kênh và vị trí của kẻ nghe
- Không còn đại lượng nào, nên an ninh lớp vật lý không dùng được

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**P_out, với một phân bố khai trước cho kênh và vị trí của kẻ nghe**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Thay γ_E bằng trung bình là sai, vì C_s là hàm lồi khúc của γ_E nên thay giá trị trung bình vào không cho trung bình của giá trị. C_s trung bình cũng cần phân bố chứ không miễn được. Phương án cuối nói quá: P_out vẫn khai được, nhưng nó là hệ quả của phân bố anh khai, nên câu kết luận phải nêu phân bố đó cùng một chỗ.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai hệ đều báo dung lượng bí mật trung bình {{s018}} bit mỗi ký hiệu. Dữ kiện nào phân biệt được chúng về mặt an ninh?

- Tỉ lệ thời gian C_s bằng {{s001}}, cộng P_out ở một R_s khai trước
- Băng thông kênh
- Sơ đồ điều chế và tốc độ mã
- Số ăng ten phát của trạm gốc

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tỉ lệ thời gian C_s bằng {{s001}}, cộng P_out ở một R_s khai trước**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Trung bình của một biến có khối lượng xác suất tại {{s001}} không xác định được phân bố: C_s bằng {{s001}} trong {{s004}} thời gian rồi {{s019}} bit trong {{s006}} thời gian cũng cho trung bình {{s018}} bit, giống hệ luôn cho {{s018}} bit. Ba phương án kia đổi giá trị của C_s nhưng không nói gì thêm khi trung bình đã cho; chỉ tỉ lệ thời gian bằng {{s001}} cùng P_out tách được hai hệ đó.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một câu biến một đại lượng của mô hình thành một tuyên bố vận hành không đứng được. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Với γ_B = {{s010}} dB và γ_E = {{s008}} dB, dung lượng bí mật của sơ đồ đề xuất là {{s013}} bit mỗi ký hiệu,
- nên hệ bảo đảm tốc độ bí mật {{s013}} bit mỗi ký hiệu trong triển khai thực tế của mục VI.
- Ở tốc độ mục tiêu {{s003}} bit mỗi ký hiệu, với γ_E phân bố mũ trung bình {{s008}} dB, xác suất mất bí mật là {{s020}}.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên hệ bảo đảm tốc độ bí mật {{s013}} bit mỗi ký hiệu trong triển khai thực tế của mục VI.**

Chữ bảo đảm và chữ thực tế đòi biết γ_E tại hiện trường, mà kẻ nghe thụ động thì không cho biết điều đó. Câu đầu hoàn toàn hợp lệ: nó nêu rõ cả hai đầu vào và là phát biểu trong mô hình. Câu thứ ba cũng hợp lệ, vì nó mới là cách khai đúng. Cách sửa cho câu này:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

đổi thành tốc độ bí mật đạt được VỚI ĐIỀU KIỆN γ_E không vượt {{s008}} dB, và nói γ_E đó lấy từ đâu, chẳng hạn từ ràng buộc hình học rằng kẻ nghe không vào trong bán kính đã nêu; hoặc bỏ hẳn câu này và báo P_out.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau mô tả cách tính một con số trung bình. Một câu làm con số đó không khai được. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi lấy mẫu {{s008}} nghìn vị trí kẻ nghe đều trong vùng phục vụ, tính C_s cho từng vị trí,
- bỏ các vị trí cho C_s bằng {{s001}} vì ở đó không có truyền bí mật, rồi lấy trung bình trên các vị trí còn lại và báo {{s021}} bit mỗi ký hiệu.
- Phân bố vị trí và mô hình suy giảm dùng cho việc lấy mẫu nêu ở mục V-A.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**bỏ các vị trí cho C_s bằng {{s001}} vì ở đó không có truyền bí mật, rồi lấy trung bình trên các vị trí còn lại và báo {{s021}} bit mỗi ký hiệu.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Bỏ đúng các mẫu bằng {{s001}} là chọn tập theo kết quả, nên con số báo ra là trung bình CÓ ĐIỀU KIỆN trên tập mà hệ hoạt động được, trong khi câu văn trình bày nó như trung bình trên vùng phục vụ. Đây là chỗ toán tử lấy phần dương bị dùng ngược: những mẫu bằng {{s001}} không phải dữ liệu thiếu, chúng là những lần hệ mất bí mật, tức đúng phần quan trọng nhất.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Câu đầu và câu cuối đều hợp lệ. Cách sửa: giữ cả mẫu bằng {{s001}} trong trung bình, VÀ báo riêng tỉ lệ mẫu bằng {{s001}}; nếu muốn giữ con số có điều kiện thì phải gọi đúng tên nó và in kèm tỉ lệ thời gian hệ nằm ngoài điều kiện đó.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Dung lượng kênh hợp pháp: C_B = log₂(1 + γ_B)
- Dung lượng kênh của kẻ nghe: C_E = log₂(1 + γ_E)
- Kênh wiretap suy giảm: tốc độ bí mật đạt được bằng hiệu hai dung lượng, R_s = C_B − C_E
- Nếu C_E không nhỏ hơn C_B thì không tồn tại tốc độ bí mật dương, nên tốc độ đạt được bằng {{s001}}
- Gộp hai nhánh bằng toán tử lấy phần dương: C_s = [log₂(1+γ_B) − log₂(1+γ_E)]⁺

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Để TÍNH được con số này cần giá trị γ_E, tức biết kênh của kẻ nghe; không có nó thì phải chuyển sang P_out với một phân bố khai trước

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: C_s = {{s013}} bit mỗi ký hiệu tại γ_B = {{s010}} dB và γ_E = {{s008}} dB · P_out = {{s020}} ở R_s = {{s003}} bit với γ̄_E = {{s008}} dB · tỉ lệ thời gian C_s bằng {{s001}} là {{s022}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biết kênh của kẻ nghe, tức biết γ_E** tắt đi: Kẻ nghe thụ động, không phát gì, nên bên phát không có cách nào lấy được γ_E.
- **Độ dài khối vô hạn và mã đạt dung lượng** tắt đi: Khối hữu hạn, cỡ vài trăm tới vài nghìn ký hiệu, như mọi hệ thật.
- **Đúng một kẻ nghe, một ăng ten, không hợp tác** tắt đi: Nhiều kẻ nghe hợp tác, hoặc một kẻ nghe nhiều ăng ten gộp tín hiệu.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biết phân bố kênh và phân bố vị trí của kẻ nghe** tắt đi: Không có cơ sở nào để chọn phân bố: không biết kẻ nghe ở đâu, không biết môi trường của nó.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ba đại lượng của cùng một hệ, cạnh nhau: dung lượng bí mật tức thời, xác suất mất bí mật, và tỉ lệ thời gian dung lượng bí mật bằng {{s001}}. Hai thanh đầu là kênh thật, thanh thứ ba là ĐỘ BẤT ĐỊNH của anh về kẻ nghe.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.5` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Equation ({{s023}}) and Table III report the secrecy capacity of the proposed scheme, and Section VI presents it as a guaranteed operating rate. The secrecy capacity requires the instantaneous eavesdropper SNR. Since the eavesdropper is passive in your own threat model (Section II), please state how this quantity is obtained in the deployment, or restate the result in terms that do not require it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right that the eavesdropper is passive, so the instantaneous eavesdropper SNR is not observable in the deployment. We have restructured the results. Equation ({{s023}}) is now presented as a model level quantity for a given channel realisation, and the operating claim is carried by the secrecy outage probability instead. Section VI-A states the assumed statistics explicitly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

exponential eavesdropper SNR with mean {{s008}} dB and uniform eavesdropper position outside a {{s024}} m exclusion radius that follows from the physical security perimeter of the site described in Section II. Table III now has three columns rather than one: secrecy capacity at the stated operating point, the fraction of realisations with zero secrecy capacity, which is {{s025}} percent under these statistics, and the secrecy outage probability at the design target of {{s003}} bits per symbol, which is {{s026}} percent.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Figure {{s027}} adds the robustness test the reviewer implies: raising the assumed mean eavesdropper SNR by {{s008}} dB moves the outage probability from {{s026}} percent to {{s028}} percent and the zero capacity fraction from {{s025}} percent to {{s029}} percent, while the instantaneous secrecy capacity at the stated point does not move at all. We therefore no longer claim a guaranteed rate, and we state that our conclusion holds for the declared statistics and not beyond them.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng dung lượng bí mật là thước đo chuẩn trong tài liệu an ninh lớp vật lý. Đúng, nhưng không chạm vào phản bác, vì phản bác nói về đầu vào chứ không về thước đo.
- Mức {{s003}}: thay γ_E bằng một giá trị trung bình hoặc một giá trị xấu nhất chọn tuỳ ý, mà không nêu cơ sở của giá trị đó. Đây vẫn là giả định ẩn, chỉ chuyển chỗ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: chuyển kết quả chính sang xác suất mất bí mật, khai rõ phân bố kênh và phân bố vị trí của kẻ nghe, và nêu tốc độ bí mật mục tiêu trước khi báo số.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table V reports an average secrecy capacity of {{s030}} bits per symbol over the service area, but Section V-B states that positions with zero secrecy capacity were excluded from the average. Please report the average over the full sampling region and the fraction of positions with zero secrecy capacity, and explain which of the two numbers supports the claim in the abstract.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have corrected the reporting. Table V now gives the average over the full sampling region, the fraction of sampled positions with zero secrecy capacity, and the secrecy outage probability at the design target.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The previously reported {{s030}} bits per symbol was a conditional average over positions where the scheme achieves a positive secrecy rate, and we now label it as such and place it next to the {{s031}} percent of positions where the secrecy capacity is zero, so that the two numbers can only be read together.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The abstract has been rewritten to carry the outage probability at the design target rather than any average, because the average of a quantity with an atom at zero does not determine the security level: a system that is secure {{s032}} percent of the time at {{s033}} bits per symbol and insecure otherwise has the same average as a system that always delivers {{s034}} bits per symbol, and these are not the same system.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: trả lời rằng các vị trí có dung lượng bí mật bằng {{s001}} không mang thông tin nên loại ra là hợp lý. Đây chính là điều phản bác bác bỏ: những vị trí đó là các lần hệ mất bí mật.
- Mức {{s003}}: báo lại trung bình trên toàn vùng nhưng không báo tỉ lệ mẫu bằng {{s001}}, nên người đọc vẫn không phân biệt được một hệ ổn định với một hệ hỏng một phần thời gian.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: báo trung bình trên toàn vùng, báo tỉ lệ mẫu bằng {{s001}}, và sửa câu trong abstract cho khớp đúng con số nào đang đỡ nó.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.5` bấm thẻ.
