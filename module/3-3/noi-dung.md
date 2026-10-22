---
tieu-de: Doppler và định thời
phu-de: Trụ 3 NTN · module 3.3
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 71
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

Doppler đỉnh của tôi là bao nhiêu kHz, nó lớn hơn khoảng cách sóng mang con bao nhiêu lần, và vì sao điều đó buộc phải bù trước?

## Hai cực trị, hai chỗ khác nhau
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này có một con số và một cái bẫy.

Con số: ở cao độ {{s001}} km, thành phần vận tốc theo đường ngắm (line of sight velocity) lớn nhất là **{{s002}} km/s**, không phải {{s003}} km/s. Lấy vận tốc quỹ đạo thay cho thành phần theo đường ngắm thổi Doppler lên **{{s004}}**. Doppler đỉnh ở {{s005}} GHz là khoảng **{{s006}} kHz**, tức **{{s007}} lần** khoảng sóng mang con {{s008}} kHz.

## Hai cực trị, hai chỗ khác nhau (tiếp)
@phut: 1
@che-do: noi

Con số {{s007}} là con số mà phản biện sẽ hỏi, vì nó lớn hơn {{s009}}, và lớn hơn {{s009}} nghĩa là trực giao (orthogonality) của OFDM không tự sống được.

## Hai cực trị, hai chỗ khác nhau (tiếp)
@phut: 1
@che-do: noi

Cái bẫy: **Doppler cực đại ở chân trời, nhưng TỐC ĐỘ BIẾN THIÊN Doppler (Doppler rate) cực đại ở đỉnh đầu.** Hai cực trị ở hai chỗ khác nhau, và ở đỉnh đầu thì Doppler bằng {{s010}} trong khi tốc độ biến thiên của nó lớn nhất, khoảng {{s011}} kHz mỗi giây ở {{s005}} GHz. Đây là điểm dễ nhớ sai nhất của cả trụ {{s012}}.

## Hai cực trị, hai chỗ khác nhau (tiếp)
@phut: 1
@che-do: noi

Nhớ sai chỗ này thì phần thiết kế vòng bám pha của bài báo sai ở đúng điểm mà reviewer vô tuyến đọc đầu tiên.

Và có một tầng thứ ba, tầng của tầng {{s013}}: nếu thiết bị không có ephemeris với GNSS thì không bù trước được, dịch tần vượt khoảng sóng mang con, nên mọi con số BER trong bài **không còn tính được** bằng mô hình đang dùng. Không phải xấu hơn.

## Khái niệm tầng 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s009}} trên bốn.*

## Khái niệm tầng 1 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Doppler chỉ nghe thấy phần vận tốc dọc theo đường nối thiết bị với vệ tinh:

`f_d = (v_r/c)·f_c` với `v_r = v·(R_E/(R_E+h))·cos ε`

Điểm phải nhớ: **v_r luôn nhỏ hơn v, và nhỏ hơn đúng hệ số R_E/(R_E+h)·cos ε**. Ở {{s001}} km thì hệ số R_E/(R_E+h) bằng {{s014}}, nên ngay ở chân trời v_r chỉ là {{s002}} km/s. Dùng {{s003}} km/s thay cho {{s002}} km/s thổi Doppler lên {{s004}}, và {{s004}} là đúng bằng h/R_E.

## Hai cực trị của một lượt qua
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s012}} trên bốn.*

## Hai cực trị của một lượt qua · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Vì `v_r ∝ cos ε`, Doppler lớn nhất ở `ε = {{s010}}` (chân trời) và bằng {{s010}} ở `ε = 90°` (đỉnh đầu).

Tốc độ biến thiên Doppler thì ngược: nó tỉ lệ với `d²d/dt²`, và ở đỉnh đầu đạo hàm bậc hai của khoảng cách lớn nhất, bằng `R_E·v²/((R_E+h)·h)`. Ở {{s001}} km và {{s005}} GHz, tốc độ biến thiên ở đỉnh đầu là khoảng {{s011}} kHz mỗi giây.

## Hai cực trị của một lượt qua · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **ở đỉnh đầu Doppler bằng {{s010}} nhưng tốc độ biến thiên của nó lớn nhất**. Đó là thời điểm khó nhất cho vòng bám pha, chứ không phải thời điểm dễ nhất. Ai nhớ hai cực trị ở cùng một chỗ sẽ thiết kế vòng bám sai ở đúng điểm quan trọng.

## Khái niệm tầng 4
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s013}} trên bốn.*

