---
tieu-de: Chuẩn và cách trích chuẩn
phu-de: Trụ 4 6G Sec · module 4.6
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 64.5
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

Tài liệu tôi trích còn hiệu lực không, và tôi trích đúng mục hay trích cả tài liệu?

## Trích chuẩn là một phép kiểm được, nên nó bị kiểm
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này không có công tắc giả thiết riêng: khi cần bàn giao diện mở của O-RAN thì dùng lại công tắc của module {{s001}}. Bù lại nó là module nặng nhất về **bắt lỗi**, vì trích chuẩn là chỗ duy nhất trong một bài an ninh mà người đọc kiểm được tuyên bố của anh **mà không cần chạy lại gì cả**. Họ chỉ cần mở tài liệu.

## Trích chuẩn là một phép kiểm được, nên nó bị kiểm (tiếp)
@phut: 1
@che-do: noi

Ba luật của module, gọn tới mức học thuộc được. Một, **TS là đặc tả, TR là nghiên cứu**, nên trích TR như một yêu cầu bắt buộc là sai thẩm quyền, không phải sai định dạng. Hai, một trích dẫn chuẩn khai được phải có **số tài liệu, số bản, và mục cụ thể**; thiếu một trường là không khai được.

## Trích chuẩn là một phép kiểm được, nên nó bị kiểm (tiếp)
@phut: 1
@che-do: noi

Ba, về trạng thái tài liệu thì dùng chữ **hết hiệu lực** chứ không dùng chữ thay thế, khi chưa kiểm quan hệ kế thừa.

## Trích chuẩn là một phép kiểm được, nên nó bị kiểm (tiếp)
@phut: 1
@che-do: noi

Luật thứ ba nhìn như chuyện câu chữ nhưng không phải: nói A thay thế B là khẳng định một quan hệ kế thừa có hướng, tức khẳng định mọi yêu cầu của B đã được A tiếp nhận. Đó là một tuyên bố mạnh hơn hẳn chuyện B hết hiệu lực, và nó sai trong rất nhiều ca thật, vì một tài liệu có thể hết hiệu lực mà phần nội dung của nó tách ra nhiều tài liệu khác nhau.

## TS, TR, và thẩm quyền của câu được trích
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## TS, TR, và thẩm quyền của câu được trích · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Trong 3GPP, nhóm **SA3** phụ trách an ninh và ra các tài liệu số `{{s003}}`, trong đó `TS {{s004}}` là đặc tả kiến trúc và thủ tục an ninh cho hệ 5G.

**TS** (technical specification) là đặc tả: nó phát ra yêu cầu, và một hệ tuân thủ phải làm theo. **TR** (technical report) là báo cáo nghiên cứu: nó khảo sát phương án, nêu đánh đổi, có khi nêu cả phương án bị loại.

## TS, TR, và thẩm quyền của câu được trích · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **trích TR như một yêu cầu bắt buộc là sai thẩm quyền**. Câu trong TR có thể hoàn toàn đúng về kỹ thuật mà vẫn không phải yêu cầu, vì nó là một phương án đang xét. Đây là lỗi nặng hơn lỗi định dạng, vì nó làm sai phần nền của lập luận: anh đang nói chuẩn ĐÒI một thứ mà chuẩn chỉ mới BÀN.

## Luật ba trường
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Luật ba trường · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mỗi trích dẫn chuẩn phải có: **số tài liệu**, **số bản** (Release hoặc version), và **mục cụ thể**. Cộng ngày tra, vì tài liệu chuẩn có bản mới theo thời gian.

## Luật ba trường · đáp (tiếp)
@phut: 1
@che-do: noi

Vì sao cả ba đều bắt buộc: số mục chỉ có nghĩa bên trong một số bản, bởi cùng một tài liệu ở hai bản khác nhau có thể đánh số mục khác nhau và chia mục khác nhau. Nên một trích dẫn có số mục mà không có số bản là một con trỏ không trỏ tới đâu, còn một trích dẫn có số bản mà không có số mục thì đẩy việc tìm sang người đọc.

