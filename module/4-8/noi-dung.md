---
tieu-de: Cảm biến tích hợp ISAC: mạng vừa truyền vừa biết anh ở đâu
phu-de: Trụ 4 6G Sec · module 4.8
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 86.5
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: 6G SEC
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Nếu trạm gốc dùng chính tín hiệu truyền thông để định vị, thì nó đạt độ chính xác bao nhiêu mét, và ai có quyền đọc con số đó?

## Cảm biến tích hợp ISAC: mạng vừa truyền vừa biết anh ở
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Cảm biến tích hợp, tức integrated sensing and communication, không thêm một khối phần cứng nào vào mô hình đe doạ (threat model) của anh. Nó chỉ nói ra một điều đã có sẵn: **phân giải cự ly (range resolution) bằng c chia hai lần băng thông**, và **phân giải vận tốc bằng bước sóng chia hai lần thời gian quan sát**. Hai đại lượng đó là hai thứ mà mọi hệ 6G đều đẩy lên vì chúng làm truyền thông tốt hơn.

## Cảm biến tích hợp ISAC: mạng vừa truyền vừa biết (tiếp)
@phut: 1
@che-do: noi

Hệ quả là một câu phải nói được thành tiếng: **khả năng cảm biến là hệ quả vật lý của băng rộng, không phải một tính năng bật tắt được**. Nên câu chúng tôi không bật cảm biến **không phải một bảo đảm riêng tư**: nó là một trạng thái cấu hình, và ai kiểm soát trạm gốc thì đổi được trạng thái đó mà không đổi phần cứng nào, không đổi chuẩn nào, không để lại dấu nào ở phía người dùng.

## Cảm biến tích hợp ISAC: mạng vừa truyền vừa biết (tiếp)
@phut: 1
@che-do: noi

Module này có ba việc. Một, cho anh bốn con số neo để nhớ thuộc: ở {{s001}} MHz thì phân giải cự ly khoảng {{s002}} m, ở {{s003}} GHz thì khoảng {{s004}} m, và ở {{s005}} GHz với {{s006}} ms quan sát thì phân giải vận tốc khoảng {{s007}} m/s. Hai, tách rõ **phân giải** khỏi **độ chính xác định vị (localisation accuracy)**:

## Cảm biến tích hợp ISAC: mạng vừa truyền vừa biết (tiếp)
@phut: 1
@che-do: noi

phân giải là trần của khả năng phân biệt, còn độ chính xác còn phụ thuộc tỉ số tín hiệu trên nhiễu, nên nó xấu hơn. Ba, thêm vào khuôn mô hình đe doạ một dòng mà bài ISAC hay thiếu: **mạng tự sinh ra dữ liệu vị trí**, dữ liệu đó nằm ở lớp nào, giữ bao lâu, và ai đọc được.

## Phân giải cự ly theo băng thông
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Phân giải cự ly theo băng thông · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`Δr = c/(2B)`. Băng thông là đại lượng duy nhất quyết định nó: không phải công suất, không phải số ăng ten, không phải tần số sóng mang.

## Phân giải cự ly theo băng thông · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **ở {{s001}} MHz thì phân giải cự ly khoảng {{s002}} m, và nó tỉ lệ nghịch với băng thông**, nên {{s003}} GHz cho khoảng {{s004}} m, tức tốt hơn đúng mười lần. Nhớ cặp này thì đọc bất kỳ bài 6G nào cũng tự nhẩm ra ngay được mức cảm biến mà hệ đó đạt tới, kể cả khi bài không nhắc chữ cảm biến nào.

## Phân giải khác độ chính xác định vị
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s008}} trên bốn.*

## Phân giải khác độ chính xác định vị · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

**Phân giải** là khoảng cách nhỏ nhất mà hai mục tiêu còn tách ra được thành hai đỉnh, và nó do băng thông cùng thời gian quan sát quyết định. **Độ chính xác định vị** là sai số khi ước lượng vị trí của MỘT mục tiêu, và nó còn phụ thuộc tỉ số tín hiệu trên nhiễu cùng hình học.

## Phân giải khác độ chính xác định vị · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **phân giải là trần của khả năng phân biệt, nên độ chính xác thật xấu hơn hoặc bằng, không bao giờ tốt hơn theo chiều người ta hay nhầm**. Hai hệ quả ngược chiều phải tách rõ:

## Phân giải khác độ chính xác định vị · đáp (tiếp)
@phut: 1
@che-do: noi

nếu anh muốn tuyên bố khả năng ĐỊNH VỊ thì phân giải là con số lạc quan và anh phải đo thêm; nếu anh muốn tuyên bố RỦI RO riêng tư thì phân giải là con số lạc quan theo chiều có lợi cho anh, nên dùng nó làm chặn là hợp lệ và phải khai là chặn.

## Vì sao cảm biến không phải một tính năng tuỳ chọn
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s009}} trên bốn.*

## Vì sao cảm biến không phải một tính năng tuỳ chọn · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Phân giải chỉ phụ thuộc băng thông và thời gian quan sát. Cả hai là thứ hệ đã có, vì cả hai làm truyền thông tốt hơn. Nên khả năng cảm biến không phải một khối chức năng được thêm vào, mà là **một hệ quả vật lý của việc hệ đó băng rộng**.

## Vì sao cảm biến không phải một tính năng tuỳ chọn (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **câu chúng tôi không bật cảm biến là một trạng thái cấu hình, không phải một bảo đảm riêng tư**. Cách viết đứng được: coi vị trí là dữ liệu MẠNG TỰ SINH RA, rồi khai bốn dòng trong mô hình đe doạ gồm dữ liệu nằm ở lớp nào, giữ bao lâu, ai đọc được, và cơ chế nào ràng buộc ba dòng trên.

## Công thức và giả thiết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Δr = c / (2·B) Δv = λ / (2·T_obs) Δθ ≈ λ / (N·d) = 2/N với d = λ/2 A_oô = Δr · R · Δθ`

**Giả thiết nó đứng trên:**

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- xung nén lý tưởng với cửa sổ chữ nhật, không trọng số giảm búp phụ; mọi cửa sổ thật làm phân giải xấu đi theo một hệ số lớn hơn {{s003}}, nên đây là trần chứ không phải phép đo
- tỉ số tín hiệu trên nhiễu đủ cao để độ chính xác đạt tới trần phân giải; nếu không thì ba con số trên là chặn, và độ chính xác thật xấu hơn theo cận Cramer Rao

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- mục tiêu đứng yên trong suốt T_obs và chuyển động dọc đường ngắm, nên phân giải vận tốc nói về một thành phần Doppler duy nhất
- dàn ăng ten tuyến tính đều, khoảng cách nửa bước sóng, mục tiêu ở hướng vuông góc với dàn; lệch khỏi hướng đó thì búp rộng ra và phân giải góc xấu đi

## Công thức và giả thiết (tiếp)
@phut: 1
@che-do: so

- cự ly tham chiếu R phải được khai khi quy ô bất định ra mét vuông, vì phân giải góc có đơn vị radian chứ không phải mét
- c = {{s010}} m/s, giá trị chính xác theo định nghĩa của mét

## Công thức · ghi chú
@phut: 1
@che-do: noi

Hai chỗ dễ sai mà cổng nào cũng xanh. Một: con số tròn {{s002}} m ở {{s001}} MHz và {{s011}} m ở {{s012}} MHz đến từ xấp xỉ `c ≈ {{s013}} × 10⁸` m/s; dùng giá trị chính xác thì ra {{s014}} m và {{s015}} m, lệch khoảng {{s016}}. Lệch đó không quan trọng về vật lý nhưng nó là dấu vết cho biết con số trong bài được tính hay được gõ tay. Hai:

## Công thức · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

**phân giải góc với khoảng cách nửa bước sóng không phụ thuộc tần số sóng mang**, vì bước sóng triệt tiêu giữa tử và mẫu. Ai viết rằng lên tần số cao hơn thì phân giải góc tốt hơn đang nhầm phân giải góc với kích thước vật lý của dàn ăng ten.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s017}} | m | Một hệ cảm biến tích hợp dùng băng thông {{s001}} MHz. Phân
!so {{s018}} | m | Cùng hệ đó nâng băng thông lên {{s003}} GHz. Phân giải cự
!so {{s019}} | m/s | Sóng mang {{s005}} GHz

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s020}} | radian | Dàn ăng ten tuyến tính đều

