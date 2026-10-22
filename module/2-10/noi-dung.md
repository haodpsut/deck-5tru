---
tieu-de: Hệ thống thật: kẻ chậm, client rơi, và thiên lệch do lấy mẫu
phu-de: Trụ 2 FL · module 2.10
tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng
noi-ngay: Tự ôn, bộ Năm trụ
profile: giang-day
tong-phut: 78
accent: "#2C6E9B"
ngon-ngu: vi
gate: khong
nguon: kho Năm trụ · https://hoc-5-tru-web.vercel.app
moc-ngay: bản kho 2026.10.06-2
---

## !cover
@phan: FL
@phut: 0.5
@che-do: noi
@notes: Đọc tên module rồi im. Để câu hỏi của module làm việc.

## Câu hỏi của module
@phut: 1.5
@che-do: hoi
@notes: Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.

!luu-y Câu phải mang về | {{TAKE_HOME}}

Một vòng của tôi mất bao lâu theo đồng hồ treo tường, và hạn chờ tôi đặt đang lặng lẽ loại nhóm client nào ra khỏi mô hình?

## Vòng của anh dài bằng client chậm nhất
@phut: 1.5
@che-do: noi
@notes: Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.

Tám module đầu của trụ {{s001}} đều giả định vòng huấn luyện diễn ra sạch sẽ: không ai rơi, không ai chậm. Module này bỏ giả định đó, và hai hệ quả xuất hiện ngay.

## Vòng của anh dài bằng client chậm nhất (tiếp)
@phut: 1
@che-do: noi

Hệ quả thứ nhất là về thời gian: vòng đồng bộ dài bằng **max**, không bằng trung bình, nên một kẻ chậm quyết định cả vòng. Số vòng là đại lượng không có đơn vị thời gian, nên một bảng chỉ báo số vòng thì không kiểm được tuyên bố nào về chi phí.

## Vòng của anh dài bằng client chậm nhất (tiếp)
@phut: 1
@che-do: noi

Hệ quả thứ hai nặng hơn và gần như không ai khai: đặt hạn chờ `D` làm trọng số của client `k` trong mô hình đổi từ `p_k` thành `p_k·q_k` chuẩn hoá lại, với `q_k` là xác suất client đó về kịp. Hệ đang tối thiểu hoá một mục tiêu **khác** mục tiêu viết trong phần phương pháp, và chênh lệch đó đi vào mô hình chứ không đi vào bảng kết quả.

## Vòng của anh dài bằng client chậm nhất (tiếp)
@phut: 1
@che-do: noi

Vì thiết bị yếu và mạng chậm thường trùng với một nhóm dân cư cụ thể, đặt hạn chờ là một quyết định về **công bằng**, không chỉ về tốc độ.

## Vòng của anh dài bằng client chậm nhất (tiếp)
@phut: 1
@che-do: noi

Một con số mà module này **cố ý không dạy**: tỉ lệ client sẵn sàng trong môi trường cross-device. Đặc tả đánh dấu nó là chưa chắc và chỉ ra chỗ phải tra là mục hệ thống của Kairouz và cộng sự {{s002}}. Thà thiếu một thẻ còn hơn dạy một con số không có chỗ ở, nên nó không có mặt ở đây.

## Kẻ chậm, và vì sao vòng đồng bộ là max
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói **định nghĩa**, rồi lật.

*Tầng {{s003}} trên bốn.*

## Kẻ chậm, và vì sao vòng đồng bộ là max · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Thời gian một vòng đồng bộ là `T_vòng = max_{k∈S}(t_tính,k + t_truyền,k)`, lấy trên tập client được chọn `S`, vì server phải chờ đủ cập nhật rồi mới tổng hợp. Client làm chậm cả vòng gọi là **kẻ chậm** (straggler).

## Kẻ chậm, và vì sao vòng đồng bộ là max · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **max chứ không phải trung bình**, nên thời gian vòng tăng theo số client được chọn và gần như không giảm khi phần cứng trung bình tốt lên. Hệ quả cho bảng kết quả: tăng số client mỗi vòng để giảm phương sai là mua một thứ bằng tiền của một thứ khác, và cái giá đó phải có trong bài dưới dạng giây mỗi vòng đo được, không phải dưới dạng số vòng.

