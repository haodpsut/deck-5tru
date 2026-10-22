---
tieu-de: Trụ 1 · NID
phu-de: Network Intrusion Detection · toàn trụ trong một lượt
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 40
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: NID
@phut: 1.5
@che-do: noi
@notes: Deck bao quát cả trụ. Chi tiết nằm ở deck từng module.

## Trụ này trả lời câu gì
@phut: 2.5
@che-do: hoi
@notes: Nói tên trụ, rồi im. Để người nghe tự hỏi mười module kia là gì.

{{TAKE_HOME}}

**Network Intrusion Detection** gồm {{s001}} module, {{s002}} khối có chấm điểm.

## Module nào dày nhất
@hinh: toan
@phut: 3
@che-do: hinh
@notes: Chỉ vào thanh dài nhất. Dày không có nghĩa là quan trọng nhất, nhưng là chỗ tốn thời gian nhất.

!hinh hinh/day-mong.svg | Số khối **có chấm điểm** của từng module. Thanh dài là chỗ phải để dành nhiều buổi hơn.

## m1.1 Đặt bài toán phát hiện
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Đơn vị quan sát (observation unit) của tôi là gói (packet) tin, luồng (flow), cửa sổ thời gian (time window) hay đồ thị, và lựa chọn đó làm cho tuyên bố nào của tôi không còn kiểm được?

## m1.1 · luận điểm
@phut: 1.5
@che-do: noi

Đơn vị quan sát là câu đầu tiên của phần đánh giá, không phải câu cuối

## m1.2 Dataset và vết thương riêng của từng cái
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Với dataset tôi đang dùng, con số tôi báo bị thổi lên bởi cơ chế nào, và tôi phải khai gì để reviewer không đánh vào chỗ đó?

## m1.2 · luận điểm
@phut: 1.5
@che-do: noi
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

Mỗi dataset có một vết thương, và nó thổi số theo một cơ chế đo được

## m1.3 Phép đo, và chi phí vận hành của phép đo
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Ở mức FPR tôi đang báo, bộ phát hiện của tôi sinh bao nhiêu cảnh báo sai mỗi ngày, và SOC có đủ người đọc không?

## m1.3 · luận điểm
@phut: 1.5
@che-do: noi

Phép đo nào khai được, phép đo nào không

## m1.4 Base-rate fallacy
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Với tỉ lệ tấn công thật trong mạng của tôi, FPR của tôi phải nhỏ tới đâu để một cảnh báo có nghĩa, và con số đó có khả thi không?

## m1.4 · luận điểm
@phut: 1
@che-do: noi

Vì sao module này đứng đầu trụ

## m1.5 Drift và cách chia dữ liệu theo thời gian
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Nếu tôi chia lại dữ liệu theo thời gian thay vì ngẫu nhiên, con số của tôi tụt bao nhiêu, và tôi có dám báo cả hai không?

## m1.5 · luận điểm
@phut: 1
@che-do: noi

Chia ngẫu nhiên không phải một lựa chọn kỹ thuật, nó là một giả thiết

## m1.6 Lẩn tránh: không gian đặc trưng so với không gian
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Nhiễu đối kháng tôi sinh ra trong không gian đặc trưng có dựng lại được thành gói tin gửi lên dây không, và nếu không thì bài của tôi đang tuyên bố cái gì?

## m1.6 · luận điểm
@phut: 1
@che-do: noi

Nghiệm trong không gian đặc trưng không phải một tấn công

## m1.7 Giải thích được, và độ ổn định của lời giải thích
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Nếu tôi chạy lại với hạt khác, {{s001}} đặc trưng quan trọng nhất có còn là {{s001}} cái đó không, và nếu không thì lời giải thích của tôi là gì?

## m1.7 · luận điểm
@phut: 1
@che-do: noi

Một lời giải thích không ổn định thì không phải một lời giải thích

## m1.8 Chọn kiến trúc mô hình, và chỗ đứng của KAN với
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Trên dữ liệu bảng của IDS, tôi có bằng chứng gì để nói mô hình mới của tôi hơn một bộ gradient boosting được tinh chỉnh tử tế?

## m1.8 · luận điểm
@phut: 1
@che-do: noi

Câu hỏi đầu tiên của mọi phản biện về mô hình mới

## m1.9 Hiệu chuẩn: điểm số của mô hình có phải xác suất
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Khi mô hình của tôi in ra {{s003}}, có đúng {{s004}} các lần như thế là tấn công thật không, và nếu không thì ngưỡng tôi chọn còn nghĩa gì?

## m1.9 · luận điểm
@phut: 1
@che-do: noi

Thứ hạng và xác suất là hai thứ khác nhau

## m1.10 Lưu lượng mã hoá: TLS 1.3
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Trong mạng năm {{s005}}, bao nhiêu phần đặc trưng mà dataset của tôi dùng còn lấy được, và bộ phát hiện của tôi có đang học trên thứ không còn tồn tại?

## m1.10 · luận điểm
@phut: 1
@che-do: noi

Ba nhóm đặc trưng, và nhóm nào còn sống

## Số của trụ
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s006}} | triệu gói mỗi giây | Liên kết {{s001}} Gbps
!so {{s007}} | nano giây | Cùng liên kết {{s001}} Gbps và khung {{s008}} byte. Ngân sách thời
!so {{s009}} | byte | Trên Ethernet, mỗi khung còn kéo theo bao nhiêu byte phí nằm

## Số của trụ (tiếp)
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s010}} | % | Trong tập huấn luyện của KDD99
!so {{s011}} | bản ghi | Tập KDDTrain+ của NSL-KDD có bao nhiêu bản ghi?
!so {{s012}} | bản ghi | Tập KDDTest+ của NSL-KDD có bao nhiêu bản ghi?

## Số của trụ (tiếp)
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s013}} | đặc trưng | UNSW-NB15 gồm khoảng {{s014}} triệu bản ghi và {{s015}} họ tấn công.
!so {{s016}} | đặc trưng | CIC-IDS2017 thu lưu lượng {{s017}} ngày liên tiếp từ thứ Hai tới
!so {{s018}} | cảnh báo mỗi ngày | FPR = 10⁻³ trên {{s001}} triệu sự kiện lành mỗi ngày. Bao

## !cam-on
@phut: 1
@che-do: lang
@notes: Nhắc lại rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 1
@che-do: noi
@notes: Món tặng: deck để định vị, site để nhớ.

Deck này chỉ là bản đồ của trụ. Chỗ học thật là `https://hoc-5-tru-web.vercel.app/#/tru/1`.
