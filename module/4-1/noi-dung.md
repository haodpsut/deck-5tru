---
tieu-de: Bề mặt tấn công: đọc kiến trúc trước khi nói về tấn công
phu-de: Trụ 4 6G Sec · module 4.1
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 84.5
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

Trong hệ tôi đang viết, mỗi giao diện kiến trúc tương ứng với năng lực nào của kẻ tấn công, và tôi đã khai đủ chưa?

## Mô hình đe doạ là một phép đếm
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này có đúng một việc: biến câu "hệ của tôi có thể bị tấn công" thành một **phép đếm kiểm được**. Phép đếm đó đi từ kiến trúc, không đi từ tên tấn công. Thứ tự bắt buộc là: liệt kê giao diện, gán năng lực cụ thể cho kẻ tấn công, rồi mới sinh danh mục đe doạ.

## Mô hình đe doạ là một phép đếm (tiếp)
@phut: 1
@che-do: noi

Quy tắc trung tâm, và cũng là chỗ reviewer của IEEE đánh mạnh nhất: **một mục đe doạ không có năng lực cụ thể của kẻ tấn công thì không phải đe doạ, chỉ là lo lắng**. Hệ quả là phần có giá trị nhất của một mô hình đe doạ tốt lại là *danh sách đe doạ bị loại*, vì nó chứng minh anh đã nghĩ tới và đã quyết, chứ không phải chưa nghĩ tới.

## Mô hình đe doạ là một phép đếm (tiếp)
@phut: 1
@che-do: noi

Thứ tự ngược lại là nguồn gốc của gần hết bài an ninh 6G bị trả: vẽ sơ đồ tấn công trước, rồi mới đi tìm kiến trúc nào khớp. Lúc đó mô hình đe doạ tự mâu thuẫn với phòng vệ được đề xuất ngay trong cùng một bài.

## Khái niệm tầng 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s001}} trên bốn.*

## Khái niệm tầng 1 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Theo thứ tự từ ngoài vào trong: **thiết bị** (device), **vô tuyến** (radio and air interface), **RAN phân tán và O-RAN** (disaggregated RAN), **lõi dịch vụ** (service based core), **lớp điều phối và AI** (orchestration and AI layer), **lớp dữ liệu và vận hành** (data and operations).

## Khái niệm tầng 1 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **bài báo chỉ được tuyên bố phủ lớp nào mà nó có giao diện cụ thể ở lớp đó**. Một bài đo trên vector đặc trưng của lưu lượng không phủ được lớp vô tuyến, và một bài mô phỏng xApp không phủ được lớp thiết bị. Khai thừa lớp là cách nhanh nhất để mất uy tín cả phần đánh giá.

## Khái niệm tầng 2
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Khái niệm tầng 2 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`E2` giữa near-RT RIC và nút RAN, `A1` giữa non-RT RIC và near-RT RIC, `O1` cho quản trị, `Open Fronthaul` giữa O-DU và O-RU, cộng `O2` cho lớp đám mây. Trên nền đó còn có **xApp và rApp của bên thứ ba** chạy ngay trong RIC.

## Khái niệm tầng 2 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **mở giao diện là mở bề mặt**. Lợi ích vận hành và chi phí an ninh phải nêu cùng nhau trong một câu, không nêu một bên. Một đoạn giới thiệu chỉ kể lợi ích của O-RAN là một đoạn mà reviewer sẽ đọc như quảng cáo, và nó làm yếu luôn phần phòng vệ phía sau vì phần đó không còn vấn đề nào để giải.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Năng lực là thứ kiểm được: **đọc** bản tin, **sửa** bản tin đang đi, **chèn** bản tin mới, **chặn** bản tin, **truy cập vật lý**, và **vị thế nội bộ** (insider position, ví dụ một xApp đã được nạp vào RIC). Ý định là thứ không kiểm được, nên không được dùng làm cơ sở phân loại.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **mỗi dòng trong bảng đe doạ phải trỏ tới đúng một năng lực trong danh sách trên**. Nếu không trỏ được thì dòng đó phải chuyển sang phần giả định, hoặc bị xoá. Đây là cách kiểm nhanh nhất một mô hình đe doạ, và cũng là cách nhanh nhất để tìm chỗ bài của mình tự mâu thuẫn: phòng vệ dựa biên giới mạng chỉ có nghĩa khi danh sách năng lực *không* chứa vị thế nội bộ.

