---
tieu-de: Trụ 2 · FL
phu-de: Federated Learning · toàn trụ trong một lượt
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
@phan: FL
@phut: 1.5
@che-do: noi
@notes: Deck bao quát cả trụ. Chi tiết nằm ở deck từng module.

## Trụ này trả lời câu gì
@phut: 2.5
@che-do: hoi
@notes: Nói tên trụ, rồi im. Để người nghe tự hỏi mười module kia là gì.

{{TAKE_HOME}}

**Federated Learning** gồm {{s001}} module, {{s002}} khối có chấm điểm.

## Module nào dày nhất
@hinh: toan
@phut: 3
@che-do: hinh
@notes: Chỉ vào thanh dài nhất. Dày không có nghĩa là quan trọng nhất, nhưng là chỗ tốn thời gian nhất.

!hinh hinh/day-mong.svg | Số khối **có chấm điểm** của từng module. Thanh dài là chỗ phải để dành nhiều buổi hơn.

## m2.1 Họ thuật toán và thứ mỗi cái sửa
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

FedProx, SCAFFOLD, FedNova mỗi cái sửa đúng một bệnh nào của FedAvg, và bệnh đó có xuất hiện trong bài của tôi không?

## m2.1 · luận điểm
@phut: 1.5
@che-do: noi

Bốn thuật toán, bốn bệnh khác nhau, và chỉ một cái là bệnh của anh

## m2.2 Non-IID: đo nó bằng gì
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Tôi khai dữ liệu của tôi là non-IID bằng con số nào, và con số đó phải xuất hiện ở đâu trong bài?

## m2.2 · luận điểm
@phut: 1.5
@che-do: noi
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

Chữ non-IID không phải một phép đo

## m2.3 Hội tụ: đọc được bound chứ không chỉ trích nó
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Trong bound của FedAvg, tăng E làm số hạng nào phình, và bound đó có áp được cho mô hình của tôi không?

## m2.3 · luận điểm
@phut: 1.5
@che-do: noi

Trích một bound là mượn thẩm quyền của giả thiết của nó

## m2.4 Nén và ngân sách truyền
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Một vòng của tôi tốn bao nhiêu byte mỗi client, và nén {{s001}} lần có thật sự giảm {{s001}} lần thời gian hội tụ không?

## m2.4 · luận điểm
@phut: 1
@che-do: noi

Byte tới mục tiêu, không phải vòng tới mục tiêu

## m2.5 Riêng tư có định nghĩa: DP và kế toán
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

epsilon của tôi là bao nhiêu, ở mức đơn vị kề nào (bản ghi hay người dùng), và đánh đổi độ chính xác là bao nhiêu điểm?

## m2.5 · luận điểm
@phut: 1
@che-do: noi

Một con số epsilon không nói gì nếu thiếu ba thứ đi kèm

## m2.6 Tấn công vào FL
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Trong ba họ tấn công (suy luận, đầu độc, cửa hậu), họ nào áp được vào hệ của tôi với đúng năng lực kẻ tấn công (attacker capability) mà tôi đã khai?

## m2.6 · luận điểm
@phut: 1
@che-do: noi

Tấn công nào khả thi là hệ quả của mô hình đe doạ, không phải của thuật toán

## m2.7 Phòng vệ và giới hạn cứng của nó
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Bộ tổng hợp bền của tôi chịu được tỉ lệ kẻ xấu tới đâu, và tôi đã khai con số đó chưa?

## m2.7 · luận điểm
@phut: 1
@che-do: noi

Mọi phòng vệ dựa khoảng cách đều mua tính bền bằng một giả thiết về client lành

## m2.8 FL cho IDS: dựng bài toán cho đúng
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Ai là client, nhãn ở đâu ra, và câu sao không gom dữ liệu về một chỗ thì tôi trả lời bằng con số nào?

## m2.8 · luận điểm
@phut: 1
@che-do: noi

Ba câu hỏi dựng bài toán, và chỉ một trong ba có thể trả lời bằng số

## m2.9 Cá nhân hoá
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Bài của tôi nên báo độ chính xác toàn cục hay độ chính xác trên từng client, và hai con số đó khác nhau bao nhiêu?

## m2.9 · luận điểm
@phut: 1
@che-do: noi

Hai con số, và cái mà bảng kết quả của anh đang báo

## m2.10 Hệ thống thật: kẻ chậm
@phut: 1
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Một vòng của tôi mất bao lâu theo đồng hồ treo tường, và hạn chờ tôi đặt đang lặng lẽ loại nhóm client nào ra khỏi mô hình?

## m2.10 · luận điểm
@phut: 1
@che-do: noi

Vòng của anh dài bằng client chậm nhất, và ai không có mặt trong mô hình

## Số của trụ
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s003}} | tỉ lệ C | Tỉ lệ client tham gia mỗi vòng
!so {{s004}} | lần | Lượng truyền một vòng một chiều của SCAFFOLD
!so {{s005}} | lớp | Dirichlet đối xứng với alpha = {{s006}} trên C = {{s001}} lớp.

## Số của trụ (tiếp)
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s007}} | lớp | Cùng công thức, alpha = {{s008}} và C = {{s001}}. Số lớp
!so {{s009}} | TV | C = {{s001}} lớp
!so {{s004}} | bậc | Trong B, số hạng chứa số bước cục bộ phình theo nó

## Số của trụ (tiếp)
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s010}} |  | Bốn client, trọng số tổng hợp đồng đều, mỗi client có sigma_k
!so {{s011}} |  | Lấy L = {{s010}} và mu = {{s006}} nên kappa = L/mu.
!so {{s012}} | MB | ResNet-18 có {{s013}} triệu tham số

## !cam-on
@phut: 1
@che-do: lang
@notes: Nhắc lại rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 1
@che-do: noi
@notes: Món tặng: deck để định vị, site để nhớ.

Deck này chỉ là bản đồ của trụ. Chỗ học thật là `https://hoc-5-tru-web.vercel.app/#/tru/2`.
