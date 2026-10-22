---
tieu-de: Lẩn tránh: không gian đặc trưng so với không gian vấn đề
phu-de: Trụ 1 NID · module 1.6
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 82.5
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

Nhiễu đối kháng tôi sinh ra trong không gian đặc trưng có dựng lại được thành gói tin gửi lên dây không, và nếu không thì bài của tôi đang tuyên bố cái gì?

## Lẩn tránh: không gian đặc trưng so với không gian vấn đề
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Bài toán quen thuộc là `min ||δ||` sao cho `f(x+δ) ≠ y`. Nghiệm của nó là một **vector đặc trưng**. Nhưng kẻ tấn công không gửi vector đặc trưng lên dây, nó gửi gói tin. Giữa hai thứ đó có một bộ trích đặc trưng `φ`, và `φ` không khả nghịch.

## Lẩn tránh: không gian đặc trưng so với không gian (tiếp)
@phut: 1
@che-do: noi

Hệ quả phải nói được trong một câu: nghiệm trong không gian đặc trưng là **chặn dưới** của chi phí tấn công thật, không phải một tấn công. Nên một bài báo đo độ bền bằng nhiễu `L2` trong không gian đặc trưng đang báo một chặn dưới của chi phí và gọi nó là độ bền. Hai chiều ngược nhau.

## Lẩn tránh: không gian đặc trưng so với không gian (tiếp)
@phut: 1
@che-do: noi

Module này có một việc duy nhất và nó là việc khó: nhớ được bốn ràng buộc không gian vấn đề, rời nhau, và nói được cái nào làm con số XẤU đi, cái nào làm câu nói **mất nghĩa**. Chỉ có một trong bốn cái thuộc loại thứ hai, và đó là cái mọi người hay bỏ qua.

## Bốn ràng buộc không gian vấn đề
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Bốn ràng buộc không gian vấn đề · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Phép biến đổi `T` mà kẻ tấn công thật dùng phải thoả cả bốn, cùng lúc: **Có sẵn:** `T` thuộc tập phép biến đổi mà kẻ tấn công thực sự làm được trên đối tượng thật. **Giữ nguyên ngữ nghĩa độc hại:** `z = T(z0)` vẫn thực hiện đúng hành vi tấn công ban đầu. **Chịu được tiền xử lý:** nhiễu còn sống sót qua chuẩn hoá, gộp luồng, cắt gói, phân mảnh lại.

## Bốn ràng buộc không gian vấn đề · đáp (tiếp)
@phut: 1
@che-do: noi

**Trông hợp lý:** đối tượng sinh ra không bị một bộ kiểm tra tính hợp lý riêng loại ngay. **Điểm phải nhớ:** ba cái {{s002}}, {{s003}}, {{s004}} làm chi phí tấn công TĂNG, tức con số đổi. Cái thứ {{s001}} thì khác loại: nếu ngữ nghĩa độc hại không còn thì mẫu sinh ra không còn là tấn công, nên câu *mô hình bị lừa* không còn đối tượng để nói về.

## Bốn ràng buộc không gian vấn đề · đáp (tiếp)
@phut: 1
@che-do: noi

Đó là lý do cái thứ {{s001}} là ràng buộc duy nhất không thương lượng được bằng cách chịu chi phí cao hơn.

## Vì sao chặn dưới chứ không phải chặn trên
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Vì sao chặn dưới chứ không phải chặn trên · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Gọi `Δ_f` là tập nhiễu khả thi trong không gian đặc trưng, và `Δ_p` là tập ảnh qua `φ` của mọi phép biến đổi khả thi trong không gian vấn đề. Vì mọi tấn công thật phải đi qua `φ`, ta có `Δ_p ⊆ Δ_f`.

Lấy cực tiểu trên một tập con thì không nhỏ hơn cực tiểu trên tập lớn, nên

`min{ ||δ|| : δ ∈ Δ_f } ≤ min{ ||δ|| : δ ∈ Δ_p }`

## Vì sao chặn dưới chứ không phải chặn trên · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** bất đẳng thức chỉ chạy một chiều. Chi phí trong không gian đặc trưng nhỏ hơn hoặc bằng chi phí thật. Nên nếu nó LỚN, anh kết luận được là tấn công đắt. Nếu nó NHỎ, anh không kết luận được gì về tấn công thật. Và phần lớn bài báo đo được một số nhỏ rồi kết luận mô hình yếu, tức dùng bất đẳng thức theo chiều nó không chạy.

