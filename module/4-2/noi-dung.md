---
tieu-de: Zero trust và danh tính, phần kế thừa từ 5G
phu-de: Trụ 4 6G Sec · module 4.2
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
@phan: 6G SEC
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Cái gì trong 5G đã là zero trust rồi, và cái tôi đề xuất thêm vào là cái gì cho chính xác?

## Zero trust và danh tính, phần kế thừa từ 5G
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này là một cổng chống tự thổi đóng góp. Cách dùng rất gọn: lập danh mục cơ chế mà bài của anh kể, rồi lật từng ô để xem ô nào đã có trong `3GPP TS {{s001}}` và ở mục nào. **Ô nào lật ra có số mục thì ô đó KHÔNG được tuyên bố là đóng góp mới.**

## Zero trust và danh tính, phần kế thừa từ 5G (tiếp)
@phut: 1
@che-do: noi

Lý do phải làm thế: kiến trúc dựa dịch vụ (service based architecture) của 5G đã chuẩn hoá sẵn khá nhiều thứ mà bài báo 6G hay kể như mới, gồm che danh tính (identity) thường trực bằng `SUCI`, TLS giữa các hàm mạng, `SEPP` với giao diện `N32` cho liên mạng, và phân quyền bằng token theo từng yêu cầu. Reviewer của IEEE trong lĩnh vực này biết các mục đó, nên một danh mục tự thổi là cách mất bài nhanh nhất.

## Zero trust và danh tính, phần kế thừa từ 5G (tiếp)
@phut: 1
@che-do: noi

Khoảng trống thật thì hẹp hơn nhiều và cũng đáng hơn nhiều: **danh tính cho khối lượng công việc AI** (AI workload identity), tức cho xApp, rApp, mô hình và dữ liệu huấn luyện, chứ không phải danh tính thuê bao. Phát biểu đúng chỗ trống đó là đóng góp; phát biểu rộng hơn là tự thổi.

## Khái niệm tầng 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Khái niệm tầng 1 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một, **không tin theo vị trí mạng**: ở trong vùng được bảo vệ không tạo ra quyền. Hai, **xác thực lại theo từng yêu cầu**, không xác thực một lần rồi cấp phiên dài. Ba, **quyền tối thiểu theo ngữ cảnh**, tức quyền phụ thuộc trạng thái hiện tại chứ không phụ thuộc vai trò tĩnh.

## Khái niệm tầng 1 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cả ba mệnh đề đều là phát biểu về CĂN CỨ tin, không phải về cơ chế mật mã**. Nên thêm TLS hay thêm chữ ký không tự làm một kiến trúc thành zero trust, còn giữ một đường biên tin cậy thì đủ để phá mệnh đề thứ nhất bất kể mật mã mạnh đến đâu. Đây là chỗ để kiểm nhanh một bài:

## Khái niệm tầng 1 · đáp (tiếp)
@phut: 1
@che-do: noi

tìm trong bài một câu lấy vị trí mạng làm căn cứ tin, nếu có thì nhãn zero trust phải bỏ.

## SUCI che cái gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## SUCI che cái gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`SUCI` là định danh thuê bao đã che, sinh bằng cách mã hoá phần định danh thường trực `SUPI` bằng khoá công khai của nhà mạng. Nó chặn kẻ thu thụ động bắt được định danh thường trực trên giao diện vô tuyến.

## SUCI che cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **SUCI che ĐỊNH DANH, không che VỊ TRÍ và không chặn theo dõi**. Định danh tạm thời vẫn tồn tại trong phiên, dấu vết vô tuyến vẫn quan trắc được, và việc một thiết bị cụ thể đang ở đâu vẫn suy ra được bằng các đường khác.

## SUCI che cái gì · đáp (tiếp)
@phut: 1
@che-do: noi

