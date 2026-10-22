---
tieu-de: Phòng hỏi đáp *hội thảo*
phu-de: Trả lời NÓI, trong hai mươi tới sáu mươi giây, không có gì để trốn
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 75
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: HỎI ĐÁP
@phut: 0.5
@che-do: noi
@notes: Mở cửa sổ người nói, bấm p. Đồng hồ là phần chính của deck này.

## Luật của phòng này
@phut: 1.5
@che-do: noi
@notes: Đọc luật rồi bắt đầu. Không tua lại thẻ đã làm hỏng.

{{TAKE_HOME}}

Khác Phòng phản biện ở chỗ cốt yếu: phản biện là trả lời VIẾT, có thời gian, tra được bảng. Đây là trả lời NÓI, trong {{s001}} tới {{s002}} giây, không có gì để trốn. Luật nhà: ⛔ không lấy nội dung từ bài đang under review. Mọi câu dưới đây dựng từ nội dung {{s003}} trụ và từ các bài đã có kết luận.

## Người hỏi: chuyên gia đối đầu
@phan: NID
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You report {{s004}} accuracy. What is the false positive rate at that operating point, and how many alerts per day does it produce at the traffic volume you described?

*Trụ NID. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu hỏi nhận chìm anh bằng chính con số anh tự hào. Bẫy là nó mời anh bảo vệ accuracy, trong khi người hỏi đã biết accuracy vô nghĩa ở tỉ lệ nền thật và đang chờ xem anh có biết điều đó không.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói thẳng rằng accuracy không phải con số đúng để đánh giá, trước khi ai kịp hỏi thêm.
- Cho FPR và số cảnh báo mỗi ngày, ví dụ FPR 10⁻³ trên {{s006}} triệu luồng lành là {{s007}} cảnh báo sai mỗi ngày.
- Tự khai rằng con số đó vượt ngân sách của một SOC, và nói cơ chế nào trong bài xử lý chuyện đó.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "nhưng accuracy của chúng tôi cao hơn các công trình trước". Nó xác nhận rằng anh vẫn đang nghĩ bằng accuracy, và người hỏi sẽ hỏi tiếp bằng tỉ lệ nền.

## Người hỏi: người ngoài ngành
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Why not just use a firewall for this?

*Trụ NID. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy không phải câu hỏi, bẫy là phản xạ của anh. Câu này nghe ngây thơ nên dễ trả lời bằng giọng hạ cố, và cả phòng sẽ thấy. Người hỏi thường là người sẽ bỏ phiếu cho anh ở một hội đồng khác.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận rằng tường lửa làm đúng một việc và làm tốt: chặn theo luật đã biết.
- Cho một con số về phần còn lại, ví dụ tỉ lệ tấn công không có luật sẵn hoặc đã mã hoá.
- Nói giới hạn của chính mình: hệ của anh không thay tường lửa, nó xếp hạng cái tường lửa cho đi qua.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "tường lửa chỉ xem cổng và địa chỉ IP thôi" bằng giọng giải thích cho người mới. Tường lửa hiện đại làm nhiều hơn thế, và câu đó vừa sai vừa làm anh mất phòng.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your evaluation uses CIC-IDS2017. That capture predates widespread TLS {{s009}}, QUIC and encrypted client hello. Do the features your model relies on still exist in a {{s010}} network?

*Trụ NID. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi đã đọc phần đặc trưng của anh. Bẫy là trả lời về TUỔI của dataset, trong khi câu hỏi thật là về NHÓM ĐẶC TRƯNG nào còn lấy được. Nói "chúng tôi sẽ dùng dataset mới hơn" là trả lời sai câu.

## Khung trả lời
@phut: 0.5
@che-do: so

- Phân nhóm đặc trưng ngay: tải tin, siêu dữ liệu bắt tay, hình dáng luồng.
- Cho con số: bao nhiêu đặc trưng của anh thuộc nhóm còn sống.
- Tự khai nhóm nào chết và kết quả nào trong bài phụ thuộc nhóm đó.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "công việc tương lai của chúng tôi là thu dataset mới". Nó biến một câu hỏi về tính hợp lệ thành một lời hứa, và người hỏi sẽ ghi lại đúng chỗ đó.

## Người hỏi: chuyên gia đối đầu
@phan: FL
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Why do you need federated learning at all? You could pool the data at one site and train a stronger model.

*Trụ FL. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu hỏi kinh điển nhất của mọi bài FL, và nó mời anh trả lời bằng chữ: riêng tư, pháp lý, bảo mật. Trả lời bằng chữ là mất điểm. Nó phải có SỐ, hoặc một điều khoản cụ thể.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói thẳng lý do nào trong ba lý do là lý do thật của anh: pháp lý, khối lượng, hay độ nhạy.
- Cho tỉ số byte, ví dụ gom hết là {{s007}} GB một ngày so với {{s008}} GB nếu truyền mô hình, tức {{s011}} lần.
- Tự khai vùng mà gom lại RẺ HƠN, vì tỉ số đó đảo chiều khi lưu lượng mỗi site nhỏ hơn hai lần kích thước mô hình.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "vì quy định không cho phép chia sẻ dữ liệu" mà không nêu được điều khoản nào. Người hỏi sẽ hỏi điều khoản, và anh không có.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You report epsilon equals eight. The classical Gaussian mechanism bound only holds for epsilon below one. Which accountant did you use, and what is your sampling assumption?

