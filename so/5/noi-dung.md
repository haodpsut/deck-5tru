---
tieu-de: Số phải dẫn lại được trong *ba mươi giây*
phu-de: Trụ 5 PQC · số, công thức, và giả thiết của chúng
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
@phan: PQC
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

`Đã trễ khi x + y > z Grover: số truy vấn bậc 2^(n/2) cho khoá đối xứng n bit Dạng điều kiện: đã trễ với mọi z nhỏ hơn (x + y)`

## Giả thiết
@phut: 0.5
@che-do: so

- x đo bằng nghĩa vụ bảo mật của dữ liệu, không bằng vòng đời thiết bị
- y là thời gian di trú xong toàn bộ nơi dùng mật mã, kể cả hệ đã bàn giao, nên nó đo được bằng kiểm kê chứ không ước bằng cảm tính
- z là ước lượng về thế giới bên ngoài, nên nó mang độ bất định và kết luận phải viết ở dạng điều kiện theo z

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- Grover giả thiết truy cập hộp đen tới hàm kiểm khoá, và số truy vấn bậc căn là tối ưu, nên không có cải tiến thuật toán nào đẩy nó xuống thấp hơn
- Tăng tốc của Grover tuần tự theo bản chất: chia việc cho M máy chỉ được lợi theo căn của M

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Grover cho tăng tốc bậc căn, nên tìm khoá đối xứng n bit mất bậc {{s001}} luỹ thừa (n/2) truy vấn. Với AES-128, số mũ đó bằng bao nhiêu? Nhập số mũ.