Nhầm che SUPI với bảo vệ vị trí là một trong hai hiểu sai kinh điển của module này, và nó làm hỏng cả phần mô hình đe doạ (threat model) vì nó cấp cho bài một tính chất riêng tư mà chuẩn không hứa.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Danh tính thuê bao trả lời câu hỏi thiết bị nào. Danh tính khối lượng công việc trả lời câu hỏi **mã nào, bản nào, dữ liệu huấn luyện nào, đã ra quyết định này**. Đối tượng được cấp danh tính ở đây là xApp, rApp, mô hình và tập dữ liệu, không phải người dùng.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **nếu không có danh tính cho khối lượng công việc thì mệnh đề thứ ba của zero trust không định nghĩa được cho xApp**, vì không có chủ thể nào để gán quyền tối thiểu theo ngữ cảnh. Đó là lý do khoảng trống này là đóng góp thật, và cũng là lý do một bài đề xuất xác thực lại theo từng yêu cầu giữa các hàm mạng thì không phải đóng góp: phần đó đã có trong chuẩn.

## Đếm đóng góp còn lại sau khi trừ phần đã chuẩn hoá
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`N_moi = max(0, N_ke − N_dachuan) tyLeTuThoi = N_dachuan / N_ke N_moi_AI = max(0, min(N_ai, N_ke − N_dachuan))`

**Giả thiết nó đứng trên:**

## Đếm đóng góp còn lại sau khi trừ phần đã chuẩn (tiếp)
@phut: 1
@che-do: so

- N_ke là số cơ chế mà bài của anh kể trong phần đóng góp, đếm theo đúng danh mục in trong bài chứ không theo cảm nhận
- N_dachuan là số cơ chế trong danh mục đó lật ra được một số mục cụ thể của TS {{s001}}, nên nó đòi anh đã mở tài liệu chứ không đoán
- Một cơ chế chỉ được tính vào N_dachuan khi tra ra ĐÚNG MỤC, vì trích cả tài liệu là không khai được

## Đếm đóng góp còn lại sau khi trừ phần đã chuẩn (tiếp)
@phut: 1
@che-do: so

- N_ai là số cơ chế trong danh mục nhắm vào danh tính khối lượng công việc AI, phần mà chuẩn 5G không phủ

## Đếm đóng góp còn lại sau khi trừ phần đã chuẩn hoá · ghi
@phut: 1
@che-do: noi

Đây là một phép đếm trên văn bản, không phải một phép đo trên hệ thống, nên nó không có sai số thống kê mà có **sai số tra cứu**. Hai chỗ sai hay gặp: tính một cơ chế là mới vì chưa tra ra mục (thiếu công, nhưng vẫn là tự thổi), và tính một cơ chế là đã chuẩn hoá chỉ vì tên nghe giống (trừ oan chính mình). Cả hai chữa bằng cùng một việc:

## Đếm đóng góp còn lại sau khi trừ phần đã chuẩn (tiếp)
@phut: 0.5
@che-do: noi

ghi số mục ngay cạnh từng dòng danh mục, rồi để một người khác lật lại.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s005}} | số mục | Trong TS {{s001}}, SEPP và bảo vệ liên mạng trên giao diện
!so {{s003}} | lược đồ | TS {{s001}} chuẩn hoá bao nhiêu lược đồ bảo vệ định danh

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bản thảo của anh kể {{s007}} cơ chế trong phần đóng góp. Lật danh mục thì {{s006}} cơ chế tra ra được số mục cụ thể trong TS {{s001}}. Bao nhiêu phần trăm danh mục không được tuyên bố là đóng góp mới?

