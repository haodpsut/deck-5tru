---
tieu-de: Kênh: suy hao, mưa, nhiễu loạn
phu-de: Trụ 3 NTN · module 3.2
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
@phan: NTN
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Ở băng Ka, biên dự phòng mưa (rain margin) của tôi là bao nhiêu dB, và nếu bỏ nó thì SE tôi báo bị thổi lên bao nhiêu?

## SE là một hàm của mức khả dụng
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module {{s001}} cho khoảng cách. Module này đổi khoảng cách thành dB, rồi đổi dB thành bit mỗi ký hiệu. Ba tầng, và mỗi tầng có một chỗ để thổi số.

## SE là một hàm của mức khả dụng (tiếp)
@phut: 1
@che-do: noi

Tầng không gian tự do thì sạch: `FSPL = {{s002}} + 20·log₁₀ d(km) + 20·log₁₀ f(GHz)`, không có tham số nào để chọn. Ở {{s003}} GHz, chênh giữa đỉnh đầu và chân trời ở cao độ {{s004}} km là **{{s005}} dB**, và con số đó rút thẳng ra từ tỉ số khoảng xiên (slant range) {{s006}} lần của module {{s001}}.

## SE là một hàm của mức khả dụng (tiếp)
@phut: 1
@che-do: noi

Tầng mưa thì không sạch. Suy hao mưa là một biến ngẫu nhiên, nên **SE là hàm của mức khả dụng (availability)**. Một bài báo in đúng một con số SE mà không nói mức khả dụng thì con số đó không so được với bài nào, kể cả với chính nó ở một tháng khác. Mất {{s007}} dB biên chỉ hạ SNR từ {{s008}} dB về {{s009}} dB, mà SE tụt **{{s010}}**:

## SE là một hàm của mức khả dụng (tiếp)
@phut: 1
@che-do: noi

thổi số theo chiều này rất dễ và rất khó bắt từ bên ngoài.

Tầng nhiễu loạn cho FSO có một cái bẫy riêng: công thức Rytov và Gamma-Gamma chỉ sống trong chế độ nhiễu loạn yếu tới trung bình. Ra khỏi đó thì BER tính từ chúng không phải một con số xấu hơn, mà là một con số không còn định nghĩa được.

## Dạng kỹ thuật của suy hao không gian tự do
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s011}} trên bốn.*

## Dạng kỹ thuật của suy hao không gian tự do · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`FSPL(dB) = {{s002}} + 20·log₁₀ d(km) + 20·log₁₀ f(GHz)`, đúng cùng một thứ với `20·log₁₀(4πd/λ)`, chỉ khác đơn vị.

## Dạng kỹ thuật của suy hao không gian tự do · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cả hai số hạng đều là 20·log₁₀, nên mỗi bậc thập phân của khoảng cách hay của tần số đều đúng {{s003}} dB**. Đi từ {{s012}} GHz lên {{s003}} GHz là đúng {{s003}} dB. Đi từ {{s004}} km ra {{s013}} km là 20·log₁₀(4,92) = {{s005}} dB. Kiểm hằng số bằng cách đặt d = {{s011}} km và f = {{s011}} GHz: hai số hạng log bằng {{s014}} nên FSPL phải ra đúng {{s002}} dB.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s009}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Suy hao mưa theo ITU-R: `A = γ_R·L_eff` với `γ_R = k·R^α`, trong đó `R` là cường độ mưa mm mỗi giờ, `k` và `α` tra theo tần số và phân cực, còn `L_eff` là chiều dài hiệu dụng của đường truyền trong mưa, phụ thuộc **góc nâng**.

Mức khả dụng là phần trăm thời gian trong năm mà liên kết còn chạy. Biên dự phòng là số dB anh để dành để đạt mức đó.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **biên dự phòng và mức khả dụng là một cặp, không bao giờ tách**. Nói {{s007}} dB biên mà không nói mức khả dụng thì không khai được, và nói {{s015}} khả dụng mà không nói toạ độ trạm với mô hình mưa thì cũng không khai được, vì cùng một mức khả dụng đòi số dB rất khác nhau ở vùng ôn đới và vùng nhiệt đới.

