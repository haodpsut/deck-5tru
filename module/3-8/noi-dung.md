---
tieu-de: Mô phỏng NTN đáng tin
phu-de: Trụ 3 NTN · module 3.8
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 80.5
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

Danh mục tham số tôi khai có đủ để người khác dựng lại đúng con số của tôi không, và dòng nào thiếu thì con số nào mất chỗ ở?

## Mười hai dòng, và luật hai đường
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này ngắn nhất của trụ {{s001}} và cũng là module duy nhất không dạy một công thức mới. Nó dạy một danh mục và một luật.

## Mười hai dòng, và luật hai đường (tiếp)
@phut: 1
@che-do: noi

**Danh mục khai tối thiểu, {{s002}} dòng:** cao độ · độ nghiêng · số vệ tinh và số mặt phẳng · góc nâng tối thiểu · băng tần · băng thông · EIRP · G/T · mô hình mưa kèm mức khả dụng · mô hình kênh kèm tham số · mô hình di động người dùng · nguồn ephemeris.

## Mười hai dòng, và luật hai đường (tiếp)
@phut: 1
@che-do: noi

**Luật hai đường:** mỗi con số trong bảng kết quả phải truy được về một dòng trong danh mục trên, hoặc về một công thức trong bài. **Không có đường thứ ba.** Con số nào không truy được về một trong hai đường đó là con số không có chỗ ở, và nó sẽ không dựng lại được, kể cả bởi chính anh sáu tháng sau.

## Mười hai dòng, và luật hai đường (tiếp)
@phut: 1
@che-do: noi

Và một luật về công cụ: TLE thật cộng bộ truyền quỹ đạo SGP4 cho phần hình học, bộ mô phỏng mức hệ thống cho phần vô tuyến, nhưng **không trộn kết quả hai nguồn vào một bảng mà không khai**. Trộn hai nguồn vào một bảng là chỗ sinh ra những con số mà về sau không ai tìm được đã chạy bằng gì.

## Mười hai dòng, và luật hai đường (tiếp)
@phut: 1
@che-do: noi

Cái mà module này nhắm vào là một lớp lỗi nhà đã đếm được ba lần: khai máy và môi trường SAU khi báo số, hoặc không khai. Lần nặng nhất là một lần chạy đúng máy mà sai môi trường, thiếu hẳn một thư viện, mà vẫn ghi ra tệp kết quả, vẫn in bảng, và vẫn thoát với mã {{s003}}.

## Danh mục khai tối thiểu của một mô phỏng NTN
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Danh mục khai tối thiểu của một mô phỏng NTN · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mười hai dòng, chia ba nhóm. **Hình học:** cao độ, độ nghiêng, số vệ tinh và số mặt phẳng, góc nâng tối thiểu, nguồn ephemeris. **Vô tuyến:** băng tần, băng thông, EIRP, G/T, mô hình mưa kèm mức khả dụng, mô hình kênh kèm tham số. **Lưu lượng:** mô hình di động người dùng.

## Danh mục khai tối thiểu của một mô phỏng NTN · (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: danh mục này không phải để làm đẹp phần thiết lập, nó là **tập hợp các chỗ ở hợp lệ cho con số**. Thiếu một dòng thì không phải thiếu một chi tiết: một tập con số trong bảng kết quả mất chỗ ở và không dựng lại được.

## Danh mục khai tối thiểu của một mô phỏng NTN · (tiếp)
@phut: 1
@che-do: noi

Thiếu góc nâng tối thiểu thì cửa sổ nhìn thấy và tần suất handover thành một khoảng rộng gấp hơn hai lần; thiếu mức khả dụng thì mọi con số SE ở băng Ka không còn định nghĩa được.

## Luật hai đường
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Luật hai đường · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mỗi con số trong bảng kết quả truy được về một dòng danh mục, hoặc về một công thức trong bài. Không có đường thứ ba. Thực hành kiểm: lấy một con số bất kỳ trong bảng, hỏi 'nó đến từ đâu', và nếu câu trả lời là 'từ mô phỏng' thì chưa phải câu trả lời.

