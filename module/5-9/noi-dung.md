---
tieu-de: Họ không phải lattice, và ca SIKE chết trong một buổi chiều
phu-de: Trụ 5 PQC · module 5.9
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 87.5
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

Nếu lattice gãy ngày mai thì tôi còn gì, và bài học từ SIKE nói gì về cách tôi nên viết câu khẳng định độ an toàn?

## Nếu lattice gãy ngày mai thì anh còn gì
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Bảy module trước của trụ này chỉ dạy lattice, nên chúng không trả lời được câu hỏi đắt nhất của cả lĩnh vực: **nếu giả định nền gãy thì sao**. Module này làm ba việc. Thứ nhất, bốn họ giả định và đánh đổi của từng họ. Thứ hai, vì sao đa dạng họ là một **yêu cầu kỹ thuật** đo được chứ không phải một lời khuyên thận trọng mơ hồ.

## Nếu lattice gãy ngày mai thì anh còn gì (tiếp)
@phut: 1
@che-do: noi

Thứ ba, bài học của ca SIKE, và nó không phải bài học mà đa số người ta rút ra.

Trục chính là **rủi ro tương quan (correlated risk)**. Hai hệ cùng một họ giả định không cho hai lần bảo vệ, vì một kết quả toán học về bài toán nền giết cả hai trong cùng một buổi chiều. Đây đúng là bài học "đa nhà cung cấp không cho lỗi độc lập" đã có trong sổ của nhà, chuyển sang mật mã.

## Nếu lattice gãy ngày mai thì anh còn gì (tiếp)
@phut: 1
@che-do: noi

**Cảnh báo về trạng thái số:** đặc tả của module này có ba dòng đánh dấu không chắc, là thời gian hồi phục khoá SIKEp434 trên một nhân, khoá công khai Classic McEliece ở mức thấp nhất, và khoá công khai HQC ở mức {{s001}} bit. **Cả ba đã bị bỏ**, không lên thẻ nào. Sự kiện và năm của ca SIKE thì chắc, nên chúng ở lại; con số thời gian cụ thể thì phải mở chính bài ra mới được viết.

## Bốn họ giả định và đánh đổi của từng họ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Bốn họ giả định và đánh đổi của từng họ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Lưới:** khoá nhỏ, chữ ký trung bình, tính nhanh, nhưng giả định mới. **Dựa mã:** khoá công khai rất lớn, giả định rất cũ, đã bị soi từ thập niên {{s003}}. **Dựa hàm băm:** khoá rất nhỏ, chữ ký rất lớn, giả định an toàn nhất vì chỉ cần một hàm băm bền. **Đa biến và isogeny:** đa số các hệ cụ thể đã bị phá.

## Bốn họ giả định và đánh đổi của từng họ · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: ba trục đánh đổi là **kích thước**, **tuổi của giả định**, và **chi phí tính**, và không họ nào tốt theo cả ba trục. Nên câu hỏi đúng không phải họ nào tốt nhất mà là **trục nào đang ràng buộc thiết kế của tôi**. Với mạng IoT trên liên kết chật thì trục ràng buộc là kích thước, và đó chính là lý do lưới thắng ở đó dù giả định của nó mới nhất.

## Rủi ro tương quan, không phải rủi ro cộng dồn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Rủi ro tương quan, không phải rủi ro cộng dồn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ghép hai hệ lại không nhân đôi độ an toàn nếu hai hệ đứng trên cùng một họ giả định. Rủi ro cần phòng ở đây là rủi ro **giả định gãy**, không phải rủi ro một cài đặt có lỗi. Một kết quả mới về bài toán trên lưới giết mọi hệ dựng trên bài toán đó trong cùng một ngày, nên hai thành phần lưới cho đúng **một** lần bảo vệ.

## Rủi ro tương quan, không phải rủi ro cộng dồn · (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đây là cùng một lớp lỗi với "đa nhà cung cấp không cho lỗi độc lập". Phép đo đúng không phải số hệ mà là **số họ giả định khác nhau**. Hệ quả cho thiết kế: muốn hai lớp thật thì thành phần thứ hai phải ở họ khác, và phải khai rõ họ nào, chứ không chỉ khai tên hệ.

