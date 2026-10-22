---
tieu-de: QKD, và cách so sánh công bằng với PQC
phu-de: Trụ 5 PQC · module 5.6
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 94
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

Key rate của tôi theo khoảng cách là bao nhiêu, và khi so với PQC thì tôi đang so trong mô hình đe doạ (threat model) nào?

## Hai con số
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này có hai nửa, và nửa thứ hai mới là nửa khó.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

Nửa thứ nhất là vật lý, và nó chắc như đinh đóng cột. Module này lấy `α = {{s001}} dB mỗi km` ở {{s002}} nm, nên hiệu suất kênh (channel efficiency) là `η = 10^(−αL/10)`. Ở {{s003}} km con số tròn tuyệt đối: `η = 10⁻²`. Chặn PLOB nói dung lượng khoá bí mật của một kênh mất mát không vượt được `−log₂(1−η)`, tức khoảng **{{s004}} bit mỗi lần dùng kênh** ở {{s003}} km. Ở {{s005}} km thì `η = 10⁻⁶`.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

Hai mốc {{s003}} km và {{s005}} km cho số mũ chẵn, nên chúng là điểm neo không thể tranh.

Nửa thứ hai là nửa reviewer đánh. Mọi câu so QKD với PQC chỉ có nghĩa khi đã **cố định mô hình đe doạ** và đã **tính cả hạ tầng**. Kết luận quan trọng nhất của module nằm ở một ô duy nhất trong bảng công tắc:

## Hai con số (tiếp)
@phut: 1
@che-do: noi

bật kẻ tấn công có máy lượng tử lớn thì PQC dựa lattice vẫn đứng theo giả định độ khó còn QKD đứng theo định luật vật lý, nhưng bật kẻ tấn công tấn công thiết bị đầu cuối thì **cả hai đổ**. Ai nhớ đúng ô đó thì không bao giờ viết một bảng so sánh hai cột ngây thơ nữa.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

**{{s001}} là con số làm việc, không phải con số của một nguồn nào.** Ba con số khác nhau hay bị gộp làm một, và một reviewer biết chỗ này sẽ hỏi đúng vào nó.
Tờ thông tin sản phẩm của sợi G.652.D bán ngoài thị trường bảo đảm **≤ {{s006}} dB mỗi km** ở {{s002}} nm.
Khuyến nghị ITU-T G.652 không nói {{s006}} cũng không nói {{s001}}:

## Hai con số (tiếp)
@phut: 1
@che-do: noi

nó đặt **trần {{s007}} dB mỗi km** cho cáp ở {{s002}} nm, vì chuẩn viết cho mọi nhà sản xuất chứ không cho một sản phẩm.
Còn **{{s001}}** là con số tròn mà giới kỹ thuật dùng, và module này dùng nó vì nó cho `η = 10⁻²` chẵn ở {{s003}} km, tức một điểm neo gõ tay được.

## Hai con số (tiếp)
@phut: 1
@che-do: noi

Khoảng cách giữa ba con số đó không nhỏ. Trên {{s003}} km: {{s006}} cho {{s008}} dB, {{s001}} cho {{s009}} dB, {{s007}} cho {{s010}} dB. Chênh {{s011}} dB giữa trần của chuẩn và con số làm việc là **hơn {{s012}} lần** về hiệu suất kênh, nên một ngân sách đường truyền dựng trên {{s001}} mà khai là "theo G.652" vừa sai nguồn vừa lạc quan. Khi trình bày, nói rõ anh lấy α từ đâu, trước khi ai kịp hỏi.

## Khái niệm tầng 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s013}} trên bốn.*

## Khái niệm tầng 1 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`η = 10^(−αL/10)` với `α` tính bằng dB mỗi km. Ở {{s001}} dB mỗi km, cứ thêm {{s014}} km là `η` mất đúng một bậc độ lớn, vì {{s001}} nhân {{s014}} bằng {{s015}} dB.

