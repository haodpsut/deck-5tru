---
tieu-de: Hybrid và giao thức
phu-de: Trụ 5 PQC · module 5.4
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 81
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

Hybrid của tôi ghép khoá theo cách nào, và nếu một nửa bị phá thì tính an toàn còn lại được bảo đảm bởi điều gì?

## Hybrid mua tính dự phòng, và nó mua bằng byte
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Hybrid ghép một bí mật cổ điển với một bí mật hậu lượng tử qua một **bộ tổ hợp (combiner)**, sao cho khoá dẫn xuất còn an toàn miễn **ít nhất một** thành phần còn an toàn. Tính chất đó là của bộ ghép, không phải hệ quả của việc có hai thành phần. Đây là chỗ nhiều bài viết hybrid nên an toàn hơn mà không chứng minh gì.

## Hybrid mua tính dự phòng, và nó mua bằng byte (tiếp)
@phut: 1
@che-do: noi

Và hybrid trả giá bằng byte, theo hai chiều không đối xứng: phía khách gửi khoá công khai, phía chủ gửi bản mã. Với EDHOC thì kích thước mỗi bản tin là tiêu chí thiết kế chính, khác hẳn TLS, nên vài chục byte chênh lệch đã là một mảnh.

## Hybrid mua tính dự phòng, và nó mua bằng byte (tiếp)
@phut: 1
@che-do: noi

**Hai ghi chú về trạng thái số.** Mọi con số byte của ML-KEM trong module này đang ở trạng thái **chưa xác minh**, chưa ai mở FIPS {{s001}} ra đối chiếu. Và đặc tả thiết kế để dấu chưa chắc cho kích thước bản tin EDHOC với chứng chỉ cổ điển, nên module này **không dạy con số đó**: thà thiếu một thẻ còn hơn dạy sai một số.

## Bộ tổ hợp (combiner) và tính chất của nó
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Bộ tổ hợp (combiner) và tính chất của nó · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Bộ tổ hợp nhận hai bí mật chia sẻ và trả một khoá. Tính chất phải có: **khoá dẫn xuất còn an toàn miễn ít nhất một trong hai bí mật thành phần còn an toàn**. Trong TLS {{s003}} và trong các bản hybrid của giao thức khác, bộ ghép phổ biến nối hai bí mật rồi đưa qua hàm dẫn xuất khoá của giao thức.

## Bộ tổ hợp (combiner) và tính chất của nó · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: tính chất này nói hybrid **không yếu hơn thành phần mạnh nhất còn sống**. Nó **không** nói hybrid mạnh hơn cả hai. Hybrid mua tính dự phòng, không mua thêm độ khó, và phân biệt hai câu đó là phân biệt một bài bảo vệ được với một bài bị bắt ngay.

## Hybrid đi ở đâu trong TLS 1.3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Hybrid đi ở đâu trong TLS 1.3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Hybrid đi trong **nhóm trao đổi khoá**: một nhóm hybrid là một mã nhóm riêng, và phần chia khoá của nó là nối hai phần chia khoá thành phần. Hai bí mật rồi cùng vào hàm dẫn xuất khoá của giao thức.

## Hybrid đi ở đâu trong TLS 1.3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: trao đổi khoá hybrid và xác thực hậu lượng tử là **hai quyết định riêng**. Một bài khai hybrid cho trao đổi khoá mà bảng byte lại chứa cả chữ ký hậu lượng tử là bảng trộn hai cấu hình, và chênh byte lúc đó gộp hai nguyên nhân không tách ra được.

## EDHOC và OSCORE
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s004}} trên bốn.*

## EDHOC và OSCORE · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

EDHOC (RFC {{s005}}) là giao thức thiết lập khoá rất gọn cho IoT, chạy trên CoAP, và khoá nó thiết lập được OSCORE (RFC {{s006}}) dùng để bảo vệ bản tin. Giao thức có **ba bản tin bắt buộc** (message_1, message_2, message_3) và **một bản tin thứ tư tuỳ chọn** chỉ dùng để xác nhận khoá, theo đúng mục {{s007}} của RFC {{s005}}.