## Trọng số hiệu dụng khi có hạn chờ
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.

*Tầng {{s004}} trên bốn.*

## Trọng số hiệu dụng khi có hạn chờ · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Với hạn chờ `D`, client `k` vào tổng hợp với xác suất `q_k = P(t_k ≤ D)`. Server chuẩn hoá lại theo tập người về kịp, nên trọng số thật của client trong mô hình là `p̃_k = p_k·q_k / Σ_j p_j·q_j`.

## Trọng số hiệu dụng khi có hạn chờ · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: **tỉ lệ client bị bỏ và mức thiên lệch là hai con số khác nhau**, và cái thứ hai mới là cái đi vào mô hình. Ở cấu hình mặc định của mô phỏng trong module này, tỉ lệ bỏ là {{s005}} trong khi trọng số hiệu dụng của nhóm chậm là {{s006}} so với danh nghĩa: nhóm đó bị loại hoàn toàn. Báo tỉ lệ bỏ rồi coi như đã khai thiên lệch là khai thiếu đúng chỗ quan trọng.

## Hạn chờ là một quyết định về công bằng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật.

*Tầng {{s007}} trên bốn.*

## Hạn chờ là một quyết định về công bằng · đáp
@phut: 1.5
@che-do: noi
@notes: So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.

Vì `q_k` phụ thuộc thiết bị và đường truyền, nó **tương quan với dữ liệu** của client chứ không độc lập với nó. Khi đó tập client đóng góp không còn là một mẫu không chệch, nên mọi bound hội tụ dựa giả thiết lấy mẫu không chệch đều mất hiệu lực, và `Γ` hiệu dụng khác `Γ` thật.

## Hạn chờ là một quyết định về công bằng · đáp (tiếp)
@phut: 1
@che-do: noi

Điểm phải nhớ: lối ra không phải siết hạn chờ mà là **khai và sửa trọng số**. Hai cách đứng được: chia lại trọng số của người về kịp theo `p_k/q_k` với `q_k` ước lượng theo nhóm, hoặc chuyển sang bán bất đồng bộ, nơi cập nhật cũ `τ` vòng được hạ trọng số thường theo `1/(1+τ)` thay vì bị bỏ hẳn. Cách thứ hai đổi bài toán: không ai bị loại, nhưng xuất hiện độ cũ phải khai.

## Thời gian vòng
@phut: 1.5
@che-do: so
@notes: Giả thiết là phần đáng nhớ, không phải biểu thức.

`T_vòng = max_{k∈S}(t_tính,k + t_truyền,k) · q_k = P(t_k ≤ D) · p̃_k = p_k·q_k / Σ_j p_j·q_j · cập nhật cũ τ vòng nhân 1/(1+τ)`

**Giả thiết nó đứng trên:**

## Thời gian vòng (tiếp)
@phut: 1
@che-do: so

- Vòng là đồng bộ: server chờ tới khi mọi client trong S báo về hoặc tới hạn chờ D, rồi mới tổng hợp, nên thời gian vòng là max chứ không phải trung bình
- Server chuẩn hoá lại trọng số theo tập người về kịp, tức chia cho tổng trọng số của những client có mặt; đây là điều cài đặt thật làm và cũng là chỗ sinh ra thiên lệch

## Thời gian vòng (tiếp)
@phut: 1
@che-do: so

- q_k chỉ phụ thuộc thiết bị và đường truyền, không phụ thuộc nội dung cập nhật; đây chính là giả thiết bị tắt ở công tắc thứ nhất
- Số client mỗi vòng đủ lớn để mẫu số tập trung quanh kỳ vọng, nên xấp xỉ bậc một của tỉ số kỳ vọng dùng được
- Hệ số hạ trọng số 1/(1+τ) chọn trước chứ không học, nên nó là một giả thiết thiết kế phải khai, không phải một kết quả

