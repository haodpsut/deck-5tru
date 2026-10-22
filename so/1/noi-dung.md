---
tieu-de: Số phải dẫn lại được trong *ba mươi giây*
phu-de: Trụ 1 NID · số, công thức, và giả thiết của chúng
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 95
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: NID
@phut: 0.5
@che-do: noi
@notes: Deck này để đọc to, có đồng hồ. Không để đọc thầm.

## Luật của deck này
@phut: 0.5
@che-do: noi
@notes: Nói luật rồi bắt đầu. Đây là deck duy nhất của bộ mà đọc thầm là vô nghĩa.

{{TAKE_HOME}}

Mỗi slide hỏi một con số hoặc một công thức. Dẫn lại **bằng miệng trong ba mươi giây**, rồi mới lật. Bấm máy tính là tính sai mục đích.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Báo động khi Λ(x) = p(x | tấn công) / p(x | bình thường) ≥ τ`

## Giả thiết
@phut: 0.5
@che-do: so

- biết cả hai phân bố điều kiện p(x | tấn công) và p(x | bình thường)
- chi phí của hai loại lỗi cố định, nên tỉ số chi phí chọn được một τ duy nhất
- một ngưỡng duy nhất, áp cho mọi mẫu và mọi thời điểm
- đơn vị quan sát x cố định, cùng một x cho cả bộ phát hiện và cho baseline

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`AUC = P(s(x₊) > s(x₋)) = U / (n₊ · n₋)`

## Giả thiết
@phut: 0.5
@che-do: so

- không có hoà điểm, hoặc hoà điểm được tính một nửa
- mọi mẫu dùng cùng một hàm điểm s và cùng một thang điểm
- hai mẫu lấy độc lập từ hai phân bố điều kiện, nên tỉ lệ nền không vào công thức

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Liên kết {{s001}} Gbps, khung Ethernet ngắn nhất {{s002}} byte. Tốc độ gói tối đa là bao nhiêu triệu gói mỗi giây?

*Module {{s003}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s004}} | triệu gói mỗi giây | module {{s003}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng liên kết {{s001}} Gbps và khung {{s002}} byte. Ngân sách thời gian để xử lý một gói là bao nhiêu nano giây?

*Module {{s003}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s005}} | nano giây | module {{s003}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trên Ethernet, mỗi khung còn kéo theo bao nhiêu byte phí nằm ngoài khung (phần mở đầu, SFD và khoảng liên khung)?

*Module {{s003}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s006}} | byte | module {{s003}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Liên kết {{s001}} Gbps, khung {{s002}} byte, phí ngoài khung {{s006}} byte. Tốc độ gói tối đa là bao nhiêu gói mỗi giây?

bit = {{s007}}, khung = {{s002}}, phi = {{s006}}

## Đáp
@phut: 0.5
@che-do: so

`bit / ((khung + phi) × {{s008}})`

Khoảng {{s009}} triệu gói mỗi giây, phân số đúng là {{s010}}. Nghịch đảo của nó là {{s011}} nano giây cho mỗi gói. Đó là lý do mọi bộ phát hiện đặt ở mức gói đều phải là mô hình nhỏ hoặc phần cứng: {{s012}} nano giây không đủ cho một lượt suy diễn mạng neural trên CPU.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

FPR mức gói là 10⁻⁴. Gộp {{s006}} gói thành một luồng theo luật báo động nếu có ít nhất một gói vượt ngưỡng. FPR mức luồng là bao nhiêu phần trăm?

f = {{s013}}, n = {{s006}}

## Đáp
@phut: 0.5
@che-do: so

`{{s014}} × ({{s015}} - Math.pow(1 - f, n))`

Khoảng {{s016}}, trong khi FPR mức gói là {{s017}}. Con số mức luồng lớn hơn khoảng {{s018}} lần, tức gần đúng bằng n lần. Hệ quả cho bài báo: nếu bảng của anh khai FPR 10⁻⁴ ở mức gói mà baseline khai FPR ở mức luồng, thì anh đang so với một con số bị quy đổi lệch gần {{s006}} lần, và không có cách nào sửa bằng cách huấn luyện lại.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Tỉ lệ lớp A sau khi nhân r lần = r·p_A / (r·p_A + {{s015}} − p_A) I(X_i; Y) = Σ p(x,y) · log( p(x,y) / (p(x) · p(y)) )`

## Giả thiết
@phut: 0.5
@che-do: so