## EDHOC và OSCORE · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **kích thước mỗi bản tin là tiêu chí thiết kế chính của EDHOC**, khác hẳn TLS nơi tiêu chí là số vòng và tính tương thích. Hệ quả: một thành phần hậu lượng tử thêm vào EDHOC không đo bằng phần trăm mà đo bằng số mảnh, và một mảnh mất là mất cả bản tin.

## Hai chiều của một bắt tay KEM không đối xứng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Hai chiều của một bắt tay KEM không đối xứng · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Trong một KEM, phía khách gửi **khoá công khai** và phía chủ gửi **bản mã**. Với ML-KEM-768 thì hai thứ đó khác kích thước, nên hai chiều của bắt tay không bằng nhau.

## Hai chiều của một bắt tay KEM không đối xứng · (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: đừng gộp một con số cho cả hai chiều. Chênh lệch giữa hai chiều là {{s009}} byte, nghe nhỏ, nhưng ở một liên kết có tải khả dụng khoảng một trăm byte mỗi mảnh thì nó đúng bằng một mảnh, và số mảnh vào số mũ của xác suất hoàn tất bắt tay. Bảng byte phải tách theo chiều.

## Hybrid: tính chất của bộ tổ hợp, và ngân sách byte
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Tính chất bộ tổ hợp: khoá dẫn xuất an toàn miễn ÍT NHẤT MỘT bí mật thành phần còn an toàn. Byte phía khách = byte cổ điển + byte khoá công khai hậu lượng tử. Byte phía chủ = byte cổ điển + byte bản mã hậu lượng tử. Số mảnh = làm tròn lên của (tổng byte chiều đó / tải khả dụng mỗi mảnh).`

## Hybrid: tính chất của bộ tổ hợp, và ngân sách (tiếp)
@phut: 1
@che-do: so

**Giả thiết nó đứng trên:**

- bộ tổ hợp có tính chất an toàn miễn ít nhất một thành phần còn an toàn, và tính chất đó phải được chứng minh hoặc dẫn, chứ không suy ra từ việc có hai thành phần
- cả hai bí mật đều vào hàm dẫn xuất khoá của giao thức, không bí mật nào bị cắt bỏ ở khâu nào trong chuỗi dẫn xuất

## Hybrid: tính chất của bộ tổ hợp, và ngân sách (tiếp)
@phut: 1
@che-do: so

- hai chiều không đối xứng: phía khách gửi khoá công khai, phía chủ gửi bản mã, nên byte hai chiều khác nhau
- tải khả dụng mỗi mảnh đã trừ tiêu đề và phần bảo mật của tầng dưới, và không có cơ chế nào gộp hai bản tin vào một mảnh

## Hybrid: tính chất của bộ tổ hợp, và ngân sách byte · ghi
@phut: 1
@che-do: noi

Để ý một chuyện về phép chia cuối: tỉ số byte hybrid trên byte chỉ cổ điển **không định nghĩa được** ở chế độ chỉ hậu lượng tử, vì lúc đó mẫu số bằng {{s010}}. Nên nếu bài của anh báo một tỉ số thì nó chỉ nói về hai trong ba chế độ, và điều đó phải nằm trong câu chứ không nằm trong đầu người viết.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s008}} | bản tin bắt buộc | EDHOC cần bao nhiêu bản tin BẮT BUỘC để thiết lập khoá?
!so {{s011}} | byte | Phần chia khoá của X25519 dài bao nhiêu byte?
!so {{s012}} | byte | Trong hybrid, phía chủ gửi bản mã của ML-KEM-768. Bản mã đó

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hybrid X25519 cộng ML-KEM-768. Phía khách gửi phần chia khoá cổ điển cộng khoá công khai hậu lượng tử. Tổng bao nhiêu byte?

cl = {{s011}}, pqk = {{s013}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`cl + pqk`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

{{s014}} byte. Đây là một trong hai con số nên nhớ bằng đầu của module, vì nó cho ước lượng ngay trong lúc nghe báo cáo: ở một liên kết có tải khả dụng khoảng một trăm byte mỗi mảnh thì nó thành {{s015}} mảnh. Để ý phép cộng này chỉ gồm hai hạng tử vì đây là phần chia khoá, chưa có chữ ký nào; thêm xác thực hậu lượng tử là một quyết định riêng và nó cộng tiếp vào.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Cả hai hạng tử đang ở trạng thái chưa xác minh.

## Cùng bộ thuật toán đó
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cùng bộ thuật toán đó, nhưng phía chủ: phần chia khoá cổ điển cộng bản mã hậu lượng tử. Tổng bao nhiêu byte?

cl = {{s011}}, pqs = {{s012}}

## Cùng bộ thuật toán đó · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`cl + pqs`

{{s016}} byte, tức nhỏ hơn phía khách {{s009}} byte. Hai chiều không đối xứng vì trong một KEM phía khách gửi khoá công khai còn phía chủ gửi bản mã. Chênh {{s009}} byte nghe nhỏ, nhưng ở tải khả dụng khoảng một trăm byte mỗi mảnh thì nó đúng bằng một mảnh, và số mảnh vào số mũ của xác suất hoàn tất bắt tay. Vì thế bảng byte phải tách theo chiều, đừng gộp một con số cho cả hai.

## Cùng bộ thuật toán đó · đáp (tiếp)
@phut: 1
@che-do: noi

Cả hai hạng tử đang ở trạng thái chưa xác minh.

## Tính chất mà một bộ tổ hợp hybrid phải có là gì?
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Tính chất mà một bộ tổ hợp hybrid phải có là gì?

- Khoá dẫn xuất ngắn hơn tổng độ dài hai bí mật thành phần
- Khoá dẫn xuất an toàn miễn ít nhất một trong hai bí mật thành phần còn an toàn
- An toàn của khoá dẫn xuất bằng tổng an toàn của hai thành phần
- Hai thành phần phải thuộc cùng một họ toán học

## Tính chất mà một bộ tổ hợp hybrid phải có là gì? · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khoá dẫn xuất an toàn miễn ít nhất một trong hai bí mật thành phần còn an toàn**

## Tính chất mà một bộ tổ hợp hybrid phải có là gì? (tiếp)
@phut: 1
@che-do: noi

Đây là tính chất phải nêu tên và phải dẫn chứng minh, vì nó là tính chất của bộ ghép chứ không phải hệ quả của việc có hai thành phần. Đáp án thứ ba là chỗ hay lẫn: an toàn không cộng được như vậy, và hybrid không mạnh hơn thành phần mạnh nhất còn sống. Nó mua tính dự phòng, không mua thêm độ khó.

## Với người thiết kế hậu lượng tử
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Với người thiết kế hậu lượng tử, EDHOC khác TLS ở chỗ nào quan trọng nhất?

- Kích thước mỗi bản tin là tiêu chí thiết kế chính, nên thêm byte là thêm mảnh trên liên kết chật
- EDHOC chạy trên TCP nên không có phân mảnh
- EDHOC không dùng hàm dẫn xuất khoá
- EDHOC không cần xác thực hai bên

## Với người thiết kế hậu lượng tử · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Kích thước mỗi bản tin là tiêu chí thiết kế chính, nên thêm byte là thêm mảnh trên liên kết chật**

## Với người thiết kế hậu lượng tử · đáp (tiếp)
@phut: 1
@che-do: noi

EDHOC thiết kế cho IoT trên CoAP, và tiêu chí chính của nó là byte mỗi bản tin, khác hẳn TLS nơi tiêu chí là số vòng và tính tương thích. Hệ quả cho người làm PQC: một thành phần hậu lượng tử thêm vào EDHOC không đo bằng phần trăm mà đo bằng số mảnh, và số mảnh là hàm bước nhảy nên nó đổi theo bậc chứ không mượt.

## Trong hybrid X25519 cộng ML-KEM-768
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trong hybrid X25519 cộng ML-KEM-768, vì sao phía khách và phía chủ không gửi cùng số byte?

- Vì phía chủ nén bản tin của mình
- Vì phía khách gửi khoá công khai còn phía chủ gửi bản mã, và hai thứ đó khác kích thước
- Vì phía chủ phải gửi thêm chữ ký trong mọi cấu hình
- Vì tải khả dụng mỗi mảnh khác nhau theo hai chiều

## Trong hybrid X25519 cộng ML-KEM-768 · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Vì phía khách gửi khoá công khai còn phía chủ gửi bản mã, và hai thứ đó khác kích thước**

## Trong hybrid X25519 cộng ML-KEM-768 · đáp (tiếp)
@phut: 1
@che-do: noi

Trong một KEM, luồng (flow) là: phía khách gửi khoá công khai, phía chủ đóng gói (packet) và gửi bản mã. Với ML-KEM-768 thì khoá công khai {{s013}} byte và bản mã {{s012}} byte, nên hai chiều chênh {{s009}} byte. Đáp án thứ ba sai vì chữ ký là một quyết định riêng, không phải thuộc tính của KEM; nó cộng vào cả hai chiều tuỳ cấu hình xác thực.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn lập luận về hybrid sau có một câu không chứng minh được. Bấm vào câu đó.

- Chúng tôi dùng hybrid X25519 cộng ML-KEM-768 cho trao đổi khoá.
- Hai bí mật chia sẻ được nối chuỗi rồi đưa qua hàm dẫn xuất khoá của giao thức.
- Vì hybrid kết hợp hai thành phần, nó an toàn hơn từng thành phần, nên thiết kế của chúng tôi an toàn hơn cả bản chỉ cổ điển và bản chỉ hậu lượng tử.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì hybrid kết hợp hai thành phần, nó an toàn hơn từng thành phần, nên thiết kế của chúng tôi an toàn hơn cả bản chỉ cổ điển và bản chỉ hậu lượng tử.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu đầu đúng và đủ cụ thể. Câu này sai hai lần. Thứ nhất, tính chất mà một bộ tổ hợp tốt cho là an toàn miễn ÍT NHẤT MỘT thành phần còn an toàn, tức hybrid không yếu hơn thành phần mạnh nhất còn sống; nó không mạnh hơn cả hai, vì hybrid mua tính dự phòng chứ không mua thêm độ khó. Thứ hai, và nặng hơn:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

câu này suy tính chất ra từ việc CÓ hai thành phần, trong khi tính chất là của BỘ GHÉP. Ghép sai cách thì hybrid không mạnh hơn thành phần yếu nhất và toàn bộ lý do dùng hybrid mất, trong khi bắt tay vẫn thành công nên không kiểm thử liên thông nào phát hiện. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

nêu tên tính chất, dẫn chứng minh hoặc dẫn đặc tả cho bộ ghép mình dùng, và thêm một phép kiểm so khoá dẫn xuất với vector tham chiếu, phép kiểm đó phải HỎNG khi bỏ một nửa đầu vào.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn tính ngân sách byte sau có một câu sai. Bấm vào câu đó.

- Phần chia khoá của hybrid gồm {{s011}} byte của thành phần cổ điển cộng phần hậu lượng tử.
- Phía khách gửi {{s014}} byte và phía chủ cũng gửi {{s014}} byte, nên tổng hai chiều là {{s017}} byte.
- Số mảnh mỗi chiều tính bằng byte chiều đó chia cho tải khả dụng mỗi mảnh, rồi làm tròn lên.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Phía khách gửi {{s014}} byte và phía chủ cũng gửi {{s014}} byte, nên tổng hai chiều là {{s017}} byte.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Phép cộng trong câu này tự nhất quán, nên nó không lộ ra khi soát số học; cái sai là coi hai chiều đối xứng. Phía khách gửi khoá công khai ML-KEM-768, tức {{s013}} byte, nên {{s011}} cộng {{s013}} bằng {{s014}} byte. Phía chủ gửi BẢN MÃ, tức {{s012}} byte, nên {{s011}} cộng {{s012}} bằng {{s016}} byte. Tổng hai chiều là {{s018}} byte chứ không phải {{s017}} byte.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Chênh {{s009}} byte nghe nhỏ, nhưng ở tải khả dụng khoảng một trăm byte mỗi mảnh thì nó đúng bằng một mảnh, và số mảnh vào số mũ của xác suất hoàn tất bắt tay. Cách sửa: tách bảng byte theo chiều gửi, đừng gộp một con số cho cả hai.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Chọn thành phần cổ điển và thành phần hậu lượng tử, rồi tra byte của từng cái THEO CHIỀU GỬI
- Byte phần chia khoá mỗi chiều = byte thành phần cổ điển + byte thành phần hậu lượng tử của chiều đó
- Ghép hai bí mật bằng một bộ tổ hợp có tính chất an toàn miễn ít nhất một thành phần còn an toàn

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Số mảnh mỗi chiều = byte chiều đó chia cho tải khả dụng mỗi mảnh, rồi làm tròn lên
- So với chế độ chỉ cổ điển và chế độ chỉ hậu lượng tử ở CÙNG cấu hình xác thực, rồi khai tiêu chí đã dùng

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Hybrid X25519 cộng ML-KEM-768 · phía khách {{s014}} byte · phía chủ {{s016}} byte · tổng hai chiều {{s018}} byte · {{s015}} mảnh ở tải khả dụng {{s019}} byte · {{s020}} lần so với chế độ chỉ cổ điển

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Bộ tổ hợp có tính chất an toàn miễn ít nhất một thành phần còn an toàn** tắt đi: Bộ ghép không có tính chất đó: nó chỉ lấy một trong hai bí mật, hoặc nó kết hợp theo cách mà kẻ biết một nửa điều khiển được đầu ra.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Cả hai bí mật đều vào hàm dẫn xuất khoá, không bên nào bị cắt bỏ** tắt đi: Một trong hai bí mật bị bỏ ở đâu đó trong chuỗi dẫn xuất, ví dụ một cài đặt nối chuỗi rồi cắt độ dài về kích thước cũ.
- **Mỗi phần chia khoá đi trọn trong một mảnh** tắt đi: Tải khả dụng mỗi mảnh nhỏ hơn phần chia khoá, nên bản tin bị phân mảnh.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Khoá công khai xác thực của hai bên đã có sẵn, không gửi trong bắt tay** tắt đi: Phải gửi cả khoá công khai và chữ ký hậu lượng tử trong bắt tay.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Ngân sách byte của một phần chia khoá hybrid. Kéo byte cổ điển về {{s010}} để được chế độ chỉ hậu lượng tử, kéo byte hậu lượng tử về {{s010}} để được chế độ chỉ cổ điển. Mọi byte hậu lượng tử ở đây đang ở trạng thái chưa xác minh.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/5.4` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III states that the hybrid key exchange is more secure than either of its components, but no property of the combiner is stated or proved, and the construction is described only as a concatenation. Please state the security property you rely on, justify that your combiner has it, and correct the claim if needed.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have corrected the claim and added the missing justification. The property we rely on is that the combiner is secure as long as at least one of the two component secrets remains secure; the hybrid is therefore no weaker than the strongest surviving component, and we no longer claim it is stronger than either. Section III-B now specifies the derivation exactly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

