---
tieu-de: Lưu lượng mã hoá: TLS 1.3, QUIC, ECH và cái chết của soi tải
phu-de: Trụ 1 NID · module 1.10
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 81.5
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

Trong mạng năm {{s001}}, bao nhiêu phần đặc trưng mà dataset của tôi dùng còn lấy được, và bộ phát hiện của tôi có đang học trên thứ không còn tồn tại?

## Ba nhóm đặc trưng, và nhóm nào còn sống
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Mọi bộ phát hiện xâm nhập đều ăn một vector đặc trưng do bộ bóc gói (packet) sinh ra. Các đặc trưng đó xếp được thành ba nhóm theo **khả năng lấy được** từ một điểm quan sát trên đường truyền: **Tải tin**: n-gram byte, chuỗi ký tự, chữ ký nội dung. Chết với TLS. **Siêu dữ liệu bắt tay**: SNI, dấu tay thư viện TLS, thời điểm và kích thước gói bắt tay. Chết dần với ECH. **Hình dáng luồng (flow)**:

## Ba nhóm đặc trưng, và nhóm nào còn sống (tiếp)
@phut: 1
@che-do: noi

thời điểm, kích thước, hướng, nhịp. Vẫn còn. Điểm quan trọng nhất của module này không phải là mã hoá làm mất đặc trưng, mà là một bảng kết quả **không khai nhóm đặc trưng nào nó dùng** thì không ai biết nó còn chạy được ở đâu. Hai bài cùng báo F1 bằng {{s002}} có thể ở hai phía của ranh giới đó, và không phép đo nào trong bảng phân biệt được chúng.

## Ba nhóm đặc trưng, và nhóm nào còn sống (tiếp)
@phut: 1
@che-do: noi

Luật thứ hai, ngược chiều với trực giác: mã hoá che **nội dung**, không che **sự tồn tại** của gói. Lẫn hai cái đó là cách nhanh nhất để kết luận sai rằng quan sát đường truyền đã hết việc.

## Ba nhóm đặc trưng, xếp theo khả năng lấy được
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Ba nhóm đặc trưng, xếp theo khả năng lấy được · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Nhóm một là **tải tin**, lấy được chỉ trên phần lưu lượng không mã hoá. Nhóm hai là **siêu dữ liệu bắt tay**, trụ chính là SNI cộng dấu tay thư viện TLS. Nhóm ba là **hình dáng luồng**: thời điểm, kích thước, hướng và nhịp gói.

## Ba nhóm đặc trưng, xếp theo khả năng lấy được · (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: bảng đặc trưng của bài phải khai nhóm cho TỪNG đặc trưng, vì nhóm quyết định bài còn chạy được ở mạng nào. Và chỉ nhóm ba còn nguyên dưới TLS {{s004}} cộng ECH, nên một dòng kết quả cho cấu hình chỉ dùng nhóm ba là dòng mà phản biện sẽ hỏi trước tiên.

## Vì sao QUIC khó hơn TCP cho người quan sát
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Vì sao QUIC khó hơn TCP cho người quan sát · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

QUIC gói bắt tay trong UDP, chuyển sang khoá bắt tay **sớm hơn** TLS trên TCP, và **bảo vệ cả số thứ tự gói**.

## Vì sao QUIC khó hơn TCP cho người quan sát · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ, và đây là chỗ hay bị nói quá: cái mất khi sang QUIC **không phải SNI**. SNI vẫn nằm trong ClientHello của gói Initial và vẫn đọc được nếu không bật ECH. Cái mất là một họ đặc trưng mức TCP: số thứ tự, cờ, truyền lại, mẫu ACK, kích thước cửa sổ. Những đặc trưng đó không có đại lượng tương đương đo được trên QUIC, nên chúng không trở thành số xấu hơn, chúng mất định nghĩa.

## ECH, và nhóm đặc trưng nào nó đánh
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s006}} trên bốn.*

## ECH, và nhóm đặc trưng nào nó đánh · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

ECH, tức Encrypted Client Hello, mã hoá ClientHello bên trong bằng khoá công khai của máy chủ, nên SNI không còn đọc được từ đường truyền.

