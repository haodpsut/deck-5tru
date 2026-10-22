#!/usr/bin/env python3
"""Sinh deck từ kho học "Năm trụ" (working/hoc-5-tru-web/data/).

    python3 sinh.py [ma-module ...]      # không tham số thì sinh tất cả

Vì sao là BỘ SINH chứ không viết tay: kho có 47 module, 977 khối, ~139.600 từ và
13.257 con số đứng một mình. Viết tay thì số có chỗ ở thứ hai ngay lập tức, và
mỗi lần kho đổi là deck lệch. Deck ở đây là HIỆN VẬT DỰNG RA, sửa thì sửa kho.

⚠ Mọi con số trong thân slide phải qua macro (cổng G7). Bộ sinh tự bóc token số
ra `so-lieu.json`, nên "một chỗ ở" của số vẫn là JSON của kho.
"""
from __future__ import annotations

import html as _html
import json
import re
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
KHO = D.parents[1] / "hoc-5-tru-web" / "data"
SITE = "https://hoc-5-tru-web.vercel.app"

MF = json.loads((KHO / "manifest.json").read_text(encoding="utf-8"))
TRU = {t["id"]: t for t in MF["tru"]}

TRAN = 90          # trần từ mỗi slide của profile giang-day
TRAN_HOI = 70      # slide hỏi để thoáng hơn

# Sổ thuật ngữ nằm TRONG KHO, không nằm ở đây: site và deck phải tra cùng một chỗ,
# nếu không hai nơi sẽ lệch nhau mà không ai biết.
_TN = json.loads((KHO / "thuat-ngu.json").read_text(encoding="utf-8"))
# dài trước ngắn sau, để "liên kết giữa vệ tinh" thắng "liên kết dịch vụ"
THUAT_NGU = sorted(((m["vi"], m["en"]) for m in _TN["muc"]),
                   key=lambda x: -len(x[0]))


# ---------------------------------------------------------------- chữ

def _can_the(s: str, the: str) -> str:
    """Bỏ thẻ đóng không có thẻ mở, và đóng nốt thẻ mở còn treo."""
    ra, sau, mo = [], 0, 0
    for m in re.finditer(r"</?%s>" % the, s):
        dong = m.group(0).startswith("</")
        if dong and mo == 0:
            ra.append(s[sau:m.start()])
            sau = m.end()
            continue
        mo += -1 if dong else 1
    ra.append(s[sau:])
    out = "".join(ra)
    return out + ("</%s>" % the) * mo