## Khái niệm tầng 1 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: quy tắc {{s014}} km một bậc. Nó cho ước lượng nhẩm mà không cần máy: {{s003}} km là 10⁻², {{s016}} km là 10⁻³, {{s005}} km là 10⁻⁶, {{s017}} km là 10⁻¹⁰. Và nó cho ngay lý do vì sao QKD sợi quang không phải bài toán kỹ thuật dần dần tốt lên: khoảng cách vào số mũ, nên không có tiến bộ tuyến tính nào đuổi được.

## Chặn PLOB: bậc độ lớn không thể vượt
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s018}} trên bốn.*

## Chặn PLOB: bậc độ lớn không thể vượt · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Chặn Pirandola, Laurenza, Ottaviani, Banchi cho dung lượng khoá bí mật của kênh mất mát: `C ≤ −log₂(1−η)`, và khi `η` nhỏ thì `−log₂(1−η) ≈ 1,44·η`.

## Chặn PLOB: bậc độ lớn không thể vượt · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đây là chặn trên cho MỌI giao thức hai điểm không có bộ lặp, kể cả giao thức chưa ai phát minh. Nên nó là công cụ phản biện mạnh nhất của module: thấy một bài báo khai key rate vượt `1,44·η` ở khoảng cách đó thì hoặc họ có bộ lặp, hoặc có node trung gian tin cậy, hoặc con số sai. Không cần đọc phần phương pháp mới biết phải hỏi gì.

## Khối hữu hạn: vì sao phải khai độ dài khối
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s019}} trên bốn.*

## Khối hữu hạn: vì sao phải khai độ dài khối · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Key rate tiệm cận là giới hạn khi độ dài khối tiến tới vô hạn. Hệ thật xử lý khối hữu hạn (finite-key), nên phải trừ phần thống kê: ước lượng sai bit trên mẫu hữu hạn có khoảng tin cậy, và khuếch đại riêng tư phải trả giá cho khoảng đó.

## Khối hữu hạn: vì sao phải khai độ dài khối · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: hệ quả của chuyện này không chỉ là con số nhỏ hơn mà là **thứ hạng có thể đảo**. Hai giao thức xếp theo key rate tiệm cận có thể đổi chỗ khi tính khối hữu hạn, vì phần phạt phụ thuộc cách từng giao thức ước lượng tham số. Nên một bảng so sánh key rate không khai độ dài khối là một bảng không so được, giống hệt chuyện bảng precision không khai tỉ lệ nền (base rate).

## So QKD với PQC: hai điều kiện trước khi được phép so
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s020}} trên bốn.*

## So QKD với PQC: hai điều kiện trước khi được phép so ·
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Điều kiện một: **cố định mô hình đe doạ**. QKD và PQC không đứng trên cùng một loại giả thiết. QKD đứng trên định luật vật lý cộng giả định thiết bị đúng như mô hình; PQC đứng trên giả định độ khó tính toán cộng giả định cài đặt đúng. Hai loại giả thiết này không so được bằng một con số bit.

## So QKD với PQC: hai điều kiện trước khi được phép (tiếp)
@phut: 1
@che-do: noi

Điều kiện hai: **tính cả hạ tầng**. PQC là một bản vá phần mềm trên hạ tầng đang có. QKD cần sợi tối hoặc kênh quang tự do, cần node trung gian tin cậy để đi xa, và cần một kênh cổ điển ĐÃ XÁC THỰC để chạy sàng lọc và khuếch đại riêng tư, mà xác thực đó lại thường lấy từ khoá chia sẻ trước hoặc từ chữ ký hậu lượng tử.

## So QKD với PQC: hai điều kiện trước khi được phép (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: câu cuối ấy là câu đắt nhất của module. QKD không thay thế PQC vì nó **cần** một dạng xác thực mà bản thân nó không cung cấp.

## Bốn công thức của module, và giả thiết của từng cái
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`η = 10^(−αL/10) C_PLOB = −log₂(1−η) ≈ 1,44·η R_BB84 = q·[1 − 2·h₂(e)] số lần dùng kênh cho K bit = K / C`

