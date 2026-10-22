---
tieu-de: Kênh bên trong cài đặt: chuẩn an toàn không có nghĩa là mã an toàn
phu-de: Trụ 5 PQC · module 5.8
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 85.5
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

Cài đặt ML-KEM tôi dùng có chống kênh bên không, và nếu có thì tôi trả giá bao nhiêu lần về thời gian?

## Chuẩn nói về lớp một, còn lỗ thường ở lớp ba
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Trụ này tới đây chỉ bàn thuật toán trên giấy. Nhưng thứ bị phá trong thực tế gần như luôn là **cài đặt**, không phải bài toán toán học. Module này tách bảo đảm an toàn thành **ba lớp** và chỉ làm đúng một việc: dạy anh không nhảy lớp khi viết câu khẳng định.

## Chuẩn nói về lớp một, còn lỗ thường ở lớp ba (tiếp)
@phut: 1
@che-do: noi

**Lớp một, thuật toán:** độ khó của bài toán nền. **Lớp hai, giao thức:** cách ghép các nguyên thuỷ lại. **Lớp ba, cài đặt:** mã đã biên dịch chạy trên một phần cứng cụ thể. FIPS {{s001}} đặc tả lớp một và một phần lớp hai. Nó **không** nói gì về việc mã của anh có chạy trong thời gian hằng hay không, và cũng không nói gì về điện năng của nó.

## Chuẩn nói về lớp một, còn lỗ thường ở lớp ba (tiếp)
@phut: 1
@che-do: noi

Việc thứ hai của module là cho anh một con số để trả lời câu hỏi mà phản biện hay hỏi: **che mặt nạ (masking) tốn của tôi bao nhiêu lần về thời gian**. Mô hình ở đây là mô hình ước lượng, khai rõ tham số, và nó dùng để ước lượng bậc độ lớn chứ không dùng để báo số trong bản thảo.

## Chuẩn nói về lớp một, còn lỗ thường ở lớp ba (tiếp)
@phut: 1
@che-do: noi

**Cảnh báo về trạng thái số:** đặc tả của module này có một dòng đánh dấu không chắc, là hệ số chậm thật đo được của ML-KEM có che mặt nạ trên Cortex-M. Dòng đó **đã bị bỏ**, không lên thẻ nào. Muốn con số đó thì phải mở một bài đo thật và ghi rõ bản cài đặt.

## Ba lớp, và chuẩn bảo đảm lớp nào
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Ba lớp, và chuẩn bảo đảm lớp nào · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Lớp một, thuật toán:** độ khó bài toán nền, ví dụ Module-LWE. **Lớp hai, giao thức:** cách ghép, ví dụ phép biến đổi Fujisaki-Okamoto biến một hệ mã hoá yếu thành KEM an toàn IND-CCA. **Lớp ba, cài đặt:** mã máy chạy trên một vi điều khiển cụ thể.

## Ba lớp, và chuẩn bảo đảm lớp nào · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **FIPS {{s001}} đặc tả lớp một và một phần lớp hai, hết.** Mã giả trong chuẩn không phải mã chạy trong thời gian hằng. Nên câu "chúng tôi dùng ML-KEM nên an toàn" là một suy luận nhảy từ lớp một sang lớp ba, và nó không phải một phát biểu yếu mà là một phát biểu không có nội dung.

## Bề mặt kênh bên riêng của mật mã lattice
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Bề mặt kênh bên riêng của mật mã lattice · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Giải mã lattice có hai bước mà mật mã trên đường cong không có: **so sánh** bản mã dựng lại với bản mã nhận được, và **lấy mẫu theo phân bố** khi sinh khoá hoặc khi ký. Viết hai bước đó phụ thuộc dữ liệu thì thời gian chạy hoặc điện năng rò bí mật ra. Lỗi kinh điển là một nhánh điều kiện trên bí mật, và lỗi thứ hai là một phép truy cập bảng có chỉ số phụ thuộc bí mật.

## Bề mặt kênh bên riêng của mật mã lattice · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: bước so sánh trong phép biến đổi Fujisaki-Okamoto phải là **so sánh toàn khối trong thời gian hằng**. Một vòng lặp thoát sớm ở byte đầu khác nhau là đủ để biến bước đó thành một kênh bên, và chỗ đó không nằm trong bất kỳ bảng kích thước nào của chuẩn.

