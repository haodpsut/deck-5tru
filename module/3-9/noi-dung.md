---
tieu-de: Định tuyến trong chòm sao: liên kết giữa vệ tinh và đồ thị động
phu-de: Trụ 3 NTN · module 3.9
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
@phan: NTN
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Đường ngắn nhất theo số chặng trong chòm sao của tôi có phải đường trễ thấp nhất không, và vì sao bảng định tuyến của tôi có hạn sử dụng?

## Định tuyến trong chòm sao: liên kết giữa vệ tinh và đồ
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Từ {{s001}} tới {{s002}}, mọi con số đều của **một** vệ tinh với **một** chặng: cao độ, góc nâng, khoảng xiên (slant range), trễ, Doppler. Module này đổi đối tượng: chòm sao là một **đồ thị**, các đỉnh là vệ tinh, các cạnh là liên kết giữa vệ tinh (inter-satellite link, ISL), và đồ thị đó **đổi theo thời gian**.

## Định tuyến trong chòm sao: liên kết giữa vệ tinh (tiếp)
@phut: 1
@che-do: noi

Hai thứ phải cài vào tay. Thứ nhất, **độ dài một chặng là hình học, không phải một tham số mô phỏng**. Với quỹ đạo tròn và `T_mp` vệ tinh chia đều pha trong một mặt phẳng, khoảng cách trong mặt phẳng là `2(R_E+h)·sin(π/T_mp)`, và ở {{s003}} km với {{s004}} vệ tinh mỗi mặt phẳng nó là **{{s005}} km**, tức trễ một chặng **{{s006}} ms**. Không cần mô phỏng để biết con số đó.

## Định tuyến trong chòm sao: liên kết giữa vệ tinh (tiếp)
@phut: 1
@che-do: noi

Thứ hai, **đếm chặng không phải đo trễ**. Chặng trong mặt phẳng không đổi theo vĩ độ, còn chặng sang mặt phẳng bên co theo `cos` vĩ độ: với {{s007}} mặt phẳng ở {{s003}} km, nó là {{s008}} km ở xích đạo và {{s009}} km ở vĩ độ {{s010}} độ. Nên hai đường cùng số chặng có thể chênh trễ rất xa, và câu *đường ngắn nhất theo số chặng* không phải câu *đường trễ thấp nhất*.

## Định tuyến trong chòm sao: liên kết giữa vệ tinh (tiếp)
@phut: 1
@che-do: noi

Một cảnh báo về chính module này: **chu kỳ đổi cấu trúc đồ thị là con số tôi KHÔNG khai**. Nó cần một chòm sao thật kèm luật vĩ độ ngắt liên kết ngang, và tôi không có hai thứ đó. Module dạy được *vì sao* đồ thị đổi và *hệ quả* của việc nó đổi, chứ không dạy *bao nhiêu lần một giờ*.

## Khái niệm tầng 1
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s011}} trên bốn.*

## Khái niệm tầng 1 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`T_mp` vệ tinh chia đều pha trên một quỹ đạo tròn bán kính `a = R_E + h`. Hai vệ tinh kề nhau cách nhau góc tâm `2π/T_mp`, nên dây cung giữa chúng là `d_ISL = 2(R_E+h)·sin(π/T_mp)`.

## Khái niệm tầng 1 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **đại lượng tỉ lệ là BÁN KÍNH QUỸ ĐẠO, không phải cao độ**. Hạ cao độ về {{s012}} thì khoảng cách không về {{s012}}, nó về `2·R_E·sin(π/T_mp)`, tức {{s013}} km ở {{s004}} vệ tinh mỗi mặt phẳng. Thứ đưa khoảng cách về {{s012}} là `T_mp` tiến tới vô cùng. Lẫn hai chuyện này là lỗi gõ công thức hay gặp nhất ở đây.

## Khái niệm tầng 2
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa và **điểm phải nhớ**, rồi lật.

*Tầng {{s014}} trên bốn.*

## Khái niệm tầng 2 · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

