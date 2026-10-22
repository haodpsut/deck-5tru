---
tieu-de: Hình học quỹ đạo
phu-de: Trụ 3 NTN · module 3.1
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 67.5
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: NTN
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Cho cao độ và góc nâng tối thiểu, tôi tính được cửa sổ nhìn thấy, khoảng xiên (slant range) lớn nhất và trễ một chiều trong bao lâu, bằng giấy?

## Hình học quỹ đạo
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Trụ này có một trục duy nhất: **cao độ, góc nâng, vận tốc quỹ đạo**. Ba cái đó quyết định bậc độ lớn của trễ, Doppler, suy hao và tần suất handover. Module {{s001}} là chỗ cài ba cái đó vào tay, vì mọi module sau đều gọi lại chúng.

## Hình học quỹ đạo (tiếp)
@phut: 1
@che-do: noi

Lợi thế thực tế khi phản biện: reviewer hỏi *khoảng cách truyền của anh là bao nhiêu ở biên vệt phủ*, và anh phải trả lời được bằng một dòng tính chứ không bằng một lần chạy mô phỏng. Ở {{s002}} km, khoảng xiên ở chân trời là **{{s003}} km**, tức **{{s004}} lần** cao độ. Ai lấy {{s002}} km làm khoảng cách truyền thì sai gần {{s005}} lần, và sai đó đi thẳng vào bảng link budget.

## Hình học quỹ đạo (tiếp)
@phut: 1
@che-do: noi

Module này cũng là chỗ tập một việc khó hơn: **phân biệt giả thiết đổi kết luận với giả thiết chỉ đổi chữ số thứ ba**. Quỹ đạo tròn là loại thứ nhất. Trái Đất cầu là loại thứ hai.

## Khoảng xiên (slant range)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s006}} trên bốn.*

## Khoảng xiên (slant range) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khoảng cách thật từ thiết bị tới vệ tinh, hàm của cao độ `h` và góc nâng `ε`:

`d(ε) = R_E·[ sqrt( ((R_E+h)/R_E)² − cos²ε ) − sin ε ]`

## Khoảng xiên (slant range) · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cao độ chỉ là khoảng xiên ở đúng một điểm, khi vệ tinh ở đỉnh đầu**. Ở {{s002}} km, khoảng xiên chạy từ {{s002}} km (đỉnh đầu) tới {{s003}} km (chân trời), nên mọi con số tỉ lệ thuận với khoảng cách đổi trong một dải {{s004}} lần, và mọi con số theo bình phương khoảng cách đổi trong một dải {{s007}} lần.

## Khái niệm tầng 2
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Khái niệm tầng 2 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Góc tâm là góc tại tâm Trái Đất giữa thiết bị và vệ tinh, ở ngưỡng góc nâng tối thiểu:

`θ = 90° − ε_min − arcsin( (R_E/(R_E+h))·cos ε_min )`

Vệ tinh quét cung `2θ` trong thời gian `t = (2θ/360°)·T`.

## Khái niệm tầng 2 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cửa sổ nhìn thấy là đại lượng dẫn ra, không phải đại lượng độc lập**. Nó chỉ cần hai số là `h` và `ε_min`. Nên bài nào báo cửa sổ nhìn thấy mà không khai `ε_min` thì con số đó không kiểm được, và cũng không so được với bài khác.

## Hai loại giả thiết
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s009}} trên bốn.*

## Hai loại giả thiết · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bỏ giả thiết **quỹ đạo tròn**: `h` không còn là một số, nên `v`, `d`, cửa sổ và trễ đều thành hàm của thời gian. Kết luận đổi về bản chất, và mọi con số trung bình trong bài phải khai thêm trung bình theo cái gì.

## Hai loại giả thiết · đáp (tiếp)
@phut: 1
@che-do: noi

Bỏ giả thiết **Trái Đất cầu bán kính {{s010}} km**: bán kính thật chạy từ {{s011}} km ở cực tới {{s010}} km ở xích đạo, tức dao động {{s012}}. Đo thử thì `d` ở chân trời lệch {{s013}} và `θ` lệch {{s014}}, tức chỉ đổi ở chữ số thứ tư. Kết luận không đổi.

## Hai loại giả thiết · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **liệt kê giả thiết là chưa đủ, phải xếp hạng chúng**. Phản biện đánh vào loại thứ nhất. Dành chỗ trong bài để tự biện cho loại thứ hai là tự tố rằng mình không phân biệt được hai loại.

## Chu kỳ và vận tốc của quỹ đạo tròn
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`T = 2π·sqrt(a³/μ) v = sqrt(μ/a) a = R_E + h`

**Giả thiết nó đứng trên:**

