---
tieu-de: Cô lập slice: cái gì thật sự được cô lập
phu-de: Trụ 4 6G Sec · module 4.7
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 91
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

Khi tôi nói hai slice được cô lập, tôi đang nói cô lập ở tầng nào, và tầng nào vẫn dùng chung?

## Cô lập là một từ, nhưng có bốn tầng
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Cô lập slice là cơ chế an ninh được quảng cáo nhiều nhất của 5G và 6G, và cũng là chỗ dễ viết ra một câu không kiểm được nhất. Câu đó là: **các slice được cô lập**. Nó không sai vì toán, nó sai vì **thiếu tầng**.

## Cô lập là một từ, nhưng có bốn tầng (tiếp)
@phut: 1
@che-do: noi

Có bốn tầng cô lập, và chúng độc lập nhau về cơ chế: **lưu lượng** (định danh riêng, đường hầm riêng), **tài nguyên vô tuyến** (khối tài nguyên dành riêng hay chia sẻ theo lịch), **tính toán** (máy ảo hay thùng chứa riêng), và **quản trị** (ai cấu hình được slice nào). Tầng một, ba và bốn thì làm được bằng cấu hình, và hệ thống thật hay làm. Tầng hai thì không:

## Cô lập là một từ, nhưng có bốn tầng (tiếp)
@phut: 1
@che-do: noi

**bộ lập lịch vô tuyến gần như luôn dùng chung**, nên tải của slice A đổi độ trễ của slice B.

## Cô lập là một từ, nhưng có bốn tầng (tiếp)
@phut: 1
@che-do: noi

Chuyện đó không phải suy đoán, nó **đo được**: tương quan giữa tải slice A và phân vị {{s001}} độ trễ của slice B. Khác {{s002}} có ý nghĩa thống kê là bằng chứng kênh phụ, và cũng là một đường từ chối dịch vụ. Module này có hai việc. Một, cho anh một cách phát biểu đứng được: thay vì nói cô lập, kể tên tầng nào cô lập, tầng nào dùng chung, và hạn mức tối thiểu là bao nhiêu.

## Cô lập là một từ, nhưng có bốn tầng (tiếp)
@phut: 1
@che-do: noi

Hai, cho thấy bằng số rằng **hạn mức tối thiểu là tham số duy nhất biến chia sẻ thành có bảo đảm**, và rằng dành riêng một phần có thể làm kênh phụ **dễ đo hơn** chứ không khó hơn.

## Bốn tầng cô lập slice
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Bốn tầng cô lập slice · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Lưu lượng:** định danh riêng, đường hầm riêng, khoá riêng. **Tài nguyên vô tuyến:** khối tài nguyên dành riêng, hay chia sẻ theo lịch. **Tính toán:** máy ảo hay thùng chứa riêng cho hàm mạng của slice. **Quản trị:** ai cấu hình được slice nào.

## Bốn tầng cô lập slice · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **bốn tầng độc lập nhau về cơ chế, nên cô lập ở ba tầng không suy ra cô lập ở tầng thứ tư**. Ba tầng đầu tiên mà hệ thật hay làm được là lưu lượng, tính toán và quản trị; tầng còn lại là tầng khó, và nó là tầng duy nhất có một đại lượng vật lý dùng chung thật.

## Hạn mức tài nguyên tối thiểu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Hạn mức tài nguyên tối thiểu · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Tỉ lệ dung lượng mà bộ lập lịch cam kết cấp cho một slice bất kể các slice khác chào bao nhiêu tải. Trong mô hình của module nó là `q`, và nó vào công thức ở đúng một chỗ: nó là phần của dung lượng dùng chung mà tải slice A **không chạm tới được**.

## Hạn mức tài nguyên tối thiểu · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **hạn mức tối thiểu là tham số duy nhất biến chia sẻ thành có bảo đảm**. Không có nó thì câu cô lập không có đại lượng nào đứng sau; có nó thì câu đứng được phải mang theo con số, vì `q = {{s005}}` và `q = {{s006}}` là hai hệ khác nhau hẳn.

## Kênh phụ qua bộ lập lịch dùng chung
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Kênh phụ qua bộ lập lịch dùng chung · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Vì bộ lập lịch cấp tài nguyên theo tải tức thời, tải của slice A đổi độ trễ của slice B. Ai ở trong slice B đo được trễ của mình thì **suy ra được tải của slice A**, và ai ở trong slice A đổi tải được thì **đổi được trễ của slice B**. Một chiều là rò rỉ thông tin, chiều kia là từ chối dịch vụ.