## ECH, và nhóm đặc trưng nào nó đánh · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: ECH đánh đúng **nhóm hai**. Nhóm một đã chết từ TLS {{s004}} chứ không chết vì ECH, và nhóm ba không đổi. Hệ quả cho đánh giá: mọi đặc trưng neo vào định danh máy chủ, gồm cả bảng tra SNI và danh sách tên miền xấu, đều có hạn sử dụng gắn với tỉ lệ triển khai ECH của mạng đích, và tỉ lệ đó phải là một con số trong bài chứ không phải một nhận xét.

## Mô hình đếm đặc trưng còn lấy được
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`F_con = f1·(1 − e) + f2·(1 − e·h) + f3t·(1 − q) + f3u ti_le_mat = {{s003}} − F_con/(f1 + f2 + f3t + f3u)`

**Giả thiết nó đứng trên:**

## Mô hình đếm đặc trưng còn lấy được (tiếp)
@phut: 1
@che-do: so

- e là tỉ lệ luồng đã mã hoá; nhóm tải tin lấy được đúng trên phần không mã hoá nên đóng góp f1·(1 − e)
- h là tỉ lệ luồng mã hoá có bật ECH, và bật ECH coi là độc lập với việc luồng có mã hoá hay không, nên SNI mất trên phần e·h
- q là tỉ lệ luồng dùng QUIC; f3t là số đặc trưng hình dáng luồng dựa chuỗi mức TCP, mất đúng trên phần QUIC

## Mô hình đếm đặc trưng còn lấy được (tiếp)
@phut: 1
@che-do: so

- f3u là số đặc trưng chỉ cần thời điểm, kích thước và hướng gói, nên không phụ thuộc giao thức vận chuyển
- Đây là mô hình ĐẾM theo kỳ vọng trên tập luồng, không phải số đo: nó cho số đặc trưng còn lấy được, nó KHÔNG cho hiệu năng phát hiện

## Mô hình đếm đặc trưng còn lấy được · ghi chú
@phut: 1
@che-do: noi

Giả thiết cuối là giả thiết đáng tiền nhất. Đi từ số đếm sang hiệu năng cần thêm một giả thiết về **độ dư thừa** giữa các đặc trưng, mà mô hình này không khai. Hai trường hợp biên đều xảy ra thật:

## Mô hình đếm đặc trưng còn lấy được · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

nếu nhóm bị mất chỉ nhắc lại thông tin đã có trong nhóm hình dáng luồng thì hiệu năng hầu như giữ nguyên; nếu nó là nguồn tín hiệu duy nhất cho một lớp tấn công thì lớp đó rơi về mức đoán ngẫu nhiên. Vì vậy con số đúng để báo trong bài là một **bảng ablation theo nhóm**, không phải một tỉ lệ đặc trưng.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} | nhóm | Module này xếp đặc trưng mạng thành mấy nhóm theo khả năng
!so {{s004}} |  | Bản TLS nào mã hoá phần sau của bắt tay

## Mô hình dùng 20 đặc trưng tải tin
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình dùng {{s007}} đặc trưng tải tin, {{s008}} đặc trưng siêu dữ liệu bắt tay và {{s009}} đặc trưng hình dáng luồng, coi nhóm hình dáng luồng lấy được đủ. Mạng đích có {{s012}} lưu lượng mã hoá, và trong phần mã hoá thì {{s013}} bật ECH. Kỳ vọng số đặc trưng còn lấy được mỗi luồng là bao nhiêu?

f1 = {{s007}}, f2 = {{s008}}, f3 = {{s009}}, enc = {{s010}}, ech = {{s011}}

## Mô hình dùng 20 đặc trưng tải tin · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`f1⋆(1-enc) + f2⋆(1-enc⋆ech) + f3`

## Mô hình dùng 20 đặc trưng tải tin · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s014}} đặc trưng mỗi luồng, trên {{s015}} đặc trưng mô hình khai dùng, tức mất {{s016}}. Để ý cấu trúc của con số: nhóm tải tin đóng góp đúng {{s003}} trên {{s007}} đặc trưng nó khai, nhóm bắt tay còn {{s017}} trên {{s008}}, còn {{s009}} đặc trưng hình dáng luồng đi qua nguyên vẹn. Nói cách khác, {{s018}} trên {{s019}} đặc trưng bị mất nằm ở một nhóm duy nhất, nên bảng ablation theo nhóm là cách duy nhất để thấy chuyện đó.