- nhân bản không thêm thông tin, nên độ chính xác trong từng lớp không đổi và chỉ trọng số của lớp đổi
- đủ mẫu để ước lượng p(x,y), nếu không thì I bị thiên lệch dương theo số ô của bảng tần số
- X_i rời rạc hoặc đã rời rạc hoá, và cách rời rạc hoá là một phần của phép đo chứ không trung lập

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trong tập huấn luyện của KDD99, khoảng bao nhiêu phần trăm bản ghi là bản trùng?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s020}} | % | module {{s019}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Tập KDDTrain+ của NSL-KDD có bao nhiêu bản ghi?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s021}} | bản ghi | module {{s019}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Tập KDDTest+ của NSL-KDD có bao nhiêu bản ghi?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s022}} | bản ghi | module {{s019}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

UNSW-NB15 gồm khoảng {{s023}} triệu bản ghi và {{s024}} họ tấn công. Mỗi bản ghi có bao nhiêu đặc trưng?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s025}} | đặc trưng | module {{s019}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

CIC-IDS2017 thu lưu lượng {{s026}} ngày liên tiếp từ thứ Hai tới thứ Sáu. CICFlowMeter sinh ra bao nhiêu đặc trưng cho mỗi luồng?

*Module {{s019}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s027}} | đặc trưng | module {{s019}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Nhãn trong dataset bị lật đối xứng với tỉ lệ {{s030}}. Một mô hình đúng thật {{s031}} so với nhãn sạch sẽ cho accuracy quan sát bao nhiêu phần trăm khi chấm trên nhãn nhiễu?

a = {{s028}}, eps = {{s029}}

## Đáp
@phut: 0.5
@che-do: so

`{{s014}} × (a × ({{s015}} - eps) + ({{s015}} - a) × eps)`

## Đáp (tiếp)
@phut: 0.5
@che-do: so

{{s032}}, phân số đúng {{s033}}. Trần của accuracy quan sát với {{s030}} nhãn lật là {{s034}}, đạt bởi một mô hình đúng thật {{s035}}. Nên một bài báo khai accuracy quan sát {{s031}} trên cùng tập nhãn đó đang báo con số CAO HƠN trần, và chỉ có hai lối giải thích: nhãn không nhiễu tới {{s030}}, hoặc con số đang đo khả năng ghi nhớ bản trùng chứ không đo khả năng tổng quát hoá.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Hệ quả thứ hai, dùng ngay khi phản biện: khoảng cách thật {{s036}} điểm phần trăm giữa hai mô hình chỉ còn quan sát được {{s037}} điểm, vì nó bị co theo hệ số ({{s015}} − 2ε) = {{s038}}.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

KDD99 có khoảng {{s041}} bản ghi huấn luyện là bản trùng. Giả sử toàn bộ phần trùng rơi vào một lớp, và lớp đó chiếm {{s042}} tập bản ghi duy nhất. Lớp đó chiếm bao nhiêu phần trăm tập có trùng?

du = {{s039}}, pa = {{s040}}

## Đáp
@phut: 0.5
@che-do: so

`{{s014}} × (du + ({{s015}} - du) × pa)`

{{s043}}, phân số đúng {{s044}}. Một bộ phân loại tầm thường luôn trả lớp đó đạt accuracy {{s043}} trên tập có trùng, trong khi trên tập bản ghi duy nhất nó chỉ đạt {{s042}}. Chênh {{s045}} điểm phần trăm ấy không phải mô hình, nó là bản trùng. Đó là lý do một con số accuracy trên KDD99 không so được với bất cứ thứ gì, và cũng là lý do NSL-KDD ra đời.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`TPR = TP/(TP+FN) FPR = FP/(FP+TN) Precision = TP/(TP+FP) cảnh báo sai mỗi ngày = FPR × N_lành`

## Giả thiết
@phut: 0.5
@che-do: so

- TPR và FPR tính trong từng lớp, nên không phụ thuộc tỉ lệ nền
- Precision trộn hai lớp, nên đổi tỉ lệ nền là đổi giá trị
- N_lành là số sự kiện lành thật sự đi qua bộ phát hiện trong một ngày

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

FPR = 10⁻³ trên {{s001}} triệu sự kiện lành mỗi ngày. Bao nhiêu cảnh báo sai mỗi ngày?

*Module {{s046}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s047}} | cảnh báo mỗi ngày | module {{s046}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Ngân sách cảnh báo là {{s001}} mỗi ngày, lưu lượng {{s001}} triệu sự kiện lành mỗi ngày. FPR tối đa được phép là {{s001}} luỹ thừa âm bao nhiêu? Nhập số mũ.

*Module {{s046}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s048}} | số mũ âm | module {{s046}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Đường cơ sở của đường PR khi tỉ lệ nền p = 10⁻⁴ là bao nhiêu (nhập dưới dạng phần trăm)?

*Module {{s046}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s049}} | % | module {{s046}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một bảng kết quả khai TP=97, FN=3, FP=2, TN=98. MCC bằng bao nhiêu?

tp = {{s050}}, fn = {{s051}}, fp = {{s052}}, tn = {{s053}}

## Đáp
@phut: 0.5
@che-do: so

`(tp⋆tn - fp⋆fn) / Math.sqrt((tp+fp)⋆(tp+fn)⋆(tn+fp)⋆(tn+fn))`

Khoảng {{s054}}. Để ý ma trận này có TN chỉ {{s053}}, tức tập kiểm tra gần cân bằng. Cùng mô hình đó chạy ở p = 10⁻⁵ thì MCC tụt sâu, vì MCC phụ thuộc tỉ lệ nền.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

SOC có {{s051}} người, mỗi người đọc {{s055}} cảnh báo một ngày. Lưu lượng {{s057}} triệu sự kiện lành mỗi ngày. FPR tối đa được phép là bao nhiêu phần triệu (nhập số)?

nguoi = {{s051}}, moiNguoi = {{s055}}, nLanh = {{s056}}

## Đáp
@phut: 0.5
@che-do: so

`1e6 × nguoi × moiNguoi / nLanh`

Khoảng {{s058}} phần triệu, tức {{s058}} × 10⁻⁶. Con số này thấp hơn FPR của gần như mọi bài báo IDS từ hai tới bốn bậc, và đó chính là lý do thực tế mà hệ thống phát hiện phải tổng hợp cảnh báo thay vì báo từng luồng.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`PPV = (TPR · p) / (TPR · p + FPR · ({{s015}} − p))`

## Giả thiết
@phut: 0.5
@che-do: so

- p là tỉ lệ nền tại thời điểm chạy, không phải tỉ lệ trong tập kiểm tra
- các sự kiện độc lập với nhau
- một ngưỡng quyết định duy nhất, cố định

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Với p = 10⁻⁵, TPR = {{s015}}, FPR = 10⁻³: PPV bằng bao nhiêu phần trăm?

*Module {{s059}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s060}} | % | module {{s059}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Vẫn p = 10⁻⁵ và TPR = {{s015}}. Muốn PPV đạt {{s042}} thì FPR phải nhỏ hơn hoặc bằng {{s001}} luỹ thừa âm bao nhiêu? Nhập số mũ, ví dụ nhập {{s061}} nghĩa là 10⁻⁴.

*Module {{s059}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s026}} | số mũ âm | module {{s059}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

FPR = 10⁻³ trên {{s001}} triệu luồng lành mỗi ngày. Bao nhiêu cảnh báo sai mỗi ngày?

*Module {{s059}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s047}} | cảnh báo mỗi ngày | module {{s059}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một bài báo khai p = 10⁻³, TPR = {{s065}}, FPR = {{s066}}. PPV bằng bao nhiêu phần trăm?

p = {{s062}}, tpr = {{s063}}, fpr = {{s064}}

## Đáp
@phut: 0.5
@che-do: so

`{{s014}} × tpr × p / (tpr × p + fpr × ({{s015}} - p))`

Kết quả khoảng {{s067}}. FPR {{s068}} nghe nhỏ, nhưng nó lớn hơn tỉ lệ nền {{s006}} lần, nên hơn {{s034}} cảnh báo là sai.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Muốn PPV đạt {{s070}} với p = 10⁻⁴ và TPR = {{s038}} thì FPR tối đa là bao nhiêu? Nhập dưới dạng phần triệu (ppm).

p = {{s013}}, tpr = {{s069}}, ppv = {{s069}}

## Đáp
@phut: 0.5
@che-do: so
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

`1e6 × tpr × p × ({{s015}} - ppv) / (ppv × ({{s015}} - p))`

Khoảng {{s001}} phần triệu. Đây là con số nên nhớ dạng bậc: muốn tin được cảnh báo thì FPR phải xuống vùng phần triệu, không phải vùng phần trăm.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một hệ đạt FPR = 10⁻⁶ với TPR = {{s015}}, chạy ở p = 10⁻⁵. PPV bằng bao nhiêu phần trăm?

p = {{s071}}, tpr = {{s015}}, fpr = {{s072}}

## Đáp
@phut: 0.5
@che-do: so

`{{s014}} × tpr × p / (tpr × p + fpr × ({{s015}} - p))`

Khoảng {{s073}}. Chỉ khi FPR tụt xuống dưới p một bậc thì cảnh báo mới đáng tin, và đây là lý do kỹ thuật thật của việc tổng hợp nhiều tín hiệu yếu thành một cảnh báo mạnh.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`AUT(f, N) = (1/(N−1)) · Σ_{k=1}^{N−1} ( f(k) + f(k+1) ) / {{s052}}`

## Giả thiết
@phut: 0.5
@che-do: so

- Mỗi mẫu có mốc thời gian đáng tin, đủ để gán vào đúng một đợt. Dataset không có mốc thời gian thì AUT không tính được, và đó là lý do chính đáng để không dùng dataset đó
- Các đợt dài bằng nhau; nếu không thì phải lấy trọng số theo độ dài đợt, và con số không so được với bài khác
- Nội suy tuyến tính giữa hai đợt liền nhau, tức bỏ qua biến động bên trong một đợt

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Mô hình KHÔNG được huấn luyện lại trong suốt N đợt; nếu có huấn luyện lại thì phải khai chu kỳ, và AUT lúc đó là của cặp mô hình cộng chu kỳ chứ không phải của mô hình

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

TESSERACT đặt ra mấy ràng buộc thời gian riêng biệt cho phần đánh giá?

*Module {{s074}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s051}} | ràng buộc | module {{s074}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Một bộ phát hiện có F1 giảm tuyến tính từ {{s075}} ở đợt đầu về {{s076}} ở đợt cuối. AUT(f, N) bằng bao nhiêu?

*Module {{s074}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s040}} |  | module {{s074}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mô hình suy giảm theo cấp số nhân, F1 bắt đầu ở {{s065}} và mỗi tháng giữ lại {{s038}} lần tháng trước, đo trên {{s077}} đợt liền nhau, không huấn luyện lại, không khoảng trống. AUT(f, {{s077}}) bằng bao nhiêu?

f0 = {{s063}}, rho = {{s069}}, n = {{s077}}

## Đáp
@phut: 0.5
@che-do: so

`f0⋆(1+rho)/2⋆((1-Math.pow(rho,n-1))/(1-rho))/(n-1)`

Khoảng {{s078}}. Để ý hai chuyện. Thứ nhất, con số này thấp hơn f0 = {{s065}} rất nhiều, tức một bài báo chỉ báo {{s065}} đang báo cái gì đó khác hẳn với điều mà mười hai tháng vận hành sẽ cho. Thứ hai, mất {{s079}} mỗi tháng nghe như là nhỏ, mà sau mười một bước nó kéo F1 cuối kỳ về khoảng {{s080}}, nên AUT tụt xuống quá nửa khoảng cách từ {{s065}} về {{s076}}.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Cấp số nhân là chỗ trực giác tuyến tính của người đọc sai nhiều nhất.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Cùng mô hình suy giảm ở trên, f0 = {{s065}}, rho = {{s038}}, {{s077}} đợt. Con số một điểm f0 cao hơn AUT bao nhiêu phần trăm tương đối, tức (f0 − AUT) chia f0 nhân 100?

f0 = {{s063}}, rho = {{s069}}, n = {{s077}}

## Đáp
@phut: 0.5
@che-do: so

`100⋆(f0 - f0⋆(1+rho)/2⋆((1-Math.pow(rho,n-1))/(1-rho))/(n-1))/f0`

Khoảng {{s081}}, tức hơn hai phần năm. Quan trọng: con số này KHÔNG phải mức thổi của chia ngẫu nhiên so với chia theo thời gian trên một dataset thật. Nó là hệ quả thuần của mô hình suy giảm cấp số nhân với rho = {{s038}} mà ta vừa đặt ra, và nó chỉ phụ thuộc rho với N, không phụ thuộc f0.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Mức thổi thật phải đo trên dataset thật, và đó là con số bài báo phải báo chứ không được suy ra từ một mô hình suy giảm.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`không gian đặc trưng: min ||δ|| sao cho f(x+δ) ≠ y · không gian vấn đề: min ||φ(T(z0)) − φ(z0)|| sao cho f(φ(T(z0))) ≠ y, T ∈ 𝒯 · quan hệ: min trên Δ_f ≤ min trên Δ_p`

## Giả thiết
@phut: 0.5
@che-do: so

- 𝒯 là tập phép biến đổi mà kẻ tấn công thật làm được trên đối tượng thật, và nó phải được liệt kê rõ trong bài chứ không nói chung là các phép biến đổi khả thi
- T giữ nguyên ngữ nghĩa độc hại của z0; nếu không thì mẫu sinh ra không còn là tấn công và bài toán không còn đối tượng

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- φ cố định và biết được; nếu bộ trích đặc trưng của bên phòng vệ bí mật thì kẻ tấn công ở chế độ khác và bài toán phải viết lại
- Nhiễu sống sót qua tiền xử lý của bên phòng vệ, tức φ áp lên đối tượng SAU tiền xử lý
- Đối tượng sinh ra qua được một bộ kiểm tra tính hợp lý riêng, nếu bên phòng vệ có bộ đó

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Có mấy ràng buộc không gian vấn đề mà một phép biến đổi tấn công thật phải thoả đồng thời?

*Module {{s082}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s061}} | ràng buộc | module {{s082}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

CICFlowMeter, bộ trích đặc trưng dùng cho CIC-IDS2017, sinh bao nhiêu đặc trưng cho mỗi luồng? Đây là số chiều của không gian đặc trưng mà nhiễu được tìm trong đó.

*Module {{s082}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s027}} | đặc trưng | module {{s082}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Trong {{s027}} đặc trưng CICFlowMeter, kẻ tấn công chỉ chạm độc lập được {{s051}} cái, và tiền xử lý của bên phòng vệ giữ lại {{s084}} biên độ nhiễu. Chi phí tấn công thật gấp bao nhiêu lần nhiễu nhỏ nhất đo trong không gian đặc trưng?

m = {{s051}}, d = {{s027}}, s = {{s083}}

## Đáp
@phut: 1
@che-do: so

`1/(Math.sqrt(m/d)⋆s)`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s085}} lần, tức gần một bậc độ lớn chứ chưa tới một bậc. Hai chuyện phải đọc ra. Thứ nhất, con số epsilon mà bài báo báo ở trục hoành của hình độ bền phải nhân với khoảng {{s086}} mới là chi phí mà kẻ tấn công thật trả, nên một mô hình trông vỡ ở epsilon = {{s087}} thật ra vỡ ở chi phí khoảng {{s088}} trong cùng đơn vị. Thứ hai, ràng buộc toạ độ góp hệ số lớn hơn hẳn:

