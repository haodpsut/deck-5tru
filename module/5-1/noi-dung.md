---
tieu-de: Vì sao và khi nào phải đổi
phu-de: Trụ 5 PQC · module 5.1
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 68.5
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

Với dữ liệu của tôi, bất đẳng thức Mosca đang nói tôi đã trễ hay chưa, và Grover có là lý do để đổi khoá đối xứng không?

## Hai đường đe doạ
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này tách hai thứ hay bị trộn. **Shor** giải bài toán phân tích số và logarit rời rạc trong thời gian đa thức, nên RSA, Diffie-Hellman trên trường hữu hạn, ECDH và ECDSA **đổ hẳn**, không phải yếu đi. **Grover** chỉ cho tăng tốc bậc căn, và tăng tốc đó tuần tự theo bản chất nên khó song song hoá; vì thế NIST vẫn xếp AES-128 ở mức an toàn thấp nhất chứ không coi nó bị phá.

## Hai đường đe doạ (tiếp)
@phut: 1
@che-do: noi

Điểm phải mang theo khi viết phần động lực: **lý do đổi hệ là khoá công khai, không phải khoá đối xứng**. Và thời điểm phải đổi không ra từ toán học mà ra từ ba con số của bất đẳng thức Mosca, trong đó đúng một con số là chỗ mọi tranh luận diễn ra.

## Bất đẳng thức Mosca
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Bất đẳng thức Mosca · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ba đại lượng: `x` là số năm dữ liệu còn cần giữ mật, `y` là số năm cần để di trú xong, `z` là số năm cho tới khi có máy lượng tử đủ sức. Nếu `x + y > z` thì đã trễ.

## Bất đẳng thức Mosca · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: hai vế không cùng hạng về độ tin cậy. `x` và `y` là đại lượng của **hệ của anh**, đo được bằng kiểm kê. `z` là **ước lượng về thế giới**, nên mọi kết luận rút ra phải viết ở dạng điều kiện theo `z`.

## Thu hoạch bây giờ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Thu hoạch bây giờ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Kẻ tấn công chỉ cần **lưu** bản mã hôm nay và đợi tới khi có máy giải. Không cần máy lượng tử ở thời điểm thu.

Điểm phải nhớ: đây là lý do câu "máy lượng tử chưa có nên chưa cần đổi" không đứng được với mọi dữ liệu có `x` lớn. Tấn công đã bắt đầu rồi, và nó bắt đầu ở phía kẻ tấn công nên anh không quan sát được.

## Shor đổ hẳn, Grover chỉ rút ngắn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Shor đổ hẳn, Grover chỉ rút ngắn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Shor: thời gian đa thức cho phân tích số và logarit rời rạc, nên mọi hệ khoá công khai đang dùng rộng rãi mất nền tảng độ khó. Grover: số truy vấn bậc `2^(n/2)` để tìm khoá đối xứng `n` bit, tức rút mũ đi một nửa.

## Shor đổ hẳn, Grover chỉ rút ngắn · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: tăng tốc của Grover **tuần tự theo bản chất**, chia cho máy song song chỉ được lợi theo căn của số máy, nên chi phí thật vẫn ngoài tầm. Hệ quả: khoá đối xứng là vấn đề về lề an toàn, khoá công khai là vấn đề về sự tồn tại.

## z là nơi tranh luận, không phải toán học
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## z là nơi tranh luận, không phải toán học · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bất đẳng thức Mosca là một phép trừ. Không ai phản bác phép trừ. Mọi phản biện về động lực của một bài PQC đều rơi vào giá trị của `z`, hoặc vào việc tác giả dùng một giá trị `z` điểm mà không khai độ bất định.

## z là nơi tranh luận, không phải toán học · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: cách viết miễn nhiễm là **phát biểu có điều kiện cộng một vùng tham số**. Thay vì "chúng tôi đã trễ", viết "với `x = {{s004}}` và `y = {{s005}}`, việc di trú đã trễ với mọi `z` nhỏ hơn {{s006}} năm". Reviewer không bác được phát biểu đó, vì nó không đòi anh biết `z`.

