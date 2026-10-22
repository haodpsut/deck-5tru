---
tieu-de: Phép đo, và chi phí vận hành của phép đo
phu-de: Trụ 1 NID · module 1.3
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 48.5
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
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Ở mức FPR tôi đang báo, bộ phát hiện của tôi sinh bao nhiêu cảnh báo sai mỗi ngày, và SOC có đủ người đọc không?

## Phép đo nào khai được, phép đo nào không
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này chỉ có một việc: tách **đại lượng bất biến với tỉ lệ nền (base rate)** ra khỏi **đại lượng phụ thuộc tỉ lệ nền**. TPR và FPR thuộc nhóm đầu, nên khai được mà không cần nói gì thêm. Precision, F1, accuracy, MCC thuộc nhóm sau, nên khai một mình là không khai được.

## Phép đo nào khai được, phép đo nào không (tiếp)
@phut: 1
@che-do: noi

Hệ quả thực tế rất gọn: bảng kết quả của anh phải có TPR và FPR, còn precision thì phải đi kèm tỉ lệ nền dùng để tính nó.

## Đường cơ sở của đường PR
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Đường cơ sở của đường PR · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một bộ phân loại ngẫu nhiên có `precision = p` ở **mọi** mức recall, nên đường cơ sở (baseline) của đường PR chính là tỉ lệ nền.

Hệ quả phải nhớ: **AUPRC không đọc được nếu không biết p**, trong khi AUROC thì luôn có đường cơ sở {{s002}} bất kể p. Đó cũng là lý do AUPRC trung thực hơn trên dữ liệu lệch nặng, nhưng chỉ khi báo kèm p.

## Ngân sách cảnh báo
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Ngân sách cảnh báo · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Số cảnh báo mà đội vận hành thật sự đọc được trong một ngày. Đây là ràng buộc cứng, do con người chứ không do mô hình.

Cách dùng: lấy ngân sách cảnh báo (alert budget) chia cho lưu lượng để ra **FPR tối đa được phép**, rồi mới đi chọn mô hình. Làm theo chiều này thì phần đánh giá của bài báo có một con số bắt buộc để so; làm chiều ngược lại thì chỉ còn nhận xét.

## Bốn phép đo, và cái nào phụ thuộc tỉ lệ nền
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`TPR = TP/(TP+FN) FPR = FP/(FP+TN) Precision = TP/(TP+FP) cảnh báo sai mỗi ngày = FPR × N_lành`

**Giả thiết nó đứng trên:**

- TPR và FPR tính trong từng lớp, nên không phụ thuộc tỉ lệ nền
- Precision trộn hai lớp, nên đổi tỉ lệ nền là đổi giá trị
- N_lành là số sự kiện lành thật sự đi qua bộ phát hiện trong một ngày

## Bốn phép đo, và cái nào phụ thuộc tỉ lệ nền · ghi chú
@phut: 1
@che-do: noi

Hệ số Matthews: `MCC = (TP·TN − FP·FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))`. MCC an toàn hơn F1 khi lớp lệch, nhưng vẫn **phụ thuộc tỉ lệ nền**, nên vẫn phải khai p.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s004}} | cảnh báo mỗi ngày | FPR = 10⁻³ trên {{s005}} triệu sự kiện lành mỗi ngày. Bao
!so {{s006}} | số mũ âm | Ngân sách cảnh báo là {{s005}} mỗi ngày
!so {{s007}} | % | Đường cơ sở của đường PR khi tỉ lệ nền p =

## Một bảng kết quả khai TP=97
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bảng kết quả khai TP=97, FN=3, FP=2, TN=98. MCC bằng bao nhiêu?

tp = {{s008}}, fn = {{s009}}, fp = {{s003}}, tn = {{s010}}

## Một bảng kết quả khai TP=97 · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(tp⋆tn - fp⋆fn) / Math.sqrt((tp+fp)⋆(tp+fn)⋆(tn+fp)⋆(tn+fn))`