## Phương sai Rytov và miền hiệu lực của Gamma-Gamma
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s016}} trên bốn.*

## Phương sai Rytov và miền hiệu lực của Gamma-Gamma · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`σ_R² = 1,23·C_n²·k^(7/6)·L^(11/6)` với `k = 2π/λ`. Phân bố Gamma-Gamma có hai tham số `α` và `β` suy ra từ chỉ số nhấp nháy, mà chỉ số nhấp nháy lại suy ra từ `σ_R²` bằng các biểu thức của chế độ nhiễu loạn yếu tới trung bình.

## Phương sai Rytov và miền hiệu lực của Gamma-Gamma (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **miền hiệu lực là một phần của công thức, không phải một chú thích**. Khi `σ_R²` vượt {{s011}}, cách suy α và β từ σ_R² hết hiệu lực, nên BER tính ra không phải xấu hơn mà là không còn định nghĩa được bằng mô hình đang dùng. Và với đường lên hoặc đường xuống qua khí quyển, `C_n²` biến thiên theo cao độ, nên phải tích phân theo đường chứ không dùng một giá trị duy nhất.

## Suy hao không gian tự do và chuỗi link budget
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`FSPL(dB) = {{s002}} + 20·log₁₀ d(km) + 20·log₁₀ f(GHz) C/N0 = EIRP − FSPL − A_mưa + G/T + {{s017}} SNR = C/N0 − 10·log₁₀ B SE = log₂(1 + 10^(SNR/10))`

**Giả thiết nó đứng trên:**

## Suy hao không gian tự do và chuỗi link budget (tiếp)
@phut: 1
@che-do: so

- Không gian tự do: không vật chắn, không phản xạ nhiều đường, anten khớp phân cực
- Hằng số {{s002}} dB chỉ đúng với d theo km và f theo GHz; đổi đơn vị là đổi hằng số
- Hằng số {{s017}} là hằng số Boltzmann theo dB, và G/T phải khai ở cùng điểm quy chiếu với FSPL để không đếm hai lần suy hao feeder
- Băng thông nhiễu bằng băng thông tín hiệu B, nhiễu trắng Gauss cộng tính

## Suy hao không gian tự do và chuỗi link budget (tiếp)
@phut: 1
@che-do: so

- SE theo Shannon là CHẶN TRÊN với mã hoá lý tưởng độ dài vô hạn; SE thực tế lấy theo bảng điều chế mã hoá nên luôn nhỏ hơn

## Suy hao không gian tự do và chuỗi link budget · ghi chú
@phut: 1
@che-do: noi

Kiểm nhanh hằng số: đặt d = {{s011}} km và f = {{s011}} GHz thì hai số hạng log bằng {{s014}} nên FSPL phải ra đúng {{s002}} dB. Kiểm nhanh thứ hai: hạ tần từ {{s003}} GHz xuống {{s012}} GHz phải làm FSPL giảm đúng {{s018}} dB, vì 20·log₁₀(10) = {{s003}}.

## Suy hao mưa và nhiễu loạn khí quyển
@phut: 1.5
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`A_mưa = γ_R·L_eff γ_R = k·R^α σ_R² = 1,23·C_n²·(2π/λ)^(7/6)·L^(11/6)`

**Giả thiết nó đứng trên:**

## Suy hao mưa và nhiễu loạn khí quyển (tiếp)
@phut: 1
@che-do: so

- k và α tra theo tần số và phân cực theo ITU-R P.838; chúng không phải tham số tự do
- L_eff phụ thuộc góc nâng, nên cùng một cường độ mưa cho suy hao khác nhau ở hai góc nâng khác nhau
- Công thức Rytov giả định nhiễu loạn yếu tới trung bình, tức σ_R² nhỏ hơn {{s011}}
- Công thức Rytov dạng này giả định đường truyền ngang đồng nhất, tức C_n² không đổi dọc đường

