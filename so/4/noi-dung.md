---
tieu-de: Số phải dẫn lại được trong *ba mươi giây*
phu-de: Trụ 4 6G Sec · số, công thức, và giả thiết của chúng
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 91.5
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
@notes: Deck này để đọc to, có đồng hồ. Không để đọc thầm.

## Luật của deck này
@phut: 1.5
@che-do: noi
@notes: Nói luật rồi bắt đầu. Đây là deck duy nhất của bộ mà đọc thầm là vô nghĩa.

{{TAKE_HOME}}

Mỗi slide hỏi một con số hoặc một công thức. Dẫn lại **bằng miệng trong ba mươi giây**, rồi mới lật. Bấm máy tính là tính sai mục đích.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`N_o = N_gd × N_hangmuc N_khathi = N_gd × N_nl N_biloai = N_gd × (N_hangmuc − N_nl) N_noibo = N_xapp × {{s002}} nếu vị thế nội bộ được cấp, ngược lại {{s003}}`

## Giả thiết
@phut: 1
@che-do: so

- Danh mục giao diện là đóng và đã biết hết, nên N_gd là một con số chứ không phải một chặn dưới
- Số hạng mục đe doạ soi trên mỗi giao diện là N_hangmuc = {{s001}}, lấy từ khung STRIDE
- Mỗi hạng mục đe doạ cần đúng một năng lực tương ứng, ánh xạ một-một, nên cấp N_nl năng lực thì có đúng N_nl hạng mục khả thi trên mỗi giao diện

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Vị thế nội bộ là năng lực thứ sáu trong danh sách, nên nó chỉ được cấp khi N_nl đạt {{s001}}
- Mỗi xApp của bên thứ ba mở thêm {{s002}} hạng mục nội bộ: sửa dữ liệu, tiết lộ thông tin, nâng quyền

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Số giao diện mở chính của O-RAN cần kể được tên, tính cả giao diện của lớp đám mây. Nhập số.