## Một bộ phát hiện chỉ dùng hai nhóm đầu
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bộ phát hiện chỉ dùng hai nhóm đầu, tức tải tin và SNI. Mạng đích có {{s012}} lưu lượng mã hoá, và {{s021}} phần mã hoá bật ECH. Trên bao nhiêu phần trăm luồng nó còn có ít nhất một đặc trưng để tính?

enc = {{s010}}, ech = {{s020}}

## Một bộ phát hiện chỉ dùng hai nhóm đầu · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆(1 - enc⋆ech)`

Khoảng {{s022}}. Dẫn lại cho chắc: tải tin lấy được trên {{s023}} luồng, SNI lấy được trên {{s024}} luồng, và tập luồng có tải tin nằm trong tập luồng có SNI, nên hợp của hai nhóm đúng bằng {{s024}}. Trên {{s025}} luồng còn lại, vector đặc trưng của bộ phát hiện này rỗng: nó không chạy chậm hơn, nó không chạy được.

## Một bộ phát hiện chỉ dùng hai nhóm đầu · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là loại con số phải nằm trong phần đánh giá, vì nó là trần cứng mà không kiến trúc nào vượt qua.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mạng đích bật ECH trên {{s026}} lưu lượng TLS. Nhóm đặc trưng nào bị đánh trực tiếp?

- Tải tin, vì ECH thêm một lớp mã hoá nữa
- Siêu dữ liệu bắt tay, vì SNI không còn đọc được từ đường truyền
- Hình dáng luồng, vì ECH đổi kích thước gói bắt tay
- Cả ba nhóm như nhau

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Siêu dữ liệu bắt tay, vì SNI không còn đọc được từ đường truyền**

ECH mã hoá ClientHello bên trong, nên SNI không còn lấy được, và SNI là trụ chính của nhóm siêu dữ liệu bắt tay. Tải tin thì đã chết từ TLS chứ không chết vì ECH, nên đổ lỗi cho ECH ở nhóm đó là nhầm thời điểm. Hình dáng luồng có xê dịch chút ít vì kích thước gói bắt tay thay đổi, nhưng nhóm đó vẫn đo được:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

cái ECH lấy đi là một trường định danh, không phải khả năng quan sát luồng. Và ba nhóm không bị ảnh hưởng như nhau, đó là lý do phải xếp nhóm ngay từ đầu.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bộ phát hiện huấn luyện trên dataset có tải tin rõ, dùng {{s007}} đặc trưng n-gram tải tin và {{s008}} đặc trưng SNI. Mạng đích có {{s012}} lưu lượng mã hoá, và {{s021}} phần mã hoá bật ECH. Điều nào mô tả đúng tình trạng của nó?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Nó chạy chậm hơn vì phải giải mã trước khi bóc đặc trưng
- Nó chạy với hiệu năng giảm đúng theo tỉ lệ số đặc trưng còn lại
- Nó vẫn chạy đúng, vì mô hình đã học được quy luật tổng quát của tấn công
- Trên {{s025}} luồng nó không có đặc trưng nào để tính, nên ở đó nó không chạy được

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Trên {{s025}} luồng nó không có đặc trưng nào để tính, nên ở đó nó không chạy được**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Tải tin lấy được trên {{s023}} luồng, SNI lấy được trên {{s024}} luồng, và tập có tải tin nằm trong tập có SNI, nên hợp của hai nhóm là {{s024}}. Trên {{s025}} còn lại vector đặc trưng rỗng, nên đây không phải chuyện chậm và cũng không phải chuyện hiệu năng giảm theo tỉ lệ: không có đầu vào thì không có đầu ra. Giải mã không phải phương án vì bộ quan sát không có khoá.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Và tuyên bố quy luật tổng quát thì không kiểm được: mô hình chỉ tổng quát trên không gian đặc trưng mà nó còn nhìn thấy.