## Suy hao mưa và nhiễu loạn khí quyển (tiếp)
@phut: 1
@che-do: so

- Với đường lên hoặc đường xuống qua khí quyển, C_n² biến thiên theo cao độ nên phải tích phân theo đường

## Suy hao mưa và nhiễu loạn khí quyển · ghi chú
@phut: 1
@che-do: noi

Suy hao mưa Ka ở vùng nhiệt đới cho một mức khả dụng cụ thể phải tra ITU-R P.618 với toạ độ trạm thật. Đặc tả của trụ này để dòng đó ở trạng thái chưa chắc, nên module này KHÔNG đưa con số đó lên thẻ: thà thiếu một thẻ còn hơn dạy sai một số.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s019}} | dB | FSPL ở khoảng xiên {{s013}} km và tần số {{s003}} GHz
!so {{s020}} | dB | FSPL ở khoảng xiên {{s004}} km
!so {{s021}} | dB | Chênh FSPL giữa đỉnh đầu và chân trời ở cao độ {{s004}}

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s022}} | dB/km | ITU-T G.652 đặt TRẦN cho suy hao của cáp
!so {{s023}} | dBW/K/Hz | Hằng số Boltzmann viết theo dB

## Khoảng xiên 1816 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Khoảng xiên {{s026}} km, tức góc nâng 10° ở cao độ {{s004}} km, tần số {{s025}} GHz. FSPL là bao nhiêu dB?

d = {{s024}}, f = {{s025}}

## Khoảng xiên 1816 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`92.45+20⋆Math.log10(d)+20⋆Math.log10(f)`

Khoảng {{s027}} dB. Để ý nó gần bằng {{s028}} dB của {{s003}} GHz ở chân trời ({{s013}} km): đi từ {{s003}} lên {{s025}} GHz đắt gần đúng bằng đi từ góc nâng 10° ra chân trời. Đó là cách ước lượng nhanh nên có trong tay khi reviewer hỏi vì sao chọn băng này mà không băng kia.

## Nhiễu loạn với C_n² = 10⁻¹⁴ m^(−2/3)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nhiễu loạn với C_n² = 10⁻¹⁴ m^(−2/3), bước sóng {{s032}} nm, đường truyền {{s031}} m. Phương sai Rytov (Rytov variance) σ_R² là bao nhiêu?

cn2 = {{s029}}, lam = {{s030}}, L = {{s031}}

## Nhiễu loạn với C_n² = 10⁻¹⁴ m^(−2/3) · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`1.23⋆cn2⋆Math.pow(2⋆Math.PI/lam,7/6)⋆Math.pow(L,11/6)`

Khoảng {{s033}}, tức nhỏ hơn {{s011}} khá nhiều, nên còn trong chế độ nhiễu loạn yếu và cách suy α với β của Gamma-Gamma từ chỉ số nhấp nháy còn hiệu lực. Nhưng tăng C_n² lên 10⁻¹³ thì σ_R² thành khoảng {{s034}}, tức vượt {{s011}}, và lúc đó mô hình hết hiệu lực chứ không phải cho số xấu hơn. Vì σ_R² đi theo L^(11/6), nhân đôi độ dài đường truyền làm nó tăng khoảng {{s035}} lần.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Liên kết có SNR {{s008}} dB khi trời quang. Mưa lấy đi {{s007}} dB. SE Shannon giảm bao nhiêu phần trăm?