## Đáp (tiếp)
@phut: 1
@che-do: so

căn của {{s051}} chia {{s027}} cho hệ số khoảng {{s089}}, còn tiền xử lý chỉ cho {{s090}}. Nên nếu phải khai một ràng buộc thì khai cái về toạ độ sửa được trước.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mô hình tuyến tính w = ({{s051}}, {{s061}}) và b = {{s076}}, điểm x có f(x) = {{s001}}. Nhiễu L2 nhỏ nhất trong không gian đặc trưng để đổi dấu f bằng bao nhiêu?

fx = {{s001}}, w1 = {{s051}}, w2 = {{s061}}

## Đáp
@phut: 1
@che-do: so

`Math.abs(fx)/Math.sqrt(w1⋆w1 + w2⋆w2)`

Đúng bằng {{s052}}, vì ||w|| = {{s026}} và {{s001}} chia {{s026}} bằng {{s052}}. Đây là khoảng cách từ điểm tới siêu phẳng, không hơn. Nhớ nó là một chặn DƯỚI của chi phí thật: nếu kẻ tấn công chỉ sửa được toạ độ thứ nhất thì nhiễu nhỏ nhất là {{s001}} chia {{s051}}, tức khoảng {{s091}}, lớn hơn {{s052}}; nếu chỉ sửa được toạ độ thứ hai thì là {{s001}} chia {{s061}}, tức {{s092}}, cũng lớn hơn {{s052}}.

