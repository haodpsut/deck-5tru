---
tieu-de: Dung lượng và tài nguyên
phu-de: Trụ 3 NTN · module 3.7
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
@phan: NTN
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Con số thông lượng tôi báo là trung bình trên cái gì, và ở biên vệt phủ nó còn lại bao nhiêu?

## Một con số trung bình luôn kèm một câu hỏi
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Vệt phủ của một chùm không đồng nhất. Ở {{s001}} km với góc nâng tối thiểu 10°, suy hao không gian tự do (free-space path loss) ở biên lớn hơn ở đỉnh đầu {{s002}} dB, và {{s002}} dB SNR không phải là một chi tiết: nó đưa SE từ {{s003}} xuống khoảng {{s004}} bit mỗi ký hiệu, tức còn khoảng một phần bảy.

## Một con số trung bình luôn kèm một câu hỏi (tiếp)
@phut: 1
@che-do: noi

Nên mọi con số SE hoặc thông lượng trong bài NTN đều là một phép lấy trung bình, và bài phải khai lấy trung bình **theo diện tích** hay **theo người dùng**. Hai cái này khác nhau rất xa khi người dùng không phân bố đều: ở trạng thái mặc định của mô phỏng dưới đây, trung bình theo diện tích cao hơn trung bình theo người dùng khoảng {{s005}}.

## Một con số trung bình luôn kèm một câu hỏi (tiếp)
@phut: 1
@che-do: noi

Và hai phân bố người dùng khác nhau có thể cho CÙNG một trung bình theo diện tích mà khác hẳn theo người dùng, vì trung bình theo diện tích không nhìn thấy người dùng ở đâu.

## Một con số trung bình luôn kèm một câu hỏi (tiếp)
@phut: 1
@che-do: noi

Hai thứ nữa luôn phải nhân vào trước khi nói thông lượng hệ thống: hệ số tái dùng tần số (frequency reuse factor) `N` chia băng cho các nhóm chùm, và tỉ lệ chiếu (illumination ratio) của beam hopping với ràng buộc tổng các tỉ lệ chiếu không vượt {{s006}}.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Trung bình theo diện tích lấy trọng số là diện tích của từng vùng trong vệt. Trung bình theo người dùng lấy trọng số là số người dùng trong từng vùng. Hai cái trùng nhau khi và chỉ khi người dùng phân bố đều theo diện tích.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **trung bình theo diện tích không nhìn thấy người dùng ở đâu**, nên nó luôn là con số dễ hơn khi vùng tốt nằm ở giữa và người dùng dồn ra biên. Dựng được hai phân bố người dùng cho cùng một trung bình theo diện tích mà khác nhau nhiều lần theo người dùng là bài tập nửa phút, và reviewer làm được bài tập đó nhanh hơn anh nghĩ.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Nên bảng kết quả phải khai trọng số, và nếu dùng trung bình theo diện tích thì phải nói rõ nó là chặn trên của trải nghiệm người dùng khi người dùng dồn ra biên.

## Hệ số tái dùng tần số N
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Hệ số tái dùng tần số N · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Băng khả dụng `B` được chia cho `N` nhóm chùm để các chùm kề nhau không dùng cùng tần số, nên mỗi chùm chỉ có `B/N`. Thông lượng hệ thống xấp xỉ `(B/N)` nhân tổng SE của các chùm.

## Hệ số tái dùng tần số N · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: `N` là một phép đánh đổi chứ không phải một hằng số công nghệ. Tăng `N` thì nhiễu đồng kênh giảm nên SE mỗi chùm tăng, nhưng băng mỗi chùm giảm theo đúng tỉ lệ `1/N`. Bài nào so thông lượng hệ thống mà không khai `N` giống nhau cho cả hai bên thì đang so hai hệ khác nhau, và chiều của phép so không đoán được từ trước.