## Sóng mang 28 GHz
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Sóng mang {{s005}} GHz, nhưng cửa sổ quan sát chỉ còn {{s008}} ms vì hệ phải trả tài nguyên lại cho truyền thông. Phân giải vận tốc bằng bao nhiêu mét trên giây?

c = {{s010}}, fGhz = {{s005}}, Tms = {{s008}}

## Sóng mang 28 GHz · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(c/(fGhz⋆1e9))/(2⋆Tms⋆1e-3)`

Khoảng {{s021}} m/s, so với {{s022}} m/s khi cửa sổ là {{s006}} ms. Rút ngắn cửa sổ năm lần làm phân giải vận tốc xấu đúng năm lần, vì quan hệ là tỉ lệ nghịch với thời gian quan sát. Đây là đòn giảm nhẹ duy nhất trong module mà có vẻ dùng được, nên phải nói rõ giới hạn của nó:

## Sóng mang 28 GHz · đáp (tiếp)
@phut: 1
@che-do: noi

ở {{s021}} m/s thì mạng vẫn phân biệt được xe chạy với người đi bộ, và phân giải cự ly thì không đổi một chút nào vì nó không đi qua thời gian quan sát.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hệ dùng {{s003}} GHz băng thông và dàn {{s024}} phần tử với khoảng cách nửa bước sóng. Ở cự ly tham chiếu {{s001}} m, diện tích ô bất định bằng bao nhiêu mét vuông?