## Khái niệm tầng 4 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mô hình kênh một tap trên mỗi sóng mang con, tức mô hình mà gần hết bài báo dùng để tính BER, đứng trên giả thiết các sóng mang con còn trực giao. Giả thiết đó đòi dịch tần còn lại phải nhỏ so với khoảng sóng mang con.

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

Thiết bị bù trước được vì nó biết hai thứ: vị trí của mình (GNSS) và quỹ đạo vệ tinh (ephemeris phát trong tín hiệu hệ thống). Thiếu một trong hai thì dịch tần còn lại là toàn bộ Doppler, tức {{s006}} kHz ở Ka, tức {{s007}} lần khoảng sóng mang con {{s008}} kHz.

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **khi dịch tần vượt khoảng sóng mang con thì BER không xấu hơn, nó hết định nghĩa** trong mô hình đang dùng, vì mô hình đó đặt nhiễu giữa các sóng mang con bằng {{s010}}. Phân biệt được hai câu đó là chỗ phân biệt một bài báo đọc được với một bài báo bị trả về.

## Doppler và thành phần vận tốc theo đường ngắm
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`f_d = (v_r/c)·f_c v_r(ε) = v·(R_E/(R_E+h))·cos ε v_r,max = v·R_E/(R_E+h) tại ε = {{s010}}`

**Giả thiết nó đứng trên:**

## Doppler và thành phần vận tốc theo đường ngắm (tiếp)
@phut: 1
@che-do: so

- Quỹ đạo tròn, nên v = sqrt(μ/(R_E+h)) không đổi trong lượt qua
- Thiết bị cố định trên mặt đất, nên vận tốc tương đối chỉ do vệ tinh; với thiết bị trên máy bay phải cộng thêm
- Hình học phẳng của một lượt qua, Trái Đất cầu bán kính R_E
- c = {{s015}} m/s, và chỉ xét Doppler bậc một, bỏ hiệu ứng tương đối tính

## Doppler và thành phần vận tốc theo đường ngắm · ghi chú
@phut: 1
@che-do: noi

Dẫn gọn quan hệ v_r theo ε: trong tam giác tâm Trái Đất, định lý hàm sin cho `sin φ = d·cos ε/(R_E+h)` với φ là góc tâm. Đạo hàm khoảng cách cho `dd/dt = R_E·v·sin φ/d`, thay sin φ vào thì d triệt tiêu và còn `dd/dt = v·(R_E/(R_E+h))·cos ε`, đúng dạng trên. Kiểm nhanh: ε = 90° cho cos ε = {{s010}} nên v_r = {{s010}}, tức Doppler bằng {{s010}} ở đỉnh đầu.

## Tốc độ biến thiên Doppler ở đỉnh đầu, và định thời
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`df_d/dt = (f_c/c)·d²d/dt² d²d/dt²|_{ε=90°} = R_E·v²/((R_E+h)·h) RTT = 2d/c`

**Giả thiết nó đứng trên:**

- Lượt qua đúng đỉnh đầu, nên biểu thức cho d²d/dt² ở trên là giá trị CỰC ĐẠI của lượt qua đó
- Quỹ đạo tròn với tốc độ góc ω = v/(R_E+h) không đổi
- Khai triển d(t) quanh đỉnh đầu tới bậc hai: d ≈ h + R_E(R_E+h)ω²t²/(2h)
- RTT chỉ gồm trễ lan truyền, không gồm trễ xử lý, xếp hàng hay trễ chặng feeder

## Tốc độ biến thiên Doppler ở đỉnh đầu, và định thời · ghi
@phut: 1
@che-do: noi

Với NR, trễ vòng vượt ngân sách định thời của mạng mặt đất nên cần `K_offset` để dịch các mốc thời gian của HARQ và của truy nhập ngẫu nhiên; tham số này và cách khai báo nó nằm trong 3GPP TS {{s016}} và TR {{s017}}. Hệ quả cho phần mô phỏng: số lần truyền lại của HARQ phải khai lại cho RTT {{s018}} ms, không bê nguyên cấu hình mặt đất.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s019}} | km/s | Thành phần vận tốc theo đường ngắm lớn nhất
!so {{s020}} | kHz | Doppler đỉnh ở băng Ka
!so {{s021}} | kHz | Doppler đỉnh ở băng S

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s008}} | kHz | Khoảng cách giữa hai sóng mang con của NR ở numerology μ
!so {{s022}} | lần | Tỉ số giữa Doppler đỉnh ở {{s005}} GHz (cao độ {{s001}} km)
!so {{s023}} | ms | Trễ vòng chỉ tính lan truyền của chặng dịch vụ

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s001}} km, góc nâng 0°, tần số sóng mang {{s024}} GHz. Doppler đỉnh là bao nhiêu kHz?