*Module {{s002}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s003}} | bit, dạng số mũ của {{s001}} | module {{s002}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng công thức đó, với AES-256 thì số mũ bằng bao nhiêu? Nhập số mũ.

*Module {{s002}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s004}} | bit, dạng số mũ của {{s001}} | module {{s002}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Hồ sơ bệnh án phải giữ mật x = {{s005}} năm. Kế hoạch di trú của anh dài y = {{s006}} năm. Anh dùng ước lượng z = {{s007}} năm. Chênh Mosca bằng bao nhiêu năm?

x = {{s005}}, y = {{s006}}, z = {{s007}}

## Đáp
@phut: 0.5
@che-do: so

`x + y - z`

{{s008}} năm, dương và lớn, tức đã trễ {{s008}} năm theo ước lượng này. Để ý điều quan trọng hơn con số: x + y = {{s009}}, nên dấu của chênh giữ nguyên với mọi z nhỏ hơn {{s009}} năm. Vì thế phát biểu nên viết là đã trễ với mọi z nhỏ hơn {{s009}} năm, và lúc đó nó không cần tới ước lượng z = {{s007}} nữa.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Vẫn z = {{s007}} năm và y = {{s006}} năm, lấy mốc hiện tại là {{s010}}. Năm muộn nhất phải bắt đầu di trú là năm nào?

z = {{s007}}, y = {{s006}}

## Đáp
@phut: 0.5
@che-do: so

`{{s010}} + z - y`

Năm {{s011}}. Nhưng con số này chỉ nói về việc kịp trước z, nó không chứa x. Với x = {{s005}} thì chênh Mosca đã dương {{s008}} năm, nên {{s011}} là một mốc muộn tới mức vô nghĩa: bản mã thu hoạch hôm nay đã nằm ngoài tầm bảo vệ từ trước. Hai con số này phải đọc cùng nhau, và chỉ chênh Mosca mới trả lời được câu đã trễ hay chưa.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Tìm s từ (A, b = A·s + e mod q), với e nhỏ. Nhiễu bằng {{s012}} ⇒ khử Gauss ra s ngay. Độ khó điều khiển bởi tỉ số (độ lớn nhiễu / q).`

## Giả thiết
@phut: 0.5
@che-do: so

- A sinh đều và công khai, nên độ khó không dựa vào việc giấu A
- e lấy từ một phân bố đã khai, thường là phân bố nhị thức tâm hoặc Gauss rời rạc, và phân bố đó phải nằm trong đặc tả chứ không phải trong cài đặt
- kẻ tấn công có nhiều mẫu LWE tuỳ ý trong giới hạn của giao thức, nên số mẫu là một tham số của bài toán

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- với MLWE: giả định không có tấn công nào khai thác được cấu trúc vành tốt hơn tấn công trên lưới không cấu trúc

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Chi phí cổ điển ≈ 2^(0,292 · β) Chi phí lượng tử ≈ 2^(0,265 · β) Suy ra: β cần cho λ bit cổ điển = λ / {{s013}}`

## Giả thiết
@phut: 0.5
@che-do: so

- bỏ hết hệ số đa thức, nên đây là chặn dưới lạc quan cho kẻ tấn công và bảo thủ cho người thiết kế
- đếm đúng một lần gọi lời giải SVP trên khối kích thước β, trong khi BKZ thật gọi rất nhiều lần
- bộ nhớ của kẻ tấn công không bị tính phí, kể cả phí truy cập ngẫu nhiên vào bộ nhớ lớn

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- β lấy từ một bộ ước lượng ở một phiên bản cố định, và phiên bản đó phải khai trong bài

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Số mũ chi phí core-SVP cổ điển: chi phí tấn công bậc {{s001}} luỹ thừa (số mũ nhân β). Số mũ đó bằng bao nhiêu?

*Module {{s014}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s015}} | số mũ trên β | module {{s014}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng tấn công đó nhưng tính trong mô hình chi phí lượng tử của core-SVP. Số mũ bằng bao nhiêu?

*Module {{s014}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s016}} | số mũ trên β | module {{s014}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Trong mô hình core-SVP cổ điển, kích thước khối BKZ cần thiết để đạt {{s004}} bit an toàn là bao nhiêu?

lam = {{s004}}, ec = {{s015}}

## Đáp
@phut: 0.5
@che-do: so

`lam / ec`

Khoảng {{s017}}, tức β khoảng {{s018}}. Phép chia này là toàn bộ nội dung của câu an toàn {{s004}} bit trong mô hình core-SVP cổ điển: lấy mức mục tiêu chia cho số mũ. Vì nó chỉ là một phép chia, mọi độ bất định của con số {{s004}} bit nằm ở hai chỗ khác: ở việc số mũ {{s013}} có đúng không, và ở việc bộ ước lượng trả về β nào cho bộ tham số của anh.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Lấy đúng bộ tham số vừa chọn để đạt {{s004}} bit cổ điển, tức β bằng {{s004}} chia {{s013}}. Trong mô hình core-SVP lượng tử, bộ tham số đó đạt bao nhiêu bit?

eq = {{s016}}, lam = {{s004}}, ec = {{s015}}

## Đáp
@phut: 0.5
@che-do: so

`eq × (lam / ec)`

Khoảng {{s019}} bit, tức THẤP HƠN {{s004}} bit chứ không bằng. Cùng một bộ tham số, hai con số khác nhau, và khoảng cách gần {{s020}} bit. Đây là lý do một bảng bộ tham số phải có hai cột chứ không một cột, và là lý do câu bộ tham số của chúng tôi an toàn {{s004}} bit phải nói rõ {{s004}} bit trong mô hình nào.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Tiêu chí {{s021}}: byte khoá công khai. Tiêu chí {{s001}}: tổng byte một lần bắt tay = khoá công khai KEM + bản mã KEM + n_chứng × (khoá công khai chữ ký + chữ ký). Tiêu chí {{s022}}: byte mỗi lần xác thực lại = byte chữ ký, khi khoá công khai đã có sẵn ở hai bên.`

## Giả thiết
@phut: 0.5
@che-do: so

- tiêu chí là lựa chọn của người viết, không phải thuộc tính của thuật toán, nên nó phải nằm trong tiêu đề bảng
- cấu hình (số chữ ký trong chuỗi chứng chỉ, khoá nào đã có sẵn) cố định cho MỌI bộ thuật toán được so, nếu không thì bảng trộn hai cấu hình

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- các bộ được so phải ở cùng một mức an toàn, nếu không thì chênh byte không quy được về chênh chi phí ở cùng mức bảo vệ
- chỉ cộng byte thuộc tiêu chí đã khai, không trộn byte của tiêu chí khác vào cùng một cột

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khoá công khai của ML-KEM-768 dài bao nhiêu byte?

*Module {{s023}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s024}} | byte | module {{s023}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Bản mã của ML-KEM-768 dài bao nhiêu byte?

*Module {{s023}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s025}} | byte | module {{s023}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khoá công khai của ML-KEM-512 dài bao nhiêu byte?

*Module {{s023}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s026}} | byte | module {{s023}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khoá công khai của ML-DSA-65 dài bao nhiêu byte?

*Module {{s023}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s027}} | byte | module {{s023}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Chữ ký của ML-DSA-65 dài bao nhiêu byte? Đây là con số đáng nhớ nhất của cả trụ.

*Module {{s023}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s028}} | byte | module {{s023}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Chữ ký của ML-DSA-44 dài bao nhiêu byte?

*Module {{s023}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s029}} | byte | module {{s023}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Chữ ký ML-DSA-65 so với chữ ký ECDSA P-256: lớn hơn bao nhiêu lần?

sigPQ = {{s028}}, sigCL = {{s003}}

## Đáp
@phut: 0.5
@che-do: so

`sigPQ / sigCL`

Khoảng {{s030}} lần, tức làm tròn là khoảng {{s031}} lần. Đây là tỉ số của RIÊNG chữ ký, đúng theo tiêu chí byte mỗi lần xác thực lại khi khoá công khai đã có sẵn ở hai bên. Nó không trả lời được câu hậu lượng tử đắt hơn bao nhiêu lần một cách chung chung: theo tiêu chí tổng byte một lần bắt tay thì tỉ số tụt xuống khoảng {{s032}} lần.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Hai hạng tử của phép chia này đang ở trạng thái chưa xác minh.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Đổi tiêu chí: đếm tổng byte một lần bắt tay với chuỗi chứng chỉ chỉ có một chữ ký. Bên hậu lượng tử gồm khoá công khai và bản mã của ML-KEM-768 cộng khoá công khai và chữ ký của ML-DSA-65; bên cổ điển gồm hai phần chia khoá X25519 cộng khoá công khai và chữ ký ECDSA P-256. Tỉ số bằng bao nhiêu lần?

## Tính ra con số (tiếp)
@phut: 0.5
@che-do: hoi

pkKem = {{s024}}, ctKem = {{s025}}, pkSig = {{s027}}, sig = {{s028}}, shareA = {{s033}}, shareB = {{s033}}, pkCl = {{s003}}, sigCl = {{s003}}

## Đáp
@phut: 0.5
@che-do: so

`(pkKem + ctKem + pkSig + sig) / (shareA + shareB + pkCl + sigCl)`

Khoảng {{s032}} lần, tức THẤP HƠN tỉ số {{s030}} lần của riêng chữ ký. Cùng một bảng kích thước, cùng một bộ thuật toán, hai tiêu chí, hai con số, và không bên nào sai số học. Bài học áp vào cách viết:

## Đáp (tiếp)
@phut: 0.5
@che-do: so

mọi câu dạng hậu lượng tử tốn khoảng N lần byte phải kèm tiêu chí ngay trong câu, nếu không thì phản biện đưa ra một tiêu chí hợp lệ khác và con số N của anh thành con số của một tiêu chí anh chưa khai. Mọi hạng tử ở đây đang ở trạng thái chưa xác minh.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`Tính chất bộ tổ hợp: khoá dẫn xuất an toàn miễn ÍT NHẤT MỘT bí mật thành phần còn an toàn. Byte phía khách = byte cổ điển + byte khoá công khai hậu lượng tử. Byte phía chủ = byte cổ điển + byte bản mã hậu lượng tử. Số mảnh = làm tròn lên của (tổng byte chiều đó / tải khả dụng mỗi mảnh).`

## Giả thiết
@phut: 0.5
@che-do: so

- bộ tổ hợp có tính chất an toàn miễn ít nhất một thành phần còn an toàn, và tính chất đó phải được chứng minh hoặc dẫn, chứ không suy ra từ việc có hai thành phần
- cả hai bí mật đều vào hàm dẫn xuất khoá của giao thức, không bí mật nào bị cắt bỏ ở khâu nào trong chuỗi dẫn xuất

## Giả thiết (tiếp)
@phut: 0.5
@che-do: so

- hai chiều không đối xứng: phía khách gửi khoá công khai, phía chủ gửi bản mã, nên byte hai chiều khác nhau
- tải khả dụng mỗi mảnh đã trừ tiêu đề và phần bảo mật của tầng dưới, và không có cơ chế nào gộp hai bản tin vào một mảnh

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

EDHOC cần bao nhiêu bản tin BẮT BUỘC để thiết lập khoá?

*Module {{s034}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s022}} | bản tin bắt buộc | module {{s034}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Phần chia khoá của X25519 dài bao nhiêu byte?

*Module {{s034}}.*

## Đáp
@phut: 0.5
@che-do: so

!so {{s033}} | byte | module {{s034}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Trong hybrid, phía chủ gửi bản mã của ML-KEM-768. Bản mã đó dài bao nhiêu byte?

*Module {{s034}}.*

## Đáp
@phut: 0.5
@che-do: so
@wow
@dan: Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số.

!so {{s025}} | byte | module {{s034}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Hybrid X25519 cộng ML-KEM-768. Phía khách gửi phần chia khoá cổ điển cộng khoá công khai hậu lượng tử. Tổng bao nhiêu byte?

cl = {{s033}}, pqk = {{s024}}

## Đáp
@phut: 0.5
@che-do: so

`cl + pqk`

## Đáp (tiếp)
@phut: 0.5
@che-do: so

{{s035}} byte. Đây là một trong hai con số nên nhớ bằng đầu của module, vì nó cho ước lượng ngay trong lúc nghe báo cáo: ở một liên kết có tải khả dụng khoảng một trăm byte mỗi mảnh thì nó thành {{s036}} mảnh. Để ý phép cộng này chỉ gồm hai hạng tử vì đây là phần chia khoá, chưa có chữ ký nào; thêm xác thực hậu lượng tử là một quyết định riêng và nó cộng tiếp vào.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Cả hai hạng tử đang ở trạng thái chưa xác minh.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Cùng bộ thuật toán đó, nhưng phía chủ: phần chia khoá cổ điển cộng bản mã hậu lượng tử. Tổng bao nhiêu byte?

cl = {{s033}}, pqs = {{s025}}

## Đáp
@phut: 0.5
@che-do: so

`cl + pqs`

{{s037}} byte, tức nhỏ hơn phía khách {{s038}} byte. Hai chiều không đối xứng vì trong một KEM phía khách gửi khoá công khai còn phía chủ gửi bản mã. Chênh {{s038}} byte nghe nhỏ, nhưng ở tải khả dụng khoảng một trăm byte mỗi mảnh thì nó đúng bằng một mảnh, và số mảnh vào số mũ của xác suất hoàn tất bắt tay. Vì thế bảng byte phải tách theo chiều, đừng gộp một con số cho cả hai.

## Đáp (tiếp)
@phut: 0.5
@che-do: so

Cả hai hạng tử đang ở trạng thái chưa xác minh.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`n_mảnh = ceil(B / W) P_hoàn_tất = ({{s021}} − p)^(v · n_mảnh) số lần thử trung bình = {{s021}} / P_hoàn_tất`

## Giả thiết
@phut: 0.5
@che-do: so

- W là tải khả dụng cho tầng trên sau mọi tiêu đề, và là hằng số với mọi mảnh của cùng một bản tin
- mỗi mảnh mất độc lập với xác suất p, không có tương quan thời gian và không có mất theo chùm
- không có truyền lại ở lớp liên kết, nên mất một mảnh là mất cả bản tin
- v vòng trao đổi đều phải hoàn tất, và mỗi vòng mang đúng B byte

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Gói lớn nhất ở TẦNG VẬT LÝ của {{s039}} (aMaxPHYPacketSize) là bao nhiêu byte?

*Module {{s040}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s041}} | B | module {{s040}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Phần chia khoá hybrid phía khách là {{s035}} byte, tải khả dụng {{s042}} byte mỗi mảnh. Bao nhiêu mảnh?

*Module {{s040}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s036}} | mảnh | module {{s040}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

{{s036}} mảnh, mỗi mảnh mất độc lập với xác suất {{s043}}, không truyền lại. Xác suất bản tin tới đủ là bao nhiêu phần trăm?

*Module {{s040}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s044}} | % | module {{s040}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cũng p = {{s043}}, nhưng bản tin chỉ còn {{s001}} mảnh. Xác suất tới đủ là bao nhiêu phần trăm?

*Module {{s040}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s045}} | % | module {{s040}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Cùng {{s035}} byte, nhưng cấu hình bảo mật nặng hơn nên tải khả dụng chỉ còn {{s046}} byte mỗi mảnh. Số mảnh là bao nhiêu?

byte = {{s035}}, tai = {{s046}}

## Đáp
@phut: 1
@che-do: so

`Math.ceil(byte/tai)`

{{s047}} mảnh. Tải khả dụng tụt {{s007}} phần trăm mà số mảnh tăng từ {{s036}} lên {{s047}}, tức thêm đúng {{s022}} mảnh. Ba mảnh đó không là thêm {{s048}} phần trăm chi phí: chúng vào số mũ, nên xác suất hoàn tất bị nhân thêm {{s049}} ba lần nữa, tức nhân {{s050}}.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

{{s047}} mảnh, p = {{s043}}, không truyền lại. Xác suất bản tin tới đủ là bao nhiêu phần trăm?

p = {{s051}}, n = {{s047}}

## Đáp
@phut: 1
@che-do: so

`100⋆Math.pow(1-p, n)`

Khoảng {{s052}} phần trăm, tức dưới một nửa. So với {{s053}} phần trăm ở {{s036}} mảnh thì ba mảnh thêm lấy đi hơn {{s006}} điểm phần trăm. Đây là lý do con số tải khả dụng phải khai trong bài: đổi một dòng cấu hình bảo mật là đổi kết quả đánh giá.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Giao thức có {{s001}} vòng, mỗi chiều {{s035}} byte, tải khả dụng {{s042}} byte, p = {{s043}}. Nén được {{s054}} byte khỏi mỗi chiều mà giữ nguyên số vòng thì xác suất hoàn tất cả bắt tay tăng bao nhiêu điểm phần trăm?

p = {{s051}}, v = {{s001}}, byte = {{s035}}, tai = {{s042}}, giam = {{s054}}

## Đáp
@phut: 1
@che-do: so

`100⋆(Math.pow(1-p, v⋆Math.ceil((byte-giam)/tai)) - Math.pow(1-p, v⋆Math.ceil(byte/tai)))`

Khoảng {{s055}} điểm phần trăm, từ {{s056}} lên {{s057}} phần trăm. Cùng phép nén {{s054}} byte đó, nếu giao thức chỉ có một vòng thì chỉ được khoảng {{s058}} điểm. Đây là nội dung thật của câu bài học: byte được nhân với số vòng trong số mũ, nên mỗi byte cắt đi được trả công ở MỌI vòng, trong khi số vòng thì giao thức đã khoá và anh không có quyền cắt.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`η = 10^(−αL/10) C_PLOB = −log₂(1−η) ≈ 1,44·η R_BB84 = q·[1 − 2·h₂(e)] số lần dùng kênh cho K bit = K / C`

## Giả thiết
@phut: 1
@che-do: so

- α là suy hao trên một km và không đổi theo chiều dài, tức sợi đồng nhất, không mối hàn, không đầu nối
- chặn PLOB áp cho kênh hai điểm KHÔNG có bộ lặp lượng tử và KHÔNG có node trung gian tin cậy
- R_BB84 ở dạng này là key rate tiệm cận, tức độ dài khối tiến tới vô hạn, chưa trừ thống kê khối hữu hạn

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- q là hệ số sàng lọc của giao thức, thường {{s059}} cho BB84 chọn cơ sở đều, nên bỏ q là tự nhân đôi kết quả
- e là sai bit lượng tử đã đo, và h₂ là entropy nhị phân tính theo bit

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Sợi G.652.D bán ngoài thị trường bảo đảm suy hao tối đa bao nhiêu dB mỗi km ở {{s060}} nm? Lấy theo tờ thông tin sản phẩm, không lấy theo trần của chuẩn.

*Module {{s061}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s062}} | dB mỗi km | module {{s061}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Sợi đơn mode {{s060}} nm với suy hao chuẩn, chiều dài L = {{s042}} km. Hiệu suất kênh η bằng {{s063}} luỹ thừa âm mấy? Nhập số mũ dương.

*Module {{s061}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s001}} | số mũ âm của {{s063}} | module {{s061}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Ở η = {{s064}}, chặn PLOB cho dung lượng khoá bí mật là bao nhiêu bit mỗi lần dùng kênh?

*Module {{s061}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s065}} | bit mỗi lần dùng kênh | module {{s061}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Cùng loại sợi đó, chiều dài L = {{s066}} km. Hiệu suất kênh η bằng {{s063}} luỹ thừa âm mấy? Nhập số mũ dương.

*Module {{s061}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s067}} | số mũ âm của {{s063}} | module {{s061}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

BB84 một chiều với key rate R = {{s021}} trừ hai lần entropy nhị phân của sai bit. Sai bit vượt ngưỡng nào, tính theo phần trăm, thì R về 0?

*Module {{s061}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s068}} | % | module {{s061}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Sợi {{s071}} dB mỗi km, chiều dài {{s070}} km. Chặn PLOB là bao nhiêu bit mỗi lần dùng kênh?

alpha = {{s069}}, L = {{s070}}

## Đáp
@phut: 1
@che-do: so

`-Math.log2(1 - Math.pow(10, -alpha⋆L/10))`

Khoảng {{s072}} bit mỗi lần dùng kênh. Để ý quan hệ với mốc {{s042}} km: thêm {{s073}} km làm chặn này mất đúng một bậc độ lớn, từ bậc {{s074}} xuống bậc {{s075}}. Và xấp xỉ {{s076}} nhân η đúng tới ba chữ số ở đây, vì η = 10⁻³ đã nhỏ.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Sợi {{s071}} dB mỗi km, {{s078}} km. Theo chặn PLOB, cần ít nhất bao nhiêu lần dùng kênh để sinh một khoá {{s077}} bit?

bit = {{s077}}, alpha = {{s069}}, L = {{s078}}

## Đáp
@phut: 1
@che-do: so

`bit / (-Math.log2(1 - Math.pow(10, -alpha⋆L/10)))`

Khoảng {{s079}} triệu lần dùng kênh. Chiều của con số này là chỗ dễ sai nhất: PLOB là chặn TRÊN của khoá mỗi lần dùng kênh, nên số lần dùng kênh suy ra từ nó là chặn DƯỚI. Hệ thật luôn cần nhiều hơn, thường nhiều hơn vài bậc, vì còn hiệu suất bộ tách, tỉ lệ sàng lọc, sửa lỗi và phạt khối hữu hạn.

## Đáp (tiếp)
@phut: 1
@che-do: so

Viết con số này vào bài kèm chữ ít nhất thì nó là một tuyên bố mạnh; viết kèm chữ chúng tôi cần thì nó là một tuyên bố sai.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`đã trễ khi x + y > z năm muộn nhất phải bắt đầu = năm nay + z − y − x số năm dữ liệu gửi hôm nay bị lộ = max(0, x + y − z)`

## Giả thiết
@phut: 1
@che-do: so

- x là số năm dữ liệu gửi HÔM NAY còn cần giữ mật, và nó đến từ dòng năm của mô hình đe doạ, không từ phỏng đoán
- y là số năm di trú thật của hệ, gồm cả kiểm kê, thử nghiệm, cập nhật thiết bị ngoài hiện trường và thời gian sống của lô thiết bị cũ

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- z là số năm cho tới khi kẻ tấn công có máy lượng tử đủ sức, và nó là ƯỚC LƯỢNG, nên mọi kết luận phải viết ở dạng điều kiện theo z
- mô hình đe doạ có thu hoạch bây giờ giải mã sau, tức kẻ tấn công lưu được bản mã hôm nay và giải mã khi có máy

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Khuôn mô hình đe doạ của module này có bao nhiêu dòng bắt buộc?

*Module {{s080}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s067}} | dòng | module {{s080}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Phép đo y tế phải giữ mật {{s007}} năm, di trú lô thiết bị mất {{s081}} năm, ước lượng cho tới khi có máy lượng tử đủ sức là {{s020}} năm. Theo Mosca, đã trễ bao nhiêu năm?

x = {{s007}}, y = {{s081}}, z = {{s020}}

## Đáp
@phut: 1
@che-do: so

`x + y - z`

Trễ {{s036}} năm, tức lẽ ra phải bắt đầu di trú từ {{s082}}. Chú ý chiều của kết luận: con số dương nghĩa là dữ liệu gửi HÔM NAY sẽ còn cần giữ mật trong {{s036}} năm sau khi kẻ tấn công đã có máy, nên nó không nói về thiết bị tương lai mà nói về dữ liệu đang chạy trên dây lúc này. Và chú ý thứ hai:

## Đáp (tiếp)
@phut: 1
@che-do: so

{{s036}} năm này nhạy với z, đổi z sang {{s007}} năm thì độ trễ về {{s081}} năm, nên câu kết luận trong bài phải viết theo dải z.

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Chữ ký của ML-DSA-65 dài bao nhiêu byte?

*Module {{s080}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s028}} | B | module {{s080}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Kiểm kê cho thấy mỗi bản cập nhật firmware mang một chữ ký. Đổi từ ECDSA P-256 ({{s003}} byte) sang ML-DSA-65 ({{s028}} byte) thì byte chữ ký tăng bao nhiêu lần?

mlDsa = {{s028}}, ecdsa = {{s003}}

## Đáp
@phut: 1
@che-do: so

`mlDsa / ecdsa`

Khoảng {{s030}} lần, tức bậc {{s073}} lần. Con số này là lý do kiểm kê phải đi trước:

## Đáp (tiếp)
@phut: 1
@che-do: so

chỗ nào trong hệ chỉ ký một lần cho một bản firmware vài trăm kB thì {{s028}} byte chiếm bậc {{s021}} phần trăm bản cập nhật, còn chỗ nào ký từng bản tin cảm biến {{s007}} byte thì chữ ký nặng hơn dữ liệu hơn {{s070}} lần và cả thiết kế phải đổi, ví dụ sang xác thực bằng khoá đối xứng với khoá do bắt tay cấp.

## Đáp (tiếp)
@phut: 1
@che-do: so

Cùng một phép đổi thuật toán, hai nơi trong cùng một hệ, hai kết luận trái ngược.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`S(d, r) = ({{s021}} − r)·(d+1) + r·(d+1)² N_vết(d) ≈ N₁ · κ^d`

## Giả thiết
@phut: 1
@che-do: so

- r là tỉ lệ THỜI GIAN CHẠY nằm ở phần phi tuyến, không phải tỉ lệ số dòng mã, và phải đo bằng profiler trên chính phần cứng đích
- phần tuyến tính trả giá bậc (d+1) vì mỗi phép tuyến tính tính riêng trên từng phần rồi tổ hợp lại
- phần phi tuyến trả giá bậc (d+1)² vì gadget nhân phải ghép mọi cặp phần, cộng chi phí làm mới nhiễu

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- nhiễu độc lập giữa các phần, nên kẻ tấn công cần đo d+1 điểm cùng lúc và số vết cần tăng theo bậc của d
- N₁ và κ là tham số KHAI SẴN của mô hình dạy học trong module này, không phải phép đo trên phần cứng của người học

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Module này tách bảo đảm an toàn của một hệ PQC thành mấy lớp, từ độ khó toán học cho tới mã chạy trên phần cứng thật?

*Module {{s083}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s022}} | lớp | module {{s083}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Che mặt nạ bậc d = {{s084}}. Mỗi bí mật bị tách thành bao nhiêu phần?

*Module {{s083}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s081}} | phần | module {{s083}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Che mặt nạ bậc d = {{s001}}, xét riêng phần phi tuyến của mã. Theo mô hình gadget nhân kiểu ISW, chi phí của riêng phần đó tăng lên bao nhiêu lần so với bản không che?

*Module {{s083}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s085}} | lần | module {{s083}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Che mặt nạ bậc d = {{s001}} trên một cài đặt mà phần phi tuyến chiếm r = {{s087}} thời gian chạy. Hệ số chậm ước lượng là bao nhiêu lần?

d = {{s001}}, r = {{s086}}

## Đáp
@phut: 1
@che-do: so

`({{s021}} - r) × (d + {{s021}}) + r × Math.pow(d + {{s021}}, {{s001}})`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s088}} lần. Hai số hạng góp không đều: phần tuyến tính chiếm {{s089}} thời gian mà chỉ góp {{s090}} × {{s022}} = {{s091}}, còn phần phi tuyến chiếm {{s092}} thời gian mà góp {{s087}} × {{s085}} = {{s093}}. Nên con số chi phí che mặt nạ phải khai r cùng với d, vì cùng bậc d trên hai cài đặt có r khác nhau cho hai kết quả khác nhau.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Cài đặt không che mặt nạ đạt {{s078}} bắt tay mỗi giây trên thiết bị đích. Bật che mặt nạ bậc d = {{s001}} với r = {{s087}}. Còn lại bao nhiêu bắt tay mỗi giây?

h0 = {{s078}}, d = {{s001}}, r = {{s086}}

## Đáp
@phut: 1
@che-do: so

`h0 / (({{s021}} - r) × (d + {{s021}}) + r × Math.pow(d + {{s021}}, {{s001}}))`

## Đáp (tiếp)
@phut: 1
@che-do: so

Khoảng {{s094}} bắt tay mỗi giây, từ {{s078}} ban đầu. Đây là con số phải đặt cạnh yêu cầu vận hành, không phải đặt cạnh con số của bài khác: nếu hệ cần {{s063}} bắt tay mỗi giây thì biên còn {{s095}} lần và che mặt nạ bậc {{s001}} khả thi; nếu hệ cần {{s096}} thì bậc {{s001}} đã không đáp ứng được và phải đổi thiết kế chứ không phải tắt che mặt nạ.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Mô hình số vết khai sẵn: N(d) = N₁ · κ^d với N₁ = {{s098}} vết cho cài đặt không che và κ = {{s073}}. Kẻ tấn công thu được 10⁶ vết. Bậc che mặt nạ nhỏ nhất để N(d) vượt số vết đó là bao nhiêu?

vet = {{s097}}, n1 = {{s098}}, kappa = {{s073}}

## Đáp
@phut: 1
@che-do: so

`Math.ceil(Math.log(vet / n1) / Math.log(kappa))`

## Đáp (tiếp)
@phut: 1
@che-do: so

Đúng bậc {{s001}}, vì N(1) = {{s099}} còn thấp hơn 10⁶ mà N(2) = {{s100}} đã vượt. Để ý tính bất đối xứng: mỗi bậc nhân số vết cần lên {{s073}} lần nhưng chỉ nhân thời gian chạy lên vài lần, nên về phía phòng vệ thì nâng bậc là món hàng rẻ. Hai tham số {{s098}} và {{s073}} là tham số dạy học khai sẵn, không phải phép đo trên phần cứng của anh, nên đừng đưa chúng vào bản thảo.

## Công thức này đứng trên giả thiết nào
@phut: 0.5
@che-do: hoi
@notes: Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.

`n_hiệu dụng = {{s021}} + (n − 1)·(1 − c) P_mất hết = p^(n_hiệu dụng) tỉ số tự lừa = p^(n_hiệu dụng) / p^n`

## Giả thiết
@phut: 1
@che-do: so

- p là xác suất một HỌ giả định gãy trong cửa sổ thời gian đang xét, không phải xác suất một cài đặt có lỗi
- c là tỉ lệ hệ dùng chung một họ giả định: c = {{s012}} là n họ khác nhau, c = {{s021}} là tất cả cùng một họ

## Giả thiết (tiếp)
@phut: 1
@che-do: so

- hai hệ cùng họ gãy cùng lúc hoàn toàn, tức tương quan nhận đúng hai giá trị {{s012}} hoặc {{s021}} ở mức họ, không có mức trung gian thật
- hybrid được ghép sao cho kẻ tấn công phải phá MỌI thành phần mới đọc được, không phải một trong số đó

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Sau vòng chuẩn hoá của NIST, bao nhiêu họ giả định còn đứng được cho triển khai thật?

*Module {{s101}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s022}} | họ | module {{s101}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Tấn công của Castryck và Decru hồi phục khoá SIKE được công bố năm nào?

*Module {{s101}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s102}} | năm | module {{s101}}

## Con số này bằng bao nhiêu
@phut: 0.5
@che-do: hoi
@notes: Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.

Họ dựa hàm băm có chữ ký rất lớn, còn họ lưới thì trung bình. Để có mốc so sánh bằng đầu: ML-DSA-65 cho chữ ký dài bao nhiêu byte?

*Module {{s101}}.*

## Đáp
@phut: 1
@che-do: so

!so {{s028}} | byte | module {{s101}}

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Ba hệ dùng song song, một nửa trong số đó chung một họ giả định nên c = {{s105}}, mỗi họ gãy với xác suất {{s106}} trong {{s063}} năm. Xác suất mất hết an toàn là bao nhiêu phần trăm?

p = {{s103}}, n = {{s022}}, c = {{s104}}

## Đáp
@phut: 1
@che-do: so

`{{s042}} × Math.pow(p, {{s021}} + (n - {{s021}}) × ({{s021}} - c))`

Đúng {{s107}}. Nếu nhân ba xác suất với nhau theo giả định độc lập thì ra {{s108}}, tức thấp hơn mười lần. Con số {{s107}} mới là con số phải đặt vào phần phân tích rủi ro, và đại lượng phải báo kèm là số lớp độc lập, ở đây bằng {{s001}}, chứ không phải số hệ bằng {{s022}}.

## Tính ra con số
@phut: 0.5
@che-do: hoi
@notes: Dẫn bằng miệng, đừng bấm máy.

Cùng cấu hình đó: ba hệ, c = {{s105}}, mỗi họ gãy với xác suất {{s106}}. Rủi ro thật lớn gấp bao nhiêu lần con số tính theo giả định độc lập?

p = {{s103}}, n = {{s022}}, c = {{s104}}

## Đáp
@phut: 1
@che-do: so

`Math.pow(p, {{s021}} + (n - {{s021}}) × ({{s021}} - c)) / Math.pow(p, n)`

Đúng {{s063}} lần. Đây là mức tự lừa khi coi hệ cùng họ là lớp bảo vệ riêng, và nó tăng rất nhanh: với ba hệ chung hết một họ, tức c = {{s021}}, tỉ số lên {{s042}} lần. Để ý chiều của nó: tỉ số luôn từ {{s021}} trở lên, nên giả định độc lập luôn cho con số LẠC QUAN hơn thực tế, không bao giờ bi quan hơn.

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
