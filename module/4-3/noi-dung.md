---
tieu-de: An ninh của chính AI trong vòng điều khiển mạng
phu-de: Trụ 4 6G Sec · module 4.3
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 91
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

Nếu mô hình AI của tôi điều khiển tài nguyên mạng, kẻ tấn công đầu độc được nó bằng cách nào mà không cần truy cập máy chủ huấn luyện?

## An ninh của chính AI trong vòng điều khiển mạng
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Module này đổi chỗ đứng. Phần lớn bài an ninh học máy giả định kẻ tấn công phải chạm được vào tập huấn luyện hoặc vào máy chủ. Khi mô hình nằm trong vòng điều khiển mạng thì giả định đó không cần nữa: **dữ liệu quan trắc mà mô hình thu từ mạng chính là thứ kẻ tấn công sinh ra được**, vì kẻ tấn công cũng ở trong mạng đó.

## An ninh của chính AI trong vòng điều khiển mạng (tiếp)
@phut: 1
@che-do: noi

Ba đường tấn công, xếp từ dễ tới khó: đầu độc **dữ liệu quan trắc** mà mô hình thu từ mạng, đầu độc **nhãn** sinh tự động từ chỉ số vận hành, và tấn công **thời điểm suy luận** bằng cách tạo ra trạng thái mạng giả. Không đường nào trong ba đường cần truy cập máy chủ huấn luyện.

## An ninh của chính AI trong vòng điều khiển mạng (tiếp)
@phut: 1
@che-do: noi

Chỗ khác biệt quan trọng nhất phải nói được bằng một câu có chữ phản hồi: **quyết định của mô hình đổi dữ liệu ở bước sau, nên lỗi tự khuếch đại**. Một phân loại tĩnh bị đầu độc {{s001}} thì sai khoảng {{s001}}; một vòng kín bị đầu độc {{s001}} thì sai bao nhiêu còn phụ thuộc số bước, và đó là một đại lượng khác hẳn.

## An ninh của chính AI trong vòng điều khiển mạng (tiếp)
@phut: 1
@che-do: noi

Và ràng buộc khả thi, nối thẳng module {{s002}}: nhiễu đối kháng trong vòng điều khiển mạng phải sinh ra được bằng lưu lượng thật, nên nhiễu `L2` tuỳ ý trên vector đặc trưng **không phải** một tấn công.

## Khái niệm tầng 2
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Khái niệm tầng 2 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Một, **đầu độc dữ liệu quan trắc**: kẻ tấn công sinh lưu lượng làm lệch thống kê mà mô hình thu, rẻ nhất vì chỉ cần ở trong mạng. Hai, **đầu độc nhãn**: nhãn sinh tự động từ chỉ số vận hành, nên bẻ được chỉ số là bẻ được nhãn. Ba, **tấn công thời điểm suy luận**: tạo ra một trạng thái mạng giả để mô hình ra quyết định sai ngay lúc đó.

## Khái niệm tầng 2 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **mô hình đe doạ nào đòi kẻ tấn công phải truy cập máy chủ huấn luyện thì đã bỏ cả ba đường này**. Hệ quả viết bài: nếu phần giả định của anh viết kẻ tấn công không có quyền trên hạ tầng huấn luyện, thì phần đó phải nói thêm nó có hay không có quyền sinh lưu lượng trong mạng được quan trắc. Hai câu đó khác nhau, và câu thứ hai mới là câu quyết định.

## Khái niệm tầng 3
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Khái niệm tầng 3 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Trong phân loại tĩnh, dữ liệu vào không phụ thuộc đầu ra của mô hình, nên một mức đầu độc cho một mức sai cố định. Trong vòng điều khiển, **quyết định của mô hình đổi trạng thái mạng, trạng thái đó thành dữ liệu quan trắc ở bước sau**, nên sai lệch đi qua một đường PHẢN HỒI và tự khuếch đại theo số bước.

