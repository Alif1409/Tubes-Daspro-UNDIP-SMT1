# ============================================================
# MAIN.PY - FILE TEST CASE UNTUK TUBES DASPRO
# ============================================================
# File ini berisi test case untuk menguji semua fungsi
# yang ada di tubes-daspro.py dengan Normal Case dan Edge Case
# ============================================================

# Import semua fungsi dari tubes-daspro
from importlib import import_module
tubes = import_module("tubes-daspro")

# Import fungsi-fungsi yang diperlukan
MakeMhs = tubes.MakeMhs
MakeMatkul = tubes.MakeMatkul
MakeTranskrip = tubes.MakeTranskrip
MakeSetTranskrip = tubes.MakeSetTranskrip
GetNIM = tubes.GetNIM
GetNama = tubes.GetNama
GetNamaMK = tubes.GetNamaMK
GetSKS = tubes.GetSKS
GetNilai = tubes.GetNilai
GetMhs = tubes.GetMhs
GetListMatkul = tubes.GetListMatkul
NilaiSekarangMK = tubes.NilaiSekarangMK
SudahAmbilMK = tubes.SudahAmbilMK
MengulangMK = tubes.MengulangMK
LulusMK = tubes.LulusMK
CariMatkul = tubes.CariMatkul
TotalSKSLulus = tubes.TotalSKSLulus
JumlahMatkulMengulang = tubes.JumlahMatkulMengulang
IPKTranskrip = tubes.IPKTranskrip
AddTranskrip = tubes.AddTranskrip
AddNilaiMatkul = tubes.AddNilaiMatkul
CariTranskripMhs = tubes.CariTranskripMhs
TopIPK = tubes.TopIPK
CountMhsPernahMengulang = tubes.CountMhsPernahMengulang
CountMhsLulusSemuaMatkul = tubes.CountMhsLulusSemuaMatkul
MatkulPalingSeringDiulang = tubes.MatkulPalingSeringDiulang
CountMhsDenganIPKRentang = tubes.CountMhsDenganIPKRentang
TotalSKS = tubes.TotalSKS