## Che mặt nạ bậc d
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Che mặt nạ bậc d · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Tách mỗi bí mật thành **d+1 phần** sao cho tổ hợp của các phần cho lại bí mật, rồi tính trên từng phần. Kẻ tấn công muốn dựng lại bí mật phải đo được **d+1 điểm cùng lúc**. Chi phí: phần tuyến tính trả giá bậc `(d+1)`, phần phi tuyến trả giá bậc `(d+1)²` vì gadget nhân phải ghép mọi cặp phần.

## Che mặt nạ bậc d · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: giả thiết nền là **nhiễu độc lập giữa các phần**. Mất giả thiết đó thì bậc d không còn tương ứng với số vết đo mà kẻ tấn công cần, nên con số bảo vệ mất nghĩa. Rò rỉ bậc cao và ghép cặp trong đường dẫn dữ liệu của bộ xử lý là hai cách giả thiết đó bị phá trên phần cứng thật.

## Oracle thất bại giải mã
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Oracle thất bại giải mã · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Kẻ tấn công gửi bản mã méo có chủ đích và đo hành vi của thiết bị. Mỗi lần thiết bị **phân biệt được** nguyên nhân thất bại, dù bằng mã lỗi, bằng dòng log, hay chỉ bằng thời gian trả lời, kẻ tấn công thu được một bit về bí mật. Gom đủ bit thì hồi phục khoá giải mã.

## Oracle thất bại giải mã · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: cài đặt phải **thất bại im lặng và trong cùng một khoảng thời gian**. Chi tiết lỗi tiện cho việc gỡ rối chính là oracle, nên một bảng mã lỗi phân biệt theo nguyên nhân là tự tay xây oracle. Đây cũng là lý do phép biến đổi Fujisaki-Okamoto dùng **từ chối ngầm**, tức trả về một khoá giả sinh từ bí mật thay vì báo lỗi.

## Hệ số chậm khi che mặt nạ bậc d
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`S(d, r) = ({{s002}} − r)·(d+1) + r·(d+1)² N_vết(d) ≈ N₁ · κ^d`

**Giả thiết nó đứng trên:**

## Hệ số chậm khi che mặt nạ bậc d (tiếp)
@phut: 1
@che-do: so

- r là tỉ lệ THỜI GIAN CHẠY nằm ở phần phi tuyến, không phải tỉ lệ số dòng mã, và phải đo bằng profiler trên chính phần cứng đích
- phần tuyến tính trả giá bậc (d+1) vì mỗi phép tuyến tính tính riêng trên từng phần rồi tổ hợp lại
- phần phi tuyến trả giá bậc (d+1)² vì gadget nhân phải ghép mọi cặp phần, cộng chi phí làm mới nhiễu

## Hệ số chậm khi che mặt nạ bậc d (tiếp)
@phut: 1
@che-do: so

- nhiễu độc lập giữa các phần, nên kẻ tấn công cần đo d+1 điểm cùng lúc và số vết cần tăng theo bậc của d
- N₁ và κ là tham số KHAI SẴN của mô hình dạy học trong module này, không phải phép đo trên phần cứng của người học

## Hệ số chậm khi che mặt nạ bậc d · ghi chú
@phut: 1
@che-do: noi

Hai ca biên khoá công thức và tính được bằng tay: `d = {{s005}}` cho `S = {{s002}}` với mọi r, vì không che thì không trả giá; `r = {{s005}}` cho `S = d+1`, vì mã toàn tuyến tính thì chỉ nhân theo số phần. Dùng hai ca này để kiểm bất kỳ con số chi phí che mặt nạ mà anh gặp trong bài của người khác:

## Hệ số chậm khi che mặt nạ bậc d · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

con số nào không về đúng hai ca biên đó thì mô hình của họ khác mô hình này, và họ phải khai mô hình.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s004}} | lớp | Module này tách bảo đảm an toàn của một hệ PQC thành
!so {{s006}} | phần | Che mặt nạ bậc d = {{s007}}. Mỗi bí mật bị tách
!so {{s008}} | lần | Che mặt nạ bậc d = {{s003}}

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Che mặt nạ bậc d = {{s003}} trên một cài đặt mà phần phi tuyến chiếm r = {{s010}} thời gian chạy. Hệ số chậm ước lượng là bao nhiêu lần?