## Beam hopping và tỉ lệ chiếu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Beam hopping và tỉ lệ chiếu · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Vệ tinh chỉ chiếu một tập con các chùm trong mỗi khe thời gian, nên chùm thứ `i` được chiếu với tỉ lệ `d_i` và ràng buộc là `Σ d_i ≤ {{s006}}` nhân số chùm chiếu đồng thời. Thông lượng mỗi chùm nhân thêm `d_i`.

## Beam hopping và tỉ lệ chiếu · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: beam hopping **không tạo thêm dung lượng**, nó phân phối lại dung lượng theo thời gian để khớp nhu cầu không đều. Nên lợi ích của nó phải đo bằng chỉ số nhu cầu được thoả, không đo bằng tổng thông lượng. Một bài báo khoe beam hopping làm tăng tổng thông lượng là bài đang đo sai đại lượng, trừ khi phần tăng đến từ việc tránh chùm không có người dùng.

## Đường truyền tới SE
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`C/N₀ = EIRP − FSPL − A_mưa + G/T − k, k = −228,6 dBW/K/Hz; SNR = C/N₀ − 10·log₁₀ B; SE ≤ log₂(1 + SNR)`

**Giả thiết nó đứng trên:**

## Đường truyền tới SE (tiếp)
@phut: 1
@che-do: so

- Nhiễu nhiệt trắng Gauss là nguồn nhiễu chi phối, nên dùng được công thức Shannon
- k là hằng số Boltzmann viết theo dB, không phụ thuộc hệ, nên nó không phải tham số cần hiệu chuẩn (calibration)
- A_mưa phụ thuộc mức khả dụng (availability) khai báo và góc nâng, nên nó KHÔNG phải một số cố định của hệ
- Shannon là chặn trên: SE thực tế lấy theo bảng điều chế mã hoá nên luôn nhỏ hơn, và rời rạc

## Đường truyền tới SE · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hai chỗ bị bỏ nhiều nhất khi chuyển từ SE mỗi liên kết sang thông lượng hệ thống: hệ số tái dùng tần số `N` và tỉ lệ chiếu `d_i` của beam hopping. Thông lượng hệ thống xấp xỉ `(B/N)·Σ(d_i·SE_i)`, không phải `B·SE_trung_bình`.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s009}} | dBW/K/Hz | Hằng số Boltzmann viết theo dB trong phương trình đường truyền có
!so {{s010}} | dB | Ở h = {{s001}} km
!so {{s011}} | bit mỗi ký hiệu | Chặn Shannon ở SNR {{s012}} dB là bao nhiêu bit mỗi ký

## SNR ở tâm vệt là 10 dB
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

SNR ở tâm vệt là {{s012}} dB, biên thấp hơn tâm {{s002}} dB. Tỉ số giữa SE ở biên và SE ở tâm là bao nhiêu?

snrTam = {{s012}}, chenh = {{s010}}

## SNR ở tâm vệt là 10 dB · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.log2(1 + Math.pow(10, (snrTam - chenh)/10))/Math.log2(1 + Math.pow(10, snrTam/10))`

## SNR ở tâm vệt là 10 dB · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s013}}, tức SE ở biên còn khoảng một phần bảy SE ở tâm. Chiều của con số là chỗ phải nhớ: {{s002}} dB không lấy đi {{s002}} phần trăm mà lấy đi gần {{s014}} phần trăm, vì SE là hàm log của SNR tuyến tính chứ không của SNR theo dB. Và tỉ số này không phải hằng số: ở SNR tâm {{s015}} dB thì cùng chênh {{s002}} dB chỉ hạ SE về khoảng {{s016}} của tâm.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Vẫn SNR tâm {{s012}} dB và chênh {{s002}} dB. Vành ngoài chiếm một nửa diện tích nhưng chứa {{s019}} người dùng. Trung bình theo diện tích cao hơn trung bình theo người dùng bao nhiêu lần?