*Module {{s004}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s005}} | giao diện | module {{s004}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khung STRIDE có bao nhiêu hạng mục đe doạ? Đây là số hạng mục soi trên mỗi giao diện trong bộ đếm của module này.

*Module {{s004}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s001}} | hạng mục | module {{s004}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Bài của anh kể {{s005}} giao diện mở (E2, A1, O1, Open Fronthaul, O2) và soi từng giao diện bằng {{s001}} hạng mục STRIDE. Ma trận đe doạ đầy đủ có bao nhiêu ô?

gd = {{s005}}, hangMuc = {{s001}}

## Đáp
@phut: 1
@che-do: so

`gd × hangMuc`

{{s006}} ô. Đó là số ô mà bài của anh phải điền hoặc phải khai là không áp dụng, cùng với lý do. Một bảng đe doạ có {{s007}} dòng trong khi ma trận đầy đủ là {{s006}} ô thì chưa sai, nhưng nó buộc anh nói rõ {{s008}} ô kia đi đâu. Nếu không nói thì reviewer sẽ hỏi, và câu hỏi đó rất khó trả lời sau khi bài đã viết xong.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mô hình đe doạ (threat model) của anh cấp cho kẻ tấn công đúng {{s009}} trong {{s001}} năng lực, với ánh xạ một năng lực ứng một hạng mục. Trên {{s005}} giao diện, bao nhiêu ô bị loại vì không có năng lực tương ứng?

gd = {{s005}}, hangMuc = {{s001}}, nl = {{s009}}

## Đáp
@phut: 1
@che-do: so

`gd × (hangMuc - nl)`

{{s010}} ô bị loại, tức đúng hai phần ba ma trận {{s006}} ô. Hai phần ba là một tỉ lệ lớn, và đó chính là lý do danh sách bị loại phải vào bài: nó cho reviewer thấy mô hình đe doạ của anh là một quyết định có lý do, không phải một danh sách ngắn vì anh nghĩ chưa tới. Và nó còn là cổng tự kiểm:

## Đáp (tiếp)
@phut: 1
@che-do: so

nếu phòng vệ của anh tuyên bố chặn một ô nằm trong {{s010}} ô đã bị loại thì bài tự mâu thuẫn.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`N_moi = max(0, N_ke − N_dachuan) tyLeTuThoi = N_dachuan / N_ke N_moi_AI = max(0, min(N_ai, N_ke − N_dachuan))`

## Giả thiết
@phut: 1
@che-do: so

- N_ke là số cơ chế mà bài của anh kể trong phần đóng góp, đếm theo đúng danh mục in trong bài chứ không theo cảm nhận
- N_dachuan là số cơ chế trong danh mục đó lật ra được một số mục cụ thể của TS {{s011}}, nên nó đòi anh đã mở tài liệu chứ không đoán
- Một cơ chế chỉ được tính vào N_dachuan khi tra ra ĐÚNG MỤC, vì trích cả tài liệu là không khai được

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- N_ai là số cơ chế trong danh mục nhắm vào danh tính (identity) khối lượng công việc AI, phần mà chuẩn 5G không phủ

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trong TS {{s011}}, SEPP và bảo vệ liên mạng trên giao diện N32 được đặc tả ở mục số bao nhiêu? Nhập số mục cấp một.

*Module {{s012}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s013}} | số mục | module {{s012}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

TS {{s011}} chuẩn hoá bao nhiêu lược đồ bảo vệ định danh thuê bao để sinh SUCI từ SUPI? Nhập số.

*Module {{s012}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s009}} | lược đồ | module {{s012}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Bản thảo của anh kể {{s014}} cơ chế trong phần đóng góp. Lật danh mục thì {{s005}} cơ chế tra ra được số mục cụ thể trong TS {{s011}}. Bao nhiêu phần trăm danh mục không được tuyên bố là đóng góp mới?

dc = {{s005}}, cc = {{s014}}

## Đáp
@phut: 1
@che-do: so

`{{s015}} × dc / cc`

{{s016}}, tức gần hai phần ba danh mục phải chuyển từ phần đóng góp sang phần nền, kèm số mục. Gần hai phần ba là mức mà abstract buộc phải viết lại, vì câu dẫn của abstract thường chính là danh mục đó. Để ý con số này không nói bài dở: nó nói bài đang đặt phần nền vào chỗ của phần đóng góp, và đó là lỗi sửa được trong một buổi, trước khi reviewer sửa hộ.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mệnh đề hai của zero trust đòi xác thực lại theo từng yêu cầu. Một xApp gọi {{s017}} yêu cầu mỗi giây trong một cửa sổ {{s018}} giây, mỗi lần xác thực lại tốn {{s020}} ms thời gian CPU. Tổng thời gian CPU chỉ để xác thực lại là bao nhiêu giây?

rps = {{s017}}, cuaSo = {{s018}}, ms = {{s019}}

## Đáp
@phut: 1
@che-do: so

`rps × cuaSo × ms / {{s021}}`

{{s022}} giây CPU trong một cửa sổ {{s018}} giây, tức khoảng {{s023}} một lõi cho đúng một xApp. Con số nhỏ, và đó là điểm đáng nói: chi phí mật mã của xác thực lại từng yêu cầu thường KHÔNG phải rào cản, nên lập luận chống zero trust bằng chi phí tính toán là lập luận yếu.

## Đáp (tiếp)
@phut: 1
@che-do: so

Rào cản thật nằm ở chỗ khác, là có hay không một danh tính để gắn quyền vào, và có hay không hạ tầng khoá để kiểm danh tính đó qua biên liên mạng.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`D_tinh = r D_vong(n) = {{s024}} − ({{s024}} − r)^(1 + g·n) A(n) = D_vong(n) / r`

## Giả thiết
@phut: 1
@che-do: so

- Đây là MÔ HÌNH ĐÓNG DẠNG để thấy cơ chế, không phải số đo thực nghiệm; mọi con số nó sinh ra là con số của mô hình này, không phải của một hệ thật
- r là tỉ lệ đầu độc trên dữ liệu quan trắc tại mỗi bước, và được giữ không đổi theo thời gian

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- g là hệ số phản hồi, tức mức mà quyết định của mô hình đổi dữ liệu ở bước sau; g bằng {{s003}} nghĩa là không có phản hồi, tức bài toán thành phân loại tĩnh
- Số bước hiệu dụng là {{s024}} + g·n, nên ở n = {{s003}} thì vòng kín trùng đúng bản tĩnh và A(0) = {{s024}}

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Suy giảm được đo trên cùng một thang cho cả hai kiến trúc, nếu không thì hệ số A không có nghĩa

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Pierazzi và cộng sự khai bao nhiêu nhóm ràng buộc trong không gian vấn đề (problem space) mà một tấn công đối kháng khả thi phải thoả? Nhập số.

*Module {{s025}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s026}} | nhóm ràng buộc | module {{s025}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Module này kể mấy đường tấn công vào mô hình trong vòng điều khiển mạng mà kẻ tấn công KHÔNG cần truy cập máy chủ huấn luyện? Nhập số.

*Module {{s025}}.*

## Đáp
@phut: 1
@che-do: so
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

!so {{s002}} | đường tấn công | module {{s025}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Dùng đúng mô hình đóng dạng đã khai, suy giảm vòng kín là {{s024}} trừ ({{s024}} trừ r) luỹ thừa ({{s024}} cộng g nhân n). Với tỉ lệ đầu độc r = {{s029}}, hệ số phản hồi g = {{s030}} và n = {{s010}} bước, suy giảm vòng kín là bao nhiêu phần trăm?

r = {{s027}}, g = {{s028}}, n = {{s010}}

## Đáp
@phut: 1
@che-do: so

`{{s015}} × ({{s024}} - Math.pow(1 - r, {{s024}} + g × n))`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s031}}, trong khi bản phân loại tĩnh ở cùng mức đầu độc chỉ suy giảm {{s032}}, tức chênh gần mười lần. Nhắc lại cho đúng tư cách con số: đây là đầu ra của mô hình đóng dạng đã khai, không phải số đo thực nghiệm, nên nó dùng để lập luận về CƠ CHẾ chứ không dùng để báo kết quả. Cái dùng được trong bài báo là câu định tính kèm theo:

## Đáp (tiếp)
@phut: 1
@che-do: so

cùng một tỉ lệ đầu độc, hai kiến trúc cho hai đại lượng khác nhau, nên phải báo theo số bước.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Vẫn mô hình đóng dạng đó. Với r = {{s029}}, hệ số phản hồi g = {{s024}} và n = {{s033}} bước, hệ số khuếch đại của vòng kín so với bản tĩnh bằng bao nhiêu?

r = {{s027}}, g = {{s024}}, n = {{s033}}

## Đáp
@phut: 1
@che-do: so

`({{s024}} - Math.pow(1 - r, {{s024}} + g × n)) / r`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s034}} lần, trong khi số bước hiệu dụng là {{s035}}. Hai con số lệch nhau, và chỗ lệch đó là điều đáng học: hệ số khuếch đại luôn NHỎ HƠN số bước hiệu dụng, vì suy giảm bị chặn trên bởi {{s036}} nên đường cong bão hoà. Hệ quả đọc ngược: hệ số khuếch đại đạt mức cao nhất ở vùng đầu độc rất nhỏ, đúng vùng mà kiểm chất lượng dữ liệu thông thường không bắt được.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`P_thu(dBW) = EIRP(dBW) + G_thu(dBi) − 20·log10(4π·d/λ), với λ = c / f_L1`

## Giả thiết
@phut: 1
@che-do: so

