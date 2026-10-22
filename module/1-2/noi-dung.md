---
tieu-de: Dataset và vết thương riêng của từng cái
phu-de: Trụ 1 NID · module 1.2
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 72.5
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

Với dataset tôi đang dùng, con số tôi báo bị thổi lên bởi cơ chế nào, và tôi phải khai gì để reviewer không đánh vào chỗ đó?

## Mỗi dataset có một vết thương
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này không xếp hạng dataset. Nó làm một việc hẹp hơn và dùng được ngay: với mỗi dataset, chỉ ra **cơ chế** làm con số của anh cao hơn khả năng tổng quát hoá thật, rồi quy cơ chế đó thành một phép tính anh làm được trên giấy.

## Mỗi dataset có một vết thương (tiếp)
@phut: 1
@che-do: noi

Ba cơ chế chính, và chỉ ba: **Trùng bản ghi.** Nhân một lớp lên r lần thì trọng số của lớp đó trong trung bình đổi, nên accuracy quan sát dịch về phía lớp đó. Khả năng tổng quát hoá không đổi một chút nào. **Rò rỉ đặc trưng (feature leakage).** Một đặc trưng đơn lẻ gần như xác định được nhãn.

## Mỗi dataset có một vết thương (tiếp)
@phut: 1
@che-do: noi

Đó là dấu hiệu quy trình sinh dữ liệu đã mã hoá nhãn vào đầu vào, không phải dấu hiệu mô hình giỏi. **Nhiễu nhãn.** Nó đặt một trần cho accuracy quan sát và co khoảng cách giữa hai mô hình lại. Hai mô hình chênh một điểm phần trăm ở vùng {{s001}} thì chênh lệch đó nằm dưới mức nhiễu nhãn có thể gây ra. Khai ba thứ này vào bài không làm con số của anh xấu đi.

## Mỗi dataset có một vết thương (tiếp)
@phut: 1
@che-do: noi

Nó lấy đi của reviewer đúng cái cây gậy mà họ hay dùng, và đổi lại anh phải bỏ chữ tổng quát hoá ra khỏi những câu mà nó không đứng được.

## Rò rỉ đặc trưng (feature leakage)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Rò rỉ đặc trưng (feature leakage) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khi một đặc trưng đầu vào mang thông tin về nhãn không phải vì cơ chế an ninh, mà vì cách dữ liệu được sinh ra hoặc được dán nhãn. Dò bằng thông tin tương hỗ một biến: `I(X_i; Y)` gần `H(Y)` nghĩa là một biến đơn lẻ gần như xác định được nhãn.

## Rò rỉ đặc trưng (feature leakage) · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** `I(X_i; Y)` gần `H(Y)` là **dấu hiệu rò rỉ**, không phải dấu hiệu mô hình giỏi. Trong các corpus IDS, cổng đích và thời lượng luồng (flow) là hai chỗ rò rỉ hay gặp nhất, vì kịch bản sinh lưu lượng gán sẵn chúng cho từng loại tấn công.

## Trần hiệu năng do nhiễu nhãn (label noise ceiling)
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Trần hiệu năng do nhiễu nhãn (label noise ceiling) · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Nếu nhãn bị lật đối xứng với tỉ lệ `ε`, thì một mô hình đúng thật hoàn hảo cũng chỉ đạt accuracy quan sát `{{s004}} − ε`. Và khoảng cách thật `δ` giữa hai mô hình chỉ còn quan sát được là `δ · ({{s004}} − 2ε)`.

## Trần hiệu năng do nhiễu nhãn (label noise (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** trần này chặn mọi mô hình như nhau, nên nó không phải cái cớ để báo số thấp. Nó là cái dùng để nói rằng một chênh lệch nhỏ ở vùng gần trần **không phân biệt được**. Với `ε` bằng {{s005}}, trần là {{s006}} và mọi con số quan sát cao hơn {{s006}} trên cùng tập nhãn đó cần một lời giải thích khác, thường là ghi nhớ bản trùng.

## Bản ghi trùng, và nó phá thứ gì
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s002}} trên bốn.*

## Bản ghi trùng, và nó phá thứ gì · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Khi cùng một bản ghi xuất hiện nhiều lần, hai chuyện xảy ra cùng lúc: trọng số của lớp bị nhân lên đổi, và tập kiểm tra có thể chứa đúng bản ghi đã nằm trong tập huấn luyện.