# ============================================================
# HELPER FUNCTION
# ============================================================
def header(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def test(name, result, expected):
    status = "PASS" if result == expected else "FAIL"
    print(f"  [{status}] {name}")
    print(f"         Hasil   : {result}")
    print(f"         Expected: {expected}")

# ============================================================
# TEST CASE 1: TIPE MAHASISWA (Mhs)
# ============================================================
header("TEST CASE 1: TIPE MAHASISWA (Mhs)")

# Normal Case
print("\n[Normal Case]")
test("MakeMhs - konstruktor",
     MakeMhs("24060122130001", "Ahmad"),
     ("24060122130001", "Ahmad"))

test("GetNIM - selektor NIM",
     GetNIM(MakeMhs("24060122130001", "Ahmad")),
     "24060122130001")

test("GetNama - selektor nama",
     GetNama(MakeMhs("24060122130001", "Ahmad")),
     "Ahmad")

# Edge Case
print("\n[Edge Case]")
test("MakeMhs - NIM dan nama kosong",
     MakeMhs("", ""),
     ("", ""))

test("GetNIM - dari Mhs kosong",
     GetNIM(MakeMhs("", "")),
     "")

# ============================================================
# TEST CASE 2: TIPE MATA KULIAH (Matkul)
# ============================================================
header("TEST CASE 2: TIPE MATA KULIAH (Matkul)")

# Normal Case
print("\n[Normal Case]")
test("MakeMatkul - konstruktor",
     MakeMatkul("Daspro", 3, [2.0, 3.0]),
     ("Daspro", 3, [2.0, 3.0]))

test("GetNamaMK - selektor nama MK",
     GetNamaMK(MakeMatkul("Daspro", 3, [2.0, 3.0])),
     "Daspro")

test("GetSKS - selektor SKS",
     GetSKS(MakeMatkul("Daspro", 3, [2.0, 3.0])),
     3)

test("GetNilai - selektor list nilai",
     GetNilai(MakeMatkul("Daspro", 3, [2.0, 3.0])),
     [2.0, 3.0])

test("NilaiSekarangMK - nilai terakhir dari list",
     NilaiSekarangMK(MakeMatkul("Daspro", 3, [2.0, 3.0])),
     3.0)

test("SudahAmbilMK - sudah ada nilai",
     SudahAmbilMK(MakeMatkul("Daspro", 3, [3.0])),
     True)

test("MengulangMK - list nilai > 1",
     MengulangMK(MakeMatkul("Daspro", 3, [2.0, 3.0])),
     True)

test("MengulangMK - list nilai = 1",
     MengulangMK(MakeMatkul("Daspro", 3, [3.0])),
     False)

test("LulusMK - nilai >= 2.0",
     LulusMK(MakeMatkul("Daspro", 3, [3.0])),
     True)

test("LulusMK - nilai < 2.0",
     LulusMK(MakeMatkul("Daspro", 3, [1.5])),
     False)

# Edge Case
print("\n[Edge Case]")
test("NilaiSekarangMK - list kosong",
     NilaiSekarangMK(MakeMatkul("Daspro", 3, [])),
     -1.0)

test("SudahAmbilMK - list kosong",
     SudahAmbilMK(MakeMatkul("Daspro", 3, [])),
     False)

test("MengulangMK - list kosong",
     MengulangMK(MakeMatkul("Daspro", 3, [])),
     False)

test("LulusMK - nilai pas batas 2.0",
     LulusMK(MakeMatkul("Daspro", 3, [2.0])),
     True)

# ============================================================
# TEST CASE 3: TIPE TRANSKRIP
# ============================================================
header("TEST CASE 3: TIPE TRANSKRIP")

# Normal Case
print("\n[Normal Case]")
test("MakeTranskrip - konstruktor",
     GetNIM(GetMhs(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])]))),
     "001")

test("GetMhs - selektor mahasiswa",
     GetMhs(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])])),
     ("001", "Ahmad"))

test("CariMatkul - matkul ditemukan",
     GetNamaMK(CariMatkul(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0]), MakeMatkul("Strukdis", 3, [4.0])]), "Daspro")),
     "Daspro")

test("TotalSKSLulus - semua lulus",
     TotalSKSLulus(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0]), MakeMatkul("Aljabar Linear", 3, [4.0])])),
     6)

test("JumlahMatkulMengulang - ada yang mengulang",
     JumlahMatkulMengulang(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("MTK1", 3, [4.0])])),
     1)

test("IPKTranskrip - hitung IPK",
     IPKTranskrip(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0]), MakeMatkul("Pancasila", 2, [4.0])])),
     3.4)

# Edge Case
print("\n[Edge Case]")
test("CariMatkul - matkul tidak ditemukan",
     CariMatkul(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])]), "Dasar Sistem"),
     [])

test("TotalSKSLulus - tidak ada yang lulus",
     TotalSKSLulus(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [1.0]), MakeMatkul("Strukdis", 3, [1.5])])),
     0)

test("JumlahMatkulMengulang - tidak ada mengulang",
     JumlahMatkulMengulang(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0]), MakeMatkul("Aljabar Linear", 3, [4.0])])),
     0)

test("IPKTranskrip - list matkul kosong",
     IPKTranskrip(MakeTranskrip(MakeMhs("001", "Ahmad"), [])),
     0.0)

test("IPKTranskrip - semua matkul belum ada nilai",
     IPKTranskrip(MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, []), MakeMatkul("MTK1", 3, [])])),
     0.0)

# ============================================================
# TEST CASE 4: SET TRANSKRIP - OPERATOR DASAR
# ============================================================
header("TEST CASE 4: SET TRANSKRIP - OPERATOR DASAR")

