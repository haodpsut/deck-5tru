---
tieu-de: Chuẩn NIST và kích thước
phu-de: Trụ 5 PQC · module 5.3
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 63
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
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Tôi nhớ bằng đầu được bao nhiêu byte cho khoá và chữ ký của từng mức, và tôi gọi tên chuẩn đúng chưa?

## Bảng kích thước chính là kiến thức làm việc
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Với người làm mạng, PQC là bài toán kích thước và thời gian, không phải bài toán toán học. Bên nào cũng an toàn {{s001}} bit; cái phân biệt là bao nhiêu byte lên dây. Nhớ được vài con số bằng đầu thì ước lượng được ngay một thiết kế có khả thi trên liên kết chật hay không, ngay trong lúc nghe báo cáo hội nghị.

## Bảng kích thước chính là kiến thức làm việc (tiếp)
@phut: 1
@che-do: noi

Hai việc của module này. Thứ nhất, **gọi tên đúng chuẩn**: Kyber thành ML-KEM trong FIPS {{s002}}, Dilithium thành ML-DSA trong FIPS {{s003}}, SPHINCS+ thành SLH-DSA trong FIPS {{s004}}. Thứ hai, và quan trọng hơn: **không có thuật toán tốt nhất, chỉ có tốt nhất theo một tiêu chí đã khai**. Đổi tiêu chí xếp hạng ba lần thì thứ hạng đảo ba lần, và module này dựng đúng ca đó.

## Bảng kích thước chính là kiến thức làm việc (tiếp)
@phut: 1
@che-do: noi

**Cảnh báo về trạng thái số:** mọi con số byte trong module này đang ở trạng thái **chưa xác minh**. Chúng lấy từ đặc tả thiết kế, chưa ai mở FIPS {{s002}} và FIPS {{s003}} ra đối chiếu. Dùng để tập ước lượng thì được; đưa vào bản thảo thì phải mở chuẩn thật trước.

## Tên vòng thi so với tên chuẩn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Tên vòng thi so với tên chuẩn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Kyber thành **ML-KEM** (FIPS {{s002}}). Dilithium thành **ML-DSA** (FIPS {{s003}}). SPHINCS+ thành **SLH-DSA** (FIPS {{s004}}). Hậu tố cũng đổi: Dilithium mức {{s006}} thành ML-DSA-65, Dilithium mức {{s007}} thành ML-DSA-44.

## Tên vòng thi so với tên chuẩn · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đây không phải chuyện văn phong. Bản chuẩn có khác biệt kỹ thuật so với bản dự thi, nên gọi tên vòng thi trong khi viện dẫn chuẩn làm người đọc không biết anh cài đặt bản nào. Trong bài {{s008}} thì phản biện bắt ngay chỗ này, và nó là loại lỗi làm mất uy tín phần cài đặt mà không tốn của họ một phút nào.

## Ba mức tham số, và mức nào là mặc định
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Ba mức tham số, và mức nào là mặc định · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Mỗi họ có ba bộ tham số ứng với ba mức an toàn (security level). Quy tắc chọn thực dụng: **mức {{s006}} (ML-KEM-768, ML-DSA-65) là mặc định hợp lý cho phần lớn giao thức**, mức {{s005}} khi ngân sách byte rất chật, mức {{s009}} khi có yêu cầu riêng.

## Ba mức tham số, và mức nào là mặc định · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: câu mức {{s006}} là mặc định hợp lý khác hẳn câu mức {{s006}} là tốt nhất. Câu đầu là một lựa chọn kỹ thuật có lý do, câu sau là một phát biểu không có nội dung vì nó chưa khai tiêu chí nào.

## Ba họ toán học, ba hình dáng chi phí
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Ba họ toán học, ba hình dáng chi phí · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Lattice phục vụ cả KEM và chữ ký, và nó cân bằng: khoá vừa, chữ ký vừa. Dựa hàm băm (SLH-DSA) cho khoá rất nhỏ nhưng chữ ký rất lớn. Dựa mã (HQC, Classic McEliece) cho khoá công khai rất lớn.

## Ba họ toán học, ba hình dáng chi phí · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: ba hình dáng chi phí đó làm cho **thứ hạng phụ thuộc tiêu chí**. Nếu tiêu chí là khoá công khai thì họ dựa băm thắng; nếu tiêu chí là byte mỗi lần xác thực lại thì nó thua đậm. Đây là lý do một bảng xếp hạng không khai tiêu chí là một bảng không đọc được.