## Đáp (tiếp)
@phut: 1
@che-do: so

Con số {{s052}} chỉ đạt được khi sửa được cả hai toạ độ theo đúng tỉ lệ {{s051}} trên {{s061}}.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`φ_i = Σ_{S ⊆ F\{i}} ( |S|!·(|F|−|S|−1)! / |F|! )·[ f(S ∪ {i}) − f(S) ] · J = |A ∩ B| / |A ∪ B| = I / (2k − I) · chi phí TreeSHAP bậc O(T·L·D²)`

## Giả thiết
@phut: 1
@che-do: so

- Hàm giá trị f(S) định nghĩa được khi thiếu đặc trưng, tức phải CHỌN nghĩa của vắng mặt: kỳ vọng biên, kỳ vọng có điều kiện, một giá trị nền, hay trung bình trên một tập nền. Chọn khác nhau cho φ khác nhau trên cùng một mô hình
- Tập nền dùng để lấy kỳ vọng phải khai rõ; đổi tập nền là đổi φ, kể cả khi mô hình không đổi

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Với Jaccard: hai tập A và B cùng cỡ k, và dùng tập không thứ tự, tức bỏ hẳn thông tin thứ hạng bên trong top-k
- Với công thức Shapley: tổng chạy trên 2^(|F|−1) tập con, nên tính chính xác chỉ khả thi ở |F| nhỏ; mọi cài đặt trên dữ liệu bảng thật đều là xấp xỉ hoặc là thuật toán riêng cho một họ mô hình

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Với TreeSHAP: mô hình là tập hợp cây, T cây với L lá và độ sâu D; bậc O(T·L·D²) không áp cho mô hình ngoài họ cây

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Chi phí TreeSHAP có bậc O(T·L·D^x) với T cây, L lá và D độ sâu. Số mũ x của độ sâu bằng bao nhiêu?

