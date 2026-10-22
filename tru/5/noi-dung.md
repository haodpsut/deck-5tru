---
tieu-de: Trụ 5 · PQC
phu-de: Post-Quantum Cryptography · toàn trụ trong một lượt
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 42
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: PQC
@phut: 0.5
@che-do: noi
@notes: Deck bao quát cả trụ. Chi tiết nằm ở deck từng module.

## Trụ này trả lời câu gì
@phut: 2.5
@che-do: hoi
@notes: Nói tên trụ, rồi im. Để người nghe tự hỏi mười module kia là gì.

{{TAKE_HOME}}

**Post-Quantum Cryptography** gồm {{s001}} module, {{s002}} khối có chấm điểm.

## Module nào dày nhất
@hinh: toan
@phut: 3.5
@che-do: hinh
@notes: Chỉ vào thanh dài nhất. Dày không có nghĩa là quan trọng nhất, nhưng là chỗ tốn thời gian nhất.

!hinh hinh/day-mong.svg | Số khối **có chấm điểm** của từng module. Thanh dài là chỗ phải để dành nhiều buổi hơn.

## m5.1 Vì sao và khi nào phải đổi
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Với dữ liệu của tôi, bất đẳng thức Mosca (Mosca inequality) đang nói tôi đã trễ hay chưa, và Grover có là lý do để đổi khoá đối xứng không?

## m5.1 · luận điểm
@phut: 1.5
@che-do: noi

Hai đường đe doạ, và chỉ một trong hai là lý do đổi hệ

## m5.2 Lattice: bài toán khó và cách ước lượng độ an toàn
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Câu an toàn {{s003}} bit của một bộ tham số lattice nghĩa là gì, và tính trong mô hình chi phí nào?

## m5.2 · luận điểm
@phut: 1.5
@che-do: noi
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

Con số bit an toàn là con số của một mô hình, không phải của hệ

## m5.3 Chuẩn NIST và kích thước
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Tôi nhớ bằng đầu được bao nhiêu byte cho khoá và chữ ký của từng mức, và tôi gọi tên chuẩn đúng chưa?

## m5.3 · luận điểm
@phut: 1.5
@che-do: noi

Bảng kích thước chính là kiến thức làm việc

## m5.4 Hybrid và giao thức
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Hybrid của tôi ghép khoá theo cách nào, và nếu một nửa bị phá thì tính an toàn còn lại được bảo đảm bởi điều gì?

## m5.4 · luận điểm
@phut: 1.5
@che-do: noi

Hybrid mua tính dự phòng, và nó mua bằng byte

## m5.5 Ràng buộc thiết bị: nơi lý thuyết gặp MTU
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Trên mạng {{s004}}, một bắt tay (handshake) hậu lượng tử của tôi tốn bao nhiêu mảnh, và tỉ lệ mất mảnh làm xác suất hoàn tất bắt tay tụt bao nhiêu?

## m5.5 · luận điểm
@phut: 1.5
@che-do: noi

Byte vào số mũ, vòng thì không

## m5.6 QKD, và cách so sánh công bằng với PQC
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Key rate của tôi theo khoảng cách là bao nhiêu, và khi so với PQC thì tôi đang so trong mô hình đe doạ (threat model) nào?

## m5.6 · luận điểm
@phut: 1.5
@che-do: noi

Hai con số, và một câu hỏi phải trả lời trước khi so

## m5.7 Di trú và cách viết phần mô hình đe doạ
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Trong hệ tôi đang viết, ai giữ khoá nào, trong bao lâu, và tôi đã nói rõ chưa?

## m5.7 · luận điểm
@phut: 1.5
@che-do: noi

Module này là bài tập viết, không phải bài tập mật mã

## m5.8 Kênh bên trong cài đặt
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Cài đặt ML-KEM tôi dùng có chống kênh bên không, và nếu có thì tôi trả giá bao nhiêu lần về thời gian?

## m5.8 · luận điểm
@phut: 1.5
@che-do: noi

Chuẩn nói về lớp một, còn lỗ thường ở lớp ba

## m5.9 Họ không phải lattice
@phut: 1.5
@che-do: hoi
@notes: Câu hỏi của module. Trả lời bằng miệng trước khi lật.

Nếu lattice gãy ngày mai thì tôi còn gì, và bài học từ SIKE nói gì về cách tôi nên viết câu khẳng định độ an toàn?

## m5.9 · luận điểm
@phut: 1.5
@che-do: noi

Nếu lattice gãy ngày mai thì anh còn gì

## Số của trụ
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s005}} | bit, dạng số mũ của {{s006}} | Grover cho tăng tốc bậc căn
!so {{s003}} | bit, dạng số mũ của {{s006}} | Cùng công thức đó
!so {{s007}} | số mũ trên β | Số mũ chi phí core-SVP cổ điển

## Số của trụ (tiếp)
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s008}} | số mũ trên β | Cùng tấn công đó nhưng tính trong mô hình chi phí lượng
!so {{s009}} | byte | Khoá công khai của ML-KEM-768 dài bao nhiêu byte?
!so {{s010}} | byte | Bản mã của ML-KEM-768 dài bao nhiêu byte?

## Số của trụ (tiếp)
@phut: 2.5
@che-do: so
@notes: Ba con số này phải bật ra không cần nghĩ.

!so {{s011}} | byte | Khoá công khai của ML-KEM-512 dài bao nhiêu byte?
!so {{s012}} | byte | Khoá công khai của ML-DSA-65 dài bao nhiêu byte?
!so {{s013}} | byte | Chữ ký của ML-DSA-65 dài bao nhiêu byte? Đây là con số

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để định vị, site để nhớ.

Deck này chỉ là bản đồ của trụ. Chỗ học thật là `https://hoc-5-tru-web.vercel.app/#/tru/5`.