snr = {{s008}}, amua = {{s007}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆(1-Math.log2(1+Math.pow(10,(snr-amua)/10))/Math.log2(1+Math.pow(10,snr/10)))`

Khoảng {{s010}}, tức gần hai phần ba. SNR chỉ đi từ {{s008}} dB về {{s009}} dB, mà SE tụt từ {{s036}} xuống {{s037}} bit mỗi ký hiệu. Nói ngược lại: con số SE của trời quang bị thổi lên {{s038}} lần so với con số ở điều kiện mưa đó. Đây là lý do SE in một mình, không kèm mức khả dụng, là con số không khai được.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Đặt d = {{s011}} km và f = {{s011}} GHz vào dạng kỹ thuật của FSPL. Kết quả là bao nhiêu?

- {{s002}} dB
- không tính được vì d quá nhỏ
- {{s014}} dB
- {{s003}} dB

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**{{s002}} dB**

Hai số hạng log bằng {{s014}} nên FSPL bằng đúng hằng số {{s002}} dB. Đây là phép kiểm rẻ nhất cho công thức, và nó bắt được lỗi gõ hằng số hoặc lẫn đơn vị (dùng m thay vì km đổi hằng số thành {{s039}} dB).

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo so FSO với RF băng Ka và báo FSO cho dung lượng cao hơn {{s016}} lần. Thiếu đúng một dữ kiện để kiểm câu đó. Dữ kiện nào?

- Tốc độ mã hoá sửa lỗi
- Khẩu độ anten của nhánh RF
- Điều kiện thời tiết dùng cho CẢ HAI nhánh, cùng một chuỗi
- Số bit mỗi ký hiệu của điều chế FSO

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Điều kiện thời tiết dùng cho CẢ HAI nhánh, cùng một chuỗi**

Mưa đánh vào RF băng Ka, còn sương mù và nhiễu loạn đánh vào FSO. Nếu mỗi nhánh được đo ở điều kiện có lợi cho nó thì tỉ số {{s016}} lần đổi dấu được, nên nó không còn là một so sánh. Ba dữ kiện kia đều cần cho việc dựng lại, nhưng chỉ dữ kiện thời tiết mới quyết định tỉ số có nghĩa hay không.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai trạm, cùng cường độ mưa mm mỗi giờ, cùng tần số, cùng phân cực. Trạm A nhìn vệ tinh ở góc nâng 60°, trạm B ở 20°. Suy hao mưa của hai trạm thế nào?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Trạm A lớn hơn, vì đường truyền dốc hơn nên qua nhiều mây hơn
- Không so được nếu không biết cao độ vệ tinh
- Bằng nhau, vì γ_R chỉ phụ thuộc cường độ mưa
- Trạm B lớn hơn, vì L_eff dài hơn ở góc nâng thấp

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Trạm B lớn hơn, vì L_eff dài hơn ở góc nâng thấp**

γ_R = k·R^α giống nhau vì cùng cường độ mưa, cùng tần số, cùng phân cực. Khác nhau ở L_eff: góc nâng thấp thì đường truyền nằm trong lớp mưa dài hơn, nên A_mưa = γ_R·L_eff lớn hơn. Đây là lý do mô hình mưa phải khai kèm góc nâng, và là lý do biên dự phòng của một chòm sao (constellation) LEO không phải một số duy nhất.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một câu làm cả bảng SE không so được với bài nào. Bấm vào câu đó.

- Đường xuống ở {{s003}} GHz, băng thông {{s040}} MHz, EIRP {{s041}} dBW, G/T của thiết bị {{s012}} dB/K.
- Khoảng xiên lấy ở góc nâng 40°, tức {{s042}} km.
- Hiệu suất phổ đạt {{s043}} bit mỗi ký hiệu.
- Thông lượng chặn trên tương ứng là {{s044}} Mbit/s.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Hiệu suất phổ đạt {{s043}} bit mỗi ký hiệu.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Con số SE in một mình. SE ở băng Ka là hàm của mức khả dụng, vì suy hao mưa là biến ngẫu nhiên: {{s043}} bit mỗi ký hiệu là giá trị TRỜI QUANG, và ở {{s015}} khả dụng nó nhỏ hơn hẳn. Với chính liên kết này, {{s045}} dB mưa đã cắt một nửa SE và {{s007}} dB cắt {{s046}}. Ba dòng trên đều hợp lệ và đủ để dựng lại FSPL với SNR. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

viết SE kèm mức khả dụng, mô hình mưa (P.618 với P.838) và toạ độ trạm, hoặc in cả hai con số trời quang và ở mức khả dụng mục tiêu cạnh nhau.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô hình kênh FSO sau có một dòng làm mọi con số BER của bài mất nghĩa. Bấm vào dòng đó.

- Nhánh quang dùng bước sóng {{s032}} nm, đường lên từ trạm mặt đất tới vệ tinh LEO.
- Nhiễu loạn mô hình bằng Gamma-Gamma, hai tham số suy từ chỉ số nhấp nháy.
- Đặt C_n² = 10⁻¹³ m^(−2/3) cho toàn bộ đường truyền và quét góc nâng từ 10° tới 90°.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Đặt C_n² = 10⁻¹³ m^(−2/3) cho toàn bộ đường truyền và quét góc nâng từ 10° tới 90°.**

Hai lỗi chồng lên nhau trong một dòng, và cả hai đều giết con số BER. Thứ nhất: một C_n² duy nhất cho đường xiên qua khí quyển là sai, vì C_n² biến thiên theo cao độ nên phải tích phân theo đường, và kết quả phụ thuộc chính cái góc nâng đang quét. Thứ hai:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

ở C_n² = 10⁻¹³ với đường truyền hiệu dụng cỡ km thì σ_R² vượt {{s011}}, nên cách suy α và β từ chỉ số nhấp nháy theo biểu thức nhiễu loạn yếu hết hiệu lực; BER tính ra không phải xấu hơn mà là không còn định nghĩa được. Cách sửa: dùng phân bố C_n²(z) khai rõ, tích phân theo đường, và IN σ_R² ở từng điểm quét để người đọc thấy điểm nào còn trong miền hiệu lực.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Mật độ công suất ở khoảng cách d từ nguồn đẳng hướng: S = P_t/(4πd²)
- Diện tích hiệu dụng của anten thu đẳng hướng: A_e = λ²/(4π)
- Tỉ số công suất: P_r/P_t = S·A_e/P_t = (λ/(4πd))², nên FSPL = 20·log₁₀(4πd/λ)
- Thay λ = c/f rồi tách thành ba số hạng: FSPL = 20·log₁₀(4π/c) + 20·log₁₀ d + 20·log₁₀ f
- Đổi d sang km và f sang GHz, ba hằng số gộp lại thành {{s002}} dB

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Công suất thu theo dBW: P_r = EIRP − FSPL − A_mưa − L_khác
- Mật độ nhiễu nhiệt theo dB: N0 = −228,6 + 10·log₁₀ T_hệ
- Trừ hai vế và gom độ lợi thu với nhiệt độ hệ thành G/T: C/N0 = EIRP − FSPL − A_mưa + G/T + {{s017}}
- Chia cho băng thông: SNR = C/N0 − 10·log₁₀ B
- Chặn trên Shannon: SE = log₂(1 + 10^(SNR/10))

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: EIRP {{s041}} dBW · G/T {{s012}} dB/K · B {{s040}} MHz · d {{s042}} km · f {{s003}} GHz · mưa {{s014}} dB → FSPL {{s047}} dB · C/N0 {{s048}} dBHz · SNR {{s049}} dB · SE {{s050}} bit mỗi ký hiệu · thông lượng {{s044}} Mbit/s

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Trời quang, không có mưa** tắt đi: Có mưa, nên suy hao là biến ngẫu nhiên theo thống kê khí hậu của toạ độ trạm và theo góc nâng.
- **Đường truyền nhiễu loạn đồng nhất, một C_n² duy nhất** tắt đi: C_n² biến thiên theo cao độ, nên đường xiên qua khí quyển đi qua nhiều chế độ nhiễu loạn khác nhau.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Nhiễu loạn yếu tới trung bình, σ_R² nhỏ hơn {{s011}}** tắt đi: Nhiễu loạn mạnh, σ_R² vượt {{s011}}, chỉ số nhấp nháy bão hoà.
- **So FSO với RF ở cùng điều kiện thời tiết** tắt đi: Hai nhánh đo ở hai điều kiện khác nhau, ví dụ FSO lấy trời quang còn RF lấy có mưa.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bảng link budget sống. Kéo EIRP, G/T, băng thông, khoảng xiên, tần số và suy hao mưa, rồi đọc FSPL, C/N0, SNR, SE và mức SE bị thổi lên nếu bỏ mưa. Cột cuối là con số mà phản biện sẽ hỏi.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.2` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table V reports a single spectral efficiency of {{s051}} bit/symbol for the Ka-band downlink. Since rain attenuation is a random process, this figure is only meaningful together with a stated availability. Please report the spectral efficiency at the target availability, name the propagation model and the station coordinates, and state the rain margin you assumed.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree that a single spectral efficiency figure is not reportable for a Ka-band link. Table V has been restructured. It now gives three values for the same link: {{s051}} bit/symbol under clear sky, and the values at {{s052}} and {{s053}} percent availability, each with the rain margin that produces it.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The margins are derived from ITU-R P.618 with the specific attenuation coefficients of P.838, evaluated at the coordinates of the gateway given in Section III-A, and at the worst served elevation of {{s007}} degrees rather than at the {{s041}} degree reference used previously, since L_eff grows as the elevation drops. We also state the sensitivity directly, because it is not small:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

at an operating SNR of {{s008}} dB, a {{s007}} dB rain event reduces the Shannon spectral efficiency by {{s054}} percent, from {{s055}} to {{s056}} bit/symbol, so the clear sky figure overstates the realistic one by a factor of {{s057}}. Every throughput number in Section VI now carries a pointer to which of the three spectral efficiency rows it was computed from.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, all figures in that table are Shannon upper bounds; the MODCOD table of the assumed waveform yields lower values, and we now say so where the bound is used.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s011}}: trả lời rằng {{s043}} bit mỗi ký hiệu lấy từ SNR trong bảng link budget. Đúng về nguồn gốc, không trả lời được điều reviewer hỏi.
- Mức {{s012}}: thêm một biên dự phòng mưa dạng một con số dB, nhưng vẫn không khai mức khả dụng và không nói mô hình mưa.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s009}}: báo SE ở hai mức khả dụng cụ thể cộng SE trời quang, khai mô hình P.618 với P.838, khai toạ độ trạm và góc nâng dùng để tính L_eff.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