## Bản ghi trùng, và nó phá thứ gì · đáp (tiếp)
@phut: 1
@che-do: noi

**Điểm phải nhớ:** chuyện thứ nhất làm con số lệch và vẫn *sửa được bằng cách tính lại*. Chuyện thứ hai thì không: lúc đó accuracy quan sát là một hỗn hợp của ghi nhớ và tổng quát hoá với tỉ lệ pha không biết, nên **hiệu năng ngoài mẫu không còn định nghĩa được** từ con số đó. Cách duy nhất là bỏ trùng rồi đo lại, và khai cả hai con số.

## Hai vết thương đo được: trọng số do trùng bản ghi
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`Tỉ lệ lớp A sau khi nhân r lần = r·p_A / (r·p_A + {{s004}} − p_A) I(X_i; Y) = Σ p(x,y) · log( p(x,y) / (p(x) · p(y)) )`

**Giả thiết nó đứng trên:**

## Hai vết thương đo được: trọng số do trùng bản ghi (tiếp)
@phut: 1
@che-do: so

- nhân bản không thêm thông tin, nên độ chính xác trong từng lớp không đổi và chỉ trọng số của lớp đổi
- đủ mẫu để ước lượng p(x,y), nếu không thì I bị thiên lệch dương theo số ô của bảng tần số
- X_i rời rạc hoặc đã rời rạc hoá, và cách rời rạc hoá là một phần của phép đo chứ không trung lập

## Hai vết thương đo được: trọng số do trùng bản ghi · ghi
@phut: 1
@che-do: noi

Hai cách đọc bắt buộc. Thứ nhất, **đi kèm một điều kiện null**: chạy lại `I` trên nhãn đã trộn ngẫu nhiên và in giá trị null cạnh giá trị thật, vì bộ ước lượng cắm vào có thiên lệch dương tăng theo số ô và giảm theo số mẫu. Thứ hai, so với `H(Y)` chứ không so với {{s007}}:

## Hai vết thương đo được: trọng số do trùng bản ghi (tiếp)
@phut: 0.5
@che-do: noi

tỉ số `I(X_i; Y) / H(Y)` là con số đọc được, và nó gần {{s004}} thì phải đi kiểm quy trình sinh dữ liệu trước khi đọc bất cứ con số hiệu năng nào.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s008}} | % | Trong tập huấn luyện của KDD99
!so {{s009}} | bản ghi | Tập KDDTrain+ của NSL-KDD có bao nhiêu bản ghi?
!so {{s010}} | bản ghi | Tập KDDTest+ của NSL-KDD có bao nhiêu bản ghi?

## Số phải biết (tiếp)
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s011}} | đặc trưng | UNSW-NB15 gồm khoảng {{s012}} triệu bản ghi và {{s013}} họ tấn công.
!so {{s014}} | đặc trưng | CIC-IDS2017 thu lưu lượng {{s015}} ngày liên tiếp từ thứ Hai tới

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nhãn trong dataset bị lật đối xứng với tỉ lệ {{s005}}. Một mô hình đúng thật {{s018}} so với nhãn sạch sẽ cho accuracy quan sát bao nhiêu phần trăm khi chấm trên nhãn nhiễu?

a = {{s016}}, eps = {{s017}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s019}} × (a × ({{s004}} - eps) + ({{s004}} - a) × eps)`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

{{s020}}, phân số đúng {{s021}}. Trần của accuracy quan sát với {{s005}} nhãn lật là {{s006}}, đạt bởi một mô hình đúng thật {{s022}}. Nên một bài báo khai accuracy quan sát {{s018}} trên cùng tập nhãn đó đang báo con số CAO HƠN trần, và chỉ có hai lối giải thích: nhãn không nhiễu tới {{s005}}, hoặc con số đang đo khả năng ghi nhớ bản trùng chứ không đo khả năng tổng quát hoá.

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Hệ quả thứ hai, dùng ngay khi phản biện: khoảng cách thật {{s023}} điểm phần trăm giữa hai mô hình chỉ còn quan sát được {{s024}} điểm, vì nó bị co theo hệ số ({{s004}} − 2ε) = {{s025}}.

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

KDD99 có khoảng {{s028}} bản ghi huấn luyện là bản trùng. Giả sử toàn bộ phần trùng rơi vào một lớp, và lớp đó chiếm {{s029}} tập bản ghi duy nhất. Lớp đó chiếm bao nhiêu phần trăm tập có trùng?

du = {{s026}}, pa = {{s027}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s019}} × (du + ({{s004}} - du) × pa)`