both shared secrets enter the protocol key schedule, and we cite the specification clause and the proof of the combiner property rather than inferring it from the presence of two components. We also added a negative test, because this failure mode is silent: the handshake still succeeds if one secret is quietly dropped from the schedule.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Test suite case KS-07 compares the derived key against a reference vector, and Appendix D shows that the test fails when either input is removed, so the test actually tests something. Finally we state the price per direction rather than one aggregate number, because the two directions are not symmetric: the client sends {{s011}} bytes plus the 1184-byte ML-KEM-768 encapsulation key, which is {{s014}} bytes, and the server sends {{s011}} bytes plus the 1088-byte ciphertext, which is {{s016}} bytes, for {{s018}} bytes in total.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

At the roughly 100-byte usable payload of our link layer, the client direction becomes {{s015}} fragments, which is the operative constraint rather than the ratio.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: thêm một trích dẫn tới một bài về hybrid và giữ nguyên câu an toàn hơn từng thành phần. Đã có tài liệu nhưng tính chất vẫn chưa nêu tên và câu vẫn sai chiều.
- Mức {{s004}}: nêu đúng tính chất an toàn miễn ít nhất một thành phần còn an toàn và sửa câu không còn nói mạnh hơn cả hai. Vẫn chưa chỉ ra bộ ghép CỦA MÌNH có tính chất đó.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s008}}: nêu tên tính chất, chỉ ra bộ ghép của mình có nó bằng cách dẫn chứng minh hoặc dẫn đặc tả giao thức, và mô tả chính xác chuỗi dẫn xuất khoá để người đọc kiểm được rằng cả hai bí mật đều vào.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table II reports that the hybrid handshake costs about {{s021}} times the bytes of the classical-only configuration, and the paper uses this single ratio throughout Section V to argue feasibility on constrained links. The ratio is reported without the configuration it was computed under, and feasibility on a constrained link is not a function of a ratio. Please justify.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree and have restructured both the table and the argument. Table II now states the configuration in its caption: the suite, the direction of each row, and the fact that authentication public keys are pre-provisioned so that no signature is carried in the handshake.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The table leads with absolute bytes per direction, {{s014}} bytes for the client and {{s016}} bytes for the server, {{s018}} bytes in total, and reports the ratio only as a secondary column, since feasibility on a constrained link is a function of absolute bytes rather than of a ratio. Section V now argues feasibility through the fragment count:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

