---
tieu-de: UAV và HAPS: năng lượng và tuổi thông tin
phu-de: Trụ 3 NTN · module 3.6
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 77
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

Mô hình năng lượng tôi dùng có phi tuyến theo vận tốc không, và AoI trung bình tôi báo tính theo định nghĩa nào, trên nút nào?

## Hai chỗ bài UAV hay thổi số
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này là module nặng nhất của trụ {{s001}}, vì nó chứa hai ca mẫu của một lớp lỗi mà nhà đã đếm được: **chọn mô hình cho số nghe kêu hơn**.

## Hai chỗ bài UAV hay thổi số (tiếp)
@phut: 1
@che-do: noi

Ca thứ nhất là năng lượng. Mô hình công suất bay của cánh quay **có cực tiểu ở vận tốc khác {{s002}}**. Hệ quả ngược trực giác: bay chậm nhất KHÔNG tiết kiệm nhất, và **treo một chỗ là tốn nhất trong cả vùng vận tốc thấp**. Nếu thay nó bằng mô hình tuyến tính theo quãng đường thì treo thành miễn phí, con số năng lượng nhỏ đi, và quan trọng hơn:

## Hai chỗ bài UAV hay thổi số (tiếp)
@phut: 1
@che-do: noi

**nghiệm quỹ đạo tối ưu đổi về bản chất**, vì bài toán thành bài toán đường đi ngắn nhất mà thời gian treo không có giá.

Ca thứ hai là AoI. `AoI trung bình` và `AoI đỉnh` là hai ràng buộc khác nhau, và có những quỹ đạo làm cái thứ nhất tốt hơn trong khi cái thứ hai tệ hơn nhiều. Báo một trong hai là bỏ một nửa bài toán.

## Hai chỗ bài UAV hay thổi số (tiếp)
@phut: 1
@che-do: noi

Thêm một chỗ phải phân biệt: **vận tốc công suất nhỏ nhất** (bay lâu nhất với một viên pin) KHÁC **vận tốc năng lượng mỗi mét nhỏ nhất** (đi xa nhất với một viên pin). Với một chuyến đi có quãng đường cố định thì cái thứ hai mới là cái đúng, và nó nằm ở vận tốc cao hơn khá nhiều.

## Hình dáng của P(V) cho cánh quay
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Hình dáng của P(V) cho cánh quay · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Ba số hạng: cánh quay tăng theo `V²`, cảm ứng GIẢM theo `V` trong vùng vận tốc thấp, ký sinh tăng theo `V³`. Tổng của một hàm giảm và hai hàm tăng là một đường hình chữ U: **có cực tiểu ở vận tốc khác {{s002}}**.

## Hình dáng của P(V) cho cánh quay · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: với bộ tham số của Zeng, Xu, Zhang {{s004}}, treo một chỗ tốn khoảng {{s005}} W, cực tiểu công suất nằm ở khoảng {{s006}} m/s và chỉ tốn khoảng {{s007}} W, tức bay tốn ít hơn treo khoảng một phần tư công suất. Đường cong quay lại mức công suất treo ở khoảng {{s008}} m/s, nên treo là phương án tốn nhất của toàn bộ vùng từ {{s002}} tới {{s009}} m/s.

## Hai vận tốc tối ưu, đừng lẫn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Hai vận tốc tối ưu, đừng lẫn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Vận tốc bay lâu nhất** là điểm cực tiểu của `P(V)`, khoảng {{s006}} m/s. Nó trả lời câu hỏi: treo lơ lửng quan sát một chỗ thì bay vòng ở vận tốc nào để pin lâu hết nhất. **Vận tốc đi xa nhất** là điểm cực tiểu của `P(V)/V`, tức năng lượng mỗi mét, khoảng {{s010}} m/s với cùng bộ tham số.

## Hai vận tốc tối ưu, đừng lẫn · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: bài toán ghé thăm một tập nút cảm biến có quãng đường gần như cố định, nên **vận tốc đúng là {{s010}} m/s chứ không phải {{s006}} m/s**. Lấy cực tiểu của `P(V)` làm vận tốc hành trình là một lỗi trộn hai bài toán, và nó làm năng lượng chuyến bay cao hơn khoảng {{s011}} so với tối ưu thật: trên vòng mặc định của mô phỏng, {{s012}} kJ thay vì {{s013}} kJ.