Khoảng {{s011}}. Để ý ma trận này có TN chỉ {{s010}}, tức tập kiểm tra gần cân bằng. Cùng mô hình đó chạy ở p = 10⁻⁵ thì MCC tụt sâu, vì MCC phụ thuộc tỉ lệ nền.

## SOC có 3 người
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

SOC có {{s009}} người, mỗi người đọc {{s012}} cảnh báo một ngày. Lưu lượng {{s014}} triệu sự kiện lành mỗi ngày. FPR tối đa được phép là bao nhiêu phần triệu (ppm) (nhập số)?

nguoi = {{s009}}, moiNguoi = {{s012}}, nLanh = {{s013}}

## SOC có 3 người · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`1e6 × nguoi × moiNguoi / nLanh`

Khoảng {{s015}} phần triệu, tức {{s015}} × 10⁻⁶. Con số này thấp hơn FPR của gần như mọi bài báo IDS từ hai tới bốn bậc, và đó chính là lý do thực tế mà hệ thống phát hiện phải tổng hợp cảnh báo thay vì báo từng luồng (flow).

## Mô hình và ngưỡng giữ nguyên
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình và ngưỡng giữ nguyên, chuyển từ tập kiểm tra cân bằng sang lưu lượng thật. Đại lượng nào KHÔNG đổi?

- Accuracy và MCC
- Số cảnh báo đúng mỗi ngày
- Precision và F1
- TPR và FPR

## Mô hình và ngưỡng giữ nguyên · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**TPR và FPR**

TPR và FPR là xác suất có điều kiện trong từng lớp. Precision, F1, accuracy, MCC đều trộn hai lớp nên đổi theo tỉ lệ nền. Số cảnh báo mỗi ngày thì đổi theo cả lưu lượng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Khi nào AUPRC đáng tin hơn AUROC để so hai bộ phát hiện?

- Khi lớp lệch nặng VÀ hai bộ được đo ở cùng một tỉ lệ nền
- Khi tập kiểm tra đã được cân bằng
- Khi chỉ quan tâm tới recall
- Luôn luôn, vì AUPRC khó đạt hơn

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khi lớp lệch nặng VÀ hai bộ được đo ở cùng một tỉ lệ nền**

AUPRC phản ánh đúng chi phí cảnh báo sai khi lớp lệch, nhưng đường cơ sở của nó chính là tỉ lệ nền, nên so hai bộ ở hai tỉ lệ nền khác nhau là so hai thước đo khác nhau.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo báo FPR {{s016}} và nói con số đó cho thấy hệ dùng được. Thiếu đúng một dữ kiện để kiểm câu đó. Dữ kiện nào?

- Thời gian huấn luyện
- Số đặc trưng đầu vào
- Kiến trúc mô hình
- Số sự kiện lành mỗi ngày của mạng đích

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Số sự kiện lành mỗi ngày của mạng đích**

FPR là tỉ lệ, còn ngân sách của con người là số tuyệt đối. Không có lưu lượng thì không chuyển được tỉ lệ thành số cảnh báo mỗi ngày, nên câu kết luận không kiểm được.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bảng kết quả sau có một dòng làm cả bảng không chuyển được sang vận hành. Bấm vào dòng đó.

- TPR: {{s017}}
- FPR: {{s018}}
- F1: {{s019}}
- Tỉ lệ nền của tập đánh giá: không khai

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Tỉ lệ nền của tập đánh giá: không khai**

TPR và FPR khai được mà không cần p. F1 thì không: nó trộn hai lớp. Dòng này bỏ trống nên F1 {{s019}} là con số không kiểm được và không so được với bài khác. Cách sửa rẻ nhất là khai p của tập đánh giá; cách sửa tốt hơn là bỏ F1 và báo precision ở vài giá trị p thật.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau có một chỗ làm phần so sánh mất hiệu lực. Bấm vào chỗ đó.

- Chúng tôi chọn ngưỡng tối đa hoá F1 trên tập kiểm tra,
- rồi báo TPR và FPR tại ngưỡng đó,
- và so với baseline ở ngưỡng mặc định {{s002}} của baseline.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và so với baseline ở ngưỡng mặc định {{s002}} của baseline.**