## Ca SIKE, và bài học KHÔNG phải cái người ta hay rút
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Ca SIKE, và bài học KHÔNG phải cái người ta hay rút ·
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

SIKE là một KEM dựa isogeny, đi tới vòng bốn của tiến trình chuẩn hoá NIST. Năm {{s005}}, tấn công của Castryck và Decru hồi phục được khoá bí mật bằng máy tính thông thường.

## Ca SIKE, và bài học KHÔNG phải cái người ta hay (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: bài học **không** phải "isogeny yếu". Bài học là **một giả định toán học mới có thể mất toàn bộ độ an toàn trong một bước chứ không suy giảm dần**, và chuyện đó xảy ra sau nhiều năm bị cả cộng đồng soi. Hai hệ quả:

## Ca SIKE, và bài học KHÔNG phải cái người ta hay (tiếp)
@phut: 1
@che-do: noi

thứ nhất, lập luận "soi thêm vài năm nữa rồi hãy chuẩn hoá" không giải quyết được gì, vì SIKE đã được soi nhiều năm; thứ hai, lưới cũng là một họ giả định mới, nên lập luận này áp cho cả lưới chứ không chỉ cho isogeny.

## Ca SIKE, và bài học KHÔNG phải cái người ta hay (tiếp)
@phut: 1
@che-do: noi

Về con số: năm {{s005}} và sự kiện thì chắc. **Thời gian hồi phục khoá cụ thể thì đừng nhớ**, phải mở chính bài ra và ghi rõ bộ tham số cùng phần cứng, nếu không thì bỏ con số đó khỏi câu.

## Câu an toàn x bit phải kèm hai thứ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s006}} trên bốn.*

## Câu an toàn x bit phải kèm hai thứ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một mức an toàn (security level) luôn là phát biểu **có điều kiện**, nên nó phải kèm **giả định nào** và **mô hình chi phí nào**. Thiếu một trong hai thì con số không kiểm được, và đó đúng là lỗi đã nêu ở module {{s007}}.

## Câu an toàn x bit phải kèm hai thứ · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: cái mất đi khi SIKE chết **không phải vài bit mà là cả giả định**. Nên con số bit chỉ có nghĩa bên trong một giả định đã khai, và một bảng mức an toàn không khai giả định là một bảng không chuyển được sang quyết định kỹ thuật. Cách viết đứng được: nêu bài toán nền, nêu phép quy đổi chi phí đã dùng, rồi mới nêu số bit, và nêu luôn kế hoạch nếu giả định đó mất.

## Công thức và giả thiết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`n_hiệu dụng = {{s002}} + (n − 1)·(1 − c) P_mất hết = p^(n_hiệu dụng) tỉ số tự lừa = p^(n_hiệu dụng) / p^n`

**Giả thiết nó đứng trên:**

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- p là xác suất một HỌ giả định gãy trong cửa sổ thời gian (time window) đang xét, không phải xác suất một cài đặt có lỗi
- c là tỉ lệ hệ dùng chung một họ giả định: c = {{s008}} là n họ khác nhau, c = {{s002}} là tất cả cùng một họ

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- hai hệ cùng họ gãy cùng lúc hoàn toàn, tức tương quan nhận đúng hai giá trị {{s008}} hoặc {{s002}} ở mức họ, không có mức trung gian thật
- hybrid được ghép sao cho kẻ tấn công phải phá MỌI thành phần mới đọc được, không phải một trong số đó

## Công thức · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

**Khai rõ:** `n_hiệu dụng` là một phép nội suy tuyến tính giữa hai ca tính được bằng tay, không phải kết quả lấy từ một bài báo. Nó dùng để dạy CHIỀU biến thiên và bậc độ lớn, không dùng để báo số trong bản thảo. Hai ca biên là chỗ duy nhất trong công thức này mà anh được phép tin: `c = {{s008}}` cho `p^n`, và `c = {{s002}}` cho `p`.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} | họ | Sau vòng chuẩn hoá của NIST
!so {{s005}} | năm | Tấn công của Castryck và Decru hồi phục khoá SIKE được công
!so {{s009}} | byte | Họ dựa hàm băm có chữ ký rất lớn

## Ba hệ dùng song song
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Ba hệ dùng song song, một nửa trong số đó chung một họ giả định nên c = {{s012}}, mỗi họ gãy với xác suất {{s013}} trong {{s014}} năm. Xác suất mất hết an toàn là bao nhiêu phần trăm?