d = {{s003}}, r = {{s009}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`({{s002}} - r) × (d + {{s002}}) + r × Math.pow(d + {{s002}}, {{s003}})`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s011}} lần. Hai số hạng góp không đều: phần tuyến tính chiếm {{s012}} thời gian mà chỉ góp {{s013}} × {{s004}} = {{s014}}, còn phần phi tuyến chiếm {{s015}} thời gian mà góp {{s010}} × {{s008}} = {{s016}}. Nên con số chi phí che mặt nạ phải khai r cùng với d, vì cùng bậc d trên hai cài đặt có r khác nhau cho hai kết quả khác nhau.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cài đặt không che mặt nạ đạt {{s017}} bắt tay (handshake) mỗi giây trên thiết bị đích. Bật che mặt nạ bậc d = {{s003}} với r = {{s010}}. Còn lại bao nhiêu bắt tay mỗi giây?

h0 = {{s017}}, d = {{s003}}, r = {{s009}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`h0 / (({{s002}} - r) × (d + {{s002}}) + r × Math.pow(d + {{s002}}, {{s003}}))`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s018}} bắt tay mỗi giây, từ {{s017}} ban đầu. Đây là con số phải đặt cạnh yêu cầu vận hành, không phải đặt cạnh con số của bài khác: nếu hệ cần {{s019}} bắt tay mỗi giây thì biên còn {{s020}} lần và che mặt nạ bậc {{s003}} khả thi; nếu hệ cần {{s021}} thì bậc {{s003}} đã không đáp ứng được và phải đổi thiết kế chứ không phải tắt che mặt nạ.

## Mô hình số vết khai sẵn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình số vết khai sẵn: N(d) = N₁ · κ^d với N₁ = {{s023}} vết cho cài đặt không che và κ = {{s024}}. Kẻ tấn công thu được 10⁶ vết. Bậc che mặt nạ nhỏ nhất để N(d) vượt số vết đó là bao nhiêu?

vet = {{s022}}, n1 = {{s023}}, kappa = {{s024}}

## Mô hình số vết khai sẵn · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.ceil(Math.log(vet / n1) / Math.log(kappa))`

## Mô hình số vết khai sẵn · đáp (tiếp)
@phut: 1
@che-do: noi

Đúng bậc {{s003}}, vì N(1) = {{s025}} còn thấp hơn 10⁶ mà N(2) = {{s026}} đã vượt. Để ý tính bất đối xứng: mỗi bậc nhân số vết cần lên {{s024}} lần nhưng chỉ nhân thời gian chạy lên vài lần, nên về phía phòng vệ thì nâng bậc là món hàng rẻ. Hai tham số {{s023}} và {{s024}} là tham số dạy học khai sẵn, không phải phép đo trên phần cứng của anh, nên đừng đưa chúng vào bản thảo.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

FIPS {{s001}} bảo đảm điều gì về cài đặt ML-KEM mà anh nạp lên vi điều khiển?

- Rằng mã chạy trong thời gian hằng nếu làm theo đúng mã giả trong chuẩn
- Rằng mã chống được tấn công điện năng bậc một
- Không bảo đảm gì về thời gian chạy hay điện năng của mã của anh
- Rằng thất bại giải mã không rò thông tin nào ra ngoài

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Không bảo đảm gì về thời gian chạy hay điện năng của mã của anh**