dc = {{s006}}, cc = {{s007}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s008}} × dc / cc`

{{s009}}, tức gần hai phần ba danh mục phải chuyển từ phần đóng góp sang phần nền, kèm số mục. Gần hai phần ba là mức mà abstract buộc phải viết lại, vì câu dẫn của abstract thường chính là danh mục đó. Để ý con số này không nói bài dở: nó nói bài đang đặt phần nền vào chỗ của phần đóng góp, và đó là lỗi sửa được trong một buổi, trước khi reviewer sửa hộ.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mệnh đề hai của zero trust đòi xác thực lại theo từng yêu cầu. Một xApp gọi {{s010}} yêu cầu mỗi giây trong một cửa sổ {{s011}} giây, mỗi lần xác thực lại tốn {{s013}} ms thời gian CPU. Tổng thời gian CPU chỉ để xác thực lại là bao nhiêu giây?

rps = {{s010}}, cuaSo = {{s011}}, ms = {{s012}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`rps × cuaSo × ms / {{s014}}`

{{s015}} giây CPU trong một cửa sổ {{s011}} giây, tức khoảng {{s016}} một lõi cho đúng một xApp. Con số nhỏ, và đó là điểm đáng nói: chi phí mật mã của xác thực lại từng yêu cầu thường KHÔNG phải rào cản, nên lập luận chống zero trust bằng chi phí tính toán là lập luận yếu.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Rào cản thật nằm ở chỗ khác, là có hay không một danh tính để gắn quyền vào, và có hay không hạ tầng khoá để kiểm danh tính đó qua biên liên mạng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Lật ô danh mục ra kết quả TS {{s001}} mục {{s005}}. Theo luật của module, dòng cơ chế đó phải xử thế nào trong bản thảo?

- Chuyển sang phần nền, trích kèm số mục và số bản, và bỏ khỏi danh sách đóng góp
- Giữ trong phần đóng góp và ghi là lần đầu áp dụng cho 6G
- Xoá hẳn khỏi bài vì đã có trong chuẩn
- Giữ trong phần đóng góp nhưng thêm trích dẫn TS {{s001}}

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chuyển sang phần nền, trích kèm số mục và số bản, và bỏ khỏi danh sách đóng góp**

Lật ra số mục nghĩa là cơ chế đã được chuẩn hoá, nên nó là nền, không phải đóng góp. Thêm trích dẫn mà giữ trong phần đóng góp là tệ nhất vì nó tự tố: reviewer đọc được số mục ngay cạnh câu tuyên bố mới.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ghi là lần đầu áp dụng cho 6G chỉ cứu được nếu anh có một phép đo cho thấy việc áp dụng có khó khăn riêng, mà đó lại là một đóng góp khác với cái đang khai. Xoá hẳn là quá tay, vì phần nền vẫn cần để người đọc hiểu kiến trúc.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài tuyên bố cơ chế của nó bảo vệ vị trí người dùng, và bằng chứng duy nhất là hệ dùng SUCI thay vì SUPI. Chỗ hổng là gì?

- Thiếu so sánh thời gian tính toán của SUCI với SUPI
- SUCI dùng khoá đối xứng nên không đủ mạnh
- SUCI che định danh thường trực, không che vị trí, nên bằng chứng không trỏ tới tuyên bố
- SUCI chỉ dùng được ở chế độ không roaming

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**SUCI che định danh thường trực, không che vị trí, nên bằng chứng không trỏ tới tuyên bố**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là hiểu sai kinh điển thứ hai của module. SUCI chặn kẻ thu thụ động lấy định danh thường trực trên giao diện vô tuyến, nhưng định danh tạm thời trong phiên và dấu vết vô tuyến vẫn còn, nên vị trí vẫn suy ra được bằng đường khác. Lỗi ở đây không phải lỗi mật mã mà là lỗi lập luận: bằng chứng và tuyên bố nói về hai đại lượng khác nhau.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Các phương án khác đều là nhận xét về cơ chế, không phải chỗ hổng của lập luận.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài của anh đề xuất xác thực lại theo từng yêu cầu qua biên liên mạng. Reviewer hỏi cơ chế đó dựa vào đâu để kiểm chứng thư của nhà mạng đối tác. Cách trả lời nào giữ được đóng góp mà không giả định thứ chưa có?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Nói rằng chuỗi tin cậy liên mạng là vấn đề triển khai, nằm ngoài phạm vi học thuật
- Thay chứng thư bằng khoá chia sẻ trước giữa hai nhà mạng, và giữ nguyên nhãn zero trust
- Dẫn một bài tổng quan khác cũng giả định hạ tầng khoá liên mạng đã có

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Khai rằng hạ tầng khoá công khai liên mạng là tiền đề, nêu nó trong phần giới hạn, và thu phạm vi đánh giá về trong một miền quản trị

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khai rằng hạ tầng khoá công khai liên mạng là tiền đề, nêu nó trong phần giới hạn, và thu phạm vi đánh giá về trong một miền quản trị**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Khai tiền đề rồi thu phạm vi là cách duy nhất giữ được đóng góp mà không đứng trên thứ chưa tồn tại ở mức vận hành. Gọi đó là vấn đề triển khai là đẩy đúng giả thiết quyết định ra khỏi bài. Khoá chia sẻ trước giữa hai nhà mạng thì chính là tin theo hợp đồng, nên nhãn zero trust phải bỏ.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Dẫn một bài khác cùng giả định không làm giả định đó thành đúng, nó chỉ làm cả hai bài cùng đứng trên một tiền đề chưa kiểm.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đóng góp sau có một câu tự thổi đóng góp. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi đề xuất một kiến trúc zero trust cho mạng 6G dựa trên ba mệnh đề căn cứ tin.
- Đóng góp thứ nhất là xác thực lại theo từng yêu cầu giữa các hàm mạng, thay cho mô hình xác thực một lần của các hệ trước.
- Đóng góp thứ hai là cấp danh tính riêng cho xApp, rApp và cho từng bản mô hình, tách khỏi danh tính thuê bao.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi giả định hạ tầng khoá công khai liên mạng hoạt động, và nêu giả định này trong phần giới hạn.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Đóng góp thứ nhất là xác thực lại theo từng yêu cầu giữa các hàm mạng, thay cho mô hình xác thực một lần của các hệ trước.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Kiến trúc dựa dịch vụ của 5G đã có TLS giữa các hàm mạng và phân quyền bằng token theo từng yêu cầu, đặc tả trong TS {{s001}}, nên dòng này lật ra được số mục và không được tuyên bố là đóng góp mới. Nặng hơn, mệnh đề thay cho mô hình xác thực một lần của các hệ trước là một phát biểu sai về chuẩn, nên reviewer biết chuẩn sẽ coi cả phần đóng góp là chưa đọc tài liệu nền.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu kia đều hợp lệ: câu một là khung, câu ba là đóng góp thật vì chuẩn 5G không phủ danh tính khối lượng công việc, câu bốn khai tiền đề đúng chiều. Cách sửa: chuyển câu này sang phần nền với trích dẫn kèm số mục và số bản, rồi đưa câu ba lên làm đóng góp thứ nhất.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bốn câu sau trích từ bốn mục của cùng một bài zero trust. Một câu làm cả nhãn zero trust của bài phải bỏ. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Mục II: chúng tôi dùng ba mệnh đề zero trust, trong đó mệnh đề một là không tin theo vị trí mạng.
- Mục IV-A: mọi lời gọi giữa hàm mạng đều mang token có ngữ cảnh và thời hạn ngắn.
- Mục IV-C: xApp chạy trong vùng quản trị nội bộ của RIC nên được miễn kiểm token, để giảm độ trễ vòng điều khiển.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Mục VI: chúng tôi chưa đánh giá hành vi của cơ chế khi hạ tầng khoá liên mạng không khả dụng.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Mục IV-C: xApp chạy trong vùng quản trị nội bộ của RIC nên được miễn kiểm token, để giảm độ trễ vòng điều khiển.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Câu này lấy vị trí mạng làm căn cứ miễn kiểm, tức phủ định đúng mệnh đề một mà Mục II vừa khai. Bài tự mâu thuẫn, và nhãn zero trust phải bỏ hoặc phạm vi phải thu lại cho đúng phần có kiểm token. Nặng thêm một bậc: miễn kiểm cho xApp chính là miễn kiểm cho thành phần của bên thứ ba, tức chỗ rủi ro nhất trong kiến trúc.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Lý do giảm độ trễ cũng yếu, vì chi phí xác thực lại từng yêu cầu thường ở mức vài phần trăm một lõi, nên nó cần một phép đo để biện minh chứ không phải một câu khẳng định. Ba câu kia đều hợp lệ, trong đó câu cuối là cách khai giới hạn đúng. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

giữ kiểm token cho xApp và đo lại độ trễ, hoặc nếu thật sự phải miễn thì khai thẳng là kiến trúc có một vùng tin cậy và bỏ nhãn zero trust cho vùng đó.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Lập danh mục N_ke cơ chế mà bản thảo đang kể trong phần đóng góp, một dòng một cơ chế
- Với từng dòng, tra TS {{s001}} và ghi số mục nếu tìm được, ghi trống nếu không
- Đếm N_dachuan là số dòng có số mục, rồi lấy N_moi = N_ke − N_dachuan
- Sửa văn: mọi dòng có số mục chuyển từ phần đóng góp sang phần nền, và trích kèm số mục

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Trong N_moi dòng còn lại, đếm N_moi_AI là số dòng nhắm vào danh tính khối lượng công việc AI, và đặt chúng làm trục của phần đóng góp
- Khai số bản của tài liệu đã tra ngay trong bài, vì N_dachuan là hàm của Release

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: {{s007}} cơ chế đã kể, {{s017}} cơ chế tra ra số mục trong TS {{s001}}, nên {{s017}} đóng góp mới còn lại, trong đó {{s003}} thuộc danh tính khối lượng công việc AI; tỉ lệ danh mục đã có trong chuẩn là {{s018}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Hạ tầng khoá công khai giữa các nhà mạng hoạt động** tắt đi: Không có chuỗi tin cậy liên mạng dùng được ở mức vận hành, nên chứng thư của nhà mạng đối tác không kiểm chứng được một cách độc lập.
- **Mọi hàm mạng phát hành và kiểm được token theo ngữ cảnh** tắt đi: Một phần hàm mạng chỉ kiểm được vai trò tĩnh, hoặc token có thời hạn dài nên ngữ cảnh lúc cấp khác ngữ cảnh lúc dùng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Khối lượng công việc AI có danh tính riêng, phân biệt được với danh tính thuê bao** tắt đi: xApp và mô hình chạy dưới một danh tính dùng chung của nền tảng, hoặc dưới danh tính của người vận hành.
- **Tài liệu chuẩn tôi trích còn hiệu lực và tôi trích đúng mục** tắt đi: Trích theo bản cũ, hoặc trích cả tài liệu mà không có số mục, hoặc mục đã hết hiệu lực ở bản mới.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bộ lật danh mục đóng góp. Mỗi lần kéo là một lần giả định anh tra được thêm một cơ chế trong danh mục ra đúng mục của TS {{s001}}. Đây là phép đếm trên văn bản, không phải phép đo trên hệ thống: con số đổi khi anh tra thêm, chứ không khi hệ thống đổi.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.2` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The contribution list in Section I includes per-request authentication between network functions, mutual TLS inside the service based architecture, and concealment of the permanent subscriber identifier. All three are already specified in 3GPP TS {{s001}}. Please restate the contribution so that it does not overlap with the standard, and justify the remaining novelty.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept the overlap and have restructured the paper. Table I is now a three-column mapping over eight mechanisms: what TS {{s001}} already specifies with the exact clause, what 6G still lacks, and what this paper adds. Four of the eight mechanisms map to clauses of TS {{s001}}, including mutual TLS inside the service based architecture, token based authorization per service request, SUPI concealment via SUCI, and inter-operator protection through SEPP on N32.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