## Thời gian vòng · ghi chú
@phut: 1
@che-do: noi

Hai con số dễ bị lẫn với nhau: **tỉ lệ client bị bỏ** là một đại lượng của hệ thống, còn **trọng số hiệu dụng** là một đại lượng của mô hình. Chúng không suy ra được từ nhau: bỏ {{s005}} client có thể ứng với thiên lệch bằng {{s008}} nếu việc bỏ là ngẫu nhiên đều, hoặc ứng với việc một nhóm bị loại hoàn toàn nếu `q_k` gần {{s008}} trên đúng nhóm đó.

## Thời gian vòng · ghi chú (tiếp)
@phut: 0.5
@che-do: noi

Con số phải vào bài là con số thứ hai, kèm cách ước lượng `q_k` theo nhóm.

## Số phải biết
@phut: 2
@che-do: so
@wow
@dan: Tắt một giả thiết rồi xem tuyên bố nào còn đứng.
@notes: Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.

!so {{s009}} | giây | Một vòng chọn {{s010}} client
!so {{s011}} |  | Nhóm chậm chiếm tỉ lệ danh nghĩa {{s012}} của dữ liệu và
!so {{s013}} | giây | Số client mỗi vòng tăng từ {{s014}} lên {{s015}}

## Tính ra con số
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Nhóm chậm có trọng số danh nghĩa {{s019}} và về kịp với xác suất {{s012}}; nhóm nhanh về kịp với xác suất {{s020}}. Trọng số hiệu dụng của nhóm chậm bằng bao nhiêu phần trăm trọng số danh nghĩa của nó?

pc = {{s016}}, qc = {{s017}}, qn = {{s018}}

## Tính ra con số · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`100⋆qc/((1-pc)⋆qn + pc⋆qc)`

## Tính ra con số · đáp (tiếp)
@phut: 1
@che-do: noi

Khoảng {{s021}} trọng số danh nghĩa. Nhóm chậm khai {{s022}} dữ liệu nhưng chỉ còn {{s023}} sức nặng trong tổng hợp, nên hệ đang tối thiểu hoá một tổng khác với tổng viết trong phần phương pháp. Con số phải vào bài là tỉ số này chứ không phải tỉ lệ client bị bỏ: ở cấu hình mặc định của mô phỏng, tỉ lệ bỏ là {{s005}} trong khi tỉ số này bằng {{s006}}, nên hai con số đo hai thứ khác nhau.

## Hạn chờ 90 giây là cái chặn thời gian vòng
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hạn chờ {{s024}} giây là cái chặn thời gian vòng, và server mất thêm {{s025}} giây tổng hợp mỗi vòng. Bao nhiêu vòng mỗi giờ?

han = {{s024}}, tth = {{s025}}

## Hạn chờ 90 giây là cái chặn thời gian vòng · đáp
@phut: 1.5
@che-do: noi
@notes: Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.

`3600/(han + tth)`

Khoảng {{s026}} vòng mỗi giờ, nên một thí nghiệm {{s027}} vòng cần khoảng {{s028}} giờ đồng hồ treo tường. Bảng cấu hình ghi {{s027}} vòng không nói gì về chi phí đó, vì số vòng là đại lượng không có đơn vị thời gian. Hai đại lượng phải khai cạnh nó là hạn chờ và thời gian tổng hợp của server, và cả hai đều là lựa chọn của người làm chứ không phải tính chất của thuật toán.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Thí nghiệm của anh báo {{s029}} vòng tới khi hội tụ. Reviewer hỏi chi phí thật. Con số nào trả lời được câu đó?