## Luật hai đường · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đường thứ ba luôn tồn tại trong thực tế và nó mang tên **hằng số sai thuộc**: một con số nằm trong mã, không có trong bài, không ai khai, và nó quyết định kết quả. Cách bắt nó rẻ nhất là đi theo chiều ngược: với mỗi dòng danh mục, liệt kê những con số trong bảng kết quả sẽ đổi nếu dòng đó đổi.

## Luật hai đường · đáp (tiếp)
@phut: 1
@che-do: noi

Dòng nào không ảnh hưởng con số nào thì nó không cần khai; con số nào không bị dòng nào ảnh hưởng thì nó là con số của đường thứ ba.

## Chuỗi truy vết từ dòng khai tới con số kết quả
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`(cao độ, góc nâng tối thiểu) → d → FSPL → (mô hình mưa, mức khả dụng) → A_mưa → C/N₀ = EIRP − FSPL − A_mưa + G/T − k → SNR = C/N₀ − 10·log₁₀ B → SE → thông lượng = B · SE`

**Giả thiết nó đứng trên:**

## Chuỗi truy vết từ dòng khai tới con số kết quả (tiếp)
@phut: 1
@che-do: so

- Mỗi mũi tên là một phép tính dùng đúng các dòng danh mục ghi trong ngoặc, không dùng gì khác
- k = −228,6 dBW/K/Hz là hằng số, không phải tham số hiệu chuẩn, nên nó không chiếm một dòng danh mục
- Tần số lấy {{s006}} GHz cố định trong mô phỏng của module này, tức nó là một dòng ĐÃ khai

## Chuỗi truy vết từ dòng khai tới con số kết quả (tiếp)
@phut: 1
@che-do: so

- Hình học dùng quỹ đạo tròn và Trái Đất cầu; nếu dùng TLE thật cộng SGP4 thì nguồn ephemeris là dòng phải khai

## Chuỗi truy vết từ dòng khai tới con số kết quả · ghi chú
@phut: 1
@che-do: noi

Đọc chuỗi này theo chiều ngược là cách kiểm nhanh một đoạn phương pháp: bắt đầu từ con số cuối trong bảng, đi ngược từng mũi tên, và dừng ở mũi tên đầu tiên không có dòng khai nào đỡ. Đó chính là dòng thiếu.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s002}} | dòng | Danh mục khai tối thiểu để người khác dựng lại được một
!so {{s007}} | vòng mỗi ngày | Một TLE khai số vòng mỗi ngày (mean motion). Với quỹ đạo

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài khai cao độ {{s008}} km nhưng KHÔNG khai góc nâng tối thiểu. Người dựng lại thử 10° còn tác giả đã dùng 30°. Cửa sổ nhìn thấy của hai cách đoán lệch nhau bao nhiêu lần?

h = {{s008}}, e1 = {{s009}}, e2 = {{s010}}, Re = {{s011}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`({{s012}} - e1 - Math.asin((Re/(Re+h))⋆Math.cos(e1⋆Math.PI/180))⋆180/Math.PI)/(90 - e2 - Math.asin((Re/(Re+h))⋆Math.cos(e2⋆Math.PI/180))⋆180/Math.PI)`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s013}} lần: {{s014}} phút với 10° so với {{s015}} phút với 30°. Một dòng không khai làm con số cửa sổ nhìn thấy bất định hơn hai lần, và vì tần suất handover là nghịch đảo của nó, cả cột tần suất handover trong bảng kết quả cũng bất định đúng {{s013}} lần. Chu kỳ quỹ đạo thì triệt tiêu trong phép chia, nên tỉ số này chỉ phụ thuộc hai góc nâng và cao độ.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bảng khai thông lượng {{s017}} Gbit/s và khai SNR {{s009}} dB, nhưng KHÔNG khai băng thông. Băng thông suy ra từ chặn Shannon là bao nhiêu MHz?