## Đếm ô ma trận đe doạ theo năng lực được cấp
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`N_o = N_gd × N_hangmuc N_khathi = N_gd × N_nl N_biloai = N_gd × (N_hangmuc − N_nl) N_noibo = N_xapp × {{s003}} nếu vị thế nội bộ được cấp, ngược lại {{s005}}`

**Giả thiết nó đứng trên:**

## Đếm ô ma trận đe doạ theo năng lực được cấp (tiếp)
@phut: 1
@che-do: so

- Danh mục giao diện là đóng và đã biết hết, nên N_gd là một con số chứ không phải một chặn dưới
- Số hạng mục đe doạ soi trên mỗi giao diện là N_hangmuc = {{s004}}, lấy từ khung STRIDE
- Mỗi hạng mục đe doạ cần đúng một năng lực tương ứng, ánh xạ một-một, nên cấp N_nl năng lực thì có đúng N_nl hạng mục khả thi trên mỗi giao diện

## Đếm ô ma trận đe doạ theo năng lực được cấp (tiếp)
@phut: 1
@che-do: so

- Vị thế nội bộ là năng lực thứ sáu trong danh sách, nên nó chỉ được cấp khi N_nl đạt {{s004}}
- Mỗi xApp của bên thứ ba mở thêm {{s003}} hạng mục nội bộ: sửa dữ liệu, tiết lộ thông tin, nâng quyền

## Đếm ô ma trận đe doạ theo năng lực được cấp · ghi chú
@phut: 1
@che-do: noi

Ánh xạ một-một giữa hạng mục và năng lực là một **mô hình đếm khai rõ** để thấy cơ chế, không phải một kết quả thực nghiệm. Trong một bài báo thật, ánh xạ đó là một bảng do tác giả tự khai và tự bảo vệ. Cái mô hình này dùng để dạy là quan hệ: `N_khathi` đi tuyến tính theo số năng lực được cấp, còn `N_noibo` thì **nhảy bậc** khi vị thế nội bộ được cấp.

## Đếm ô ma trận đe doạ theo năng lực được cấp · ghi (tiếp)
@phut: 0.5
@che-do: noi

Nhảy bậc đó chính là chỗ phòng vệ dựa biên giới mạng mất hiệu lực.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s006}} | giao diện | Số giao diện mở chính của O-RAN cần kể được tên
!so {{s004}} | hạng mục | Khung STRIDE có bao nhiêu hạng mục đe doạ? Đây là số

## Bài của anh kể 5 giao diện mở (E2
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Bài của anh kể {{s006}} giao diện mở (E2, A1, O1, Open Fronthaul, O2) và soi từng giao diện bằng {{s004}} hạng mục STRIDE. Ma trận đe doạ đầy đủ có bao nhiêu ô?

gd = {{s006}}, hangMuc = {{s004}}

## Bài của anh kể 5 giao diện mở (E2 · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`gd × hangMuc`

{{s007}} ô. Đó là số ô mà bài của anh phải điền hoặc phải khai là không áp dụng, cùng với lý do. Một bảng đe doạ có {{s008}} dòng trong khi ma trận đầy đủ là {{s007}} ô thì chưa sai, nhưng nó buộc anh nói rõ {{s009}} ô kia đi đâu. Nếu không nói thì reviewer sẽ hỏi, và câu hỏi đó rất khó trả lời sau khi bài đã viết xong.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình đe doạ của anh cấp cho kẻ tấn công đúng {{s002}} trong {{s004}} năng lực, với ánh xạ một năng lực ứng một hạng mục. Trên {{s006}} giao diện, bao nhiêu ô bị loại vì không có năng lực tương ứng?