*Module {{s093}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s052}} | số mũ | module {{s093}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Mô hình có |F| = {{s006}} đặc trưng. Để tính CHÍNH XÁC φ_i cho MỘT đặc trưng theo đúng định nghĩa, phải xét bao nhiêu tập con S?

*Module {{s093}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s094}} | tập con | module {{s093}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một rừng gradient boosting có {{s014}} cây, mỗi cây {{s002}} lá và độ sâu {{s048}}. Theo bậc O(T·L·D²), số đơn vị công việc để giải thích MỘT mẫu bằng TreeSHAP là bao nhiêu?

t = {{s014}}, l = {{s002}}, dd = {{s048}}

## Đáp
@phut: 1
@che-do: so

`t⋆l⋆Math.pow(dd,2)`

{{s095}} đơn vị công việc cho MỘT mẫu. Chỗ phải đọc ra: nhân với số mẫu cần giải thích thì con số nổ rất nhanh. Giải thích {{s096}} mẫu của tập kiểm là bậc {{s097}} tỉ đơn vị, nên phần giải thích của bài báo thường đắt hơn phần huấn luyện. Và nếu muốn đo độ ổn định top-k qua {{s006}} hạt thì nhân thêm {{s006}} lần nữa; đó là lý do thật mà nhiều bài bỏ phép đo độ ổn định:

## Đáp (tiếp)
@phut: 1
@che-do: so

nó đắt, không phải vì nó khó.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Hai lần chạy, mỗi lần báo top {{s001}} đặc trưng, và {{s048}} đặc trưng xuất hiện ở cả hai lần. Chỉ số Jaccard bằng bao nhiêu?

i = {{s048}}, k = {{s001}}

## Đáp
@phut: 1
@che-do: so

`i/(2⋆k-i)`

Khoảng {{s098}}, tức đúng phân số {{s099}}. Đây là chỗ trực giác lệch: trùng {{s048}} trên {{s001}} nghe như {{s084}}, mà Jaccard chỉ khoảng {{s100}}, vì mẫu số là HỢP của hai tập, tức {{s101}} đặc trưng, không phải {{s001}}. Hệ quả thực hành:

## Đáp (tiếp)
@phut: 1
@che-do: so

khi phản biện đòi con số độ ổn định thì báo Jaccard kèm cả k và tổng số đặc trưng, vì tỉ lệ trùng trên k phụ thuộc k theo cách khác và không so được giữa hai bài dùng k khác nhau.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`KAN: f(x) = Σ_q Φ_q( Σ_p φ_{q,p}(x_p) ) · QSVM: số phần tử phải ước lượng = n(n−1)/2 · số lần chạy mạch mỗi phần tử bậc 1/ε² · tổng số lần chạy mạch = n(n−1)/2 · 1/ε²`

## Giả thiết
@phut: 1
@che-do: so

- Với KAN: định lý Kolmogorov-Arnold là định lý TỒN TẠI của một biểu diễn, không kèm thuật toán tìm, không kèm số mẫu cần, và không bảo đảm các hàm một biến trơn. Biểu diễn được không kéo theo học được
- Với KAN: so sánh số tham số chỉ có nghĩa khi khai cùng lúc thời gian huấn luyện và thời gian suy luận, vì một tham số của KAN là một hàm trên cạnh chứ không phải một số vô hướng

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Với QSVM: ma trận nhân đối xứng và đường chéo bằng {{s015}}, tức dùng nhân fidelity giữa hai trạng thái đã mã hoá; nếu nhân khác thì số phần tử khác
- Với QSVM: mỗi phần tử nhân là một XÁC SUẤT, chỉ đọc được bằng cách chạy mạch nhiều lần rồi đếm tần suất; không có cách đọc biên độ trực tiếp

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Với QSVM: bậc 1/ε² là chặn DƯỚI, vì nó chỉ tính nhiễu lấy mẫu. Nhiễu phần cứng, lỗi đọc và trôi hiệu chuẩn đều làm số lần chạy thật lớn hơn
- Với QSVM: giả thiết có phần cứng chạy được số lần chạy mạch đó; nếu con số chạy trên bộ mô phỏng cổ điển thì mọi tuyên bố về thời gian là tuyên bố về bộ mô phỏng

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Theo Grinsztajn và cộng sự, có mấy tính chất của dữ liệu bảng làm cho tập hợp cây vẫn thắng mạng neural?

*Module {{s102}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s051}} | tính chất | module {{s102}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trong sổ lỗi của nhà, có bao nhiêu tuyên bố của bài KAN gốc đã bị phản bác bởi công trình sau đó?

*Module {{s102}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s026}} | tuyên bố | module {{s102}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

QSVM trên {{s103}} mẫu huấn luyện, muốn sai số cộng tính {{s066}} cho mỗi phần tử ma trận nhân. Tổng số lần chạy mạch cho MỘT lần huấn luyện là bao nhiêu?

n = {{s103}}, eps = {{s064}}

## Đáp
@phut: 1
@che-do: so

`n⋆(n-1)/2/(eps⋆eps)`

Khoảng {{s104}} × 10⁹ lần chạy mạch, tức gần năm tỉ. Hai chuyện phải đọc ra. Thứ nhất, nới sai số từ {{s105}} lên {{s066}} chỉ bớt được bốn lần số lần chạy, trong khi nhân đôi số mẫu từ {{s106}} lên {{s103}} lại nhân bốn, nên hai hiệu ứng triệt tiêu nhau và tổng vẫn ở cùng bậc năm tỉ. Thứ hai, con số này là CHẶN DƯỚI:

## Đáp (tiếp)
@phut: 1
@che-do: so

nó chỉ tính nhiễu lấy mẫu, chưa tính lỗi đọc, nhiễu phần cứng, trôi hiệu chuẩn, và chưa tính tinh chỉnh siêu tham số hay kiểm chéo.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Cùng QSVM, nay trên {{s107}} mẫu với sai số cộng tính {{s105}}, và mỗi lần chạy mạch mất {{s108}} giây. Một lần huấn luyện tiêu bao nhiêu ngày máy lượng tử liên tục?

n = {{s107}}, eps = {{s049}}, tq = {{s013}}

## Đáp
@phut: 1
@che-do: so

`n⋆(n-1)/2/(eps⋆eps)⋆tq/86400`

Khoảng {{s109}} ngày máy lượng tử liên tục, cho MỘT ma trận nhân ở MỘT bộ siêu tham số. Đây là con số dùng được ngay trong phản biện, theo hai chiều. Chiều thứ nhất, nếu bài báo khai chạy QSVM trên {{s107}} mẫu thật thì phải khai luôn đã chạy ở đâu và trong bao lâu, vì {{s109}} ngày là một dữ kiện kiểm được.

## Đáp (tiếp)
@phut: 1
@che-do: so

Chiều thứ hai, nếu con số thời gian trong bài nhỏ hơn thế nhiều thì nó là thời gian của bộ mô phỏng cổ điển, và lúc đó tuyên bố về tăng tốc lượng tử không có đại lượng nào đỡ. Đối chiếu: {{s107}} mẫu là một mẫu con rất nhỏ so với {{s110}} bản ghi huấn luyện của NSL-KDD.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Hiệu chuẩn hoàn hảo: P(y = {{s015}} | s(x) = p) = p ECE = sum_m (|B_m|/n) · |acc(B_m) − conf(B_m)| Hiệu chỉnh nhiệt độ: s'(x) = sigma(z(x)/T) Ngưỡng theo chi phí: q⋆ = c_FP/(c_FP + c_FN)`

## Giả thiết
@phut: 1
@che-do: so

- ECE: mỗi ô có đủ mẫu để tần suất trong ô là một ước lượng dùng được; thiếu điều này thì con số đo cái sàn chứ không đo sai lệch
- ECE: số ô M chốt TRƯỚC khi xem kết quả, nếu không thì giá trị nhỏ nhất trên một họ M là một đại lượng khác hẳn
- Hiệu chỉnh nhiệt độ: T học trên một tập hiệu chuẩn tách khỏi tập kiểm, và T lớn hơn {{s076}}

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- Ngưỡng theo chi phí: chi phí mỗi loại lỗi là một hằng số, quyết định từng luồng độc lập, và điểm số đã hiệu chuẩn nên dùng được thay cho xác suất hậu nghiệm

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Một bộ phân loại hiệu chuẩn hoàn hảo, nghĩa là P(y = {{s015}} | s(x) = p) = p với mọi p. ECE dân số của nó bằng bao nhiêu?

*Module {{s111}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s076}} |  | module {{s111}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Anh áp hiệu chỉnh nhiệt độ với một T khác {{s015}} lên cùng bộ logit, trên cùng tập đánh giá. AUROC đổi bao nhiêu?

*Module {{s111}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s076}} |  | module {{s111}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khi báo ECE, công trình nền của chủ đề này chia điểm số thành bao nhiêu ô? Nhập đúng con số nó dùng trong mọi bảng kết quả.

*Module {{s111}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s112}} | ô | module {{s111}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một bảng tin cậy chia ba ô trên {{s118}} mẫu kiểm. Ô một có {{s113}} mẫu và lệch tin cậy {{s066}}; ô hai có {{s114}} mẫu và lệch {{s119}}; ô ba có {{s116}} mẫu và lệch {{s120}}. ECE bằng bao nhiêu?

n1 = {{s113}}, d1 = {{s064}}, n2 = {{s114}}, d2 = {{s115}}, n3 = {{s116}}, d3 = {{s117}}

## Đáp
@phut: 1
@che-do: so

`(n1⋆d1 + n2⋆d2 + n3⋆d3)/(n1 + n2 + n3)`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s121}}. Con số này chỉ đọc được khi khai kèm số ô, ở đây là ba ô: cùng bộ điểm số đó chia {{s112}} ô sẽ cho một giá trị khác, thường cao hơn, vì ô hẹp hơn thì ít sai lệch trong ô bị làm phẳng. Để ý thêm là ô ba chỉ có {{s116}} mẫu mà lại mang lệch lớn nhất, nên phải kiểm xem {{s120}} là sai lệch thật hay là sàn do ít mẫu.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Bỏ sót một tấn công tốn {{s014}} đơn vị, một cảnh báo sai tốn {{s015}} đơn vị. Ngưỡng tối ưu trên xác suất hậu nghiệm bằng bao nhiêu?