at the roughly 100-byte usable payload of the target link, the client direction becomes {{s015}} fragments and the server direction {{s022}}, and we give the completion probability as a function of the fragment count rather than a single number. We also flag that the fragment count is a step function, so we checked the margin:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

{{s014}} bytes sits {{s023}} bytes above a 12-fragment boundary, which means a few bytes of additional encoding overhead would not change the count, but a reduction of {{s023}} bytes would. We state explicitly that the ratio is undefined in the post-quantum-only configuration, where the classical component is absent and the denominator is zero, so the ratio column describes two of our three configurations and not the third.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, the authentication configuration is now tabulated separately in Table III, so that a byte difference attributable to signatures is not mixed into the key exchange comparison.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s002}}: thêm một câu nói tỉ số tính cho cấu hình trao đổi khoá. Đã khai một phần cấu hình nhưng vẫn dùng tỉ số để lập luận khả thi.
- Mức {{s004}}: khai đủ cấu hình (bộ thuật toán, chiều gửi, có gửi chữ ký hay không) và in thêm byte tuyệt đối cạnh tỉ số. Chưa nối byte sang số mảnh nên chưa trả lời câu khả thi.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s008}}: in byte tuyệt đối theo từng chiều, chuyển sang số mảnh ở tải khả dụng của liên kết đích, và lập luận khả thi bằng số mảnh chứ bằng tỉ số.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/5.4` bấm thẻ.