## Chuẩn hoá đặc trưng không phải phòng vệ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Chuẩn hoá đặc trưng không phải phòng vệ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Chuẩn hoá từng biến, dù là min-max hay chuẩn hoá theo trung bình và độ lệch, là một phép biến đổi đơn điệu khả nghịch trên từng toạ độ. Nó không bỏ bớt phần tử nào khỏi tập phép biến đổi khả thi, nên **tập tấn công khả thi không đổi**.

Nó chỉ đổi cách đo khoảng cách. Một nhiễu nhìn nhỏ trong thang đã chuẩn hoá có thể lớn trong đơn vị gốc, và ngược lại.

## Chuẩn hoá đặc trưng không phải phòng vệ · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** khi phản biện hỏi về độ bền, câu trả lời *chúng tôi chuẩn hoá đầu vào* không trả lời gì cả. Nó còn tệ hơn im lặng, vì nó cho thấy người trả lời đang nhầm giữa thang đo với tập khả thi. Thứ đổi được tập khả thi là ràng buộc trên đối tượng thật, ví dụ không được bỏ bớt trường bắt buộc của giao thức, không được giảm số byte đã gửi.

## Ba bài toán, và chỗ chúng khác nhau
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`không gian đặc trưng: min ||δ|| sao cho f(x+δ) ≠ y · không gian vấn đề: min ||φ(T(z0)) − φ(z0)|| sao cho f(φ(T(z0))) ≠ y, T ∈ 𝒯 · quan hệ: min trên Δ_f ≤ min trên Δ_p`

**Giả thiết nó đứng trên:**

## Ba bài toán, và chỗ chúng khác nhau (tiếp)
@phut: 1
@che-do: so

- 𝒯 là tập phép biến đổi mà kẻ tấn công thật làm được trên đối tượng thật, và nó phải được liệt kê rõ trong bài chứ không nói chung là các phép biến đổi khả thi
- T giữ nguyên ngữ nghĩa độc hại của z0; nếu không thì mẫu sinh ra không còn là tấn công và bài toán không còn đối tượng

## Ba bài toán, và chỗ chúng khác nhau (tiếp)
@phut: 1
@che-do: so

- φ cố định và biết được; nếu bộ trích đặc trưng của bên phòng vệ bí mật thì kẻ tấn công ở chế độ khác và bài toán phải viết lại
- Nhiễu sống sót qua tiền xử lý của bên phòng vệ, tức φ áp lên đối tượng SAU tiền xử lý
- Đối tượng sinh ra qua được một bộ kiểm tra tính hợp lý riêng, nếu bên phòng vệ có bộ đó

## Ba bài toán, và chỗ chúng khác nhau · ghi chú
@phut: 1
@che-do: noi

Hai chỗ hay bị trộn. Thứ nhất, `Δ_p ⊆ Δ_f` nên quan hệ giữa hai cực tiểu chỉ chạy MỘT chiều: chi phí đặc trưng là chặn dưới.

## Ba bài toán, và chỗ chúng khác nhau · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

Thứ hai, trong không gian vấn đề thì **bản thân chuẩn `||·||` cũng không còn là đại lượng cần tối thiểu hoá**; cái cần tối thiểu hoá là chi phí thật của kẻ tấn công, ví dụ số gói phải thêm hoặc số giây phải chờ, và chuẩn trong không gian đặc trưng chỉ là một đại diện cho nó.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s004}} | ràng buộc | Có mấy ràng buộc không gian vấn đề mà một phép biến
!so {{s005}} | đặc trưng | CICFlowMeter, bộ trích đặc trưng dùng cho CIC-IDS2017, sinh bao nhiêu đặc

## Trong 80 đặc trưng CICFlowMeter
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong {{s005}} đặc trưng CICFlowMeter, kẻ tấn công chỉ chạm độc lập được {{s003}} cái, và tiền xử lý của bên phòng vệ giữ lại {{s007}} biên độ nhiễu. Chi phí tấn công thật gấp bao nhiêu lần nhiễu nhỏ nhất đo trong không gian đặc trưng?

m = {{s003}}, d = {{s005}}, s = {{s006}}

## Trong 80 đặc trưng CICFlowMeter · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`1/(Math.sqrt(m/d)⋆s)`