## Luật ba trường · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **trích cả tài liệu là không khai được**. Câu kiểu xem TS {{s004}} để biết chi tiết nói với người đọc rằng anh đã đọc tài liệu đó, chứ không nói tài liệu đó đỡ cho điều gì. Và nó là loại lỗi tự lộ: ai mở tài liệu ra cũng thấy nó dài hàng trăm trang.

## Trạng thái tài liệu: hết hiệu lực
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s006}} trên bốn.*

## Trạng thái tài liệu: hết hiệu lực · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khi một tài liệu không còn là bản đang dùng, câu đứng được là **tài liệu đó đã hết hiệu lực từ ngày nêu**, kèm nguồn cho ngày đó.

## Trạng thái tài liệu: hết hiệu lực · đáp (tiếp)
@phut: 1
@che-do: noi

Chữ **thay thế** là một tuyên bố mạnh hơn: nó khẳng định một quan hệ kế thừa có hướng, tức mọi yêu cầu của tài liệu cũ đã được tài liệu mới tiếp nhận. Muốn viết chữ đó thì phải kiểm được quan hệ kế thừa, và trong nhiều ca thật quan hệ đó không tồn tại: tài liệu cũ hết hiệu lực mà nội dung của nó tách ra nhiều tài liệu khác nhau, hoặc một phần bị bỏ hẳn.

## Trạng thái tài liệu: hết hiệu lực · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **chưa kiểm quan hệ kế thừa thì viết hết hiệu lực**. Luật này sinh từ một ca thật trong sổ của nhà, và nó rẻ: viết hết hiệu lực không bao giờ sai, còn viết thay thế thì sai được. Cũng để ý một ca riêng: tài liệu HẾT HIỆU LỰC vẫn trích được một cách hợp lệ, miễn là anh đang nói về trạng thái lịch sử và nói rõ điều đó.

## Một trích dẫn chuẩn khai được
@phut: 1.5
@che-do: so
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`trích dẫn khai được = số tài liệu + số bản (Release hoặc version) + mục cụ thể + ngày tra`

**Giả thiết nó đứng trên:**

## Một trích dẫn chuẩn khai được (tiếp)
@phut: 1
@che-do: so

- số mục chỉ có nghĩa BÊN TRONG một số bản: cùng một tài liệu, hai bản khác nhau có thể đánh số mục khác nhau, nên thiếu số bản thì số mục không trỏ tới đâu
- tài liệu chuẩn sống động, tức có bản mới theo thời gian, nên ngày tra là phần của trích dẫn chứ không phải phần của phép lịch sự

## Một trích dẫn chuẩn khai được (tiếp)
@phut: 1
@che-do: so

- thẩm quyền của câu được trích đến từ LOẠI tài liệu: đặc tả thì phát ra yêu cầu, báo cáo nghiên cứu thì không
- nếu dùng để đỡ một tuyên bố bắt buộc thì phải trích câu có động từ quy phạm trong mục đó, không trích tiêu đề mục

## Một trích dẫn chuẩn khai được · ghi chú
@phut: 1
@che-do: noi

Phép kiểm nhanh một danh mục tham khảo: đếm số trích dẫn chuẩn thiếu **bất kỳ** một trong bốn trường. Tỉ lệ đó là thứ reviewer đo được trong vài phút mà không cần hiểu bài, nên nó là bề mặt tuyên bố rẻ nhất để làm sạch và cũng là chỗ mất điểm vô ích nhất. Nối với sổ lỗi của nhà: văn xuôi của hiện vật cũng là bề mặt tuyên bố.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s007}} | trường | Luật trích chuẩn của nhà đòi mỗi trích dẫn phải khai mấy
!so {{s008}} | Release | Đặc tả kiến trúc an ninh của hệ 5G

