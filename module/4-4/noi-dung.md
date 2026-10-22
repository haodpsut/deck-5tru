---
tieu-de: An ninh phi mặt đất: GNSS, đường vệ tinh, TT&C
phu-de: Trụ 4 6G Sec · module 4.4
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 78
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

Tôi phân biệt được gây nhiễu, giả mạo và phát lại bằng dấu hiệu quan trắc nào, và cơ chế phát hiện tôi đề xuất cần thêm phần cứng gì?

## Phân loại theo hiệu ứng quan trắc, không theo ý định
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Mô hình đe doạ GNSS tự mâu thuẫn gần như luôn vì một lý do: nó phân loại tấn công theo **ý định của kẻ tấn công** (muốn chặn, muốn lừa) rồi lại đo bằng dấu hiệu của loại khác. Ý định không quan trắc được. Cái quan trắc được là ba thứ: tỉ số công suất sóng mang trên mật độ nhiễu `C/N0`, nghiệm vị trí, và nghiệm thời gian.

## Phân loại theo hiệu ứng quan trắc, không theo ý (tiếp)
@phut: 1
@che-do: noi

Nên module này chỉ làm một việc: xếp ba loại tấn công theo **hiệu ứng trên ba đại lượng đó**, rồi hỏi mỗi dấu hiệu phát hiện cần thêm phần cứng gì. Phần có giá trị nhất không phải danh sách dấu hiệu, mà là **ma trận chỗ trống**: ô nào không dấu hiệu nào phủ được. Chỗ trống đó chính là lập luận chính đáng cho một bài phát hiện đa dấu hiệu, và cũng là chỗ reviewer hỏi đầu tiên.

## Phân loại theo hiệu ứng quan trắc, không theo ý (tiếp)
@phut: 1
@che-do: noi

Một con số đi xuyên cả module: mức công suất thu danh định của tín hiệu dân dụng rất nhỏ, nên kẻ tấn công ở gần không cần công suất lớn. Hệ quả của riêng con số đó đã đủ bẻ hai hiểu sai kinh điển ở cuối module.

## Ba loại tấn công GNSS
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Ba loại tấn công GNSS · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Gây nhiễu:** `C/N0` sụt, AGC nhảy, bộ thu mất bám. Nghiệm vị trí biến mất chứ không sai.

**Giả mạo:** `C/N0` giữ trong dải bình thường, số vệ tinh bám được vẫn đủ, nhưng nghiệm vị trí hoặc nghiệm thời gian lệch khỏi giá trị thật.

## Ba loại tấn công GNSS · đáp (tiếp)
@phut: 1
@che-do: noi

**Phát lại:** giữ gần như bình thường cả `C/N0` lẫn cấu trúc tín hiệu, vì nó phát lại tín hiệu thật. Dấu hiệu đặc trưng là **lệch thời gian tăng dần**, do đường truyền thêm và do trôi của bộ đệm.

## Ba loại tấn công GNSS · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: ba loại này khác nhau ở **cái gì đo được**, không ở ý định. Một bản thảo mô tả tấn công bằng động cơ rồi đo bằng dấu hiệu của loại khác là bản thảo tự mâu thuẫn, và reviewer bắt ở đúng chỗ đó.

## Năm dấu hiệu phát hiện, xếp theo chi phí phần cứng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Năm dấu hiệu phát hiện, xếp theo chi phí phần cứng · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Từ rẻ tới đắt: Bất thường `C/N0` và AGC: chỉ cần đọc trường bộ thu đã in ra. Nhảy bậc của sai lệch đồng hồ: cần một mốc thời gian tương đối ổn định bên trong bộ thu. Nhất quán Doppler với ephemeris: cần quỹ đạo khai báo đáng tin và tính lại Doppler kỳ vọng. Nhất quán giữa nhiều chòm sao: cần bộ thu đa chòm sao. Góc tới bằng nhiều ăng ten:

## Năm dấu hiệu phát hiện, xếp theo chi phí phần (tiếp)
@phut: 1
@che-do: noi

cần dàn ăng ten, biết khoảng cách phần tử, và hiệu chuẩn pha. Đắt nhất, mạnh nhất. Điểm phải nhớ: **thứ tự này là thứ tự chi phí, và nó phải xuất hiện trong bài báo**. Một bài đề xuất dấu hiệu số {{s003}} mà không khai thêm phần cứng đang trộn hai hệ thống khác nhau vào một bảng kết quả.