gd = {{s006}}, hangMuc = {{s004}}, nl = {{s002}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`gd × (hangMuc - nl)`

{{s010}} ô bị loại, tức đúng hai phần ba ma trận {{s007}} ô. Hai phần ba là một tỉ lệ lớn, và đó chính là lý do danh sách bị loại phải vào bài: nó cho reviewer thấy mô hình đe doạ của anh là một quyết định có lý do, không phải một danh sách ngắn vì anh nghĩ chưa tới. Và nó còn là cổng tự kiểm:

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

nếu phòng vệ của anh tuyên bố chặn một ô nằm trong {{s010}} ô đã bị loại thì bài tự mâu thuẫn.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bảng đe doạ có dòng ghi tấn công kênh phụ trên giao diện A1 nhưng không trỏ tới năng lực nào trong danh sách đã khai. Theo quy tắc của module, phải làm gì với dòng đó?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chuyển sang phần giả định và khai rõ là chưa gắn năng lực, hoặc xoá khỏi bảng
- Giữ lại và ghi là nằm ngoài phạm vi, không cần nói thêm
- Giữ lại, vì kênh phụ là đe doạ thật trong thực tế
- Gán cho nó năng lực đọc, vì kênh phụ luôn cần quan trắc

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chuyển sang phần giả định và khai rõ là chưa gắn năng lực, hoặc xoá khỏi bảng**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Quy tắc trung tâm là một mục đe doạ không có năng lực cụ thể thì không phải đe doạ, chỉ là lo lắng. Phương án gán năng lực đọc là tệ nhất trong bốn cái, vì nó đưa một phép gán bịa vào bảng để bảng trông đầy. Ghi nằm ngoài phạm vi mà không nói thêm cũng không đủ: phạm vi phải khai thành câu kiểm được, nếu không thì đó là chỗ trốn cho mọi thứ chưa nghĩ tới.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình đe doạ của một bài khai kẻ tấn công kiểm soát một xApp đã được nạp vào near-RT RIC. Phần phòng vệ của cùng bài đó đề xuất lọc bản tin E2 ở biên miền tin cậy và báo giảm {{s011}} số bản tin độc. Vấn đề nặng nhất là gì?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Giao diện E2 nên được thay bằng O1 cho an toàn hơn
- Con số {{s011}} thiếu khoảng tin cậy
- Phòng vệ đo trên một đường đi mà kẻ tấn công đã khai không hề dùng, nên con số không nói về mô hình đe doạ của bài
- Thiếu so sánh với một baseline học sâu

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Phòng vệ đo trên một đường đi mà kẻ tấn công đã khai không hề dùng, nên con số không nói về mô hình đe doạ của bài**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là ca tự mâu thuẫn kinh điển và nó nặng hơn mọi vấn đề thống kê: mô hình đe doạ đặt kẻ tấn công ở trong RIC, còn phòng vệ lại chặn ở biên. Con số {{s011}} có thể đúng tuyệt đối trên dữ liệu của nó và vẫn không trả lời câu hỏi nào của bài. Khoảng tin cậy và baseline là việc đáng làm, nhưng làm xong thì cái lỗi lập luận vẫn còn nguyên.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Anh muốn bảo vệ con số bề mặt tấn công trước một reviewer kể ra một giao diện anh bỏ sót. Cách khai nào làm con số vẫn còn giá trị sau cú đó?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Bỏ con số, chỉ để lại mô tả định tính
- Tăng con số lên cho an toàn, dự phòng giao diện chưa biết
- Khai con số là chính xác, vì sơ đồ đã được đồng nghiệp đọc lại
- Khai phạm vi bằng câu cụ thể và trình con số như chặn dưới trên phạm vi đó

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khai phạm vi bằng câu cụ thể và trình con số như chặn dưới trên phạm vi đó**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Khai phạm vi cộng trình con số như chặn dưới là cách duy nhất mà một giao diện bỏ sót làm con số CHẶT HƠN chứ không làm nó SAI. Khai chính xác là tự đặt mình vào chỗ một phản ví dụ phá được cả bảng. Bỏ con số thì mất luôn phần kiểm được. Tăng con số dự phòng là bịa, và còn tệ hơn vì không ai dựng lại được.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô hình đe doạ sau có một chỗ làm cả bảng không kiểm được. Bấm vào chỗ đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi xét kẻ tấn công kiểm soát một nút O-RU đã bị chiếm,
- với năng lực đọc và sửa bản tin trên Open Fronthaul, không có truy cập vào near-RT RIC,
- nên bảng đe doạ giữ {{s002}} trong {{s004}} hạng mục STRIDE trên giao diện đó và loại {{s012}} hạng mục kèm lý do.
- Hình {{s002}} liệt kê thêm tấn công nâng quyền và tấn công kênh phụ, để cho thấy bề mặt tấn công rộng.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Hình {{s002}} liệt kê thêm tấn công nâng quyền và tấn công kênh phụ, để cho thấy bề mặt tấn công rộng.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mục thêm vào không trỏ tới năng lực nào trong danh sách đã khai, nên chúng không phải đe doạ mà là lo lắng. Nặng hơn: nâng quyền đòi vị thế nội bộ hoặc truy cập RIC, đúng cái mà câu hai đã khai là KHÔNG có, nên Hình {{s002}} phủ định chính mô hình đe doạ ở trên nó. Ba đoạn đầu đều hợp lệ và viết đúng thứ tự.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Cách sửa rẻ nhất là chuyển hai mục đó sang một bảng riêng mang tên đe doạ bị loại, cùng lý do loại. Cách sửa tốt hơn là mở rộng danh sách năng lực nếu anh thật sự muốn xét chúng, và lúc đó phải viết lại cả phần phòng vệ cho khớp.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn giới thiệu sau có một câu làm yếu phần phòng vệ ở sau của chính bài. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Kiến trúc O-RAN tách RAN thành các khối chức năng nối với nhau bằng giao diện mở.
- Nhờ giao diện mở và xApp của bên thứ ba, nhà mạng thoát khoá nhà cung cấp, tối ưu được theo thời gian thực và giảm chi phí vận hành.
- Trong bài này chúng tôi chỉ xét các giao diện vẽ trong Hình {{s001}}, và không xét kênh cập nhật phần mềm.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Phần III dựng ma trận đe doạ cho từng giao diện theo khung STRIDE.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Nhờ giao diện mở và xApp của bên thứ ba, nhà mạng thoát khoá nhà cung cấp, tối ưu được theo thời gian thực và giảm chi phí vận hành.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Câu này kể bốn lợi ích mà không kể chi phí an ninh của chính việc mở giao diện, nên nó đọc như quảng cáo. Hậu quả không phải là giọng điệu mà là lập luận: nếu phần giới thiệu không nêu bề mặt tấn công mới thì phần phòng vệ ở sau không còn vấn đề nào để giải, và đóng góp của bài tự co lại. Cách sửa chỉ cần một mệnh đề nối:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

thêm vào ngay câu đó rằng mỗi giao diện mở và mỗi xApp của bên thứ ba đồng thời là một điểm vào mới, rồi trỏ tới ma trận đe doạ. Hai câu kia đều trung tính và không cần sửa.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bốn câu sau trích từ bốn mục khác nhau của cùng một bài. Một câu làm cả bài tự mâu thuẫn. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Mục III-A: kẻ tấn công của chúng tôi có vị thế nội bộ, cụ thể là một xApp độc đã qua được quy trình nạp.
- Mục III-B: do đó chúng tôi không giả định bất kỳ đường biên tin cậy nào bên trong RIC.
- Mục V-C: cơ chế đề xuất đặt bộ kiểm chính sách tại biên giữa RIC và nút RAN, và lọc được {{s011}} bản tin E2 độc.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Mục VI: chúng tôi chưa đánh giá chi phí tính toán của bộ kiểm chính sách dưới tải cao.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Mục V-C: cơ chế đề xuất đặt bộ kiểm chính sách tại biên giữa RIC và nút RAN, và lọc được {{s011}} bản tin E2 độc.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mục III đã khai kẻ tấn công ở BÊN TRONG RIC và khai thẳng là không có đường biên tin cậy bên trong. Mục V-C lại dựng phòng vệ ở một đường biên và đo trên lưu lượng qua đường biên đó, tức nó vừa dùng lại cái vừa bị phủ định, vừa đo trên một đường đi mà kẻ tấn công đã khai không dùng.

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Con số {{s011}} có thể đúng tuyệt đối và vẫn không nói gì về mô hình đe doạ của bài. Câu cuối thì hợp lệ vì nó khai giới hạn đúng chiều. Cách sửa: hoặc đổi mô hình đe doạ về kẻ tấn công ngoài miền tin cậy và khai thẳng là bài không xử xApp độc, hoặc giữ mô hình đe doạ và chuyển phòng vệ vào trong RIC, ví dụ xác thực và phân quyền giữa xApp với nền tảng.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Liệt kê N_gd giao diện của hệ, mỗi giao diện ghi hai đầu và loại dữ liệu đi qua
- Soi từng giao diện bằng N_hangmuc = {{s004}} hạng mục STRIDE, ra ma trận N_o = N_gd × {{s004}} ô
- Khai danh sách năng lực được cấp cho kẻ tấn công, N_nl trong sáu năng lực
- Giữ lại N_khathi = N_gd × N_nl ô, loại N_biloai = N_gd × ({{s004}} − N_nl) ô và ghi lý do loại

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Nếu vị thế nội bộ được cấp thì cộng thêm N_xapp × {{s003}} ô nội bộ, nằm ngoài ma trận giao diện
- In cả hai danh sách, giữ lại và bị loại, rồi kiểm từng dòng phòng vệ có trỏ về đúng một ô không

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: {{s006}} giao diện × {{s004}} hạng mục = {{s007}} ô; cấp {{s003}} năng lực nên {{s013}} ô khả thi và {{s013}} ô bị loại; {{s005}} ô nội bộ vì vị thế nội bộ chưa được cấp

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Kẻ tấn công ở ngoài miền tin cậy** tắt đi: Cho phép xApp của bên thứ ba đã được nạp vào RIC là kẻ tấn công, tức kẻ tấn công có vị thế nội bộ ngay từ đầu.
- **Mỗi hạng mục đe doạ ứng đúng một năng lực, ánh xạ một-một** tắt đi: Một hạng mục cần ghép nhiều năng lực cùng lúc, ví dụ phát lại cần cả đọc và chèn, còn một năng lực lại mở nhiều hạng mục.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Danh mục giao diện là đóng và biết hết** tắt đi: Còn cổng quản trị ngoài luồng, cổng gỡ lỗi, giao diện riêng của nhà cung cấp, hoặc kênh cập nhật phần mềm không nằm trong sơ đồ.
- **Giao diện mở được giám sát và ghi vết** tắt đi: Không có bản ghi trên E2 và A1, hoặc bản ghi bị chính kẻ tấn công xoá được.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Bộ đếm bề mặt tấn công theo năng lực kẻ tấn công. Đây là một mô hình đếm khai rõ ({{s004}} hạng mục STRIDE trên mỗi giao diện, ánh xạ một-một hạng mục với năng lực), không phải số đo thực nghiệm. Kéo số giao diện mở, số xApp của bên thứ ba và số năng lực được cấp, rồi đọc cả hai con số: ô khả thi và ô bị loại.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.1` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section III states that the adversary controls a malicious xApp already admitted into the near-RT RIC, yet the proposed defence in Section V-C is a policy checker placed at the boundary between the RIC and the RAN nodes. These two statements describe different adversaries. Please reconcile the threat model with the defence, and state which of the reported results survive under the threat model you actually claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree the two sections described different adversaries, and we have resolved this by narrowing the threat model rather than widening the defence. Section III now defines a single adversary A1 with the capabilities read, modify and inject on E2, no insider position and no physical access, and Table II lists all {{s007}} interface-by-STRIDE cells with the {{s013}} cells we exclude and the capability each exclusion rests on.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The boundary policy checker of Section V-C is matched to A1, and the {{s014}} percent figure is now reported as a bound for A1 only. The malicious-xApp adversary is moved to Section VI as explicitly out of scope, together with the reason: a boundary mechanism cannot bound an adversary that does not traverse the boundary, so reporting any filtering rate against it would be measuring the wrong path. We also added the counting model behind Table II so the cell counts can be reconstructed:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

{{s006}} interfaces, {{s004}} STRIDE items each, and one capability per item.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: trả lời rằng kẻ tấn công nội bộ vẫn phải gửi bản tin E2 nên bộ kiểm ở biên vẫn thấy. Sai, vì xApp độc tác động qua giao diện nội bộ của nền tảng RIC, không nhất thiết qua E2.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s002}}: thừa nhận lệch và nới mô hình đe doạ thành kẻ tấn công có thể ở trong hoặc ngoài RIC, nhưng giữ nguyên bảng kết quả. Lúc này mô hình đe doạ rộng hơn phòng vệ, nên con số vẫn không gắn với tuyên bố nào.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: chọn một trong hai và viết lại cho khớp. Nếu giữ kẻ tấn công nội bộ thì chuyển phòng vệ vào trong RIC và đo lại; nếu giữ phòng vệ ở biên thì hạ mô hình đe doạ về kẻ tấn công ngoài miền tin cậy và khai thẳng là bài không xử xApp độc.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Figure {{s002}} enumerates eleven attack names across the O-RAN interfaces, but the paper never states what the adversary can do. Without a capability set, the figure is not a threat model and the coverage claim in the abstract cannot be checked. Please provide the adversary model and justify the completeness claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced Figure {{s002}} with an explicit adversary model and a full matrix. Section III-A defines the capability set as read, modify, inject, block, physical access and insider position, and grants the adversary the first three. Table II is the complete 5-by-6 matrix over E2, A1, O1, Open Fronthaul and O2 against the six STRIDE items, with {{s013}} feasible cells and {{s013}} excluded cells; every exclusion names the missing capability.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Four of the eleven attack names in the old figure could not be mapped to any granted capability and have been moved to Section VI as assumptions we do not evaluate. The abstract no longer claims comprehensive coverage; it now claims coverage of the interfaces in Figure {{s001}} under adversary A1, and states that the cell count is a lower bound because vendor-specific and software-update channels are out of scope.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: thêm một đoạn văn nói kẻ tấn công là một tác nhân có động cơ kinh tế và có tài nguyên đáng kể. Đây là mô tả ý định, không kiểm được, nên nó không trả lời phản bác.
- Mức {{s002}}: thêm bảng năng lực nhưng vẫn giữ nguyên mười một tên tấn công, trong đó vài cái không trỏ được về năng lực nào. Bảng mới và hình cũ nói hai chuyện.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: khai năng lực bằng danh sách kiểm được (đọc, sửa, chèn, chặn, truy cập vật lý, vị thế nội bộ), gắn từng mục đe doạ về đúng một năng lực, và bỏ hoặc chuyển sang phần giả định những mục không gắn được.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The introduction argues that opening the RAN interfaces improves security because the system becomes auditable. Section III then counts {{s007}} threat cells across those same interfaces. One of these two statements has to be rewritten. Which one, and what is the correct formulation?

## Đáp mẫu
@phut: 1.5
@che-do: noi

The introduction was wrong and has been rewritten. Opening the interfaces increases the attack surface, and Section III now quantifies that: each additional open interface adds six STRIDE cells under our counting model. Auditability is a separate quantity: it improves detection after entry, not the number of entry points, so the two do not cancel. We also state the condition under which auditability is a defence at all, namely that the records are outside the control of the adversary.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Under our adversary A1 that holds, because A1 has no insider position. We note explicitly that for an insider adversary the records fall inside the adversary's reach and every detection rate we report would lose its evidentiary status, which is why the insider case is out of scope rather than silently covered.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s001}}: giữ cả hai và nói rằng hai câu nhìn vấn đề từ hai góc khác nhau. Không trả lời được, vì hai câu nói về cùng một đại lượng theo hai chiều trái nhau.
- Mức {{s002}}: hạ câu giới thiệu xuống dạng mềm hơn, kiểu giao diện mở có cả lợi ích và rủi ro, nhưng không gắn vào phép đếm nào.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: viết lại câu giới thiệu theo đúng hai đại lượng khác nhau: mở giao diện LÀM TĂNG bề mặt tấn công, đồng thời LÀM TĂNG khả năng quan trắc, và hai thứ đó không bù nhau vì một cái nói về điểm vào còn một cái nói về phát hiện sau khi vào.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.1` bấm thẻ.