## Khái niệm tầng 3 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cùng một tỉ lệ đầu độc, hai kiến trúc cho hai đại lượng khác nhau**, nên không so được bằng một con số duy nhất. Hệ quả thực hành: bài của anh phải báo suy giảm theo SỐ BƯỚC, không báo một con số, và phải khai hệ số phản hồi đã dùng. Báo một con số cho hệ vòng kín là báo một điểm trên một đường cong mà không nói điểm nào.

## Khái niệm tầng 4
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s005}} trên bốn.*

## Khái niệm tầng 4 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Độ tin của mô hình, độ chính xác trực tuyến, tỉ lệ cảnh báo theo thời gian: cả ba đều tính TRÊN dữ liệu quan trắc. Khi dữ liệu quan trắc là thứ kẻ tấn công sinh ra được thì cả ba là chỉ số do một hệ đã bị tác động tự báo về.

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **một hệ bị tấn công thành công thường báo cáo rằng nó vẫn khoẻ, vì chính phép đo nằm trong tầm kẻ tấn công**. Nên không được dùng chỉ số tự báo làm bằng chứng an toàn. Cách xử chỉ có hai đường, và bài phải chọn một rồi khai thẳng:

## Khái niệm tầng 4 · đáp (tiếp)
@phut: 1
@che-do: noi

có một đường quan trắc độc lập với vòng điều khiển, hoặc không có, và lúc đó mọi tuyên bố an toàn hạ xuống thành tuyên bố về hành vi quan sát được trong điều kiện không bị tấn công. Đây gần đúng lớp lỗi của nhà: công cụ đo hỏng đọc thành kết quả âm.

## Mô hình khuếch đại dạng đóng cho vòng kín
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`D_tinh = r D_vong(n) = {{s007}} − ({{s007}} − r)^(1 + g·n) A(n) = D_vong(n) / r`

**Giả thiết nó đứng trên:**

- Đây là MÔ HÌNH ĐÓNG DẠNG để thấy cơ chế, không phải số đo thực nghiệm; mọi con số nó sinh ra là con số của mô hình này, không phải của một hệ thật
- r là tỉ lệ đầu độc trên dữ liệu quan trắc tại mỗi bước, và được giữ không đổi theo thời gian

## Mô hình khuếch đại dạng đóng cho vòng kín (tiếp)
@phut: 1
@che-do: so

- g là hệ số phản hồi, tức mức mà quyết định của mô hình đổi dữ liệu ở bước sau; g bằng {{s006}} nghĩa là không có phản hồi, tức bài toán thành phân loại tĩnh
- Số bước hiệu dụng là {{s007}} + g·n, nên ở n = {{s006}} thì vòng kín trùng đúng bản tĩnh và A(0) = {{s007}}

## Mô hình khuếch đại dạng đóng cho vòng kín (tiếp)
@phut: 1
@che-do: so

- Suy giảm được đo trên cùng một thang cho cả hai kiến trúc, nếu không thì hệ số A không có nghĩa

## Mô hình khuếch đại dạng đóng cho vòng kín · ghi chú
@phut: 1
@che-do: noi

Hai trường hợp biên kiểm được bằng tay, và chúng là lý do mô hình này dùng được để dạy. Ở `n = {{s006}}` thì số mũ bằng {{s007}} nên `D_vong = r`, tức hai kiến trúc BẰNG NHAU. Ở `r = {{s006}}` thì cơ số bằng {{s007}} nên `D_vong = {{s006}}` với mọi n, tức không đầu độc thì không suy giảm bất kể bao nhiêu bước. Dạng hàm {{s007}} trừ luỹ thừa cũng nói đúng một điều quan trọng:

## Mô hình khuếch đại dạng đóng cho vòng kín · ghi (tiếp)
@phut: 0.5
@che-do: noi

suy giảm **bão hoà**, nên một bài báo cho thấy đường suy giảm đi lên rồi phẳng không phải đã chứng minh hệ bền, nó chỉ đang ở phần bão hoà của chính đường cong đó.

## Số phải biết
@phut: 2
@che-do: so
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s005}} | nhóm ràng buộc | Pierazzi và cộng sự khai bao nhiêu nhóm ràng buộc trong không
!so {{s004}} | đường tấn công | Module này kể mấy đường tấn công vào mô hình trong vòng