cfp = {{s015}}, cfn = {{s014}}

## Đáp
@phut: 1
@che-do: so

`cfp/(cfp + cfn)`

Khoảng {{s122}}, tức đúng {{s123}}. Để ý biểu thức không chứa tỉ lệ nền: tỉ lệ nền đã nằm trong xác suất hậu nghiệm, nên ngưỡng Bayes trên xác suất là cùng một con số ở mọi mạng. Và đây là chỗ hiệu chuẩn đi vào: con số này áp trực tiếp lên điểm số của mô hình chỉ khi điểm số đã hiệu chuẩn.

## Đáp (tiếp)
@phut: 1
@che-do: so

Chưa hiệu chuẩn thì phải quét đường ROC với tỉ lệ nền khai rõ, và lúc đó ngưỡng trên thang điểm số không còn đọc được từ tỉ lệ chi phí.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Theo mô hình khai trong mô phỏng, logit lớp lành là Logistic(0, {{s015}}) nên ngưỡng điểm số {{s038}} trên thang đã chia nhiệt độ T cho FPR bằng 1/(1 + 9^T). Ở T = {{s052}}, FPR là bao nhiêu phần trăm?

T = {{s052}}

## Đáp
@phut: 1
@che-do: so

`100/(1 + Math.pow(9, T))`

