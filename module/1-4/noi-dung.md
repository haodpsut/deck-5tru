---
tieu-de: Base-rate fallacy
phu-de: Trụ 1 NID · module 1.4
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 50
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

Với tỉ lệ tấn công thật trong mạng của tôi, FPR của tôi phải nhỏ tới đâu để một cảnh báo có nghĩa, và con số đó có khả thi không?

## Vì sao module này đứng đầu trụ
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Đây là module duy nhất trong trụ {{s001}} mà một công thức ba dòng đủ sức bác một bảng kết quả đẹp. Mọi bài IDS đều phải đi qua nó, và phần lớn câu hỏi phản biện dạng *practical deployability* là phiên bản lịch sự của nó.

## Vì sao module này đứng đầu trụ (tiếp)
@phut: 1
@che-do: noi

Mục tiêu không phải nhớ công thức. Mục tiêu là **dùng được nó trong {{s002}} giây trên giấy**, giữa một buổi phản biện, để biết con số của đối phương hay của chính mình có nghĩa hay không.

## Tỉ lệ nền (base rate, prevalence)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Tỉ lệ nền (base rate, prevalence) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Tỉ lệ sự kiện tấn công trên tổng số sự kiện quan sát, **tại thời điểm chạy thật**, ký hiệu `p`.

Điểm phải nhớ: **ROC không nhìn thấy nó.** TPR và FPR đều là xác suất có điều kiện trong từng lớp, nên đổi `p` thì cả hai không đổi, trong khi precision, F1 và số cảnh báo mỗi ngày đổi hết. Đó là lý do một đường ROC đẹp không chứng minh gì về vận hành.

## PPV, cũng chính là precision
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## PPV, cũng chính là precision · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`PPV = P(có tấn công | máy báo động)`. Đây là đại lượng mà nhà phân tích SOC thật sự trải nghiệm: trong {{s003}} lần máy kêu, bao nhiêu lần có chuyện.

## PPV, cũng chính là precision · đáp (tiếp)
@phut: 1
@che-do: noi

Phân biệt cho chặt: **TPR trả lời câu hỏi của nhà nghiên cứu** (máy có bắt được tấn công không), còn **PPV trả lời câu hỏi của người vận hành** (tôi có nên tin tiếng kêu này không). Hai câu hỏi khác nhau, và chỉ câu thứ hai quyết định hệ thống có được triển khai.

## Bayes cho giá trị dự đoán dương
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`PPV = (TPR · p) / (TPR · p + FPR · ({{s001}} − p))`

**Giả thiết nó đứng trên:**

- p là tỉ lệ nền (base rate) tại thời điểm chạy, không phải tỉ lệ trong tập kiểm tra
- các sự kiện độc lập với nhau
- một ngưỡng quyết định duy nhất, cố định

## Bayes cho giá trị dự đoán dương · ghi chú
@phut: 1
@che-do: noi

Đảo ngược để lấy yêu cầu thiết kế: `FPR ≤ TPR · p · ({{s001}} − PPV⋆) / (PPV⋆ · ({{s001}} − p))`. Đây là dạng dùng được nhất, vì nó cho ra **một con số bắt buộc** chứ không phải một nhận xét.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s004}} | % | Với p = 10⁻⁵
!so {{s005}} | số mũ âm | Vẫn p = 10⁻⁵ và TPR = {{s001}}. Muốn PPV đạt {{s006}}
!so {{s007}} | cảnh báo mỗi ngày | FPR = 10⁻³ trên {{s008}} triệu luồng (flow) lành mỗi ngày. Bao nhiêu

## Một bài báo khai p = 10⁻³
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai p = 10⁻³, TPR = {{s012}}, FPR = {{s013}}. PPV bằng bao nhiêu phần trăm?

p = {{s009}}, tpr = {{s010}}, fpr = {{s011}}

## Một bài báo khai p = 10⁻³ · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s003}} × tpr × p / (tpr × p + fpr × ({{s001}} - p))`