`P` mặt phẳng chia đều {{s015}} độ kinh của nút lên. Hai mặt phẳng kề nhau cách nhau góc `2π/P` ở xích đạo, nhưng các mặt phẳng gặp nhau ở vùng cực, nên khoảng cách giữa hai vệ tinh ở hai mặt phẳng kề nhau tại vĩ độ `φ` xấp xỉ `2(R_E+h)·sin(π/P)·cos φ`.

## Khái niệm tầng 2 · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **cùng một số chặng cho hai trễ khác nhau**, vì chặng ngang ở vĩ độ cao ngắn hơn chặng ngang ở xích đạo. Ở {{s003}} km với {{s007}} mặt phẳng: {{s008}} km ở xích đạo, {{s009}} km ở vĩ độ {{s010}} độ, và về {{s012}} ở cực. Chính chỗ về {{s012}} đó là lý do vật lý phải TẮT liên kết ngang gần cực: tốc độ quay ăng ten để giữ bắt đường ngắm tăng vô hạn.

## Đồ thị động, và hạn sử dụng của một bảng định tuyến
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s016}} trên bốn.*

## Đồ thị động, và hạn sử dụng của một bảng định tuyến ·
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Vì liên kết ngang bị tắt gần vùng cực, **bậc của một đỉnh đổi theo vị trí quỹ đạo**. Đồ thị chòm sao không phải một đồ thị, nó là một họ đồ thị theo thời gian.

## Đồ thị động, và hạn sử dụng của một bảng định (tiếp)
@phut: 1
@che-do: noi

Ba hệ quả phải nói được trong một câu mỗi cái. Một, **bảng định tuyến có hạn sử dụng**: tính trên một ảnh chụp đồ thị thì chỉ đúng cho một khoảng thời gian. Hai, **trễ trung bình phải khai trung bình trên cái gì**: trên tập cặp nào, ở vĩ độ nào, và với luật ngắt nào, đúng như yêu cầu ở {{s017}}.

## Đồ thị động, và hạn sử dụng của một bảng định (tiếp)
@phut: 1
@che-do: noi

Ba, với một số cặp nguồn đích ở một số thời điểm thì **không còn đường nào trong chòm sao**, lưu lượng phải xuống mặt đất, và lúc đó trễ ISL không còn là đại lượng mô tả hệ.

Điểm phải nhớ: **một con số trễ ISL duy nhất cho một chòm sao là một con số chưa khai đủ điều kiện**, không phải một con số sai.

## Khoảng cách liên kết
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`d_ISL = 2(R_E+h)·sin(π/T_mp) d_ngang(φ) = 2(R_E+h)·sin(π/P)·cos φ τ_chặng = d/c n_chặng ≈ ceil( D·T_mp / (2π·R_E) ) τ_sợi = D·n_g/c`

**Giả thiết nó đứng trên:**

## Khoảng cách liên kết (tiếp)
@phut: 1
@che-do: so

- Quỹ đạo tròn, T_mp vệ tinh chia đều pha trong một mặt phẳng, nên góc tâm giữa hai vệ tinh kề nhau đúng bằng 2π/T_mp
- P mặt phẳng chia đều {{s015}} độ kinh của nút lên, tức khuôn Walker delta, nên hai mặt phẳng kề nhau cách nhau góc 2π/P tại xích đạo
- Đường ngắm giữa hai vệ tinh không bị Trái Đất chắn, và liên kết ngang đang BẬT ở vĩ độ đang xét

## Khoảng cách liên kết (tiếp)
@phut: 1
@che-do: so

- c = {{s018}} km/s trong chân không, và n_g = {{s019}} là chiết suất nhóm của sợi đơn mode ở {{s020}} nm
- Số chặng là ƯỚC LƯỢNG chỉ đếm chặng trong mặt phẳng: hai thiết bị cách nhau D trên mặt đất thì hai vệ tinh phục vụ chúng cách nhau cùng góc tâm D/R_E, và mỗi chặng trong mặt phẳng tiến được 2π/T_mp của góc đó