Chuẩn đặc tả hàm cần tính và bộ tham số, tức lớp thuật toán và một phần lớp giao thức. Thời gian chạy, điện năng, và cách xử lý thất bại là tính chất của mã đã biên dịch trên một phần cứng cụ thể, nên chúng nằm ngoài phạm vi của FIPS {{s001}}.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Mã giả trong chuẩn viết cho người đọc hiểu, không phải mã chạy trong thời gian hằng, và cả phép biến đổi Fujisaki-Okamoto cũng chỉ bảo đảm ở mức toán học chứ không bảo đảm rằng vòng lặp so sánh của anh không thoát sớm.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai cài đặt cùng là ML-KEM-768. Cài đặt A có r = {{s027}}, cài đặt B có r = {{s028}}. Bật che mặt nạ bậc {{s003}} lên cả hai. Điều nào đúng?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Cài đặt B chậm đi nhiều hơn, vì chi phí phần phi tuyến tăng theo bình phương số phần
- Hai cài đặt chậm đi như nhau, vì cùng bậc che mặt nạ và cùng bộ tham số
- Cài đặt A chậm đi nhiều hơn, vì phần tuyến tính chiếm chỗ lớn hơn trong thời gian chạy
- Không so được, vì hệ số chậm chỉ phụ thuộc phần cứng chứ không phụ thuộc mã

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cài đặt B chậm đi nhiều hơn, vì chi phí phần phi tuyến tăng theo bình phương số phần**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Hệ số chậm là {{s029}} lần ở r = {{s027}} và {{s030}} lần ở r = {{s028}}, tức cùng một bậc che mặt nạ cho hai con số cách nhau gần hai lần. Lý do là phần tuyến tính trả giá bậc (d+1) = {{s004}} còn phần phi tuyến trả giá bậc (d+1)² = {{s008}}, nên cài đặt nào có nhiều việc phi tuyến hơn thì trả giá nhiều hơn. Hệ quả cho cách viết:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

mọi con số chi phí che mặt nạ phải khai r cùng với d, và phải nói r đo bằng gì.

## Phản biện viết
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phản biện viết: The security claim does not account for implementation attacks. Cách trả lời nào đứng được?

## Phản biện viết (tiếp)
@phut: 0.5
@che-do: hoi

- Nói rằng tấn công cài đặt nằm ngoài phạm vi vì bài này bàn về giao thức
- Thêm một câu rằng cài đặt dùng một thư viện đã được kiểm toán
- Dẫn FIPS {{s001}} để chứng minh thuật toán đã được chuẩn hoá và an toàn
- Khai mô hình kẻ tấn công ở lớp cài đặt, nói rõ bản cài đặt nào và che mặt nạ bậc mấy, rồi báo chi phí thời gian đo trên chính phần cứng đích

## Phản biện viết · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khai mô hình kẻ tấn công ở lớp cài đặt, nói rõ bản cài đặt nào và che mặt nạ bậc mấy, rồi báo chi phí thời gian đo trên chính phần cứng đích**

## Phản biện viết · đáp (tiếp)
@phut: 1
@che-do: noi

Phản biện không đòi anh chống được mọi tấn công, nó đòi anh khai vị trí của mình. Câu trả lời đứng được là câu ghi rõ bản cài đặt, bậc che mặt nạ, và chi phí đo trên phần cứng đích, vì đó là ba dữ kiện người đọc cần để tự xét.

## Phản biện viết · đáp (tiếp)
@phut: 1
@che-do: noi

Viện dẫn chuẩn chỉ trả lời cho lớp thuật toán nên không chạm tới phản biện; còn cụm "thư viện đã được kiểm toán" là một nhãn chứ không phải một phép đo, và nó mời ngay câu hỏi tiếp là kiểm toán cái gì, phiên bản nào, bằng công cụ nào.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau có một mệnh đề nhảy lớp. Bấm vào mệnh đề đó.

- Chúng tôi dùng ML-KEM-768 theo FIPS {{s001}} cho phần thiết lập khoá,
- với bộ tham số ở mức an toàn (security level) {{s004}} của NIST,
- nên cài đặt trên thiết bị của chúng tôi an toàn trước tấn công kênh bên.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên cài đặt trên thiết bị của chúng tôi an toàn trước tấn công kênh bên.**

Hai mệnh đề đầu đều hợp lệ và kiểm được: chúng nói về lớp thuật toán, và FIPS {{s001}} bảo đảm đúng lớp đó. Mệnh đề thứ ba suy một tính chất của lớp cài đặt từ một bảo đảm ở lớp thuật toán, mà chuẩn không nói gì về thời gian chạy hay điện năng của mã. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

bỏ chữ nên, rồi viết một câu riêng khai mô hình kẻ tấn công ở lớp cài đặt, bản cài đặt đã dùng, bậc che mặt nạ nếu có, và công cụ đã dùng để kiểm thời gian hằng. Nếu chưa làm gì ở lớp ba thì khai thẳng là chưa, vì một giới hạn tự khai mạnh hơn một câu khẳng định không đứng được.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn so sánh sau làm cả bảng chi phí mất hiệu lực. Bấm vào chỗ đó.