c = {{s010}}, Bhz = {{s023}}, R = {{s001}}, N = {{s024}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`(c/(2⋆Bhz))⋆R⋆(2/N)`

Khoảng {{s025}} m², tức một ô chừng nửa mét mỗi chiều: hai người đứng cách nhau hơn thế thì mạng tách ra được thành hai mục tiêu. Hai chỗ phải khai cạnh con số này. Một, cự ly tham chiếu {{s001}} m là giả thiết, vì phân giải góc có đơn vị radian nên ô bất định nở ra tuyến tính theo cự ly.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Hai, đây là trần của khả năng phân biệt ở tỉ số tín hiệu trên nhiễu cao, nên ô thật rộng hơn và con số này là chặn có lợi cho lập luận riêng tư, phải khai là chặn.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài của anh viết rằng hệ không bật chế độ cảm biến nên không thu vị trí người dùng. Reviewer bác câu đó. Lập luận nào của reviewer là lập luận mạnh nhất?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chuẩn cho cảm biến tích hợp chưa đóng băng, nên tuyên bố không kiểm được.
- Phân giải cự ly và phân giải vận tốc chỉ phụ thuộc băng thông và thời gian quan sát, nên mọi hệ băng rộng đều cảm biến được; không bật là một trạng thái cấu hình, không phải một tính chất của hệ.
- Cảm biến đòi thêm chuỗi xử lý ở trạm gốc, nên chi phí tính toán mới là ràng buộc thật.

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Độ chính xác định vị thấp hơn phân giải, nên con số phân giải trong bài không đáng lo.

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Phân giải cự ly và phân giải vận tốc chỉ phụ thuộc băng thông và thời gian quan sát, nên mọi hệ băng rộng đều cảm biến được; không bật là một trạng thái cấu hình, không phải một tính chất của hệ.**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Chỗ hổng không nằm ở trạng thái của chuẩn và cũng không nằm ở chi phí tính toán: khả năng cảm biến là hệ quả vật lý của băng thông và thời gian quan sát, hai thứ hệ đã có vì chúng làm truyền thông tốt hơn, nên ai kiểm soát trạm gốc thì bật lại được mà không đổi phần cứng nào. Lập luận về độ chính xác thì đi ngược hẳn chiều:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

phân giải là trần của khả năng phân biệt, nên độ chính xác thật xấu hơn và ô bất định RỘNG hơn, tức rủi ro tính theo phân giải là một chặn có lợi cho bên bị đo chứ không phải lý do bỏ qua.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình đe doạ của một bài ISAC đã khai đủ cấu hình hệ nhưng vẫn bị trả vì thiếu một dòng. Dòng nào?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Danh sách giao thức mã hoá dùng ở lớp truyền tải giữa trạm gốc và lõi.
- Số phần tử ăng ten của trạm gốc và khoảng cách giữa chúng.
- Băng thông cực đại mà sóng mang hỗ trợ.
- Mạng tự sinh ra dữ liệu vị trí, dữ liệu đó nằm ở lớp nào, giữ bao lâu, và ai đọc được.

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Mạng tự sinh ra dữ liệu vị trí, dữ liệu đó nằm ở lớp nào, giữ bao lâu, và ai đọc được.**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ba dòng kia là tham số hệ, và chúng đã nằm ở mục cấu hình rồi; khai lại chúng trong mô hình đe doạ không thêm chủ thể nào và không thêm năng lực nào. Dòng còn thiếu là dòng về DỮ LIỆU: mạng tự sinh ra cự ly, vận tốc và góc từ chính tín hiệu người dùng buộc phải phát, nên phải nói rõ dữ liệu đó nằm ở lớp nào, giữ bao lâu và chủ thể nào đọc được.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Thiếu dòng đó thì mô hình đe doạ không có ai giữ dữ liệu, và mọi cơ chế đồng ý dựa trên việc người dùng cấp dữ liệu đều không áp được.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn sau có một chỗ đổi một đại lượng thành một đại lượng khác. Bấm vào chỗ đó.

- Hệ của chúng tôi dùng {{s012}} MHz băng thông ở dải {{s005}} GHz,
- nên phân giải cự ly đạt khoảng {{s026}} m,
- do đó hệ định vị người dùng với sai số {{s026}} m ở mọi tỉ số tín hiệu trên nhiễu.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**do đó hệ định vị người dùng với sai số {{s026}} m ở mọi tỉ số tín hiệu trên nhiễu.**

Hai mệnh đề đầu đều đúng: {{s012}} MHz cho phân giải cự ly {{s015}} m với tốc độ sáng chính xác. Mệnh đề này đổi PHÂN GIẢI thành ĐỘ CHÍNH XÁC, hai đại lượng khác nhau.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Phân giải là khoảng cách nhỏ nhất mà hai mục tiêu còn tách ra thành hai đỉnh, và nó là trần ở điều kiện tốt nhất; độ chính xác là sai số khi ước lượng vị trí của một mục tiêu, và nó còn phụ thuộc tỉ số tín hiệu trên nhiễu cùng hình học, nên nó xấu hơn.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Cụm ở mọi tỉ số tín hiệu trên nhiễu làm câu sai thêm một lần nữa, vì chính tham số đó là tham số bị bỏ. Cách sửa: giữ {{s015}} m làm trần và khai là trần, rồi báo sai số định vị theo cận Cramer Rao như một hàm của tỉ số tín hiệu trên nhiễu.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Ba câu sau nằm trong cùng một bài, cách nhau hai mục. Bấm vào câu làm cả ba tự mâu thuẫn.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Mô hình đe doạ của chúng tôi giả định kẻ tấn công nội bộ đọc được dữ liệu ở lớp điều phối,
- và dữ liệu cảm biến được giữ ở lớp điều phối trong ba mươi ngày để huấn luyện mô hình dự báo tải,
- nhưng riêng tư vị trí nằm ngoài phạm vi bài này, vì chúng tôi không xử lý dữ liệu người dùng.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nhưng riêng tư vị trí nằm ngoài phạm vi bài này, vì chúng tôi không xử lý dữ liệu người dùng.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu là lựa chọn thiết kế hợp lệ và khai được. Mệnh đề này mâu thuẫn với CHÍNH HAI MỆNH ĐỀ TRƯỚC theo hai đường cùng lúc. Đường thứ nhất: bài đã tự cấp cho kẻ tấn công quyền đọc đúng cái lớp đang giữ vị trí ba mươi ngày, nên riêng tư vị trí nằm TRONG phạm vi theo chính giả thiết của bài, không phải ngoài. Đường thứ hai:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

dữ liệu cảm biến là dữ liệu MẠNG TỰ SINH RA từ tín hiệu mà người dùng buộc phải phát, nên câu không xử lý dữ liệu người dùng không loại nó ra được. Đây đúng là loại mâu thuẫn mà reviewer bắt được chỉ bằng cách đọc hai mục cạnh nhau, và cách sửa là đưa riêng tư vị trí vào phạm vi, kèm thời gian giữ dữ liệu và danh sách chủ thể đọc được.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Hai mục tiêu tách được theo cự ly khi hai tiếng vọng của chúng cách nhau trong miền thời gian ít nhất bằng độ rộng xung sau nén, tức τ = 1/B
- Độ lệch thời gian τ ứng với hiệu quãng đường đi và về bằng c·τ, nên hiệu cự ly bằng c·τ/2
- Thế τ = 1/B vào: Δr = c/(2B)
- Theo trục Doppler, phân giải tần số của một cửa sổ quan sát dài T_obs là 1/T_obs hertz

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Đổi hertz sang m/s bằng f_D = 2v/λ, nên Δv = λ/(2·T_obs)
- Ô bất định là tích của phân giải cự ly với bề rộng ngang R·Δθ, trong đó Δθ ≈ 2/N với khoảng cách nửa bước sóng

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Phân giải cự ly {{s014}} m ở {{s001}} MHz · phân giải vận tốc {{s022}} m/s ở {{s005}} GHz với {{s006}} ms · phân giải góc {{s027}} độ với {{s028}} ăng ten · ô bất định {{s029}} m² ở cự ly {{s001}} m

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Cảm biến là một tính năng tuỳ chọn, bật tắt được** tắt đi: Phân giải chỉ phụ thuộc băng thông và thời gian quan sát, nên mọi hệ băng rộng đều cảm biến được; không bật chỉ là một trạng thái cấu hình mà người kiểm soát trạm gốc đổi được.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dữ liệu cảm biến không được lưu** tắt đi: Dữ liệu cự ly, vận tốc và góc được giữ ở lớp điều phối để huấn luyện mô hình, trong một khoảng thời gian phải khai.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Tỉ số tín hiệu trên nhiễu đủ cao để độ chính xác đạt tới trần phân giải** tắt đi: Mục tiêu ở xa hoặc bị che, nên tỉ số tín hiệu trên nhiễu thấp và sai số ước lượng lớn hơn trần phân giải theo cận Cramer Rao.
- **Biết cự ly tham chiếu để quy phân giải góc ra mét** tắt đi: Không khai cự ly nào, chỉ báo phân giải góc theo độ hoặc theo radian.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bốn thanh kéo là bốn tham số mà anh đẩy lên vì chúng làm truyền thông tốt hơn. Bốn đầu ra là mức cảm biến mà hệ đạt tới như một hệ quả. Để ý xem thanh nào KHÔNG đổi được đầu ra nào: đó là chỗ nhiều bài viết sai chiều.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.8` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section VI argues that privacy is preserved because the sensing mode is disabled by default in the proposed deployment. The range and velocity resolutions you derive in Section III depend only on bandwidth and observation time, both of which the system already uses for communication. Please explain in what sense a disabled mode is a privacy guarantee rather than a configuration state.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right and we have rewritten the claim. Sensing capability is not a feature of our design, it is a consequence of the bandwidth and observation time the system already uses, so we now report it as an available capability and state its ceiling: {{s030}} m range resolution at {{s001}} MHz, {{s031}} m at {{s012}} MHz, {{s032}} m/s velocity resolution at {{s005}} GHz with a {{s006}} ms window, and a {{s033}} square metre uncertainty cell at {{s001}} m with {{s028}} elements.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

These figures hold whether or not a sensing mode is enabled, because no configuration flag appears in any of them. Section VI no longer claims that a disabled mode preserves privacy. It now states who can enable processing of that information, namely any party holding management rights on the gNB, and what constrains them, namely the role separation and configuration audit of Section III-A. We then moved the privacy argument to where it is measurable:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the sensing derived quantities are retained for {{s034}} days at the orchestration layer, the access list has three roles, and the threat model of Section II grants the internal adversary read access to that layer, so location privacy is in scope by our own assumptions. We also state that the resolution figures are a high signal to noise ratio bound, so the true uncertainty cell is larger, which makes the bound conservative for a risk claim and we label it as such.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: trả lời rằng chế độ cảm biến tắt theo mặc định và việc bật nó đòi thay đổi cấu hình, nên rủi ro thấp. Đúng về mô tả hệ, không trả lời được phản bác, vì nó vẫn coi một trạng thái cấu hình là một bảo đảm.
- Mức {{s008}}: thêm rằng việc bật cảm biến sẽ bị ghi nhận trong vết kiểm toán, nhưng không nói ai quản vết đó và vẫn giữ câu riêng tư được bảo đảm.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s013}}: khai rằng khả năng cảm biến là hệ quả của băng thông và thời gian quan sát nên nó có sẵn, báo phân giải như trần của năng lực, và chuyển lập luận riêng tư sang kiểm soát dữ liệu.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table III reports a positioning accuracy of {{s035}} m, and Section III derives that figure from the range resolution expression c over twice the bandwidth. Resolution and estimation accuracy are different quantities, and the latter depends on the signal to noise ratio, which Table III does not report. Please either relabel the column or provide accuracy results against the signal to noise ratio.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have relabelled the column and separated the two quantities throughout. Table III now reads range resolution, {{s031}} m at {{s012}} MHz computed from c over twice the bandwidth with the exact value of c, and we state the assumptions behind it: ideal pulse compression, rectangular window, and a signal to noise ratio high enough that estimation reaches the resolution bound.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We added Table IV, which reports the root mean square positioning error from the Cramer Rao bound against the signal to noise ratio from {{s036}} to {{s034}} dB, together with the simulated estimator error; the two agree at high signal to noise ratio and diverge as it falls, and we give the crossover measured on our own setup rather than a generic figure.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We then audited every sentence in the paper by the type of claim it makes, because the direction of the bound differs. For capability claims, such as the one in Section VII on industrial positioning, the resolution figure is optimistic and we now cite Table IV instead.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

For risk claims, such as the privacy discussion in Section VI, the resolution figure is conservative, because a lower signal to noise ratio only widens the uncertainty cell, and we keep it there with an explicit label that it is a best case bound.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng hai đại lượng gần nhau về độ lớn nên con số vẫn dùng được. Không nhận ra là hai đại lượng khác nhau về định nghĩa, nên không trả lời được phản bác.
- Mức {{s008}}: đổi tên cột thành phân giải nhưng vẫn giữ nguyên mọi câu kết luận về năng lực định vị ở các mục khác, nên bài tự mâu thuẫn giữa bảng và văn.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s013}}: đổi tên cột thành phân giải, khai rằng nó là trần ở tỉ số tín hiệu trên nhiễu cao, và báo thêm sai số ước lượng theo cận Cramer Rao như một hàm của tỉ số tín hiệu trên nhiễu.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The threat model in Section II lists device, radio and core interfaces, and the adversary capabilities read, modify, inject and physical access. Sensing derived location is produced by the network itself and is not a message on any of those interfaces. The model therefore has no row for it, and Section VI nevertheless draws a privacy conclusion. Please state where that data lives, how long it is kept, and who can read it.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have added the missing row and rewritten the conclusion on top of it. Section II now carries a fifth asset row, network generated location, with four fields: the data lives at the orchestration layer as range, velocity and angle estimates; it is retained for {{s034}} days to train the load prediction model; three roles can read it, namely the RAN operations role, the analytics role and the platform administrator; and the constraint is the role separation plus the configuration audit of Section III-A.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also state the generating party explicitly, because it changes which mechanisms apply: this data is produced by the network from the signal a user must transmit in order to be served, not submitted by the user, so consent mechanisms that rest on the user supplying data do not apply here, and the control point is retention and access rather than collection. Section VI now distinguishes instantaneous from historical privacy.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

A single {{s033}} square metre uncertainty cell at {{s001}} m is one point and does not identify a person, but {{s034}} days of such points form a trajectory, and a trajectory re identifies a person even when no single point does. We therefore report the retention period as the primary privacy parameter of the design and give the measured accuracy of re identification from trajectories in Section VI-B.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng dữ liệu cảm biến là dữ liệu nội bộ của nhà mạng nên nó nằm trong miền tin cậy. Đúng về mô tả triển khai, không trả lời được phản bác, vì mô hình đe doạ của chính bài đã có kẻ tấn công nội bộ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s008}}: thêm một dòng cho dữ liệu cảm biến vào bảng mô hình đe doạ, nhưng chỉ khai lớp chứa dữ liệu và bỏ thời gian giữ cùng danh sách truy cập.
- Mức {{s013}}: thêm đủ bốn dòng gồm lớp chứa dữ liệu, thời gian giữ, danh sách chủ thể đọc được, và cơ chế ràng buộc ba dòng trên; rồi xét lại kết luận riêng tư theo mô hình mới.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.8` bấm thẻ.