**Giả thiết nó đứng trên:**

## Bốn công thức của module, và giả thiết của từng (tiếp)
@phut: 1
@che-do: so

- α là suy hao trên một km và không đổi theo chiều dài, tức sợi đồng nhất, không mối hàn, không đầu nối
- chặn PLOB áp cho kênh hai điểm KHÔNG có bộ lặp lượng tử và KHÔNG có node trung gian tin cậy
- R_BB84 ở dạng này là key rate tiệm cận, tức độ dài khối tiến tới vô hạn, chưa trừ thống kê khối hữu hạn

## Bốn công thức của module, và giả thiết của từng (tiếp)
@phut: 1
@che-do: so

- q là hệ số sàng lọc của giao thức, thường {{s021}} cho BB84 chọn cơ sở đều, nên bỏ q là tự nhân đôi kết quả
- e là sai bit lượng tử đã đo, và h₂ là entropy nhị phân tính theo bit

## Bốn công thức của module, và giả thiết của từng cái ·
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Bốn công thức này trả lời bốn câu khác nhau, nên trộn chúng là chỗ sai phổ biến nhất. `η` là tính chất của SỢI. `C_PLOB` là chặn trên của BẤT KỲ giao thức trên sợi đó. `R_BB84` là key rate của MỘT giao thức cụ thể. Còn số lần dùng kênh là đại lượng VẬN HÀNH, và chỉ có nó mới đổi được sang giây và sang tiền.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s022}} | dB mỗi km | Sợi G.652.D bán ngoài thị trường bảo đảm suy hao tối đa
!so {{s018}} | số mũ âm của {{s015}} | Sợi đơn mode {{s002}} nm với suy hao chuẩn
!so {{s023}} | bit mỗi lần dùng kênh | Ở η = {{s024}}

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s025}} | số mũ âm của {{s015}} | Cùng loại sợi đó
!so {{s026}} | % | BB84 một chiều với key rate R = {{s013}} trừ hai lần

## Sợi 0,2 dB mỗi km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Sợi {{s001}} dB mỗi km, chiều dài {{s016}} km. Chặn PLOB là bao nhiêu bit mỗi lần dùng kênh?

alpha = {{s027}}, L = {{s016}}

## Sợi 0,2 dB mỗi km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`-Math.log2(1 - Math.pow(10, -alpha⋆L/10))`

Khoảng {{s028}} bit mỗi lần dùng kênh. Để ý quan hệ với mốc {{s003}} km: thêm {{s014}} km làm chặn này mất đúng một bậc độ lớn, từ bậc {{s004}} xuống bậc {{s029}}. Và xấp xỉ {{s030}} nhân η đúng tới ba chữ số ở đây, vì η = 10⁻³ đã nhỏ.

## Sợi 0,2 dB mỗi km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Sợi {{s001}} dB mỗi km, {{s032}} km. Theo chặn PLOB, cần ít nhất bao nhiêu lần dùng kênh để sinh một khoá {{s031}} bit?

bit = {{s031}}, alpha = {{s027}}, L = {{s032}}

## Sợi 0,2 dB mỗi km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`bit / (-Math.log2(1 - Math.pow(10, -alpha⋆L/10)))`

Khoảng {{s033}} triệu lần dùng kênh. Chiều của con số này là chỗ dễ sai nhất: PLOB là chặn TRÊN của khoá mỗi lần dùng kênh, nên số lần dùng kênh suy ra từ nó là chặn DƯỚI. Hệ thật luôn cần nhiều hơn, thường nhiều hơn vài bậc, vì còn hiệu suất bộ tách, tỉ lệ sàng lọc, sửa lỗi và phạt khối hữu hạn.

## Sợi 0,2 dB mỗi km · đáp (tiếp)
@phut: 1
@che-do: noi