- Thời gian treo tường một vòng, bằng max của tính cộng truyền trên tập client được chọn, nhân với số vòng, kèm hạn chờ đã đặt
- Tổng số bước SGD trên toàn hệ
- Số tham số của mô hình và kích thước một cập nhật
- Thông lượng mạng trung bình của client

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Thời gian treo tường một vòng, bằng max của tính cộng truyền trên tập client được chọn, nhân với số vòng, kèm hạn chờ đã đặt**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Phải là giây mỗi vòng đo được nhân số vòng, kèm hạn chờ. Lý do: số vòng là đại lượng không có đơn vị thời gian, nên nó không chuyển thành chi phí nếu không biết một vòng dài bao lâu, và một vòng dài bằng client chậm nhất chứ không bằng client trung bình. Tổng số bước SGD lại càng xa, vì bước cục bộ chạy song song trên các client nên nó không cộng dồn theo thời gian.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Kích thước cập nhật và thông lượng trung bình là đầu vào để ước thời gian truyền, không phải phép đo chi phí, và trung bình thì sai thước đo ngay từ đầu vì cái chặn vòng là đuôi chậm.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Hạn chờ của anh cắt {{s030}} client mỗi vòng. Điều gì KHÔNG suy ra được từ con số {{s030}} đó?

- Rằng mỗi vòng tổng hợp ít cập nhật hơn so với khi không có hạn chờ
- Rằng thời gian một vòng bị chặn trên bởi hạn chờ cộng thời gian tổng hợp
- Mức thiên lệch mà việc cắt gây ra cho mô hình
- Rằng số vòng mỗi giờ cao hơn so với khi chờ mọi client

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Mức thiên lệch mà việc cắt gây ra cho mô hình**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Không suy ra được mức thiên lệch, vì thiên lệch phụ thuộc việc xác suất hoàn tất có tương quan với dữ liệu hay không, chứ không phụ thuộc tỉ lệ bị cắt. Cùng một tỉ lệ {{s030}} có thể ứng với thiên lệch bằng {{s008}} nếu việc cắt là ngẫu nhiên đều, hoặc ứng với việc một nhóm bị loại hoàn toàn nếu xác suất hoàn tất gần {{s008}} trên đúng nhóm đó.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Ba điều còn lại thì suy ra được ngay từ định nghĩa của hạn chờ: ít cập nhật hơn, vòng bị chặn trên, và số vòng mỗi giờ cao hơn. Đại lượng đo được thiên lệch là trọng số hiệu dụng theo nhóm, và nó đòi phải ước lượng xác suất hoàn tất theo nhóm.

## Chọn một phương án
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.

Cách sửa nào thật sự khôi phục được tính không chệch của tổng hợp khi có hạn chờ?

- Tăng số client lấy mẫu mỗi vòng, vì mẫu lớn hơn thì ít chệch hơn
- Chia lại trọng số của người về kịp theo p_k chia q_k, với q_k ước lượng và khai theo nhóm
- Tăng số vòng huấn luyện để bù phần dữ liệu bị mất
- Giảm số bước cục bộ để mỗi vòng ngắn hơn hạn chờ

## Chọn một phương án · đáp
@phut: 1.5
@che-do: noi
@notes: Vì sao ba phương án kia sai mới là phần đáng nhớ.

**Chia lại trọng số của người về kịp theo p_k chia q_k, với q_k ước lượng và khai theo nhóm**

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Cách đứng được là chia lại trọng số theo p_k chia q_k, tức lấy mẫu theo tầm quan trọng: nó bù đúng hệ số q_k mà hạn chờ đã nhân vào, nên kỳ vọng của cập nhật tổng hợp quay về gradient của mục tiêu danh nghĩa. Tăng số client không sửa được gì, vì chệch là một thiên lệch hệ thống chứ không phải phương sai: lấy mẫu nhiều hơn chỉ ước lượng chính xác hơn cái mục tiêu đã bị đổi.

## Chọn một phương án · đáp (tiếp)
@phut: 1
@che-do: noi

Tăng số vòng cũng vậy, nó hội tụ chắc hơn về điểm sai. Giảm số bước cục bộ thì làm mọi người về kịp nên có giúp, nhưng nó mua bằng việc đổi thuật toán và làm phình số hạng truyền, nên nó là đánh đổi khác chứ không phải phép hiệu chỉnh, và nó không khôi phục gì khi nguyên nhân chậm là đường truyền.

## Câu nào không được số nào chống đỡ · ca một
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn kết quả sau có một mệnh đề mà hai mệnh đề trước nó đã bác. Bấm vào mệnh đề đó.