## Dùng đúng mô hình đóng dạng đã khai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Dùng đúng mô hình đóng dạng đã khai, suy giảm vòng kín là {{s007}} trừ ({{s007}} trừ r) luỹ thừa ({{s007}} cộng g nhân n). Với tỉ lệ đầu độc r = {{s011}}, hệ số phản hồi g = {{s012}} và n = {{s010}} bước, suy giảm vòng kín là bao nhiêu phần trăm?

r = {{s008}}, g = {{s009}}, n = {{s010}}

## Dùng đúng mô hình đóng dạng đã khai · đáp
@phut: 1.5
@che-do: noi
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`{{s013}} × ({{s007}} - Math.pow(1 - r, {{s007}} + g × n))`

## Dùng đúng mô hình đóng dạng đã khai · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s014}}, trong khi bản phân loại tĩnh ở cùng mức đầu độc chỉ suy giảm {{s001}}, tức chênh gần mười lần. Nhắc lại cho đúng tư cách con số: đây là đầu ra của mô hình đóng dạng đã khai, không phải số đo thực nghiệm, nên nó dùng để lập luận về CƠ CHẾ chứ không dùng để báo kết quả. Cái dùng được trong bài báo là câu định tính kèm theo:

## Dùng đúng mô hình đóng dạng đã khai · đáp (tiếp)
@phut: 1
@che-do: noi

cùng một tỉ lệ đầu độc, hai kiến trúc cho hai đại lượng khác nhau, nên phải báo theo số bước.

## Vẫn mô hình đóng dạng đó. Với r = 0,05
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Vẫn mô hình đóng dạng đó. Với r = {{s011}}, hệ số phản hồi g = {{s007}} và n = {{s015}} bước, hệ số khuếch đại của vòng kín so với bản tĩnh bằng bao nhiêu?

r = {{s008}}, g = {{s007}}, n = {{s015}}

## Vẫn mô hình đóng dạng đó. Với r = 0,05 · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`({{s007}} - Math.pow(1 - r, {{s007}} + g × n)) / r`

## Vẫn mô hình đóng dạng đó. Với r = 0,05 · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s016}} lần, trong khi số bước hiệu dụng là {{s017}}. Hai con số lệch nhau, và chỗ lệch đó là điều đáng học: hệ số khuếch đại luôn NHỎ HƠN số bước hiệu dụng, vì suy giảm bị chặn trên bởi {{s018}} nên đường cong bão hoà. Hệ quả đọc ngược: hệ số khuếch đại đạt mức cao nhất ở vùng đầu độc rất nhỏ, đúng vùng mà kiểm chất lượng dữ liệu thông thường không bắt được.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Mô hình đe doạ của bài viết rằng kẻ tấn công không có quyền trên hạ tầng huấn luyện. Theo module này, câu đó còn thiếu dữ kiện nào để kiểm được?

- Kẻ tấn công có hay không quyền sinh lưu lượng trong mạng được quan trắc
- Số lượng tham số của mô hình
- Tần số lấy mẫu của bộ thu thập dữ liệu
- Kiến trúc mạng neural của mô hình

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Kẻ tấn công có hay không quyền sinh lưu lượng trong mạng được quan trắc**

Cả ba đường đầu độc của module đều không cần máy chủ huấn luyện: đường dữ liệu quan trắc, đường nhãn tự sinh, và đường thời điểm suy luận. Nên câu không có quyền trên hạ tầng huấn luyện không loại được đường nào trong ba đường, và dữ kiện quyết định là quyền sinh lưu lượng trong mạng được quan trắc.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Tần số lấy mẫu có ảnh hưởng tới mức dễ của tấn công nhưng nó không phải dữ kiện làm câu khai trở nên kiểm được.

## Hai hệ cùng bị đầu độc 5%
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai hệ cùng bị đầu độc {{s001}}: một phân loại tĩnh và một mô hình trong vòng điều khiển có phản hồi. Cách báo kết quả nào là cách duy nhất so sánh được?

## Hai hệ cùng bị đầu độc 5% (tiếp)
@phut: 0.5
@che-do: hoi

