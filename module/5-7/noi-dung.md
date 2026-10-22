---
tieu-de: Di trú và cách viết phần mô hình đe doạ
phu-de: Trụ 5 PQC · module 5.7
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 87
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: PQC
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Trong hệ tôi đang viết, ai giữ khoá nào, trong bao lâu, và tôi đã nói rõ chưa?

## Module này là bài tập viết
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Có một câu phản biện lặp lại nhiều hơn mọi câu khác trong hồ sơ của nhà: **the threat model is not clearly stated**. Nó rẻ để viết ra, tốn kém để trả lời, và không bao giờ trả lời được bằng cách thêm một thí nghiệm. Module này dạy đúng một thứ: khuôn **sáu dòng** để viết phần mô hình đe doạ, và cách kiểm xem từng câu kết luận trong bài còn cơ sở hay không khi thiếu một dòng.

## Module này là bài tập viết (tiếp)
@phut: 1
@che-do: noi

Sáu dòng, học thuộc theo thứ tự: tài sản cần bảo vệ; kẻ tấn công và năng lực; cái kẻ tấn công **không** làm được; giả định tin cậy; thời hạn bảo mật; điều gì nằm ngoài phạm vi. Dòng ba là dòng bị bỏ nhiều nhất, và bỏ nó thì mọi tuyên bố an toàn đều đổ, vì một kẻ tấn công không bị giới hạn gì thì phá được mọi thứ.

## Module này là bài tập viết (tiếp)
@phut: 1
@che-do: noi

Dòng năm là dòng duy nhất cho ra một con số, và con số đó chính là `x` trong bất đẳng thức Mosca.

## Module này là bài tập viết (tiếp)
@phut: 1
@che-do: noi

Và một thứ tự không đổi được của việc di trú: **kiểm kê trước, phân loại theo thời hạn bảo mật, rồi mới chọn thuật toán**. Chọn thuật toán trước là sai thứ tự, và nó lộ ra ngay trong bài: phần đánh giá so byte của ba bộ tham số rất kỹ, mà không ai biết dữ liệu của hệ cần giữ mật bao lâu.

## Khuôn mô hình đe doạ sáu dòng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Khuôn mô hình đe doạ sáu dòng · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một, tài sản cần bảo vệ. Hai, kẻ tấn công và năng lực. Ba, cái kẻ tấn công KHÔNG làm được. Bốn, giả định tin cậy, tức ai giữ khoá nào và ai được đọc bản rõ. Năm, thời hạn bảo mật, tức dữ liệu phải giữ mật bao nhiêu năm. Sáu, điều gì nằm ngoài phạm vi.

## Khuôn mô hình đe doạ sáu dòng · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: sáu dòng này không phải để làm đẹp phần mở đầu, chúng là **sáu điều kiện mà mỗi câu kết luận của bài phải tra vào**. Một câu kết luận không tra được vào dòng nào là một câu không có cơ sở, và đó chính là thứ reviewer phát hiện khi họ viết the threat model is not clearly stated. Thiếu dòng ba hoặc dòng bốn là hai ca nặng nhất.

## Thứ tự di trú không đảo được
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Thứ tự di trú không đảo được · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ba bước: kiểm kê nơi nào trong hệ đang dùng mật mã khoá công khai; phân loại từng nơi theo `x`, tức số năm dữ liệu ở đó còn cần giữ mật; rồi mới chọn thuật toán và bộ tham số cho từng nhóm.

## Thứ tự di trú không đảo được · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: thứ tự này không đảo được vì `x` là thứ quyết định nơi nào gấp. Hai nơi trong cùng một hệ có thể cần hai lời giải khác nhau: khoá phiên của một kênh điều khiển thời gian thực có `x` bằng vài phút nên không gấp theo nghĩa thu hoạch trước giải mã sau, còn một phép đo y tế có `x` bằng vài chục năm nên đã trễ từ lâu.

## Thứ tự di trú không đảo được · đáp (tiếp)
@phut: 1
@che-do: noi

Chọn thuật toán trước là tự ép cả hệ vào một lời giải, và trong bài báo nó lộ ra ở chỗ phần đánh giá so byte rất kỹ mà không ai nói dữ liệu cần giữ mật bao lâu.

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