snrTam = {{s012}}, chenh = {{s010}}, aN = {{s017}}, pN = {{s018}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`((1-aN)⋆Math.log2(1 + Math.pow(10, snrTam/10)) + aN⋆Math.log2(1 + Math.pow(10, (snrTam - chenh)/10)))/((1-pN)⋆Math.log2(1 + Math.pow(10, snrTam/10)) + pN⋆Math.log2(1 + Math.pow(10, (snrTam - chenh)/10)))`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s020}} lần, tức trung bình theo diện tích cao hơn trung bình theo người dùng {{s005}}. Cùng một hệ, cùng một lúc, hai con số hợp lệ, chênh nhau gần hai lần. Nếu abstract của anh in con số theo diện tích và phần kết luận nói về trải nghiệm người dùng thì anh vừa chuyển đại lượng giữa hai câu mà không khai, và reviewer dựng lại được phép chuyển đó bằng một phép chia.

## Hệ có băng khả dụng B
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hệ có băng khả dụng B, hệ số tái dùng tần số N, và beam hopping với tỉ lệ chiếu d_i cho chùm thứ i. Thông lượng hệ thống xấp xỉ bằng?

- B nhân SE trung bình của các chùm
- (B/N) nhân tổng của d_i nhân SE_i
- (B·N) nhân tổng của d_i nhân SE_i
- B nhân tổng SE_i, vì beam hopping không giảm tổng thời gian chiếu

## Hệ có băng khả dụng B · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**(B/N) nhân tổng của d_i nhân SE_i**

## Hệ có băng khả dụng B · đáp (tiếp)
@phut: 1
@che-do: noi

Tái dùng tần số chia băng nên mỗi chùm chỉ có B/N, và beam hopping chia thời gian nên chùm thứ i chỉ được chiếu tỉ lệ d_i. Hai thứ nhân vào theo hai trục khác nhau, một trục tần số và một trục thời gian. Phương án đầu bỏ cả hai và cho con số cao hơn nhiều lần; phương án cuối hiểu sai beam hopping thành không mất gì, trong khi tổng các tỉ lệ chiếu bị ràng buộc.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai bài báo cùng khai SE trung bình {{s021}} bit mỗi ký hiệu trên cùng một cấu hình vệt phủ, nhưng trải nghiệm người dùng mô phỏng của chúng chênh nhau bốn lần. Nguyên nhân khả dĩ nhất?

- Hai bài dùng hệ số tái dùng tần số khác nhau
- Một bài quên trừ hằng số Boltzmann
- Một bài tính sai công thức Shannon
- Hai bài lấy trung bình theo cùng diện tích nhưng phân bố người dùng khác nhau

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Hai bài lấy trung bình theo cùng diện tích nhưng phân bố người dùng khác nhau**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Trung bình theo diện tích mù với phân bố người dùng theo đúng định nghĩa, nên hai phân bố rất khác nhau cho cùng một con số theo diện tích. Thử trên mô phỏng: giữ nguyên mọi thứ, đổi tỉ lệ người dùng ở vành ngoài từ {{s022}} sang {{s023}} thì trung bình theo người dùng đi từ {{s024}} xuống {{s025}}, tức chênh khoảng {{s026}} lần, trong khi trung bình theo diện tích không nhích một chữ số.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Hệ số tái dùng tần số thì đổi thông lượng chứ không đổi SE mỗi ký hiệu.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo ở băng Ka khai SE {{s003}} bit mỗi ký hiệu và nói hệ đạt dung lượng mục tiêu. Thiếu đúng một dữ kiện để kiểm câu đó. Dữ kiện nào?

- Mức khả dụng và mô hình mưa dùng để trừ suy hao
- Kiến trúc payload trong suốt (transparent) hay tái sinh
- Độ nghiêng quỹ đạo
- Số chùm trên vệ tinh

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Mức khả dụng và mô hình mưa dùng để trừ suy hao**

Ở băng Ka, suy hao mưa là hàm của mức khả dụng khai báo: cùng một hệ cho SE khác nhau ở {{s027}}, {{s028}} và {{s029}}. Nên một con số SE không kèm mức khả dụng không xác định được điều kiện nào, và không so được với bài khác. Số chùm và độ nghiêng đều cần cho tái lập, nhưng chúng không đổi SE của một liên kết đã cho.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bảng kết quả dung lượng dưới đây có một dòng không khai được. Bấm vào dòng đó.