## Hai vận tốc tối ưu, đừng lẫn · đáp (tiếp)
@phut: 1
@che-do: noi

Đặc tả gọi cực tiểu của `P(V)` là 'vận tốc tiết kiệm năng lượng nhất'; cách gọi đó chỉ đúng cho bài toán bay lâu, không đúng cho bài toán ghé nút.

## AoI trung bình so với AoI đỉnh
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s001}} trên bốn.*

## AoI trung bình so với AoI đỉnh · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

AoI là `Δ(t) = t − U(t)` với `U(t)` là thời điểm SINH của gói mới nhất đã nhận. Nó không phải trễ (trễ đo một gói), không phải thông lượng (thông lượng đo số gói). Với lấy mẫu chu kỳ `T` và thời gian phục vụ `S`: `AoI trung bình ≈ T/2 + E[S]`, `AoI đỉnh ≈ T + S`.

## AoI trung bình so với AoI đỉnh · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: hai đại lượng này tối ưu theo hai nghiệm khác nhau. Bỏ thăm một nút xa cứ vài vòng một lần làm chu kỳ của các nút gần ngắn đi, nên AoI trung bình theo nút tốt hơn, trong khi nút bị bỏ thăm có AoI đỉnh tệ hơn nhiều lần.

## AoI trung bình so với AoI đỉnh · đáp (tiếp)
@phut: 1
@che-do: noi

Một ứng dụng có hạn tươi cứng thì chỉ quan tâm AoI đỉnh, nên báo AoI trung bình giảm {{s014}} mà không nói AoI đỉnh tăng {{s015}} là báo nửa bài toán.

## Công suất bay của cánh quay
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`P(V) = P₀(1 + 3V²/U_tip²) + P_i·[ sqrt(1 + V⁴/(4v₀⁴)) − V²/(2v₀²) ]^(1/2) + (1/2)·d₀·ρ·s·A·V³`

**Giả thiết nó đứng trên:**

## Công suất bay của cánh quay (tiếp)
@phut: 1
@che-do: so

- Bay ngang ở vận tốc không đổi, không gia tốc, nên không có số hạng năng lượng động học
- Gió bằng {{s002}}, nên V là vận tốc so với đất và cũng là vận tốc so với không khí
- Khối lượng không đổi trong chuyến bay, nên P₀ và P_i là hằng số
- Mật độ không khí ρ không đổi, tức bay ở một cao độ

## Công suất bay của cánh quay (tiếp)
@phut: 1
@che-do: so

- Bộ tham số của Zeng, Xu, Zhang {{s004}}: P₀ = {{s016}} W, P_i = {{s017}} W, U_tip = {{s018}} m/s, v₀ = {{s019}} m/s, d₀ = {{s020}}, ρ = {{s021}} kg/m³, s = {{s022}}, A = {{s023}} m²

## Công suất bay của cánh quay · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Hai cực tiểu khác nhau, đừng trộn. Cực tiểu của `P(V)` ở khoảng {{s006}} m/s cho công suất {{s007}} W, dùng cho bài toán bay LÂU. Cực tiểu của `P(V)/V` ở khoảng {{s010}} m/s cho {{s024}} J mỗi mét, dùng cho bài toán đi XA, tức bài toán ghé một tập nút. Và `P(0) = P₀ + P_i = {{s025}} W`: treo một chỗ tốn hơn bay ở cả hai vận tốc đó.