Tách lựa chọn thuật toán ra khỏi giao thức và khỏi kiến trúc, để đổi thuật toán mà không đổi định dạng bản tin, không đổi quy trình cấp chứng chỉ, không đổi lịch cập nhật firmware. Cụ thể là bộ định danh thuật toán có chỗ ở trong bản tin, kích thước khoá không bị mã hoá cứng vào bộ nhớ đệm, và thiết bị thương lượng được.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đây là đóng góp **dễ bảo vệ hơn** một thuật toán mới, vì nó không cần ai tin một giả định độ khó mới. Nhưng nó chỉ được tính là đóng góp khi bài báo chứng minh được tính linh hoạt bằng cách **thực sự đổi**: chạy cùng hệ với hai bộ thuật toán khác kích thước và đo chi phí của việc đổi.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Khai linh hoạt mà trong mã vẫn cố định ML-KEM-768 là chỗ reviewer bắt, và đó là một thẻ bắt lỗi của module này.

## Mosca, và hai đại lượng suy ra từ nó
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`đã trễ khi x + y > z năm muộn nhất phải bắt đầu = năm nay + z − y − x số năm dữ liệu gửi hôm nay bị lộ = max(0, x + y − z)`

**Giả thiết nó đứng trên:**

## Mosca, và hai đại lượng suy ra từ nó (tiếp)
@phut: 1
@che-do: so

- x là số năm dữ liệu gửi HÔM NAY còn cần giữ mật, và nó đến từ dòng năm của mô hình đe doạ, không từ phỏng đoán
- y là số năm di trú thật của hệ, gồm cả kiểm kê, thử nghiệm, cập nhật thiết bị ngoài hiện trường và thời gian sống của lô thiết bị cũ

## Mosca, và hai đại lượng suy ra từ nó (tiếp)
@phut: 1
@che-do: so

- z là số năm cho tới khi kẻ tấn công có máy lượng tử đủ sức, và nó là ƯỚC LƯỢNG, nên mọi kết luận phải viết ở dạng điều kiện theo z
- mô hình đe doạ có thu hoạch bây giờ giải mã sau, tức kẻ tấn công lưu được bản mã hôm nay và giải mã khi có máy

## Mosca, và hai đại lượng suy ra từ nó · ghi chú
@phut: 1
@che-do: noi

Vì z là ước lượng, phần lớn tranh luận về PQC thật ra là tranh luận về z chứ không về toán học. Cách viết an toàn trong bài báo: không khai một giá trị z, mà khai kết luận theo DẢI z, rồi chỉ ra dải nào làm kết luận đảo chiều.

## Mosca, và hai đại lượng suy ra từ nó · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

Khi x lớn (dữ liệu y tế, hồ sơ quốc phòng) thì kết luận không phụ thuộc z trong cả dải hợp lý, và đó là loại dữ liệu đáng viết bài về.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s004}} | dòng | Khuôn mô hình đe doạ của module này có bao nhiêu dòng
!so {{s005}} | B | Chữ ký của ML-DSA-65 dài bao nhiêu byte?

## Phép đo y tế phải giữ mật 20 năm
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phép đo y tế phải giữ mật {{s006}} năm, di trú lô thiết bị mất {{s007}} năm, ước lượng cho tới khi có máy lượng tử đủ sức là {{s008}} năm. Theo Mosca, đã trễ bao nhiêu năm?

x = {{s006}}, y = {{s007}}, z = {{s008}}

## Phép đo y tế phải giữ mật 20 năm · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`x + y - z`

Trễ {{s009}} năm, tức lẽ ra phải bắt đầu di trú từ {{s010}}. Chú ý chiều của kết luận: con số dương nghĩa là dữ liệu gửi HÔM NAY sẽ còn cần giữ mật trong {{s009}} năm sau khi kẻ tấn công đã có máy, nên nó không nói về thiết bị tương lai mà nói về dữ liệu đang chạy trên dây lúc này. Và chú ý thứ hai:

## Phép đo y tế phải giữ mật 20 năm · đáp (tiếp)
@phut: 1
@che-do: noi

{{s009}} năm này nhạy với z, đổi z sang {{s006}} năm thì độ trễ về {{s007}} năm, nên câu kết luận trong bài phải viết theo dải z.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Kiểm kê cho thấy mỗi bản cập nhật firmware mang một chữ ký. Đổi từ ECDSA P-256 ({{s011}} byte) sang ML-DSA-65 ({{s005}} byte) thì byte chữ ký tăng bao nhiêu lần?