Khoảng {{s124}}. Cùng ba chữ ngưỡng {{s038}} mà ở T = {{s015}} thì FPR là {{s079}}, còn ở T = {{s052}} chỉ còn {{s124}}: tám lần chênh lệch cho một nhãn ngưỡng không đổi. Đó là nội dung đầy đủ của câu ngưỡng trên điểm số chưa hiệu chuẩn là một nhãn, không phải một điểm làm việc. Hệ quả cho bài báo: phải khai điểm làm việc bằng cặp TPR với FPR, chứ không khai bằng giá trị ngưỡng.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`F_con = f1·(1 − e) + f2·(1 − e·h) + f3t·(1 − q) + f3u ti_le_mat = {{s015}} − F_con/(f1 + f2 + f3t + f3u)`

## Giả thiết
@phut: 1
@che-do: so

- e là tỉ lệ luồng đã mã hoá; nhóm tải tin lấy được đúng trên phần không mã hoá nên đóng góp f1·(1 − e)
- h là tỉ lệ luồng mã hoá có bật ECH, và bật ECH coi là độc lập với việc luồng có mã hoá hay không, nên SNI mất trên phần e·h
- q là tỉ lệ luồng dùng QUIC; f3t là số đặc trưng hình dáng luồng dựa chuỗi mức TCP, mất đúng trên phần QUIC

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- f3u là số đặc trưng chỉ cần thời điểm, kích thước và hướng gói, nên không phụ thuộc giao thức vận chuyển
- Đây là mô hình ĐẾM theo kỳ vọng trên tập luồng, không phải số đo: nó cho số đặc trưng còn lấy được, nó KHÔNG cho hiệu năng phát hiện

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Module này xếp đặc trưng mạng thành mấy nhóm theo khả năng lấy được dưới mã hoá? Nhập số nhóm.