## AoI của lấy mẫu chu kỳ
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Δ(t) = t − U(t); AoI trung bình ≈ T/2 + E[S]; AoI đỉnh ≈ T + S`

**Giả thiết nó đứng trên:**

## AoI của lấy mẫu chu kỳ (tiếp)
@phut: 1
@che-do: so

- Không mất gói: mọi gói sinh ra đều tới đích
- Hàng đợi không tích luỹ, tức tốc độ phục vụ theo kịp tốc độ sinh, nên S không phình theo thời gian
- Lấy mẫu đúng chu kỳ T, không jitter, nên đường AoI là răng cưa đều
- Một nguồn một đích, không cạnh tranh tài nguyên với nguồn khác

## AoI của lấy mẫu chu kỳ · ghi chú
@phut: 1
@che-do: noi

Bỏ hai giả thiết đầu thì phải dùng công thức theo hàng đợi, và lúc đó **AoI trung bình với AoI đỉnh tách nhau rất xa** vì đuôi phân bố thời gian chờ chi phối AoI đỉnh. Đó là lý do một bài khai 'AoI trung bình {{s026}} s' mà không khai mô hình hàng đợi thì con số đó không truy được về đâu.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s027}} |  | Trong công thức AoI trung bình của lấy mẫu chu kỳ
!so {{s028}} | W | Với bộ tham số cánh quay in trong Zeng
!so {{s029}} | m/s | Với cùng bộ tham số cánh quay đó

## Với bộ tham số Zeng 2019
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Với bộ tham số Zeng {{s004}}, tỉ số giữa công suất bay ở {{s030}} m/s và công suất lúc treo một chỗ là bao nhiêu?

V = {{s030}}, P0 = {{s031}}, Pi = {{s032}}, Ut2 = {{s033}}, f4 = {{s034}}, f2 = {{s035}}, c3 = {{s036}}

## Với bộ tham số Zeng 2019 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(P0⋆(1+3⋆V⋆V/Ut2) + Pi⋆Math.sqrt(Math.sqrt(1+Math.pow(V,4)/f4) - V⋆V/f2) + c3⋆Math.pow(V,3))/(P0+Pi)`

Khoảng {{s037}}, tức bay ở {{s030}} m/s chỉ tốn khoảng ba phần tư công suất của treo một chỗ. Chiều của con số là chỗ phải nhớ: tỉ số NHỎ HƠN {{s038}} nên bay rẻ hơn treo. Mô hình tuyến tính theo quãng đường cho tỉ số này bằng vô cùng, vì nó đặt công suất treo bằng {{s002}}, và đó là lý do nghiệm của nó thích treo.

## Một nút được ghé theo chu kỳ T = 120 s
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một nút được ghé theo chu kỳ T = {{s018}} s, thời gian phục vụ S = {{s039}} s, không mất gói và hàng đợi không tích luỹ. Tỉ số giữa AoI đỉnh và AoI trung bình là bao nhiêu?

T = {{s018}}, S = {{s039}}

## Một nút được ghé theo chu kỳ T = 120 s · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(T + S)/(T/2 + S)`

Khoảng {{s040}} lần, tức AoI đỉnh gần gấp đôi AoI trung bình ngay trong trường hợp dễ nhất, là lấy mẫu đúng chu kỳ và phục vụ đều. Tỉ số này tiến tới {{s003}} khi S nhỏ so với T, và giảm về {{s038}} khi S lớn.

## Một nút được ghé theo chu kỳ T = 120 s · đáp (tiếp)
@phut: 1
@che-do: noi

Nên một bài chỉ báo AoI trung bình thì người đọc vẫn đoán được AoI đỉnh trong trường hợp lý tưởng; cái không đoán được là trường hợp có mất gói hoặc có hàng đợi tích luỹ, vì lúc đó tỉ số do đuôi phân bố quyết định.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một UAV cánh quay phải ghé {{s039}} nút trên một vòng dài {{s041}} m rồi về chỗ cũ. Vận tốc hành trình nào làm năng lượng chuyến bay nhỏ nhất, với bộ tham số Zeng 2019?

- Khoảng {{s010}} m/s, vì đó là cực tiểu của P(V)/V
- Càng nhanh càng tốt, vì thời gian bay ngắn hơn
- Càng chậm càng tốt, vì công suất tăng theo vận tốc
- Khoảng {{s006}} m/s, vì đó là cực tiểu của P(V)

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khoảng {{s010}} m/s, vì đó là cực tiểu của P(V)/V**