## Đường TT&C khác đường tải trọng ở chỗ nào
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Đường TT&C khác đường tải trọng ở chỗ nào · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Đường tải trọng chở dữ liệu người dùng; mất bí mật ở đó là mất dữ liệu. Đường **TT&C** (telemetry, tracking and command) chở lệnh điều khiển vệ tinh; mất **tính xác thực** ở đó là mất quyền điều khiển.

## Đường TT&C khác đường tải trọng ở chỗ nào · đáp (tiếp)
@phut: 1
@che-do: noi

Hệ quả về thứ tự ưu tiên, và đây là chỗ nhiều bản thảo viết ngược: trên TT&C, **xác thực lệnh và chống phát lại quan trọng hơn bảo mật nội dung**. Một lệnh bị đọc thì kẻ tấn công biết trạm đang làm gì; một lệnh bị chèn hoặc bị phát lại thì vệ tinh làm theo.

## Đường TT&C khác đường tải trọng ở chỗ nào · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: chống phát lại trên đường lệnh là một cơ chế riêng (bộ đếm đơn điệu, nhãn thời gian, số dùng một lần), **mã hoá không tự cho tính chất đó**. Nếu mô hình đe doạ của anh ghi kẻ tấn công có năng lực chèn và chặn, thì bất kỳ thiết kế nào không có bộ đếm hoặc nhãn thời gian là thiết kế đã bị bác bằng chính mô hình anh khai.

## Vì sao giả mạo khả thi về mặt công suất
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Vì sao giả mạo khả thi về mặt công suất · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mức công suất thu danh định của tín hiệu dân dụng rất nhỏ, còn suy hao không gian tự do thì tăng {{s005}} dB mỗi lần khoảng cách tăng {{s006}} lần. Vệ tinh ở cách hơn hai vạn kilomet; kẻ tấn công ở cách trăm mét. Chênh khoảng cách năm bậc độ lớn cho chênh suy hao khoảng {{s007}} dB.

## Vì sao giả mạo khả thi về mặt công suất · đáp (tiếp)
@phut: 1
@che-do: noi

Hệ quả: **một nguồn công suất rất thấp ở gần vẫn áp đảo**, và điều ngược lại cũng đúng và quan trọng hơn: kẻ tấn công ở gần có thể **hạ công suất xuống cỡ nanowatt** để tín hiệu giả chỉ nhô hơn mức danh định vài dB.

## Vì sao giả mạo khả thi về mặt công suất · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: vì kẻ tấn công điều chỉnh được công suất, **dấu hiệu dựa mức công suất không phải dấu hiệu chống giả mạo**. Nó chống gây nhiễu. Viết ngược chỗ này là hiểu sai kinh điển số một của lĩnh vực.

## Ngân sách công suất của một nguồn giả mạo mặt đất
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`P_thu(dBW) = EIRP(dBW) + G_thu(dBi) − 20·log10(4π·d/λ), với λ = c / f_L1`

**Giả thiết nó đứng trên:**

## Ngân sách công suất của một nguồn giả mạo mặt đất (tiếp)
@phut: 1
@che-do: so

- truyền lan không gian tự do, không che chắn, không đa đường: đây là ràng buộc chặt nhất và nó cho lề LẠC QUAN cho kẻ tấn công ở gần
- ăng ten bộ thu có cùng độ lợi về hướng nguồn giả và về hướng vệ tinh, tức bỏ qua giản đồ hướng, nên con số ra là chặn trên của lề
- λ tính từ tần số sóng mang L1, không gõ tay: λ = c / f_L1

## Ngân sách công suất của một nguồn giả mạo mặt đất (tiếp)
@phut: 1
@che-do: so

- mức so sánh là công suất thu DANH ĐỊNH quy định trong chuẩn, không phải công suất thu đo được tại hiện trường

## Ngân sách công suất của một nguồn giả mạo mặt đất · ghi
@phut: 1
@che-do: noi

Mức danh định là mức tối thiểu mà chuẩn bảo đảm ở đầu ra ăng ten người dùng với điều kiện quy định; công suất thu thật có thể cao hơn. Vì mức này nằm rất sâu dưới sàn nhiệt, bộ thu chỉ lấy lại được tín hiệu sau khi tương quan với mã giả ngẫu nhiên. Đúng tính chất đó làm **giả mạo rẻ**: kẻ tấn công chỉ cần nhô hơn một mức rất thấp, chứ không cần áp đảo một mức cao.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s008}} | dBW | Mức công suất thu tối thiểu quy định cho tín hiệu GPS
!so {{s009}} | MHz | Tần số sóng mang GPS L1

## Một nguồn giả mạo phát 10 mW đẳng hướng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một nguồn giả mạo phát {{s006}} mW đẳng hướng, cách bộ thu {{s007}} m, ăng ten bộ thu {{s011}} dBi. Lề công suất của nó so với mức danh định -158,5 dBW bằng bao nhiêu dB?