# Normal Case
print("\n[Normal Case]")
test("AddTranskrip - tambah ke set kosong",
     len(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])]))),
     1)

test("AddTranskrip - tambah mahasiswa baru",
     len(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Strukdis", 3, [4.0])]))),
     2)

test("CariTranskripMhs - ditemukan",
     GetNama(GetMhs(CariTranskripMhs(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])])), "001"))),
     "Ahmad")

test("AddNilaiMatkul - tambah nilai baru",
     GetNilai(CariMatkul(CariTranskripMhs(AddNilaiMatkul(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [2.0])])), "001", "Daspro", 3.0), "001"), "Daspro")),
     [2.0, 3.0])

# Edge Case
print("\n[Edge Case]")
test("AddTranskrip - duplikat NIM tidak ditambah",
     len(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])])), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Pancasila", 2, [4.0])]))),
     1)

test("CariTranskripMhs - tidak ditemukan",
     CariTranskripMhs(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])])), "999"),
     [])

test("CariTranskripMhs - set kosong",
     CariTranskripMhs(MakeSetTranskrip([]), "001"),
     [])

# ============================================================
# TEST CASE 5: SET TRANSKRIP - OPERATOR LANJUTAN
# ============================================================
header("TEST CASE 5: SET TRANSKRIP - OPERATOR LANJUTAN")

# Normal Case
print("\n[Normal Case]")
test("TopIPK - mahasiswa IPK tertinggi",
     GetNama(TopIPK(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Daspro", 3, [3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Aljabar Linear", 3, [4.0])])))),
     "Budi")

test("CountMhsPernahMengulang - ada yang mengulang",
     CountMhsPernahMengulang(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("MTK1", 3, [2.0, 3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Daspro", 3, [4.0])]))),
     1)

test("CountMhsLulusSemuaMatkul - semua lulus",
     CountMhsLulusSemuaMatkul(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Strukdis", 3, [3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Pancasila", 2, [4.0])]))),
     2)

test("MatkulPalingSeringDiulang",
     MatkulPalingSeringDiulang(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Dasar Sistem", 3, [2.0, 3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Dasar Sistem", 3, [1.0, 4.0])]))),
     "Dasar Sistem")

test("CountMhsDenganIPKRentang - rentang 3.0-4.0",
     CountMhsDenganIPKRentang(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("MTK1", 3, [3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Aljabar Linear", 3, [4.0])])), 3.0, 4.0),
     2)

# Edge Case
print("\n[Edge Case]")
test("TopIPK - set kosong",
     TopIPK(MakeSetTranskrip([])),
     None)

test("TopIPK - satu mahasiswa",
     GetNama(TopIPK(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Strukdis", 3, [3.0])])))),
     "Ahmad")

test("CountMhsPernahMengulang - tidak ada mengulang",
     CountMhsPernahMengulang(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Pancasila", 2, [3.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Dasar Sistem", 3, [4.0])]))),
     0)

test("CountMhsLulusSemuaMatkul - ada tidak lulus",
     CountMhsLulusSemuaMatkul(AddTranskrip(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("MTK1", 3, [1.0])])), MakeTranskrip(MakeMhs("002", "Budi"), [MakeMatkul("Aljabar Linear", 3, [4.0])]))),
     1)

test("CountMhsDenganIPKRentang - tidak ada dalam rentang",
     CountMhsDenganIPKRentang(AddTranskrip(MakeSetTranskrip([]), MakeTranskrip(MakeMhs("001", "Ahmad"), [MakeMatkul("Strukdis", 3, [3.0])])), 4.5, 5.0),
     0)

test("CountMhsDenganIPKRentang - set kosong",
     CountMhsDenganIPKRentang(MakeSetTranskrip([]), 0.0, 4.0),
     0)

# ============================================================
# RINGKASAN
# ============================================================
header("TEST CASE SELESAI")
print("\nSemua test case telah dijalankan.")
print("Periksa hasil di atas untuk melihat status PASS/FAIL.")