*Trụ FL. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Đây là câu hỏi của người đã làm DP thật. Bẫy là nó có hai phần, và trả lời một phần sẽ bị hỏi lại ngay. Phần thứ hai, giả thiết lấy mẫu, là chỗ phần lớn bài DP-FL hở.

## Khung trả lời
@phut: 0.5
@che-do: so

- Trả lời tên bộ kế toán ngay, đừng vòng.
- Cho tham số: noise multiplier, clip norm, sampling rate, số vòng, và delta.
- Tự khai giả thiết lấy mẫu và nói nếu cài đặt dùng shuffling thì con số epsilon không còn là bảo đảm.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "epsilon bằng tám là mức thường dùng trong tài liệu". Đó là lời kêu gọi theo số đông cho một đại lượng có định nghĩa chính xác, và người hỏi biết điều đó.

## Người hỏi: chủ toạ ép thời gian
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

We are out of time. In one sentence, what is the contribution?

*Trụ FL. Khung trả lời {{s012}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là anh có một bài dài và muốn nói ba đóng góp. Chủ toạ cho anh một câu, và nếu anh dùng hai câu thì câu thứ hai không ai nghe. Đây là bài tập nén, không phải bài tập nội dung.

## Khung trả lời
@phut: 0.5
@che-do: so

- Một câu duy nhất, có động từ, nói anh ĐO được cái gì mà trước đó chưa ai đo.
- Một con số trong chính câu đó.
- Không khai giới hạn ở đây. Giới hạn dành cho câu hỏi tiếp, không dành cho {{s001}} giây này.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "chúng tôi có ba đóng góp". Chủ toạ vừa nói hết giờ, và câu đó báo rằng anh không nghe.

## Người hỏi: người biết đúng điểm yếu
@phan: NTN
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your handover rate assumes one beam per satellite. Operational constellations use dozens of beams per satellite. Does your result survive that change?

*Trụ NTN. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi biết hình học. Bẫy là trả lời "chúng tôi sẽ mở rộng", trong khi con số thật đổi theo một hệ số đơn giản và anh nên biết hệ số đó ngay tại chỗ.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói hướng đổi trước khi nói độ lớn: nhiều chùm thì tần suất chuyển giao TĂNG, không giảm.
- Cho con số: cửa sổ nhìn thấy {{s013}} phút cho chặn dưới {{s014}} lần mỗi giờ với một chùm, và khoảng {{s002}} lần với tám chùm.
- Tự khai rằng kết luận định tính sống sót nhưng con số tuyệt đối thì không, và chỉ ra chỗ nào trong bài phụ thuộc con số tuyệt đối.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "số chùm không ảnh hưởng kết quả của chúng tôi". Nó ảnh hưởng, và người hỏi biết nó ảnh hưởng theo hướng nào.

## Người hỏi: người ngoài ngành
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Is this not already solved? Commercial satellite internet seems to work.

*Trụ NTN. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là trả lời bằng cách hạ thấp hệ thống thương mại, hoặc bằng cách nói bài của anh khác mà không nói khác ở đâu. Cả hai đều nghe như biện hộ.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận rằng nó hoạt động, và nói rõ nó hoạt động cho trường hợp nào.
- Cho con số phân biệt trường hợp của anh, ví dụ thiết bị không có nguồn liên tục, hoặc liên kết chỉ nhìn thấy {{s015}} phút một lượt.
- Tự khai rằng nếu điều kiện của anh không xảy ra trong thực tế thì bài của anh mất lý do tồn tại.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "hệ thống thương mại không công bố chi tiết nên không so được". Nó nghe như tránh câu hỏi.

## Người hỏi: chuyên gia đối đầu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your UAV energy model is linear in distance flown. In that model hovering is free. Is that not the whole difficulty of the problem?

*Trụ NTN. Khung trả lời {{s016}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi vừa chỉ ra rằng mô hình của anh bỏ mất chính cơ chế đắt nhất. Bẫy là chống đỡ. Câu trả lời đúng bắt đầu bằng việc nhận, và đi kèm con số cho thấy anh ĐÃ đo độ lệch.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận ngay rằng mô hình tuyến tính coi treo một chỗ là miễn phí, và đó là sai cơ chế.
- Cho con số độ lệch: mô hình phi tuyến cho khoảng {{s017}} kJ trên cùng một quỹ đạo, tuyến tính cho khoảng {{s018}} kJ, lệch gần một nửa.
- Tự khai hệ quả nặng hơn: nghiệm quỹ đạo tối ưu của hai mô hình khác nhau về bản chất, không chỉ khác con số.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "mô hình tuyến tính là một xấp xỉ hợp lý trong tài liệu". Nó biến một lỗi cơ chế thành một lựa chọn phong cách, và người hỏi sẽ không chấp nhận.

## Người hỏi: chuyên gia đối đầu
@phan: 6G SEC
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your threat model gives the attacker read access to the E2 interface but not write access. Why is that the right split, and what breaks if you give write access too?

*Trụ 6G Sec. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là câu hỏi nghe như đòi biện minh một lựa chọn, nhưng thật ra nó kiểm xem anh có biết kết quả nào của mình phụ thuộc lựa chọn đó. Nếu anh không biết, cả phòng sẽ thấy.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói lý do chọn bằng một tính chất của hệ, không bằng sự tiện lợi.
- Cho con số hoặc một danh sách: bao nhiêu phát hiện trong bài còn đứng khi cho thêm quyền ghi.
- Tự khai rằng với quyền ghi thì phòng vệ dựa biên giới mạng mất hiệu lực, không phải yếu đi.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "chúng tôi chọn mô hình chỉ đọc để bài toán đơn giản hơn". Đó là lý do của tác giả, không phải lý do của hệ thống.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You claim the slices are isolated, but the radio scheduler is shared. Did you measure the correlation between slice A load and slice B latency?

*Trụ 6G Sec. Khung trả lời {{s016}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

Người hỏi đã biết chỗ hở của mọi tuyên bố cô lập. Bẫy là trả lời "có, chúng tôi cô lập" mà không nói cô lập ở TẦNG NÀO, và người hỏi sẽ đọc lại slide của anh.

## Khung trả lời
@phut: 0.5
@che-do: so

- Tách bốn tầng cô lập ngay, và nói rõ tầng nào anh có và tầng nào dùng chung.
- Cho con số tương quan nếu đã đo, hoặc nói thẳng là chưa đo.
- Tự khai rằng khi bộ lập lịch dùng chung thì cô lập chỉ là cô lập ba tầng, và viết lại tuyên bố cho đúng.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "theo chuẩn thì các slice được cô lập". Chuẩn định nghĩa nhiều mức cô lập, và câu đó chỉ cho người hỏi biết anh chưa đọc mức nào.

## Người hỏi: chuyên gia đối đầu
@phan: PQC
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your hybrid handshake is over {{s019}} bytes on a link whose frames are {{s020}} bytes. That is more than a dozen fragments. Did the handshake actually complete on your testbed, and at what loss rate?

*Trụ PQC. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi đã nhẩm ra số mảnh trước khi hỏi. Bẫy là trả lời về kích thước khoá, trong khi câu hỏi là về XÁC SUẤT HOÀN TẤT, và đó là một đại lượng khác hẳn.

## Khung trả lời
@phut: 0.5
@che-do: so

- Trả lời số mảnh và xác suất hoàn tất ngay, vì đó là điều được hỏi.
- Cho con số: {{s021}} byte với tải khả dụng khoảng {{s022}} byte là {{s023}} mảnh, và với tỉ lệ mất {{s024}} mỗi mảnh thì xác suất hoàn tất khoảng {{s025}}.
- Tự khai mô hình mất gói, vì con số trên giả định mất độc lập và mất theo chùm cho kết quả khác.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "ML-KEM-768 là mức NIST khuyến nghị nên chúng tôi dùng nó". Nó trả lời câu hỏi về lựa chọn thuật toán, trong khi người ta hỏi về xác suất hoàn tất.

## Người hỏi: người ngoài ngành
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Quantum computers that can break RSA do not exist. Why should anyone spend money on this now?

*Trụ PQC. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là tranh luận về việc máy lượng tử bao giờ có, tức đi vào đúng chỗ không ai thắng được. Câu trả lời đúng chuyển trục sang một bất đẳng thức không cần biết ngày.

## Khung trả lời
@phut: 0.5
@che-do: so

- Chuyển trục ngay: vấn đề không phải khi nào có máy, mà là dữ liệu hôm nay giữ mật bao lâu.
- Cho ba con số của bất đẳng thức Mosca: thời gian giữ mật, thời gian di trú, thời gian tới khi có máy.
- Tự khai rằng con số thứ ba là ước lượng, nên kết luận phải viết ở dạng điều kiện.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "các chuyên gia dự đoán khoảng năm {{s026}}". Anh vừa biến câu trả lời của mình thành một con số mà anh không bảo vệ được.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You use a standardised algorithm, but is your implementation constant time, and is it masked?

*Trụ PQC. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là trả lời bằng tên chuẩn. Câu hỏi nằm ở lớp cài đặt, nơi chuẩn không bảo đảm gì, và người hỏi biết chính xác chỗ đó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Tách ba lớp ngay: thuật toán, giao thức, cài đặt. Nói chuẩn bảo đảm lớp nào.
- Cho con số về cài đặt của anh: thư viện nào, bản nào, có che mặt nạ hay không, và nếu có thì chậm bao nhiêu lần.
- Tự khai rằng nếu chưa kiểm thời gian hằng thì kết quả an ninh của bài không nói gì về lớp cài đặt.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "chúng tôi dùng ML-KEM nên nó an toàn". Đó đúng là câu mà câu hỏi được thiết kế để bắt.

## Người hỏi: người hỏi lệch chủ đề
@phan: NID
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Have you considered applying large language models to this problem?

*Trụ NID. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu hỏi không nằm trong bài và người hỏi cũng biết thế. Bẫy là hai cực: chê câu hỏi, hoặc hứa hẹn một thứ anh chưa làm. Cả hai đều mất điểm, và cách ra đúng là từ chối có kèm một tiêu chí.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận câu hỏi trong một câu, không khen không chê.
- Cho một tiêu chí cụ thể để nói vì sao nó không nằm trong bài này, kèm con số nếu có.
- Tự khai điều kiện nào sẽ làm anh đổi ý, để lời từ chối có nội dung.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "đó là công việc tương lai thú vị" rồi dừng. Nó là cách nói không mà nghe như có, và người hỏi sẽ nhớ anh không có tiêu chí nào.

## Người hỏi: chủ toạ ép thời gian
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

We are over time, so thirty seconds only. Is the number your model outputs a probability, yes or no?

*Trụ NID. Khung trả lời {{s012}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Chủ toạ cho anh {{s012}} giây và một câu hỏi có đúng hai đáp án. Bẫy là dùng {{s012}} giây để giải thích rồi bị cắt giữa câu, và cả phòng nghe thấy phần giải thích chứ không nghe thấy câu trả lời. Phải nói có hoặc không TRƯỚC, phần còn lại chỉ nói nếu còn giờ.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói "không" ngay từ chữ đầu tiên, vì đó là đáp án đúng và chủ toạ chỉ cần một chữ.
- Một con số làm chứng: điểm {{s027}} ở tỉ lệ nền 10⁻⁵ tương ứng PPV dưới {{s028}} phần trăm, chứ không phải {{s029}} phần trăm.
- Tự khai đã làm gì: hiệu chuẩn lại trên một tập giữ riêng, và báo đường tin cậy cạnh AUROC.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng mở đầu bằng "câu này hơi phức tạp". Chủ toạ hỏi vì hết giờ, và câu đó tiêu đúng số giây anh còn.

## Người hỏi: người đọc sai kết quả
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your figure shows an AUROC of {{s030}}. So at one percent false positives you detect about {{s031}} percent of attacks, correct?

*Trụ NID. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi đọc sai, và đọc sai theo hướng CÓ LỢI cho anh. Bẫy là gật đầu. Nếu câu đó được để đứng thì nó vào biên bản, rồi một người khác trong phòng sẽ bác, và lúc đó anh là người nói quá. Phải sửa mà không làm người hỏi mất mặt.

## Khung trả lời
@phut: 0.5
@che-do: so

- Sửa ngay nhưng đứng về phía người hỏi: AUROC không khoá điểm làm việc nào cả.
- Con số: một đường ROC nằm sát trục tới FPR {{s028}} phần trăm rồi dựng đứng vẫn cho diện tích {{s032}}, nên AUROC {{s033}} tương thích với việc bắt được {{s034}} phần trăm ở đúng ngưỡng đó.
- Cho con số người hỏi thật sự muốn: TPR tại một FPR cố định, lấy từ bảng điểm làm việc.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "đúng rồi, gần như vậy". Đó là cách một con số sai đi vào biên bản hội thảo dưới tên anh.

## Người hỏi: người đòi được trích dẫn
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Our group published a graph based intrusion detector in {{s035}} on the same dataset with higher reported numbers. Why is it not in your comparison table?

*Trụ NID. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Hai bẫy chồng nhau. Bẫy thứ nhất là xin lỗi và hứa thêm vào, tức nhận rằng bảng của anh thiếu trong khi anh chưa biết nó có so được không. Bẫy thứ hai là chê công trình của họ, và người đó thường đang phản biện anh ở một nơi khác. Đường ra là chốt điều kiện so sánh.

## Khung trả lời
@phut: 0.5
@che-do: so

- Xin tên bài chính xác và nói sẽ đọc, không hứa đưa vào bảng trước khi biết nó so được không.
- Nêu ba điều kiện để hai con số nói về cùng một việc, rồi cho con số của mình ở đúng ba điều kiện đó: cùng phép chia dữ liệu, cùng điểm làm việc, cùng đơn vị báo cáo.
- Tự khai: nếu nó so được và họ cao hơn thì đó là kết quả phải dẫn, và anh sẽ dẫn.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "tôi không biết bài đó" rồi dừng. Nó vừa hạ anh vừa không trả lời, và người hỏi sẽ nhắc lại lúc thảo luận chung.

## Người hỏi: người ngoài ngành
@phan: FL
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

If every hospital keeps its own data and never shares it, how can the model learn anything at all?

*Trụ FL. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu hỏi thật thà và đúng chỗ, nên bẫy nằm ở giọng và ở mức trừu tượng. Dễ trả lời bằng sơ đồ kiến trúc, mà người hỏi không cần kiến trúc: họ cần biết CÁI GÌ đi qua đường truyền. Không nói được cái gì đi qua thì cả phòng sẽ cho rằng dữ liệu vẫn đi qua.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói rõ thứ đi qua đường truyền không phải bệnh án mà là bản cập nhật tham số.
- Cho khối lượng: một mô hình một triệu tham số ở float32 là khoảng {{s036}} MB mỗi client mỗi vòng.
- Tự khai giới hạn: bản cập nhật vẫn rỉ thông tin, nên phải có kế toán riêng tư, không phải chỉ có một lời hứa.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "dữ liệu không bao giờ rời khỏi bệnh viện nên hoàn toàn riêng tư". Câu sau phủ định câu trước, và người biết nghề trong phòng sẽ nhặt đúng chỗ đó.

## Người hỏi: người hỏi lệch chủ đề
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Could blockchain be used here to make the whole process trustworthy?

*Trụ FL. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu lệch, nhưng lệch một cách lịch sự, nên không được gạt. Bẫy là hai cực: gật cho qua rồi bị hỏi tiếp chi tiết không có, hoặc bác thẳng và thành người khó chịu suốt phần còn lại của phiên. Việc cần làm là nói nó giải bài toán NÀO, rồi chỉ ra bài toán của anh không phải bài toán đó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói rõ sổ ghi phân tán giải một bài toán thật: ai gửi cái gì, ghi lại và không sửa được về sau.
- Con số: mỗi vòng của chúng tôi có {{s022}} bản cập nhật, nên sổ phải chốt {{s022}} bản ghi trong một vòng tính bằng giây.
- Tự khai giới hạn của chính sổ đó: nó ghi rất trung thực một bản cập nhật độc hại, nên nó không phải phòng vệ đầu độc.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "blockchain không liên quan gì tới bài này". Nó đóng cửa câu hỏi, và phần sau của phiên anh sẽ nói một mình.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You report one hundred rounds. What fraction of clients actually participated in a typical round, and were the clients you dropped random?

*Trụ FL. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi biết số vòng là con số dễ báo còn tỉ lệ tham gia là con số dễ bỏ qua. Bẫy nằm ở chữ random: nếu anh cắt theo hạn chờ thì client bị cắt là client CHẬM, tức thiên lệch có hệ thống. Trả lời "ngẫu nhiên" là tự khai một điều sai, và họ hỏi vì họ đã biết điều đó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Cho tỉ lệ tham gia trước khi bị hỏi lại, và nói cơ chế chọn client là gì.
- Con số: chọn {{s006}} trên {{s022}} client mỗi vòng thì sau {{s022}} vòng kỳ vọng mỗi client vào {{s006}} lần, nhưng con số thật của client chậm thấp hơn.
- Tự khai rằng cắt theo hạn chờ là thiên lệch có hệ thống chứ không ngẫu nhiên, và nói anh đo nó bằng gì.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "client rơi là ngẫu nhiên nên không ảnh hưởng". Đó là một giả thiết, không phải một phép đo, và người hỏi đang hỏi vì họ biết nó thường sai.

## Người hỏi: chuyên gia đối đầu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

If every client keeps a personalised head, what exactly is being federated, and whose accuracy is the number on your slide?

*Trụ FL. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Hai câu gói làm một, và câu thứ hai là câu giết. Khi mỗi client có đầu riêng thì KHÔNG AI chạy mô hình toàn cục, nên một con số trung bình trên mô hình toàn cục là con số của một mô hình không tồn tại. Bẫy là trả lời câu đầu cho gọn rồi dừng lại.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói rõ phần nào chia chung và phần nào riêng, bằng tên lớp chứ không bằng chữ cá nhân hoá.
- Con số: báo trung bình có trọng số theo số mẫu VÀ phân vị thứ {{s006}}, vì trung bình che được một phần mười client tệ nhất.
- Tự khai rằng mô hình toàn cục không ai chạy, nên con số của nó là chẩn đoán chứ không phải kết quả.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "chúng tôi báo độ chính xác trung bình trên tất cả client" rồi im. Trung bình trên các mô hình khác nhau không phải phép đo của một hệ, nó là một con số không có chủ.

## Người hỏi: người đọc sai kết quả
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You use epsilon equals eight. That means roughly an eight percent chance that a record leaks, does it not?

*Trụ FL. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi gắn epsilon với một xác suất, và cách đọc đó nghe hợp lý nên cả phòng sẽ tin nếu anh không sửa. Bẫy ngược là sửa bằng một định nghĩa dài rồi hết giờ mà chưa cho con số nào. Phải đưa đúng một con số thay thế, và con số đó là e mũ {{s015}}.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói rõ epsilon không phải xác suất, nó chặn một tỉ số khả năng xảy ra.
- Con số thay thế: e mũ {{s015}} bằng {{s037}}, tức một đầu ra có thể trở nên gần ba nghìn lần dễ xảy ra hơn khi đổi một bản ghi.
- Tự khai rằng {{s037}} là một bảo đảm YẾU, và nói vì sao anh vẫn chọn mức đó.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "epsilon bằng {{s015}} là mức thường dùng trong các công trình trước". Nó đổi câu hỏi về Ý NGHĨA thành một lời viện dẫn thói quen, và người hỏi sẽ hỏi lại đúng câu cũ.

## Người hỏi: chủ toạ ép thời gian
@phan: NTN
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

There are two questions left and one minute. Give us the single number that matters most in your work.

*Trụ NTN. Khung trả lời {{s012}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là chọn con số TO nhất thay vì con số RÀNG BUỘC nhất. Chủ toạ đang cho anh chọn thứ cả phòng sẽ nhớ: một con số về hiệu năng của anh thì bị quên sau mười phút, còn một con số về vật lý thì không ai bác được và nó kéo theo cả bài.

## Khung trả lời
@phut: 0.5
@che-do: so

- Chọn một con số của BÀI TOÁN, không phải một con số của phương pháp.
- Cho nó kèm đơn vị và kèm hệ quả: {{s038}} km/s ở cao độ {{s039}} km, nên trong mười giây vệ tinh đi {{s040}} kilômét.
- Nói một câu hệ quả duy nhất, rồi dừng và nhường micro.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng chọn con số cải thiện của riêng mình, kiểu "chúng tôi giảm {{s041}} phần trăm". Không ai kiểm được nó trong một phút, và không ai nhớ nó sau phiên.

## Người hỏi: người hỏi lệch chủ đề
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

What about space debris? Should we be launching thousands of these satellites at all?

*Trụ NTN. Khung trả lời {{s042}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu hỏi chính đáng nhưng không thuộc bài của anh, và nó mời anh phát biểu quan điểm. Bẫy là đoán một con số về rác quỹ đạo cho trông có hiểu biết. Bịa một con số ở đây thì mọi con số khác trong bài mất giá trị cùng lúc, vì cả phòng vừa thấy anh làm việc đó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận câu hỏi là chính đáng trong một câu, và nói thẳng là anh không có số về nó.
- Cho con số anh THẬT SỰ có, và nó dẫn về bài của anh: chu kỳ {{s043}} phút, tức khoảng {{s044}} lần qua lại trên cùng một vùng mỗi ngày.
- Nói ranh giới của bài: anh nghiên cứu điều kiện liên kết, không nghiên cứu chính sách phóng.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói một con số về số vật thể đang bay. Nếu nó sai thì cả phòng vừa nghe anh bịa một con số, và họ sẽ áp cách đọc đó cho bảng kết quả của anh.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Your routing graph is recomputed at fixed time steps. What is the step, and what happens to a path when a link breaks between two recomputations?

*Trụ NTN. Khung trả lời {{s016}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi đã nhìn ra rằng đồ thị tĩnh từng bước là một XẤP XỈ, và họ hỏi về khoảng GIỮA hai bước, tức đúng chỗ xấp xỉ đó hỏng. Bẫy là trả lời bước thời gian rồi dừng, vì phần thứ hai của câu mới là phần tính điểm.

## Khung trả lời
@phut: 0.5
@che-do: so

- Cho bước thời gian và nói ngay nó tương ứng bao nhiêu kilômét chuyển động.
- Con số: bước {{s006}} giây là {{s040}} kilômét chuyển động của mỗi đầu liên kết, nên đồ thị luôn cũ hơn thực tế.
- Tự khai hành vi giữa hai bước: gói đang trên đường đi theo bảng cũ, nên phải nói rõ anh đếm nó là mất, là trễ, hay không đếm.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "giữa hai bước thì liên kết coi như không đổi". Đó chính là giả thiết người hỏi đang nhắm vào, nhắc lại nó là nhận rằng anh chưa đo chỗ đó.

## Người hỏi: chuyên gia đối đầu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

A synchronous training round takes longer than one visibility window. So who aggregates, and does the convergence bound you cited still apply?

*Trụ NTN. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi nối hai thứ anh trình bày rời nhau: cửa sổ nhìn thấy ở phần hệ thống, và bound hội tụ ở phần lý thuyết. Bẫy là bảo vệ từng phần một. Bound anh dẫn gần như chắc chắn giả thiết tham gia đầy đủ hoặc lấy mẫu độc lập, còn lịch quá cảnh thì tuần hoàn, không độc lập.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói ai tổng hợp và tổng hợp ở đâu: trên vệ tinh, ở trạm mặt đất, hay qua liên kết giữa vệ tinh.
- Con số: chu kỳ {{s043}} phút, nên lịch gặp lại là tuần hoàn chứ không phải lấy mẫu ngẫu nhiên độc lập.
- Tự khai rằng bound dẫn trong bài giả thiết lấy mẫu độc lập, nên nó KHÔNG áp dụng nguyên văn, và nói anh dùng gì thay.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "bound vẫn đúng vì nó là trường hợp tổng quát hơn". Người hỏi biết nó không tổng quát hơn, và câu đó biến một giới hạn tự khai thành một tuyên bố sai.

## Người hỏi: người đòi được trích dẫn
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

We proposed a predictive handover scheme in {{s045}} that already does this. How is your contribution different?

*Trụ NTN. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Nghe như đòi trích dẫn, nhưng thật ra đòi anh nêu đóng góp trong một câu, trước mặt người đã làm việc gần nhất. Bẫy là so sánh định tính kiểu "của chúng tôi tổng quát hơn". Chữ tổng quát không có đơn vị, nên phải nêu một điều kiện ĐO ĐƯỢC chia hai bên.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận đó là công trình gần nhất và nói sẽ dẫn, nếu chưa dẫn thì nói thẳng là anh sẽ sửa.
- Nêu một điều kiện đo được: ngưỡng góc nâng, vì chuyển từ {{s006}} lên {{s008}} độ là đổi hẳn số lần chuyển giao.
- Tự khai phần anh KHÔNG khác: nếu cơ chế dự báo giống thì nói giống, rồi nói phần anh thêm là gì.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "của chúng tôi tổng quát hơn". Không có đơn vị nào cho chữ tổng quát, và người hỏi sẽ xin anh một ví dụ ngay tại chỗ.

## Người hỏi: người ngoài ngành
@phan: 6G SEC
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Why is an AI inside the network a security problem? It is just another piece of software.

*Trụ 6G Sec. Khung trả lời {{s005}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu hỏi thẳng và hợp lý, nên bẫy là trả lời bằng một danh sách thuật ngữ tấn công. Thứ phân biệt một mô hình với một phần mềm thường là mô hình có một đầu vào mà kẻ tấn công điều khiển được KHÔNG CẦN quyền gì, và hành vi của nó thay đổi theo đầu vào đó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói đúng điểm khác: phần mềm thường có hành vi do người viết quyết, mô hình học từ chính thứ kẻ tấn công gửi tới.
- Cho con số: một mô hình cập nhật trực tuyến mỗi {{s003}} phút cho kẻ tấn công {{s046}} lượt dạy mỗi ngày.
- Tự khai giới hạn: không phải mô hình nào trong mạng cũng học trực tuyến, nên nói rõ bài của anh nói về loại nào.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "AI thì luôn có thể bị tấn công đối kháng". Nó đúng ở mức khẩu hiệu mà không chỉ ra điều gì khác với phần mềm thường, nên người hỏi vẫn chưa được trả lời.

## Người hỏi: chủ toạ ép thời gian
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

We are over time. One sentence: what should an operator do tomorrow morning?

*Trụ 6G Sec. Khung trả lời {{s012}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Chủ toạ xin một VIỆC LÀM ĐƯỢC, không xin một kết luận. Bẫy là tóm tắt bài. Nếu câu trả lời là một lời khuyên chung thì phần cuối phiên, thứ cả phòng nhớ nhất, là một câu không ai làm được sáng mai.

## Khung trả lời
@phut: 0.5
@che-do: so

- Một việc, có động từ, làm xong trong một ngày.
- Một con số làm ngưỡng: chỉ cần MỘT thành phần đọc được giao diện điều khiển ngoài danh sách là mô hình đe doạ đã đổi.
- Nói hệ quả nếu không làm, trong nửa câu, rồi dừng.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "cần một cách tiếp cận zero trust toàn diện". Nó không phải việc làm được sáng mai, và nó là câu cuối cùng cả phòng nghe thấy.

## Người hỏi: người hỏi lệch chủ đề
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Is this not a regulation problem rather than an engineering problem? Should regulators not simply require it?

*Trụ 6G Sec. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu lệch nhưng có lý, và nó mời anh bàn chính sách, chỗ anh không có dữ liệu. Bẫy là đồng ý cho êm rồi tự đẩy đóng góp của mình thành phụ. Đường ra là chỉ đúng chỗ hai thứ gặp nhau: một yêu cầu pháp lý chỉ có nghĩa khi tồn tại một phép đo để kiểm nó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Đồng ý một phần, trong một câu, và không bàn thêm về chính sách.
- Cho con số của mình: một yêu cầu không kiểm được thì bằng không, và bài này đưa ra {{s047}} phép đo cho {{s047}} yêu cầu trong văn bản chuẩn.
- Tự khai phần anh không trả lời: anh không nghiên cứu hiệu lực thực thi, chỉ nghiên cứu phép kiểm.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "đúng rồi, cần quy định bắt buộc chuyện này". Nó khiến phần kỹ thuật của anh thành một chi tiết, và không ai trong phòng kiểm được câu đó.

## Người hỏi: người biết đúng điểm yếu
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

If the network senses user position as a by-product, you have built a tracking system. Where is the privacy analysis in your paper?

*Trụ 6G Sec. Khung trả lời {{s016}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi biết bài anh không có mục riêng tư, và họ đóng khung hệ của anh bằng một từ. Hai bẫy ngược nhau: phủ nhận khả năng định vị để thoát, và như thế phủ nhận chính đóng góp cảm biến của mình; hay nhận cái khung đó và mất quyền mô tả hệ của mình. Đường ra là cho con số phân giải thật.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nhận rằng hệ sinh ra thông tin vị trí, và cho ngay độ phân giải thật thay vì tranh luận về từ ngữ.
- Con số: phân giải khoảng cách bằng c chia hai lần băng thông, nên với {{s048}} MHz là {{s049}} xentimet, tức mức decimet chứ không phải xentimet.
- Tự khai rằng bài không có phân tích riêng tư, và nói đúng cái thiếu là gì chứ không hứa một mục mới.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "chúng tôi chỉ cảm biến chứ không nhận dạng người dùng". Trong một mạng thì vị trí gắn với một kết nối đã xác thực, nên câu đó sai ngay trong kiến trúc của chính anh.

## Người hỏi: chủ toạ ép thời gian
@phan: PQC
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

Thirty seconds. Which algorithm should they deploy, and at which parameter set?

*Trụ PQC. Khung trả lời {{s012}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Chủ toạ xin một khuyến nghị, và bẫy là trả lời "tuỳ ngữ cảnh". Câu đó đúng về mặt học thuật và vô dụng trong {{s012}} giây, và nó khiến cả phòng nghĩ anh không có ý kiến. Phải chốt một tên và một mức ngay câu đầu, rồi mới nói một điều kiện trong nửa câu.

## Khung trả lời
@phut: 0.5
@che-do: so

- Một tên thuật toán và một bộ tham số, nói ra ngay câu đầu.
- Một con số làm chứng là kích thước thật: khoá công khai ML-KEM-768 là {{s050}} byte, khoá công khai ML-DSA-65 là {{s051}} byte.
- Một điều kiện duy nhất, nửa câu, rồi dừng.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "tuỳ vào yêu cầu cụ thể của hệ thống". Trong {{s012}} giây nó tương đương với không trả lời, và chủ toạ sẽ chuyển micro.

## Người hỏi: người hỏi lệch chủ đề
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

What is your opinion on recent quantum supremacy claims?

*Trụ PQC. Khung trả lời {{s008}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Câu mời anh phát biểu quan điểm về một tranh luận không thuộc bài, và cả hai hướng trả lời đều làm anh yếu đi: nói máy lượng tử còn xa thì anh tự bác động lực của bài, nói nó gần thì anh đưa ra một con số không có nguồn. Đường ra là chỉ ra quyết định di trú không phụ thuộc vào câu đó.

## Khung trả lời
@phut: 0.5
@che-do: so

- Nói rằng anh không đoán mốc thời gian, và nói vì sao mốc đó không phải biến quyết định.
- Cho con số điều kiện: nếu dữ liệu phải bí mật {{s044}} năm thì việc thu hoạch hôm nay đã đủ thành vấn đề.
- Tự khai giới hạn: điều đó đúng cho dữ liệu lưu lâu, không đúng cho mọi hệ.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "theo tôi thì còn khoảng mười năm nữa". Đó là một con số không có nguồn, và nó biến phần động lực của bài anh thành một dự đoán cá nhân.

## Người hỏi: người đọc sai kết quả
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

You said SIKE was broken in {{s045}}. So isogeny based schemes are dead and lattices are the only safe family, correct?

*Trụ PQC. Khung trả lời {{s016}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Người hỏi nối ba bước, và hai bước sau đều sai, nhưng bước đầu là thứ anh vừa nói nên anh phải sửa phần họ SUY RA chứ không sửa phần họ nghe. Bẫy ngược là câu này nghe vừa tai: để nó đứng thì cả phòng nghĩ lattice là lựa chọn duy nhất, và đó là tuyên bố anh không muốn gắn tên vào.

## Khung trả lời
@phut: 0.5
@che-do: so

- Xác nhận phần đúng, rồi tách hai phần sai: một lược đồ bị phá không giết một họ, và lattice không phải họ duy nhất còn lại.
- Cho con số: cài đặt Magma phá SIKEp434 trong khoảng {{s006}} phút trên một nhân, nên đây là một tấn công thật chứ không phải một suy giảm an toàn.
- Tự khai điều anh không biết: không ai chứng minh được lattice an toàn, nó chỉ là chưa bị phá.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "đúng rồi, nên giờ ai cũng dùng lattice". Nó biến một quan sát về thị trường thành một tuyên bố về an toàn, đúng loại câu mà ca SIKE vừa dạy chúng ta đừng nói.

## Người hỏi: người đòi được trích dẫn
@phut: 0.5
@che-do: hoi
@notes: BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.

There is a {{s052}} paper on hybrid key exchange for constrained links reporting lower overhead than yours. Why is it missing from your related work?

*Trụ PQC. Khung trả lời {{s016}} giây.*

## Bẫy nằm ở đâu
@phut: 0.5
@che-do: noi

Bẫy là nhận rằng anh thiếu, rồi tranh luận về con số mào đầu của một bài anh chưa đọc. Người hỏi có thể đúng, và điều đó không sao cả. Việc phải làm là chốt ĐƠN VỊ so sánh trước khi bàn con số nào lớn hơn, vì mào đầu đo bằng byte, bằng phân đoạn, hay bằng số lần truyền lại là ba con số khác nhau.

## Khung trả lời
@phut: 0.5
@che-do: so

- Xin tên bài, nói sẽ đọc và sẽ dẫn nếu nó so được, không phủ nhận cũng không hứa vượt.
- Chốt đơn vị bằng con số của mình: {{s050}} cộng {{s053}} là {{s021}} byte, trên khung {{s054}} byte ở tầng MAC là khoảng {{s055}} phân đoạn, chưa trừ mào đầu phân đoạn.
- Tự khai: nếu họ ít phân đoạn hơn thì họ đã đổi một thứ, và việc của anh là tìm ra họ đổi gì, không phải bác con số.

## Đừng nói
@phut: 0.5
@che-do: noi

**Đừng nói:**

- Đừng nói "con số của họ chắc không tính mào đầu phân đoạn". Anh chưa đọc bài đó, nên đây là đoán về công trình của người đang ngồi trước mặt.

## !cam-on
@phan: HỎI ĐÁP
@phut: 0.5
@che-do: lang
@notes: Nhắc lại rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: tiêu chí ôn là THỜI GIAN, không phải đúng sai.

Thẻ nào trả lời quá khung giờ thì ghi lại, đó mới là thẻ phải ôn, không phải thẻ trả lời sai.