Quãng đường cố định nên năng lượng bằng tích của năng lượng mỗi mét với quãng đường, và năng lượng mỗi mét là P(V)/V. Cực tiểu của P(V) ở {{s006}} m/s trả lời câu hỏi khác: bay LÂU nhất. Chạy thử trên vòng mặc định: {{s006}} m/s cho {{s042}} kJ còn {{s043}} m/s cho {{s044}} kJ.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Bay chậm hơn nữa thì tệ nhanh, vì thời gian bay dài ra mà công suất không giảm tương ứng; bay nhanh hơn {{s045}} m/s thì số hạng ký sinh theo V³ ăn hết phần lợi về thời gian.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Thay mô hình năng lượng phi tuyến bằng mô hình tuyến tính theo quãng đường. Điều gì đổi?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chỉ con số năng lượng, nghiệm quỹ đạo giữ nguyên vì hình học không đổi
- Chỉ nghiệm quỹ đạo, con số năng lượng vẫn so được vì đã hiệu chuẩn c
- Cả con số và nghiệm quỹ đạo, vì thời gian treo mất giá nên bài toán thành bài toán đường đi ngắn nhất
- Không đổi gì đáng kể nếu c được hiệu chuẩn từ dữ liệu bay thật

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Cả con số và nghiệm quỹ đạo, vì thời gian treo mất giá nên bài toán thành bài toán đường đi ngắn nhất**

Mô hình tuyến tính không có số hạng nào phụ thuộc thời gian, nên treo một chỗ có giá {{s002}}. Hàm mục tiêu đổi, nên nghiệm đổi: nó cho phép treo bao lâu cũng được miễn đường đi ngắn. Con số cũng đổi, ở trạng thái mặc định của mô phỏng là thấp hơn {{s046}}.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Và hiệu chuẩn c không cứu được, vì giá trị c khớp ({{s047}} J mỗi mét) phụ thuộc chính thời gian treo của quỹ đạo đang xét, tức c là tham số của một quỹ đạo chứ không của máy bay.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả dưới đây có một câu làm phần nghiệm thu mất hiệu lực. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Quỹ đạo tối ưu ghé {{s039}} nút gần mỗi vòng và ghé nút xa một lần mỗi hai vòng.
- AoI trung bình theo nút giảm từ {{s048}} s xuống {{s049}} s, tức tốt hơn {{s050}}.
- Ngân sách năng lượng mỗi chu kỳ được khai là {{s051}} kJ, quỹ đạo dùng {{s052}} kJ.
- Do đó quỹ đạo thoả ràng buộc tươi {{s053}} s của ứng dụng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Do đó quỹ đạo thoả ràng buộc tươi {{s053}} s của ứng dụng.**

Ba câu đầu đều khai được: quỹ đạo rõ, AoI trung bình có cả giá trị trước và sau, ngân sách năng lượng có số và có mức dùng. Câu cuối mới sai: ràng buộc tươi {{s053}} s là ràng buộc trên AoI ĐỈNH, mà chính quỹ đạo này đẩy AoI đỉnh từ {{s054}} lên {{s055}} s, tức VI PHẠM ràng buộc đúng ở chỗ nó vừa khoe cải thiện.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

AoI trung bình tốt hơn không suy ra AoI đỉnh tốt hơn, và ở đây hai thứ đi ngược chiều nhau. Cách sửa: in AoI đỉnh của nút tệ nhất cạnh AoI trung bình, và nghiệm thu bằng AoI đỉnh nếu ứng dụng có hạn tươi cứng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô hình hệ thống dưới đây có một chỗ làm nghiệm tối ưu sai về bản chất. Bấm vào chỗ đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Năng lượng bay được mô hình bằng E = c·L với c = {{s024}} J mỗi mét, hiệu chuẩn từ điểm năng lượng mỗi mét nhỏ nhất của máy bay.
- UAV phải treo tại mỗi nút đủ lâu để thu hết dữ liệu của nút đó.
- Bài toán được giải bằng cách tối thiểu hoá tổng quãng đường bay với ràng buộc ngân sách năng lượng.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Bài toán được giải bằng cách tối thiểu hoá tổng quãng đường bay với ràng buộc ngân sách năng lượng.**