p = {{s010}}, n = {{s006}}, c = {{s011}}

## Ba hệ dùng song song · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s015}} × Math.pow(p, {{s002}} + (n - {{s002}}) × ({{s002}} - c))`

Đúng {{s016}}. Nếu nhân ba xác suất với nhau theo giả định độc lập thì ra {{s017}}, tức thấp hơn mười lần. Con số {{s016}} mới là con số phải đặt vào phần phân tích rủi ro, và đại lượng phải báo kèm là số lớp độc lập, ở đây bằng {{s004}}, chứ không phải số hệ bằng {{s006}}.

## Cùng cấu hình đó: ba hệ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cùng cấu hình đó: ba hệ, c = {{s012}}, mỗi họ gãy với xác suất {{s013}}. Rủi ro thật lớn gấp bao nhiêu lần con số tính theo giả định độc lập?

p = {{s010}}, n = {{s006}}, c = {{s011}}

## Cùng cấu hình đó: ba hệ · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.pow(p, {{s002}} + (n - {{s002}}) × ({{s002}} - c)) / Math.pow(p, n)`

Đúng {{s014}} lần. Đây là mức tự lừa khi coi hệ cùng họ là lớp bảo vệ riêng, và nó tăng rất nhanh: với ba hệ chung hết một họ, tức c = {{s002}}, tỉ số lên {{s015}} lần. Để ý chiều của nó: tỉ số luôn từ {{s002}} trở lên, nên giả định độc lập luôn cho con số LẠC QUAN hơn thực tế, không bao giờ bi quan hơn.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một thiết kế hybrid ghép ML-KEM-768 với một KEM thứ hai cũng dựa trên bài toán trên lưới. Nó cho mấy lớp bảo vệ độc lập trước rủi ro giả định gãy?

- Hai, vì có hai hệ và kẻ tấn công phải phá cả hai
- Một, vì cả hai đứng trên cùng một họ giả định
- Hai, vì hai hệ dùng hai bộ tham số khác nhau
- Không xác định được nếu chưa biết kích thước khoá của từng hệ

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Một, vì cả hai đứng trên cùng một họ giả định**

Rủi ro cần phòng ở đây là rủi ro GIẢ ĐỊNH gãy, không phải rủi ro một cài đặt có lỗi. Một kết quả mới về bài toán trên lưới giết mọi hệ dựng trên bài toán đó cùng lúc, nên số lớp độc lập bằng một, bất kể bộ tham số hay kích thước khoá.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Muốn hai lớp thật thì thành phần thứ hai phải ở họ khác, ví dụ dựa mã, và lúc đó anh trả giá bằng kích thước khoá công khai.

## Bài học đúng rút ra từ ca SIKE là gì?
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài học đúng rút ra từ ca SIKE là gì?

- Isogeny là một hướng toán học yếu nên phải tránh
- Cần nhiều năm soi xét hơn trước khi đưa một hệ vào chuẩn
- Khoá nhỏ luôn đi kèm giả định yếu, nên phải chọn khoá lớn
- Một giả định toán học mới có thể mất toàn bộ độ an toàn trong một bước chứ không suy giảm dần

## Bài học đúng rút ra từ ca SIKE là gì? · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Một giả định toán học mới có thể mất toàn bộ độ an toàn trong một bước chứ không suy giảm dần**

## Bài học đúng rút ra từ ca SIKE là gì? · đáp (tiếp)
@phut: 1
@che-do: noi

SIKE đã bị cả cộng đồng soi nhiều năm và đi tới vòng bốn của tiến trình chuẩn hoá trước khi gãy, nên lập luận soi thêm vài năm nữa không phải lời giải. Cái chết của một hệ cụ thể cũng không chứng minh cả hướng toán học không dùng được, và kích thước khoá thì không có quan hệ nhân quả với tuổi của giả định. Điều rút ra được là về HÌNH DẠNG của rủi ro:

## Bài học đúng rút ra từ ca SIKE là gì? · đáp (tiếp)
@phut: 1
@che-do: noi