{{s030}}, phân số đúng {{s031}}. Một bộ phân loại tầm thường luôn trả lớp đó đạt accuracy {{s030}} trên tập có trùng, trong khi trên tập bản ghi duy nhất nó chỉ đạt {{s029}}. Chênh {{s032}} điểm phần trăm ấy không phải mô hình, nó là bản trùng. Đó là lý do một con số accuracy trên KDD99 không so được với bất cứ thứ gì, và cũng là lý do NSL-KDD ra đời.

## Trên một corpus IDS
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Trên một corpus IDS, một đặc trưng đơn lẻ có I(X_i; Y) đo được bằng {{s033}} lần H(Y). Đọc con số này thế nào?

## Trên một corpus IDS (tiếp)
@phut: 0.5
@che-do: hoi

- Mô hình chưa học đủ, cần thêm tầng hoặc thêm tham số
- Không đọc được, vì thông tin tương hỗ cần biết tỉ lệ nền (base rate) của mạng đích
- Đặc trưng đó là tín hiệu an ninh mạnh, nên giữ lại và nhấn mạnh trong bài
- Dấu hiệu nhãn đã được mã hoá sẵn vào đặc trưng, phải kiểm quy trình sinh dữ liệu trước khi đọc bất cứ con số hiệu năng nào

## Trên một corpus IDS · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Dấu hiệu nhãn đã được mã hoá sẵn vào đặc trưng, phải kiểm quy trình sinh dữ liệu trước khi đọc bất cứ con số hiệu năng nào**

## Trên một corpus IDS · đáp (tiếp)
@phut: 1
@che-do: noi

Một biến đơn lẻ xác định được gần hết nhãn là chuyện gần như không xảy ra trong lưu lượng thật, vì tấn công thật không mang một trường nào chỉ thẳng ra nó là tấn công. Khi nó xảy ra trong một corpus thì lời giải thích nhiều khả năng hơn là kịch bản sinh lưu lượng đã gán sẵn trường đó cho từng loại tấn công. Lưu ý thêm:

## Trên một corpus IDS · đáp (tiếp)
@phut: 1
@che-do: noi

thông tin tương hỗ tính trong chính dataset nên không cần tỉ lệ nền của mạng đích, nhưng nó cần một điều kiện null trên nhãn đã trộn ngẫu nhiên để biết sàn thiên lệch của bộ ước lượng.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

NSL-KDD bỏ bản trùng của KDD99. Việc đó chữa được vết thương nào, và KHÔNG chữa được vết thương nào?

## Chọn một phương án (tiếp)
@phut: 0.5
@che-do: hoi

- Chữa trùng bản ghi, nhưng không làm dữ liệu trở nên đại diện cho lưu lượng và cho họ tấn công hiện nay
- Không chữa gì, chỉ đổi tên và đổi cách chia
- Chữa rò rỉ đặc trưng, vì bỏ trùng làm giảm thông tin tương hỗ của từng đặc trưng
- Chữa trùng bản ghi, và chữa luôn chuyện dữ liệu mô tả một mạng của thập niên {{s034}}

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chữa trùng bản ghi, nhưng không làm dữ liệu trở nên đại diện cho lưu lượng và cho họ tấn công hiện nay**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Bỏ trùng xử lý đúng một cơ chế: trọng số lệch và tập kiểm tra chồng tập huấn luyện. Nó không chạm tới nguồn gốc của dữ liệu, nên mọi lập luận kiểu dữ liệu này đại diện cho mạng hôm nay vẫn không đứng được. Nó cũng không chạm tới rò rỉ đặc trưng: bỏ bản trùng không đổi quan hệ giữa một đặc trưng và nhãn, chỉ đổi số mẫu dùng để ước lượng quan hệ đó.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đánh giá sau có một câu không được chống đỡ bởi dữ liệu nào trong bài. Bấm vào câu đó.