- Phương pháp của chúng tôi đạt cùng mức mất mát sau {{s031}} vòng, còn baseline cần {{s032}} vòng,
- trong đó mỗi vòng của chúng tôi chạy {{s014}} bước cục bộ còn baseline chạy {{s001}} bước,
- nên phương pháp của chúng tôi nhanh gấp ba lần theo đồng hồ treo tường.

## Câu không được chống đỡ · ca một · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**nên phương pháp của chúng tôi nhanh gấp ba lần theo đồng hồ treo tường.**

Hai mệnh đề đầu là số đo, và chúng nói ngược với kết luận. Tỉ số {{s004}} là tỉ số SỐ VÒNG. Nó chỉ chuyển thành tỉ số thời gian khi một vòng của hai bên dài như nhau, mà mệnh đề thứ hai vừa khai rằng không: vòng của anh chứa {{s014}} bước cục bộ thay vì {{s001}}, nên phần tính của nó lớn hơn khoảng năm lần.

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

Nếu phần tính chi phối thì thời gian thật là {{s031}} nhân {{s033}} bằng {{s034}} đơn vị so với {{s032}}, tức CHẬM hơn {{s035}} lần chứ không nhanh gấp ba. Nếu hệ bị chặn bởi hạn chờ thì cả hai bên đều mất đúng hạn chờ mỗi vòng và tỉ số về lại {{s004}}. Khoảng thật nằm giữa hai cực đó và chỉ đo được chứ không suy được. Cách sửa:

## Câu không được chống đỡ · ca một · đáp (tiếp)
@phut: 1
@che-do: noi

báo giây mỗi vòng đo được cho cả hai phương pháp, kèm hạn chờ, rồi mới nhân với số vòng.

## Câu nào không được số nào chống đỡ · ca hai
@phut: 1
@che-do: hoi
@notes: HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.

Đoạn phương pháp sau làm phần bảo đảm lý thuyết mất hiệu lực. Bấm vào chỗ gây ra chuyện đó.

- Mỗi vòng chúng tôi lấy mẫu {{s010}} client đều và độc lập từ {{s036}} client,
- đặt hạn chờ {{s024}} giây và bỏ các cập nhật về muộn,
- và vì phép lấy mẫu là không chệch, bound hội tụ bản lấy mẫu một phần áp được cho hệ của chúng tôi.

## Câu không được chống đỡ · ca hai · đáp
@phut: 1.5
@che-do: noi
@notes: Đây đúng là việc reviewer làm với bài của mình.

**và vì phép lấy mẫu là không chệch, bound hội tụ bản lấy mẫu một phần áp được cho hệ của chúng tôi.**

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Hai mệnh đề đầu là mô tả hệ thống và đều hợp lệ, thậm chí đáng khen vì khai rõ hạn chờ. Chỗ đổ là mệnh đề cuối: phép lấy mẫu CỦA SERVER không chệch thật, nhưng tập client thật sự đóng góp là tập đã qua bộ lọc hạn chờ, nên trọng số thật là p_k nhân q_k chuẩn hoá lại chứ không còn p_k.

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

Nếu q_k tương quan với dữ liệu của client, kỳ vọng của cập nhật tổng hợp không còn là gradient của mục tiêu khai trong bài, nên bound đang trích nói về một mục tiêu khác, bất kể nó đúng với mục tiêu riêng của nó. Đây cùng họ với lỗi sai thẩm quyền ở module {{s037}}: câu văn mượn uy tín của một định lý mà tiền đề của định lý không áp. Cách sửa:

## Câu không được chống đỡ · ca hai · đáp (tiếp)
@phut: 1
@che-do: noi

khai q_k theo nhóm rồi chia lại trọng số theo p_k chia q_k, hoặc khai lại mục tiêu của bài thành mục tiêu có trọng số hiệu dụng và trích bound cho đúng mục tiêu đó.

## Dẫn lại từng bước
@phut: 2
@che-do: so
@notes: Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.