## Khoảng cách liên kết (tiếp)
@phut: 1
@che-do: so

- Trễ chỉ gồm trễ lan truyền, không gồm trễ xếp hàng, trễ xử lý, và trễ bắt đường ngắm ở mỗi vệ tinh

## Khoảng cách liên kết · ghi chú
@phut: 1
@che-do: noi

Hai phép kiểm biên bắt buộc làm trước khi dùng. Một, đặt `T_mp = {{s021}}` thì `sin(π/6) = {{s022}}` nên `d_ISL = R_E + h` đúng bằng bán kính quỹ đạo, tức {{s023}} km ở `h = {{s003}}`. Hai, đặt `φ = {{s024}}` độ thì `cos φ = {{s012}}` nên `d_ngang = {{s012}}`: các mặt phẳng gặp nhau ở cực.

## Khoảng cách liên kết · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

Công thức `d_ngang` là xấp xỉ bậc một theo khoảng cách kinh tuyến, nó bỏ qua hiệu ứng pha tương đối giữa hai mặt phẳng, nên dùng được để so bậc độ lớn chứ không dùng để báo chữ số thứ ba.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s005}} | km | Khoảng cách liên kết giữa hai vệ tinh kề nhau trong cùng
!so {{s025}} | ms | Trễ lan truyền một chiều của một chặng ISL dài {{s026}} km
!so {{s027}} | lần | Chiết suất nhóm của sợi quang đơn mode tiêu chuẩn ở bước

## Cao độ 1200 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s028}} km, {{s029}} vệ tinh mỗi mặt phẳng. Khoảng cách liên kết trong mặt phẳng là bao nhiêu km?

h = {{s028}}, tmp = {{s029}}

## Cao độ 1200 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`2⋆(6378+h)⋆Math.sin(Math.PI/tmp)`

Khoảng {{s030}} km, tức {{s031}} lần con số {{s005}} km ở cao độ {{s003}} km với {{s004}} vệ tinh mỗi mặt phẳng. Hai thứ kéo ngược nhau ở đây: cao độ tăng {{s032}} lần theo bán kính quỹ đạo nên kéo khoảng cách LÊN, còn số vệ tinh mỗi mặt phẳng tăng {{s033}} lần nên kéo khoảng cách XUỐNG qua sin(π/T_mp). Hệ số thứ hai thắng. Bài học vận hành:

## Cao độ 1200 km · đáp (tiếp)
@phut: 1
@che-do: noi

muốn chặng ngắn thì tăng mật độ trong mặt phẳng, không phải hạ cao độ, vì cao độ chỉ vào qua R_E + h và R_E đã là {{s034}} km.

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s003}} km, {{s004}} vệ tinh mỗi mặt phẳng, cặp nguồn đích cách nhau {{s036}} km trên mặt đất. Trễ tổng qua chòm sao là bao nhiêu ms, gồm hai chặng lên xuống ở đỉnh đầu?