- Quỹ đạo tròn, nên a là bán kính quỹ đạo và v không đổi dọc quỹ đạo
- Bài toán hai vật, chỉ có lực hấp dẫn của một khối cầu đồng nhất
- μ = 3,986·10¹⁴ m³/s², R_E = {{s010}} km, và khối lượng vệ tinh bỏ qua được so với Trái Đất

## Chu kỳ và vận tốc của quỹ đạo tròn · ghi chú
@phut: 1
@che-do: noi

Với quỹ đạo lệch tâm, `T` vẫn đúng nếu đọc `a` là bán trục lớn (định luật Kepler thứ ba), nhưng `v = sqrt(μ/a)` thì sai: vận tốc đổi theo vị trí. Đây là lý do `T` sống qua công tắc quỹ đạo tròn còn `v` thì không.

## Khoảng xiên, góc tâm, cửa sổ nhìn thấy
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`d(ε) = R_E·[ sqrt( ((R_E+h)/R_E)² − cos²ε ) − sin ε ] θ = 90° − ε − arcsin( (R_E/(R_E+h))·cos ε ) t = (2θ/360°)·T τ = d/c`

**Giả thiết nó đứng trên:**

## Khoảng xiên, góc tâm, cửa sổ nhìn thấy (tiếp)
@phut: 1
@che-do: so

- Trái Đất cầu bán kính R_E không đổi, và thiết bị nằm ngay trên mặt cầu
- Đường nhìn thẳng, không khúc xạ khí quyển và không che chắn địa hình
- Công thức cửa sổ t giả định vệ tinh đi qua đúng đỉnh đầu thiết bị, nên nó là CHẶN TRÊN cho mọi lượt qua khác
- c = {{s015}} km/s, và trễ chỉ là trễ lan truyền, không gồm trễ xử lý

## Khoảng xiên, góc tâm, cửa sổ nhìn thấy · ghi chú
@phut: 1
@che-do: noi

Kiểm nhanh bắt buộc làm trước khi dùng: đặt `ε = 90°` thì `cos ε = {{s016}}` và `sin ε = {{s006}}`, nên `d = R_E·[ (R_E+h)/R_E − {{s006}} ] = h`. Trường hợp biên này tính được bằng tay và nó bắt được gần hết lỗi gõ công thức.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s017}} | phút | Chu kỳ quỹ đạo tròn ở cao độ {{s002}} km
!so {{s018}} | km/s | Vận tốc quỹ đạo tròn ở cao độ {{s002}} km
!so {{s003}} | km | Khoảng xiên ở cao độ {{s002}} km và góc nâng 0°

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s019}} | km | Khoảng xiên ở cao độ {{s002}} km và góc nâng 40°
!so {{s020}} | phút | Cửa sổ nhìn thấy lớn nhất ở cao độ {{s002}} km với
!so {{s021}} | ms | Trễ lan truyền một chiều khi vệ tinh ở đúng đỉnh đầu

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s002}} km, góc nâng 0°. Trễ lan truyền một chiều là bao nhiêu ms?