## Bất đẳng thức Mosca, và bậc truy vấn của Grover
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Đã trễ khi x + y > z Grover: số truy vấn bậc 2^(n/2) cho khoá đối xứng n bit Dạng điều kiện: đã trễ với mọi z nhỏ hơn (x + y)`

**Giả thiết nó đứng trên:**

## Bất đẳng thức Mosca, và bậc truy vấn của Grover (tiếp)
@phut: 1
@che-do: so

- x đo bằng nghĩa vụ bảo mật của dữ liệu, không bằng vòng đời thiết bị
- y là thời gian di trú xong toàn bộ nơi dùng mật mã, kể cả hệ đã bàn giao, nên nó đo được bằng kiểm kê chứ không ước bằng cảm tính
- z là ước lượng về thế giới bên ngoài, nên nó mang độ bất định và kết luận phải viết ở dạng điều kiện theo z

## Bất đẳng thức Mosca, và bậc truy vấn của Grover (tiếp)
@phut: 1
@che-do: so

- Grover giả thiết truy cập hộp đen tới hàm kiểm khoá, và số truy vấn bậc căn là tối ưu, nên không có cải tiến thuật toán nào đẩy nó xuống thấp hơn
- Tăng tốc của Grover tuần tự theo bản chất: chia việc cho M máy chỉ được lợi theo căn của M

## Bất đẳng thức Mosca, và bậc truy vấn của Grover · ghi
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hai dạng viết cho cùng một bất đẳng thức. Dạng **khẳng định** (đã trễ) cần biết `z`. Dạng **điều kiện** (đã trễ với mọi `z` nhỏ hơn `x + y`) không cần biết `z`, và đó là dạng nên dùng trong bài báo. Chúng nói cùng một điều, nhưng chỉ một trong hai bác được bằng cách bác ước lượng `z` của anh.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s007}} | bit, dạng số mũ của {{s002}} | Grover cho tăng tốc bậc căn
!so {{s008}} | bit, dạng số mũ của {{s002}} | Cùng công thức đó

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hồ sơ bệnh án phải giữ mật x = {{s004}} năm. Kế hoạch di trú của anh dài y = {{s005}} năm. Anh dùng ước lượng z = {{s009}} năm. Chênh Mosca bằng bao nhiêu năm?

x = {{s004}}, y = {{s005}}, z = {{s009}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`x + y - z`

{{s010}} năm, dương và lớn, tức đã trễ {{s010}} năm theo ước lượng này. Để ý điều quan trọng hơn con số: x + y = {{s006}}, nên dấu của chênh giữ nguyên với mọi z nhỏ hơn {{s006}} năm. Vì thế phát biểu nên viết là đã trễ với mọi z nhỏ hơn {{s006}} năm, và lúc đó nó không cần tới ước lượng z = {{s009}} nữa.

## Vẫn z = 20 năm và y = 7 năm
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Vẫn z = {{s009}} năm và y = {{s005}} năm, lấy mốc hiện tại là {{s011}}. Năm muộn nhất phải bắt đầu di trú là năm nào?

z = {{s009}}, y = {{s005}}

## Vẫn z = 20 năm và y = 7 năm · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s011}} + z - y`

Năm {{s012}}. Nhưng con số này chỉ nói về việc kịp trước z, nó không chứa x. Với x = {{s004}} thì chênh Mosca đã dương {{s010}} năm, nên {{s012}} là một mốc muộn tới mức vô nghĩa: bản mã thu hoạch hôm nay đã nằm ngoài tầm bảo vệ từ trước. Hai con số này phải đọc cùng nhau, và chỉ chênh Mosca mới trả lời được câu đã trễ hay chưa.

## Hệ nào Shor làm đổ hẳn, chứ không chỉ làm yếu đi?
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hệ nào Shor làm đổ hẳn, chứ không chỉ làm yếu đi?

- HMAC và các hàm dẫn xuất khoá dựa băm
- AES-128 và AES-256
- SHA-256 và SHA-3
- RSA, Diffie-Hellman trên trường hữu hạn, ECDH và ECDSA

## Hệ nào Shor làm đổ hẳn, chứ không chỉ làm yếu đi? · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**RSA, Diffie-Hellman trên trường hữu hạn, ECDH và ECDSA**

Shor giải phân tích số và logarit rời rạc trong thời gian đa thức, và cả bốn hệ ở đáp án đúng đều lấy một trong hai bài toán đó làm nền tảng độ khó. Ba đáp án kia là đối xứng hoặc dựa băm: chúng chỉ chịu tăng tốc bậc căn của Grover, tức mất một nửa số mũ, nên bị thu hẹp lề an toàn chứ không mất nền tảng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Vì sao NIST vẫn xếp AES-128 ở mức an toàn thấp nhất chứ không coi nó là bị phá?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Vì Grover chỉ áp dụng được cho khoá dài hơn {{s008}} bit
- Vì tăng tốc của Grover là bậc căn và tuần tự theo bản chất, nên khó song song hoá và chi phí thật vẫn ngoài tầm
- Vì AES không phải hệ khoá công khai nên không máy lượng tử nào chạm tới được
- Vì NIST chưa cập nhật tiêu chí cho khoá đối xứng

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Vì tăng tốc của Grover là bậc căn và tuần tự theo bản chất, nên khó song song hoá và chi phí thật vẫn ngoài tầm**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Bậc {{s002}} luỹ thừa {{s007}} truy vấn là con số bé nếu các truy vấn chạy song song được, nhưng Grover tuần tự theo bản chất: chia việc cho M máy chỉ được lợi theo căn của M, nên phải chạy một mạch rất dài trên một máy có độ mạch sâu tương ứng. Đáp án thứ ba sai vì Grover áp được cho AES, chỉ là nó không phá được.