## Phản biện hỏi
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Phản biện hỏi: bộ phát hiện của anh còn chạy được trong mạng hiện đại không? Câu trả lời nào kiểm được?

## Phản biện hỏi (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi đạt F1 bằng {{s002}}, cao hơn mọi baseline trên cùng dataset
- Dataset của chúng tôi thu năm {{s027}} nên vẫn đại diện cho lưu lượng doanh nghiệp
- Chúng tôi khai bảng đặc trưng theo ba nhóm, báo một dòng kết quả cho cấu hình chỉ dùng nhóm hình dáng luồng, và ghi rõ nhóm nào mất ở mức mã hoá nào
- Chúng tôi dùng học sâu nên mô hình tự học đặc trưng, không phụ thuộc nhóm nào

## Phản biện hỏi · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chúng tôi khai bảng đặc trưng theo ba nhóm, báo một dòng kết quả cho cấu hình chỉ dùng nhóm hình dáng luồng, và ghi rõ nhóm nào mất ở mức mã hoá nào**

## Phản biện hỏi · đáp (tiếp)
@phut: 1
@che-do: noi

Chỉ một câu trong số này sinh ra con số mà phản biện kiểm được: bảng ablation theo nhóm đặc trưng, cộng một dòng kết quả cho cấu hình chỉ còn nhóm hình dáng luồng. F1 trên cùng dataset không nói gì về mạng đích, vì cả hai bên đều đo trên cùng không gian đặc trưng đã chết. Năm thu dữ liệu là lập luận ngược chiều với chính nó: càng cũ càng ít đại diện.

## Phản biện hỏi · đáp (tiếp)
@phut: 1
@che-do: noi

Và học sâu vẫn ăn vector do bộ bóc gói sinh ra, nên nó phụ thuộc nhóm đúng như mọi mô hình khác.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đánh giá sau có một dòng nhảy phạm vi. Bấm vào dòng đó.

- Chúng tôi đánh giá trên CIC-IDS2017, dùng {{s028}} đặc trưng do CICFlowMeter sinh.
- Bộ phát hiện đạt F1 bằng {{s029}} và FPR bằng {{s030}}.
- Kết quả cho thấy phương pháp dùng được trong mạng doanh nghiệp hiện nay.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Kết quả cho thấy phương pháp dùng được trong mạng doanh nghiệp hiện nay.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai dòng đầu là phát biểu về một bộ dữ liệu và chúng hợp lệ. Dòng thứ ba nhảy từ bộ dữ liệu sang mạng đang chạy, mà bước nhảy đó cần một tiền đề không được khai: những đặc trưng mô hình dùng còn lấy được trong mạng đó. Trong {{s028}} đặc trưng của CICFlowMeter có cả họ dựa chuỗi mức TCP, mà họ đó mất định nghĩa trên QUIC. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

khai bảng đặc trưng theo ba nhóm, rồi báo một dòng kết quả cho cấu hình chỉ còn nhóm hình dáng luồng. Nếu dòng đó tụt sâu thì đó là kết quả thật của bài, không phải thứ để bỏ ra.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau có một dòng sai về bản chất của dấu tay. Bấm vào dòng đó.

- Chúng tôi dùng dấu tay JA3 của ClientHello làm đặc trưng định danh ứng dụng.
- JA3 là bất biến của ứng dụng, nên bảng tra học trên tập huấn luyện dùng lại được mà không cần cập nhật.
- Với các luồng không có JA3 trong bảng tra, chúng tôi lùi về đặc trưng hình dáng luồng.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**JA3 là bất biến của ứng dụng, nên bảng tra học trên tập huấn luyện dùng lại được mà không cần cập nhật.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

JA3 băm danh sách bộ mã, nhóm đường cong và danh sách phần mở rộng theo đúng thứ tự mà phía khách gửi, nên nó đổi khi thư viện TLS nâng cấp, khi bật hoặc tắt một phần mở rộng, và khi hệ điều hành đổi mặc định. Nó là dấu tay của MỘT bản dựng, không phải của ứng dụng. Hệ quả:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