- Chúng tôi đo ML-KEM-768 bằng cài đặt tham khảo, không bật che mặt nạ,
- và đo X25519 bằng một thư viện nhúng đã bật chống kênh bên,
- rồi kết luận rằng PQC chỉ chậm hơn {{s031}} lần nên khả thi trên thiết bị ràng buộc.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**rồi kết luận rằng PQC chỉ chậm hơn {{s031}} lần nên khả thi trên thiết bị ràng buộc.**

Hai mệnh đề đầu đều là mô tả trung thực về việc đã làm, nên chúng không phải lỗi. Lỗi là ở câu kết luận: nó so một bên KHÔNG có chống kênh bên với một bên CÓ, nên con số {{s031}} lần trộn hai mức bảo vệ khác nhau vào một tỉ số.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Theo mô hình trong module này, chỉ riêng che mặt nạ bậc {{s003}} ở r = {{s010}} đã nhân thời gian lên {{s032}} lần, tức lớn hơn chính tỉ số đang được báo. Cách sửa: đo cả hai bên ở cùng mức bảo vệ, hoặc báo hai tỉ số và khai rõ mức bảo vệ của từng bên.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả cài đặt sau tự xây một oracle. Bấm vào chỗ đó.

- Khi kiểm tra bản mã thất bại, cài đặt trả về mã lỗi phân biệt từng nguyên nhân để tiện gỡ rối,
- và ghi một dòng log kèm nhãn thời gian.
- Khoá bí mật không bao giờ xuất hiện trong log.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Khi kiểm tra bản mã thất bại, cài đặt trả về mã lỗi phân biệt từng nguyên nhân để tiện gỡ rối,**

Đây là oracle giải mã thất bại, viết bằng tay và đưa vào đặc tả. Mỗi mã lỗi phân biệt được là một bit về bí mật, và gom đủ bit thì hồi phục được khoá giải mã. Hai mệnh đề sau không phải lỗi:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

ghi log kèm nhãn thời gian là việc bình thường nếu nội dung log không phân biệt nguyên nhân, và việc khoá bí mật không xuất hiện trong log là một tính chất tốt nhưng nó không cứu được chỗ này. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