## Ba tiêu chí đếm byte
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Tiêu chí {{s005}}: byte khoá công khai. Tiêu chí {{s007}}: tổng byte một lần bắt tay = khoá công khai KEM + bản mã KEM + n_chứng × (khoá công khai chữ ký + chữ ký). Tiêu chí {{s006}}: byte mỗi lần xác thực lại = byte chữ ký, khi khoá công khai đã có sẵn ở hai bên.`

## Ba tiêu chí đếm byte (tiếp)
@phut: 1
@che-do: so

**Giả thiết nó đứng trên:**

- tiêu chí là lựa chọn của người viết, không phải thuộc tính của thuật toán, nên nó phải nằm trong tiêu đề bảng
- cấu hình (số chữ ký trong chuỗi chứng chỉ, khoá nào đã có sẵn) cố định cho MỌI bộ thuật toán được so, nếu không thì bảng trộn hai cấu hình

## Ba tiêu chí đếm byte (tiếp)
@phut: 1
@che-do: so

- các bộ được so phải ở cùng một mức an toàn, nếu không thì chênh byte không quy được về chênh chi phí ở cùng mức bảo vệ
- chỉ cộng byte thuộc tiêu chí đã khai, không trộn byte của tiêu chí khác vào cùng một cột

## Ba tiêu chí đếm byte · ghi chú
@phut: 1
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.

Ba tiêu chí này dùng đúng cùng một bảng kích thước, nên **không bên nào sai số học**. Chúng vẫn cho ba thứ hạng khác nhau, và đó là nội dung thật của module. Hệ quả cho cách viết: khai tiêu chí trong chính tiêu đề bảng, rồi báo luôn kết quả phép kiểm thứ hạng có bền khi đổi tiêu chí hay không. Thứ hạng không bền là một kết quả phải báo, không phải một chi tiết nên giấu.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s010}} | byte | Khoá công khai của ML-KEM-768 dài bao nhiêu byte?
!so {{s011}} | byte | Bản mã của ML-KEM-768 dài bao nhiêu byte?
!so {{s012}} | byte | Khoá công khai của ML-KEM-512 dài bao nhiêu byte?

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s013}} | byte | Khoá công khai của ML-DSA-65 dài bao nhiêu byte?
!so {{s014}} | byte | Chữ ký của ML-DSA-65 dài bao nhiêu byte? Đây là con số
!so {{s015}} | byte | Chữ ký của ML-DSA-44 dài bao nhiêu byte?

## Chữ ký ML-DSA-65 so với chữ ký ECDSA P-256
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Chữ ký ML-DSA-65 so với chữ ký ECDSA P-256: lớn hơn bao nhiêu lần?

sigPQ = {{s014}}, sigCL = {{s016}}

## Chữ ký ML-DSA-65 so với chữ ký ECDSA P-256 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`sigPQ / sigCL`

Khoảng {{s017}} lần, tức làm tròn là khoảng {{s018}} lần. Đây là tỉ số của RIÊNG chữ ký, đúng theo tiêu chí byte mỗi lần xác thực lại khi khoá công khai đã có sẵn ở hai bên. Nó không trả lời được câu hậu lượng tử đắt hơn bao nhiêu lần một cách chung chung: theo tiêu chí tổng byte một lần bắt tay (handshake) thì tỉ số tụt xuống khoảng {{s019}} lần.

## Chữ ký ML-DSA-65 so với chữ ký ECDSA P-256 · đáp (tiếp)
@phut: 1
@che-do: noi

Hai hạng tử của phép chia này đang ở trạng thái chưa xác minh.

## Đổi tiêu chí
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Đổi tiêu chí: đếm tổng byte một lần bắt tay với chuỗi chứng chỉ chỉ có một chữ ký. Bên hậu lượng tử gồm khoá công khai và bản mã của ML-KEM-768 cộng khoá công khai và chữ ký của ML-DSA-65; bên cổ điển gồm hai phần chia khoá X25519 cộng khoá công khai và chữ ký ECDSA P-256. Tỉ số bằng bao nhiêu lần?

## Đổi tiêu chí (tiếp)
@phut: 0.5
@che-do: hoi

pkKem = {{s010}}, ctKem = {{s011}}, pkSig = {{s013}}, sig = {{s014}}, shareA = {{s020}}, shareB = {{s020}}, pkCl = {{s016}}, sigCl = {{s016}}

## Đổi tiêu chí · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(pkKem + ctKem + pkSig + sig) / (shareA + shareB + pkCl + sigCl)`

Khoảng {{s019}} lần, tức THẤP HƠN tỉ số {{s017}} lần của riêng chữ ký. Cùng một bảng kích thước, cùng một bộ thuật toán, hai tiêu chí, hai con số, và không bên nào sai số học. Bài học áp vào cách viết:

## Đổi tiêu chí · đáp (tiếp)
@phut: 1
@che-do: noi