Hai câu đầu đều hợp lệ như lời khai: câu một khai rõ mô hình và cách hiệu chuẩn, câu hai khai rõ là có treo. Câu ba mới là chỗ sai, và nó sai vì hai câu trên đặt cạnh nhau:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

dưới E = c·L thì thời gian treo của câu hai có giá bằng {{s002}}, nên 'tối thiểu hoá tổng quãng đường' KHÔNG phải tối thiểu hoá năng lượng, và nghiệm tìm được sẽ treo thoải mái ở nút gần nhất trong khi năng lượng thật tốn {{s025}} W mỗi giây treo. Với quỹ đạo mặc định của mô phỏng, chênh lệch là {{s046}}. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

hoặc thêm số hạng P(0) nhân tổng thời gian treo vào mục tiêu, hoặc dùng P(V) phi tuyến và tối thiểu hoá theo thời gian thay vì theo quãng đường.

## Dẫn lại từng bước · ca một
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Ngay sau một lần nhận, tuổi của thông tin tại đích bằng đúng S, vì gói mất S để đi
- Giữa hai lần nhận, tuổi tăng với độ dốc {{s038}} theo thời gian
- Nên đường AoI là răng cưa đi từ S lên S + T rồi rơi về S, chu kỳ T
- Trung bình thời gian của một răng cưa tuyến tính là trung bình hai đầu, tức S + T/2

## Dẫn lại từng bước · ca hai
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Mô hình tuyến tính khai E = c·L, tức năng lượng chỉ phụ thuộc quãng đường bay
- Treo một chỗ có L = {{s002}} nên E = {{s002}}: dưới mô hình này treo là MIỄN PHÍ
- Bài toán tối ưu thành bài toán đường đi ngắn nhất, và thời gian treo tại nút trở thành biến tự do không có giá

## Dẫn lại từng bước · ca hai (tiếp)
@phut: 1
@che-do: so

- Mô hình phi tuyến thì P(0) = {{s025}} W, cao hơn công suất ở mọi vận tốc từ {{s002}} tới {{s008}} m/s
- Nên nghiệm phi tuyến đổi treo thành bay vòng quanh nút ở vận tốc đi xa nhất, hình quỹ đạo khác về bản chất, không chỉ khác độ dài
- Và con số của mô hình tuyến tính nhỏ hơn: ở trạng thái mặc định của mô phỏng nó báo thấp hơn khoảng {{s056}}, đúng ở chỗ nó bỏ qua

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: P(12 m/s) = {{s057}} W · năng lượng một chu kỳ phi tuyến {{s058}} kJ · tuyến tính {{s059}} kJ · lệch âm {{s046}} · AoI trung bình theo nút {{s048}} s · AoI đỉnh {{s054}} s

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mô hình năng lượng phi tuyến theo vận tốc** tắt đi: Thay bằng mô hình tuyến tính theo quãng đường, E = c·L, với c hiệu chuẩn ở điểm năng lượng mỗi mét nhỏ nhất ({{s024}} J mỗi mét).
- **Không mất gói và hàng đợi không tích luỹ** tắt đi: Có mất gói và có lúc hàng đợi dồn, nên thời gian phục vụ S là biến ngẫu nhiên có đuôi.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Các nút có cùng độ quan trọng** tắt đi: Mỗi nút có một trọng số tươi riêng, hoặc một hạn tươi cứng riêng.
- **Gió bằng {{s002}} và khối lượng không đổi** tắt đi: Có gió, và khối lượng giảm dần nếu UAV nhả tải hoặc tăng nếu thu mẫu.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Một UAV cánh quay ghé một vòng gồm nNut nút gần cách nhau dNut, cộng một nút xa nằm cách vòng dXa và chỉ được ghé một lần mỗi kBo vòng. Trang tính song song hai mô hình năng lượng cho CÙNG một quỹ đạo, cộng AoI trung bình theo nút và AoI đỉnh của hệ. Mô hình tuyến tính không có chỗ nào để tính tiền thời gian treo, nên nó luôn báo thiếu phần đó.