Kết quả khoảng {{s014}}. FPR {{s015}} nghe nhỏ, nhưng nó lớn hơn tỉ lệ nền {{s016}} lần, nên hơn {{s017}} cảnh báo là sai.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Muốn PPV đạt {{s020}} với p = 10⁻⁴ và TPR = {{s021}} thì FPR tối đa là bao nhiêu? Nhập dưới dạng phần triệu (ppm).

p = {{s018}}, tpr = {{s019}}, ppv = {{s019}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`1e6 × tpr × p × ({{s001}} - ppv) / (ppv × ({{s001}} - p))`

Khoảng {{s008}} phần triệu. Đây là con số nên nhớ dạng bậc: muốn tin được cảnh báo thì FPR phải xuống vùng phần triệu, không phải vùng phần trăm.

## Một hệ đạt FPR = 10⁻⁶ với TPR = 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một hệ đạt FPR = 10⁻⁶ với TPR = {{s001}}, chạy ở p = 10⁻⁵. PPV bằng bao nhiêu phần trăm?

p = {{s022}}, tpr = {{s001}}, fpr = {{s023}}

## Một hệ đạt FPR = 10⁻⁶ với TPR = 1 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s003}} × tpr × p / (tpr × p + fpr × ({{s001}} - p))`

Khoảng {{s024}}. Chỉ khi FPR tụt xuống dưới p một bậc thì cảnh báo mới đáng tin, và đây là lý do kỹ thuật thật của việc tổng hợp nhiều tín hiệu yếu thành một cảnh báo mạnh.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình A có TPR = {{s027}} và FPR = {{s028}}. Triển khai vào mạng có p = 10⁻⁴. Trong {{s003}} cảnh báo, khoảng bao nhiêu cảnh báo là đúng?

- Khoảng {{s001}}
- Khoảng {{s025}}
- Khoảng {{s026}}
- Khoảng {{s008}}

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khoảng {{s001}}**

PPV = 0,99·10⁻⁴ / (0,99·10⁻⁴ + 0,01·0,9999) ≈ {{s029}}, tức khoảng {{s001}} trên {{s003}}. FPR {{s030}} nghe rất nhỏ nhưng lớn hơn p tới {{s003}} lần.

## Đại lượng nào KHÔNG đổi khi tỉ lệ nền p đổi
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Đại lượng nào KHÔNG đổi khi tỉ lệ nền p đổi, trong khi mô hình và ngưỡng giữ nguyên?

- Số cảnh báo đúng mỗi ngày
- Precision
- F1
- AUROC

## Đại lượng nào KHÔNG đổi khi tỉ lệ nền p đổi · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**AUROC**

AUROC chỉ phụ thuộc thứ tự điểm trong từng lớp nên bất biến với p. Chính tính chất đó làm AUROC trở thành con số dễ gây hiểu nhầm nhất khi báo một mình: nó đẹp như nhau ở mọi tỉ lệ nền.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn abstract dưới đây có đúng một chỗ không khai được từ số đã cho. Bấm vào chỗ đó.

- Our detector achieves {{s031}} accuracy
- and a false positive rate of {{s032}} on CIC-IDS2017,
- demonstrating practical deployability for enterprise networks.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**demonstrating practical deployability for enterprise networks.**

Hai mệnh đề đầu là số đo, khai được. Mệnh đề thứ ba là một suy luận cần thêm tỉ lệ nền, mà abstract không có. Với FPR {{s033}} trên {{s008}} triệu luồng lành mỗi ngày thì đó là {{s034}} cảnh báo sai mỗi ngày, tức ngược hẳn với kết luận. Đây là lớp lỗi câu văn quanh con số sai trong khi con số đúng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bảng kết quả sau có một dòng làm ba dòng trên mất giá trị vận hành. Bấm vào dòng đó.

- Accuracy: {{s035}}
- Precision: {{s036}}
- Recall: {{s037}}
- Tập kiểm tra: {{s006}} tấn công, {{s006}} lành

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Tập kiểm tra: {{s006}} tấn công, {{s006}} lành**

Precision {{s038}} được đo ở p = {{s039}}. Chuyển sang p = 10⁻⁵ thì precision tụt về bậc {{s040}} trong khi recall giữ nguyên. Dòng này không sai, nhưng nó làm hai dòng precision và accuracy không chuyển được sang vận hành. Cách sửa: báo thêm precision ở tỉ lệ nền thật, hoặc báo FPR thay cho precision.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- P(T | C) = P(C | T) · P(T) / P(C)
- P(C | T) = TPR và P(T) = p
- P(C) = P(C | T) · P(T) + P(C | ¬T) · P(¬T)
- P(C | ¬T) = FPR và P(¬T) = {{s001}} − p
- PPV = (TPR · p) / (TPR · p + FPR · ({{s001}} − p))

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: PPV ≈ {{s041}} với p = 10⁻⁵, TPR = {{s012}}, FPR = 10⁻³

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Sự kiện độc lập với nhau** tắt đi: Tấn công đến theo chùm, nên p cục bộ trong một cửa sổ cao hơn p toàn cục nhiều bậc. PPV trong chùm tốt hơn hẳn, PPV ngoài chùm tệ hơn hẳn.
- **Một ngưỡng quyết định duy nhất** tắt đi: Với ngưỡng thích ứng theo tải hoặc theo ngữ cảnh, TPR và FPR là hàm của trạng thái hệ thống.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **p đo được và biết trước** tắt đi: Không ai biết tỉ lệ tấn công thật của mạng đích, vì biết nó tức là đã phát hiện xong.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Kéo bốn tham số và đọc cùng lúc bốn đầu ra. Hai con số bên phải là thứ quyết định hệ thống có được triển khai, không phải TPR.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.4` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The authors report a false positive rate of {{s044}} as evidence of practical applicability. At the traffic volumes described in Section V, this corresponds to several thousand false alerts per day. Please justify the operational feasibility of the proposed system, or revise the claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree and have revised the claim. At {{s008}} million benign flows per day, an FPR of {{s044}} yields {{s045}} false alerts per day, and at a base rate of 1e-5 the resulting PPV is {{s046}}. We now report PPV across a range of base rates (Table VI) rather than accuracy alone, and we state the design requirement explicitly: reaching PPV {{s006}} at p = 1e-5 requires FPR below 1e-5.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Section V-D adds window-level alert aggregation, which reduces analyst-facing alerts by a factor of X while retaining Y% of true detections. The abstract no longer claims practical deployability from FPR alone.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: bảo vệ con số FPR và nói nó thấp so với các công trình liên quan. Không trả lời đúng câu hỏi.
- Mức {{s042}}: thừa nhận số cảnh báo, hứa công việc tương lai. Reviewer sẽ giữ nguyên ý kiến.
- Mức {{s043}}: tính ra số cảnh báo sai mỗi ngày, báo thêm PPV ở tỉ lệ nền thật, và sửa câu tuyên bố trong abstract.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Accuracy and precision are reported on a balanced test set (Table III), which does not reflect the class prior of real network traffic. The reported precision therefore does not transfer to deployment. Please re-evaluate under realistic priors.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have separated training-time balancing from evaluation-time reporting. Class balancing remains in training (Section IV-B) and is now explicitly scoped there. Evaluation is reported on the original class distribution, using TPR and FPR as primary metrics because they are invariant to the class prior, with precision tabulated at p in {1e-3, 1e-4, 1e-5} (Table VI). Accuracy has been removed from the abstract.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: nói rằng cân bằng tập kiểm tra là thực hành phổ biến. Đúng về thực hành, không trả lời được phản bác.
- Mức {{s042}}: chạy lại trên tập không cân bằng nhưng vẫn báo accuracy làm số chính.
- Mức {{s043}}: báo lại bằng FPR và TPR (hai đại lượng bất biến với p), cộng precision tính ở vài giá trị p thật.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.4` bấm thẻ.