Viết con số này vào bài kèm chữ ít nhất thì nó là một tuyên bố mạnh; viết kèm chữ chúng tôi cần thì nó là một tuyên bố sai.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai key rate {{s034}} bit mỗi lần dùng kênh ở {{s003}} km sợi {{s001}} dB mỗi km, không có bộ lặp. Phản ứng đúng là gì?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chấp nhận, vì {{s034}} bit mỗi lần dùng kênh là con số nhỏ và hợp lý
- Hỏi ngay, vì chặn PLOB ở đó chỉ khoảng {{s004}} bit mỗi lần dùng kênh nên con số này vượt chặn trên
- Hỏi về hiệu suất bộ tách, vì đó là nguyên nhân thường gặp
- Không kết luận được mà chưa biết sai bit của họ

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hỏi ngay, vì chặn PLOB ở đó chỉ khoảng {{s004}} bit mỗi lần dùng kênh nên con số này vượt chặn trên**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Chặn PLOB không phụ thuộc giao thức, không phụ thuộc thiết bị, không phụ thuộc sai bit: nó là chặn trên cho mọi giao thức hai điểm không bộ lặp trên kênh có hiệu suất η đó. Nên {{s034}} lớn hơn {{s004}} là đủ để hỏi, trước khi đọc bất cứ phần nào khác. Ba câu trả lời có thể có: họ có bộ lặp, họ có node trung gian tin cậy, hoặc họ tính sai. Đáp án thứ tư đảo chiều logic:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

biết sai bit chỉ làm con số THẤP hơn nữa, nên nó không cứu được.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bảng VI của một bài so key rate QKD với thông lượng của bắt tay (handshake) PQC. Lỗi nặng nhất của bảng đó là gì?

- Chưa dùng bộ tham số ML-KEM lớn nhất
- Chưa đo trên sợi thật mà chỉ mô phỏng
- Thiếu thanh sai số trên cột QKD
- Hai cột khác đơn vị và khác mô hình đe doạ, nên bảng không so cái gì cả

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hai cột khác đơn vị và khác mô hình đe doạ, nên bảng không so cái gì cả**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Key rate QKD là bit khoá bí mật mỗi lần dùng kênh quang, còn thông lượng bắt tay PQC là byte trên một kênh dữ liệu đã có, trong một đơn vị thời gian. Đổi được sang cùng đơn vị chỉ sau khi nhân tốc độ lặp nguồn, và dù đổi xong thì hai con số vẫn đứng trong hai mô hình đe doạ khác nhau. Ba đáp án kia đều là thiếu sót thật nhưng chúng sửa được mà bảng vẫn vô nghĩa.

## Trong bốn công tắc của mô hình đe doạ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong bốn công tắc của mô hình đe doạ, công tắc nào làm CẢ QKD VÀ PQC cùng mất một con số an toàn để in?

- Kẻ tấn công tấn công thiết bị đầu cuối
- Độ dài khối hữu hạn
- Không có kênh cổ điển đã xác thực
- Kẻ tấn công có máy lượng tử quy mô lớn

## Trong bốn công tắc của mô hình đe doạ · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Kẻ tấn công tấn công thiết bị đầu cuối**

## Trong bốn công tắc của mô hình đe doạ · đáp (tiếp)
@phut: 1
@che-do: noi

Máy lượng tử chỉ giết phần cổ điển của hybrid, PQC hậu lượng tử và QKD đều còn số. Khối hữu hạn chỉ hạ con số QKD. Thiếu xác thực giết QKD mà PQC thì tự dựng được xác thực bằng chữ ký. Chỉ tấn công thiết bị đầu cuối làm cả hai mất nền: chứng minh của QKD là chứng minh về mô hình thiết bị, còn khoá của PQC nằm trong bộ nhớ thiết bị.