## Bài tập ở cuối module có 8 trích dẫn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài tập ở cuối module có {{s009}} trích dẫn, trong đó {{s006}} cái không khai được. Tỉ lệ không khai được là bao nhiêu phần trăm?

loi = {{s006}}, tong = {{s009}}

## Bài tập ở cuối module có 8 trích dẫn · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s010}} × loi / tong`

{{s011}}. Con số này cao hơn hẳn cảm giác của người viết, và đó là điều đáng chú ý: ba lỗi trong tám trích dẫn nghe như ít, còn gần bốn trên mười trích dẫn không khai được thì nghe như một danh mục chưa kiểm. Cùng một dữ kiện, hai cách đọc, và reviewer đọc theo cách thứ hai.

## Danh mục 8 trích dẫn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Danh mục {{s009}} trích dẫn, {{s006}} cái không khai được, nên {{s012}} cái sạch. Người đọc mở {{s006}} cái khác nhau, lấy ngẫu nhiên không hoàn lại. Xác suất họ bắt được ít nhất một lỗi là bao nhiêu phần trăm?

sach = {{s012}}, tong = {{s009}}

## Danh mục 8 trích dẫn · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s010}} × ({{s002}} - (sach⋆(sach-1)⋆(sach-2))/(tong⋆(tong-1)⋆(tong-2)))`

Khoảng {{s013}}, tức mở ba trích dẫn trong tám thì hơn bốn lần trên năm là thấy vấn đề, vì xác suất ba cái đều sạch chỉ là {{s014}} trên {{s015}}. Con số này nói ngược hẳn với mô phỏng ở trên, và lý do là ở đó danh mục dài {{s016}} cái với tỉ lệ lỗi {{s017}}: chính TỈ LỆ lỗi quyết định xác suất bị bắt, không phải số lỗi.

## Danh mục 8 trích dẫn · đáp (tiếp)
@phut: 1
@che-do: noi

Danh mục tám cái với ba lỗi có tỉ lệ {{s011}}, gần bốn lần cao hơn.

## Bản thảo viết: theo TR 33.809 của 3GPP
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bản thảo viết: theo TR {{s018}} của 3GPP, bộ thu bắt buộc phải phát hiện trạm gốc giả trước khi nối. Lỗi ở đâu?

- Sai vì phải trích tài liệu mới nhất
- Không có lỗi, vì TR cũng là tài liệu của 3GPP
- Sai thẩm quyền: TR là báo cáo nghiên cứu, nó không phát ra yêu cầu bắt buộc
- Chỉ thiếu số mục, thêm số mục là xong

## Bản thảo viết: theo TR 33.809 của 3GPP · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Sai thẩm quyền: TR là báo cáo nghiên cứu, nó không phát ra yêu cầu bắt buộc**

Câu trong một báo cáo nghiên cứu có thể đúng hoàn toàn về kỹ thuật mà vẫn không phải yêu cầu, vì nó là phương án đang xét chứ không phải điều một hệ tuân thủ phải làm. Thêm số mục không chữa được chỗ đó: nó làm trích dẫn đủ trường mà vẫn sai thẩm quyền. Cách sửa:

## Bản thảo viết: theo TR 33.809 của 3GPP · đáp (tiếp)
@phut: 1
@che-do: noi