- Báo suy giảm của hệ vòng kín ở bước có suy giảm nhỏ nhất, để bi quan ít nhất
- Báo một con số suy giảm cho mỗi hệ, đo ở cuối thí nghiệm
- Báo suy giảm theo số bước cho hệ vòng kín, cùng với hệ số phản hồi đã dùng
- Báo trung bình suy giảm trên toàn bộ các bước của hệ vòng kín

## Hai hệ cùng bị đầu độc 5% · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Báo suy giảm theo số bước cho hệ vòng kín, cùng với hệ số phản hồi đã dùng**

Suy giảm của vòng kín là một hàm của số bước, nên một con số là một điểm trên đường cong mà không nói điểm nào. Báo ở cuối thí nghiệm thì rơi vào vùng bão hoà và che mất chỗ đáng chú ý. Trung bình trên các bước trộn vùng đầu với vùng bão hoà nên không dựng lại được.

## Hai hệ cùng bị đầu độc 5% · đáp (tiếp)
@phut: 1
@che-do: noi

Chọn bước có suy giảm nhỏ nhất là chọn ngưỡng cho khớp kết luận, đúng lớp lỗi nặng nhất của việc có số đo mà kết luận vẫn sai.

## Theo mô hình đóng dạng của module
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Theo mô hình đóng dạng của module, hệ số khuếch đại của vòng kín so với bản tĩnh đạt mức cao nhất ở vùng nào của tỉ lệ đầu độc, và vì sao điều đó quan trọng?

## Theo mô hình đóng dạng của module (tiếp)
@phut: 0.5
@che-do: hoi

- Không phụ thuộc tỉ lệ đầu độc, chỉ phụ thuộc số bước
- Ở vùng đầu độc trung bình, vì đó là chỗ đường cong dốc nhất
- Ở vùng đầu độc lớn, vì càng nhiều dữ liệu độc thì càng khuếch đại
- Ở vùng đầu độc nhỏ, vì suy giảm bị chặn trên nên tỉ số giảm khi mẫu số tăng, và vùng nhỏ chính là vùng kiểm chất lượng dữ liệu không bắt được

## Theo mô hình đóng dạng của module · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Ở vùng đầu độc nhỏ, vì suy giảm bị chặn trên nên tỉ số giảm khi mẫu số tăng, và vùng nhỏ chính là vùng kiểm chất lượng dữ liệu không bắt được**

## Theo mô hình đóng dạng của module · đáp (tiếp)
@phut: 1
@che-do: noi