h = {{s001}}, eps = {{s010}}, fc = {{s024}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.sqrt(3.986e14/((6378+h)⋆1e3))⋆(6378/(6378+h))⋆Math.cos(eps⋆Math.PI/180)/299792458⋆fc⋆1e9/1e3`

Khoảng {{s025}} kHz, tức {{s026}} lần khoảng sóng mang con {{s008}} kHz và {{s027}} lần khoảng sóng mang con {{s028}} kHz. Lên băng Q hay V thì tỉ số này còn tăng tuyến tính theo tần số, nên bù trước Doppler (Doppler pre-compensation) không phải một tuỳ chọn thiết kế mà là điều kiện để mô hình kênh của bài báo còn có nghĩa.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo dùng vận tốc quỹ đạo thay cho thành phần theo đường ngắm để tính Doppler đỉnh, ở cao độ {{s001}} km. Con số bị thổi lên bao nhiêu phần trăm?

h = {{s001}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆h/6378`

Khoảng {{s004}}. Để ý biểu thức gọn đến mức này: tỉ số v/v_r,max bằng (R_E+h)/R_E, nên mức thổi lên đúng bằng h/R_E. Ở {{s001}} km là {{s004}}, ở {{s029}} km là {{s030}}. Doppler đỉnh ở {{s005}} GHz từ {{s006}} kHz thành {{s031}} kHz, và sai số đó đi thẳng vào phần thiết kế dải bắt của vòng bám tần.

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s001}} km, băng S với tần số sóng mang {{s032}} GHz. Tốc độ biến thiên Doppler ở đỉnh đầu là bao nhiêu kHz mỗi giây?