mọi câu dạng hậu lượng tử tốn khoảng N lần byte phải kèm tiêu chí ngay trong câu, nếu không thì phản biện đưa ra một tiêu chí hợp lệ khác và con số N của anh thành con số của một tiêu chí anh chưa khai. Mọi hạng tử ở đây đang ở trạng thái chưa xác minh.

## Trong một bài báo năm 2026
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong một bài báo năm {{s008}}, tên chuẩn của Dilithium là gì?

- Tên không đổi, Dilithium vẫn là tên chuẩn
- ML-KEM, trong FIPS {{s002}}
- ML-DSA, trong FIPS {{s003}}
- SLH-DSA, trong FIPS {{s004}}

## Trong một bài báo năm 2026 · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**ML-DSA, trong FIPS {{s003}}**

Dilithium thành ML-DSA trong FIPS {{s003}}, và hậu tố cũng đổi: Dilithium mức {{s006}} thành ML-DSA-65. ML-KEM là tên chuẩn của Kyber trong FIPS {{s002}}, SLH-DSA là tên chuẩn của SPHINCS+ trong FIPS {{s004}}. Đây không phải chuyện văn phong: bản chuẩn có khác biệt kỹ thuật so với bản dự thi, nên gọi tên vòng thi làm người đọc không biết anh cài đặt bản nào.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Khi nào câu thuật toán X tiết kiệm byte hơn thuật toán Y mới có nội dung kiểm được?

- Chỉ khi hai thuật toán cùng một họ toán học
- Chỉ khi hai thuật toán đo trên cùng một bộ vi điều khiển
- Luôn có nội dung, vì kích thước byte là đại lượng khách quan
- Chỉ sau khi khai tiêu chí đếm byte và cấu hình, vì ba tiêu chí thường dùng cho ba thứ hạng khác nhau

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chỉ sau khi khai tiêu chí đếm byte và cấu hình, vì ba tiêu chí thường dùng cho ba thứ hạng khác nhau**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Byte là khách quan, nhưng tiêu chí đếm byte là một lựa chọn. Cùng bảng kích thước cho {{s021}} lần theo khoá công khai, khoảng {{s019}} lần theo tổng byte một lần bắt tay, và {{s022}} lần theo byte mỗi lần xác thực lại. Cùng họ toán học hay cùng vi điều khiển đều không cứu được: hai bộ cùng họ lattice vẫn đảo thứ hạng khi đổi tiêu chí.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả cấu hình sau có một câu phản biện bắt ngay. Bấm vào câu đó.

- Chúng tôi dùng Kyber-768 cho trao đổi khoá và Dilithium-3 cho chữ ký, theo chuẩn do NIST ban hành.
- Khoá công khai và bản mã đi trong bản tin bắt tay của giao thức.
- Kích thước các tham số lấy từ bảng kích thước trong văn bản chuẩn tương ứng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Chúng tôi dùng Kyber-768 cho trao đổi khoá và Dilithium-3 cho chữ ký, theo chuẩn do NIST ban hành.**

Câu này gọi tên vòng thi ngay chỗ phải gọi tên chuẩn. Kyber thành ML-KEM trong FIPS {{s002}}, Dilithium thành ML-DSA trong FIPS {{s003}}, SPHINCS+ thành SLH-DSA trong FIPS {{s004}}, và hậu tố cũng đổi: Dilithium mức {{s006}} thành ML-DSA-65.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Nửa sau của câu làm lỗi nặng hơn, vì nó viện dẫn chuẩn trong khi gọi tên bản dự thi, mà bản chuẩn có khác biệt kỹ thuật so với bản dự thi; người đọc không biết anh cài đặt bản nào, nên phần cài đặt mất uy tín mà phản biện không tốn một phút. Cách sửa: viết ML-KEM-768 và ML-DSA-65 ở mọi chỗ, và nếu cần nhắc tên cũ thì để trong ngoặc đúng một lần ở lần xuất hiện đầu.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết luận sau có một câu nhảy tiêu chí giữa dòng. Bấm vào câu đó.

- Bảng VI xếp hạng các bộ thuật toán theo kích thước khoá công khai.
- ML-KEM-768 có khoá công khai {{s010}} byte, nhỏ hơn {{s013}} byte của ML-DSA-65.
- Vì thế ML-KEM-768 là lựa chọn tiết kiệm byte nhất cho bắt tay của chúng tôi.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì thế ML-KEM-768 là lựa chọn tiết kiệm byte nhất cho bắt tay của chúng tôi.**