h = {{s002}}, eps = {{s016}}, c = {{s022}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(6378⋆(Math.sqrt(Math.pow((6378+h)/6378,2)-Math.pow(Math.cos(eps⋆Math.PI/180),2))-Math.sin(eps⋆Math.PI/180)))/c`

Khoảng {{s023}} ms. Chia cho trễ ở đỉnh đầu {{s024}} ms thì được {{s004}} lần, đúng bằng tỉ số khoảng xiên {{s003}} km trên {{s002}} km. Đây là lý do lấy cao độ làm khoảng cách truyền sai gần {{s005}} lần ở biên, và vì FSPL đi theo bình phương khoảng cách, sai đó thành {{s025}} dB trong bảng link budget.

## Cao độ 1200 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s026}} km, góc nâng 30°. Khoảng xiên là bao nhiêu km?

h = {{s026}}, eps = {{s027}}

## Cao độ 1200 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`6378⋆(Math.sqrt(Math.pow((6378+h)/6378,2)-Math.pow(Math.cos(eps⋆Math.PI/180),2))-Math.sin(eps⋆Math.PI/180))`

Khoảng {{s028}} km, tức {{s029}} lần cao độ {{s026}} km. Ở {{s002}} km với cùng góc nâng 30° thì khoảng xiên là {{s030}} km, tức {{s031}} lần cao độ. Vậy tỉ số d/h GIẢM khi cao độ tăng, vì hình học tiến dần tới đường thẳng đứng. Đừng lẫn phát biểu này với phát biểu về cửa sổ nhìn thấy, cái đó tăng theo cao độ.

## Cao độ 1200 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s026}} km, góc nâng tối thiểu 10°, lượt qua đúng đỉnh đầu. Cửa sổ nhìn thấy là bao nhiêu phút?

h = {{s026}}, em = {{s032}}

## Cao độ 1200 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(2⋆(90-em-180/Math.PI⋆Math.asin(6378/(6378+h)⋆Math.cos(em⋆Math.PI/180)))/360)⋆2⋆Math.PI⋆Math.sqrt(Math.pow((6378+h)⋆1e3,3)/3.986e14)/60`

Khoảng {{s033}} phút, lớn hơn {{s034}} phút ở {{s002}} km đúng {{s035}} lần. Chu kỳ chỉ dài hơn {{s036}} lần ({{s037}} so với {{s038}} phút), nên mức tăng đến chủ yếu từ góc tâm θ, cái tăng từ 14,96° lên 24,02°, chứ không đến từ chu kỳ.

## Ở cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Ở cao độ {{s002}} km, tỉ số giữa khoảng xiên ở chân trời và khoảng xiên ở đỉnh đầu gần nhất với con số nào?

- {{s039}} lần
- {{s040}} lần
- {{s041}} lần
- {{s042}} lần

## Ở cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**{{s041}} lần**

{{s003}} km chia {{s002}} km bằng {{s004}} lần. Vì suy hao không gian tự do đi theo bình phương khoảng cách, {{s004}} lần thành 20·log₁₀(4,92) = {{s025}} dB. Hai con số này là cùng một dữ kiện viết ở hai đơn vị, nên nhớ một cái là có cái kia.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai cao độ {{s002}} km và báo cửa sổ nhìn thấy {{s043}} phút, không nói gì thêm. Thiếu đúng một dữ kiện để người khác dựng lại con số đó. Dữ kiện nào?

- Số vệ tinh trong chòm sao
- Băng tần sử dụng
- Độ nghiêng quỹ đạo
- Góc nâng tối thiểu ε_min

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Góc nâng tối thiểu ε_min**

Cửa sổ nhìn thấy chỉ cần hai số: h và ε_min. Ở {{s002}} km, ε_min = 10° cho {{s034}} phút, còn ε_min = 25° cho giá trị ngắn hơn hẳn. Độ nghiêng và số vệ tinh đổi TẦN SUẤT lượt qua chứ không đổi độ dài một lượt qua đỉnh đầu, còn băng tần thì không vào hình học.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn link budget sau có một dòng làm cả bảng lệch {{s025}} dB. Bấm vào dòng đó.

- Chòm sao mô phỏng ở cao độ {{s002}} km, góc nâng tối thiểu 10°.
- Tần số đường xuống {{s044}} GHz, băng thông {{s045}} MHz.
- Suy hao không gian tự do tính với khoảng cách truyền {{s002}} km, tức cao độ của vệ tinh.
- Biên dự phòng mưa (rain margin) {{s046}} dB, mức khả dụng (availability) mục tiêu {{s047}}.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Suy hao không gian tự do tính với khoảng cách truyền {{s002}} km, tức cao độ của vệ tinh.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng cách truyền là KHOẢNG XIÊN, không phải cao độ. Ở ε_min = 10° khoảng xiên là {{s048}} km, và ở chân trời là {{s003}} km. Lấy {{s002}} km làm khoảng cách truyền cho FSPL thấp hơn thực tế {{s049}} dB ở 10° và {{s025}} dB ở biên, nên mọi con số SNR, SE và thông lượng trong bài đều lạc quan một chiều. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

tính FSPL ở góc nâng xấu nhất mà bài còn phục vụ, rồi khai rõ góc nâng đó cạnh con số.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một câu không dẫn ra được từ dữ kiện đã khai. Bấm vào câu đó.

- Với h = {{s002}} km và ε_min = 10°, góc tâm Trái Đất (Earth central angle) là 14,96°.
- Cửa sổ nhìn thấy của một lượt qua đỉnh đầu là {{s034}} phút.
- Vậy thời gian phục vụ trung bình của một thiết bị là {{s034}} phút, và tần suất handover là {{s050}} lần mỗi giờ.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vậy thời gian phục vụ trung bình của một thiết bị là {{s034}} phút, và tần suất handover là {{s050}} lần mỗi giờ.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu đều đúng và dẫn được từ hình học. Mệnh đề thứ ba lẫn CỰC ĐẠI với TRUNG BÌNH: {{s034}} phút là cửa sổ của lượt qua đúng đỉnh đầu, tức chặn trên. Trung bình trên mọi lượt qua phụ thuộc phân bố góc nâng cực đại, nên nó là hàm của hình học chòm sao chứ không của một vệ tinh, và nó nhỏ hơn hẳn.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Thêm nữa, thời gian phục vụ còn ngắn hơn cửa sổ nhìn thấy vì còn chia chùm và chia tải. Cách sửa: gọi {{s034}} phút là chặn trên, rồi báo thời gian trú (dwell time) trung bình đo từ mô phỏng chòm sao kèm mô hình gán chùm.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Lực hấp dẫn đóng vai lực hướng tâm: μm/a² = m·v²/a
- Rút ra v = sqrt(μ/a)
- Chu kỳ là chu vi chia vận tốc: T = 2πa/v
- Thay v: T = 2πa/sqrt(μ/a) = 2π·sqrt(a³/μ)
- Đặt a = R_E + h với R_E = {{s010}} km để ra T theo cao độ

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Dựng tam giác tâm Trái Đất O, thiết bị U, vệ tinh S với OU = R_E và OS = R_E + h
- Góc tại U giữa UO kéo dài và US bằng 90° + ε, vì ε đo từ mặt phẳng ngang tại U
- Định lý hàm cos tại U: (R_E+h)² = R_E² + d² − 2·R_E·d·cos(90°+ε) = R_E² + d² + 2·R_E·d·sin ε

## Dẫn lại từng bước · ca hai (tiếp)
@phut: 1
@che-do: so

- Giải phương trình bậc hai theo d và lấy nghiệm dương: d = R_E·[ sqrt( ((R_E+h)/R_E)² − cos²ε ) − sin ε ]
- Kiểm biên ε = 90°: cos ε = {{s016}} và sin ε = {{s006}} cho d = h đúng bằng cao độ

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: h {{s002}} km · ε_min 10° → T {{s038}} phút · v {{s051}} km/s · d ở ε=0 là {{s003}} km · θ 14,96° · cửa sổ {{s034}} phút · trễ đỉnh đầu {{s024}} ms

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Quỹ đạo tròn** tắt đi: Quỹ đạo lệch tâm, độ lệch tâm e khác {{s016}}, nên cao độ đổi theo vị trí trên quỹ đạo.
- **Trái Đất cầu bán kính {{s010}} km** tắt đi: Dùng ellipsoid WGS-84, bán kính chạy từ {{s011}} km ở cực tới {{s010}} km ở xích đạo, dao động {{s012}}.
- **Vệ tinh đi qua đúng đỉnh đầu thiết bị** tắt đi: Lượt qua lệch tâm, góc nâng cực đại của lượt qua nhỏ hơn 90°.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Đường nhìn thẳng, không khúc xạ và không che chắn địa hình** tắt đi: Ở góc nâng thấp có khúc xạ khí quyển, cây, nhà, núi, nên góc nâng khả dụng cao hơn góc nâng hình học.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Hai thanh kéo, bảy con số. Kéo cao độ và góc nâng tối thiểu rồi đọc đồng thời chu kỳ, vận tốc, khoảng xiên, góc tâm, cửa sổ nhìn thấy và trễ. Đây là bảng mà anh phải dựng lại được bằng giấy.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.1` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV states an altitude of {{s002}} km and a minimum elevation of {{s032}} degrees, and then reports a single propagation delay and a single visibility window. Please clarify which elevation each reported value corresponds to, and justify the use of a per-satellite visibility window as the service time in your handover rate derivation.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have made the elevation dependence explicit. Table II now lists slant range and one-way propagation delay at three elevations for h = {{s002}} km: {{s002}} km and {{s021}} ms at zenith, {{s048}} km and {{s054}} ms at the {{s032}} degree service threshold, and {{s003}} km and {{s055}} ms at the geometric horizon. The {{s056}} dB spread between zenith and horizon is now carried through the link budget of Section V, which is evaluated at the worst served elevation rather than at nadir.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

On the second point, we agree the previous text conflated two quantities. The figure of {{s020}} minutes follows from theta = {{s057}} degrees and T = {{s017}} min and is the visibility window of a zenith pass, that is, an upper bound.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The handover rate in Section VI is now derived from a measured mean dwell time obtained from the constellation simulation with the beam assignment and load model stated in Section VI-A, and the {{s020}} minute figure is reported only as the bound it is. We also note which geometric assumptions matter:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

circular orbits change the conclusions, because h ceases to be a single number and v, d and the window all become functions of time, whereas replacing the spherical Earth by WGS-84 moves the third significant digit only.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s006}}: trả lời rằng {{s002}} km là cao độ danh định của chòm sao và {{s032}} độ là ngưỡng thông dụng trong TR {{s052}}. Đúng về bối cảnh, không trả lời được điều reviewer hỏi.
- Mức {{s008}}: ghi rõ trễ ứng với góc nâng nào, nhưng vẫn giữ cửa sổ nhìn thấy làm thời gian phục vụ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s046}}: lập bảng trễ và khoảng xiên ở ba góc nâng ({{s016}}, {{s032}}, {{s053}} độ), ghi rõ trễ {{s024}} ms là cận dưới và {{s023}} ms là chặn trên, và khai cửa sổ {{s034}} phút là CHẶN TRÊN của lượt qua đỉnh đầu chứ không phải thời gian phục vụ.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.1` bấm thẻ.