h = {{s003}}, tmp = {{s004}}, dd = {{s035}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`Math.ceil(dd⋆tmp/(2⋆Math.PI⋆6378))⋆2⋆(6378+h)⋆Math.sin(Math.PI/tmp)/299.792458 + 2⋆h/299.792458`

Khoảng {{s037}} ms, với {{s038}} chặng ISL. Cáp quang trên cùng {{s036}} km cho {{s039}} ms, nên biên của chòm sao là {{s040}} ms, rộng hơn hẳn biên {{s041}} ms ở cặp {{s042}} km. Cơ chế: phần lên xuống {{s043}} ms là hằng số theo khoảng cách, còn phần ISL và phần sợi đều tỉ lệ với khoảng cách, nên biên mở ra theo khoảng cách.

## Cao độ 550 km · đáp (tiếp)
@phut: 1
@che-do: noi

Đây là lý do đúng để nói chòm sao có lợi thế trễ trên tuyến đường DÀI, và nó khác hẳn lý do hay bị viết, câu nói vì ánh sáng đi trong chân không.

## Cao độ 550 km
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cao độ {{s003}} km, {{s007}} mặt phẳng, một chặng sang mặt phẳng bên tại vĩ độ {{s010}} độ. Khoảng cách chặng đó là bao nhiêu km?

h = {{s003}}, np = {{s007}}, lat = {{s010}}

## Cao độ 550 km · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`2⋆(6378+h)⋆Math.sin(Math.PI/np)⋆Math.cos(lat⋆Math.PI/180)`

Khoảng {{s044}} km, tức {{s045}} lần con số {{s046}} km ở xích đạo, đúng bằng cos {{s010}} độ. Đặt cạnh chặng trong mặt phẳng {{s026}} km thì ra điều quan trọng nhất của module: ở cấu hình này một chặng ngang rẻ hơn một chặng dọc {{s047}} lần về trễ. Nên hai đường cùng {{s021}} chặng chênh trễ rất xa:

## Cao độ 550 km · đáp (tiếp)
@phut: 1
@che-do: noi

đường {{s021}} chặng dọc dài {{s048}} km tức {{s049}} ms, còn đường {{s050}} dọc {{s050}} ngang ở vĩ độ {{s010}} độ dài {{s051}} km tức {{s052}} ms, chỉ bằng {{s053}} lần. Bất cứ ai lấy số chặng làm đại diện cho trễ đều sai theo cách không bù trừ được.

## Hai vệ tinh kề nhau trong cùng một mặt phẳng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hai vệ tinh kề nhau trong cùng một mặt phẳng, {{s004}} vệ tinh mỗi mặt phẳng. Cho cao độ tiến tới {{s012}} thì khoảng cách liên kết trong mặt phẳng tiến tới đâu?

- Tới {{s013}} km, tức 2·R_E·sin(π/22)
- Tới {{s012}}
- Tới {{s003}} km
- Tới 2·R_E, tức {{s054}} km

## Hai vệ tinh kề nhau trong cùng một mặt phẳng · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tới {{s013}} km, tức 2·R_E·sin(π/22)**

Khoảng cách là 2(R_E+h)·sin(π/T_mp), tỉ lệ với bán kính quỹ đạo R_E + h chứ không với cao độ h. Cho h về {{s012}} thì bán kính về R_E = {{s034}} km, nên khoảng cách về 2·6378·sin(π/22) = {{s013}} km. Đại lượng đưa khoảng cách về {{s012}} là T_mp tiến tới vô cùng, và đại lượng cho 2·R_E là T_mp bằng {{s014}}, tức hai vệ tinh đối xuyên tâm.

## Hai vệ tinh kề nhau trong cùng một mặt phẳng · (tiếp)
@phut: 1
@che-do: noi

Lẫn cao độ với bán kính quỹ đạo là lỗi gõ công thức phổ biến nhất ở chỗ này.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Đường ít chặng nhất trong chòm sao khi nào KHÔNG phải đường trễ lan truyền thấp nhất?

- Không bao giờ, ít chặng nhất luôn cho trễ thấp nhất
- Chỉ khi có trễ xếp hàng ở mỗi vệ tinh
- Khi các chặng trên đường đi dài khác nhau, vì chặng ngang co theo cos vĩ độ
- Chỉ khi chòm sao có nhiều hơn một tầng cao độ

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Khi các chặng trên đường đi dài khác nhau, vì chặng ngang co theo cos vĩ độ**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Trễ lan truyền của một đường là tổng ĐỘ DÀI chia c, không phải số chặng chia gì cả. Ở {{s003}} km, chặng dọc là {{s026}} km với {{s004}} vệ tinh mỗi mặt phẳng và không đổi theo vĩ độ, còn chặng ngang với {{s007}} mặt phẳng là {{s046}} km ở xích đạo và {{s044}} km ở vĩ độ {{s010}} độ. Nên hai đường cùng {{s021}} chặng chênh trễ tới {{s055}} lần:

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

{{s049}} ms cho đường toàn chặng dọc so với {{s052}} ms cho đường {{s050}} dọc {{s050}} ngang ở vĩ độ {{s010}} độ. Trễ xếp hàng là một cơ chế khác và nó cộng theo số chặng, nên nó còn làm đường ít chặng nhất có lợi thêm chứ không làm mất lợi thế. Nhiều tầng cao độ là một cấu hình đặc biệt, không phải điều kiện cần.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Một bài báo khai trễ ISL trung bình {{s056}} ms cho chòm sao của họ, không nói gì thêm. Thiếu đúng một nhóm dữ kiện để người khác dựng lại con số đó. Nhóm nào?

- Băng tần của liên kết giữa vệ tinh
- Công suất phát của ăng ten liên kết ngang
- Tổng số vệ tinh trong chòm sao
- Tập cặp nguồn đích, vĩ độ dùng để lấy trung bình, và luật ngắt liên kết ngang

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Tập cặp nguồn đích, vĩ độ dùng để lấy trung bình, và luật ngắt liên kết ngang**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Trễ ISL là hàm của hình học và của cấu trúc đồ thị, nên một con số trung bình chỉ có nghĩa khi khai trung bình trên tập cặp nào, ở dải vĩ độ nào, và với luật tắt liên kết ngang nào, đúng cùng một yêu cầu đã nêu ở module {{s017}}. Băng tần và công suất phát vào ngân sách đường truyền chứ không vào trễ lan truyền.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Tổng số vệ tinh một mình không cho ra số vệ tinh mỗi mặt phẳng, và đó mới là đại lượng duy nhất vào công thức khoảng cách chặng.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn so sánh sau có một dòng làm dấu của kết luận bị lật. Bấm vào dòng đó.

## Câu nào không được số nào chống đỡ · ca một (tiếp)
@phut: 0.5
@che-do: hoi

- Chòm sao mô phỏng ở cao độ {{s003}} km, {{s004}} vệ tinh mỗi mặt phẳng, {{s007}} mặt phẳng.
- Khoảng cách liên kết trong mặt phẳng là {{s026}} km, nên trễ lan truyền một chặng là {{s057}} ms.
- Đường ngắn nhất cho cặp cách nhau {{s042}} km là {{s021}} chặng, tức {{s049}} ms, cộng hai chặng lên xuống {{s043}} ms thành {{s058}} ms.
- So với {{s042}} km cáp quang, tức {{s059}} ms, chòm sao chậm hơn {{s060}} ms.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**So với {{s042}} km cáp quang, tức {{s059}} ms, chòm sao chậm hơn {{s060}} ms.**

Sợi quang không truyền ở tốc độ ánh sáng trong chân không. Với chiết suất nhóm {{s019}} thì {{s042}} km sợi cho {{s061}} ms, không phải {{s059}} ms. Nên chòm sao NHANH HƠN {{s041}} ms chứ không chậm hơn {{s060}} ms, và dấu của kết luận bị lật. Ba mệnh đề đầu đều dựng lại được từ hình học và đều đúng. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

luôn nhân {{s019}} cho chặng sợi, và khai thêm rằng tuyến sợi thật dài hơn đường tròn lớn vì nó đi theo địa hình và theo tuyến cáp biển, nên biên thật của chòm sao còn rộng hơn {{s041}} ms.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau có một câu không dẫn ra được từ dữ kiện đã khai. Bấm vào câu đó.

## Câu nào không được số nào chống đỡ · ca hai (tiếp)
@phut: 0.5
@che-do: hoi

- Chúng tôi chạy định tuyến đường ngắn nhất theo trọng số độ dài trên đồ thị chòm sao lấy tại một thời điểm.
- Trễ ISL trung bình trên {{s042}} cặp nguồn đích lấy mẫu đều theo diện tích mặt cầu là {{s062}} ms.
- Vì chòm sao gần đều, bảng định tuyến tính một lần này dùng được cho toàn bộ thời gian mô phỏng.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**Vì chòm sao gần đều, bảng định tuyến tính một lần này dùng được cho toàn bộ thời gian mô phỏng.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Liên kết ngang phải tắt gần vùng cực, vì các mặt phẳng tụ lại ở đó và tốc độ quay ăng ten để giữ bắt đường ngắm tăng quá nhanh. Nên bậc của một đỉnh đổi theo vị trí quỹ đạo và cấu trúc đồ thị đổi theo thời gian: đồ thị gần đều ở một thời điểm không có nghĩa nó là CÙNG một đồ thị ở thời điểm sau.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Bảng tính trên một ảnh chụp có hạn sử dụng, và với một số cặp ở một số thời điểm thì không còn đường nào trong chòm sao. Hai mệnh đề đầu hợp lệ nếu khai rõ thời điểm chụp và tập cặp. Cách sửa: khai chu kỳ tính lại bảng và cách chọn nó, báo trễ theo thời gian chứ không một con số, và báo tỉ lệ cặp không có đường tại mỗi thời điểm. Lưu ý:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

chu kỳ đổi cấu trúc đồ thị là con số module này cố tình KHÔNG khai, vì nó cần một chòm sao thật kèm vĩ độ ngắt.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- T_mp vệ tinh chia đều pha trên một vòng tròn bán kính a = R_E + h, nên góc tâm giữa hai vệ tinh kề nhau là 2π/T_mp
- Tâm Trái Đất O và hai vệ tinh kề nhau S1, S2 tạo tam giác cân với OS1 = OS2 = a và góc đỉnh 2π/T_mp
- Hạ đường cao từ O xuống dây S1S2: nó chia đôi cả góc đỉnh và dây, nên nửa dây bằng a·sin(π/T_mp)

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Nhân hai: d_ISL = 2a·sin(π/T_mp) = 2(R_E+h)·sin(π/T_mp)
- Kiểm biên: T_mp = {{s021}} cho sin(π/6) = {{s022}} nên d_ISL = R_E + h, và cho h về {{s012}} thì d_ISL về 2·R_E·sin(π/T_mp) chứ KHÔNG về {{s012}}

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: h {{s003}} km · {{s004}} vệ tinh mỗi mặt phẳng · {{s007}} mặt phẳng · cặp cách {{s042}} km → d_ISL {{s026}} km · trễ một chặng {{s057}} ms · {{s021}} chặng · trễ tổng {{s058}} ms · cáp quang {{s061}} ms · biên {{s041}} ms

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Liên kết ngang luôn bật, ở mọi vĩ độ** tắt đi: Liên kết sang mặt phẳng bên bị tắt khi vệ tinh vượt một vĩ độ ngắt, vì tốc độ quay ăng ten để giữ bắt đường ngắm tăng quá nhanh khi các mặt phẳng tụ lại gần cực.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Mọi chặng dài như nhau, tức bỏ qua vĩ độ của chặng ngang** tắt đi: Chặng ngang co theo cos vĩ độ, nên độ dài một chặng phụ thuộc chỗ nó nằm trên quỹ đạo.
- **Trễ chỉ gồm trễ lan truyền** tắt đi: Mỗi vệ tinh cộng thêm trễ xếp hàng, trễ chuyển mạch và trễ bắt lại đường ngắm, nên trễ tỉ lệ cả với số chặng chứ không chỉ với tổng độ dài.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Biết ephemeris của mọi vệ tinh ở một thời điểm chung** tắt đi: Mỗi vệ tinh chỉ biết lân cận của nó và một đồng hồ lệch, nên không ai dựng được đồ thị đầy đủ tại một thời điểm.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Năm thanh kéo, sáu con số. Kéo cao độ, số vệ tinh mỗi mặt phẳng, số mặt phẳng, vĩ độ của chặng ngang và khoảng cách của cặp nguồn đích. Đồ thị là trễ tổng qua chòm sao theo cao độ, có vạch mốc ở cao độ mà chòm sao hoà với cáp quang cùng khoảng cách.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/3.9` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section V reports a single average inter-satellite propagation delay of {{s063}} ms and uses it throughout the evaluation. The routing graph in Fig. {{s021}} appears to be a single snapshot. Please state the source destination set and the latitude range used for the average, state the cross-plane link cutoff latitude, and justify using one static graph for a time varying topology.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We have replaced the single figure by a distribution. Table VI now reports inter-satellite propagation delay for the {{s064}} source destination pairs grouped by the absolute latitude of the pair midpoint, in six bands from {{s012}} to {{s065}} degrees, with median and interquartile range in each band. The reason the single number was misleading is geometric and is now stated in Section V-A:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

at {{s003}} km with {{s004}} satellites per plane the intra plane hop is {{s066}} km and does not vary with latitude, whereas with {{s007}} planes the cross plane hop is {{s067}} km at the equator and {{s068}} km at {{s010}} degrees latitude, so two paths with the same hop count can differ in delay by a factor of up to {{s069}}, which is the ratio between a six intra plane hop path at {{s070}} ms and a three plus three mixed path at {{s071}} ms.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also now state the cross plane cutoff latitude explicitly in Table I, together with the antenna slew rate limit that sets it. On the static graph, we agree it was not justified.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Section V-B now evaluates a sequence of topology snapshots over one full orbital period, states the table recomputation interval and how it was chosen, and reports the fraction of pairs with no in constellation path at each snapshot, which rises from zero at low latitude pairs to a nonzero value for pairs whose shortest path crosses the cutoff.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Finally, Table VII separates the ideal global shortest path delay, which is a lower bound, from the delay of the distributed forwarding rule we actually implement, and reports the ratio between them.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s011}}: trả lời rằng chòm sao gần đều nên một con số trung bình là đại diện hợp lý. Đúng về trực giác, không trả lời được điều reviewer hỏi.
- Mức {{s014}}: khai tập cặp nguồn đích và dải vĩ độ dùng để lấy trung bình, nhưng vẫn giữ một đồ thị tĩnh và vẫn báo một con số trễ duy nhất.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s050}}: khai tập cặp và dải vĩ độ, khai vĩ độ ngắt liên kết ngang, và báo trễ theo dải vĩ độ của cặp kèm độ phân tán, thay cho một con số trung bình.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

The paper claims the proposed routing scheme is near optimal because it finds paths within one hop of the minimum hop path. Hop count is not latency. Please justify hop count as the optimization objective, or report path length and end to end delay instead.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We accept the objection and have changed the objective. Section IV now minimizes total path length, with per hop switching delay added as an explicit weight whose value and measurement source are stated in Table I. The geometric reason is now given in Section IV-A:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

an intra plane hop at {{s003}} km with {{s004}} satellites per plane is {{s066}} km, while a cross plane hop with {{s007}} planes is {{s067}} km at the equator and shrinks as the cosine of latitude, so hop count and path length are different objectives and minimizing one does not minimize the other. Table V now reports, on the same {{s064}} pairs, the minimum hop path and the minimum delay path side by side:

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

they coincide for pairs whose shortest path uses only intra plane hops, and differ by up to {{s069}} times in delay for pairs whose path crosses planes at high latitude. The optimality gap of our scheme is now stated against the minimum delay path and in milliseconds, not against the minimum hop path and in hops. We have removed the phrase near optimal where it referred to hop count only.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s011}}: trả lời rằng số chặng là thước đo tiêu chuẩn trong tài liệu định tuyến chòm sao. Đúng về thực hành, không trả lời được phản bác.
- Mức {{s014}}: thêm độ dài đường đi bên cạnh số chặng, nhưng vẫn giữ số chặng làm hàm mục tiêu và vẫn gọi kết quả là gần tối ưu.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s050}}: đổi hàm mục tiêu sang tổng độ dài đường đi, chỉ ra bằng hình học vì sao số chặng không đại diện được cho trễ, và báo lại khoảng cách tới tối ưu theo trễ chứ không theo chặng.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/3.9` bấm thẻ.