độ an toàn của một giả định mới không trôi dần mà có thể rơi xuống không trong một bước, nên kế hoạch phải là tính linh hoạt mật mã (crypto-agility) chứ không phải theo dõi số bit còn lại. Lập luận này áp cho cả lưới, vì lưới cũng là một họ giả định mới.

## Phản biện viết
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phản biện viết: The claim of {{s001}} bit security is not qualified. Cách sửa nào trả lời đúng phản biện?

## Phản biện viết (tiếp)
@phut: 0.5
@che-do: hoi

- Viết rõ mức an toàn đó đứng trên giả định nào, tính trong mô hình chi phí nào, và theo phép quy đổi của bộ tham số nào
- Đổi sang bộ tham số ở mức cao hơn để có thêm biên an toàn
- Thêm một trích dẫn tới chuẩn của NIST cho bộ tham số đã dùng
- Báo thêm thời gian chạy và kích thước khoá để người đọc tự xét

## Phản biện viết · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Viết rõ mức an toàn đó đứng trên giả định nào, tính trong mô hình chi phí nào, và theo phép quy đổi của bộ tham số nào**

Phản biện đòi điều kiện của con số, không đòi con số to hơn. Mức an toàn {{s001}} bit là một phát biểu có điều kiện: nó đúng bên trong một giả định đã khai và một mô hình chi phí đã khai.

## Phản biện viết · đáp (tiếp)
@phut: 1
@che-do: noi

Nâng tham số đổi con số mà không bổ sung hai điều kiện đó, nên phản biện vẫn đứng nguyên; trích dẫn chuẩn cho biết bộ tham số nhưng không cho biết phép quy đổi chi phí; còn thời gian chạy và kích thước khoá là đại lượng khác, không phải điều kiện của mức an toàn. Ca SIKE là lý do chuyện này quan trọng: cái mất đi khi một hệ gãy không phải vài bit mà là cả giả định.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau có một mệnh đề suy sai mức. Bấm vào mệnh đề đó.

- Lược đồ hybrid của chúng tôi ghép ML-KEM-768 với một KEM thứ hai cũng dựa trên bài toán trên lưới mô đun,
- nên hệ còn an toàn ngay cả khi một trong hai thành phần bị phá.
- Chi phí thêm vào là một lần đóng gói (packet) khoá nữa cho mỗi lần bắt tay (handshake).

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên hệ còn an toàn ngay cả khi một trong hai thành phần bị phá.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai thành phần chung một họ giả định, nên một kết quả mới về bài toán trên lưới giết cả hai trong cùng một ngày. Câu này mô tả độc lập ở mức CÀI ĐẶT rồi suy ra độc lập ở mức GIẢ ĐỊNH, mà hai mức đó không kéo theo nhau. Mệnh đề đầu là mô tả trung thực nên không phải lỗi, và mệnh đề cuối về chi phí cũng đúng. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

hoặc đổi thành phần thứ hai sang một họ khác và khai rõ họ nào, hoặc giữ nguyên thiết kế nhưng viết lại câu thành hệ cho một lớp bảo vệ ở mức giả định, và nói lý do chọn như vậy là kích thước.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau rút bài học sai mức từ ca SIKE. Bấm vào chỗ đó.

- Ca SIKE cho thấy mật mã dựa isogeny không đủ chín để triển khai,
- nên chúng tôi chọn một hệ dựa trên lưới cho phần thiết lập khoá.
- Bộ tham số là ML-KEM-768, ở mức an toàn {{s006}} của NIST.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Ca SIKE cho thấy mật mã dựa isogeny không đủ chín để triển khai,**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Một tấn công vào một hệ cụ thể không chứng minh cả hướng toán học không dùng được, và đó cũng không phải điều đáng học nhất từ ca đó. Điều đáng học là hình dạng của rủi ro: một giả định mới có thể mất toàn bộ độ an toàn trong một bước, sau nhiều năm bị cả cộng đồng soi. Kết luận sai mức này còn có một hậu quả thực tế rất xấu:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

nó dẫn người đọc tới chỗ coi lưới là an toàn vì chưa gãy, trong khi lưới cũng là một họ giả định mới và chịu đúng lớp rủi ro đó. Hai mệnh đề sau không phải lỗi: chọn lưới cho thiết lập khoá là quyết định hợp lý trên liên kết chật, và khai bộ tham số là việc phải làm.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau khai mức an toàn đúng cách rồi hỏng ở câu cuối. Bấm vào câu đó.