## Kênh phụ qua bộ lập lịch dùng chung · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **bằng chứng là một tương quan, không phải một con số một chiều**. Phép đo đứng được là tương quan giữa tải slice A và phân vị {{s001}} độ trễ của slice B, đo khi hai tải được điều khiển độc lập. Thông lượng trung bình của slice B là phép đo sai, vì hạn mức tối thiểu bảo vệ trung bình trước khi nó bảo vệ phần đuôi.

## Cách phát biểu cô lập mà đứng được trước phản biện
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Cách phát biểu cô lập mà đứng được trước phản biện · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Không viết các slice được cô lập. Viết: **cô lập ở tầng lưu lượng, tầng tính toán và tầng quản trị; chia sẻ bộ lập lịch ở tầng tài nguyên vô tuyến, với hạn mức tài nguyên tối thiểu q cho slice B**. Rồi báo tương quan đo được giữa tải slice A và phân vị {{s001}} độ trễ của slice B, kèm khoảng tin.

## Cách phát biểu cô lập mà đứng được trước phản (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **câu đứng được là câu kể tên tầng và mang theo một con số**. Nó dài hơn, nhưng nó là câu duy nhất mà reviewer kiểm được, và nó biến một điểm bị đánh thành một đóng góp đo được. Câu ngắn kia thì hoặc sai số (còn tương quan dư), hoặc sai bản chất (không có đại lượng nào gọi là cô lập ở tầng đó).

## Công thức và giả thiết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`μ_B = d/n + ({{s003}} − d)·[ q + ({{s003}} − q)·(1 − a) ] W₉₅ = ln(20) / (μ_B − λ_B) r = |S| / sqrt(S² + σ²), S = (dW₉₅/da)·sd(a)`

**Giả thiết nó đứng trên:**

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- dung lượng tổng của ô chuẩn hoá về {{s003}}, và thời gian phục vụ trung bình ở dung lượng đầy là {{s003}} ms, nên mọi trễ ở đây đọc theo ms
- slice B chào tải cố định λ_B = {{s009}} trong suốt phép đo; chỉ tải a của slice A thay đổi
- phần dành riêng d chia đều cho n slice và không cho vay, nên slice B luôn giữ d/n dù nó không dùng hết

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- trong phần dùng chung {{s003}} − d, bộ lập lịch bảo đảm cho slice B hạn mức tối thiểu q, phần còn lại chia theo tải và slice A nhả ngay phần nó không dùng
- hàng đợi M/M/1 cho slice B: đến Poisson, thời gian phục vụ mũ, một hàng đợi duy nhất, nên thời gian lưu trú phân bố mũ với tham số μ_B − λ_B và phân vị {{s001}} bằng ln(20) chia cho tham số đó

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- n − {{s004}} slice còn lại không có tải, đây là giả thiết bi quan nhất cho việc dành riêng và phải khai
- nhiễu đo σ = {{s010}} ms trong phân vị {{s001}} của slice B, độc lập với tải slice A; quét a đều trên toàn dải nên sd(a) = 1/sqrt(12)

## Công thức · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Đây là mô hình **đóng dạng**, khai ra để thấy chiều đánh đổi, không phải để thay một phép đo trên hệ thật. Hai chỗ nó nói đúng chiều và dùng được: μ_B không phụ thuộc a khi `d = {{s003}}` hoặc `q = {{s003}}`, và dung lượng bị mắc kẹt tăng theo số slice. Chỗ nó không dùng được:

## Công thức · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

nó không có kênh phụ qua bộ đệm, qua cache hay qua CPU, nên nó là **chặn dưới** của mức rò rỉ, không phải toàn bộ.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s008}} | tầng | Khi anh viết hai slice được cô lập
!so {{s002}} |  | Mức dành riêng đặt {{s011}}

## Một ô có bốn slice
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một ô có bốn slice, mức dành riêng đặt {{s011}} nên dung lượng chia đều và không cho vay. Slice A chào tải {{s006}}, slice B chào {{s009}}, hai slice còn lại không có tải. Bao nhiêu phần trăm dung lượng tổng bị mắc kẹt?

d = {{s003}}, n = {{s008}}, a = {{s012}}, lamB = {{s013}}

## Một ô có bốn slice · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆(Math.max(d/n - a, {{s002}}) + Math.max(d/n - lamB, {{s002}}) + (n-2)⋆d/n)`