- Mục tiêu khai trong bài: tối thiểu hoá Σ_k p_k·F_k(w), với p_k tỉ lệ số mẫu n_k
- Thêm hạn chờ D: client k chỉ vào tổng hợp khi t_k ≤ D, tức với xác suất q_k = P(t_k ≤ D)
- Server chia cho tổng trọng số của người về kịp, nên cập nhật tổng hợp là Σ_k p_k·1{t_k ≤ D}·g_k chia Σ_j p_j·1{t_j ≤ D}

## Dẫn lại từng bước (tiếp)
@phut: 1
@che-do: so

- Lấy kỳ vọng với xấp xỉ bậc một của tỉ số: trọng số thật của client k là p̃_k = p_k·q_k / Σ_j p_j·q_j
- Vậy hệ đang tối thiểu hoá Σ_k p̃_k·F_k chứ không phải Σ_k p_k·F_k, và hai mục tiêu này khác nhau đúng khi q_k khác nhau giữa các client
- Do đó mọi bound hội tụ phát biểu cho Σ_k p_k·F_k với giả thiết lấy mẫu không chệch đều không áp được, và Γ hiệu dụng khác Γ thật

## Tắt từng giả thiết
@phut: 2
@che-do: so
@notes: Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.

Kết quả gốc: tỉ lệ bỏ {{s038}} · trọng số hiệu dụng của nhóm chậm {{s039}} · thời gian vòng {{s040}} giây · {{s041}} vòng mỗi giờ · {{s042}} client hoàn tất mỗi vòng, ở hạn chờ {{s024}} giây, σ = {{s043}}, tỉ lệ chậm {{s012}}, m = {{s010}}

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Client được lấy mẫu đều và độc lập với dữ liệu của họ** tắt đi: Khả năng hoàn tất tương quan với dữ liệu: thiết bị yếu và mạng chậm trùng với một nhóm dân cư cụ thể, nên nhóm đó vừa chậm hơn vừa có phân bố dữ liệu khác.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Vòng là đồng bộ, server chờ tới hạn chờ rồi mới tổng hợp** tắt đi: Hệ chuyển sang bán bất đồng bộ: server tổng hợp liên tục và hạ trọng số cập nhật cũ τ vòng theo 1/(1+τ).
- **Thời gian hoàn tất độc lập giữa các vòng** tắt đi: Client chậm thì chậm ở mọi vòng, vì nguyên nhân là phần cứng và đường truyền chứ không phải nhiễu.

## Tắt từng giả thiết (tiếp)
@phut: 1
@che-do: so

- **Thời gian hoàn tất không tương quan với số mẫu cục bộ** tắt đi: Client nhiều dữ liệu tính lâu hơn, nên p_k lớn đi cùng q_k nhỏ.

## Chỗ này phải tự kéo, không xem được
@phut: 1.5
@che-do: demo
@notes: Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.

Hai nhóm client. Nhóm nhanh có thời gian một vòng phân bố đều quanh {{s044}} giây với độ lệch chuẩn σ, nên nửa bề rộng là căn ba nhân σ; nhóm chậm cùng dạng nhưng chậm gấp năm lần. Kéo hạn chờ và đọc HAI con số cạnh nhau: tỉ lệ client bị bỏ, và trọng số hiệu dụng của nhóm chậm. Chúng không đi cùng nhau.

*Mở `https://hoc-5-tru-web.vercel.app/#/module/2.10` và kéo thanh. Slide đứng yên, mô phỏng thì không.*

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Table II reports the number of communication rounds but not wall clock time. In a synchronous protocol the round duration is the maximum over the sampled clients, so a lower round count does not imply a lower training cost, especially since your method performs more local steps per round than the baseline. Please report measured seconds per round for both methods and state the deadline you used.

## Đáp mẫu
@phut: 1.5
@che-do: noi

We agree that round counts alone do not establish cost, and we have added the measurement. Table II now reports measured seconds per round for both methods under an identical configuration: the same {{s024}} second deadline, {{s010}} clients per round, and the same device pool.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