## Trong bốn công tắc của mô hình đe doạ · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là lý do nên đọc một bảng so sánh hai cột từ dòng mô hình đe doạ trở lên, không từ dòng con số trở xuống.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn so sánh sau có một câu không so cái gì cả. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Ở {{s003}} km, hệ QKD của chúng tôi cho key rate {{s035}} kbit mỗi giây với nguồn lặp {{s003}} MHz,
- tức khoảng 1,2·10⁻⁵ bit mỗi lần dùng kênh, nằm dưới chặn PLOB {{s004}} bit mỗi lần dùng kênh.
- Trong khi đó liên kết dữ liệu của chúng tôi chạy {{s013}} Gbit mỗi giây,
- nên QKD hiện chỉ đạt khoảng một phần triệu (ppm) thông lượng của kênh dữ liệu.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên QKD hiện chỉ đạt khoảng một phần triệu thông lượng của kênh dữ liệu.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu đầu đều hợp lệ: câu một khai cả tốc độ lặp nên đổi đơn vị được, câu hai đối chiếu đúng với chặn PLOB ở cùng đơn vị, câu ba chỉ là một dữ kiện. Câu này mới là chỗ sai, và nó sai về MỤC ĐÍCH chứ không về số học. Khoá bí mật và dữ liệu không cùng mục đích nên tỉ số giữa chúng không là một đại lượng nói lên điều gì:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

khoá dùng để làm mới khoá cho mật mã đối xứng, và {{s035}} kbit mỗi giây đủ cấp khoá AES-256 mới vài lần mỗi giây, tức ĐỦ cho đúng việc nó phải làm. Cách sửa: so khoá sinh được với nhu cầu làm mới khoá, không với thông lượng dữ liệu.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau có một chỗ làm con số chính của bài không kiểm được. Bấm vào chỗ đó.

- Sai bit lượng tử đo được là {{s036}} phần trăm, dưới ngưỡng {{s026}} phần trăm của BB84 một chiều,
- nên key rate sau sàng lọc một nửa là {{s037}} phần nghìn bit mỗi lần dùng kênh ở {{s003}} km,
- và chúng tôi báo con số này là key rate của hệ.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và chúng tôi báo con số này là key rate của hệ.**

Hai câu đầu đúng cả: {{s013}} trừ hai lần entropy nhị phân của {{s038}} cho {{s039}}, nhân một nửa và nhân η = {{s024}} ra 3,59·10⁻³, tức {{s040}} phần nghìn... và chính ở đây lộ ra chuyện thứ hai, rằng con số trong câu hai lệch một bậc so với phép tính, nên nó phải được kiểm lại. Nhưng lỗi NẶNG hơn nằm ở câu này:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

key rate vừa tính là key rate TIỆM CẬN, tức khối vô hạn, trong khi hệ thật chạy khối hữu hạn. Báo nó là key rate của hệ mà không khai độ dài khối, tham số an toàn và cách ước lượng tham số là in một con số không ai dựng lại được, và nó luôn cao hơn con số thật. Cách sửa: hai cột trong bảng, tiệm cận và khối hữu hạn, cộng độ dài khối ghi ngay trên đầu cột.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mở đầu sau có một câu reviewer gạch ngay. Bấm vào câu đó.

- Mật mã khoá công khai cổ điển đổ trước thuật toán Shor, nên phải đổi hệ.
- Mật mã hậu lượng tử (post-quantum cryptography) đứng trên giả định độ khó tính toán, tức an toàn có điều kiện.
- Phân phối khoá lượng tử (quantum key distribution) an toàn vô điều kiện, nên nó là lựa chọn đúng cho hệ của chúng tôi.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Phân phối khoá lượng tử an toàn vô điều kiện, nên nó là lựa chọn đúng cho hệ của chúng tôi.**