In Section IV-C the optical branch uses a single refractive index structure parameter for a slant path, and the Gamma-Gamma parameters are obtained from the scintillation index using weak fluctuation expressions. Please justify the validity range at every point of the C_n squared sweep in Figure {{s058}}, and report the Rytov variance alongside each BER curve.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have made the validity range part of the reported data rather than a footnote. Figure {{s058}} now carries a second axis showing the Rytov variance at each sweep point, and the two highest C_n squared points, where the variance exceeds unity, have been removed from the figure rather than annotated, because the weak fluctuation route from scintillation index to the Gamma-Gamma shape parameters is not defined there and the resulting BER is not a measurement.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

For the slant path we have replaced the single structure parameter with a path integral over a Hufnagel-Valley profile, stated in Section IV-C with its ground level value and wind speed, evaluated per elevation; this changes the curves qualitatively and not only in magnitude, because the effective turbulence now depends on the same elevation that the sweep varies, and we have redrawn Figure {{s059}} accordingly.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also note, for the record, that our own consistency checks could have caught this and did not, since none of them compared the sweep range against the validity condition of the model; that check is now part of the artifact.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s011}}: trả lời rằng Gamma-Gamma là mô hình tiêu chuẩn cho nhiễu loạn khí quyển (atmospheric turbulence) và được dùng rộng rãi. Đúng về thực hành, không trả lời được điều reviewer hỏi.
- Mức {{s012}}: thêm giá trị σ_R² ở một điểm đại diện, thường là điểm thuận lợi nhất, và vẫn giữ một C_n² duy nhất cho đường xiên.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s009}}: in σ_R² cạnh TỪNG điểm quét, đánh dấu rõ các điểm đã ra khỏi miền nhiễu loạn yếu tới trung bình, và thay một C_n² duy nhất bằng tích phân theo đường với một phân bố C_n²(z) khai rõ.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.2` bấm thẻ.