## Một ô có bốn slice · đáp (tiếp)
@phut: 1
@che-do: noi

Đúng {{s014}}, tức một nửa dung lượng của ô không ai dùng được. Hai slice không có tải giữ trọn hai khối một phần tư, và cô lập tĩnh nghĩa là không cho vay, nên hai khối đó mắc kẹt. Con số này là cái giá của trạng thái tương quan bằng {{s002}}, và nó tăng theo số slice: đó là lý do dành riêng {{s011}} không phải một lựa chọn vận hành, và là lý do hạn mức tối thiểu tồn tại.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Ba slice, không dành riêng tĩnh, hạn mức tối thiểu của slice B là {{s005}}, slice B chào tải {{s009}}. Slice A đẩy tải lên {{s017}}. Phân vị {{s001}} độ trễ của slice B bằng bao nhiêu ms?

d = {{s002}}, n = {{s007}}, q = {{s015}}, a = {{s016}}, lamB = {{s013}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.log(20)/(d/n + (1-d)⋆(q + (1-q)⋆(1-a)) - lamB)`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s018}} ms, so với {{s019}} ms khi slice A ở tải {{s020}}. Slice B không đổi gì cả: cùng tải, cùng hạn mức, cùng cấu hình, mà trễ đuôi của nó xấu đi hơn ba lần vì một slice khác bận hơn. Đây là kênh phụ nhìn từ phía nạn nhân, và nó cũng là đường từ chối dịch vụ nhìn từ phía slice A. Hạn mức {{s005}} không chặn được chuyện này, nó chỉ đặt một sàn cho dung lượng:

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

muốn chặn hẳn thì phải đẩy hạn mức lên {{s003}} hoặc dành riêng tĩnh, và cả hai đều có giá.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Ba slice chạy trên cùng một gNB. Mỗi slice có định danh riêng, đường hầm riêng, thùng chứa riêng và quyền quản trị tách riêng. Bộ lập lịch vô tuyến dùng chung và không cấu hình hạn mức tối thiểu nào. Phát biểu nào đứng được?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Ba slice được cô lập hoàn toàn.
- Ba slice được cô lập ở tầng tài nguyên vô tuyến, nhờ định danh riêng.
- Không tầng nào được cô lập, vì bộ lập lịch dùng chung.
- Cô lập ở tầng lưu lượng, tầng tính toán và tầng quản trị; tầng tài nguyên vô tuyến dùng chung và không có bảo đảm nào.

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cô lập ở tầng lưu lượng, tầng tính toán và tầng quản trị; tầng tài nguyên vô tuyến dùng chung và không có bảo đảm nào.**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ba trong bốn tầng được cô lập, và tầng tài nguyên vô tuyến thì không, vì không có hạn mức tối thiểu nào biến chia sẻ thành có bảo đảm. Nói cô lập hoàn toàn là mở rộng kết luận sang tầng chưa đo. Nói không tầng nào cô lập là bỏ mất ba tầng mà hệ đã làm được, và đó cũng là một câu không kiểm được. Còn định danh riêng là cơ chế của tầng lưu lượng:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

nó tách luồng (flow), nó không cấp khối tài nguyên vô tuyến nào.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh muốn đưa vào bài một bằng chứng rằng kênh phụ qua bộ lập lịch dùng chung tồn tại. Đại lượng nào là bằng chứng?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Tương quan khác {{s002}} có ý nghĩa thống kê giữa tải slice A và phân vị {{s001}} độ trễ của slice B, đo khi tải hai slice được điều khiển độc lập theo lịch của anh.
- Thông lượng trung bình của slice B đo trong một giờ cao điểm.
- Độ trễ trung bình của slice B vượt mục tiêu dịch vụ đã cam kết.
- Số slice được cấu hình trên gNB và mức dành riêng khai trong tệp cấu hình.

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tương quan khác {{s002}} có ý nghĩa thống kê giữa tải slice A và phân vị {{s001}} độ trễ của slice B, đo khi tải hai slice được điều khiển độc lập theo lịch của anh.**

Bằng chứng phải là một QUAN HỆ giữa hai đại lượng, đo khi hai tải được điều khiển độc lập; thiếu phần điều khiển thì tương quan có thể đến từ nhu cầu dùng chung chứ không từ bộ lập lịch.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Một con số một chiều của riêng slice B thì không phân biệt được nguyên nhân từ slice A với nguyên nhân từ chính tải của slice B, nên cả thông lượng trung bình lẫn trễ trung bình đều không trả lời được câu hỏi. Trung bình còn yếu hơn nữa, vì hạn mức tối thiểu bảo vệ trung bình trước khi nó bảo vệ phần đuôi. Và con số khai trong tệp cấu hình là tham số, không phải phép đo.

## Tắt giả thiết quản trị tách riêng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Tắt giả thiết quản trị tách riêng: người vận hành slice A đổi được cấu hình của slice B, gồm cả hạn mức tối thiểu. Chuyện gì xảy ra với cô lập ở ba tầng còn lại?

## Tắt giả thiết quản trị tách riêng (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng yếu đi theo tỉ lệ số tham số bị lộ.
- Chúng không đổi, vì quản trị là một tầng độc lập với ba tầng kia.
- Chúng thành vô nghĩa, vì mọi cấu hình cô lập đều do tầng quản trị đặt, nên kẻ tấn công đặt được.
- Chúng chỉ còn đúng cho phần lưu lượng đã mã hoá đầu cuối.

## Tắt giả thiết quản trị tách riêng · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chúng thành vô nghĩa, vì mọi cấu hình cô lập đều do tầng quản trị đặt, nên kẻ tấn công đặt được.**

## Tắt giả thiết quản trị tách riêng · đáp (tiếp)
@phut: 1
@che-do: noi

Cô lập ở ba tầng kia là một CẤU HÌNH, và cấu hình nào cũng do tầng quản trị đặt. Khi kẻ tấn công đặt được cấu hình thì không còn đại lượng nào đo được gọi là cô lập, vì mọi giá trị đo hôm nay đều đổi được ngày mai bởi chính kẻ tấn công. Nên đây không phải chuyện yếu đi theo tỉ lệ, và cũng không phải chuyện bốn tầng độc lập nhau:

## Tắt giả thiết quản trị tách riêng · đáp (tiếp)
@phut: 1
@che-do: noi

ba tầng kia phụ thuộc tầng quản trị theo một chiều, chứ không đối xứng. Mã hoá đầu cuối thì bảo vệ nội dung, nó không giữ lại được tính chất cô lập nào ở tầng tài nguyên hay tầng tính toán.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau có một chỗ nhảy một tầng mà không ai cấp cầu. Bấm vào chỗ đó.

- Chúng tôi triển khai ba slice trên cùng một gNB,
- mỗi slice có định danh riêng, đường hầm riêng và thùng chứa riêng cho hàm mạng của nó,
- nên ba slice được cô lập và tải của slice này không ảnh hưởng tới slice kia.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên ba slice được cô lập và tải của slice này không ảnh hưởng tới slice kia.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu đều đúng và đều kiểm được: chúng khai cô lập ở tầng lưu lượng và tầng tính toán. Mệnh đề này nhảy sang tầng tài nguyên vô tuyến, tầng duy nhất mà hai slice chia nhau một đại lượng vật lý, và không có gì ở trên cấp cho nó cái cầu đó. Định danh riêng tách luồng, thùng chứa riêng tách tiến trình, nhưng cả hai không cấp khối tài nguyên vô tuyến nào.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Cách sửa rẻ nhất là bỏ hẳn mệnh đề thứ ba và kể tên hai tầng đã làm được; cách sửa tốt hơn là khai hạn mức tối thiểu đã cấu hình, rồi báo tương quan đo được giữa tải slice A và phân vị {{s001}} độ trễ của slice B.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thực nghiệm sau cho một kết quả âm, và kết quả âm đó không chứng minh gì. Bấm vào chỗ làm nó mất hiệu lực.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Để kiểm cô lập, chúng tôi tăng tải slice A từ {{s021}} lên {{s006}} theo mười bậc,
- giữ tải slice B cố định ở {{s009}} và giữ hạn mức tối thiểu của slice B ở {{s005}},
- rồi đo thông lượng trung bình của slice B ở mỗi bậc và thấy nó đổi dưới {{s022}},
- và báo kết quả đó trong mục đánh giá.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**rồi đo thông lượng trung bình của slice B ở mỗi bậc và thấy nó đổi dưới {{s022}},**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là phép đo sai đại lượng, và nó cho một kết quả âm theo thiết kế. Hạn mức tối thiểu {{s005}} bảo đảm sàn dung lượng cho slice B, mà tải slice B chỉ là {{s009}}, nên thông lượng trung bình của slice B gần như bị ràng buộc phải không đổi bất kể slice A làm gì: công cụ đo không thể bắt được thứ nó đang đi tìm.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Kênh phụ sống ở PHẦN ĐUÔI của trễ, không ở trung bình của thông lượng. Cách sửa: đo phân vị {{s001}} hoặc {{s023}} của trễ slice B, báo hệ số tương quan với tải slice A kèm khoảng tin, và khai lịch điều khiển tải để tương quan nói được chuyện nhân quả.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Trong mô hình của module, chính dải quét {{s021}} tới {{s006}} này cho trễ đuôi của slice B đi từ {{s024}} ms lên {{s025}} ms, tức một tín hiệu hơn hai mươi lần mà phép đo kia không thấy.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Chuẩn hoá dung lượng ô về {{s003}} và đặt λ_B = {{s009}}, tức slice B chào một phần tư dung lượng tổng
- Phần dành riêng d chia đều cho n slice, nên slice B luôn có d/n và không ai lấy được
- Trong phần dùng chung {{s003}} − d, slice B nhận hạn mức q cộng phần chia theo tải ({{s003}} − q)(1 − a)

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Gộp hai nguồn: μ_B = d/n + ({{s003}} − d)[ q + ({{s003}} − q)(1 − a) ]
- Thời gian lưu trú M/M/1 phân bố mũ với tham số μ_B − λ_B, nên W₉₅ = ln(20)/(μ_B − λ_B)
- Tuyến tính hoá quanh điểm làm việc: S = (dW₉₅/da)·sd(a) và r = |S|/sqrt(S² + σ²)

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Trễ phân vị {{s001}} của slice B {{s019}} ms · tương quan tải A với trễ B {{s026}} · dung lượng bị mắc kẹt {{s027}} ở mức dành riêng {{s002}} và hạn mức {{s005}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Bộ lập lịch dành riêng tài nguyên cho từng slice** tắt đi: Một bộ lập lịch duy nhất, chia theo tải tức thời, không có hạn mức tối thiểu nào và không có khối tài nguyên tĩnh nào.
- **Quản trị tách riêng giữa các slice** tắt đi: Người vận hành slice A có quyền đổi cấu hình slice B, gồm cả hạn mức tối thiểu và khối tài nguyên dành riêng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Tải của các slice độc lập thống kê với nhau** tắt đi: Hai slice phục vụ cùng một nhóm người dùng hoặc cùng một sự kiện, nên tải của chúng tương quan với nhau mà không qua bộ lập lịch.
- **Mỗi slice chạy thùng chứa trên nhân riêng, không chia cache** tắt đi: Các hàm mạng của hai slice chạy trên cùng cụm nhân, dùng chung cache mức cuối và dùng chung băng thông bộ nhớ.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ba đại lượng của cùng một cấu hình slice, cạnh nhau: trễ phân vị {{s001}} của slice B, tương quan đo được giữa tải slice A và trễ đó, và dung lượng bị mắc kẹt do dành riêng. Hai thanh đầu là tải và hạn mức, hai thanh sau là lựa chọn kiến trúc của anh.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.7` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III states that the proposed architecture isolates the slices. The only isolation mechanisms described are per slice identifiers, per slice tunnels and per slice containers. None of these constrains the radio scheduler, which Section II describes as a single shared proportional fair scheduler. Please either restate the isolation claim at the layer where it holds, or provide a measurement that supports it at the radio resource layer.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have restated the claim at the layer where it holds. Section III now reads: the design isolates traffic (per slice identifiers and tunnels), compute (per slice containers on dedicated cores) and management (per slice role based access), and shares the radio scheduler, which is configured with a minimum resource quota of {{s015}} for the URLLC slice. We added Section V-D, a controlled experiment:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the load of slice A follows a schedule we impose, independent of the load of slice B, swept from {{s002}} to {{s016}} of cell capacity over ten levels. The 95th percentile delay of slice B rises from {{s028}} ms to {{s029}} ms over that sweep, and the Pearson correlation between the load of slice A and that percentile is {{s030}} with a {{s001}} percent confidence interval of {{s031}} to {{s032}} over {{s033}} repetitions.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We report this as evidence that the radio resource layer is not isolated, and we state the figure as a lower bound on cross slice leakage, because shared last level cache and memory bandwidth at the compute layer were not instrumented. Section V-E reports the alternative: full static partitioning drives the correlation to zero but strands {{s034}} percent of cell capacity at two slices and {{s035}} percent at four, which is why we report the quota value rather than an isolation label.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng cô lập slice là tính chất đã được chuẩn hoá của kiến trúc slice, nên không cần đo. Đúng về mặt dẫn chuẩn, không trả lời được phản bác, vì chuẩn định nghĩa cơ chế chứ không bảo đảm một đại lượng.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: thêm một câu rằng bộ lập lịch có cấu hình hạn mức tối thiểu, nhưng vẫn giữ câu các slice được cô lập và vẫn không có phép đo nào ở tầng tài nguyên.
- Mức {{s007}}: phát biểu lại theo tầng, kể tên ba tầng cô lập được và khai tầng tài nguyên vô tuyến là dùng chung với hạn mức tối thiểu đã cấu hình, cộng một phép đo trễ đuôi của slice B theo tải slice A.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The threat model in Section II assumes the attacker is an external party outside the operator domain. Section VI then claims that slice isolation protects the URLLC slice from a compromised eMBB slice tenant. A tenant is inside the operator domain and holds management rights over its own slice. Which model should the reader use?

## Đáp mẫu
@phut: 1.5
@che-do: noi

The two sections were inconsistent and we have collapsed them into one model. Section II now defines a single adversary that includes a compromised slice tenant, which holds management rights over its own slice and no rights over other slices. We then re examine each isolation layer under that model. Traffic, compute and management isolation are configurations, and every configuration is set at the management layer, so the first three layers are no stronger than the access control on that layer:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

if a tenant can edit another slice profile, isolation at the other three layers does not weaken, it loses meaning, because any measured value can be changed by the adversary. We therefore added Section III-A, which states the role separation we rely on and cites the configuration audit that enforces it. At the radio resource layer the quota remains a shared scheduler guarantee, and Section V-D reports the residual correlation of {{s030}} under that configuration.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also removed the sentence that claimed protection against a compromised tenant at the radio layer, because the quota bounds capacity and does not bound the delay tail.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng hai mục nói về hai tình huống khác nhau và sẽ làm rõ bằng một câu. Nhận ra vấn đề về trình bày, chưa nhận ra là mô hình đe doạ tự mâu thuẫn.
- Mức {{s004}}: mở rộng mô hình đe doạ sang kẻ tấn công nội bộ, nhưng vẫn giữ nguyên phần phòng vệ và vẫn khai bốn tầng cô lập như trước.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: chọn một mô hình đe doạ duy nhất gồm cả thuê bao nội bộ, rồi xét lại từng tầng cô lập theo mô hình đó, và khai rõ tầng quản trị là điều kiện của ba tầng kia.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table V reports that increasing the dedicated resource fraction from {{s002}} to {{s037}} improves isolation. Your own Figure {{s036}} shows the measured correlation between the load of slice A and the delay tail of slice B rising over that same range. One of the two is wrong, or the metric called isolation in Table V is not the quantity plotted in Figure {{s036}}. Please resolve this.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Table V and Figure {{s036}} were measuring different things, and we have fixed the table. The column previously labelled isolation was the configured dedicated resource fraction, a parameter, not an observable. We removed the label and now report the measured correlation as the primary metric. The rising trend in Figure {{s036}} is real and we now explain it:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

partial static partitioning removes capacity from the shared pool, so the service rate available to slice B falls from {{s038}} to {{s039}} of cell capacity and slice B sits closer to its own saturation point. The sensitivity of the delay tail scales with the inverse square of the margin between that service rate and the offered load of slice B, and over this range it grows faster than the factor that the dedicated fraction removes.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The correlation therefore rises from {{s030}} to {{s032}} before collapsing to zero only at full partitioning. We state the operational consequence explicitly: a partial mitigation can make this side channel easier to measure, so the dedicated fraction must not be reported as a monotone isolation knob, and full partitioning strands {{s034}} percent of cell capacity at two slices and {{s035}} percent at four.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng Hình {{s036}} có nhiễu đo và sẽ chạy thêm lần lặp. Không nhận ra là hai chỗ đang đo hai đại lượng khác nhau.
- Mức {{s004}}: sửa Bảng V cho khớp Hình {{s036}} bằng cách bỏ cột cô lập, nhưng không giải thích vì sao tương quan tăng, nên người đọc vẫn không biết tin chỗ nào.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: khai rằng Bảng V đo tỉ lệ dung lượng dành riêng, tức một tham số cấu hình, còn Hình {{s036}} đo tương quan, tức một đại lượng quan trắc, và hai thứ không thay thế nhau; rồi báo tương quan làm thước đo chính.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.7` bấm thẻ.