Hai câu đầu đều chính xác. Câu này sai ở hai chỗ độc lập, và cả hai đều là chỗ reviewer bắt.

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Thứ nhất, vô điều kiện là cách nói tắt cho không phụ thuộc năng lực tính toán của kẻ tấn công; chứng minh an toàn của QKD vẫn đứng trên giả định THIẾT BỊ ĐÚNG NHƯ MÔ HÌNH, nên bỏ cụm đó đi là nói quá, và đúng chỗ đó là nơi mọi tấn công QKD thật đã xảy ra (làm mù bộ tách, kênh phụ (side channel) thời gian).

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Thứ hai, nên nó là lựa chọn đúng không suy ra được từ an toàn vô điều kiện: QKD cần một kênh cổ điển đã xác thực mà bản thân nó không cung cấp, nên trong hệ thật nó nằm TRÊN mật mã hậu lượng tử hoặc trên khoá chia sẻ trước. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

viết an toàn không phụ thuộc năng lực tính toán, với giả định thiết bị đúng như mô hình, rồi nói rõ QKD bổ sung cho PQC chứ không thay thế.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đổi suy hao tổng ra dB: A = α·L, ở {{s001}} dB mỗi km và {{s032}} km thì A = {{s041}} dB
- Đổi dB ra hiệu suất: η = 10^(−A/10) = 10⁻⁴
- Lấy chặn PLOB: C = −log₂(1−η), ở đây khoảng 1,443·10⁻⁴ bit mỗi lần dùng kênh
- Số lần dùng kênh N = K / C với K = {{s031}} bit, ra khoảng {{s033}} triệu

## Dẫn lại từng bước · ca một (tiếp)
@phut: 1
@che-do: so

- Đọc chiều của kết quả: C là CHẶN TRÊN nên N là chặn DƯỚI, hệ thật chỉ cần nhiều lần dùng kênh hơn

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Viết key rate một chiều: R = {{s013}} − h₂(e) − h₂(e), một h₂ cho sửa lỗi và một cho khuếch đại riêng tư
- Gộp lại: R = {{s013}} − 2·h₂(e)
- Đặt R = {{s042}} và giải h₂(e) = {{s021}}
- Nghiệm của h₂(e) = {{s021}} trong khoảng từ {{s042}} tới {{s021}} cho e khoảng {{s043}}, tức {{s026}} phần trăm

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: sợi {{s003}} km · η = {{s024}} · chặn PLOB {{s004}} bit mỗi lần dùng kênh · PQC: một bắt tay hybrid {{s044}} byte · cả hai cột đang khai an toàn {{s045}} bit hoặc hơn

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Kẻ tấn công KHÔNG có máy lượng tử quy mô lớn** tắt đi: Kẻ tấn công có máy lượng tử chạy được Shor ở quy mô cần thiết.
- **Thiết bị đúng như mô hình** tắt đi: Kẻ tấn công tấn công thiết bị đầu cuối: làm mù bộ tách, dò kênh phụ thời gian và công suất, chạm vào bộ sinh số ngẫu nhiên, hoặc đọc bộ nhớ thiết bị chạy PQC.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Đã có kênh cổ điển ĐƯỢC XÁC THỰC giữa hai bên** tắt đi: Chưa có xác thực sẵn, hai bên chỉ có một kênh cổ điển công khai mà kẻ tấn công xen vào được.
- **Độ dài khối tiến tới vô hạn** tắt đi: Khối hữu hạn, ví dụ 10⁶ lần dùng kênh mỗi khối.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Suy hao {{s001}} dB mỗi km ở {{s002}} nm là con số do ITU-T G.652 quy định.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỔ**

ĐỔ ở chỗ DẪN NGUỒN, trong khi con số thì dùng được. Khuyến nghị G.652 không nêu giá trị điển hình, nó đặt TRẦN cho cáp: tối đa {{s046}} dB mỗi km ở {{s047}} nm và tối đa {{s007}} ở {{s002}} nm. Con số {{s001}} không có trong khuyến nghị. Tờ sản phẩm của sợi G.652.D bán ngoài thị trường bảo đảm ≤ {{s006}} ở {{s002}} nm, còn {{s001}} là con số tròn của giới kỹ thuật.

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