Suy giảm vòng kín bị chặn trên bởi {{s018}} trong khi mẫu số r tăng tuyến tính, nên hệ số khuếch đại giảm khi r tăng và tiến tới số bước hiệu dụng khi r tiến tới {{s006}}. Hệ quả thực hành là chỗ đáng giá: một bài chỉ thử ở mức đầu độc lớn sẽ kết luận vòng kín không tệ hơn bản tĩnh bao nhiêu, và kết luận đó sai chiều ở đúng vùng mà hệ thật hay rơi vào.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn đánh giá độ bền sau có một câu làm cả phần đó không nói gì về mạng. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi huấn luyện bộ điều khiển trên dữ liệu quan trắc thu từ mười nút RAN trong bốn tuần.
- Để đánh giá độ bền đối kháng, chúng tôi sinh nhiễu bằng tối ưu trong quả cầu L2 bán kính epsilon {{s019}} trên vector đặc trưng đã chuẩn hoá.
- Mỗi cấu hình chạy {{s010}} hạt giống, và chúng tôi báo trung vị cùng khoảng giữa phân vị {{s020}} và {{s021}}.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi cũng đo suy giảm theo số bước vòng kín, với hệ số phản hồi khai trong Bảng III.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Để đánh giá độ bền đối kháng, chúng tôi sinh nhiễu bằng tối ưu trong quả cầu L2 bán kính epsilon {{s019}} trên vector đặc trưng đã chuẩn hoá.**

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Nhiễu trong một quả cầu L2 trên vector đặc trưng đã chuẩn hoá không ứng với một chuỗi gói tin nào mà kẻ tấn công sinh ra được, nên phép đo này đúng về tính toán và không nói gì về mạng. Nó còn chạm vào quy tắc trung tâm của trụ: không có phép biến đổi khả thi nào thì không có năng lực kẻ tấn công, nên đây là lo lắng chứ không phải đe doạ.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu kia đều hợp lệ, trong đó câu cuối là phần thú vị nhất của bài. Cách sửa: khai một tập phép biến đổi trên lưu lượng thật, ví dụ chèn luồng, dịch thời điểm, đổi kích thước gói, rồi sinh nhiễu bằng cách tìm trong tập đó. Nếu không làm được thì chuyển phần này sang phụ lục và nói rõ nó là phép đo trong không gian đặc trưng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một câu dùng chính hệ bị tấn công để chứng minh hệ an toàn. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi chạy chiến dịch đầu độc trên dữ liệu quan trắc trong {{s022}} bước vòng kín.
- Bộ thu thụ động nằm ngoài vòng điều khiển ghi lại trạng thái thật của mạng ở từng bước.
- Mô hình báo độ chính xác trực tuyến trên {{s023}} suốt chiến dịch, nên chúng tôi kết luận cơ chế của mình bền với đầu độc.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi chưa thử chiến dịch nhắm vào đường sinh nhãn, và nêu việc đó trong phần hạn chế.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Mô hình báo độ chính xác trực tuyến trên {{s023}} suốt chiến dịch, nên chúng tôi kết luận cơ chế của mình bền với đầu độc.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Độ chính xác trực tuyến tính trên chính dữ liệu quan trắc đã bị đầu độc, nên nó là chỉ số do một hệ đang bị tấn công tự báo về. Một hệ bị tấn công thành công thường báo rằng nó vẫn khoẻ, đúng vì phép đo nằm trong tầm kẻ tấn công. Chỗ làm câu này nặng hơn nữa là câu hai:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

bài ĐÃ CÓ một bộ thu thụ động ngoài vòng điều khiển, tức đã có đường quan trắc độc lập, mà kết luận lại dựa vào chỉ số tự báo. Cách sửa gần như không tốn gì: tính lại suy giảm bằng dữ liệu của bộ thu thụ động và báo con số đó làm kết quả chính, còn chỉ số tự báo thì để cạnh nó như một minh hoạ cho việc hệ không tự thấy mình bị tấn công.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Ba câu kia đều hợp lệ và câu cuối khai giới hạn đúng chiều.

## Câu nào không được số nào chống đỡ · ca ba
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Bốn câu sau trích từ bốn mục của cùng một bài. Một câu làm mô hình đe doạ của bài tự mâu thuẫn. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Mục III: kẻ tấn công không có quyền nào trên hạ tầng huấn luyện và không truy cập được tập dữ liệu lưu trữ.
- Mục III: kẻ tấn công kiểm soát một số thiết bị đầu cuối và sinh được lưu lượng trong mạng được quan trắc.
- Mục IV: tấn công của chúng tôi lật nhãn của {{s001}} mẫu trong tập huấn luyện bằng cách sửa trực tiếp tệp nhãn.

## Câu nào không được số nào chống đỡ · ca ba (tiếp)
@phut: 0.5
@che-do: hoi

- Mục V: chúng tôi báo suy giảm theo số bước, và khai hệ số phản hồi của từng cấu hình.

## Câu không được chống đỡ · ca ba · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Mục IV: tấn công của chúng tôi lật nhãn của {{s001}} mẫu trong tập huấn luyện bằng cách sửa trực tiếp tệp nhãn.**

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

Sửa trực tiếp tệp nhãn đòi quyền trên hạ tầng huấn luyện, đúng cái mà câu một đã khai là KHÔNG có, nên bài tự mâu thuẫn ngay trong hai mục liền nhau. Và nó bỏ mất đúng đường tấn công mạnh nhất mà câu hai vừa mở ra: nhãn sinh tự động từ chỉ số vận hành thì bẻ được chỉ số là bẻ được nhãn, không cần chạm vào tệp nào. Cách sửa cũng là cách làm bài mạnh hơn:

## Câu không được chống đỡ · ca ba · đáp (tiếp)
@phut: 1
@che-do: noi

thực hiện việc bẻ nhãn qua đường chỉ số vận hành, rồi báo tỉ lệ nhãn bị bẻ như một đại lượng dẫn xuất chứ không như một tham số tự đặt. Ba câu kia đều hợp lệ, và câu cuối là cách khai độ phủ đúng chiều.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Đặt phần dữ liệu còn lành sau một bước là ({{s007}} − r)
- Trong phân loại tĩnh, chỉ có một bước, nên suy giảm D_tinh = {{s007}} − ({{s007}} − r) = r
- Trong vòng kín, quyết định ở bước i đổi dữ liệu ở bước i+1, nên mỗi bước nhân thêm một lần hệ số ({{s007}} − r) với trọng số g

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Sau n bước, phần còn lành là ({{s007}} − r)^(1 + g·n), nên D_vong(n) = {{s007}} − ({{s007}} − r)^(1 + g·n)
- Lấy tỉ số A(n) = D_vong(n) / r để có hệ số khuếch đại so với bản tĩnh
- Kiểm hai biên: n = {{s006}} cho A = {{s007}}, và r = {{s006}} cho D_vong = {{s006}}

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: tỉ lệ đầu độc {{s001}}, hệ số phản hồi {{s012}}, {{s010}} bước: bản tĩnh suy giảm {{s001}}, vòng kín suy giảm khoảng {{s014}}, hệ số khuếch đại khoảng {{s024}} lần

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Dữ liệu quan trắc đáng tin** tắt đi: Kẻ tấn công sinh được lưu lượng trong mạng được quan trắc, nên dữ liệu mà mô hình thu đã nằm một phần trong tầm của nó.
- **Nhiễu đối kháng sinh ra được bằng lưu lượng thật** tắt đi: Cho phép nhiễu tuỳ ý trên vector đặc trưng, tức bỏ ràng buộc không gian vấn đề.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Quyết định của mô hình đổi dữ liệu ở bước sau, tức có phản hồi** tắt đi: Mô hình chỉ quan sát và báo cáo, không tác động lên tài nguyên mạng, nên bài toán thành phân loại tĩnh.
- **Nhãn sinh tự động từ chỉ số vận hành là nhãn đúng** tắt đi: Kẻ tấn công đổi được chỉ số vận hành, nên đổi được nhãn mà quy trình tự gán.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Vòng kín so với phân loại tĩnh ở cùng tỉ lệ đầu độc. KHAI RÕ: đây là một mô hình đóng dạng để thấy cơ chế khuếch đại, KHÔNG phải số đo thực nghiệm; mọi con số dưới đây là con số của công thức {{s007}} trừ ({{s007}} trừ r) luỹ thừa ({{s007}} cộng g nhân n), không phải của một hệ thật. Kéo tỉ lệ đầu độc, số bước vòng kín và hệ số phản hồi.

## Chỗ này phải tự kéo, không xem được (tiếp)
@phut: 1
@che-do: demo

*Mở `https://hoc-5-tru-web.vercel.app/#/module/4.3` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V concludes that the controller is robust to poisoning because the online accuracy reported by the model stays above {{s025}} percent throughout the campaign. That metric is computed on the very observation stream the attacker is perturbing, so it cannot serve as evidence of safety. Please provide an evaluation that does not depend on data under adversarial control.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept the objection and have changed the evidence, not the wording. Section IV-C now describes a passive collector outside the control loop: it observes the same links but no decision of the controller affects what it records, so its stream is not under the control of the adversary in the same way. Table VII reports degradation computed from that independent stream, per closed loop step, for poisoning rates from {{s026}} to {{s010}} percent, and this is now the primary result.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The online accuracy reported by the model is kept in Figure {{s027}} but relabelled as a self-reported quantity, placed next to the independent measurement precisely to show the gap: the model reports above {{s025}} percent while the independent stream shows a far larger degradation, which is the point of the figure rather than a result. We also state the fallback explicitly:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