Hai câu đầu đều đúng và đều hợp lệ. Câu này đổi tiêu chí giữa dòng: bảng xếp theo khoá công khai, còn kết luận nói về byte của cả lần bắt tay, và hai tiêu chí cho hai thứ hạng.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Theo tổng byte một lần bắt tay với chuỗi hai chữ ký, bộ hậu lượng tử tốn {{s023}} byte so với {{s024}} byte của bộ cổ điển, tức {{s025}} lần; theo byte của riêng chữ ký thì tỉ số là {{s014}} trên {{s016}}, tức {{s022}} lần. Thêm một lỗi nữa: một KEM và một lược đồ chữ ký làm hai việc khác nhau nên chúng không nằm cùng một bảng xếp hạng, bỏ KEM đi thì không còn bắt tay. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

khai tiêu chí ngay trong tiêu đề bảng, in cả ba cột tiêu chí, và viết kết luận theo đúng cột mình dùng.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Khai tiêu chí: byte nào được đếm, và đếm một lần hay đếm mỗi lần xác thực lại
- Khai cấu hình: số chữ ký trong chuỗi chứng chỉ, và khoá nào đã có sẵn ở hai bên
- Tra bảng kích thước trong văn bản chuẩn cho từng bộ tham số, chỉ lấy các bộ ở cùng mức an toàn
- Cộng byte theo đúng tiêu chí đã khai ở bước một

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Xếp hạng, rồi lặp lại từ bước một với một tiêu chí khác và xem thứ hạng có bền hay không

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Chuỗi {{s007}} chữ ký · {{s005}} lần xác thực lại · bắt tay hậu lượng tử {{s023}} byte, cổ điển {{s024}} byte · tỉ số theo tổng byte bắt tay {{s025}} lần · tỉ số theo byte mỗi lần xác thực lại {{s022}} lần

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Tiêu chí xếp hạng đã khai, và nó là kích thước khoá công khai** tắt đi: Bảng không khai tiêu chí, hoặc tiêu chí đổi giữa bảng và kết luận.
- **Chuỗi chứng chỉ chỉ có một chữ ký** tắt đi: Chuỗi dài hơn, mỗi mắt thêm một khoá công khai và một chữ ký.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Khoá công khai của hai bên đã có sẵn, không gửi lại ở mỗi lần xác thực lại** tắt đi: Mỗi lần xác thực lại phải gửi lại cả khoá công khai chữ ký.
- **Mọi bộ tham số trong bảng ở cùng một mức an toàn** tắt đi: Bảng trộn mức, ví dụ xếp ML-KEM-512 cạnh ML-DSA-65.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Một bảng kích thước duy nhất, ba tiêu chí đếm byte. Kéo số chữ ký trong chuỗi và số lần xác thực lại, rồi xem tỉ số hậu lượng tử trên cổ điển chạy giữa ba con số khác nhau. Mọi byte trong mô phỏng này đang ở trạng thái chưa xác minh.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.3` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table VI ranks the candidate algorithm suites and the text concludes that the chosen suite is the most byte-efficient option. The ranking criterion is never stated, and the conclusion appears to use a different criterion from the one tabulated. Please state the criterion and show whether the ranking is stable under reasonable alternatives.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have rewritten Table VI and the surrounding text. The table caption now names the criterion explicitly, and the table reports three criteria side by side rather than one: public key bytes, total bytes of a single handshake, and bytes per re-authentication. The configuration used for the last two is stated in the caption (certificate chain length, and whether public keys are cached between re-authentications), and it is identical for every row.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The ranking is not stable, and we now say so rather than hide it: for our suite the post-quantum to classical byte ratio is about {{s021}} under the public key criterion, about {{s026}} under the single handshake criterion with a one-signature chain, and about {{s027}} under the per-re-authentication criterion. We therefore removed the sentence claiming a most byte-efficient option and replaced it with a statement tied to one criterion and one configuration.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Section VII-A now states which of our conclusions depend on the ranking (only the suite recommendation in VII-C) and which do not (the fragmentation result in Section VI, which depends on absolute byte counts, not on the ordering).

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Every byte count in the table now carries a citation to the specific size table of FIPS {{s002}} or FIPS {{s003}}, and we removed two rows that mixed security levels, since a difference in bytes between rows at different levels also contains a difference in protection and cannot be read off one column.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s005}}: thêm một câu nói bảng xếp theo kích thước khoá công khai. Đã khai tiêu chí nhưng chưa sửa chỗ kết luận dùng tiêu chí khác, nên phản bác vẫn đứng.
- Mức {{s007}}: khai tiêu chí trong tiêu đề bảng và viết lại kết luận theo đúng tiêu chí đó. Đã nhất quán, nhưng chưa cho người đọc thấy thứ hạng có bền hay không.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s006}}: in cả ba tiêu chí thành ba cột (khoá công khai, tổng byte một lần bắt tay, byte mỗi lần xác thực lại), khai cấu hình dùng để tính cột hai và cột ba, và chỉ ra thứ hạng đổi ở đâu.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.3` bấm thẻ.