- Chúng tôi đánh giá trên KDDTrain+ và KDDTest+ của NSL-KDD, gồm {{s035}} và {{s036}} bản ghi.
- Mô hình đạt F1 {{s037}} trên KDDTest+, cao hơn ba baseline gần nhất.
- Kết quả này cho thấy phương pháp sẵn sàng bảo vệ hạ tầng doanh nghiệp hiện nay.
- Thời gian huấn luyện là {{s038}} phút trên một GPU đơn.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Kết quả này cho thấy phương pháp sẵn sàng bảo vệ hạ tầng doanh nghiệp hiện nay.**

Hai câu trước đều kiểm được: một câu khai hiện vật, một câu khai con số đo trên hiện vật đó. Câu này nhảy từ một con số trên corpus dẫn xuất từ lưu lượng mô phỏng của thập niên {{s034}} sang một kết luận về hạ tầng hiện nay, mà trong bài không có một mẫu nào từ hạ tầng hiện nay. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

hoặc bỏ câu kết luận và nói rõ phạm vi là NSL-KDD, hoặc thêm một corpus gần đây cộng một lần đánh giá chia theo thời gian, rồi báo cả hai con số.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn mô tả đặc trưng sau có một chỗ làm toàn bộ phần kết quả mất hiệu lực. Bấm vào chỗ đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi dùng toàn bộ {{s014}} đặc trưng mà CICFlowMeter sinh ra cho mỗi luồng.
- Không có bước chọn đặc trưng nào, nên không có nguy cơ rò rỉ từ việc chọn đặc trưng trên tập kiểm tra.
- Vì dùng hết tập đặc trưng gốc mà không can thiệp, biểu diễn đầu vào của chúng tôi là trung lập.
- Mọi đặc trưng được chuẩn hoá bằng tham số tính trên riêng tập huấn luyện.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì dùng hết tập đặc trưng gốc mà không can thiệp, biểu diễn đầu vào của chúng tôi là trung lập.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu trước đều đúng và đáng khai: dùng hết đặc trưng, và không có rò rỉ từ bước chọn đặc trưng. Câu này đổi nghĩa chữ trung lập: không can thiệp vào tập đặc trưng không làm tập đó trung lập, vì chính CICFlowMeter đã quyết định đo gì, và kịch bản sinh lưu lượng đã gán sẵn cổng đích với thời lượng luồng cho từng loại tấn công.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Dùng hết {{s014}} đặc trưng là nhận nguyên biểu diễn đó, kể cả phần mã hoá sẵn nhãn. Cách sửa: in I(X_i; Y) chia H(Y) cho từng đặc trưng cùng giá trị null trên nhãn đã trộn, rồi báo hiệu năng ở cả hai cấu hình có và không có nhóm nghi rò rỉ.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn báo kết quả sau có một chỗ trộn hai thứ không trộn được. Bấm vào chỗ đó.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Tập đánh giá gồm luồng TCP và luồng UDP, hai nhóm có phân bố thời lượng khác nhau hẳn.
- Chúng tôi báo kết quả riêng cho từng giao thức trong Bảng VI.
- Để gọn, phần abstract báo một khoảng chung cho cả hai giao thức: F1 từ {{s039}} tới {{s040}}.
- Bảng VI khai số luồng của từng giao thức trong tập đánh giá.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Để gọn, phần abstract báo một khoảng chung cho cả hai giao thức: F1 từ {{s039}} tới {{s040}}.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Hai câu trước là cách làm đúng: nhận ra hai phân bố khác nhau, và báo riêng từng cái. Câu này gộp hai phân bố vào một khoảng, nên con số trong abstract không ứng với bất cứ tình huống vận hành nào: không có mạng nào vừa là TCP vừa là UDP theo tỉ lệ ngầm đã dùng để sinh khoảng đó, và người đọc không có cách nào biết đầu nào của khoảng thuộc giao thức nào. Cách sửa:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