## Chỗ này phải tự kéo, không xem được (tiếp)
@phut: 1
@che-do: demo

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.6` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III models propulsion energy as a linear function of travelled distance. For a rotary-wing platform the power curve has a nonzero-speed minimum and hovering is the most expensive regime below roughly {{s009}} m/s, so a distance-linear model assigns zero cost to hovering. This does not merely rescale your energy figure; it changes the optimizer's objective and therefore the optimal trajectory. Please justify the model or report both.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced the distance-linear model with the rotary-wing power model of Zeng et al. and we now report both, because the reviewer's point is about the objective and not only about the reported figure. For the trajectory of Figure {{s060}} the nonlinear model gives {{s061}} kJ per cycle while the distance-linear model gives {{s062}} kJ, an underestimate of {{s063}} percent, even though c was calibrated at the aircraft's best energy-per-metre point of {{s064}} J per metre. The gap is the hovering time:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

{{s065}} s at {{s028}} W. We also report that the linear coefficient required to match the nonlinear figure on this trajectory is {{s066}} J per metre, which is {{s067}} times the best value the aircraft can achieve and which changes with the trajectory itself, so c is a property of a trajectory rather than of the platform. Re-solving the problem under the nonlinear model changes the solution structure rather than only its length:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

hovering is replaced by loitering at the maximum-range speed of {{s068}} m/s, and the cruise speed moves from the minimum-power speed of {{s029}} m/s to {{s068}} m/s. As a negative control, Table VII evaluates the linear-model solution under the nonlinear model: it costs {{s069}} percent more than the nonlinear solution. Energy comparisons against prior work are now grouped by energy model.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s038}}: trả lời rằng mô hình tuyến tính được dùng rộng rãi trong tài liệu và hệ số c được hiệu chuẩn từ dữ liệu bay. Đúng về thực hành, không trả lời được rằng treo có giá {{s002}} dưới mô hình đó.
- Mức {{s003}}: thêm một số hạng công suất treo vào công thức năng lượng nhưng vẫn giữ nghiệm quỹ đạo cũ và vẫn báo con số cũ ở abstract.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: chạy lại bài toán tối ưu với mô hình phi tuyến đầy đủ, báo cả hai con số năng lượng cho CÙNG một quỹ đạo kèm độ lệch, và báo cả hai nghiệm quỹ đạo để cho thấy chúng khác nhau về hình.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The abstract claims an {{s070}} percent reduction in average AoI. Table VI shows the proposed trajectory visits the remote node once every two cycles. Average AoI over nodes is dominated by the eight near nodes, so this reduction is compatible with a large increase in peak AoI at the remote node. The freshness requirement stated in Section II is a hard deadline. Please report peak AoI per node and restate the claim against the requirement that your application actually has.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right and we have corrected both the metric and the claim. Table VI now lists peak AoI for every node, and Figure {{s039}} replaces the single operating point with the tradeoff frontier between average AoI over nodes and system peak AoI, parameterised by how often the remote node is visited.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The configuration that gave the {{s070}} percent average improvement (visiting the remote node once every two cycles) raises system peak AoI from {{s071}} s to {{s072}} s and therefore violates the {{s053}} s hard deadline of Section II, so it is no longer presented as the proposed operating point. The trajectory we now propose visits every node each cycle, meets the deadline with peak AoI {{s071}} s, and we report its average AoI of {{s073}} s without claiming an improvement in that quantity.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also state explicitly that averaging uniformly over nodes gives the eight near nodes eight ninths of the weight, which is why an average can hide one starved node, and we give the weighted alternative in Appendix C. Energy for the proposed trajectory is {{s061}} kJ per cycle against the {{s051}} kJ budget.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s038}}: trả lời rằng AoI trung bình là chỉ số chuẩn trong tài liệu AoI. Không nối con số với ràng buộc của ứng dụng.
- Mức {{s003}}: thêm AoI đỉnh của toàn hệ như một con số duy nhất, nhưng vẫn để {{s050}} ở abstract và không in theo từng nút.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s001}}: in bảng AoI đỉnh theo từng nút, nhận rằng ràng buộc tươi cứng được nghiệm thu bằng AoI đỉnh, và sửa abstract thành tuyên bố về đại lượng đúng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.6` bấm thẻ.