hoặc đổi câu thành báo cáo nghiên cứu này KHẢO SÁT các phương án phát hiện trạm gốc giả, hoặc tìm một đặc tả có câu quy phạm tương ứng rồi trích đúng mục của nó.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh thấy bản {{s019}} của một tài liệu không còn nằm trong danh mục bản đang dùng, và chưa kiểm được phần nội dung của nó đi đâu. Câu nào đứng được trong bản thảo?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Tài liệu đó đã bị tài liệu mới thay thế
- Tài liệu đó đã hết hiệu lực từ ngày nêu, theo nguồn đã dẫn
- Tài liệu đó không còn giá trị tham khảo
- Tài liệu đó vẫn còn hiệu lực cho tới khi có thông báo

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tài liệu đó đã hết hiệu lực từ ngày nêu, theo nguồn đã dẫn**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Chữ thay thế khẳng định quan hệ kế thừa có hướng, tức mọi yêu cầu của bản cũ đã được bản mới tiếp nhận, và đó là điều anh vừa nói là chưa kiểm được. Phương án thứ ba nói quá theo chiều khác: tài liệu hết hiệu lực vẫn trích được hợp lệ khi bàn trạng thái lịch sử. Phương án cuối thì ngược với dữ kiện. Chỉ phương án thứ hai nói đúng những gì anh kiểm được, không hơn.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Ba trích dẫn đầu trong tám trích dẫn của bài tập. Một cái trỏ tới một tài liệu không tồn tại. Bấm vào cái đó.

- [{{s002}}] 3GPP TS {{s004}}, Release {{s020}}, mục {{s021}} về thủ tục xác thực và thoả thuận khoá chính.
- [{{s005}}] 3GPP TS {{s004}}, Release {{s022}}, mục {{s023}} về thủ tục 5G AKA.
- [{{s006}}] IS-GPS-200, bản revision đang hiệu lực ngày {{s024}}, mục quy định mức công suất tín hiệu thu tối thiểu của L1 C/A.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**[{{s005}}] 3GPP TS {{s004}}, Release {{s022}}, mục {{s023}} về thủ tục 5G AKA.**

Tài liệu TS {{s004}} ra cùng pha đầu của hệ 5G, tức từ Release {{s008}}, nên không tồn tại bản Release {{s022}} của nó. Đây là lỗi SỐ BẢN, và nó nặng hơn lỗi hình thức vì người đọc không mở được thứ anh trích: trích dẫn trỏ tới một tài liệu không có. Hai trích dẫn kia đều đủ ba trường và số bản của chúng tồn tại. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

chốt số bản mình thật sự đọc, mở đúng bản đó, rồi lấy số mục từ chính bản đó, vì hai bản khác nhau có thể đánh số mục khác nhau.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Ba trích dẫn tiếp theo, lần này gắn với câu văn dùng chúng. Một cái dùng tài liệu sai thẩm quyền. Bấm vào cái đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- [{{s007}}] Theo 3GPP TS {{s025}}, Release {{s026}}, mục về thủ tục an ninh giữa thiết bị người dùng và các phần tử mạng EPS, hệ LTE phải dẫn xuất khoá theo cây khoá đã nêu.
- [{{s012}}] Theo 3GPP TR {{s018}}, bản mới nhất, mục về phát hiện trạm gốc giả, bộ thu bắt buộc phải xác minh thông tin hệ thống trước khi nối.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- [{{s027}}] Theo RFC {{s028}}, mục {{s007}} về tầng bản ghi của DTLS {{s029}}, bản ghi mang số thứ tự được bảo vệ.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**[{{s012}}] Theo 3GPP TR {{s018}}, bản mới nhất, mục về phát hiện trạm gốc giả, bộ thu bắt buộc phải xác minh thông tin hệ thống trước khi nối.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

TR là báo cáo nghiên cứu: nó khảo sát và so sánh phương án, nên nó không phát ra yêu cầu bắt buộc. Chữ bắt buộc phải ở đây gán cho nó thẩm quyền của một đặc tả. Để ý trích dẫn này còn thiếu số bản cụ thể, nhưng đó là lỗi nhẹ hơn và không phải lỗi chính: thêm số bản vào thì trích dẫn đủ trường mà vẫn sai thẩm quyền.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai trích dẫn kia đều dùng đặc tả để đỡ tuyên bố bắt buộc, tức đúng loại tài liệu. Cách sửa: đổi câu thành báo cáo nghiên cứu này khảo sát các phương án phát hiện trạm gốc giả, hoặc tìm đặc tả có câu quy phạm tương ứng rồi trích đúng mục của nó.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Hai trích dẫn cuối trong tám. Một cái không khai được vì trích cả tài liệu. Bấm vào cái đó.