abstract báo hai con số có tên giao thức, hoặc báo con số của giao thức xấu hơn kèm một câu nói rõ đó là trường hợp xấu hơn.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt p_A là tỉ lệ lớp A trên tập bản ghi DUY NHẤT, acc_A và acc_B là độ chính xác thật trong từng lớp
- Nhân lớp A lên r lần thì khối lượng lớp A thành r·p_A, còn lớp B vẫn là {{s004}} − p_A
- Tỉ lệ lớp A sau khi nhân = r·p_A / (r·p_A + {{s004}} − p_A)
- Accuracy quan sát là trung bình của acc_A và acc_B có trọng số theo khối lượng MỚI

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Accuracy quan sát = (r·p_A·acc_A + ({{s004}} − p_A)·acc_B) / (r·p_A + {{s004}} − p_A)
- Độ thổi phồng = (r − 1)·p_A·(1 − p_A)·(acc_A − acc_B) / (r·p_A + {{s004}} − p_A)

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: Accuracy quan sát {{s018}} · F1 {{s037}} · hơn baseline mạnh nhất {{s023}} điểm phần trăm

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Nhãn trong dataset là đúng** tắt đi: Giả lập {{s005}} nhãn bị lật đối xứng, đúng mức mà một quy trình dán nhãn tự động theo kịch bản sinh lưu lượng có thể sai.
- **Bản ghi trong tập kiểm tra không xuất hiện trong tập huấn luyện** tắt đi: Dùng KDD99 nguyên bản, nơi khoảng {{s028}} bản ghi huấn luyện là bản trùng và phần trùng vắt qua cả hai tập.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Đặc trưng không mã hoá sẵn nhãn** tắt đi: Cổng đích và thời lượng luồng trong corpus sinh theo kịch bản cho I(X_i; Y) gần H(Y), tức một biến đơn lẻ gần như xác định được nhãn.
- **Tỉ lệ lớp trong dataset là tỉ lệ thật của mạng đích** tắt đi: Corpus có tỉ lệ tấn công hàng chục phần trăm, trong khi mạng thật thường ở mức phần vạn hoặc thấp hơn.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Cùng một mô hình, cùng một độ chính xác trong từng lớp. Kéo hệ số nhân bản và xem con số trong bảng kết quả đi lên trong khi mô hình không học thêm gì cả.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/1.2` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The evaluation rests on NSL-KDD and CIC-IDS2017. Two concerns. First, the reported accuracy above {{s041}} percent on NSL-KDD lies in the range attributable to residual record redundancy and to label noise rather than to the proposed architecture: with symmetric label noise of a few percent, the observable ceiling is below your reported figure, and a {{s042}} point margin over the baseline is not separable. Second, the CICFlowMeter feature set encodes artifacts of the traffic generation procedure, in particular destination port and flow duration.

## Phản biện hỏi (tiếp)
@phut: 1
@che-do: hoi

Please demonstrate that the reported gain is not explained by either effect.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept both concerns and have separated them into two measurements rather than one defence. On label noise: we now report an estimated symmetric flip rate for the evaluation labels and the observable ceiling it implies. At a flip rate of {{s015}} percent the ceiling on observed accuracy is {{s043}} percent and a true gap of {{s042}} points is attenuated to {{s044}} points, so we no longer present the absolute figure as the headline.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table III now leads with the paired comparison under identical preprocessing for both systems, with a confidence interval, and Section V-C states explicitly that margins of about one point in this regime are not separable. On redundancy: we deduplicate by record key before splitting, report both the deduplicated and the original numbers side by side, and confirm that no test record appears in the training partition. On feature leakage:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Table IV lists I(X_i; Y) divided by H(Y) for every feature together with a null value computed on randomly permuted labels, which identifies destination port and flow duration as the two leaking groups. We report performance in both configurations: F1 drops from {{s045}} to {{s046}} when those groups are removed, and we state plainly that this ablation does not prove the remaining features are leak free.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, Section VI adds a recent corpus with a strictly temporal split, and the deployability discussion now rests on that result rather than on NSL-KDD.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s004}}: trả lời rằng hai dataset này là chuẩn của lĩnh vực và được dùng rộng rãi. Đúng về thực hành, không trả lời được điều gì trong phản bác.
- Mức {{s002}}: thêm độ lệch chuẩn qua nhiều hạt giống và một lần cắt thử nhóm đặc trưng nghi rò rỉ, nhưng vẫn giữ nguyên câu kết luận và vẫn báo con số cũ làm con số chính.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s003}}: khai một ước lượng cho tỉ lệ nhãn sai, chỉ ra trần quan sát được và nói rõ khoảng cách nào phân biệt được ở trần đó; cộng in thông tin tương hỗ chia H(Y) cho từng đặc trưng với một điều kiện null; cộng báo hiệu năng ở cả hai cấu hình có và không có nhóm cổng đích và thời lượng luồng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/1.2` bấm thẻ.