## Trong một bài PQC
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong một bài PQC, phần lớn tranh luận của phản biện về động lực rơi vào đại lượng nào của bất đẳng thức Mosca?

- z, số năm cho tới khi có máy lượng tử đủ sức
- Không đại lượng nào, vì bất đẳng thức là toán học thuần
- x, số năm dữ liệu còn cần giữ mật
- y, số năm di trú

## Trong một bài PQC · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**z, số năm cho tới khi có máy lượng tử đủ sức**

x và y là đại lượng của hệ anh, đo được và bác được bằng cách đòi bản kiểm kê. z là ước lượng về thế giới, không ai có số thật, nên nó là chỗ duy nhất phản biện có thể đứng mà không cần dữ liệu. Cách rút chỗ đứng đó khỏi họ là viết kết luận ở dạng điều kiện theo z.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mở đầu sau có một câu lẫn khái niệm. Bấm vào câu đó.

- Máy tính lượng tử đe doạ mật mã đang triển khai theo hai đường khác nhau.
- Shor giải phân tích số và logarit rời rạc trong thời gian đa thức, nên RSA và ECC mất nền tảng độ khó.
- Grover hạ an toàn của AES-128 xuống {{s007}} bit, nên việc cấp thiết nhất là nâng mọi khoá đối xứng lên AES-256.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Grover hạ an toàn của AES-128 xuống {{s007}} bit, nên việc cấp thiết nhất là nâng mọi khoá đối xứng lên AES-256.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai chuyện bị trộn. Thứ nhất, con số {{s007}} bit là số mũ truy vấn, và vì tăng tốc của Grover tuần tự theo bản chất nên chi phí thật của {{s002}} luỹ thừa {{s007}} truy vấn tuần tự vẫn ngoài tầm. Chính vì thế NIST vẫn xếp AES-128 ở mức an toàn thấp nhất chứ không coi nó bị phá. Thứ hai, chữ cấp thiết nhất đặt sai chỗ:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

hệ khoá công khai mất nền tảng tồn tại, khoá đối xứng chỉ mất lề. Cách sửa: giữ câu về Grover như một ghi chú về lề an toàn, rồi nói rõ lý do đổi hệ là khoá công khai.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn trả lời phản biện sau có một câu không đứng được. Bấm vào câu đó.

- Chúng tôi đồng ý rằng máy lượng tử đủ sức chưa tồn tại ở thời điểm viết.
- Vì thế hệ của chúng tôi chưa cần hệ khoá công khai hậu lượng tử ở thời điểm này.
- Chúng tôi dự kiến đánh giá lại khi có khuyến nghị mới của cơ quan chuẩn hoá.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì thế hệ của chúng tôi chưa cần hệ khoá công khai hậu lượng tử ở thời điểm này.**

Câu này bỏ qua thu hoạch bây giờ giải mã sau. Kẻ tấn công chỉ cần lưu bản mã hôm nay, nên đồng hồ của x chạy từ bây giờ chứ không chạy từ lúc máy xuất hiện. Điều kiện đúng là x cộng y so với z, và với x lớn thì chênh đã dương từ trước. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