dùng từ chối ngầm của phép biến đổi Fujisaki-Okamoto, tức trả về một khoá giả sinh từ bí mật, cùng một đường mã và cùng một khoảng thời gian cho mọi nguyên nhân thất bại, rồi đếm số lần thất bại ở một chỗ mà kẻ tấn công không đọc được.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Tách mỗi bí mật thành d+1 phần sao cho tổ hợp của chúng cho lại bí mật
- Phép tuyến tính tính riêng trên từng phần rồi tổ hợp, nên chi phí nhân (d+1)
- Phép phi tuyến phải ghép mọi cặp phần, nên chi phí nhân (d+1)²
- Gọi r là tỉ lệ thời gian chạy nằm ở phần phi tuyến, nên phần tuyến tính chiếm {{s002}} − r

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Lấy trung bình có trọng số hai số hạng: S(d, r) = ({{s002}} − r)·(d+1) + r·(d+1)²
- Kiểm hai ca biên: d = {{s005}} cho S = {{s002}} với mọi r, và r = {{s005}} cho S = d+1

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: d = {{s003}} · r = {{s010}} · hệ số chậm {{s032}} lần · {{s018}} bắt tay mỗi giây · cần {{s026}} vết để thắng bậc {{s003}} · biên {{s020}} lần so với yêu cầu {{s019}} mỗi giây

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mã chạy trong thời gian hằng, không nhánh và không truy cập bộ nhớ phụ thuộc bí mật** tắt đi: Bước so sánh trong phép biến đổi Fujisaki-Okamoto thoát sớm ở byte đầu khác nhau, tức có một nhánh phụ thuộc bí mật trong đường giải mã.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Nhiễu độc lập giữa các phần mặt nạ** tắt đi: Rò rỉ bậc cao, hoặc hai phần cùng đi qua một đường dẫn dữ liệu của bộ xử lý và ghép lại trong một chu kỳ.
- **Thất bại giải mã im lặng và trong cùng một khoảng thời gian** tắt đi: Cài đặt trả về mã lỗi phân biệt theo nguyên nhân, hoặc trả lời nhanh hơn khi bản mã méo.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **r đo bằng profiler trên chính phần cứng đích** tắt đi: r lấy từ một bài đo trên máy tính để bàn, hoặc ước theo tỉ lệ số dòng mã.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Hai câu hỏi cùng lúc, trên cùng một bộ tham số: che mặt nạ tốn của anh bao nhiêu lần về thời gian, và nó đẩy số vết đo mà kẻ tấn công cần lên bao nhiêu. Đồ thị vẽ số vết cần theo bậc che mặt nạ, trục dọc thang log vì đại lượng đó trải mười bậc độ lớn.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.8` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V states that the proposed handshake is secure because it instantiates ML-KEM-768 as standardized in FIPS {{s001}}. FIPS {{s001}} specifies the algorithm, not its implementation, and it makes no claim about timing or power behaviour. Please state your implementation level attack model, identify the implementation you measured, and report whether any side channel countermeasure was enabled.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree, and we have restructured the security discussion into three explicit layers. Section III-A now states the algorithmic claim, which is the one FIPS {{s001}} supports. Section VI-A is new and states the implementation level attack model: an adversary with physical access to the device, able to measure execution time over the network and power traces on the board, and able to submit malformed ciphertexts.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We measured the pq-crystals reference implementation at the commit recorded in Table VII, with first order masking enabled in the decapsulation path and with the Fujisaki-Okamoto comparison replaced by a constant time full block comparison. Masking costs {{s033}} times the unmasked run time on our target at a measured nonlinear work fraction of {{s009}}, which leaves {{s034}} handshakes per second against an operational requirement of {{s019}}. We also state what we did not verify:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

our leakage assessment covers first order leakage only, so it says nothing about higher order leakage, which is exactly the case where the masking order no longer corresponds to the number of traces an adversary needs.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: trả lời rằng ML-KEM là chuẩn của NIST và được dùng rộng rãi. Đúng về thực hành, không chạm tới phản biện, vì phản biện nói đúng chỗ chuẩn không bảo đảm.
- Mức {{s003}}: thêm một câu rằng cài đặt dùng một thư viện đã được kiểm toán. Đây là một nhãn, không phải một phép đo, và nó mời ngay câu hỏi kiểm toán cái gì và phiên bản nào.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: tách rõ ba lớp trong phần an toàn, khai mô hình kẻ tấn công ở lớp cài đặt, nói rõ bản cài đặt và phiên bản, khai có hay không có che mặt nạ và bậc mấy, rồi báo chi phí thời gian đo trên phần cứng đích.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table VI compares your post quantum handshake against an X25519 baseline and reports a {{s035}} times overhead. The post quantum side uses an unprotected reference implementation while the classical baseline uses a hardened embedded library. This is not a like for like comparison, and the stated overhead therefore cannot support the feasibility claim in Section I.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right, and the comparison has been redone. Table VI now reports two columns per scheme: unprotected and protected. At the protected level, our ML-KEM-768 path uses first order masking with a constant time comparison, and the X25519 baseline keeps the hardened library that was used before. We also report the masking cost separately, as a function of the masking order and the measured nonlinear work fraction, so that a reader on a different platform can interpolate rather than reuse our ratio.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, we no longer phrase the feasibility claim as a ratio against the classical baseline. Section VI-C states it against an operational requirement instead: the protected implementation sustains {{s034}} handshakes per second on the target board, and the deployment of Section II requires {{s019}}, which is a margin of {{s036}} times. We state the protection level in the claim itself, because the same sentence is false at masking order {{s007}}, where the margin falls to about {{s037}} times.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: nói rằng cài đặt tham khảo là cách đo thông dụng trong lĩnh vực. Đúng về thực hành, không trả lời được phản biện, vì vấn đề là hai bên ở hai mức bảo vệ khác nhau.
- Mức {{s003}}: thêm một câu khai rằng bên hậu lượng tử không có che mặt nạ, nhưng vẫn giữ nguyên tỉ số {{s031}} lần làm con số kết luận về tính khả thi.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: đo lại cả hai bên ở cùng một mức bảo vệ, báo hai tỉ số thay vì một, và nói rõ mức bảo vệ của từng cài đặt trong chú thích bảng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.8` bấm thẻ.