- Lược đồ của chúng tôi đạt mức an toàn {{s001}} bit,
- tính theo phép quy đổi lõi lưới cho bài toán Module-LWE với bộ tham số ở Bảng II,
- và biên an toàn này sẽ giảm dần theo thời gian nên chúng tôi theo dõi nó để biết khi nào phải di trú (migration).

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và biên an toàn này sẽ giảm dần theo thời gian nên chúng tôi theo dõi nó để biết khi nào phải di trú.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu làm đúng việc mà module {{s007}} đòi: con số {{s001}} bit được khai kèm giả định nền và mô hình chi phí, nên nó kiểm được. Mệnh đề thứ ba đưa vào một giả thiết mới và không khai: rằng rủi ro suy giảm dần, tức có cảnh báo sớm. Ca SIKE bác đúng giả thiết đó. Hệ quả cho bản thảo:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

kế hoạch di trú phải dựa vào TÍNH LINH HOẠT mật mã, tức đổi được hệ mà không đổi giao thức và không đổi định dạng bản tin, chứ không dựa vào việc theo dõi số bit còn lại. Cách sửa rẻ nhất là thay câu cuối bằng một câu nói hệ hỗ trợ thương lượng bộ nguyên thuỷ và nêu chi phí của việc đổi.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Ca độc lập: n hệ ở n họ khác nhau, mỗi họ gãy với xác suất p, muốn mất hết thì cả n phải gãy, nên P = p^n
- Ca tương quan hoàn toàn: n hệ cùng một họ, một kết quả toán học giết cả n cùng lúc, nên P = p
- So hai ca: số mũ của p chạy từ n ở ca độc lập xuống {{s002}} ở ca tương quan hoàn toàn

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Đặt số mũ là n_hiệu dụng = {{s002}} + (n − 1)·(1 − c), nội suy tuyến tính theo c
- P_mất hết = p^(1 + (n − 1)·(1 − c)); kiểm biên c = {{s008}} cho p^n và c = {{s002}} cho p

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: n = {{s006}} · tỉ lệ cùng họ {{s012}} · xác suất một họ gãy {{s013}} · xác suất mất hết {{s018}} · tỉ số tự lừa {{s019}} lần · {{s020}} lớp bảo vệ độc lập

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Các hệ gãy độc lập** tắt đi: Hai thành phần của hybrid đều đứng trên bài toán trên lưới, nên một kết quả mới về bài toán đó giết cả hai cùng lúc.
- **Giả định toán học suy giảm dần, nên có cảnh báo sớm** tắt đi: Ca SIKE: một giả định mất toàn bộ độ an toàn trong một bước, sau nhiều năm bị cả cộng đồng soi.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Hybrid ghép theo kiểu kẻ tấn công phải phá MỌI thành phần** tắt đi: Ghép kiểu chọn một trong hai, ví dụ thương lượng để tương thích ngược, nên phá được một thành phần là đủ.
- **Biết p, tức xác suất một họ gãy trong cửa sổ thời gian** tắt đi: p là ước lượng chủ quan, và với một họ giả định mới thì không có dữ liệu tần suất để ước.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Kéo tỉ lệ hệ cùng họ từ {{s008}} tới {{s002}} và đọc hai con số cạnh nhau: xác suất mất hết an toàn thật, và con số anh sẽ tính nếu coi các hệ là độc lập. Tỉ số giữa chúng là mức tự lừa. Trục dọc thang log vì đại lượng này trải tới mười bậc độ lớn trong dải thanh kéo.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.9` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV describes the key establishment as a hybrid that provides defence in depth. Both components are lattice based, so a single advance against the underlying lattice problem would affect both at once. Please justify the defence in depth claim, or restate it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right and we have restated the claim. Section IV-A now reports the number of distinct assumption families rather than the number of schemes, and that number is one for the current design. We no longer use the phrase defence in depth for this construction. We also state why we chose it:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

on the {{s021}} links of Section II the binding constraint is message size, and a second component from the code based family would raise the public key by orders of magnitude over the {{s022}} byte ML-KEM-768 encapsulation key, which does not fit the fragmentation budget of Table III. Section VII-B is new and states what we do instead: the protocol negotiates the primitive suite, so a replacement can be deployed without changing message formats, and we report the cost of that negotiation.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We make the reasoning explicit because the SIKE case shows that a new assumption can lose its security in one step rather than degrading gradually, so a plan that depends on watching the residual bit level has no input.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng hai thành phần là hai hệ khác nhau, do hai nhóm thiết kế và cài đặt riêng. Đúng ở mức cài đặt, không trả lời được phản biện, vì phản biện nói về mức giả định.
- Mức {{s004}}: thêm một câu rằng hai hệ dùng hai bộ tham số khác nhau nên rủi ro không hoàn toàn trùng. Vẫn trộn hai mức, vì bộ tham số không đổi được họ giả định.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: rút lại cụm phòng vệ nhiều lớp, khai rằng số lớp độc lập ở mức giả định bằng một, và nói rõ lý do kỹ thuật của thiết kế hiện tại, ví dụ ràng buộc kích thước trên liên kết chật.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table II reports {{s001}} bit security for the chosen parameter set without stating the assumption or the cost model used to obtain it. Different estimators and different cost models give materially different bit levels for the same parameters, so the number as printed cannot be checked.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree that the number as printed was not checkable, and Table II has been rewritten. Each row now carries three fields in addition to the bit level: the underlying problem, the estimator and its version, and the cost model used.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

For the selected parameter set we report the bit level under two cost models rather than one, so that the reader sees the spread rather than a single point, and the text states which of the two we use for the comparison in Section VI. We also added one sentence that the reviewer did not ask for but that we think the claim needs:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the bit level is conditional on the stated assumption, and the SIKE case shows that what a scheme can lose is not a few bits but the whole assumption, in one step and after years of public scrutiny. For that reason Section VII states a migration plan based on primitive negotiation rather than on monitoring a residual bit level.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng bộ tham số là bộ do NIST chuẩn hoá nên mức an toàn là mức của chuẩn. Đúng về xuất xứ tham số, không trả lời được phản biện về phép quy đổi.
- Mức {{s004}}: thêm trích dẫn tới một bộ ước lượng độ an toàn, nhưng không nói dùng mô hình chi phí nào trong bộ đó và không nói phiên bản nào.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: khai bài toán nền, khai bộ ước lượng cùng phiên bản, khai mô hình chi phí đã chọn, rồi báo mức bit kèm điều kiện đó.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

You argue for cryptographic agility rather than selecting a single conservative primitive. A simpler design would adopt a code based KEM, whose underlying assumption is far older and has resisted analysis for decades. Please justify why agility is preferable in your setting, and quantify what agility costs you.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Agility and a conservative assumption are not alternatives, and we should have said so explicitly. Section VII-C now separates the two. On the assumption side we accept the reviewer's point: the code based family has the oldest assumption of the three that remain, and if our link budget allowed it we would prefer it. The constraint is size.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The ML-KEM-768 encapsulation key is {{s022}} bytes, a value we verified against Table {{s006}} of FIPS {{s023}}, and the code based public key is larger by orders of magnitude, which exceeds the fragmentation budget in Table III for the {{s021}} links of Section II. We do not state a code based key size in the paper because we have not verified one from the specification, and we prefer a stated gap to an unverified number.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

On the agility side we now quantify what it costs: the negotiation adds one round in the worst case, the second primitive path adds to the firmware image, and the test matrix doubles. We also state the limit of agility: it shortens migration time, it does not make a new assumption older. Finally we give the condition under which we would switch to a code based design, namely a link layer that admits larger payloads.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng linh hoạt mật mã là thực hành tốt được khuyến nghị rộng rãi. Đúng mà không có nội dung, vì phản biện đang đề nghị một thiết kế cụ thể thay thế.
- Mức {{s004}}: nói rằng khoá công khai của họ dựa mã quá lớn, nhưng không đưa ràng buộc kích thước của chính triển khai và không đưa chi phí của linh hoạt.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: đặt kích thước khoá cạnh ngân sách byte của liên kết đích, chỉ ra chỗ thiết kế dựa mã vỡ ràng buộc, rồi khai chi phí của linh hoạt gồm thương lượng, mã nguồn, và bề mặt kiểm thử.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.9` bấm thẻ.