Hai bên được chọn ngưỡng theo hai cách khác nhau, nên đây là so mô hình đã tinh chỉnh với baseline để mặc định. Hai mệnh đề đầu đều hợp lệ nếu khai rõ. Cách sửa: chọn ngưỡng cho cả hai bên theo cùng một tiêu chí, hoặc so trên cả đường cong thay vì tại một điểm.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt B = số cảnh báo đội vận hành đọc được mỗi ngày
- Số cảnh báo sai mỗi ngày ≈ FPR × N_lành, vì N_lành ≫ số tấn công
- Đòi FPR × N_lành ≤ B
- FPR ≤ B / N_lành

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: TPR {{s020}} · FPR 10⁻³ · precision {{s021}} · {{s022}} cảnh báo sai mỗi ngày

- **Tỉ lệ nền lúc kiểm giống lúc chạy thật** tắt đi: Tập kiểm tra cân bằng hoặc lấy mẫu lại, nên p lúc đo khác p lúc chạy.
- **Một ngưỡng duy nhất, cố định** tắt đi: Ngưỡng thích ứng theo tải hoặc theo giờ, nên TPR và FPR là hàm của trạng thái hệ thống.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mỗi cảnh báo được một người xem** tắt đi: Có tầng tổng hợp hoặc xếp hạng ở giữa, nên đơn vị cảnh báo mà người đọc khác đơn vị mà mô hình sinh.

## Tuyên bố này đứng hay đổ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình đạt AUROC {{s023}}, nên ở mức báo động sai {{s024}} nó bắt được khoảng {{s025}} tấn công.

## Tuyên bố này đứng hay đổ · đáp
@phut: 1.5
@che-do: noi

**ĐỔ**

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

ĐỔ. AUROC là xác suất một mẫu tấn công được xếp trên một mẫu lành, lấy trung bình trên MỌI ngưỡng, nên nó không khoá điểm làm việc nào. Phản ví dụ dựng được bằng tay: một đường ROC nằm sát trục hoành tới FPR {{s024}} rồi dựng đứng lên TPR {{s001}} có diện tích khoảng {{s026}}, lớn hơn {{s023}}, trong khi TPR tại FPR {{s024}} bằng {{s027}}. Nên AUROC {{s023}} tương thích với việc bắt được KHÔNG phần trăm ở đúng ngưỡng đó.

## Tuyên bố này đứng hay đổ · đáp (tiếp)
@phut: 1
@che-do: noi

Con số phải báo là TPR tại một FPR cố định.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Một mô hình duy nhất, một họ ROC duy nhất. Kéo ngưỡng và xem hai câu chuyện khác nhau: đường ROC vẫn đẹp trong khi precision tụt sàn.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.3` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table IV reports F1 and accuracy only. Since the evaluation set is resampled, these quantities depend on the class prior and do not transfer to the deployment setting described in Section II. Please report prior-independent metrics and state the alert volume implied by your operating point.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have separated resampling (training only, Section IV-B) from reporting. Table IV now leads with TPR and FPR, which are invariant to the class prior, and tabulates precision at p in {1e-3, 1e-4, 1e-5}. At our operating point (FPR 1e-3) and the traffic volume of Section II (1e7 benign flows per day), the system produces about {{s028}} false alerts per day, which exceeds a three-analyst budget by roughly {{s029}} times. We therefore also state the design requirement in the inverse direction:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

a 180-alert daily budget at this volume requires FPR below 1.8e-5. Section V-E reports the window-level aggregation that closes this gap and its own measured cost.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: nói rằng F1 là thước đo phổ biến trong lĩnh vực. Đúng về thực hành, không trả lời được phản bác.
- Mức {{s003}}: thêm precision và recall nhưng vẫn đo trên tập đã lấy mẫu lại.
- Mức {{s009}}: báo TPR và FPR làm thước đo chính, cộng precision ở vài giá trị tỉ lệ nền thật, cộng số cảnh báo mỗi ngày tại điểm làm việc.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.3` bấm thẻ.