Our method takes {{s045}} seconds per round against {{s046}} for the baseline, because it runs {{s014}} local steps instead of {{s001}}, so the wall clock ratio is {{s031}} times {{s045}} against {{s032}} times {{s046}}, that is {{s047}} hours against {{s048}} hours, a factor of {{s049}} rather than the factor of {{s004}} that the round count suggests.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also separated computation from communication in Table III, which shows that communication dominates at this model size, and this is why the extra local steps cost less than their nominal ratio. Finally we report the distribution of per round duration rather than only its mean, since the round is bounded by the slowest sampled client, and we note that whenever the deadline binds the measured duration equals the deadline by construction and therefore carries no information about the hardware.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng số vòng truyền là thước đo quy ước trong học liên bang vì truyền thông là cổ chai. Đúng về quy ước, không trả lời được chuyện vòng của hai bên dài khác nhau.
- Mức {{s001}}: thêm một con số giây mỗi vòng, nhưng là con số ước từ kích thước cập nhật và thông lượng trung bình, chứ không phải con số đo được, và không khai hạn chờ.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: báo giây mỗi vòng ĐO ĐƯỢC cho cả hai phương pháp ở cùng hạn chờ và cùng số client mỗi vòng, nhân ra tổng thời gian treo tường, và nói rõ thời gian vòng là max chứ không phải trung bình.

## Phản biện hỏi
@phut: 1.5
@che-do: hoi
@notes: Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.

Section IV sets a {{s024}} second deadline, discards late updates, and then invokes the partial participation convergence bound on the grounds that clients are sampled uniformly at random. If the probability of completing within the deadline correlates with client data, the aggregate is biased and the bound no longer applies. Please state the per group completion probabilities, the resulting effective weights, and whether the reported heterogeneity constant refers to the nominal or the effective objective.

## Đáp mẫu
@phut: 1.5
@che-do: noi

The reviewer is right, and the correction changes a claim rather than only a number. We measured completion probability by device group: {{s050}} for the two faster groups and {{s051}} for the slowest group, which holds {{s052}} percent of the data. The renormalised effective weight of that group is therefore {{s053}}, that is {{s054}} percent of its nominal weight, so the system was minimising a reweighted objective and not the one stated in Section III.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

The heterogeneity constant we reported was computed for the nominal objective and did not apply. Section IV-C now implements importance reweighting, dividing each surviving client weight by its group completion probability estimated online, and Table V reports results under that estimator, with the nominal objective restored and the heterogeneity constant recomputed for it.

## Đáp mẫu (tiếp)
@phut: 1
@che-do: noi

We also state the fairness consequence explicitly, since the slowest group is defined by device class rather than by anything we chose, and we report per group accuracy before and after the correction so that the cost of the deadline is visible rather than implicit.

## Thang chấm
@phut: 1
@che-do: noi

**Chấm theo:**

- Mức {{s003}}: trả lời rằng phép lấy mẫu client là đều và độc lập nên tổng hợp không chệch. Lặp lại đúng chỗ bị phản bác.
- Mức {{s001}}: thừa nhận rằng một số client bị bỏ và báo tỉ lệ bị bỏ mỗi vòng, rồi coi tỉ lệ đó là mức thiên lệch. Vẫn lẫn một đại lượng của hệ thống với một đại lượng của mô hình.

## Thang chấm (tiếp)
@phut: 0.5
@che-do: noi

- Mức {{s004}}: báo xác suất hoàn tất theo nhóm, tính trọng số hiệu dụng p_k nhân q_k chuẩn hoá lại, và khai rõ rằng bound đang trích phát biểu cho mục tiêu danh nghĩa nên nó không áp cho mục tiêu mà hệ thật sự tối thiểu hoá.

## !cam-on
@phut: 0.5
@che-do: lang
@notes: Nhắc lại một lần rồi dừng.

{{TAKE_HOME}}

## !one-more-thing
@phut: 0.5
@che-do: noi
@notes: Món tặng: deck để NÓI, site để NHỚ.

Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `https://hoc-5-tru-web.vercel.app/#/module/2.10` bấm thẻ.