## Trong 80 đặc trưng CICFlowMeter · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s008}} lần, tức gần một bậc độ lớn chứ chưa tới một bậc. Hai chuyện phải đọc ra. Thứ nhất, con số epsilon mà bài báo báo ở trục hoành của hình độ bền phải nhân với khoảng {{s009}} mới là chi phí mà kẻ tấn công thật trả, nên một mô hình trông vỡ ở epsilon = {{s010}} thật ra vỡ ở chi phí khoảng {{s011}} trong cùng đơn vị. Thứ hai, ràng buộc toạ độ góp hệ số lớn hơn hẳn:

## Trong 80 đặc trưng CICFlowMeter · đáp (tiếp)
@phut: 1
@che-do: noi

căn của {{s003}} chia {{s005}} cho hệ số khoảng {{s012}}, còn tiền xử lý chỉ cho {{s013}}. Nên nếu phải khai một ràng buộc thì khai cái về toạ độ sửa được trước.

## Mô hình tuyến tính w = (3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình tuyến tính w = ({{s003}}, {{s004}}) và b = {{s015}}, điểm x có f(x) = {{s014}}. Nhiễu L2 nhỏ nhất trong không gian đặc trưng để đổi dấu f bằng bao nhiêu?

fx = {{s014}}, w1 = {{s003}}, w2 = {{s004}}

## Mô hình tuyến tính w = (3 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.abs(fx)/Math.sqrt(w1⋆w1 + w2⋆w2)`

Đúng bằng {{s001}}, vì ||w|| = {{s016}} và {{s014}} chia {{s016}} bằng {{s001}}. Đây là khoảng cách từ điểm tới siêu phẳng, không hơn. Nhớ nó là một chặn DƯỚI của chi phí thật: nếu kẻ tấn công chỉ sửa được toạ độ thứ nhất thì nhiễu nhỏ nhất là {{s014}} chia {{s003}}, tức khoảng {{s017}}, lớn hơn {{s001}}; nếu chỉ sửa được toạ độ thứ hai thì là {{s014}} chia {{s004}}, tức {{s018}}, cũng lớn hơn {{s001}}.

## Mô hình tuyến tính w = (3 · đáp (tiếp)
@phut: 1
@che-do: noi

Con số {{s001}} chỉ đạt được khi sửa được cả hai toạ độ theo đúng tỉ lệ {{s003}} trên {{s004}}.

## Một bài báo đo được
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo đo được: dưới nhiễu L2 với epsilon bằng {{s019}} trong không gian đặc trưng, độ chính xác tụt từ {{s020}} về {{s021}}. Kết luận nào rút ra được một cách hợp lệ?

## Một bài báo đo được (tiếp)
@phut: 0.5
@che-do: hoi

- Mô hình không bền với tấn công thực tế
- Chi phí tấn công thật nhỏ hơn hoặc bằng {{s019}} trong cùng đơn vị
- Có một hướng trong không gian đặc trưng, dài {{s019}}, làm mô hình đổi quyết định; chưa biết hướng đó có dựng lại được thành đối tượng thật hay không
- Bộ trích đặc trưng rò rỉ nhãn

## Một bài báo đo được · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Có một hướng trong không gian đặc trưng, dài {{s019}}, làm mô hình đổi quyết định; chưa biết hướng đó có dựng lại được thành đối tượng thật hay không**

## Một bài báo đo được · đáp (tiếp)
@phut: 1
@che-do: noi

Phép đo đó là một phát biểu về hình học của mô hình trong không gian đặc trưng, không hơn. Đáp án thứ nhất là dùng bất đẳng thức theo chiều nó không chạy. Đáp án thứ hai đảo ngược dấu: chi phí đặc trưng là chặn DƯỚI của chi phí thật, nên chi phí thật lớn hơn hoặc bằng, không nhỏ hơn hoặc bằng. Đáp án thứ tư là chuyện của module {{s022}} và không liên quan tới phép đo này.

## Trong bốn ràng buộc không gian vấn đề
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong bốn ràng buộc không gian vấn đề, cái nào mà vi phạm nó làm tỉ lệ tấn công thành công KHÔNG CÒN ĐỊNH NGHĨA ĐƯỢC, chứ không chỉ làm nó đổi giá trị?

- Chịu được tiền xử lý
- Trông hợp lý
- Có sẵn phép biến đổi
- Giữ nguyên ngữ nghĩa độc hại

## Trong bốn ràng buộc không gian vấn đề · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Giữ nguyên ngữ nghĩa độc hại**