- Cao độ {{s001}} km, góc nâng tối thiểu 10°, băng Ka {{s030}} GHz.
- Băng khả dụng {{s031}} MHz, hệ số tái dùng tần số {{s032}}, tỉ lệ chiếu {{s033}}.
- SE ở tâm vệt {{s034}} và SE ở biên vệt {{s035}} bit mỗi ký hiệu, ở điều kiện trời quang.
- SE trung bình trên vệt phủ: {{s036}} bit mỗi ký hiệu.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**SE trung bình trên vệt phủ: {{s036}} bit mỗi ký hiệu.**

Ba dòng trên đều khai được: cấu hình đủ, tài nguyên đủ, và hai con số SE theo VỊ TRÍ có kèm điều kiện trời quang. Dòng cuối mới là chỗ không khai được, vì nó là một phép lấy trung bình mà không nói trọng số: {{s036}} là trung bình theo diện tích, còn trung bình theo người dùng ở cùng cấu hình này là {{s037}}, tức thấp hơn {{s038}}.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai con số đều hợp lệ nhưng trả lời hai câu khác nhau, và người đọc không có cách nào biết dòng này là cái nào. Cách sửa: đổi nhãn thành 'trung bình theo diện tích' và thêm một dòng 'trung bình theo người dùng' kèm phân bố người dùng đã dùng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn tính thông lượng dưới đây có một chỗ làm con số cao lên nhiều lần. Bấm vào chỗ đó.

- Mỗi chùm được cấp một phần băng theo hệ số tái dùng tần số {{s032}}, tức {{s039}} MHz.
- Lịch beam hopping cho mỗi chùm tỉ lệ chiếu {{s033}}.
- SE trung bình của chùm là {{s036}} bit mỗi ký hiệu.
- Thông lượng hệ thống do đó là {{s031}} MHz nhân {{s036}}, tức khoảng {{s040}} Mbit/s mỗi chùm.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Thông lượng hệ thống do đó là {{s031}} MHz nhân {{s036}}, tức khoảng {{s040}} Mbit/s mỗi chùm.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Ba dòng đầu khai đúng và đủ: {{s039}} MHz mỗi chùm sau khi chia {{s032}}, tỉ lệ chiếu {{s033}}, SE {{s036}}. Dòng cuối thì bỏ sạch cả hai thứ vừa khai ở trên và nhân lại bằng toàn bộ {{s031}} MHz với tỉ lệ chiếu bằng {{s006}}. Con số đúng là {{s039}} nhân {{s033}} nhân {{s036}}, tức khoảng {{s041}} Mbit/s mỗi chùm, nên dòng này cao hơn đúng {{s042}} lần. Đây là kiểu lỗi khó thấy vì các dòng trên vẫn đúng:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

chỗ sai nằm ở việc con số cuối không truy được về các dòng trên nó. Cách sửa: viết công thức thông lượng bằng chính các biến đã khai, và kiểm bằng cách thay số của chính bảng.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Từ cao độ và góc nâng tối thiểu, tính khoảng xiên (slant range) lớn nhất d(ε_min)
- Tính FSPL = {{s043}} + 20·log₁₀ d(km) + 20·log₁₀ f(GHz) ở khoảng xiên đó
- Tra A_mưa từ mô hình mưa ứng với MỨC KHẢ DỤNG đã khai và góc nâng ở biên
- C/N₀ = EIRP − FSPL − A_mưa + G/T − k với k = −228,6 dBW/K/Hz
- SNR = C/N₀ − 10·log₁₀ B với B là băng thông thật của sóng mang

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- SE ≤ log₂(1 + SNR), rồi hạ xuống bậc điều chế mã hoá gần nhất của bảng

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: SE tâm {{s034}} · SE biên {{s035}} · biên còn {{s044}} tâm · trung bình theo diện tích {{s036}} · trung bình theo người dùng {{s037}} bit mỗi ký hiệu · thông lượng mỗi chùm {{s045}} Mbit/s

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Người dùng phân bố đều trong vệt** tắt đi: Người dùng dồn về một phần của vệt, ở đây là {{s019}} người dùng trong nửa diện tích ngoài.
- **Trời quang, không trừ suy hao mưa** tắt đi: Băng Ka ở vùng mưa nhiều, suy hao mưa phụ thuộc mức khả dụng khai báo và góc nâng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi chùm được chiếu liên tục** tắt đi: Beam hopping: mỗi khe chỉ chiếu một tập con các chùm, chùm thứ i được chiếu với tỉ lệ d_i.
- **SE thực tế đạt đúng chặn Shannon** tắt đi: SE lấy theo bảng điều chế mã hoá, rời rạc và có khoảng cách tới Shannon.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hằng số Boltzmann dùng trong phương trình đường truyền là một giá trị ĐỊNH NGHĨA, không mang sai số đo.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỨNG**