h = {{s001}}, fc = {{s032}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`6378e3⋆3.986e14/(Math.pow((6378+h)⋆1e3,2)⋆h⋆1e3)/299792458⋆fc⋆1e9/1e3`

Khoảng {{s033}} kHz mỗi giây, nhỏ hơn giá trị ở {{s005}} GHz đúng {{s034}} lần vì biểu thức tuyến tính theo tần số sóng mang. Và nhớ chỗ nó sống: con số này là của ĐỈNH ĐẦU, nơi Doppler bằng {{s010}}, chứ không phải của chân trời, nơi Doppler cực đại.

## Trong một lượt qua đỉnh đầu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong một lượt qua đỉnh đầu, thời điểm nào khó nhất cho vòng bám pha?

- Lúc vệ tinh ở đỉnh đầu, vì Doppler bằng {{s010}} nhưng tốc độ biến thiên lớn nhất
- Lúc vệ tinh lặn, vì Doppler đổi dấu
- Khó như nhau, vì vòng bám chỉ quan tâm độ lớn Doppler
- Lúc vệ tinh mọc ở chân trời, vì Doppler lớn nhất

## Trong một lượt qua đỉnh đầu · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Lúc vệ tinh ở đỉnh đầu, vì Doppler bằng {{s010}} nhưng tốc độ biến thiên lớn nhất**

## Trong một lượt qua đỉnh đầu · đáp (tiếp)
@phut: 1
@che-do: noi

Ở chân trời Doppler lớn nhưng gần như không đổi, nên một vòng bậc một bám được. Ở đỉnh đầu Doppler bằng {{s010}} trong khi tốc độ biến thiên cực đại, khoảng {{s011}} kHz mỗi giây ở {{s005}} GHz, nên vòng bậc một chạy sau liên tục và dồn sai số pha. Doppler đổi dấu không phải vấn đề riêng: nó chính là lúc đi qua {{s010}} ở đỉnh đầu.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo mô phỏng NB-IoT qua vệ tinh LEO cho thiết bị cảm biến giá rẻ, không có GNSS, và báo BER tính bằng mô hình một tap trên mỗi sóng mang con. Vấn đề nặng nhất ở đâu?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Thiếu mô hình kênh nhiều đường
- Băng thông mô phỏng quá hẹp so với thực tế
- Không bù trước được Doppler nên giả thiết trực giao sụp, và con số BER không còn định nghĩa được bằng mô hình đó
- Số lần lặp của bộ giải mã chưa khai

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Không bù trước được Doppler nên giả thiết trực giao sụp, và con số BER không còn định nghĩa được bằng mô hình đó**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Không GNSS thì không có vị trí thiết bị, nên không tính trước được dịch tần, nên dịch tần còn lại là toàn bộ Doppler. Ở băng S với SCS {{s028}} kHz thì {{s027}} kHz Doppler là {{s035}} lần khoảng sóng mang con, nên năng lượng rơi sang sóng mang con lân cận và mô hình một tap đặt nhiễu giữa sóng mang con bằng {{s010}} không còn mô tả hệ.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ba phương án kia đều là thiếu sót về mô tả, còn phương án này làm con số mất nghĩa.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài báo bê nguyên cấu hình HARQ của mạng mặt đất vào kịch bản LEO với RTT lan truyền {{s018}} ms. Hệ quả trực tiếp nhất là gì?

- Suy hao mưa bị bỏ qua
- Góc nâng tối thiểu bị đặt sai
- Doppler bị tính sai
- Số tiến trình HARQ không đủ để lấp thời gian chờ phản hồi, nên thông lượng báo ra không dựng lại được

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Số tiến trình HARQ không đủ để lấp thời gian chờ phản hồi, nên thông lượng báo ra không dựng lại được**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

RTT {{s018}} ms chỉ là trễ lan truyền của chặng dịch vụ, và với kiến trúc trong suốt còn cộng chặng feeder nữa. Ngân sách định thời của NR mặt đất không chứa nổi khoảng đó, nên cần K_offset và cần khai lại số tiến trình HARQ cùng số lần truyền lại. Bê nguyên cấu hình mặt đất làm con số thông lượng không truy được về một dòng tham số nào, nên người khác không dựng lại được.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết kế vòng bám sau có một câu đặt sai chỗ của một cực trị. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Doppler đỉnh ở cao độ {{s001}} km và {{s005}} GHz là khoảng {{s036}} kHz, đạt khi vệ tinh ở chân trời.
- Doppler giảm theo cos của góc nâng và bằng {{s010}} khi vệ tinh ở đỉnh đầu.
- Vậy thời điểm khắt khe nhất cho vòng bám là lúc vệ tinh mọc, nơi cả Doppler và tốc độ biến thiên Doppler đều lớn nhất.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vậy thời điểm khắt khe nhất cho vòng bám là lúc vệ tinh mọc, nơi cả Doppler và tốc độ biến thiên Doppler đều lớn nhất.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu đều đúng. Mệnh đề thứ ba đặt HAI cực trị vào CÙNG một chỗ, và đây là điểm dễ nhớ sai nhất của cả trụ {{s012}}. Doppler cực đại ở chân trời, nhưng tốc độ biến thiên Doppler cực đại ở ĐỈNH ĐẦU, bằng (f_c/c)·R_E·v²/((R_E+h)·h), tức khoảng {{s011}} kHz mỗi giây ở {{s001}} km và {{s005}} GHz; ở chân trời tốc độ biến thiên gần như bằng {{s010}} vì cos ε phẳng quanh {{s010}}. Hệ quả thật:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

thời điểm khắt khe nhất là lúc vệ tinh ở đỉnh đầu, nơi Doppler bằng {{s010}}. Cách sửa: tách hai yêu cầu, dải bắt của vòng đặt theo Doppler đỉnh ở chân trời, còn băng thông vòng đặt theo tốc độ biến thiên ở đỉnh đầu.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn tính Doppler sau có một dòng thổi con số lên {{s004}}. Bấm vào dòng đó.

- Cao độ chòm sao (constellation) {{s001}} km, nên bán kính quỹ đạo là {{s037}} km.
- Vận tốc quỹ đạo tròn v = sqrt(μ/a) cho {{s003}} km/s.
- Doppler đỉnh ở {{s005}} GHz tính bằng f_d = (v/c)·f_c, cho khoảng {{s038}} kHz.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Doppler đỉnh ở {{s005}} GHz tính bằng f_d = (v/c)·f_c, cho khoảng {{s038}} kHz.**

Doppler chỉ nghe thấy THÀNH PHẦN vận tốc theo đường ngắm, không nghe thấy toàn bộ vận tốc quỹ đạo. Thành phần đó lớn nhất ở chân trời và bằng v·R_E/(R_E+h) = {{s039}} km/s, nhỏ hơn {{s003}} km/s đúng hệ số R_E/(R_E+h) = {{s014}}. Nên Doppler đỉnh là {{s006}} kHz, không phải {{s038}} kHz, và mức thổi lên {{s004}} chính là h/R_E. Hai dòng trên đều đúng. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

thêm hệ số R_E/(R_E+h) và ghi rõ cos ε để người đọc thấy nó là một phép chiếu.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Viết khoảng cách theo góc tâm φ: d² = R_E² + (R_E+h)² − 2·R_E·(R_E+h)·cos φ
- Đạo hàm hai vế theo thời gian: 2d·(dd/dt) = 2·R_E·(R_E+h)·sin φ·(dφ/dt)
- Thay tốc độ góc dφ/dt = ω = v/(R_E+h): dd/dt = R_E·v·sin φ/d
- Định lý hàm sin trong cùng tam giác cho sin φ = d·cos ε/(R_E+h)
- Thay vào, d triệt tiêu và còn v_r = dd/dt = v·(R_E/(R_E+h))·cos ε

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: h {{s001}} km · ε 0° · f_c {{s005}} GHz · SCS {{s008}} kHz → v_r {{s039}} km/s · Doppler {{s041}} kHz · tỉ số {{s042}} lần · tốc độ biến thiên ở đỉnh đầu {{s043}} kHz/s · RTT {{s040}} ms

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Thiết bị có ephemeris và có GNSS, nên bù trước được Doppler** tắt đi: Thiết bị không biết vị trí của mình hoặc không nhận được ephemeris của vệ tinh, nên không tính trước được dịch tần.
- **Lượt qua đúng đỉnh đầu, đối xứng** tắt đi: Góc nâng cực đại của lượt qua nhỏ hơn 90°, nên lượt qua lệch tâm.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Quỹ đạo tròn, vận tốc không đổi trong lượt qua** tắt đi: Quỹ đạo lệch tâm, nên v và h đổi theo vị trí trên quỹ đạo.
- **Ngân sách định thời của NR mặt đất còn dùng được** tắt đi: RTT {{s040}} ms vượt ngân sách định thời giữa truyền và phản hồi của cấu hình mặt đất.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Doppler theo góc nâng, và tốc độ biến thiên Doppler ở đỉnh đầu, trên cùng một bảng. Kéo góc nâng từ chân trời lên đỉnh đầu và nhìn hai con số đi hai chiều ngược nhau.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.3` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V assumes ideal Doppler pre-compensation, yet the deployment scenario in Section II includes low cost sensor terminals without GNSS. Please state how the residual frequency offset is obtained, how it compares with the subcarrier spacing, and whether the BER results of Figure {{s044}} remain valid when the orthogonality assumption no longer holds.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have separated the terminal classes, because the assumption does not hold uniformly across them. For terminals with GNSS and system ephemeris, Section V-A now states the residual offset budget explicitly and Figure {{s044}} is restricted to that class. For the low cost class of Section II without GNSS, the residual offset is the full Doppler shift:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

{{s020}} kHz at {{s005}} GHz and {{s021}} kHz at {{s032}} GHz for h = {{s001}} km, which is {{s022}} and {{s045}} times the {{s008}} kHz and {{s028}} kHz subcarrier spacings respectively. Above one subcarrier spacing the orthogonality assumption fails, and the single tap per subcarrier model used for Figure {{s044}} sets the intercarrier interference term to zero by construction.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The BER values for that class are therefore not worse, they are not defined in that model, and we have removed them rather than annotated them; Section V-D replaces them with a waveform level simulation that carries the intercarrier interference explicitly. We also corrected a related conflation in the loop design of Section V-B:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the acquisition range is now set from the peak Doppler at the horizon, while the loop bandwidth is set from the maximum Doppler rate, which occurs at zenith where the Doppler itself is zero and equals {{s046}} kHz per second at {{s001}} km and {{s005}} GHz. Finally, the peak Doppler now uses the line of sight component v·R_E/(R_E+h) = {{s047}} km/s rather than the orbital speed {{s048}} km/s; the earlier figure was {{s049}} percent high, which is exactly h/R_E.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s009}}: trả lời rằng bù Doppler lý tưởng là giả thiết thông dụng trong các nghiên cứu NTN và dẫn TR {{s017}}. Đúng về thực hành, không trả lời được điều reviewer hỏi.
- Mức {{s032}}: thêm một con số dịch tần còn lại dạng phần trăm của khoảng sóng mang con, nhưng vẫn giữ nguyên các đường BER của mô hình một tap.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s012}}: tính dịch tần còn lại cho từng lớp thiết bị, so với khoảng sóng mang con, và giới hạn các kết quả BER cho đúng lớp thiết bị mà giả thiết trực giao còn đứng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.3` bấm thẻ.