def md(s) -> str:
    """HTML của kho sang markdown của kit. Giữ nhấn mạnh, bỏ thẻ còn lại."""
    if not s:
        return ""
    s = str(s)
    # ⚠ Đổi dấu sao của NỘI DUNG trước, rồi mới chèn dấu nhấn markdown của mình.
    # Kho dùng `w*` `E*` theo nghĩa "tối ưu" và `a * b` theo nghĩa nhân; cả hai đi
    # thẳng ra chữ hiện ra và cổng G24 bắt. Đổi sau khi chèn `**` thì không còn
    # phân biệt được dấu nào của kho với dấu nào của mình.
    s = re.sub(r"\s\*\s", " × ", s)
    s = s.replace("*", "⋆")
    # ⚠ Cân THẺ trước khi đổi sang dấu nhấn. Kho có một khối mang `</b>` thừa,
    # trình duyệt bỏ qua nên trên site không ai thấy, nhưng đổi sang markdown thì
    # nó thành một dấu `**` lẻ và hiện nguyên hình trên slide. Rác vào thì bộ sinh
    # phải chịu được, chứ không được đẻ ra hiện vật hỏng.
    s = _can_the(s, "b")
    s = _can_the(s, "strong")
    s = re.sub(r"</p>\s*<p>", "\n\n", s)
    s = re.sub(r"<br\s*/?>", " ", s)
    for a, b in (("b", "**"), ("strong", "**"), ("i", "*"), ("em", "*")):
        s = re.sub(r"</?%s>" % a, b, s)
    s = re.sub(r"</?code>", "`", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s)
    # ⚠ Cấm em-dash ở MỌI đầu ra (cổng G8). Kho có cả en-dash lẫn em-dash.
    s = s.replace("—", ", ").replace("–", ", ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def bt(s) -> str:
    """Biểu thức toán sang dạng in được.

    ⚠ Dấu nhân ASCII `*` trong `bieuThuc` đi thẳng ra chữ hiện ra và cổng G24 bắt,
    vì nó không phân biệt được dấu nhân với dấu nhấn markdown chưa xử lý. Cổng
    đúng: `*` lọt ra màn hình là lỗi. Sửa ở nguồn, đừng nới cổng.
    """
    return re.sub(r"\s*\*\s*", " × ", md(s))


def _noi_cap(ds: list, dau: str) -> list:
    """Nối lại cặp nhấn bị cắt qua nhiều mẩu, bằng cách ĐÓNG ở mẩu này và MỞ LẠI
    ở mẩu sau.

    ⚠ Hai bản trước đều vá TỪNG MẨU RIÊNG RẼ và cả hai đều sai, vì một mẩu không
    tự biết nó đang nằm trong hay ngoài một cặp. Bản đếm chẵn lẻ dán thêm dấu vào
    cuối, ra `****` hiện nguyên hình. Bản đoán theo vị trí dấu thì đoán sai khi
    mẩu có sẵn một cặp trọn vẹn cộng một dấu lẻ. Chỉ có đi tuần tự và NHỚ TRẠNG
    THÁI mở hay đóng mới đúng, và nó đúng cho mọi trường hợp chứ không phải phần
    lớn trường hợp.
    """
    ra, dang_mo = [], False
    for x in ds:
        if dang_mo:
            x = dau + x
        if x.count(dau) % 2:
            x, dang_mo = x + dau, True
        else:
            dang_mo = False
        ra.append(x)
    return ra


def tu(s: str) -> int:
    return len(re.sub(r"\{\{[^}]*\}\}", "x", s or "").split())


class So:
    """Sổ số liệu của một deck. Mọi token số đứng một mình đi qua đây."""

    def __init__(self):
        self.gt: dict[str, str] = {}
        self._nguoc: dict[str, str] = {}

    def macro(self, tok: str) -> str:
        if tok in self._nguoc:
            return "{{%s}}" % self._nguoc[tok]
        k = "s%03d" % (len(self.gt) + 1)
        self.gt[k] = tok
        self._nguoc[tok] = k
        return "{{%s}}" % k

    def qua(self, s: str) -> str:
        """Thay mọi token số đứng một mình bằng macro, giữ nguyên chữ quanh nó."""
        if not s:
            return s
        ra = []
        for tok in re.split(r"(\s+)", s):
            if not tok.strip():
                ra.append(tok)
                continue
            dau = ""
            cuoi = ""
            loi = tok
            while loi and loi[0] in "(（[*`\"'":
                dau += loi[0]
                loi = loi[1:]
            while loi and loi[-1] in ").,:;*`\"'）]":
                cuoi = loi[-1] + cuoi
                loi = loi[:-1]
            if loi and re.fullmatch(r"\d[\d.,/%×x+-]*", loi):
                loi = self.macro(loi)
            ra.append(dau + loi + cuoi)
        return "".join(ra)


def chia(s: str, tran: int) -> list[str]:
    """Cắt văn xuôi thành nhiều mẩu, mỗi mẩu dưới trần từ. Cắt ở ranh giới đoạn
    trước, hết đoạn mới cắt ở ranh giới câu."""
    doan = [p.strip() for p in s.split("\n\n") if p.strip()]
    nho = []
    for p in doan:
        if tu(p) <= tran:
            nho.append(p)
            continue
        # ⚠ Danh sách gạch đầu dòng là MỘT đoạn mà không có dấu chấm, nên cắt theo
        # câu không tìm được chỗ nào và trả về nguyên khối quá trần. Cắt theo DÒNG
        # trước, vì mỗi gạch đầu dòng tự nó đã là một đơn vị đọc.
        if "\n" in p:
            cau = [x for x in p.split("\n") if x.strip()]
        else:
            cau = re.split(r"(?<=[.?!:])\s+", p)
        cum, dem = [], 0
        for c in cau:
            n = tu(c)
            noi = "\n" if p.lstrip().startswith(("-", "*")) else " "
            if cum and dem + n > tran:
                nho.append(noi.join(cum))
                cum, dem = [c], n
            else:
                cum.append(c)
                dem += n
        if cum:
            nho.append(("\n" if p.lstrip().startswith(("-", "*")) else " ").join(cum))
    # ⚠ Gộp theo kiểu "nhét đầy rồi sang mẩu mới" để lại mẩu cuối chỉ một gạch đầu
    # dòng, nhìn như slide bị bỏ quên. Tính TRƯỚC số mẩu cần, rồi chia đều.
    tong = sum(tu(x) for x in nho)
    n_mau = max(1, -(-tong // max(1, tran)))
    muc = tong / n_mau if n_mau else tong
    ra, cum, dem = [], [], 0
    for p in nho:
        n = tu(p)
        day = "\n\n".join(cum)
        chan = day.count("**") % 2 == 0 and day.count("`") % 2 == 0
        # ⚠ Giữ cặp nhấn nguyên vẹn là ƯU TIÊN, không phải luật tuyệt đối: bám vào
        # nó tới cùng thì mẩu phình qua trần mật độ và cổng G6 bắt. Quá trần thì
        # cắt, rồi để can_bang() vá dấu lẻ.
        # ⚠ "Quá trần thì luôn cắt" phải thắng TUYỆT ĐỐI. Bản trước chỉ ép cắt khi
        # phần đã gom tự nó vượt trần, nên một mẩu 60 từ cộng một câu 34 từ nằm
        # trong cặp nhấn vẫn dính lại thành 94 từ. can_bang() đã vá được dấu lẻ
        # theo vị trí rồi, nên cắt giữa cặp nhấn không còn là lỗi.
        if cum and (dem + n > tran
                    or (chan and dem >= muc and len(ra) < n_mau - 1)):
            ra.append(day)
            cum, dem = [p], n
        else:
            cum.append(p)
            dem += n
    if cum:
        ra.append("\n\n".join(cum))
    return _noi_cap(_noi_cap(ra, "**"), "`") or [""]


def ngan(s: str, toi_da: int = 15) -> str:
    """Rút một câu xuống dưới `toi_da` từ, cắt ở mệnh đề chứ không cắt giữa chừng."""
    s = re.sub(r"\s+", " ", md(s)).strip().rstrip(".")
    if tu(s) <= toi_da:
        return s
    for d in (", ", ": ", ";"):
        if d in s:
            dau = s.split(d)[0]
            if 4 <= tu(dau) <= toi_da:
                return dau
    return " ".join(s.split()[:toi_da])


def tieu_de(s: str, du_phong: str, toi_da: int = 12) -> str:
    """Tiêu đề slide: chỉ cắt ở RANH GIỚI MỆNH ĐỀ, không bao giờ cắt giữa cụm từ.

    ⚠ Bản đầu cắt cứng ở từ thứ 11, ra "Đơn vị quan sát là câu đầu tiên của phần
    đánh", mất chữ "giá". Không cổng nào bắt được, chỉ mắt thấy. Cắt không sạch
    thì thà dùng tên dự phòng.
    """
    # ⚠ Trần theo KÝ TỰ nữa, không chỉ theo từ. Tiêu đề dài bị khung đầu slide cắt
    # nên không tới được lớp chữ của PDF, và cổng G11 bắt. Đo được: 52 ký tự thì qua.
    KY_TU = 52
    g = re.sub(r"\s+", " ", md(s)).strip().rstrip(".")
    if tu(g) <= toi_da and len(g) <= KY_TU:
        return g
    for dd in (", ", ": ", "; "):
        if dd in g:
            dau = g.split(dd)[0]
            if 3 <= tu(dau) <= toi_da and len(dau) <= KY_TU:
                return dau
    return du_phong


# ---------------------------------------------------------------- slide

class Deck:
    TRAN_PROFILE = {"giang-day": 90, "nghien-cuu": 60, "hoi-thao": 45}

    def chu_giai(self, s: str) -> str:
        """Kèm tiếng Anh vào LẦN ĐẦU một thuật ngữ xuất hiện trong deck này.

        ⚠ Lần đầu thôi. Kèm mọi lần thì slide loãng và mắt bỏ qua luôn cả chú giải.
        ⚠ Không chèn vào trong khối mã, và không chèn nếu chỗ ấy đã có sẵn tiếng
        Anh, vì kho đã tự chú giải 34 thẻ rồi.
        """
        if not s:
            return s
        # tách khối mã ra, chỉ xét phần văn xuôi
        phan = re.split(r"(`[^`]*`)", s)
        for i, x in enumerate(phan):
            if x.startswith("`"):
                continue
            for vi, en in THUAT_NGU:
                if vi in self.da_chu:
                    continue
                m = re.search(r"(?<![\w])(%s)(?![\w])" % re.escape(vi), x, re.I)
                if not m:
                    continue
                sau = x[m.end():m.end() + 60]
                if en.lower() in sau.lower():      # kho đã chú giải sẵn ở đây
                    self.da_chu.add(vi)
                    continue
                x = x[:m.end()] + " (%s)" % en + x[m.end():]
                self.da_chu.add(vi)
            phan[i] = x
        return "".join(phan)

    def __init__(self, thu_muc: Path, tieu_de, phu_de, profile, phan_mac=""):
        self.da_chu: set = set()
        self.tran = self.TRAN_PROFILE[profile] - 6
        self.d = thu_muc
        self.tieu_de = tieu_de
        self.phu_de = phu_de
        self.profile = profile
        self.phan_mac = phan_mac
        self.so = So()
        self.sl: list[dict] = []

    def them(self, tieu_de, che_do, phut, than, phan=None, hinh=None,
             notes="", wow=False, dan=""):
        """⚠ TỰ CHIA theo trần của profile ngay tại chỗ thêm.

        Bản trước để mỗi chỗ gọi tự nhớ gọi `chia()`, và ba chỗ quên: slide mô
        phỏng 138 từ, slide trắc nghiệm, slide bản đồ 50 từ trên trần 45. Luật mà
        người gọi phải nhớ thì không phải luật, nó là một lời nhắc.
        """
        than = self.chu_giai(than)
        mau = chia(than, self.tran) if than else [than]
        for i, x in enumerate(mau):
            t = tieu_de if i == 0 else tieu_de + " (tiếp)"
            # ⚠ Tiêu đề dài bị khung đầu slide CẮT nên không tới được lớp chữ của
            # PDF, cổng G11 bắt. Trần phải đặt trên tiêu đề ĐÃ CỘNG HẬU TỐ, vì
            # " · đáp (tiếp)" một mình đã chiếm mười ba ký tự.
            while len(t) > 56 and " " in t:
                bo = t.rsplit(" ", 2)[0] if t.endswith(")") else t.rsplit(" ", 1)[0]
                t = bo + (" (tiếp)" if t.endswith("(tiếp)") else "")
            self.sl.append(dict(
                tieu_de=t,
                che_do=che_do, phut=phut if i == 0 else max(0.5, phut / 2),
                than=x, phan=phan if phan is not None else self.phan_mac,
                hinh=hinh if i == 0 else None, notes=notes if i == 0 else "",
                wow=wow and i == 0, dan=dan if i == 0 else ""))

    # ---- cân nhịp -------------------------------------------------------
    def can(self, lo, hi, run_toi_da):
        """Đưa tổng phút vào dải của profile, rồi bẻ mọi đoạn cùng chế độ quá dài.

        ⚠ Hai ràng buộc này đá nhau: kéo dài slide để đủ phút tối thiểu thì đoạn
        cùng chế độ dài ra theo. Nên phải cân phút TRƯỚC, bẻ đoạn SAU, và bẻ bằng
        cách đổi chế độ chứ không bằng cách cắt phút.
        """
        tong = sum(s["phut"] for s in self.sl)
        he = 1.0
        if tong < lo:
            he = lo / tong
        elif tong > hi:
            he = hi / tong
        for s in self.sl:
            s["phut"] = max(0.5, round(s["phut"] * he * 2) / 2)
        # ⚠ Làm tròn lên nửa phút cộng sàn 0,5 làm tổng BẬT NGƯỢC lên trên trần:
        # nhân hệ số rồi tin là xong thì có deck ra 104 phút trong khi trần là 95.
        # Phải chỉnh lại từng nửa phút, bớt ở slide dài nhất, thêm ở slide ngắn nhất.
        while sum(x["phut"] for x in self.sl) > hi:
            c = max((x for x in self.sl if x["phut"] > 0.5), key=lambda x: x["phut"], default=None)
            if c is None:
                break
            c["phut"] -= 0.5
        while sum(x["phut"] for x in self.sl) < lo:
            c = min(self.sl, key=lambda x: x["phut"])
            c["phut"] += 0.5
        # bẻ đoạn cùng chế độ
        i = 0
        while i < len(self.sl):
            j, cong = i, 0.0
            while j < len(self.sl) and self.sl[j]["che_do"] == self.sl[i]["che_do"]:
                cong += self.sl[j]["phut"]
                j += 1
            if cong > run_toi_da and j - i >= 2:
                giua = (i + j) // 2
                cu = self.sl[giua]["che_do"]
                self.sl[giua]["che_do"] = "hoi" if cu != "hoi" else "noi"
                continue
            i = j
        return sum(s["phut"] for s in self.sl)

    def dat_wow(self, dich=0.30):
        """Đặt điểm wow theo VỊ TRÍ THỜI GIAN, không theo thứ tự khối trong kho.

        ⚠ Bản đầu gắn wow vào khối `cong_tac`, mà khối ấy nằm gần cuối module nên
        wow rơi vào phút 55 trên 72, tức 77% bài. Cửa sổ của profile là 15-50%.
        Thứ tự trong kho là thứ tự HỌC, không phải thứ tự NÓI.
        """
        tong = sum(s["phut"] for s in self.sl)
        dan = ""
        for s in self.sl:
            if s["wow"]:
                dan = dan or s["dan"]
            s["wow"] = False
            s["dan"] = ""
        dan = dan or "Chỗ này là chỗ tuyên bố đổi nghĩa, không phải chỗ thêm số."
        cong, tot, lech = 0.0, None, 1e9
        for i, s in enumerate(self.sl):
            giua = cong + s["phut"] / 2
            cong += s["phut"]
            if s["tieu_de"].startswith("!") or s["che_do"] in ("lang", "hoi"):
                continue
            if "(tiếp)" in s["tieu_de"]:
                continue
            e = abs(giua / tong - dich)
            if e < lech:
                lech, tot = e, i
        if tot is None:
            tot = len(self.sl) // 3
        self.sl[tot]["wow"] = True
        self.sl[tot]["dan"] = dan

    def ghi(self, nguoi_nghe, take_home, nguon, moc):
        self.d.mkdir(parents=True, exist_ok=True)
        tong = sum(s["phut"] for s in self.sl)
        ra = ["---",
              "tieu-de: %s" % self.tieu_de,
              "phu-de: %s" % self.phu_de,
              "tac-gia: Đỗ Phúc Hảo · CAIRA, Đại học Kiến trúc Đà Nẵng",
              "noi-ngay: Tự ôn, bộ Năm trụ",
              "profile: %s" % self.profile,
              "tong-phut: %g" % tong,
              'accent: "#2C6E9B"',
              "ngon-ngu: vi",
              "gate: khong",
              "nguon: %s" % nguon,
              "moc-ngay: %s" % moc,
              "---", ""]
        qua_dai = [s["tieu_de"] for s in self.sl if len(s["tieu_de"]) > 56]
        assert not qua_dai, "tiêu đề quá dài, sẽ bị cắt khỏi PDF: %r" % qua_dai[:2]
        phan_cu = None
        for s in self.sl:
            ra.append("## " + s["tieu_de"])
            if s["phan"] and s["phan"] != phan_cu:
                ra.append("@phan: " + s["phan"])
                phan_cu = s["phan"]
            if s["hinh"]:
                ra.append("@hinh: " + s["hinh"])
            ra.append("@phut: %g" % s["phut"])
            ra.append("@che-do: " + s["che_do"])
            if s["wow"]:
                ra.append("@wow")
                ra.append("@dan: " + s["dan"])
            if s["notes"]:
                ra.append("@notes: " + s["notes"])
            ra.append("")
            if s["than"]:
                ra.append(s["than"])
                ra.append("")
        (self.d / "noi-dung.md").write_text("\n".join(ra), encoding="utf-8")
        (self.d / "so-lieu.json").write_text(
            json.dumps({"_nguon": {"kho": "working/hoc-5-tru-web/data, bản %s" % MF["version"],
                                   "sinh_boi": "slides/5tru/sinh.py"},
                        "_thuat_ngu": {vi: en for vi, en in THUAT_NGU if vi in self.da_chu},
                        **self.so.gt}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        (self.d / "nguoi-nghe.md").write_text(nguoi_nghe, encoding="utf-8")
        # ⚠ Take-home cũng phải được chú giải. Nó vào slide qua macro {{TAKE_HOME}}
        # nên chu_giai() không bao giờ thấy nó, mà nó lại là câu hiện SỚM NHẤT và
        # lặp lại nhiều nhất trong deck.
        (self.d / "take-home.txt").write_text(self.chu_giai(take_home.strip()) + "\n",
                                              encoding="utf-8")
        return tong


# ---------------------------------------------------------------- deck module

def _ds(x):
    return x if isinstance(x, list) else ([x] if x else [])


def deck_module(ma: str) -> Path:
    meta = next(x for x in MF["module"] if x["ma"] == ma)
    d = json.loads((KHO / meta["file"]).read_text(encoding="utf-8"))
    t = TRU[d["tru"]]
    thu_muc = D / "module" / ma.replace(".", "-")
    van = [b for b in d["khoi"] if b.get("kind") == "van"]
    th = ngan(van[0]["heading"]) if van else ngan(d["ten"])

    dk = Deck(thu_muc, d["ten"], "Trụ %s %s · module %s" % (t["id"], t["tenNgan"], ma),
              "giang-day", phan_mac=t["tenNgan"].upper())
    q = dk.so.qua

    dk.them("!cover", "noi", 0.5, "", notes="Đọc tên module rồi im. Để câu hỏi của module làm việc.")
    dk.them("Câu hỏi của module", "hoi", 1.5,
            "!luu-y Câu phải mang về | {{TAKE_HOME}}\n\n" + q(md(d.get("cauHoiModule", ""))),
            notes="Hỏi rồi đếm ba giây. Đây là câu phải trả lời được khi hết module.")

    # văn xuôi mở đầu
    for b in van:
        dk.them(tieu_de(b.get("heading", d["ten"]), d["ten"]), "noi", 1.5,
                q(md(b.get("html", ""))),
                notes="Phần dẫn. Nói nhanh, chỗ đáng dừng nằm ở các thẻ phía sau.")

    def hoi_dap(tieu, hoi_than, dap_than, p_hoi=1.0, p_dap=1.5, ghi=""):
        # ⚠ Vế HỎI cũng phải chia. Bản đầu chỉ chia vế đáp, nên câu hỏi dài của
        # trắc nghiệm và của bắt lỗi vượt trần mật độ mà không ai cắt.
        # ⚠ Chia hai lần là hỏng: `them()` đã tự chia, nên gọi `chia()` ở đây nữa
        # thì mỗi mẩu vào `them()` như một slide RIÊNG, và hai slide liền nhau mang
        # CÙNG một tiêu đề, không cái nào có dấu "(tiếp)". Nhìn ra như in trùng.
        dk.them(tieu, "hoi", p_hoi, hoi_than,
                notes="HỎI TRƯỚC. Không lật slide cho tới khi đã thử trả lời thành tiếng.")
        dk.them(tieu + " · đáp", "noi", p_dap, dap_than, notes=ghi)

    # thẻ khái niệm
    for b in [x for x in d["khoi"] if x.get("kind") == "the_kn"]:
        # ⚠ Mặt trước đã là TIÊU ĐỀ slide. Lặp nó xuống thân là in một câu hai lần
        # trên cùng một màn hình; thân chỉ còn việc ra lệnh phải làm gì.
        # ⚠ Lời nhắc đổi theo TẦNG. Một câu dùng lại cho cả 151 thẻ của kho thì tới
        # thẻ thứ ba mắt đã bỏ qua nó, và lời nhắc thôi làm việc.
        NHAC = {1: "Nói **định nghĩa**, rồi lật.",
                2: "Nói định nghĩa và **điểm phải nhớ**, rồi lật.",
                3: "Nói định nghĩa, điểm phải nhớ, và **chỗ nó gãy**, rồi lật.",
                4: "Nói nó, rồi nói **chỗ mình từng dùng sai**, rồi lật."}
        hoi_dap(tieu_de(b["mat_truoc"], "Khái niệm tầng %s" % b.get("tang", 1)),
                NHAC.get(b.get("tang", 1), NHAC[2]) + "\n\n*Tầng {{%s}} trên bốn.*"
                % dk.so.macro(str(b.get("tang", 1)))[2:-2],
                q(md(b["mat_sau"])), 0.8, 1.5,
                ghi="So lời mình vừa nói với mặt sau. Khác chỗ nào thì chỗ đó là chỗ chưa nắm.")

    # công thức và giả thiết
    for b in [x for x in d["khoi"] if x.get("kind") == "cong_thuc"]:
        gt = "\n".join("- " + q(md(g)) for g in _ds(b.get("giaThiet")))
        than = "`%s`\n\n**Giả thiết nó đứng trên:**\n\n%s" % (q(bt(b["bieuThuc"])), gt)
        dk.them(tieu_de(b["ten"], "Công thức và giả thiết"), "so", 1.5, than,
                notes="Giả thiết là phần đáng nhớ, không phải biểu thức.")
        if b.get("ghiChu"):
            dk.them(tieu_de(b["ten"], "Công thức") + " · ghi chú", "noi", 1.0,
                    q(md(b["ghiChu"])))

    # số phải biết, gộp ba ô một slide
    spb = [x for x in d["khoi"] if x.get("kind") == "so_phai_biet"]
    for i in range(0, len(spb), 3):
        dong = []
        for b in spb[i:i + 3]:
            dong.append("!so %s | %s | %s" % (
                dk.so.macro(str(b["giaTri"])), q(md(b.get("donVi", "giá trị"))),
                q(ngan(b.get("stem", ""), 12))))
        dk.them("Số phải biết" + ("" if i == 0 else " (tiếp)"), "so", 2.0, "\n".join(dong),
                notes="Đọc to con số và ĐƠN VỊ. Nhớ số mà quên đơn vị là chưa nhớ.")

    # tính số
    for b in [x for x in d["khoi"] if x.get("kind") == "tinh_so"]:
        tham = ", ".join("%s = %s" % (k, dk.so.macro(str(v)))
                         for k, v in (b.get("thamSo") or {}).items())
        hoi_dap(tieu_de(b["stem"], "Tính ra con số"),
                q(md(b["stem"])) + ("\n\n" + tham if tham else ""),
                "`%s`\n\n%s" % (q(bt(b["bieuThuc"])), q(md(b.get("visao", "")))),
                0.8, 1.5, ghi="Dẫn lại bằng miệng trong ba mươi giây, đừng bấm máy tính.")

    # trắc nghiệm
    for b in [x for x in d["khoi"] if x.get("kind") == "single_choice"]:
        op = b.get("options") or []
        ds = "\n".join("- %s" % q(md(o)) for o in op)
        dung = op[b["answerIndex"]] if 0 <= b.get("answerIndex", -1) < len(op) else ""
        hoi_dap(tieu_de(b["stem"], "Chọn một phương án"), q(md(b["stem"])) + "\n\n" + ds,
                "**%s**\n\n%s" % (q(md(dung)), q(md(b.get("visao", "")))),
                1.0, 1.5, ghi="Vì sao ba phương án kia sai mới là phần đáng nhớ.")

    # bắt lỗi
    bl = [x for x in d["khoi"] if x.get("kind") == "bat_loi"]
    for n_bl, b in enumerate(bl):
        hau = "" if len(bl) < 2 else " · ca %s" % "một hai ba bốn năm".split()[n_bl]
        doan = b.get("doan") or []
        ds = "\n".join("- %s" % q(md(c.get("t", ""))) for c in doan)
        sai = [c for c in doan if c.get("loi")]
        dap = "\n\n".join("**%s**\n\n%s" % (q(md(c.get("t", ""))), q(md(c.get("viSao", ""))))
                          for c in sai)
        dk.them("Câu nào không được số nào chống đỡ" + hau, "hoi", 1.2,
                q(md(b["stem"])) + "\n\n" + ds,
                notes="HỎI TRƯỚC. Chỉ ra câu sai bằng miệng rồi mới lật.")
        dk.them("Câu không được chống đỡ" + hau + " · đáp", "noi", 1.5, dap,
                notes="Đây đúng là việc reviewer làm với bài của mình.")

    # dẫn công thức
    dct = [x for x in d["khoi"] if x.get("kind") == "dan_cong_thuc"]
    for n_dc, b in enumerate(dct):
        hau2 = "" if len(dct) < 2 else " · ca %s" % "một hai ba bốn năm".split()[n_dc]
        bu = b.get("buoc") or []
        # ⚠ Không đánh số "1." "2.": cổng G7 thấy đó là con số gõ thẳng. Thứ tự
        # đã nằm trong thứ tự dòng rồi, đánh số là nói hai lần.
        ds = "\n".join("- " + q(md(x.get("t", ""))) for x in bu)
        dk.them("Dẫn lại từng bước" + hau2, "so", 2.0, ds,
                notes="Bước nào có giả thiết riêng thì đó là chỗ gãy khi dùng lại.")

    # công tắc giả thiết: đây là slide WOW của module
    ct = [x for x in d["khoi"] if x.get("kind") == "cong_tac"]
    for k, b in enumerate(ct):
        ds = "\n".join("- **%s** tắt đi: %s" % (q(md(c.get("ten", ""))), q(md(c.get("khiTat", ""))))
                       for c in (b.get("congTac") or []))
        than = "Kết quả gốc: %s\n\n%s" % (q(md(b.get("dauRaGoc", ""))), ds)
        dk.them("Tắt từng giả thiết" + ("" if len(ct) < 2 else " · ca %s"
                % "một hai ba bốn năm".split()[k]), "so", 2.0, than, wow=(k == 0),
                dan="Tắt một giả thiết rồi xem tuyên bố nào còn đứng." if k == 0 else "",
                notes="Tuyên bố nào đổ khi tắt một công tắc thì tuyên bố ấy là của GIẢ THIẾT, không phải của phương pháp.")

    # khám tuyên bố
    for b in [x for x in d["khoi"] if x.get("kind") == "kham_claim"]:
        hoi_dap("Tuyên bố này đứng hay đổ", q(md(b["tuyenBo"])),
                "**%s**\n\n%s" % ("ĐỨNG" if b.get("dung") else "ĐỔ", q(md(b.get("bangChung", "")))),
                1.0, 1.5)

    # mô phỏng: trỏ về site, slide không chạy được widget
    for b in [x for x in d["khoi"] if x.get("kind") == "mo_phong"]:
        dk.them("Chỗ này phải tự kéo, không xem được", "demo", 1.5,
                q(md(b.get("stem", ""))) + "\n\n*Mở `%s/#/module/%s` và kéo thanh. Slide đứng yên, mô phỏng thì không.*"
                % (SITE, ma),
                notes="Dừng bài, mở site, kéo thật. Đây là khối slide KHÔNG thay được.")

    # phản biện
    for b in [x for x in d["khoi"] if x.get("kind") == "phan_bien"]:
        ru = "\n".join("- " + q(md(r)) for r in _ds(b.get("rubric"))[:3])
        dk.them("Phản biện hỏi", "hoi", 1.5, q(md(b["cauHoi"])),
                notes="Đọc to như reviewer đọc. Trả lời bằng miệng trước khi lật.")
        dk.them("Đáp mẫu", "noi", 1.5, q(md(b.get("dapAnMau", ""))))
        if ru:
            dk.them("Thang chấm", "noi", 1.0, "**Chấm theo:**\n\n" + ru)

    dk.them("!cam-on", "lang", 0.5, "{{TAKE_HOME}}",
            notes="Nhắc lại một lần rồi dừng.")
    dk.them("!one-more-thing", "noi", 0.5,
            "Tiến độ lặp giãn cách nằm ở site, không nằm ở deck này. Học xong thì về `%s/#/module/%s` bấm thẻ." % (SITE, ma),
            notes="Món tặng: deck để NÓI, site để NHỚ.")

    dk.can(40, 95, 10.0)
    dk.dat_wow()
    nn = ("# Nguoi nghe\n\n"
          "ho-la-ai: Chính tôi, đang ôn trụ %s để nói được nội dung này mà không mở ghi chú.\n"
          "sau-buoi-ho-lam-duoc: Trả lời câu hỏi của module thành tiếng, và dẫn lại được số của module.\n"
          "ho-da-biet-san: Nền toán và mạng ở mức nghiên cứu sinh. Không giảng lại định nghĩa cơ bản.\n"
          'cau-hoi-hiem-nhat: "Chỗ nào trong module này tôi đang tin mà chưa kiểm?"\n'
          % t["tenNgan"])
    dk.ghi(nn, th, "kho Năm trụ · %s" % SITE, "bản kho %s" % MF["version"])
    return thu_muc


if __name__ == "__main__":
    ds = sys.argv[1:] or [x["ma"] for x in MF["module"]]
    for ma in ds:
        p = deck_module(ma)
        print("  %-6s -> %s" % (ma, p.relative_to(D.parents[1])))
    print("đã sinh %d deck module" % len(ds))


# ---------------------------------------------------------------- thống kê kho

def _nap(ma):
    meta = next(x for x in MF["module"] if x["ma"] == ma)
    return json.loads((KHO / meta["file"]).read_text(encoding="utf-8"))


def _thong_ke():
    """Đếm khối theo trụ và theo module. Một chỗ ở duy nhất cho mọi con số đếm."""
    ra = {}
    for x in MF["module"]:
        d = _nap(x["ma"])
        ra[x["ma"]] = dict(tru=d["tru"], ten=d["ten"], khoi=len(d["khoi"]),
                           tang=max([b.get("tang", 1) for b in d["khoi"]] or [1]),
                           d=d)
    return ra


def _hinhkit():
    sys.path.insert(0, str(D.parents[1] / "_templates" / "deck-web" / "kit"))
    import hinhkit as hk
    return hk


# ---------------------------------------------------------------- deck trụ

def deck_tru(idt: int) -> Path:
    t = TRU[idt]
    tk = _thong_ke()
    ms = [x for x in MF["module"] if x["tru"] == idt]
    thu_muc = D / "tru" / str(idt)
    (thu_muc / "hinh").mkdir(parents=True, exist_ok=True)

    hk = _hinhkit()
    muc = [(tk[x["ma"]]["ten"], float(tk[x["ma"]]["khoi"])) for x in ms]
    phu = {tk[x["ma"]]["ten"]: "m " + x["ma"] for x in ms}
    lon = max(v for _, v in muc)
    r = hk.mo(1190, 520)
    r.append(hk.thanh_ngang(muc, 40, 70, 1110, 330, phu=phu,
                            nhan_nhan=tuple(n for n, v in muc if v == lon)))
    r.append(hk.ghi_chu_lon(40, 452, "Module dày nhất của trụ là module khó bỏ nhất",
                            "Trục: số khối có chấm điểm. Nguồn: kho Năm trụ bản %s." % MF["version"]))
    (thu_muc / "hinh" / "day-mong.svg").write_text(hk.dong(r), encoding="utf-8")

    dk = Deck(thu_muc, "Trụ %s · %s" % (idt, t["tenNgan"]),
              t.get("ten", t["tenNgan"]) + " · toàn trụ trong một lượt",
              "giang-day", phan_mac=t["tenNgan"].upper())
    q = dk.so.qua
    th = "Trụ %s đứng hay đổ là do giả thiết, không do thuật toán" % idt

    dk.them("!cover", "noi", 0.5, "", notes="Deck bao quát cả trụ. Chi tiết nằm ở deck từng module.")
    dk.them("Trụ này trả lời câu gì", "hoi", 2.0,
            "{{TAKE_HOME}}\n\n**%s** gồm {{%s}} module, {{%s}} khối có chấm điểm."
            % (t.get("ten", t["tenNgan"]),
               dk.so.macro(str(len(ms)))[2:-2],
               dk.so.macro(str(sum(tk[x['ma']]['khoi'] for x in ms)))[2:-2]),
            notes="Nói tên trụ, rồi im. Để người nghe tự hỏi mười module kia là gì.")
    dk.them("Module nào dày nhất", "hinh", 2.5, "", hinh="toan",
            notes="Chỉ vào thanh dài nhất. Dày không có nghĩa là quan trọng nhất, nhưng là chỗ tốn thời gian nhất.")
    dk.sl[-1]["than"] = "!hinh hinh/day-mong.svg | Số khối **có chấm điểm** của từng module. Thanh dài là chỗ phải để dành nhiều buổi hơn."

    for x in ms:
        d = tk[x["ma"]]["d"]
        van = [b for b in d["khoi"] if b.get("kind") == "van"]
        luan = md(van[0]["heading"]) if van else d["ten"]
        dk.them("m%s %s" % (x["ma"], tieu_de(d["ten"], d["ten"])), "hoi", 1.0,
                q(md(d.get("cauHoiModule", ""))),
                notes="Câu hỏi của module. Trả lời bằng miệng trước khi lật.")
        for i, mau in enumerate(chia(q(luan), TRAN - 6)):
            dk.them("m%s · luận điểm" % x["ma"] + ("" if i == 0 else " (tiếp)"), "noi", 1.0, mau)

    spb = [b for x in ms for b in tk[x["ma"]]["d"]["khoi"] if b.get("kind") == "so_phai_biet"]
    for i in range(0, min(len(spb), 9), 3):
        dong = ["!so %s | %s | %s" % (dk.so.macro(str(b["giaTri"])),
                                      q(md(b.get("donVi", "giá trị"))),
                                      q(ngan(b.get("stem", ""), 12)))
                for b in spb[i:i + 3]]
        dk.them("Số của trụ" + ("" if i == 0 else " (tiếp)"), "so", 2.0, "\n".join(dong),
                notes="Ba con số này phải bật ra không cần nghĩ.")

    dk.them("!cam-on", "lang", 0.5, "{{TAKE_HOME}}", notes="Nhắc lại rồi dừng.")
    dk.them("!one-more-thing", "noi", 0.5,
            "Deck này chỉ là bản đồ của trụ. Chỗ học thật là `%s/#/tru/%s`." % (SITE, idt),
            notes="Món tặng: deck để định vị, site để nhớ.")
    dk.can(40, 95, 10.0)
    dk.dat_wow()
    nn = ("# Nguoi nghe\n\n"
          "ho-la-ai: Chính tôi, đang ôn cả trụ %s trong một lượt trước khi vào từng module.\n"
          "sau-buoi-ho-lam-duoc: Gọi tên %s module của trụ và nói luận điểm cốt lõi của từng cái.\n"
          "ho-da-biet-san: Nền toán và mạng ở mức nghiên cứu sinh.\n"
          'cau-hoi-hiem-nhat: "Module nào của trụ này tôi vẫn chưa nói lại được mà không mở ghi chú?"\n'
          % (t["tenNgan"], len(ms)))
    dk.ghi(nn, th, "kho Năm trụ · %s" % SITE, "bản kho %s" % MF["version"])
    return thu_muc


# ---------------------------------------------------------------- deck bản đồ

def deck_ban_do() -> Path:
    tk = _thong_ke()
    thu_muc = D / "ban-do"
    (thu_muc / "hinh").mkdir(parents=True, exist_ok=True)
    hk = _hinhkit()

    muc = [(t["tenNgan"], float(sum(tk[x["ma"]]["khoi"] for x in MF["module"] if x["tru"] == t["id"])))
           for t in MF["tru"]]
    phu = {t["tenNgan"]: "%d module" % len([x for x in MF["module"] if x["tru"] == t["id"]])
           for t in MF["tru"]}
    lon = max(v for _, v in muc)
    r = hk.mo(1190, 500)
    r.append(hk.thanh_ngang(muc, 40, 80, 1110, 260, phu=phu,
                            nhan_nhan=tuple(n for n, v in muc if v == lon)))
    r.append(hk.ghi_chu_lon(40, 430, "Năm trụ không đều nhau, và không cần đều",
                            "Trục: số khối có chấm điểm. Nguồn: kho Năm trụ bản %s." % MF["version"]))
    (thu_muc / "hinh" / "nam-tru.svg").write_text(hk.dong(r), encoding="utf-8")

    bang = {"cot": ["trụ", "tên đầy đủ", "module", "khối"],
            "hang": [[t["tenNgan"], t.get("ten", t["tenNgan"]),
                      str(len([x for x in MF["module"] if x["tru"] == t["id"]])),
                      str(sum(tk[x["ma"]]["khoi"] for x in MF["module"] if x["tru"] == t["id"]))]
                     for t in MF["tru"]],
            "chu_thich": "Kho Năm trụ, bản %s. Khối là đơn vị có chấm điểm, không phải trang." % MF["version"],
            "nhan_hang": 0}

    dk = Deck(thu_muc, "Năm trụ, *một bản đồ*", "Tôi đang học gì, và vì sao đúng năm trụ ấy",
              "hoi-thao", phan_mac="BẢN ĐỒ")
    q = dk.so.qua
    dk.them("!cover", "noi", 0.5, "", notes="Deck này để NGƯỜI KHÁC hiểu tôi đang học gì.")
    dk.them("Năm trụ, và vì sao đúng năm", "noi", 2.0,
            "{{TAKE_HOME}}\n\nNăm trụ phủ đúng trục nghiên cứu của tôi: an ninh cho mạng phi mặt đất, trụ hai là mật mã hậu lượng tử.",
            notes="Nói trục trước, kho sau. Kho tồn tại vì trục, không ngược lại.")
    dk.them("Kho lớn tới đâu", "so", 2.5,
            "!so {{%s}} | module đã soạn xong | trên {{%s}} trụ\n"
            "!so {{%s}} | khối có chấm điểm | không phải số trang\n"
            "!so {{%s}} | thẻ hỏi đáp hội thảo | trả lời NÓI, không phải viết"
            % (dk.so.macro(str(len(MF["module"])))[2:-2],
               dk.so.macro(str(len(MF["tru"])))[2:-2],
               dk.so.macro(str(sum(v["khoi"] for v in tk.values())))[2:-2],
               dk.so.macro(str(MF["nhanh"][0]["soThe"]))[2:-2]),
            notes="Ba con số này là lý do deck không thay được site.")
    dk.them("Năm trụ, dày mỏng khác nhau", "hinh", 2.5,
            "!hinh hinh/nam-tru.svg | Trụ dày không phải trụ quan trọng hơn. Nó là trụ **có nhiều chỗ sai được hơn**.",
            hinh="toan", notes="Chỉ vào thanh dài nhất rồi hỏi phòng: vì sao trụ ấy dày.")
    dk.them("Năm trụ, bảng đầy đủ", "so", 2.5, "!bang bang_tru",
            notes="Bảng này sinh thẳng từ kho, không gõ tay.")
    for t in MF["tru"]:
        ms = [x for x in MF["module"] if x["tru"] == t["id"]]
        ds = "\n".join("- m%s %s" % (x["ma"], q(md(tk[x["ma"]]["ten"]))) for x in ms)
        for i, mau in enumerate(chia(ds, 40)):
            dk.them("Trụ %s %s" % (t["id"], t["tenNgan"]) + ("" if i == 0 else " (tiếp)"),
                    "noi", 1.5, mau,
                    notes="Đọc lướt. Ai hỏi sâu thì mở deck riêng của trụ.")
    dk.them("Vì sao học kiểu thẻ, không học kiểu slide", "noi", 2.0,
            "Kho có {{%s}} khối, phần lớn là khối **phải LÀM**.\n\n"
            "Slide luôn hiện đáp án nên không thay được chỗ ấy. Deck để **nói**, site để **nhớ**."
            % dk.so.macro(str(sum(v["khoi"] for v in tk.values())))[2:-2],
            notes="Đây là câu trả lời cho người hỏi vì sao không làm hết thành slide.")
    dk.them("!cam-on", "lang", 0.5, "{{TAKE_HOME}}", notes="Nhắc lại rồi dừng.")
    dk.them("!one-more-thing", "noi", 0.5,
            "Kho mở, không cần khoá: `%s`. Ai muốn học cùng thì tự mở." % SITE,
            notes="Món tặng: địa chỉ kho.")
    dk.can(5, 45, 3.5)
    dk.dat_wow()
    import json as _j
    nn = ("# Nguoi nghe\n\n"
          "ho-la-ai: Đồng nghiệp hoặc học viên muốn biết tôi đang học gì và có gì học cùng được.\n"
          "sau-buoi-ho-lam-duoc: Gọi tên năm trụ và biết mở kho ở đâu để tự học.\n"
          "ho-da-biet-san: Nền mạng và học máy cơ bản. Không cần biết trước năm trụ là gì.\n"
          'cau-hoi-hiem-nhat: "Vì sao không làm hết kho thành slide cho tiện?"\n')
    tong = dk.ghi(nn, "Năm trụ là bản đồ, site là chỗ nhớ, deck là chỗ nói",
                  "kho Năm trụ · %s" % SITE, "bản kho %s" % MF["version"])
    p = thu_muc / "so-lieu.json"
    o = _j.loads(p.read_text(encoding="utf-8"))
    o["bang_tru"] = bang
    p.write_text(_j.dumps(o, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return thu_muc


# ---------------------------------------------------------------- deck hỏi đáp

def deck_hoi_dap() -> Path:
    h = json.loads((KHO / "hoi-dap.json").read_text(encoding="utf-8"))
    thu_muc = D / "hoi-dap"
    dk = Deck(thu_muc, "Phòng hỏi đáp *hội thảo*",
              "Trả lời NÓI, trong hai mươi tới sáu mươi giây, không có gì để trốn",
              "giang-day", phan_mac="HỎI ĐÁP")
    q = dk.so.qua
    dk.them("!cover", "noi", 0.5, "", notes="Mở cửa sổ người nói, bấm p. Đồng hồ là phần chính của deck này.")
    dk.them("Luật của phòng này", "noi", 2.0,
            "{{TAKE_HOME}}\n\n" + q(md(h.get("ghiChu", ""))),
            notes="Đọc luật rồi bắt đầu. Không tua lại thẻ đã làm hỏng.")
    for i, c in enumerate(h["the"]):
        t = TRU.get(c.get("tru"), {}).get("tenNgan", "chung")
        giay = int(c.get("thoiGianGiay", 45))
        p = max(0.5, round(giay / 60 * 2) / 2)
        dk.them("Người hỏi: %s" % q(md(c.get("kieuNguoiHoi", "ẩn danh"))), "hoi", p,
                q(md(c["cauHoi"])) + "\n\n*Trụ %s. Khung trả lời {{%s}} giây.*"
                % (t, dk.so.macro(str(giay))[2:-2]),
                phan=t.upper(),
                notes="BẤM ĐỒNG HỒ. Trả lời thành tiếng hết khung giờ rồi mới lật.")
        if c.get("bayTrongCauHoi"):
            for k, mau in enumerate(chia(q(md(c["bayTrongCauHoi"])), TRAN - 6)):
                dk.them("Bẫy nằm ở đâu" + ("" if k == 0 else " (tiếp)"), "noi", 1.0, mau,
                        phan=t.upper())
        kt = "\n".join("- " + q(md(x)) for x in _ds(c.get("khungTraLoi")))
        if kt:
            for k, mau in enumerate(chia(kt, TRAN - 6)):
                dk.them("Khung trả lời" + ("" if k == 0 else " (tiếp)"), "so", 1.0, mau,
                        phan=t.upper())
        if c.get("dungNoi"):
            ds = "\n".join("- " + q(md(x)) for x in _ds(c["dungNoi"]))
            for k, mau in enumerate(chia("**Đừng nói:**\n\n" + ds, TRAN - 6)):
                dk.them("Đừng nói" + ("" if k == 0 else " (tiếp)"), "noi", 1.0, mau,
                        phan=t.upper())
    dk.them("!cam-on", "lang", 0.5, "{{TAKE_HOME}}", notes="Nhắc lại rồi dừng.")
    dk.them("!one-more-thing", "noi", 0.5,
            "Thẻ nào trả lời quá khung giờ thì ghi lại, đó mới là thẻ phải ôn, không phải thẻ trả lời sai.",
            notes="Món tặng: tiêu chí ôn là THỜI GIAN, không phải đúng sai.")
    dk.can(40, 95, 10.0)
    dk.dat_wow()
    nn = ("# Nguoi nghe\n\n"
          "ho-la-ai: Chính tôi, đang tập trả lời nói trước khi lên hội thảo.\n"
          "sau-buoi-ho-lam-duoc: Trả lời trọn mỗi câu trong khung giờ của nó, không lan man.\n"
          "ho-da-biet-san: Nội dung năm trụ. Đây là tập NÓI, không phải học lại nội dung.\n"
          'cau-hoi-hiem-nhat: "Câu nào tôi trả lời đúng nhưng quá giờ?"\n')
    dk.ghi(nn, "Trả lời nói trong khung giờ, không phải trả lời đúng mà dài",
           "kho Năm trụ · %s" % SITE, "bản kho %s" % MF["version"])
    return thu_muc


# ---------------------------------------------------------------- deck số

def deck_so(idt: int) -> Path:
    t = TRU[idt]
    tk = _thong_ke()
    ms = [x for x in MF["module"] if x["tru"] == idt]
    thu_muc = D / "so" / str(idt)
    dk = Deck(thu_muc, "Số phải dẫn lại được trong *ba mươi giây*",
              "Trụ %s %s · số, công thức, và giả thiết của chúng" % (idt, t["tenNgan"]),
              "giang-day", phan_mac=t["tenNgan"].upper())
    q = dk.so.qua
    dk.them("!cover", "noi", 0.5, "", notes="Deck này để đọc to, có đồng hồ. Không để đọc thầm.")
    dk.them("Luật của deck này", "noi", 1.5,
            "{{TAKE_HOME}}\n\nMỗi slide hỏi một con số hoặc một công thức. Dẫn lại **bằng miệng trong ba mươi giây**, rồi mới lật. Bấm máy tính là tính sai mục đích.",
            notes="Nói luật rồi bắt đầu. Đây là deck duy nhất của bộ mà đọc thầm là vô nghĩa.")
    for x in ms:
        d = tk[x["ma"]]["d"]
        for b in d["khoi"]:
            k = b.get("kind")
            if k == "so_phai_biet":
                dk.them("Con số này bằng bao nhiêu", "hoi", 0.5,
                        q(md(b.get("stem", ""))) + "\n\n*Module {{%s}}.*"
                        % dk.so.macro(x["ma"])[2:-2],
                        notes="Nói số VÀ đơn vị. Thiếu đơn vị là chưa nhớ.")
                dk.them("Đáp", "so", 1.0,
                        "!so %s | %s | module %s"
                        % (dk.so.macro(str(b["giaTri"])), q(md(b.get("donVi", "giá trị"))),
                           dk.so.macro(x["ma"])))
            elif k == "tinh_so":
                tham = ", ".join("%s = %s" % (kk, dk.so.macro(str(vv)))
                                 for kk, vv in (b.get("thamSo") or {}).items())
                dk.them("Tính ra con số", "hoi", 0.5,
                        q(md(b["stem"])) + ("\n\n" + tham if tham else ""),
                        notes="Dẫn bằng miệng, đừng bấm máy.")
                for i, mau in enumerate(chia("`%s`\n\n%s" % (q(bt(b["bieuThuc"])),
                                                            q(md(b.get("visao", "")))), TRAN - 6)):
                    dk.them("Đáp" + ("" if i == 0 else " (tiếp)"), "so", 1.0, mau)
            elif k == "cong_thuc":
                gt = "\n".join("- " + q(md(g)) for g in _ds(b.get("giaThiet")))
                dk.them("Công thức này đứng trên giả thiết nào", "hoi", 0.5,
                        "`%s`" % q(bt(b["bieuThuc"])),
                        notes="Kể đủ giả thiết trước khi lật. Thiếu một cái là chỗ gãy khi dùng lại.")
                for i, mau in enumerate(chia(gt, TRAN - 6)):
                    dk.them("Giả thiết" + ("" if i == 0 else " (tiếp)"), "so", 1.0, mau)
    dk.them("!cam-on", "lang", 0.5, "{{TAKE_HOME}}", notes="Nhắc lại rồi dừng.")
    dk.them("!one-more-thing", "noi", 0.5,
            "Số nào dẫn lại quá ba mươi giây thì nó chưa thuộc, dù đáp đúng.",
            notes="Món tặng: tiêu chí là thời gian dẫn, không phải đáp đúng.")
    dk.can(40, 95, 10.0)
    dk.dat_wow()
    nn = ("# Nguoi nghe\n\n"
          "ho-la-ai: Chính tôi, đang luyện dẫn lại số và công thức của trụ %s bằng miệng.\n"
          "sau-buoi-ho-lam-duoc: Dẫn lại mọi con số của trụ trong ba mươi giây, kèm đơn vị.\n"
          "ho-da-biet-san: Nội dung trụ. Đây là luyện TỐC ĐỘ dẫn lại, không phải học mới.\n"
          'cau-hoi-hiem-nhat: "Số nào tôi nhớ giá trị nhưng quên đơn vị?"\n' % t["tenNgan"])
    dk.ghi(nn, "Dẫn lại được trong ba mươi giây mới tính là thuộc",
           "kho Năm trụ · %s" % SITE, "bản kho %s" % MF["version"])
    return thu_muc


# ---------------------------------------------------------------- trang chủ

def _doc_deck(p: Path):
    """Đọc lại chính deck đã dựng: tiêu đề, phụ đề, số phút, số slide.

    ⚠ Đọc từ HIỆN VẬT, không từ biến trong bộ nhớ lúc sinh. Trang chủ phải nói
    đúng cái đang nằm trên đĩa, kể cả khi ai đó sửa tay một deck.
    """
    f = p / "noi-dung.md"
    if not f.exists():
        return None
    t = f.read_text(encoding="utf-8")
    g = lambda k: (re.search(r"^%s:\s*(.+)$" % k, t, re.M) or [None, ""])[1].strip()
    return dict(duong=str(p.relative_to(D)), tieu_de=re.sub(r"\*", "", g("tieu-de")),
                phu_de=g("phu-de"), phut=g("tong-phut"),
                slide=len(re.findall(r"^## ", t, re.M)),
                co=(p / "index.html").exists())


def trang_chu() -> Path:
    muc = []
    for p in [D / "ban-do", D / "hoi-dap"]:
        d = _doc_deck(p)
        if d:
            muc.append(("Bắt đầu ở đây", d))
    for t in MF["tru"]:
        nhom = "Trụ %s · %s" % (t["id"], t.get("ten", t["tenNgan"]))
        for p in [D / "tru" / str(t["id"]), D / "so" / str(t["id"])]:
            d = _doc_deck(p)
            if d:
                muc.append((nhom, d))
        for x in [m for m in MF["module"] if m["tru"] == t["id"]]:
            d = _doc_deck(D / "module" / x["ma"].replace(".", "-"))
            if d:
                d["ma"] = x["ma"]
                muc.append((nhom, d))

    nhoms = []
    for ten, d in muc:
        if not nhoms or nhoms[-1][0] != ten:
            nhoms.append((ten, []))
        nhoms[-1][1].append(d)

    tong_slide = sum(d["slide"] for _, d in muc)
    tong_phut = sum(float(d["phut"] or 0) for _, d in muc)
    than = []
    for ten, ds in nhoms:
        than.append('<section><h2>%s</h2><div class="luoi">' % _html.escape(ten))
        for d in ds:
            ma = ('<span class="ma">%s</span>' % _html.escape(d["ma"])) if d.get("ma") else ""
            than.append(
                '<a class="the%s" href="%s/index.html"><div class="tren">%s<b>%s</b></div>'
                '<p>%s</p><div class="chan"><span>%s slide</span><span>%s phút</span></div></a>'
                % ("" if d["co"] else " chua", _html.escape(d["duong"]), ma,
                   _html.escape(d["tieu_de"]), _html.escape(d["phu_de"]),
                   d["slide"], d["phut"]))
        than.append("</div></section>")

    doc = """<!doctype html><html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Năm trụ · bộ slide</title><style>
:root{--accent:#2C6E9B;--giay:#f7f8fa;--ink:#17202a;--ink-mo:#5b6775;--vien:#e3e7ec}
*{box-sizing:border-box}
body{margin:0;background:var(--giay);color:var(--ink);
 font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
 line-height:1.55}
header{padding:3rem 1.5rem 2rem;max-width:1180px;margin:0 auto}
.gach{width:56px;height:4px;background:var(--accent);border-radius:2px;margin-bottom:1.1rem}
h1{font-size:clamp(1.8rem, 1.2rem + 2vw, 2.8rem);margin:0 0 .5rem;letter-spacing:-.02em}
.phu{color:var(--ink-mo);margin:0 0 1.4rem;max-width:62ch}
.so{display:flex;gap:2.2rem;flex-wrap:wrap;margin:0 0 .4rem}
.so div b{display:block;font-size:1.7rem;color:var(--accent);font-variant-numeric:tabular-nums}
.so div span{font-size:.82rem;color:var(--ink-mo)}
main{max-width:1180px;margin:0 auto;padding:0 1.5rem 4rem}
#tim{width:100%;max-width:420px;padding:.7rem .9rem;border:1px solid var(--vien);
 border-radius:10px;font:inherit;background:#fff;margin:1.2rem 0 2rem}
h2{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-mo);
 margin:2.4rem 0 .9rem;font-weight:650}
.luoi{display:grid;gap:.85rem;grid-template-columns:repeat(auto-fill,minmax(270px,1fr))}
/* thẻ cao bằng nhau trong một hàng thì dòng chân phải NEO ĐÁY, nếu không
   mỗi thẻ một chỗ và hàng nhìn như so le */
.the{display:flex;flex-direction:column;background:#fff;border:1px solid var(--vien);
 border-radius:12px;padding:.95rem 1.05rem;text-decoration:none;color:inherit;transition:.15s}
.the:hover{border-color:var(--accent);transform:translateY(-2px);
 box-shadow:0 6px 18px rgba(23,32,42,.07)}
.tren{display:flex;align-items:baseline;gap:.5rem;margin-bottom:.3rem}
.ma{font-size:.72rem;color:var(--accent);font-weight:700;font-variant-numeric:tabular-nums}
.the b{font-size:1.02rem;letter-spacing:-.01em}
.the p{margin:0 0 .7rem;font-size:.84rem;color:var(--ink-mo)}
.chan{display:flex;gap:.9rem;font-size:.74rem;color:var(--ink-mo);margin-top:auto;
 border-top:1px solid var(--vien);padding-top:.5rem;font-variant-numeric:tabular-nums}
.the.chua{opacity:.45;pointer-events:none}
footer{max-width:1180px;margin:0 auto;padding:0 1.5rem 3rem;color:var(--ink-mo);font-size:.84rem}
footer a{color:var(--accent)}
@media (prefers-color-scheme:dark){
 :root{--giay:#11161c;--ink:#e8edf3;--ink-mo:#96a2b1;--vien:#222a33}
 .the{background:#161c23}}
</style></head><body>
<header><div class="gach"></div>
<h1>Năm trụ, bộ slide</h1>
<p class="phu">Deck để <b>nói</b>, kho để <b>nhớ</b>. Phần lớn kho là khối phải LÀM, mà slide thì luôn hiện đáp án, nên deck ở đây không thay được kho. Dùng deck khi cần ôn thành tiếng, cần bấm giờ, hoặc cần kể cho người khác.</p>
<div class="so">
<div><b>__DECK__</b><span>deck</span></div>
<div><b>__SLIDE__</b><span>slide</span></div>
<div><b>__GIO__</b><span>giờ nói</span></div>
<div><b>__MODULE__</b><span>module của kho</span></div>
</div></header>
<main><input id="tim" type="search" placeholder="Lọc theo tên hoặc mã module, ví dụ 1.4 hoặc doppler" autocomplete="off">
__THAN__
</main>
<footer>Sinh từ kho <a href="__SITE__">hoc-5-tru-web</a>, bản __VER__, bằng <code>slides/5tru/sinh.py</code>.
Sửa thì sửa kho rồi dựng lại, đừng sửa tay vào deck. Mỗi deck mở bằng bàn phím, bấm <b>p</b> ra cửa sổ người nói có đồng hồ, bấm <b>e</b> để xuất PDF.</footer>
<script>
const o=document.getElementById('tim');
o.addEventListener('input',()=>{
 const q=o.value.trim().toLowerCase();
 document.querySelectorAll('section').forEach(s=>{
  let con=0;
  s.querySelectorAll('.the').forEach(a=>{
   const hop=!q||a.textContent.toLowerCase().includes(q);
   a.style.display=hop?'':'none'; if(hop)con++;
  });
  s.style.display=con?'':'none';
 });
});
</script></body></html>"""
    doc = (doc.replace("__THAN__", "\n".join(than))
              .replace("__DECK__", str(len(muc)))
              .replace("__SLIDE__", format(tong_slide, ","))
              .replace("__GIO__", "%.0f" % (tong_phut / 60))
              .replace("__MODULE__", str(len(MF["module"])))
              .replace("__SITE__", SITE).replace("__VER__", MF["version"]))
    p = D / "index.html"
    p.write_text(doc, encoding="utf-8")
    return p