Trên {{s003}} km, ba con số cho {{s008}}, {{s009}} và {{s010}} dB; chênh {{s011}} dB là hơn {{s012}} lần hiệu suất kênh.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Key rate theo khoảng cách, vẽ cùng chặn PLOB trên thang log. Kéo khoảng cách và để ý trục dọc: nó là SỐ MŨ, nên một đoạn ngắn trên hình là nhiều bậc độ lớn.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.6` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The secret key rates in Table III are asymptotic. The authors do not state the block length, the security parameter, or how the parameter estimation is performed, so the reported rates cannot be compared with the finite-key results of the works cited in Table IV.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree, and we have separated the two regimes rather than mixing them. Table III now has two columns. The asymptotic column is kept because it is the only quantity that can be checked against the PLOB bound, and we state that check explicitly: at {{s003}} km with {{s027}} dB per km the channel efficiency is 1e-2 and the PLOB bound is {{s023}} bit per channel use, so every asymptotic rate we report lies below it by at least one order of magnitude.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The finite-key column is new and states its parameters in the column head: block length 1e9 channel uses, security parameter 1e-9, and parameter estimation by the Chernoff-Hoeffding bound described in Section IV-C. We also corrected the comparison in Table IV, which previously placed our asymptotic rate next to finite-key rates from the cited works.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

With both in the finite-key regime, the ordering of protocols B and C reverses relative to the asymptotic ordering, because the parameter-estimation penalty scales differently for the decoy-state and the no-decoy variants, and we now report that reversal as a result rather than hiding it. Finally, the block length we use is the one reachable in a single operational window of our testbed, and Section VI states how long that window is.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s013}}: nói rằng key rate tiệm cận là cách báo thông dụng. Đúng về thực hành, không trả lời được phản bác, vì reviewer đang hỏi về khả năng so sánh chứ không về thông lệ.
- Mức {{s018}}: thêm một dòng khai độ dài khối nhưng vẫn giữ bảng tiệm cận làm bảng chính và vẫn so với các bài khối hữu hạn.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s019}}: báo hai cột, tiệm cận và khối hữu hạn, khai độ dài khối cùng tham số an toàn, và sửa lại mọi câu so sánh để so cùng chế độ với cùng chế độ.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section VII concludes that QKD offers stronger security than post-quantum key exchange for the proposed architecture. This comparison is not meaningful as presented: the two are secured under different threat models, the QKD figures exclude the trusted-node and authentication infrastructure they require, and no attack surface on the terminal devices is considered.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have removed the claim that one is stronger than the other and replaced Section VII with a comparison that fixes the threat model first. Three changes. First, we state the type of assumption on each side: the post-quantum key exchange rests on the hardness of MLWE in a stated cost model, while QKD rests on physical law plus the assumption that the devices behave as modelled; these are different kinds of assumption and we no longer place them in a single bit-security column.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Second, we now count the infrastructure that QKD requires in our architecture: the classical channel must be authenticated before sifting and privacy amplification can run, and in our design that authentication is provided by ML-DSA signatures, so QKD in this architecture sits on top of post-quantum cryptography rather than replacing it; the trusted-node assumption needed to exceed {{s005}} km of fibre is also stated, with the consequence that keys exist in the clear at each trusted node.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Third, we add the endpoint threat model, under which neither side retains a security claim, and we say what follows from that: the two technologies are complementary at different layers, with post-quantum signatures carrying authentication and key establishment at the protocol layer, and QKD carrying symmetric key refresh on the links where the fibre budget allows it.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s013}}: mềm hoá câu kết luận thành QKD hứa hẹn hơn mà không đổi nội dung so sánh. Reviewer sẽ giữ nguyên ý kiến.
- Mức {{s018}}: thêm một đoạn bàn về mô hình đe doạ nhưng vẫn giữ bảng hai cột và vẫn kết luận một bên hơn bên kia.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s019}}: cố định mô hình đe doạ trước khi so, khai rõ loại giả thiết của từng bên, và tính cả hạ tầng xác thực cùng node trung gian tin cậy vào phía QKD.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.6` bấm thẻ.
