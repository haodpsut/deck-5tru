# Năm trụ, bộ slide

Bộ slide web sinh từ kho học **Năm trụ** (`hoc-5-tru-web`). Mở `index.html` ở gốc là
vào được tất cả: một trang, một ô lọc, năm mươi chín deck.

> Deck để **nói**, kho để **nhớ**.

Kho có 977 khối, trong đó **873 khối là khối phải LÀM**: lật thẻ, tính số, bắt câu không
có số chống đỡ, trả lời phản biện. Slide thì luôn hiện đáp án, nên bộ này **không thay
được kho**. Dùng nó khi cần ôn thành tiếng, cần bấm giờ, hoặc cần kể cho người khác.

## Có gì

| nhóm | số deck | để làm gì |
|---|---|---|
| bản đồ | 1 | năm trụ là gì, cho người ngoài |
| phòng hỏi đáp | 1 | 36 thẻ, mỗi thẻ mang đúng khung giờ trả lời của nó |
| deck trụ | 5 | cả một trụ trong một lượt |
| deck số | 5 | số và công thức, luyện dẫn lại trong ba mươi giây |
| deck module | 47 | từng module, đầy đủ |

## Dùng

Mở một deck rồi dùng bàn phím:

- mũi tên hoặc cách: sang slide
- **p**: cửa sổ người nói, có ghi chú, đồng hồ, và phút thật so với phút kế hoạch
- **e**: xuất PDF
- cuộn chuột: cùng tệp ấy đọc được như một trang dài

Mỗi deck là **một tệp `index.html` tự chứa**, không gọi tài nguyên ngoài, nên mất mạng
vẫn chạy.

## Dựng lại

Nội dung có **một chỗ ở duy nhất** là kho `hoc-5-tru-web/data/`. Đừng sửa tay vào deck.

```bash
python3 sinh.py                 # sinh lại toàn bộ deck từ kho
```

Rồi dựng và chấm bằng bộ kit `deck-web`:

```bash
python3 dung.py      <deck>     # ra index.html
python3 xuat_pdf.py  <deck>     # ra deck.pdf và ảnh từng slide
python3 qa.py        <deck>     # 26 cổng
```

Ảnh và PDF không đẩy lên kho vì sinh lại được, và chúng nặng 3,4 GB.

## Chuẩn

Theo bộ kit của nhà: [github.com/haodpsut/deck-web](https://github.com/haodpsut/deck-web).
Màu nhấn `#2C6E9B`, nền lấy từ `kit/nen.json`, mọi con số đi qua macro từ `so-lieu.json`,
hình vẽ tại chỗ bằng `hinhkit`. Cả 59 deck phải qua **26 cổng** mới tính là xong.