thay câu này bằng một phát biểu có điều kiện trên x, ví dụ với dữ liệu đo lường hết giá trị trong một giờ thì x gần bằng {{s013}} nên chênh âm với mọi z hợp lý, trong khi với khoá gốc nạp một lần thì x bằng vòng đời thiết bị và kết luận đảo chiều.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt x = số năm tập dữ liệu này còn phải giữ mật kể từ hôm nay
- Đặt y = số năm để di trú xong mọi nơi dùng mật mã trong hệ, lấy từ kiểm kê
- Đặt z = số năm cho tới khi có máy lượng tử đủ sức, kèm dải bất định
- Dữ liệu còn trong tầm bảo vệ khi và chỉ khi x + y ≤ z

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Năm muộn nhất phải bắt đầu di trú = năm hiện tại + z − y, và nếu x + y > z thì mốc đó đã ở quá khứ

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: x = {{s014}} năm · y = {{s015}} năm · z = {{s016}} năm · chênh Mosca {{s013}} năm, đúng ở biên · năm muộn nhất phải bắt đầu di trú {{s017}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biết z, tức có một ước lượng điểm cho thời điểm có máy lượng tử đủ sức** tắt đi: z chỉ biết nằm trong một dải rộng, hoặc không biết gì.
- **Kẻ tấn công lưu được bản mã hôm nay để giải mã sau** tắt đi: Không có kênh lưu trữ dài hạn, hoặc dữ liệu chỉ có giá trị trong phiên.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **y đo được từ kiểm kê nơi dùng mật mã** tắt đi: Chưa kiểm kê, nên y là phỏng đoán của người viết bài.
- **Mối đe doạ duy nhất là máy lượng tử** tắt đi: Có lỗi cài đặt, kênh phụ, sinh số ngẫu nhiên yếu, hoặc khoá bị lộ theo đường quản trị.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ba thanh cho ba đại lượng Mosca. Để ý một chuyện: chỉ có thanh z là ước lượng về thế giới, hai thanh kia là đại lượng của hệ anh. Đầu ra cuối cùng cho biết kết luận của anh có phụ thuộc z hay không.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.1` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section I motivates the entire contribution by asserting that quantum computers will break the deployed key exchange, but the paper gives no timeline, no threat model, and no statement of how long the protected data must stay confidential. As written, the urgency claim is not falsifiable. Please justify it quantitatively or soften it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have rewritten the motivation as a conditional statement, so that it no longer depends on any point estimate of the quantum timeline. Section I-A now applies the Mosca inequality with the two quantities we can actually measure. For the device root keys in our deployment, the confidentiality lifetime is x = {{s009}} years (device service life, Table I) and the migration time is y = {{s005}} years (from the cryptographic inventory in Appendix A, {{s018}} call sites in {{s003}} firmware images).

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We therefore state: migration is already late for every z below {{s019}} years. We make no claim about the value of z. For the telemetry payloads in the same system, x is under one hour, so the inequality is satisfied for any plausible z, and we say so explicitly rather than treating the whole system as one class. We also state the mechanism that starts the clock now:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

an adversary only needs to store ciphertext today, so the x clock runs from deployment, not from the arrival of a cryptanalytic machine. Finally, Section II-D lists what our threat model excludes: side channels, weak randomness, and key compromise through administrative channels, any of which would dominate the quantum risk if present.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: dẫn thêm tài liệu nói máy lượng tử là mối đe doạ, và dẫn mốc của một cơ quan chuẩn hoá. Đúng về bối cảnh nhưng vẫn là phát biểu khẳng định phụ thuộc một ước lượng z mà phản biện bác được ngay.
- Mức {{s002}}: nêu bất đẳng thức Mosca và điền một bộ ba số, kèm trích dẫn cho z. Đã định lượng, nhưng toàn bộ kết luận vẫn treo trên một giá trị z điểm.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: viết kết luận ở dạng điều kiện theo z, tức phát biểu đã trễ với mọi z nhỏ hơn x cộng y, và khai x cùng y lấy từ đâu. Lúc này phản biện không bác được bằng cách bác z.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The authors invoke Grover's algorithm to justify upgrading the symmetric cipher from AES-128 to AES-256, and present this as the primary quantum countermeasure. This conflates the asymmetric and the symmetric risk. Please clarify why the symmetric primitive needs to change at all, and what the actual driver of the redesign is.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have separated the two risks. Shor's algorithm removes the hardness assumption that RSA, finite field Diffie-Hellman, ECDH and ECDSA rest on, so the public key layer faces an existence problem and must be replaced. Grover's algorithm reduces the query exponent for an n-bit symmetric key to n/2, so AES-128 faces a margin problem, not an existence problem. We now make the margin argument explicit rather than assert urgency:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Grover's speedup is inherently sequential, distributing the search across M machines gains only a factor of the square root of M, so the cost of a sequential search of that depth remains out of reach, which is why NIST still places AES-128 at the lowest security category rather than treating it as broken.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Accordingly, Section III now presents the public key replacement as the contribution, and the move to AES-256 appears in Section VI-B as an optional margin choice for the subset of data whose confidentiality lifetime exceeds twenty years, with its measured cost stated in Table VII. We also verify that the main result of the paper is unchanged if AES-128 is retained, which separates the contribution from the margin choice.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: nhận rằng Grover chỉ cho tăng tốc bậc căn, nhưng vẫn giữ việc nâng AES làm biện pháp chính. Chưa tách được hai loại rủi ro.
- Mức {{s002}}: tách đúng hai loại rủi ro và nói lý do đổi hệ là khoá công khai, nhưng không giải thích vì sao bậc {{s002}} luỹ thừa {{s007}} vẫn ngoài tầm, nên phản biện còn chỗ đánh.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: nói rõ Shor làm hệ khoá công khai mất nền tảng tồn tại còn Grover chỉ thu hẹp lề, nêu được tính tuần tự theo bản chất của Grover và hệ quả là chia cho M máy chỉ lợi theo căn của M, và chuyển việc nâng AES thành một ghi chú về lề an toàn chứ không phải biện pháp chính.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.1` bấm thẻ.