- [{{s030}}] Chi tiết về che danh tính (identity) thường trực của thuê bao, xem 3GPP TS {{s004}}.
- [{{s009}}] NIST FIPS {{s031}}, bản cuối tháng {{s009}} năm {{s019}}, mục {{s030}} về các thuật toán của ML-KEM.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**[{{s030}}] Chi tiết về che danh tính thường trực của thuê bao, xem 3GPP TS {{s004}}.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Trích cả tài liệu mà không có số bản và không có mục cụ thể. Câu này nói với người đọc rằng anh đã đọc tài liệu đó, chứ không nói tài liệu đó đỡ cho điều gì: nó đẩy việc tìm trong hàng trăm trang sang phía người đọc. Đây cũng là loại lỗi tự lộ nhất trong ba loại, vì ai mở tài liệu ra cũng thấy ngay. Trích dẫn [{{s009}}] thì đủ cả ba trường nên khai được. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

chốt số bản, tìm mục quy định cơ chế che danh tính trong đúng bản đó, rồi ghi cả số bản và số mục cùng ngày tra.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đọc LOẠI tài liệu từ số của nó: đặc tả hay báo cáo nghiên cứu
- So loại tài liệu với việc tôi đang dùng nó để làm gì: đỡ một yêu cầu bắt buộc, hay đỡ một nhận định về hiện trạng
- Chốt số bản đang dùng, rồi mở đúng bản đó
- Tìm mục cụ thể và đọc câu có động từ quy phạm trong mục đó, không lấy tiêu đề mục

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Ghi lại số tài liệu, số bản, số mục và ngày tra; nếu bản đó không còn là bản đang dùng thì ghi là đã hết hiệu lực, không ghi là bị thay thế

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Danh mục tham khảo của anh như một bài toán lấy mẫu. Kéo số trích dẫn, tỉ lệ trích dẫn không khai được, và số trích dẫn mà người đọc thật sự mở ra kiểm.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.6` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Reference [{{s012}}] is a 3GPP technical report, yet Section III cites it as a mandatory requirement on the receiver. Several other standard references give no version and no clause, so I cannot check the statements they support. Please correct the normative basis of Section III and complete the standard citations.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have corrected the normative basis and the citations. Section III no longer rests on a technical report: every requirement statement now cites a technical specification with document number, release and clause, and the technical report is cited only where we describe candidate mechanisms that are still under study, with the wording changed from the receiver shall to the report studies mechanisms in which the receiver verifies.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

All standard references now carry document number, release or version, the specific clause, and the date on which we consulted them, listed in Table II so that each statement can be checked without reading the whole document. We audited the complete reference list rather than a sample, which removed three further incomplete entries that the reviewer did not reach.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Where a cited version is no longer the current one, we state that it is no longer in force as of the given date and we cite the source for that date; we deliberately avoid saying that it was superseded, because we have not verified that every requirement of the earlier version was carried into a single later document.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: thêm số mục vào trích dẫn báo cáo nghiên cứu và coi là xong. Trích dẫn thành đủ trường mà vẫn sai thẩm quyền, nên phản bác chính chưa được trả lời.
- Mức {{s005}}: đổi câu văn từ bắt buộc sang được khuyến nghị nhưng vẫn để báo cáo nghiên cứu đỡ cho một yêu cầu thiết kế của bài, và vẫn còn trích dẫn thiếu số bản.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: tách rõ hai loại nguồn, dùng đặc tả cho mọi tuyên bố bắt buộc và dùng báo cáo nghiên cứu chỉ để mô tả phương án đang xét, cộng bổ số bản và mục cụ thể cho toàn bộ trích dẫn chuẩn.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.6` bấm thẻ.