bảng tra JA3 có hạn sử dụng, và mô hình neo vào nó tụt dần mà không ai thấy lý do, vì phép đo tổng gộp không tách được phần dấu tay chưa gặp. Dòng đầu và dòng cuối đều hợp lệ, kể cả đường lùi về hình dáng luồng.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn thảo luận sau tự mâu thuẫn. Bấm vào dòng gây ra mâu thuẫn.

- Vì {{s012}} lưu lượng đã mã hoá, soi tải không còn là phương án.
- Do đó mọi phương pháp dựa trên quan sát đường truyền đều mất hiệu lực, và chỉ còn đặt tác tử trên máy trạm.
- Chúng tôi vì vậy cũng báo kết quả cho cấu hình chỉ dùng thời điểm, kích thước và hướng gói.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Do đó mọi phương pháp dựa trên quan sát đường truyền đều mất hiệu lực, và chỉ còn đặt tác tử trên máy trạm.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Mã hoá che NỘI DUNG, không che SỰ TỒN TẠI của gói. Thời điểm, kích thước, hướng và nhịp của luồng vẫn quan sát được nguyên vẹn trên mọi phiên TLS {{s004}} và QUIC, và đó chính là nhóm đặc trưng mà dòng cuối của cùng đoạn này dùng. Vậy dòng giữa suy từ dòng đầu ra một kết luận mạnh hơn dữ kiện, và nó mâu thuẫn ngay với dòng kế tiếp. Dòng đầu đúng, dòng cuối đúng. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

thu phạm vi về đúng nhóm bị mất, tức tải tin và siêu dữ liệu bắt tay, rồi nói rõ nhóm hình dáng luồng là nhóm còn làm được việc.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt f1, f2, f3t, f3u là số đặc trưng mô hình dùng trong bốn họ: tải tin, siêu dữ liệu bắt tay, hình dáng luồng dựa chuỗi mức TCP, và hình dáng luồng chỉ cần thời điểm với kích thước
- Tải tin lấy được đúng trên phần luồng không mã hoá, nên kỳ vọng đóng góp là f1·(1 − e)
- SNI mất đúng trên phần luồng vừa mã hoá vừa bật ECH, nên nhóm hai đóng góp f2·(1 − e·h)

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Đặc trưng dựa chuỗi mức TCP mất trên phần QUIC, nên đóng góp f3t·(1 − q), còn f3u đóng góp đủ vì nó không phụ thuộc giao thức vận chuyển
- Cộng bốn họ: F_con = f1·(1 − e) + f2·(1 − e·h) + f3t·(1 − q) + f3u, và tỉ lệ đặc trưng mất là {{s003}} − F_con chia tổng bốn họ

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Dừng ở đây. Số đếm này KHÔNG chuyển được sang hiệu năng phát hiện, nên bước tiếp theo trong bài là một bảng ablation theo nhóm, không phải một phép nhân

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: {{s031}} đặc trưng khai dùng · {{s032}} còn lấy được mỗi luồng · mất {{s033}} · bộ phát hiện cần tải tin còn chạy trên {{s023}} luồng

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Soi được tải tin trên phần lưu lượng không mã hoá** tắt đi: Điểm quan sát không giải mã được gì, và phần cleartext cũng không còn.
- **Đọc được SNI trong bắt tay** tắt đi: Mạng đích bật ECH trên toàn bộ lưu lượng TLS.
- **Luồng dùng TCP, nên số thứ tự gói và nhịp ACK có định nghĩa** tắt đi: Lưu lượng đích chuyển hết sang QUIC.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dataset và mạng đích có cùng tập đặc trưng lấy được** tắt đi: Dataset thu khi tải tin còn rõ, mạng đích thì không.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Mô phỏng này là một **mô hình đếm**, không phải số đo. Nó trả lời đúng một câu: ở cấu hình mạng đang đặt, bảng đặc trưng của anh còn lấy được bao nhiêu phần. Nó **không** trả lời câu hiệu năng phát hiện giảm bao nhiêu, vì để đi từ số đếm sang hiệu năng phải khai độ dư thừa giữa các đặc trưng, và mô phỏng không khai điều đó.

## Chỗ này phải tự kéo, không xem được (tiếp)
@phut: 1
@che-do: demo