ptW = {{s010}}, gr = {{s011}}, d = {{s007}}, fMHz = {{s009}}, pminDbw = {{s008}}

## Một nguồn giả mạo phát 10 mW đẳng hướng · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`10⋆Math.log10(ptW) + gr - 20⋆Math.log10(4⋆Math.PI⋆d/(299792458/(fMHz⋆1e6))) - pminDbw`

Khoảng {{s012}} dB, tức khoảng {{s013}} triệu lần mạnh hơn mức danh định. Con số này lớn tới mức nó đổi chiều lập luận: vấn đề của kẻ tấn công không phải đủ công suất, mà là hạ công suất cho vừa đủ để không lộ ra ở C/N0 và AGC.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một tấn công phát lại chạy qua bộ đệm trôi {{s001}} microgiây mỗi giây. Sau {{s006}} phút, sai lệch thời gian quy ra sai lệch khoảng cách giả bằng bao nhiêu mét?

c = {{s014}}, troi = {{s015}}, t = {{s016}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`c × troi × t`

Khoảng {{s017}} nghìn mét, tức gần {{s017}} km. Con số này lớn hơn mọi sai số truyền lan, sai số đồng hồ hay sai số đa đường của một bộ thu bình thường vài bậc độ lớn, nên lệch thời gian TĂNG DẦN là dấu hiệu đọc được ngay từ nghiệm của chính bộ thu, không cần thêm phần cứng. Đó là lý do nó là dấu hiệu đặc trưng của phát lại.

## Bộ thu báo C/N0 trong dải bình thường
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bộ thu báo C/N0 trong dải bình thường, bám đủ số vệ tinh, nhưng nghiệm vị trí lệch dần khỏi vị trí thật. Hiệu ứng quan trắc này khớp nhất với cái gì?

- Giả mạo
- Che chắn và đa đường trong phố
- Mất ephemeris
- Gây nhiễu băng rộng

## Bộ thu báo C/N0 trong dải bình thường · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Giả mạo**

Gây nhiễu làm C/N0 sụt và thường làm mất bám, nên không khớp. Che chắn và đa đường làm nghiệm nhiễu hơn và C/N0 dao động, nhưng không kéo nghiệm lệch có hướng và tăng dần. Mất ephemeris thì bộ thu không ra nghiệm chứ không ra nghiệm sai. Chỉ giả mạo cho đúng tổ hợp: công suất bình thường, bám bình thường, nghiệm lệch.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Dấu hiệu nào tách được PHÁT LẠI khỏi GIẢ MẠO tự sinh tín hiệu?

- AGC nhảy bậc khi tấn công bắt đầu
- C/N0 sụt dưới ngưỡng
- Lệch thời gian tăng dần theo thời gian quan trắc
- Số vệ tinh bám được giảm

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Lệch thời gian tăng dần theo thời gian quan trắc**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Phát lại chở chính tín hiệu thật nên C/N0, số vệ tinh và cấu trúc mã đều gần bình thường; ba phương án kia đều là dấu hiệu của gây nhiễu hoặc của một bước nhảy khi tấn công bắt đầu, nên chúng không tách phát lại khỏi giả mạo. Chỉ độ trôi của đường truyền thêm và của bộ đệm cho một đại lượng TĂNG DẦN, và đó là chỗ phát lại tự khai ra.

## Trong năm dấu hiệu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong năm dấu hiệu, cái nào đòi thêm phần cứng mà bộ thu thương mại thường không có, nên phải khai trong phần chi phí của bài báo?

- Nhảy bậc của sai lệch đồng hồ
- Bất thường AGC
- Nhất quán giữa nhiều chòm sao
- Góc tới bằng nhiều ăng ten

## Trong năm dấu hiệu · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Góc tới bằng nhiều ăng ten**

AGC và sai lệch đồng hồ đọc được từ trường mà bộ thu đã in ra. Nhất quán nhiều chòm sao cần bộ thu đa chòm sao, và phần lớn bộ thu hiện nay đã đa chòm sao nên chi phí thêm gần bằng không. Góc tới cần dàn ăng ten, biết khoảng cách phần tử và hiệu chuẩn pha, nên nó là dấu hiệu duy nhất đổi hẳn phần cứng của hệ.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đánh giá sau có một câu làm toàn bộ phần so sánh không so được với bài giả mạo nào khác. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi dựng kịch bản giả mạo bằng một nguồn mặt đất phát lại cấu trúc tín hiệu L1 C/A, đặt cách bộ thu {{s018}} m,
- giữ công suất thu của tín hiệu giả cao hơn mức danh định khoảng {{s004}} dB để bộ thu bám được mà C/N0 vẫn trong dải bình thường,
- và báo hiệu năng phát hiện theo tỉ số nhiễu trên tín hiệu J/S, giống như với tấn công gây nhiễu.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và báo hiệu năng phát hiện theo tỉ số nhiễu trên tín hiệu J/S, giống như với tấn công gây nhiễu.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

J/S là trục của GÂY NHIỄU: nó giả định kẻ tấn công thêm công suất không mang tin, nên hiệu năng đo theo J/S nói về khả năng chịu nhiễu. Giả mạo thì phát tín hiệu hợp lệ về cấu trúc, và câu thứ hai của chính đoạn này đã khai lề chỉ {{s004}} dB, tức chủ ý giữ C/N0 bình thường. Hai câu đầu đều hợp lệ. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

vẽ hiệu năng theo lề công suất của tín hiệu giả tính bằng dB so với mức danh định, theo độ lệch nghiệm vị trí, hoặc theo tốc độ lệch thời gian, và khai rõ kẻ tấn công có thích ứng với bộ phát hiện hay không.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết lập sau có một câu làm một trong ba dấu hiệu đã khai không thể chạy được. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Bộ phát hiện đề xuất hợp ba dấu hiệu: bất thường C/N0, nhất quán Doppler với ephemeris, và góc tới của tín hiệu.
- Thực nghiệm chạy trên bản ghi IQ của một bộ thu thương mại một ăng ten, lấy tại hai địa điểm trong ba ngày,
- và so với ba đường cơ sở ở cùng tỉ lệ cảnh báo sai.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Thực nghiệm chạy trên bản ghi IQ của một bộ thu thương mại một ăng ten, lấy tại hai địa điểm trong ba ngày,**

Góc tới không tính được từ một ăng ten đơn: nó cần tối thiểu hai phần tử, biết khoảng cách giữa chúng và hiệu chuẩn pha. Câu đầu khai ba dấu hiệu trong đó dấu hiệu mạnh nhất đòi dàn ăng ten, còn câu này nói dữ liệu chỉ có một kênh.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Vậy hoặc phần góc tới không thật sự chạy, hoặc nó chạy trên một bộ dữ liệu khác với hai dấu hiệu kia và kết quả hợp ba dấu hiệu là kết quả ghép từ hai hệ. Câu thứ ba thì hợp lệ và đúng chuẩn so sánh. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

khai số phần tử ăng ten và khoảng cách phần tử trong phần thiết lập, và nếu không có dàn ăng ten thì bỏ góc tới khỏi danh sách đóng góp thay vì để nó trong bảng.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Lấy mức công suất thu danh định P_min của tín hiệu dân dụng làm mốc so sánh
- Tính bước sóng từ tần số sóng mang: λ = c / f_L1
- Viết suy hao không gian tự do ở khoảng cách d: L(d) = 20·log10(4π·d/λ)
- Lề của nguồn giả mạo: M(d) = EIRP − L(d) − P_min, tính bằng dB
- Đảo quan hệ: khoảng cách mà nguồn ngang mức danh định là d_eq = (λ/4π)·10^((EIRP − P_min)/20)

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Đọc hai chiều: ở d nhỏ thì M(d) rất dương, nên kẻ tấn công PHẢI hạ công suất để không lộ; đó là lý do dấu hiệu dựa công suất không bắt được giả mạo

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Gây nhiễu: bắt được bằng C/N0 và AGC · Giả mạo: bắt được bằng nhất quán Doppler, nhất quán nhiều chòm sao, góc tới · Phát lại: bắt được bằng nhảy bậc đồng hồ và lệch thời gian tăng dần

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Có dàn nhiều ăng ten, biết khoảng cách phần tử, hiệu chuẩn pha** tắt đi: Chỉ có một ăng ten, như mọi bộ thu thương mại và mọi bản ghi IQ một kênh.
- **Bộ thu có mốc thời gian riêng tương đối ổn định** tắt đi: Đồng hồ bộ thu rẻ, trôi mạnh, và mọi mốc thời gian đều lấy lại từ chính nghiệm GNSS.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Kẻ tấn công không biết bộ phát hiện của tôi** tắt đi: Kẻ tấn công đọc bài báo của tôi, nên nó hạ công suất cho khớp dải C/N0 và AGC bình thường, và dựng Doppler nhất quán với ephemeris công khai.
- **Có ephemeris đúng và đáng tin để đối chiếu** tắt đi: Ephemeris lấy từ chính tín hiệu đang bị tấn công, hoặc từ một nguồn hỗ trợ cũng do kẻ tấn công kiểm soát.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mức công suất thu tối thiểu mà đặc tả giao diện GPS bảo đảm cho tín hiệu L1 C/A là −158,5 dBW.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỨNG**

ĐỨNG, và đây là con số nên nhớ vì nó là điểm tựa của mọi lập luận về giả mạo tín hiệu. Table 3-V của đặc tả giao diện in mức thu tối thiểu cho khối II/IIA/IIR: trên L1, P(Y) là −161,5 dBW và C/A là −158,5 dBW; trên L2 là −164,5 dBW.

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

Vì đây là mức SÀN bảo đảm ở mặt đất, một máy phát giả chỉ cần vượt sàn đó vài dB là đã lấn được, nên khoảng cách công suất chứ không phải thuật toán là chỗ phải bảo vệ.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ngân sách công suất của một nguồn giả mạo mặt đất, so với mức công suất thu danh định của L1 C/A. Kéo công suất phát và khoảng cách, đọc lề bằng dB và số lần mạnh hơn mức danh định.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.4` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V claims the proposed detector separates spoofing from jamming, yet Table III reports detection performance against J/S only. Since a spoofer controls its own transmit power and your own link budget in Section III shows a {{s012}} dB margin at {{s007}} m, the attacker can lower power until C/N0 and AGC stay nominal. Please state the attacker power model and the observable on which detection performance is reported.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree, and we have separated the two attack classes. Table III now reports jamming resistance against J/S and spoofing detection against the power margin of the counterfeit signal relative to the specified minimum received power, which is the quantity the attacker actually controls. Section III-B states the attacker power model explicitly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

an adjustable ground source at {{s005}} m to {{s002}} km with EIRP from -60 dBm to {{s005}} dBm, which covers the regime in which the counterfeit signal exceeds the specified minimum by only {{s004}} dB and therefore leaves C/N0 and AGC within their nominal range. Figure {{s019}} adds an adaptive attacker that knows the detector and selects the lowest power that still achieves lock.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Under that attacker the power based features fall to near chance, detection rests on multi constellation consistency, and the angle of arrival feature is reported separately because it requires a two element array, which we now state in Table I as an added hardware cost.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: trả lời rằng J/S là trục phổ biến trong tài liệu chống nhiễu. Đúng về thực hành, nhưng không chạm vào phản bác, vì phản bác nói chính trục đó là trục của loại tấn công khác.
- Mức {{s002}}: đổi trục sang lề công suất của tín hiệu giả, nhưng vẫn để kẻ tấn công ở một mức công suất cố định, nên phần đánh giá vẫn đo trên kẻ tấn công không thích ứng mà không nói ra.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai mô hình năng lực kẻ tấn công gồm dải công suất điều chỉnh được, vẽ hiệu năng theo lề công suất trong dải đó, và tách bảng kết quả thành gây nhiễu và giả mạo với hai trục khác nhau.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The threat model in Section II grants the adversary the ability to inject and to block messages on the TT&C link, but the proposed command protection in Section IV provides only encryption of the command payload. Please explain how your design resists replay of a previously valid command under the stated threat model.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The threat model grants injection and blocking, so confidentiality alone does not meet it and we have corrected Section IV. Command authenticity now rests on a message authentication code computed over the command, a monotonic command counter, and a coarse timestamp, all inside the authenticated input. The spacecraft stores the highest accepted counter in non volatile memory and rejects any command whose counter is not strictly greater, which removes replay of previously valid commands.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Because the adversary may also block, a withheld command can be delivered late, so Section IV-C states the acceptance window of {{s020}} seconds and the resynchronisation procedure used after a reboot or after a loss of contact, in which the station performs a challenge based counter resynchronisation rather than accepting a lower counter. Table V reports the operational cost of the window: shrinking it below {{s006}} seconds causes measurable command loss at low elevation passes.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: trả lời rằng lệnh đã được mã hoá nên kẻ tấn công không đọc được nội dung. Không chạm vào phản bác: phát lại không cần đọc nội dung.
- Mức {{s002}}: thêm kiểm tra toàn vẹn hoặc mã xác thực thông điệp, nhưng vẫn không có đại lượng biến đổi theo thời gian, nên một lệnh hợp lệ cũ vẫn qua được.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: thêm bộ đếm đơn điệu hoặc nhãn thời gian vào phần được xác thực, khai cửa sổ chấp nhận, và nói rõ trạng thái bộ đếm giữ ở đâu trên vệ tinh.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.4` bấm thẻ.