Ba ràng buộc còn lại chỉ làm tập nhiễu khả thi nhỏ lại, nên chi phí tăng và tỉ lệ thành công giảm, cả hai vẫn là số. Khi ngữ nghĩa độc hại mất thì mẫu sinh ra không phải tấn công, nên tử số của tỉ lệ thành công đang đếm những thứ không thuộc mẫu số.

## Trong bốn ràng buộc không gian vấn đề · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là chỗ phân biệt số xấu đi với không còn nói được gì, và là lý do mọi bài tấn công phải báo tỉ lệ mẫu bị loại ở bước kiểm ngữ nghĩa.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phản biện hỏi mô hình của anh có bền với lẩn tránh hay không. Câu trả lời nào KHÔNG trả lời gì cả, dù nghe như đang trả lời?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi chuẩn hoá mọi đặc trưng về đoạn [{{s010}}] trước khi đưa vào mô hình
- Chúng tôi liệt kê tập phép biến đổi mà kẻ tấn công làm được và đo lại độ bền chỉ trên không gian con tương ứng
- Chúng tôi dựng lại nhiễu thành gói tin, phát lại, và báo tỉ lệ mẫu bị loại ở bước kiểm ngữ nghĩa

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi tấn công ở đầu vào của đường ống xử lý chứ không ở vector đặc trưng đã trích sẵn

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chúng tôi chuẩn hoá mọi đặc trưng về đoạn [{{s010}}] trước khi đưa vào mô hình**

Chuẩn hoá là phép biến đổi đơn điệu khả nghịch trên từng toạ độ, nên tập tấn công khả thi không đổi; nó chỉ đổi thang đo của chuẩn. Ba đáp án kia mỗi cái gỡ đúng một ràng buộc không gian vấn đề: ràng buộc có sẵn, ràng buộc ngữ nghĩa, và ràng buộc tiền xử lý.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả tấn công sau có một chỗ làm toàn bộ con số độ bền mất giá trị. Bấm vào chỗ đó.

- Chúng tôi lấy các vector đặc trưng {{s005}} chiều đã trích sẵn trong bản phát hành của dataset,
- chạy PGD với epsilon bằng {{s010}} theo chuẩn L2 trên toàn bộ {{s005}} chiều,
- và báo độ chính xác tụt từ {{s023}} về {{s024}}.
- Chúng tôi kết luận rằng mô hình cần huấn luyện đối kháng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**chạy PGD với epsilon bằng {{s010}} theo chuẩn L2 trên toàn bộ {{s005}} chiều,**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Tấn công toàn bộ {{s005}} chiều coi mọi đặc trưng là sửa được độc lập, trong khi phần lớn chúng là đặc trưng dẫn xuất: thời lượng luồng, số byte trung bình mỗi gói, độ lệch chuẩn khoảng cách gói. Kẻ tấn công không đặt được giá trị cho từng cái một cách độc lập. Hậu quả đúng tên: con số sinh ra là chặn dưới của chi phí thật, chứ không phải độ bền. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

liệt kê tập phép biến đổi khả thi, chiếu bài toán xuống không gian con mà chúng chạm tới được, và đo lại ở đó. Câu đầu cũng có vấn đề nhỏ hơn, là ngầm đặt tỉ lệ nhiễu sống sót qua tiền xử lý bằng {{s002}}, nhưng nó chỉ làm sai hệ số còn câu này làm sai cả loại kết luận.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn trả lời phản biện sau có một câu không đứng được. Bấm vào câu đó.

- Chúng tôi đồng ý rằng nhiễu trong không gian đặc trưng không phải tấn công, nên đã thêm bước dựng lại.
- Bước dựng lại sinh gói tin thật từ vector nhiễu bằng cách giải bài toán ngược của bộ trích đặc trưng.
- Vì chuẩn hoá đặc trưng làm nhiễu nhỏ đi, mô hình của chúng tôi vốn đã có một lớp phòng vệ sẵn.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Bảng mới báo tỉ lệ mẫu bị loại ở bước kiểm ngữ nghĩa và tỉ lệ thành công tính trên phần còn lại.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì chuẩn hoá đặc trưng làm nhiễu nhỏ đi, mô hình của chúng tôi vốn đã có một lớp phòng vệ sẵn.**