*Module {{s125}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s051}} | nhóm | module {{s125}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Bản TLS nào mã hoá phần sau của bắt tay, gồm cả chuỗi chứng chỉ của máy chủ, nên nhóm siêu dữ liệu bắt tay rút về còn SNI với dấu tay thư viện? Nhập số bản, dùng dấu phẩy thập phân.

*Module {{s125}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s046}} |  | module {{s125}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mô hình dùng {{s006}} đặc trưng tải tin, {{s077}} đặc trưng siêu dữ liệu bắt tay và {{s126}} đặc trưng hình dáng luồng, coi nhóm hình dáng luồng lấy được đủ. Mạng đích có {{s034}} lưu lượng mã hoá, và trong phần mã hoá thì {{s128}} bật ECH. Kỳ vọng số đặc trưng còn lấy được mỗi luồng là bao nhiêu?

f1 = {{s006}}, f2 = {{s077}}, f3 = {{s126}}, enc = {{s063}}, ech = {{s127}}

## Đáp
@phut: 1
@che-do: so

`f1⋆(1-enc) + f2⋆(1-enc⋆ech) + f3`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s129}} đặc trưng mỗi luồng, trên {{s130}} đặc trưng mô hình khai dùng, tức mất {{s131}}. Để ý cấu trúc của con số: nhóm tải tin đóng góp đúng {{s015}} trên {{s006}} đặc trưng nó khai, nhóm bắt tay còn {{s132}} trên {{s077}}, còn {{s126}} đặc trưng hình dáng luồng đi qua nguyên vẹn. Nói cách khác, {{s133}} trên {{s134}} đặc trưng bị mất nằm ở một nhóm duy nhất, nên bảng ablation theo nhóm là cách duy nhất để thấy chuyện đó.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Một bộ phát hiện chỉ dùng hai nhóm đầu, tức tải tin và SNI. Mạng đích có {{s034}} lưu lượng mã hoá, và {{s084}} phần mã hoá bật ECH. Trên bao nhiêu phần trăm luồng nó còn có ít nhất một đặc trưng để tính?

enc = {{s063}}, ech = {{s083}}

## Đáp
@phut: 1
@che-do: so

`100⋆(1 - enc⋆ech)`

Khoảng {{s135}}. Dẫn lại cho chắc: tải tin lấy được trên {{s030}} luồng, SNI lấy được trên {{s136}} luồng, và tập luồng có tải tin nằm trong tập luồng có SNI, nên hợp của hai nhóm đúng bằng {{s136}}. Trên {{s137}} luồng còn lại, vector đặc trưng của bộ phát hiện này rỗng: nó không chạy chậm hơn, nó không chạy được.

## Đáp (tiếp)
@phut: 1
@che-do: so

Đây là loại con số phải nằm trong phần đánh giá, vì nó là trần cứng mà không kiến trúc nào vượt qua.

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