mlDsa = {{s005}}, ecdsa = {{s011}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`mlDsa / ecdsa`

Khoảng {{s012}} lần, tức bậc {{s013}} lần. Con số này là lý do kiểm kê phải đi trước:

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

chỗ nào trong hệ chỉ ký một lần cho một bản firmware vài trăm kB thì {{s005}} byte chiếm bậc {{s001}} phần trăm bản cập nhật, còn chỗ nào ký từng bản tin cảm biến {{s006}} byte thì chữ ký nặng hơn dữ liệu hơn {{s014}} lần và cả thiết kế phải đổi, ví dụ sang xác thực bằng khoá đối xứng với khoá do bắt tay cấp.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Cùng một phép đổi thuật toán, hai nơi trong cùng một hệ, hai kết luận trái ngược.

## Bài báo viết
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài báo viết: chúng tôi chọn ML-KEM-768 vì nó là mặc định hợp lý, rồi đo chi phí trên thiết bị. Sai thứ tự ở đâu?

## Bài báo viết (tiếp)
@phut: 0.5
@che-do: hoi

- Phải chọn mức tham số cao nhất rồi hạ dần khi đo thấy quá nặng
- Phải kiểm kê và phân loại theo thời hạn bảo mật trước, vì chính thời hạn đó quyết định mức tham số và quyết định nơi nào gấp
- Phải đo chi phí trước rồi mới chọn thuật toán theo ngân sách
- Không sai thứ tự, vì mức {{s003}} đúng là mặc định hợp lý

## Bài báo viết · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Phải kiểm kê và phân loại theo thời hạn bảo mật trước, vì chính thời hạn đó quyết định mức tham số và quyết định nơi nào gấp**

## Bài báo viết · đáp (tiếp)
@phut: 1
@che-do: noi

Thứ tự di trú là kiểm kê, phân loại theo x, rồi chọn thuật toán. Chọn trước rồi đo là tự ép cả hệ vào một lời giải, và nó làm mất chính thông tin đáng giá nhất của bài: hai nơi trong cùng một hệ có x khác nhau vài bậc thì cần hai lời giải khác nhau. Đáp án thứ ba nghe hợp lý nhưng vẫn sai, vì ngân sách chi phí không nói được dữ liệu phải giữ mật bao lâu.

## Bài báo viết · đáp (tiếp)
@phut: 1
@che-do: noi

Đáp án thứ tư đúng rằng mức {{s003}} là mặc định hợp lý, nhưng một mặc định hợp lý không thay được một bước kiểm kê.

## Trong sáu dòng của mô hình đe doạ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong sáu dòng của mô hình đe doạ, thiếu dòng nào thì MỌI tuyên bố an toàn của bài đổ cùng lúc?

- Dòng sáu, điều gì nằm ngoài phạm vi
- Dòng một, tài sản cần bảo vệ
- Dòng ba, cái kẻ tấn công KHÔNG làm được
- Dòng năm, thời hạn bảo mật

## Trong sáu dòng của mô hình đe doạ · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Dòng ba, cái kẻ tấn công KHÔNG làm được**

Thiếu dòng ba thì kẻ tấn công không bị giới hạn gì, và một kẻ tấn công đọc được bộ nhớ thiết bị phá được mọi hệ, kể cả hệ hoàn hảo về mật mã. Nên không còn tuyên bố an toàn nào đứng. Thiếu dòng một thì tuyên bố mất đối tượng nhưng chúng thường suy được từ ngữ cảnh. Thiếu dòng năm thì phần động lực sụp mà phần đánh giá vẫn đứng.

## Trong sáu dòng của mô hình đe doạ · đáp (tiếp)
@phut: 1
@che-do: noi

Thiếu dòng sáu thì tuyên bố bị đọc rộng hơn ý định, tệ nhưng sửa được bằng một câu.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Phần mô hình đe doạ sau thiếu đúng một dòng, và thiếu dòng đó thì mọi tuyên bố an toàn của bài đổ. Bấm vào chỗ lộ ra sự thiếu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Tài sản cần bảo vệ: phép đo y tế của bệnh nhân, và định danh của thiết bị.
- Kẻ tấn công: một đối thủ lưu được toàn bộ lưu lượng vô tuyến và lưu lượng Internet trên đường đi, và về sau có máy lượng tử.
- Giả định tin cậy: server bệnh viện tin cậy, gateway chỉ chuyển tiếp bản mã và không chấm dứt OSCORE.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Thời hạn bảo mật: {{s006}} năm, theo quy định lưu hồ sơ bệnh án. Ngoài phạm vi: tính sẵn sàng và tấn công kênh phụ.
- Do đó hệ của chúng tôi bảo đảm tính bí mật của phép đo y tế trong {{s006}} năm kể cả trước kẻ tấn công có máy lượng tử.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Do đó hệ của chúng tôi bảo đảm tính bí mật của phép đo y tế trong {{s006}} năm kể cả trước kẻ tấn công có máy lượng tử.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Bốn dòng trên đều viết tốt: có tài sản, có kẻ tấn công và năng lực, có giả định tin cậy, có thời hạn bảo mật và có phạm vi. Thiếu đúng dòng ba của khuôn, tức cái kẻ tấn công KHÔNG làm được, và câu này là chỗ sự thiếu đó thành một lỗi thật:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

kẻ tấn công đã được khai là lưu được mọi thứ mà chưa bị cấm điều gì, nên không gì ngăn họ tháo cảm biến và đọc khoá riêng, và lúc đó bí mật {{s006}} năm sai ngay trong năm đầu. Cách sửa mất một dòng: kẻ tấn công không có truy cập vật lý kéo dài vào cảm biến, không trích được khoá khỏi vùng lưu trữ an toàn, và không chạm được vào quy trình cấp khoá ban đầu.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp di trú sau có một bước đặt sai thứ tự. Bấm vào bước đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi chọn ML-KEM-768 và ML-DSA-65 vì chúng là mức mặc định hợp lý cho phần lớn giao thức,
- sau đó kiểm kê toàn bộ các nơi trong hệ đang dùng mật mã khoá công khai, gồm bắt tay, cập nhật firmware và chứng chỉ thiết bị,
- phân loại từng nơi theo số năm dữ liệu ở đó còn cần giữ mật,
- rồi đo chi phí byte và chu kỳ cho từng nhóm trên thiết bị thật.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Chúng tôi chọn ML-KEM-768 và ML-DSA-65 vì chúng là mức mặc định hợp lý cho phần lớn giao thức,**

Đây là bước chọn thuật toán, và nó đứng TRƯỚC kiểm kê với phân loại, tức sai thứ tự. Ba bước di trú không đảo được: kiểm kê nơi dùng mật mã, phân loại theo thời hạn bảo mật, rồi mới chọn thuật toán. Hậu quả không phải là chọn sai bộ tham số, mà là mất chính kết quả đáng giá nhất của bài:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

trong cùng một hệ, khoá phiên của kênh điều khiển có thời hạn bảo mật vài phút còn phép đo y tế có thời hạn {{s006}} năm, nên hai nơi đó cần hai lời giải khác nhau, và một lựa chọn chung cho cả hệ che mất chuyện đó. Ba đoạn sau đều hợp lệ và chúng chính là thứ phải chạy TRƯỚC đoạn này.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đóng góp sau có một câu mà phần còn lại của bài không đỡ được. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Đóng góp thứ nhất: một kiến trúc tách bộ định danh thuật toán ra khỏi định dạng bản tin, nên đổi KEM không đổi định dạng.
- Đóng góp thứ hai: một phép đo chi phí byte và chu kỳ của ML-KEM-768 trên thiết bị lớp Cortex-M.
- Nhờ tính linh hoạt mật mã này, hệ của chúng tôi đổi sang bất kỳ KEM hậu lượng tử tương lai nào mà không cần đổi kiến trúc.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Nhờ tính linh hoạt mật mã này, hệ của chúng tôi đổi sang bất kỳ KEM hậu lượng tử tương lai nào mà không cần đổi kiến trúc.**

Hai đóng góp trên đều phát biểu được và kiểm được. Câu này nói quá theo hai cách. Một, bất kỳ KEM tương lai nào là một lượng tử hoá toàn phần mà bài không chứng minh:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

nó chỉ đúng cho các KEM có kích thước khoá và bản mã nằm trong vùng bộ nhớ đệm đã cấp, nên một KEM dựa mã với khoá công khai vài chục kB phá vỡ ngay, dù bộ định danh thuật toán có chỗ ở trong bản tin. Hai, bài chỉ chạy MỘT bộ thuật toán, nên tính linh hoạt chưa được chứng minh bằng cách thực sự đổi. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

chạy cùng hệ với hai bộ thuật toán khác kích thước, đo chi phí của việc đổi, rồi phát biểu điều kiện cụ thể mà kiến trúc đỡ được, ví dụ mọi KEM có khoá công khai không vượt {{s002}} kB.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Kiểm kê: liệt kê mọi nơi trong hệ dùng mật mã khoá công khai, gồm bắt tay EDHOC, cập nhật firmware, và chứng chỉ thiết bị
- Phân loại theo x: phép đo y tế x bằng {{s006}} năm theo quy định lưu hồ sơ, khoá phiên điều khiển x bằng vài phút
- Đo y cho nhóm có x lớn nhất: ở đây {{s007}} năm, vì thiết bị ngoài hiện trường chỉ cập nhật được theo lịch bảo trì

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Lấy z từ một dải công bố và chọn một giá trị để trình bày, ở đây z bằng {{s008}} năm, và khai rõ đó là ước lượng
- Tính: năm muộn nhất phải bắt đầu bằng năm nay cộng z trừ y trừ x, ra {{s010}}, tức đã trễ

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: mô hình đe doạ đủ {{s004}} dòng · tài sản: phép đo y tế · thời hạn bảo mật x = {{s006}} năm · di trú y = {{s007}} năm · z = {{s008}} năm · Mosca: trễ {{s009}} năm · hybrid {{s016}} byte phía khách

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dòng {{s001}}: tài sản cần bảo vệ** tắt đi: Bài không nói bảo vệ cái gì, chỉ nói bảo vệ truyền thông.
- **Dòng {{s002}}: kẻ tấn công và năng lực** tắt đi: Bài không nói ai tấn công và làm được gì, chỉ nói kẻ tấn công.
- **Dòng {{s003}}: cái kẻ tấn công KHÔNG làm được** tắt đi: Bài không đặt giới hạn nào cho kẻ tấn công.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dòng {{s015}}: giả định tin cậy, ai giữ khoá nào** tắt đi: Bài không nói gateway và server được đọc gì.
- **Dòng {{s007}}: thời hạn bảo mật** tắt đi: Bài không nói dữ liệu phải giữ mật bao lâu.
- **Dòng {{s004}}: điều gì nằm ngoài phạm vi** tắt đi: Bài không khai cái gì không xét.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Lịch di trú theo Mosca, và chỗ nó nối vào dòng năm của mô hình đe doạ. Kéo ba đại lượng và để ý rằng thứ đổi kết luận mạnh nhất không phải z mà là x, tức con số đến từ nghĩa vụ giữ bí mật chứ không từ dự báo công nghệ.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.7` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The threat model is not clearly stated. It is therefore impossible to assess the claim in Section I that the proposed design provides end-to-end security for the medical measurements, or to judge whether the post-quantum migration is urgent for this system.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Section I now opens with an explicit six-line threat model, and we have rewritten the security claim so that every part of it maps to one of those lines. The asset is the content of the medical measurements and the patient activity pattern that the measurement timing reveals. The adversary records all radio and Internet traffic on the path and later obtains a large quantum computer, which is what makes harvest-now-decrypt-later relevant here.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The adversary does not have prolonged physical access to the sensor, cannot extract keys from its secure storage, and cannot interfere with initial key provisioning. The trust assumptions are stated with the architecture figure: plaintext exists only at the sensor and at the hospital server, and the home gateway forwards OSCORE messages without terminating them. The secrecy lifetime is {{s006}} years, from the record-retention obligation. Availability and side-channel attacks are out of scope. Two consequences follow.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

First, we removed the phrase end-to-end security and replaced it with the two endpoints named above, because the earlier phrasing was ambiguous about the gateway. Second, the secrecy lifetime now carries the motivation quantitatively: with a 20-year lifetime, a 5-year device-fleet migration and a 12-year estimate for a capable quantum adversary, the Mosca inequality gives a 13-year deficit, so data on the wire today would have needed post-quantum protection since {{s010}}. We state the dependence on the estimate explicitly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the conclusion holds for every value of that estimate below {{s017}} years.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: thêm một đoạn nói kẻ tấn công là kẻ tấn công Dolev-Yao chuẩn. Đúng về hình thức, không trả lời được, vì nó không nói tài sản, không nói giới hạn, không nói thời hạn.
- Mức {{s002}}: viết một đoạn mô hình đe doạ nhưng vẫn thiếu dòng cái kẻ tấn công KHÔNG làm được hoặc thiếu thời hạn bảo mật, nên tuyên bố vẫn chưa kiểm được.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: viết đủ sáu dòng (tài sản, kẻ tấn công và năng lực, cái kẻ tấn công không làm được, giả định tin cậy, thời hạn bảo mật, ngoài phạm vi), và bỏ cụm đầu cuối tới đầu cuối để viết thẳng chỗ nào bản rõ xuất hiện.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section VI claims that crypto-agility is a main contribution, but the implementation hard-codes ML-KEM-768 buffer sizes and the evaluation reports a single algorithm suite. The claim is therefore not supported by evidence.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept the criticism and have replaced the claim with a measured one. Three changes. First, buffer sizes are now derived from the negotiated algorithm identifier at compile time rather than fixed, and Section IV-D documents the single place in the code where that derivation happens. Second, the evaluation now runs the same system with two suites of different size, ML-KEM-512 and ML-KEM-768, and reports the cost of switching:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the client key share grows from {{s018}} to {{s016}} bytes, the fragment count at a 100-byte usable payload grows from {{s019}} to {{s009}}, peak RAM grows by {{s020}} kB, and no protocol message format changes. Third, we state the boundary instead of claiming generality.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The architecture holds for key establishment methods whose public key and ciphertext each stay within {{s002}} kB, which covers the lattice KEMs but not code-based KEMs with public keys of tens of kilobytes; for those the fragmentation layer and the message buffer would both need redesign, and we say so rather than implying otherwise. The contribution is therefore stated as agility within a declared size envelope, with the envelope given as a number.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: nói rằng kiến trúc có chỗ cho bộ định danh thuật toán nên nó linh hoạt về thiết kế. Không trả lời được, vì reviewer đòi bằng chứng chứ không đòi ý định.
- Mức {{s002}}: bỏ mã hoá cứng kích thước bộ đệm nhưng vẫn chỉ báo một bộ thuật toán, nên vẫn chưa có phép đổi nào được chứng minh.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: chạy cùng hệ với tối thiểu hai bộ thuật toán khác kích thước, báo chi phí của việc đổi (byte, bộ nhớ đỉnh, số dòng mã phải sửa), và phát biểu điều kiện cụ thể mà kiến trúc đỡ được.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The motivation in Section I asserts that migration is urgent, but the paper gives no quantity to support this. The Mosca inequality is cited without instantiating its parameters for the system under study.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have instantiated the inequality for this system and traced every parameter to a source inside the paper. The secrecy lifetime x is {{s006}} years, taken from the record-retention obligation stated in the threat model, not from our own judgement. The migration time y is {{s007}} years, derived from the maintenance schedule of the deployed fleet in Section II, because field devices are updated only at scheduled service visits. For the time to a capable quantum adversary we do not use a single value.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We report the conclusion across the range {{s007}} to {{s021}} years: the deficit x plus y minus z is positive for every estimate below {{s017}} years, and at the 12-year estimate it is {{s009}} years, meaning that data on the wire today would have needed post-quantum protection since {{s010}}. We also state the structural point that makes this argument robust:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

because x is {{s006}} years, no estimate within the published range removes the deficit by more than {{s006}} years of margin, so the conclusion for this data class does not rest on our choice of estimate. For the control-plane session keys in the same system, where x is minutes, the inequality gives no deficit at any estimate in the range, and we therefore recommend different timelines for the two data classes rather than one timeline for the system.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: thêm một câu nói nhiều tổ chức đã bắt đầu di trú. Đúng mà không liên quan, vì nó không nói gì về hệ đang xét.
- Mức {{s002}}: dẫn Mosca và cho một giá trị cho từng tham số, nhưng không nói các giá trị đó lấy từ đâu, nên con số không kiểm được.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: khai x từ nghĩa vụ giữ bí mật đã viết ở dòng năm của mô hình đe doạ, y từ lịch bảo trì lô thiết bị thật, z từ một dải công bố, rồi cho con số độ trễ và mốc năm phải bắt đầu.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.7` bấm thẻ.