Chuẩn hoá từng biến là phép biến đổi đơn điệu khả nghịch trên từng toạ độ, nên nó không loại bỏ phần tử nào khỏi tập phép biến đổi khả thi. Tập tấn công khả thi KHÔNG ĐỔI; chỉ con số đọc được của chuẩn đổi, vì đổi thang đo. Đây là nhầm thang đo với tập khả thi.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Câu thứ hai cũng đáng nghi vì φ nói chung không khả nghịch, nhưng nó còn là một mô tả kỹ thuật kiểm được; câu này thì là một kết luận sai về bản chất. Cách sửa: bỏ câu này, và thay bằng khai những ràng buộc miền thật sự loại được nhiễu, ví dụ kiểm số gói không âm và kiểm tổng số byte không nhỏ hơn phần tiêu đề.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bảng kết quả tấn công sau có một dòng làm con số ở dòng cuối không đọc được. Bấm vào dòng đó.

- Tập phép biến đổi khả thi: thêm gói đệm, trễ gói, chia nhỏ payload ({{s003}} phép)
- Số mẫu sinh ra: {{s025}}
- Số mẫu qua được bộ kiểm hợp lệ của giao thức: {{s026}}
- Số mẫu được xác nhận còn hành vi độc hại trong sandbox: không khai
- Tỉ lệ tấn công thành công báo trong bài: {{s027}}

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Số mẫu được xác nhận còn hành vi độc hại trong sandbox: không khai**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Dòng cuối chia cho {{s025}} hoặc cho {{s026}}, nhưng cả hai mẫu số đó đều chứa những mẫu có thể đã mất ngữ nghĩa độc hại. Thiếu dòng này thì tỉ lệ tấn công thành công là tỉ lệ của một tập chưa biết là tấn công, tức con số không đọc được chứ không phải kém chính xác. Chú ý ba dòng trên đều hợp lệ và đều cần: chúng gỡ ràng buộc có sẵn và ràng buộc trông hợp lý. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