without an independent observation path, no claim of robustness to poisoning is supportable, and the strongest statement available would be about behaviour under the absence of attack.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s007}}: trả lời rằng độ chính xác trực tuyến được tính trên một tập giữ lại, nên nó khách quan. Không trả lời được phản bác nếu tập giữ lại cũng lấy từ cùng dòng quan trắc.
- Mức {{s003}}: thêm khoảng tin cậy và nhiều hạt giống cho chỉ số tự báo. Siết thống kê trên một phép đo đã mất tư cách bằng chứng thì không đổi được tư cách đó.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: dựng một đường quan trắc độc lập với vòng điều khiển, ví dụ một bộ thu thụ động mà mô hình không tác động tới, rồi báo suy giảm tính trên dòng dữ liệu đó làm kết quả chính.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The adversarial robustness evaluation in Section VI perturbs the normalised feature vector inside an L2 ball. For a controller that consumes network telemetry, it is not clear that any sequence of packets realises such a perturbation. Please either show that the perturbations are realisable in the problem space or withdraw the robustness claim.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced the feature-space evaluation with a problem-space one. Section VI-A now defines a transformation set over real traffic, namely injecting additional flows from controlled endpoints, shifting transmission times within a bounded window, and changing packet sizes within protocol limits, and each transformation is annotated with the problem-space constraint group it satisfies and with its cost to the attacker.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The attack is now a search over that set rather than an optimisation in an L2 ball, and Table IX reports degradation as a function of the attacker budget measured in injected flows per minute, which is a quantity an operator can reason about. The former L2 result is retained in Appendix B and relabelled as a loose upper bound on what any realisable attack could achieve, not as a robustness measurement, since the feasible set is strictly smaller than the ball.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s007}}: trả lời rằng nhiễu L2 là chuẩn mực trong lĩnh vực học máy đối kháng. Đúng về thực hành ở ảnh, không trả lời được cho dữ liệu mạng.
- Mức {{s003}}: giảm bán kính nhiễu cho nhỏ hơn và lập luận rằng nhiễu nhỏ thì khả thi. Bán kính nhỏ không làm một phép biến đổi không tồn tại trở nên tồn tại.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: khai một tập phép biến đổi trên lưu lượng thật, ví dụ chèn luồng, dịch thời điểm, đổi kích thước gói, rồi sinh nhiễu bằng cách tìm trong tập đó và báo lại độ bền theo tập ấy.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table VI reports a single degradation figure for the closed loop system and a single figure for the static baseline at the same poisoning rate, and concludes that the closed loop design is only mildly more fragile. Since degradation in the closed loop depends on the number of steps and on the feedback strength, a single number does not identify what was measured. Please restate the comparison.

## Đáp mẫu
@phut: 1.5
@che-do: noi

Table VI has been replaced. We now report degradation as a function of the closed loop step for each configuration, with the feedback strength stated for every row, and we compare against the static baseline step by step rather than at a single point. We also swept the poisoning rate across three orders of magnitude, from {{s026}} percent to {{s010}} percent. The sweep reverses our earlier conclusion:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

the amplification relative to the static baseline is largest at the smallest poisoning rates, because closed loop degradation is bounded above while the static reference grows linearly with the poisoning rate. This matters operationally because the small-rate region is exactly the region that routine data quality checks do not flag.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We state explicitly that our previous single-number comparison was taken at a high poisoning rate, which is the saturated part of the curve, and that reporting it that way understated the gap in the direction that favoured our own design.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s007}}: thêm độ lệch chuẩn cho hai con số và giữ nguyên cách so. Độ phân tán không nói được điểm nào trên đường cong đã được báo.
- Mức {{s003}}: báo con số của vòng kín ở bước cuối cùng của thí nghiệm, coi đó là trường hợp xấu nhất. Bước cuối thường nằm trong vùng bão hoà, nên con số này che mất vùng đáng chú ý nhất.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: báo suy giảm theo số bước cho hệ vòng kín, khai hệ số phản hồi của từng cấu hình, và so với bản tĩnh ở từng bước thay vì tại một điểm.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/4.3` bấm thẻ.