ĐỨNG, từ lần định nghĩa lại hệ SI năm {{s046}}. Trang tra hằng số của NIST in giá trị 1,380649·10⁻²³ J/K và in độ bất định chuẩn là "(exact)". Nghĩa là đơn vị kelvin nay được định nghĩa THEO hằng số này, nên nó không còn là đại lượng đo được tinh chỉnh dần. Hệ quả thực dụng cho ngân sách đường truyền:

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

10·log₁₀ k = −228,599 dBW/K/Hz là một hằng số cố định, nên mọi sai lệch trong chuỗi C/N0 nằm ở G/T, ở suy hao và ở băng thông, không nằm ở đây.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Một vệt phủ chia hai vành: vành trong có SNR ở tâm, vành ngoài thấp hơn đúng một chênh lệch khai được. Hai thanh kéo riêng cho tỉ lệ DIỆN TÍCH của vành ngoài và tỉ lệ NGƯỜI DÙNG ở vành ngoài, để thấy hai con số trung bình tách nhau khi hai tỉ lệ đó khác nhau.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.7` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table III reports an average spectral efficiency of {{s047}} bit per symbol over the beam footprint. The averaging weight is not stated. Since free space loss alone varies by {{s010}} dB between boresight and the {{s012}} degree elevation edge at {{s001}} km, and since the user distribution in Section II is explicitly non-uniform, an area-weighted average and a user-weighted average differ substantially. Please state the weight, report both, and clarify whether the clear sky assumption applies to the Ka band figures.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have made the weighting explicit and we now report both. Table III lists area-weighted average spectral efficiency {{s048}} bit per symbol and user-weighted average {{s049}} bit per symbol for the user distribution of Section II, where the outer half of the footprint by area carries {{s050}} percent of the users: the area-weighted figure is {{s051}} percent higher.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Figure {{s052}} replaces the single number with the cumulative distribution of spectral efficiency over users, together with the fraction of users below the lowest available MCS, which is {{s052}} percent. We also state why the two numbers must both appear: an area-weighted average is by construction blind to where users are, and we give two distributions in Appendix B that share the same area-weighted value of {{s048}} while their user-weighted values are {{s053}} and {{s054}}, a factor of about {{s055}}.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

All Ka band figures are now tagged with the availability level and rain model: the {{s048}} and {{s049}} values are for {{s056}} percent availability under ITU-R P.618 with the local rain rate of Section II, and the clear sky values, previously reported without a tag, are given separately in Table III-b. Comparisons with prior work in Table IV are now grouped by averaging weight and by availability level, and we removed two comparisons that could not be matched on both.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s006}}: trả lời rằng SE trung bình được tính trên toàn vệt phủ nên nó đại diện cho hệ. Không phân biệt trọng số diện tích với trọng số người dùng.
- Mức {{s008}}: khai rằng đó là trung bình theo diện tích, nhưng không thêm con số theo người dùng và vẫn để con số cũ ở abstract.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s007}}: in cả hai con số với trọng số rõ, cộng khai mức khả dụng và mô hình mưa cho mọi con số băng Ka, cộng sửa phần kết luận để dùng đúng đại lượng mà câu kết luận nói về.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.7` bấm thẻ.