chạy lại từng mẫu sinh ra trong sandbox, báo số mẫu còn hành vi, và tính tỉ lệ thành công trên đúng con số đó.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Với mô hình tuyến tính f(x) = w·x + b, nhiễu L2 nhỏ nhất làm đổi dấu f là |f(x)| chia ||w||, đạt được khi δ cùng hướng với w
- Nếu chỉ các toạ độ trong tập M sửa được, thì δ bị buộc nằm trong không gian con sinh bởi M, và nhiễu nhỏ nhất thành |f(x)| chia ||w_M||

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Nếu các thành phần của w có độ lớn tương đương nhau thì ||w_M|| chia ||w|| xấp xỉ căn của phi, với phi = |M| chia d là tỉ lệ toạ độ sửa được
- Nếu chỉ một phần s của nhiễu sống sót qua tiền xử lý thì phải tiêm vào gấp {{s002}} chia s lần để còn lại đúng lượng cần

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Ghép lại: chi phí trong không gian vấn đề xấp xỉ |f(x)| chia ||w|| rồi chia tiếp cho căn của phi nhân s, nên tỉ số chi phí là {{s002}} chia (căn phi nhân s), luôn lớn hơn hoặc bằng {{s002}}

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: nhiễu nhỏ nhất trong không gian đặc trưng {{s028}} · chi phí thật {{s029}} · tỉ số {{s029}} · chi phí nếu chỉ ràng buộc toạ độ {{s029}} · {{s030}} trên {{s005}} đặc trưng sửa được · mẫu sinh ra vẫn là tấn công

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Phép biến đổi có sẵn, tức mọi toạ độ đặc trưng đều sửa được độc lập** tắt đi: Phần lớn toạ độ là đặc trưng dẫn xuất: thời lượng luồng, số byte trung bình mỗi gói, độ lệch chuẩn khoảng cách gói. Sửa một cái là kéo theo nhiều cái khác, nên chỉ một tập con nhỏ chạm tới được một cách độc lập.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Giữ nguyên ngữ nghĩa độc hại** tắt đi: Phép biến đổi tìm ra làm đổi hành vi: thêm byte đệm vào chỗ làm payload không chạy nữa, hoặc giảm số lần thử tới mức không còn là dò quét.
- **Chịu được tiền xử lý** tắt đi: Bên phòng vệ gộp lại luồng, cắt đuôi, chuẩn hoá về cửa sổ cố định, hoặc lắp lại phân mảnh. Chỉ một phần s của biên độ nhiễu còn sống tới chỗ trích đặc trưng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Trông hợp lý** tắt đi: Bên phòng vệ có một bộ kiểm tra riêng, không phải mô hình: kiểm tính hợp lệ của trường giao thức, kiểm mối quan hệ giữa các đặc trưng, kiểm biên vật lý như số gói không âm.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Mô hình tuyến tính, nhiễu L2. Kéo tỉ lệ toạ độ đặc trưng mà phép biến đổi thật chạm tới được, và tỉ lệ nhiễu sống sót qua tiền xử lý. Xem chi phí tấn công thật tách khỏi con số đo trong không gian đặc trưng.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.6` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section VI measures robustness by applying L2-bounded PGD directly to the 80-dimensional feature vectors shipped with the dataset. These features are derived quantities, so an attacker cannot set them independently, and the perturbation is never mapped back to packets. The reported robustness therefore does not characterise an attacker. Please either construct problem-space attacks or restate the claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree and have restructured Section VI. First, we now state the threat model as an explicit transformation set: three operations the attacker can perform on the wire, namely injecting padding packets, delaying packets, and splitting payloads. Second, the attack has been moved to the input of the pipeline: we generate packet traces, replay them through the same CICFlowMeter configuration used to build the training data, and optimise over the transformation parameters rather than over the {{s005}} feature coordinates.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Third, every generated sample is replayed in a sandbox and we report the fraction that no longer exhibits the original malicious behaviour; the attack success rate is computed only over the samples that survive that check, and both the numerator and the denominator are stated.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Fourth, we keep the original feature-space figure but relabel it as a lower bound on attack cost rather than a robustness measurement, and we report the ratio between the problem-space cost and that lower bound so the reader can see how loose the bound is. Finally we removed the word robust from the abstract and the conclusion, replacing it with a conditional statement naming the transformation set, since robustness without a threat model is not a measurable property.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also note explicitly that normalising the features does not change the feasible transformation set, only the scale in which the norm is read, so it is not part of our defence.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: lập luận rằng tấn công trong không gian đặc trưng là chuẩn mực trong lĩnh vực và cho một đánh giá trường hợp xấu nhất. Sai về chiều: nó cho một chặn DƯỚI của chi phí tấn công, tức một đánh giá lạc quan về sức mạnh phòng vệ, không phải trường hợp xấu nhất.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: giữ nguyên thí nghiệm và thêm một câu rằng khả thi trong không gian vấn đề là hướng nghiên cứu tương lai, trong khi tóm tắt vẫn dùng chữ robust. Mặt tiền vẫn hứa cái mà thân bài đã rút lại.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: liệt kê tập phép biến đổi khả thi một cách tường minh, chiếu bài toán tối ưu xuống không gian con mà chúng chạm tới được, đo lại độ bền ở đó, và đổi mọi câu kết luận từ robust thành một phát biểu có điều kiện kèm tập đe doạ.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

You report an attack success rate of {{s031}} percent. Table IX lists how many generated samples pass the protocol validity check, but not how many still perform the original malicious action. Without that number the denominator of the success rate is a set of objects that are not known to be attacks. Please clarify.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Table IX now carries three counts rather than two: {{s029}} samples generated, {{s032}} passing the protocol validity check, and {{s033}} confirmed in the sandbox to still perform the original action, identified by the same observable behaviour used to label the original sample. The success rate is recomputed over the {{s033}} confirmed attacks and we report the numerator and denominator explicitly instead of a bare percentage.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also keep the previously reported figure in the same table, marked as computed over the unverified denominator, so the difference is visible rather than silently corrected. The semantic check is described in Section VI-C, including the observable we rely on and its limitations, since the sandbox is itself an instrument that can fail. Finally we break the counts down by transformation:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

payload splitting accounts for most of the semantic loss, so we now report it separately and discuss whether it belongs in the threat model at all, rather than only removing its failures from the denominator.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng phép biến đổi được thiết kế để giữ ngữ nghĩa nên không cần kiểm. Thiết kế là một ý định, không phải một phép đo, và đây đúng là chỗ reviewer đang chỉ vào.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: thêm một kiểm tra bằng quy tắc, ví dụ xác nhận payload vẫn còn nguyên byte, rồi gọi đó là kiểm ngữ nghĩa. Đã là một phép đo nhưng là phép đo đại diện: byte còn nguyên không suy ra hành vi còn chạy.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: chạy lại mọi mẫu sinh ra trong sandbox, xác nhận hành vi độc hại bằng dấu hiệu quan sát được, báo số mẫu còn hành vi, và tính lại tỉ lệ thành công trên đúng mẫu số đó, kèm cả tử số và mẫu số bằng số tuyệt đối.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.6` bấm thẻ.