Bốn họ đặc trưng khai bằng bốn thanh kéo, ba điều kiện mạng khai bằng ba thanh tỉ lệ. Việc phải làm: kéo cả ba tỉ lệ về {{s003}} và xem con số nào còn lại.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.10` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Your evaluation uses CIC-IDS2017 with CICFlowMeter features. A substantial part of that feature set is derived from cleartext payload inspection and from TCP sequence behaviour such as flags, retransmissions and ACK patterns. In a deployment with TLS {{s004}}, Encrypted Client Hello and a large QUIC share, several of those features are either unavailable or have no transport level equivalent. Please state which of your features remain observable, and report detection performance restricted to that subset.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have added the feature inventory the reviewer asks for. Table II now classifies all {{s028}} features into three groups: {{s034}} payload derived, {{s035}} handshake metadata, and {{s036}} flow shape. Within flow shape we further separate {{s037}} features that depend on TCP sequence state, which have no measurable equivalent on QUIC, from {{s009}} that need only packet timing, size and direction. Section V-D adds the restricted result.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Using only the {{s009}} transport agnostic features, macro F1 falls from {{s038}} to {{s039}}, and per class results show that the drop is concentrated in two web attack classes that relied on payload n-grams, while denial of service and port scan classes are essentially unchanged. We now present the restricted number as the headline result and the full feature number as an upper bound measured on a corpus with cleartext payload. We also state explicitly that the feature count is not a performance predictor:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

going from a count to a performance figure needs an assumption about redundancy between features, which we do not make, which is why we report the ablation rather than a scaling factor.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: nói rằng CIC-IDS2017 là dataset chuẩn của lĩnh vực và được dùng rộng rãi. Đúng về thực hành, không trả lời được phản bác, vì phản bác không hỏi về độ phổ biến mà hỏi về khả năng lấy được.
- Mức {{s005}}: thừa nhận một phần đặc trưng không còn lấy được, nhưng chỉ nói định tính, không khai bảng đặc trưng theo nhóm và không có dòng kết quả nào cho tập con còn lại.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: khai bảng đặc trưng theo ba nhóm với số đếm từng nhóm, cộng một dòng kết quả cho cấu hình chỉ dùng nhóm hình dáng luồng không phụ thuộc giao thức vận chuyển, và nói rõ con số chính của bài là dòng nào.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III states that JA3 fingerprints identify the client application and that the fingerprint table learned on the training set transfers without updating. JA3 is a hash over the ClientHello cipher list, curve list and extension ordering, so it changes with the TLS library build and with extension configuration. Please state the collection window of your fingerprint table, report performance on flows whose fingerprint is not in that table, and explain what happens to this feature group under Encrypted Client Hello.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have corrected the claim and added the measurements. Section III now states that a JA3 value fingerprints a specific client build and configuration, not an application, and that the mapping therefore expires. Our fingerprint table was collected over a four week window, and Table VI reports that {{s040}} percent of test flows carry a fingerprint absent from that table.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

On those flows macro F1 is {{s041}} against {{s038}} on flows with a known fingerprint, and the model falls back to flow shape features, which we now state in the method rather than in the appendix. On Encrypted Client Hello the entire handshake metadata group, {{s035}} features including JA3, becomes unavailable, so Section V-D adds a configuration that uses no handshake feature at all.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

That configuration reaches macro F1 of {{s039}} and it is the number we now report as the main result, precisely so that the headline does not depend on the ECH deployment rate of the target network, which is outside our control and which we do not claim to measure.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: nói rằng JA3 được dùng rộng rãi trong công nghiệp. Không trả lời cả ba câu hỏi, và câu hỏi thứ ba thì chưa được chạm tới.
- Mức {{s005}}: khai cửa sổ thu bảng tra và thừa nhận dấu tay đổi theo bản dựng, nhưng không có con số cho luồng có dấu tay chưa gặp, nên phản biện vẫn không kiểm được mức tụt.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: khai cửa sổ thu, báo tỉ lệ luồng có dấu tay chưa gặp trên tập kiểm, và báo hiệu năng riêng cho nhóm luồng đó, cộng nói rõ ECH làm cả nhóm này mất.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.10` bấm thẻ.