R = {{s016}}, snr = {{s009}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(R/Math.log2(1 + Math.pow(10, snr/10)))/1e6`

Khoảng {{s018}} MHz. Đây là cách dùng luật hai đường theo chiều ngược: con số thông lượng truy về công thức, công thức đòi băng thông, nên băng thông suy ra được dù tác giả không khai. Và nó là một phép thử rẻ cho người phản biện: nếu con số suy ra rơi ra ngoài băng mà hệ thật có, ví dụ hệ chỉ có {{s019}} MHz, thì bảng kết quả có chỗ không khớp. Để ý chiều:

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

vì Shannon là CHẶN TRÊN của SE, băng thông thật phải LỚN HƠN {{s018}} MHz chứ không nhỏ hơn.

## Một bài khai đủ cao độ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài khai đủ cao độ, độ nghiêng, số vệ tinh, số mặt phẳng, băng tần, băng thông, EIRP, G/T, mô hình kênh và mô hình di động, nhưng không khai góc nâng tối thiểu. Nhóm con số nào mất chỗ ở nặng nhất?

## Một bài khai đủ cao độ (tiếp)
@phut: 0.5
@che-do: hoi

- Số vệ tinh cần thiết, vì nó đã được khai
- EIRP và G/T, vì chúng phụ thuộc hướng ăng ten
- Cửa sổ nhìn thấy, thời gian trú và tần suất handover
- Hằng số Boltzmann, vì nó phụ thuộc hình học

## Một bài khai đủ cao độ · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cửa sổ nhìn thấy, thời gian trú và tần suất handover**

## Một bài khai đủ cao độ · đáp (tiếp)
@phut: 1
@che-do: noi

Góc nâng tối thiểu vào trực tiếp góc tâm Trái Đất, nên nó quyết định cửa sổ nhìn thấy và mọi thứ suy ra từ cửa sổ. Thử đoán 10° so với 30° ở {{s008}} km: cửa sổ nhìn thấy đi từ {{s014}} xuống {{s015}} phút, tức bất định {{s013}} lần, và tần suất handover bất định đúng {{s013}} lần theo. EIRP và G/T là hai dòng đã khai, còn hằng số Boltzmann là hằng số nên không phụ thuộc gì.

## Phần hình học của bài lấy từ TLE thật qua SGP4
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phần hình học của bài lấy từ TLE thật qua SGP4, phần vô tuyến lấy từ một bộ mô phỏng mức hệ thống chạy trên quỹ đạo tròn lý tưởng. Cả hai cùng vào Bảng III. Phải làm gì?

## Phần hình học của bài lấy từ TLE thật qua SGP4 (tiếp)
@phut: 0.5
@che-do: hoi

- Bỏ phần SGP4 và chuyển hết sang quỹ đạo tròn cho nhất quán
- Giữ nguyên nhưng thêm một câu nói rằng hai công cụ đều được chấp nhận trong tài liệu
- Không cần làm gì, vì hai quỹ đạo gần như trùng nhau nên sai số nhỏ
- Khai rõ dòng nào của bảng đến từ nguồn nào, và kiểm rằng hai nguồn cho cùng hình học trong khoảng sai số đã khai

## Phần hình học của bài lấy từ TLE thật qua SGP4 · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khai rõ dòng nào của bảng đến từ nguồn nào, và kiểm rằng hai nguồn cho cùng hình học trong khoảng sai số đã khai**

## Phần hình học của bài lấy từ TLE thật qua SGP4 · (tiếp)
@phut: 1
@che-do: noi

Vấn đề không phải độ lớn của sai số mà là một bảng có hai hệ tham chiếu không khai. Người dựng lại chạy một trong hai công cụ sẽ khớp một nửa bảng và không hiểu nửa kia. Phương án bỏ SGP4 cũng chấp nhận được về mặt kỹ thuật nhưng nó bỏ luôn thứ duy nhất đỡ cho nhóm hình học, nên nó không phải lựa chọn tốt hơn.

## Phần hình học của bài lấy từ TLE thật qua SGP4 · (tiếp)
@phut: 1
@che-do: noi

Và câu nói 'hai công cụ đều được chấp nhận' không khai dòng nào của ai, nên không giúp dựng lại được gì.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thiết lập mô phỏng dưới đây thiếu một dòng danh mục, và có đúng một câu không dựng lại được vì chỗ thiếu đó. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chòm sao gồm {{s020}} vệ tinh ở cao độ {{s008}} km, {{s021}} mặt phẳng, độ nghiêng 53°.
- Liên kết dịch vụ ở băng Ka {{s006}} GHz, băng thông {{s010}} MHz, EIRP {{s022}} dBW, G/T {{s023}} dB/K.
- Kênh theo mô hình Rice với hệ số K = {{s009}} dB, người dùng tĩnh phân bố đều trong vệt.
- Trung bình trên {{s024}} lượt qua, cửa sổ phục vụ của một vệ tinh là {{s025}} phút.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Trung bình trên {{s024}} lượt qua, cửa sổ phục vụ của một vệ tinh là {{s025}} phút.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu đầu khai được: hình học chòm sao đủ, bốn tham số vô tuyến đủ, mô hình kênh có tham số và mô hình di động người dùng có. Dòng còn thiếu trong cả đoạn là GÓC NÂNG TỐI THIỂU, và câu cuối là câu duy nhất dùng tới nó. Hệ quả cụ thể: {{s025}} phút chỉ dựng lại được nếu góc nâng tối thiểu là 10°; với 30° con số thành {{s015}} phút, tức lệch {{s013}} lần. Nặng thêm một bậc:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

câu này còn gọi {{s025}} phút là TRUNG BÌNH trên {{s024}} lượt qua, trong khi {{s014}} phút là cửa sổ của lượt qua ĐỈNH ĐẦU, tức giá trị lớn nhất; trung bình của {{s024}} lượt qua phải nhỏ hơn hẳn. Cách sửa: khai góc nâng tối thiểu, rồi nói rõ {{s025}} phút là lớn nhất hay trung bình.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp dưới đây thiếu mức khả dụng. Bấm vào câu bị chỗ thiếu đó làm mất hiệu lực.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Suy hao mưa được tính theo ITU-R P.618 với cường độ mưa của trạm mặt đất tại Đà Nẵng.
- Góc nâng tối thiểu 10°, cao độ {{s008}} km, băng Ka {{s006}} GHz, băng thông {{s010}} MHz.
- EIRP {{s022}} dBW và G/T {{s023}} dB/K, lấy từ trang thông số của nhà cung cấp.
- Hệ đạt SE {{s026}} bit mỗi ký hiệu, cao hơn {{s027}} so với [{{s028}}].

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Hệ đạt SE {{s026}} bit mỗi ký hiệu, cao hơn {{s027}} so với [{{s028}}].**

Ba câu đầu khai đúng và khá đầy đủ: có mô hình mưa, có toạ độ, có hình học, có bốn tham số vô tuyến. Nhưng mô hình mưa không có mức khả dụng thì nó chưa cho ra một con số: P.618 trả về suy hao ỨNG VỚI một tỉ lệ phần trăm thời gian. Hệ quả:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

SE {{s026}} là con số của trời quang, tức suy hao mưa bằng {{s003}}, trong khi trong khoảng {{s003}} tới {{s029}} dB của băng Ka thì SE đi từ {{s026}} xuống {{s030}} bit mỗi ký hiệu. Nên con số không định nghĩa được, và phép so '{{s027}} cao hơn [{{s028}}]' mất hiệu lực hoàn toàn vì [{{s028}}] gần như chắc chắn khai ở một mức khả dụng khác. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

gắn mức khả dụng vào mọi con số băng Ka, và chỉ so với bài khác ở cùng mức.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp dưới đây trộn hai nguồn vào một bảng. Bấm vào câu làm việc trộn đó thành không khai được.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Hình học lượt qua được lấy từ TLE công khai của chòm sao, truyền quỹ đạo bằng SGP4.
- Thống kê vô tuyến được lấy từ một bộ mô phỏng mức hệ thống dùng quỹ đạo tròn lý tưởng ở cùng cao độ.
- Bảng III gộp cả hai: cột thời gian trú từ nguồn thứ nhất, cột SE và thông lượng từ nguồn thứ hai.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Vì hai nguồn dùng cùng cao độ nên các cột của Bảng III nhất quán với nhau.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì hai nguồn dùng cùng cao độ nên các cột của Bảng III nhất quán với nhau.**

Ba câu đầu đều là lời khai hợp lệ, và câu thứ ba thậm chí là một lời khai TỐT: nó nói rõ cột nào từ nguồn nào, đúng điều mà luật 'không trộn mà không khai' đòi. Câu cuối mới là chỗ sai:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

cùng cao độ KHÔNG suy ra nhất quán, vì quỹ đạo thật có độ lệch tâm nhỏ, có nhiễu loạn J2 và có thời điểm gốc, nên hai nguồn cho hai hình học khác nhau ở chữ số thứ hai tới thứ ba, và cho phân bố thời gian trú khác nhau nhiều hơn thế. Một câu khẳng định nhất quán phải có phép đo đi kèm. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

chạy cùng một đại lượng hình học qua CẢ HAI nguồn, in độ lệch, và chỉ gộp bảng khi độ lệch nhỏ hơn mức đã khai.

## Câu nào không được số nào chống đỡ · ca bốn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn khai môi trường chạy dưới đây có một chỗ làm toàn bộ con số không tái lập được. Bấm vào chỗ đó.

- Mô phỏng chạy trên máy trạm {{s031}} nhân, {{s032}} GB RAM, Python {{s033}}, numpy {{s034}}, mỗi cấu hình {{s006}} hạt giống.
- Mã nguồn và tệp cấu hình được công bố, kèm tệp khoá phiên bản của toàn bộ môi trường.
- Dữ liệu quỹ đạo lấy từ TLE của chòm sao, tải về từ một trang công khai.

## Câu không được chống đỡ · ca bốn · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Dữ liệu quỹ đạo lấy từ TLE của chòm sao, tải về từ một trang công khai.**

Hai câu đầu là khai môi trường rất tốt: có máy, có phiên bản thư viện, có số hạt giống, có tệp khoá phiên bản. Câu thứ ba thì thiếu đúng thứ làm TLE trở thành dữ liệu: THỜI ĐIỂM GỐC của bộ TLE và cửa sổ thời gian truyền quỹ đạo.

## Câu không được chống đỡ · ca bốn · đáp (tiếp)
@phut: 1
@che-do: noi

SGP4 mất chính xác nhanh khi đi xa thời điểm gốc, và TLE của một chòm sao đổi mỗi ngày, nên 'tải về từ một trang công khai' không xác định được bộ dữ liệu nào. Hệ quả: toàn bộ nhóm con số hình học không tái lập được, dù môi trường tính toán đã khai hoàn hảo. Cách sửa:

## Câu không được chống đỡ · ca bốn · đáp (tiếp)
@phut: 1
@che-do: noi

công bố chính các tệp TLE đã dùng cùng thời điểm gốc của chúng, hoặc khai mã định danh bộ dữ liệu và thời điểm tải.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Cao độ và góc nâng tối thiểu cho khoảng xiên lớn nhất d
- d và băng tần cho FSPL
- Mô hình mưa và mức khả dụng cho A_mưa tại góc nâng đó
- EIRP, G/T và hằng số Boltzmann cho C/N₀
- Băng thông cho SNR từ C/N₀
- Mô hình kênh và bảng điều chế mã hoá cho SE, rồi SE nhân băng thông cho thông lượng

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: cửa sổ {{s014}} phút · khoảng xiên {{s037}} km · FSPL {{s038}} dB · C/N₀ {{s039}} dBHz · SNR {{s040}} dB · SE {{s026}} bit mỗi ký hiệu · thông lượng {{s041}} Mbit/s

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dòng {{s005}} có khai: góc nâng tối thiểu** tắt đi: Bài chỉ khai cao độ, người dựng lại phải đoán góc nâng tối thiểu trong khoảng {{s009}} tới {{s010}} độ.
- **Dòng {{s035}} có khai: mô hình mưa kèm MỨC KHẢ DỤNG** tắt đi: Bài khai 'điều kiện trời quang' hoặc khai mô hình mưa mà không khai mức khả dụng.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dòng {{s036}} có khai: băng thông** tắt đi: Bảng khai thông lượng bit mỗi giây mà không khai băng thông của sóng mang.
- **Dòng {{s002}} có khai: nguồn ephemeris** tắt đi: Bài dùng quỹ đạo tròn lý tưởng ở chỗ lẽ ra phải dùng TLE thật cộng SGP4, hoặc dùng TLE mà không khai thời điểm gốc và cửa sổ truyền quỹ đạo.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Mỗi thanh kéo ở đây là một DÒNG trong danh mục khai. Kéo một thanh tức là giả định dòng đó không được khai nên người dựng lại phải đoán. Đọc xem khi dòng đó đi lang thang trong khoảng hợp lý thì con số nào trong bảng kết quả đi theo, và đi bao nhiêu.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.8` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V reports a spectral efficiency of {{s043}} bit per symbol and a throughput of {{s044}} Mbit per second, and Section IV states that rain attenuation follows ITU-R P.618. The availability level is never given. P.618 returns an attenuation for a stated percentage of time, so without that percentage the reported figures are not defined rather than merely imprecise, and the {{s045}} percent advantage over [{{s028}}] cannot be checked. Please state the availability level for every Ka band figure.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept the point and we have separated the rain model from its parameter. Every Ka band figure in Section V is now tagged with an availability level, and Table V reports three of them: at {{s046}} percent availability the spectral efficiency is {{s047}} bit per symbol, at {{s048}} percent it is {{s049}}, and at {{s050}} percent it is {{s051}}, against the clear sky value of {{s043}} that the previous version reported without a tag.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Figure {{s009}} replaces the single point with spectral efficiency as a function of availability, because the span of that one undeclared line ({{s003}} to {{s052}} dB of rain attenuation, which takes spectral efficiency from {{s043}} down to {{s053}} bit per symbol) is larger than every improvement the paper claims.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The comparison with [{{s028}}] is now made only at {{s048}} percent availability, which is the level [{{s028}}] declares, and the advantage there is {{s005}} percent rather than {{s045}} percent; we state this explicitly in the abstract. We also audited the whole evaluation against a twelve-line minimum declaration list and added the three lines that were missing: availability level, minimum elevation angle ({{s009}} degrees), and the epoch of the TLE set used for the orbital geometry.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s042}}: trả lời rằng mô hình mưa đã được khai là ITU-R P.618 nên phần kênh là tái lập được. Không phân biệt mô hình với tham số của mô hình.
- Mức {{s004}}: thêm một mức khả dụng duy nhất vào phần thiết lập, nhưng không chạy lại và vẫn giữ con số cũ cùng phép so với [{{s028}}].

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: gắn mức khả dụng vào từng con số băng Ka, chạy lại ở ít nhất ba mức, và chỉ giữ phép so với [{{s028}}] ở mức mà [{{s028}}] khai.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table III mixes two simulation sources: dwell time statistics from real TLE data propagated with SGP4, and spectral efficiency and throughput from a system level simulator running an ideal circular orbit. Section IV asserts the columns are consistent because both use the same altitude. Equal altitude does not imply equal geometry: eccentricity, J2 drift and epoch all differ. Please quantify the discrepancy or separate the tables.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced the consistency assertion with a measurement. Table III-a now lists, for the same quantity computed both ways, the longest visibility window and the distribution of dwell time: the longest window agrees to {{s054}} percent between the circular-orbit model and SGP4 on the declared TLE set, but the standard deviation of dwell time differs by {{s055}} percent, and the fraction of time with no satellite above the minimum elevation differs by {{s056}} percentage points.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Since the second group exceeds the {{s057}} percent tolerance we declare, we split the results: Table III now carries only the quantities that agree within tolerance, and the dwell time distribution and outage fraction moved to Table VIII, which is computed entirely from SGP4. We also added the epoch of the TLE set (2026-03-14T00:00Z) and the propagation window ({{s021}} hours), and we publish the TLE files themselves rather than naming a website.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

As a negative control, Appendix D runs the system level simulator on the SGP4 geometry: spectral efficiency changes by less than {{s058}} percent, which is why the radio columns could stay in Table III.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s042}}: trả lời rằng quỹ đạo của chòm sao gần tròn nên hai nguồn gần như trùng. Không có phép đo nào.
- Mức {{s004}}: thêm một câu nói rõ cột nào từ nguồn nào, nhưng vẫn giữ câu khẳng định nhất quán mà không đo.
- Mức {{s001}}: chạy cùng một đại lượng hình học qua CẢ HAI nguồn, in độ lệch, và chỉ gộp bảng nếu độ lệch nhỏ hơn mức đã khai; nếu không thì tách thành hai bảng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.8` bấm thẻ.