These four have moved from Section I to Section II as background, each cited with clause and release. The contribution is now stated narrowly: identity for AI workloads, meaning xApps, rApps, model versions and training datasets, which is the object the 5G identity framework does not cover. We also state that the count of pre-existing mechanisms is a function of the release we consulted, and we name that release.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, we declare inter-operator public key infrastructure as a precondition rather than a result, and we confine the evaluation to a single administrative domain where that precondition holds.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: thêm trích dẫn TS {{s001}} vào ba dòng đó nhưng giữ chúng trong danh sách đóng góp. Điều này làm phản bác mạnh hơn, vì số mục nằm ngay cạnh câu tuyên bố mới.
- Mức {{s003}}: bỏ ba dòng khỏi danh sách đóng góp nhưng không nói còn lại gì, nên phần đóng góp thành một chỗ trống và bài mất trục.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: chuyển ba dòng sang phần nền với số mục và số bản, rồi phát biểu lại đóng góp đúng vào phần chuẩn 5G không phủ, tức danh tính cho khối lượng công việc AI.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V claims that the proposed scheme protects user location privacy, and the supporting evidence is that the system uses SUCI rather than SUPI. Concealing the permanent identifier does not conceal location. Please either provide evidence for the location claim or remove it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have removed the location privacy claim. Section V now states only what the mechanism supports: a passive eavesdropper on the air interface cannot recover the permanent subscriber identifier, because the identifier is concealed before transmission. We added an explicit privacy threat model with the adversary capabilities, namely passive radio observation without operator-side access, and we state that linkability through temporary session identifiers, radio fingerprints and operations-layer side information remains open and is outside the scope of this work.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table V was relabelled from location privacy to identifier exposure, and the one row that reported a location error metric has been removed because no experiment in the paper measured it.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: lập luận rằng không có định danh thường trực thì không theo dõi được, nên vị trí được bảo vệ. Sai, vì định danh tạm thời trong phiên và dấu vết vô tuyến vẫn cho phép liên kết.
- Mức {{s003}}: làm mềm tuyên bố thành góp phần bảo vệ riêng tư, nhưng không nói góp phần vào đại lượng nào và đo bằng gì, nên tuyên bố vẫn không kiểm được.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: bỏ tuyên bố về vị trí, giữ đúng tuyên bố mà bằng chứng đỡ được, tức chặn kẻ thu thụ động lấy định danh thường trực trên giao diện vô tuyến.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The inter-operator part of the design assumes that certificates of the partner operator can be validated. In current deployments there is no operational public key infrastructure spanning operators, so the mechanism reduces to trust derived from the roaming agreement. Please explain what your scheme adds beyond contractual trust.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree and have separated the two layers of trust. Section III now distinguishes contractual trust between operators, which our scheme does not replace, from cryptographic trust inside one administrative domain, which it does provide. Inter-operator public key infrastructure is declared as a precondition in Section III-A and repeated in the limitations, and every inter-operator claim in Section V has been scoped to that precondition. We also state precisely what survives when the precondition fails:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

per-request authorization and workload identity inside the domain remain fully defined and measurable, because they rely only on the domain's own trust anchor, while any statement about detecting a compromised partner operator becomes undefined rather than weaker, since there is nothing independent of the roaming agreement against which to verify the partner. The evaluation has been rerun inside one domain and Table VI now reports only intra-domain results.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng hạ tầng khoá liên mạng đang được chuẩn hoá nên giả định là hợp lý. Đây là một lời hứa về tương lai, không phải bằng chứng cho kết quả hiện tại.
- Mức {{s003}}: thay chứng thư bằng khoá chia sẻ trước giữa hai nhà mạng và giữ nguyên nhãn zero trust liên mạng. Nhưng khoá chia sẻ trước chính là tin theo hợp đồng, nên nhãn không còn đúng.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai hạ tầng khoá liên mạng là tiền đề, nêu trong phần giới hạn, và thu phạm vi tuyên bố về trong một miền quản trị nơi tiền đề thoả.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.2` bấm thẻ.