- truyền lan không gian tự do, không che chắn, không đa đường: đây là ràng buộc chặt nhất và nó cho lề LẠC QUAN cho kẻ tấn công ở gần
- ăng ten bộ thu có cùng độ lợi về hướng nguồn giả và về hướng vệ tinh, tức bỏ qua giản đồ hướng, nên con số ra là chặn trên của lề
- λ tính từ tần số sóng mang L1, không gõ tay: λ = c / f_L1

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- mức so sánh là công suất thu DANH ĐỊNH quy định trong chuẩn, không phải công suất thu đo được tại hiện trường

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Mức công suất thu tối thiểu quy định cho tín hiệu GPS L1 C/A, tính bằng dBW. Nhập số âm.

*Module {{s037}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s038}} | dBW | module {{s037}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Tần số sóng mang GPS L1, tính bằng MHz. Cần con số này vì λ = c / f, và λ vào thẳng suy hao không gian tự do (free-space path loss).

*Module {{s037}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s039}} | MHz | module {{s037}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một nguồn giả mạo phát {{s033}} mW đẳng hướng, cách bộ thu {{s015}} m, ăng ten bộ thu {{s003}} dBi. Lề công suất của nó so với mức danh định -158,5 dBW bằng bao nhiêu dB?

ptW = {{s040}}, gr = {{s003}}, d = {{s015}}, fMHz = {{s039}}, pminDbw = {{s038}}

## Đáp
@phut: 1
@che-do: so

`10⋆Math.log10(ptW) + gr - 20⋆Math.log10(4⋆Math.PI⋆d/(299792458/(fMHz⋆1e6))) - pminDbw`

Khoảng {{s041}} dB, tức khoảng {{s042}} triệu lần mạnh hơn mức danh định. Con số này lớn tới mức nó đổi chiều lập luận: vấn đề của kẻ tấn công không phải đủ công suất, mà là hạ công suất cho vừa đủ để không lộ ra ở C/N0 và AGC.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một tấn công phát lại chạy qua bộ đệm trôi {{s024}} microgiây mỗi giây. Sau {{s033}} phút, sai lệch thời gian quy ra sai lệch khoảng cách giả bằng bao nhiêu mét?

c = {{s043}}, troi = {{s044}}, t = {{s045}}

## Đáp
@phut: 1
@che-do: so

`c × troi × t`

Khoảng {{s046}} nghìn mét, tức gần {{s046}} km. Con số này lớn hơn mọi sai số truyền lan, sai số đồng hồ hay sai số đa đường của một bộ thu bình thường vài bậc độ lớn, nên lệch thời gian TĂNG DẦN là dấu hiệu đọc được ngay từ nghiệm của chính bộ thu, không cần thêm phần cứng. Đó là lý do nó là dấu hiệu đặc trưng của phát lại.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`C_s = [ log₂(1 + γ_B) − log₂(1 + γ_E) ]⁺`

## Giả thiết
@phut: 1
@che-do: so

- biết γ_E, tức biết kênh của kẻ nghe; đây là giả thiết nặng nhất và cả module nói về nó
- kênh của kẻ nghe là bản suy giảm của kênh hợp pháp (kênh wiretap suy giảm), nên tốc độ bí mật đạt được là hiệu hai dung lượng
- độ dài khối vô hạn và mã đạt dung lượng; với khối hữu hạn (finite-key) thì tốc độ bí mật đạt được thấp hơn

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- đúng MỘT kẻ nghe, một ăng ten, không hợp tác với kẻ nghe khác
- nhiễu Gauss trắng cộng tính, công suất phát cố định, không có ăng ten nhiễu chủ động

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`P_out = P( C_s nhỏ hơn R_s ), với γ_E ~ phân bố khai trước, γ_B cho trước`

## Giả thiết
@phut: 1
@che-do: so

- khai được PHÂN BỐ của kênh kẻ nghe, thường là phân bố mũ cho γ_E tức pha đinh Rayleigh, cộng một phân bố cho vị trí của kẻ nghe
- pha đinh tựa tĩnh theo khối: trong một khối thì kênh không đổi, giữa các khối thì độc lập
- R_s là tốc độ bí mật mục tiêu, do thiết kế chọn trước chứ không chọn sau khi thấy kết quả

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- γ_B coi như biết và cố định, vì người nhận hợp pháp có phản hồi

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Kẻ nghe ở gần hơn, nên tỉ số tín hiệu trên nhiễu của nó không nhỏ hơn của người nhận hợp pháp. Dung lượng bí mật (secrecy capacity) bằng bao nhiêu bit mỗi ký hiệu?

*Module {{s047}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s003}} | bit mỗi ký hiệu | module {{s047}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Người nhận hợp pháp ở {{s010}} dB, kẻ nghe ở {{s033}} dB. Dung lượng bí mật bằng bao nhiêu bit mỗi ký hiệu? Đây là điểm neo nên nhớ thuộc.

*Module {{s047}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s048}} | bit mỗi ký hiệu | module {{s047}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Người nhận hợp pháp ở {{s049}} dB, kẻ nghe ở {{s005}} dB. Dung lượng bí mật bằng bao nhiêu bit mỗi ký hiệu?

gbdB = {{s049}}, gedB = {{s005}}

## Đáp
@phut: 1
@che-do: so

`Math.max(0, Math.log2(1+Math.pow(10,gbdB/10)) - Math.log2(1+Math.pow(10,gedB/10)))`

Khoảng {{s050}} bit mỗi ký hiệu. Để ý: cách biệt vẫn đúng {{s033}} dB như ca {{s010}} dB với {{s033}} dB, mà kết quả nhỏ hơn {{s051}} bit của ca đó. Cách biệt dB không ánh xạ thành số bit, vì số {{s024}} cộng thêm trong mỗi log đè nặng hơn khi tỉ số tín hiệu trên nhiễu thấp. Ai lấy hiệu dB chia cho {{s052}} sẽ ra {{s053}} bit cho cả hai ca, tức sai cả hai.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Người nhận hợp pháp cố định ở {{s010}} dB. Kẻ nghe có tỉ số tín hiệu trên nhiễu phân bố mũ với trung bình {{s033}} dB. Tốc độ bí mật mục tiêu là {{s009}} bit mỗi ký hiệu. Xác suất mất bí mật (secrecy outage probability) bằng bao nhiêu phần trăm?

gbdB = {{s010}}, rs = {{s009}}, gebardB = {{s033}}

## Đáp
@phut: 1
@che-do: so

`100⋆Math.exp(-((1+Math.pow(10,gbdB/10))/Math.pow(2,rs) - 1)/Math.pow(10,gebardB/10))`

Khoảng {{s054}}, tức cỡ một phần mười khối tin không đạt mục tiêu bí mật, trong khi dung lượng bí mật tức thời ở cùng cặp {{s010}} dB với {{s033}} dB vẫn là {{s051}} bit, nghe như thừa sức cho mục tiêu {{s009}} bit. Hai con số không mâu thuẫn: một cái nói về MỘT thực hiện kênh, cái kia nói về cả phân bố.

## Đáp (tiếp)
@phut: 1
@che-do: so

Và chỉ cần đổi trung bình của phân bố lên {{s010}} dB là con số này lên khoảng {{s055}}, trong khi dung lượng tức thời đứng yên.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`trích dẫn khai được = số tài liệu + số bản (Release hoặc version) + mục cụ thể + ngày tra`

## Giả thiết
@phut: 1
@che-do: so

- số mục chỉ có nghĩa BÊN TRONG một số bản: cùng một tài liệu, hai bản khác nhau có thể đánh số mục khác nhau, nên thiếu số bản thì số mục không trỏ tới đâu
- tài liệu chuẩn sống động, tức có bản mới theo thời gian, nên ngày tra là phần của trích dẫn chứ không phải phần của phép lịch sự

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- thẩm quyền của câu được trích đến từ LOẠI tài liệu: đặc tả thì phát ra yêu cầu, báo cáo nghiên cứu thì không
- nếu dùng để đỡ một tuyên bố bắt buộc thì phải trích câu có động từ quy phạm trong mục đó, không trích tiêu đề mục

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Luật trích chuẩn của nhà đòi mỗi trích dẫn phải khai mấy trường thì người ngoài mới kiểm được mà không cần hỏi lại?

*Module {{s056}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s026}} | trường | module {{s056}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Đặc tả kiến trúc an ninh của hệ 5G, số tài liệu TS {{s011}} của 3GPP, xuất hiện lần đầu ở bản Release thứ mấy? Cần con số này để biết ngay một trích dẫn ghi số bản sớm hơn là trích dẫn không tồn tại.

*Module {{s056}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s049}} | Release | module {{s056}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Bài tập ở cuối module có {{s014}} trích dẫn, trong đó {{s002}} cái không khai được. Tỉ lệ không khai được là bao nhiêu phần trăm?

loi = {{s002}}, tong = {{s014}}

## Đáp
@phut: 1
@che-do: so

`{{s015}} × loi / tong`

{{s057}}. Con số này cao hơn hẳn cảm giác của người viết, và đó là điều đáng chú ý: ba lỗi trong tám trích dẫn nghe như ít, còn gần bốn trên mười trích dẫn không khai được thì nghe như một danh mục chưa kiểm. Cùng một dữ kiện, hai cách đọc, và reviewer đọc theo cách thứ hai.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Danh mục {{s014}} trích dẫn, {{s002}} cái không khai được, nên {{s005}} cái sạch. Người đọc mở {{s002}} cái khác nhau, lấy ngẫu nhiên không hoàn lại. Xác suất họ bắt được ít nhất một lỗi là bao nhiêu phần trăm?

sach = {{s005}}, tong = {{s014}}

## Đáp
@phut: 1
@che-do: so

`{{s015}} × ({{s024}} - (sach⋆(sach-1)⋆(sach-2))/(tong⋆(tong-1)⋆(tong-2)))`

Khoảng {{s058}}, tức mở ba trích dẫn trong tám thì hơn bốn lần trên năm là thấy vấn đề, vì xác suất ba cái đều sạch chỉ là {{s033}} trên {{s059}}. Con số này nói ngược hẳn với mô phỏng ở trên, và lý do là ở đó danh mục dài {{s017}} cái với tỉ lệ lỗi {{s060}}: chính TỈ LỆ lỗi quyết định xác suất bị bắt, không phải số lỗi.

## Đáp (tiếp)
@phut: 1
@che-do: so

Danh mục tám cái với ba lỗi có tỉ lệ {{s057}}, gần bốn lần cao hơn.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`μ_B = d/n + ({{s024}} − d)·[ q + ({{s024}} − q)·(1 − a) ] W₉₅ = ln(20) / (μ_B − λ_B) r = |S| / sqrt(S² + σ²), S = (dW₉₅/da)·sd(a)`

## Giả thiết
@phut: 1
@che-do: so

- dung lượng tổng của ô chuẩn hoá về {{s024}}, và thời gian phục vụ trung bình ở dung lượng đầy là {{s024}} ms, nên mọi trễ ở đây đọc theo ms
- slice B chào tải cố định λ_B = {{s061}} trong suốt phép đo; chỉ tải a của slice A thay đổi
- phần dành riêng d chia đều cho n slice và không cho vay, nên slice B luôn giữ d/n dù nó không dùng hết

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- trong phần dùng chung {{s024}} − d, bộ lập lịch bảo đảm cho slice B hạn mức tối thiểu q, phần còn lại chia theo tải và slice A nhả ngay phần nó không dùng
- hàng đợi M/M/1 cho slice B: đến Poisson, thời gian phục vụ mũ, một hàng đợi duy nhất, nên thời gian lưu trú phân bố mũ với tham số μ_B − λ_B và phân vị {{s062}} bằng ln(20) chia cho tham số đó

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- n − {{s009}} slice còn lại không có tải, đây là giả thiết bi quan nhất cho việc dành riêng và phải khai
- nhiễu đo σ = {{s005}} ms trong phân vị {{s062}} của slice B, độc lập với tải slice A; quét a đều trên toàn dải nên sd(a) = 1/sqrt(12)

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khi anh viết hai slice được cô lập, một phát biểu đứng được phải tách rõ bao nhiêu tầng cô lập? Kể tên từng tầng trước khi nhập số.

*Module {{s063}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s026}} | tầng | module {{s063}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Mức dành riêng đặt {{s036}}, mỗi slice giữ một khối tài nguyên vô tuyến riêng và không cho vay. Trong mô hình của module, hệ số tương quan giữa tải slice A và phân vị {{s062}} độ trễ của slice B bằng bao nhiêu?

*Module {{s063}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s003}} |  | module {{s063}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một ô có bốn slice, mức dành riêng đặt {{s036}} nên dung lượng chia đều và không cho vay. Slice A chào tải {{s066}}, slice B chào {{s061}}, hai slice còn lại không có tải. Bao nhiêu phần trăm dung lượng tổng bị mắc kẹt?

d = {{s024}}, n = {{s026}}, a = {{s064}}, lamB = {{s065}}

## Đáp
@phut: 1
@che-do: so

`100⋆(Math.max(d/n - a, {{s003}}) + Math.max(d/n - lamB, {{s003}}) + (n-2)⋆d/n)`

## Đáp (tiếp)
@phut: 1
@che-do: so

Đúng {{s067}}, tức một nửa dung lượng của ô không ai dùng được. Hai slice không có tải giữ trọn hai khối một phần tư, và cô lập tĩnh nghĩa là không cho vay, nên hai khối đó mắc kẹt. Con số này là cái giá của trạng thái tương quan bằng {{s003}}, và nó tăng theo số slice: đó là lý do dành riêng {{s036}} không phải một lựa chọn vận hành, và là lý do hạn mức tối thiểu tồn tại.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Ba slice, không dành riêng tĩnh, hạn mức tối thiểu của slice B là {{s070}}, slice B chào tải {{s061}}. Slice A đẩy tải lên {{s071}}. Phân vị {{s062}} độ trễ của slice B bằng bao nhiêu ms?

d = {{s003}}, n = {{s002}}, q = {{s068}}, a = {{s069}}, lamB = {{s065}}

## Đáp
@phut: 1
@che-do: so

`Math.log(20)/(d/n + (1-d)⋆(q + (1-q)⋆(1-a)) - lamB)`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s072}} ms, so với {{s073}} ms khi slice A ở tải {{s074}}. Slice B không đổi gì cả: cùng tải, cùng hạn mức, cùng cấu hình, mà trễ đuôi của nó xấu đi hơn ba lần vì một slice khác bận hơn. Đây là kênh phụ (side channel) nhìn từ phía nạn nhân, và nó cũng là đường từ chối dịch vụ nhìn từ phía slice A. Hạn mức {{s070}} không chặn được chuyện này, nó chỉ đặt một sàn cho dung lượng:

## Đáp (tiếp)
@phut: 1
@che-do: so

muốn chặn hẳn thì phải đẩy hạn mức lên {{s024}} hoặc dành riêng tĩnh, và cả hai đều có giá.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Δr = c / (2·B) Δv = λ / (2·T_obs) Δθ ≈ λ / (N·d) = 2/N với d = λ/2 A_oô = Δr · R · Δθ`

## Giả thiết
@phut: 1
@che-do: so

- xung nén lý tưởng với cửa sổ chữ nhật, không trọng số giảm búp phụ; mọi cửa sổ thật làm phân giải xấu đi theo một hệ số lớn hơn {{s024}}, nên đây là trần chứ không phải phép đo
- tỉ số tín hiệu trên nhiễu đủ cao để độ chính xác đạt tới trần phân giải; nếu không thì ba con số trên là chặn, và độ chính xác thật xấu hơn theo cận Cramer Rao

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- mục tiêu đứng yên trong suốt T_obs và chuyển động dọc đường ngắm, nên phân giải vận tốc nói về một thành phần Doppler duy nhất
- dàn ăng ten tuyến tính đều, khoảng cách nửa bước sóng, mục tiêu ở hướng vuông góc với dàn; lệch khỏi hướng đó thì búp rộng ra và phân giải góc xấu đi

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- cự ly tham chiếu R phải được khai khi quy ô bất định ra mét vuông, vì phân giải góc có đơn vị radian chứ không phải mét
- c = {{s043}} m/s, giá trị chính xác theo định nghĩa của mét

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Một hệ cảm biến tích hợp (integrated sensing) dùng băng thông {{s015}} MHz. Phân giải cự ly (range resolution) bằng bao nhiêu mét?

*Module {{s075}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s076}} | m | module {{s075}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng hệ đó nâng băng thông lên {{s024}} GHz. Phân giải cự ly bằng bao nhiêu mét?

*Module {{s075}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s077}} | m | module {{s075}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Sóng mang {{s078}} GHz, thời gian quan sát {{s033}} ms. Phân giải vận tốc bằng bao nhiêu mét trên giây?

*Module {{s075}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s079}} | m/s | module {{s075}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Dàn ăng ten tuyến tính đều, {{s080}} phần tử, khoảng cách nửa bước sóng, mục tiêu ở hướng vuông góc với dàn. Phân giải góc xấp xỉ bao nhiêu radian?

*Module {{s075}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s081}} | radian | module {{s075}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Sóng mang {{s078}} GHz, nhưng cửa sổ quan sát chỉ còn {{s009}} ms vì hệ phải trả tài nguyên lại cho truyền thông. Phân giải vận tốc bằng bao nhiêu mét trên giây?

c = {{s043}}, fGhz = {{s078}}, Tms = {{s009}}

## Đáp
@phut: 1
@che-do: so

`(c/(fGhz⋆1e9))/(2⋆Tms⋆1e-3)`

Khoảng {{s082}} m/s, so với {{s083}} m/s khi cửa sổ là {{s033}} ms. Rút ngắn cửa sổ năm lần làm phân giải vận tốc xấu đúng năm lần, vì quan hệ là tỉ lệ nghịch với thời gian quan sát. Đây là đòn giảm nhẹ duy nhất trong module mà có vẻ dùng được, nên phải nói rõ giới hạn của nó:

## Đáp (tiếp)
@phut: 1
@che-do: so

ở {{s082}} m/s thì mạng vẫn phân biệt được xe chạy với người đi bộ, và phân giải cự ly thì không đổi một chút nào vì nó không đi qua thời gian quan sát.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Hệ dùng {{s024}} GHz băng thông và dàn {{s085}} phần tử với khoảng cách nửa bước sóng. Ở cự ly tham chiếu {{s015}} m, diện tích ô bất định bằng bao nhiêu mét vuông?

c = {{s043}}, Bhz = {{s084}}, R = {{s015}}, N = {{s085}}

## Đáp
@phut: 1
@che-do: so

`(c/(2⋆Bhz))⋆R⋆(2/N)`

Khoảng {{s086}} m², tức một ô chừng nửa mét mỗi chiều: hai người đứng cách nhau hơn thế thì mạng tách ra được thành hai mục tiêu. Hai chỗ phải khai cạnh con số này. Một, cự ly tham chiếu {{s015}} m là giả thiết, vì phân giải góc có đơn vị radian nên ô bất định nở ra tuyến tính theo cự ly.

## Đáp (tiếp)
@phut: 1
@che-do: so

Hai, đây là trần của khả năng phân biệt ở tỉ số tín hiệu trên nhiễu cao, nên ô thật rộng hơn và con số này là chặn có lợi cho lập luận riêng tư, phải khai là chặn.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: tiêu chí là thời gian dẫn, không phải đáp đúng.

Số nào dẫn lại quá ba mươi giây thì nó chưa thuộc, dù đáp đúng.
