# 2 Bagian 1 — Tipe Bentukan Dasar
# 2.1 Tipe Mahasiswa (Mhs)
# Definisi: Type Mhs berisi nim dan nama.

# Type Mhs: tuple of (string, string)
# {Mhs adalah tipe data untuk merepresentasikan
#  data mahasiswa yang terdiri dari NIM dan nama}
type Mhs = tuple[str, str]

#DEFINISI DAN SPESIFIKASI KONTRUKTOR
# MakeMhs: <string, string> → Mhs
# {MakeMhs(nim, nama) membuat objek Mhs dengan NIM nim dan nama
# nama}
def MakeMhs(nim: str, nama: str) -> Mhs:
    return (nim, nama)

#DEFINISI DAN SPESIFIKASI SELEKTOR
# {GetNIM(M) mengambil NIM dari mahasiswa M}
def GetNIM(M: Mhs) -> str:
    return M[0]

# {GetNama(M) mengambil nama dari mahasiswa M}
def GetNama(M: Mhs) -> str:
    return M[1]

# 2.2 Tipe Mata Kuliah (Matkul)
# Definisi: Matkul memiliki namamk, sks, dan list nilai (0–4) yang terurut naik. Nilai
# terakhir adalah nilai akhir.

# Type Matkul: tuple of (string, integer, list of real)
# {Matkul adalah tipe data untuk merepresentasikan
#  data mata kuliah yang terdiri dari nama mata kuliah, jumlah SKS, dan list nilai}
type Matkul = tuple[str, int, list]

#DEFINISI DAN SPESIFIKASI KONTRUKTOR

# MakeMatkul: <string, integer, list of real> → Matkul
# {MakeMatkul(nama, sks, listNilai) membuat objek Matkul dengan nama
# mata kuliah nama, jumlah SKS sks, dan list nilai listNilai}
def MakeMatkul(nama: str, sks: int, listnilai: list) -> Matkul:
    return (nama, sks, listnilai)

#DEFINISI DAN SPESIFIKASI SELEKTOR

# GetNamaMK: Matkul → string
# {GetNamaMK(MK) mengambil nama mata kuliah dari MK}
def GetNamaMK(MK: Matkul) -> str:
    return MK[0]

# GetSKS: Matkul → integer
# {GetSKS(MK) mengambil jumlah SKS dari MK}
def GetSKS(MK: Matkul) -> int:
    return MK[1]

# GetNilai: Matkul → list of real
# {GetNilai(MK) mengambil list nilai dari MK}
def GetNilai(MK: Matkul) -> list:
    return MK[2]

 # FirstElmt(L): List tidak kosong -> elemen
 #  {FirstElmt(L) mengembalikan elemen pertama dari L.}
 # Realisasi:
def FirstElmt(L):
    return L[0]

 # LastElmt(L): List tidak kosong -> elemen
 #  {LastElmt(L) mengembalikan elemen terakhir dari L.}
 # Realisasi:
def LastElmt(L):
    return L[-1]

 # Head(L): List tidak kosong -> List
 #  {Head(L) mengembalikan list L tanpa elemen terakhir 
#   dari L; dapat menghasilkan list kosong.}
 # Realisasi:
def Head(L):
    return L[:-1]

 # Tail(L): List tidak kosong -> List
 #  {Tail(L) mengembalikan list L tanpa elemen pertama 
 #   dari L; dapat menghasilkan list kosong.}
def Tail(L):
    return L[1:]

 # DEFINISI DAN SPESIFIKASI PREDIKAT
 # isEmpty(L): List -> boolean
 #  {isEmpty(L) bernilai True jika List merupakan list kosong.}
def isEmpty(L):
    return L == []

 # IsOneElmt(L): List -> boolean
 #  {IsOneElmt(L) bernilai True jika List hanya memiliki 
 #   tepat satu elemen.}
def IsOneElmt(L):
    if isEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []

#IsMember: elemen, List -> boolean
# {IsMember(e,L) mengembalikan true jika e adalah anggota dari L}
def IsMember (X, L):
    if isEmpty (L):
        return False
    elif FirstElmt (L) == X:
        return True
    else:
        return IsMember (X, Tail (L))



# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
 # Konso: elemen, List -> List
 #  {Konso(e, L) menghasilkan sebuah list dari e dan L 
 #   dengan e sebagai elemen pertama dari L.}
def Konso (E, L):
    return [E] + L

 # Konsi: elemen, List -> List
 # {Konsi(e, L) menghasilkan sebuah list dari e dan L
 # dengan e sebagai elemen terakhir dari L.}
def Konsi (L,E):
    return L + [E]

# Fungsi konsLo (L, S)  membentuk list baru dengan list (L) sebagai elemen pertama list of list 
# konsLo: list, list of list -> list of list
def konsLo(L, S):
    return [L] + S

# Fungsi konsLi (S, L) membentuk list baru dengan list (L) sebagai elemen terakhir list of list
# konsLi: list of list, list -> list of list
def konsLi(S, L):
    return S + [L]


# DEFINISI DAN SPESIFIKASI OPERATOR

# NilaiSekarangMK: Matkul → real
# {NilaiSekarangMK(MK) mengambil nilai akhir dari MK.}
# {Jika list kosong → −1.0.}
# {Jika tidak → elemen terakhir}
def NilaiSekarangMK(MK: Matkul) -> float:
    if isEmpty(GetNilai(MK)):
        return -1.0
    else:
        if IsOneElmt(GetNilai(MK)):
            return FirstElmt(GetNilai(MK))
        else:
            return NilaiSekarangMK(MakeMatkul(GetNamaMK(MK), GetSKS(MK), Tail(GetNilai(MK))))

# SudahAmbilMK: Matkul → boolean
# {SudahAmbilMK(MK) mengembalikan True jika list nilai MK tidak kosong}
def SudahAmbilMK(MK: Matkul) -> bool:
    if isEmpty(GetNilai(MK)):
        return False
    else:
        return True

# MengulangMK: Matkul → boolean
# {MengulangMK(MK) mengembalikan True jika panjang list nilai MK > 1}
def MengulangMK(MK: Matkul) -> bool:
    if isEmpty(GetNilai(MK)):
        return False
    else:
        if IsOneElmt(GetNilai(MK)):
            return False
        else:
            return True

# LulusMK: Matkul → boolean
# {LulusMK(MK) mengembalikan True jika nilai akhir MK ≥ 2.0}
def LulusMK(MK: Matkul) -> bool:
    if NilaiSekarangMK(MK) >= 2.0:
        return True
    else:
        return False
    
# 2.3 Tipe Transkrip
# Definisi: Transkrip berisi data mahasiswa dan daftar mata kuliahnya.
# Type Transkrip: tuple of (Mhs, list of Matkul)
# {Transkrip adalah tipe data untuk merepresentasikan
#  data transkrip yang terdiri dari data mahasiswa dan list mata kuliah}
type Transkrip = tuple[Mhs, Matkul]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeTranskrip: <Mhs, list of Matkul> → Transkrip
# {MakeTranskrip(M, listMK) membuat objek Transkrip dengan data
# mahasiswa M dan list mata kuliah listMK}
def MakeTranskrip(M: Mhs, ListMK: Matkul) -> Transkrip:
    return (M, ListMK)

# DEFINISI DAN SPESIFIKASI SELEKTOR
# GetMhs: Transkrip → Mhs
# {GetMhs(T) mengambil data mahasiswa dari transkrip T}
def GetMhs(T: Transkrip) -> Mhs:
    return T[0]

# GetListMatkul: Transkrip → list of Matkul
# {GetListMatkul(T) mengambil list mata kuliah dari transkrip T}
def GetListMatkul(T: Transkrip) -> Matkul:
    return T[1]

#DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# TotalNilaiSKS: Transkrip → real
# {TotalNilaiSKS(T) menghitung total dari NilaiAkhir * SKS untuk setiap matkul di T}
# {Hanya menghitung matkul yang sudah ada nilainya (SudahAmbilMK = True)}
def TotalNilaiSKS(T: Transkrip) -> float:
    if isEmpty(GetListMatkul(T)):
        return 0.0
    else:
        if SudahAmbilMK(FirstElmt(GetListMatkul(T))):
            return (NilaiSekarangMK(FirstElmt(GetListMatkul(T))) * GetSKS(FirstElmt(GetListMatkul(T)))) + TotalNilaiSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return TotalNilaiSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
    
# TotalSKS: Transkrip → integer
# {TotalSKS(T) menghitung total SKS dari semua matkul di T}
# {Hanya menghitung matkul yang sudah ada nilainya (SudahAmbilMK = True)}
def TotalSKS(T: Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        if SudahAmbilMK(FirstElmt(GetListMatkul(T))):
            return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return TotalSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

# DEFINISI DAN SPESIFIKASI OPERATOR

# CariMatkul: <Transkrip, string> → Matkul
# {CariMatkul(T, namaMK) mencari dan mengambil Matkul dari
# transkrip T berdasarkan nama mata kuliah namaMK}
def CariMatkul(T: Transkrip, namaMK: str) -> Matkul:
    if isEmpty(GetListMatkul(T)):
        return GetListMatkul(T)
    else:
        if GetNamaMK(FirstElmt(GetListMatkul(T))) == namaMK:
            return FirstElmt(GetListMatkul(T))
        else:
            return CariMatkul(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))), namaMK)

# TotalSKSLulus: Transkrip → integer
# {TotalSKSLulus(T) menjumlahkan seluruh SKS dari mata kuliah yang lulus
# (nilai ≥ 2.0) pada transkrip T}
def TotalSKSLulus(T: Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        if LulusMK(FirstElmt(GetListMatkul(T))):
            return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKSLulus(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return TotalSKSLulus(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
    
#  IPKTranskrip: Transkrip → real
#  {IPKTranskrip(T) menghitung IPK dari transkrip T dengan rumus:
#  Σ(NilaiAkhir * SKS)/ ΣSKS}
def IPKTranskrip(T: Transkrip) -> float:
    if TotalSKS(T) == 0:
        return 0.0
    else:
        return TotalNilaiSKS(T) / TotalSKS(T)

# Bagian 2 — Set Transkrip
# Definisi: SetTranskrip adalah list berisi beberapa Transkrip mahasiswa.

# DEFINISI DAN SPESIFIKASI KONSTRUKOR
# MakeSetTranskrip: → SetTranskrip
# {MakeSetTranskrip() membuat SetTranskrip kosong (list kosong)}
def MakeSetTranskrip( SetTranskrip: list) -> list:
    return  SetTranskrip

# DEFINISI DAN SPESIFIKASI SELEKTOR
# GetAllNamaMatkul: SetTranskrip -> list
# {GetAllNamaMatkul(S) mengumpulkan semua nama mata kuliah dari SetTranskrip S tanpa duplikat}
def GetAllNamaMatkul(S: list) -> list:
    if isEmpty(S):
        return []
    else:
        return GabungNamaMatkul(GetNamaMatkulDariList(GetListMatkul(FirstElmt(S))), GetAllNamaMatkul(Tail(S)))

# GetNamaMatkulDariList: list -> list
# {GetNamaMatkulDariList(ListMK) mengambil semua nama matkul dari ListMK}
def GetNamaMatkulDariList(ListMK: list) -> list:
    if isEmpty(ListMK):
        return []
    else:
        return Konso(GetNamaMK(FirstElmt(ListMK)), GetNamaMatkulDariList(Tail(ListMK)))
    
# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# UpdateListMatkul: <list of Matkul, string, real> → list of Matkul
 # {UpdateListMatkul(ListMK, namaMK, nilai) mengupdate list mata kuliah
 # ListMK dengan menambahkan nilai baru nilai ke mata kuliah namaMK}       
def UpdateListMatkul(ListMK: list, namaMK: str, nilai: float) -> list:
    if isEmpty(ListMK):
        return ListMK
    else:
        if GetNamaMK(FirstElmt(ListMK)) == namaMK:
            return Konso(MakeMatkul(GetNamaMK(FirstElmt(ListMK)), GetSKS(FirstElmt(ListMK)), Konsi(GetNilai(FirstElmt(ListMK)), nilai)), Tail(ListMK))
        else:
            return Konso(FirstElmt(ListMK), UpdateListMatkul(Tail(ListMK), namaMK, nilai))

 # JumlahMatkulMengulang: Transkrip → integer
 # {JumlahMatkulMengulang(T) menghitung jumlah mata kuliah yang
 # diulang (panjang list nilai > 1) pada transkrip T}
def JumlahMatkulMengulang(T: Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        if MengulangMK(FirstElmt(GetListMatkul(T))):
            return 1 + JumlahMatkulMengulang(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return JumlahMatkulMengulang(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        
    
# CountMengulangDiTranskrip: <string, list> -> integer
# {CountMengulangDiTranskrip(namaMK, ListMK) menghitung apakah matkul namaMK diulang di ListMK}
def CountMengulangDiTranskrip(namaMK: str, ListMK: list) -> int:
    if isEmpty(ListMK):
        return 0
    else:
        if GetNamaMK(FirstElmt(ListMK)) == namaMK:
            if MengulangMK(FirstElmt(ListMK)):
                return 1
            else:
                return 0
        else:
            return CountMengulangDiTranskrip(namaMK, Tail(ListMK))
        
# GabungNamaMatkul: <list, list> -> list
# {GabungNamaMatkul(L1, L2) menggabungkan L1 dan L2 tanpa duplikat}
def GabungNamaMatkul(L1: list, L2: list) -> list:
        if isEmpty(L1):
            return L2
        else:
            if IsMember(FirstElmt(L1), L2):
                return GabungNamaMatkul(Tail(L1), L2)
            else:
                return GabungNamaMatkul(Tail(L1), Konso(FirstElmt(L1), L2))
    
    # MaxFrekuensiMatkul: <SetTranskrip, list> -> string
    # {MaxFrekuensiMatkul(S, matkulList) mencari nama matkul dengan frekuensi mengulang tertinggi}
def MaxFrekuensiMatkul(S: list, matkulList: list) -> str:
        if isEmpty(matkulList):
            return ""
        elif IsOneElmt(matkulList):
            return FirstElmt(matkulList)
        else:
            return BandingkanFrekuensi(S, FirstElmt(matkulList), MaxFrekuensiMatkul(S, Tail(matkulList)))
    
    # BandingkanFrekuensi: <SetTranskrip, string, string> -> string
    # {BandingkanFrekuensi(S, mk1, mk2) membandingkan frekuensi mk1 dan mk2, mengembalikan yang lebih besar}
def BandingkanFrekuensi(S: list, mk1: str, mk2: str) -> str:
        if mk2 == "":
            return mk1
        else:
            if CountFrekuensiMengulang(mk1, S) > CountFrekuensiMengulang(mk2, S):
                return mk1
            else:
                return mk2
# CountFrekuensiMengulang: <string, SetTranskrip> -> integer
# {CountFrekuensiMengulang(namaMK, S) menghitung berapa kali mata kuliah namaMK diulang di seluruh SetTranskrip S}
def CountFrekuensiMengulang(namaMK: str, S: list) -> int:
    if isEmpty(S):
         return 0
    else:
        return CountMengulangDiTranskrip(namaMK, GetListMatkul(FirstElmt(S))) + CountFrekuensiMengulang(namaMK, Tail(S))
    
# DEFINISI DAN SPESIFIKASI OPERATOR
# AddTranskrip: <SetTranskrip, Transkrip> → SetTranskrip
# {AddTranskrip(S, T) menambahkan transkrip T ke akhir SetTranskrip S
# jika NIM mahasiswa pada T belum ada di S.
# Jika sudah ada, tidak ditambahkan}
def AddTranskrip(S: list, T: Transkrip) -> MakeSetTranskrip:
    if isEmpty(S):
        return Konso(T, S)
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == GetNIM(GetMhs(T)):
            return S
        else:
            return Konso(FirstElmt(S), AddTranskrip(Tail(S), T))

# AddNilaiMatkul: <SetTranskrip, string, string, real> →
# SetTranskrip
# {AddNilaiMatkul(S, nim, namaMK, nilai) menambahkan nilai baru nilai ke
# mata kuliah namaMK pada transkrip mahasiswa dengan NIM nim di
# SetTranskrip S}
def AddNilaiMatkul(S: list, nim: str, namaMK: str, nilai: float) -> MakeSetTranskrip:
    if isEmpty(S):
        return S
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == nim:
            return Konso(MakeTranskrip(GetMhs(FirstElmt(S)), UpdateListMatkul(GetListMatkul(FirstElmt(S)), namaMK, nilai)), Tail(S))
        else:
            return Konso(FirstElmt(S), AddNilaiMatkul(Tail(S), nim, namaMK, nilai))
        
# CariTranskripMhs: <SetTranskrip, string> → Transkrip
# {CariTranskripMhs(S, nim) mencari dan mengembalikan transkrip pertama
# dengan NIM nim dari SetTranskrip S}
def CariTranskripMhs(S: list, nim: str) -> Transkrip:
    if isEmpty(S):
        return []
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == nim:
            return FirstElmt(S)
        else:
            return CariTranskripMhs(Tail(S), nim)
        
# TopIPK: SetTranskrip → Mhs
# {TopIPK(S) menghasilkan mahasiswa dengan IPK tertinggi dari
# SetTranskrip S }
def TopIPK(S: list) -> Mhs:
    if isEmpty(S):
        return None  # Return None jika list kosong
    elif IsOneElmt(S):
        return GetMhs(FirstElmt(S))
    else:
        if IPKTranskrip(FirstElmt(S)) >= IPKTranskrip(CariTranskripMhs(S, GetNIM(TopIPK(Tail(S))))):
            return GetMhs(FirstElmt(S))
        else:
            return TopIPK(Tail(S))
        
# CountMhsPernahMengulang: SetTranskrip → integer
# {CountMhsPernahMengulang(S) menghitung jumlah mahasiswa yang
# pernah mengulang minimal 1 mata kuliah pada SetTranskrip S}
def CountMhsPernahMengulang(S: list) -> int:
    if isEmpty(S):
        return 0
    else:
        if JumlahMatkulMengulang(FirstElmt(S)) > 0:
            return 1 + CountMhsPernahMengulang(Tail(S))
        else:
            return CountMhsPernahMengulang(Tail(S))
        
# CountMhsLulusSemuaMatkul: SetTranskrip → integer
# {CountMhsLulusSemuaMatkul(S) menghitung jumlah mahasiswa yang
# lulus seluruh mata kuliah yang diambil pada SetTranskrip S}
# CountMhsLulusSemuaMatkul: SetTranskrip → integer
# {CountMhsLulusSemuaMatkul(S) menghitung jumlah mahasiswa yang
# lulus seluruh mata kuliah yang diambil pada SetTranskrip S}
def CountMhsLulusSemuaMatkul(S: list) -> int:
    if isEmpty(S):
        return 0
    else:
        if TotalSKSLulus(FirstElmt(S)) == TotalSKS(FirstElmt(S)):
            return 1 + CountMhsLulusSemuaMatkul(Tail(S))
        else:
            return CountMhsLulusSemuaMatkul(Tail(S))


# MatkulPalingSeringDiulang: SetTranskrip → string
# {MatkulPalingSeringDiulang(S) menghasilkan nama mata kuliah yang
# paling sering diulang (frekuensi tertinggi) pada SetTranskrip S}
def MatkulPalingSeringDiulang(S: list) -> str:
    # CountFrekuensiMengulang: <string, SetTranskrip> -> integer
    # {CountFrekuensiMengulang(namaMK, S) menghitung berapa kali mata kuliah namaMK diulang di seluruh SetTranskrip S}
    def CountFrekuensiMengulang(namaMK: str, S: list) -> int:
        if isEmpty(S):
            return 0
        else:
            return CountMengulangDiTranskrip(namaMK, GetListMatkul(FirstElmt(S))) + CountFrekuensiMengulang(namaMK, Tail(S))
    return MaxFrekuensiMatkul(S, GetAllNamaMatkul(S))


# {CountMhsDenganIPKRentang(S, a, b) menghitung jumlah mahasiswa
# dengan IPK dalam rentang [a, b] pada SetTranskrip S}
# {CountMhsDenganIPKRentang(S, a, b) menghitung jumlah mahasiswa
# dengan IPK dalam rentang [a, b] pada SetTranskrip S}
def CountMhsDenganIPKRentang(S: list, a: float, b: float) -> int:
    if isEmpty(S):
        return 0
    else:
        ipk = IPKTranskrip(FirstElmt(S))
        if a <= ipk <= b:
            return 1 + CountMhsDenganIPKRentang(Tail(S), a, b)
        else:
            return CountMhsDenganIPKRentang(Tail(S), a, b)
    
print("="*50)
print("Tubes RAPI - Implementasi Tipe Bentukan Data")
print("="*50)

print("="*50)
print("TES TIPE MHS")
print("="*50)
print(GetNIM(MakeMhs("A11.2020.01234", "Reno"))) # Output: "A11.2020.01234"
print(GetNama(MakeMhs("A11.2020.01234", "Reno"))) # Output: "Reno"

print("="*50)
print("TES TIPE MATKUL")
print("="*50)
print(GetNamaMK(MakeMatkul("Daspro", 3, [2.0, 3.0]))) # Output: "Daspro"
print(GetSKS(MakeMatkul("Daspro", 3, [2.0, 3.0]))) # Output: 3
print(GetNilai(MakeMatkul("Daspro", 3, [2.0, 3.0]))) # Output: [2.0, 3.0]
print(NilaiSekarangMK(MakeMatkul("Daspro", 3, [2.0, 3.0]))) # Output: 3.0
print(NilaiSekarangMK(MakeMatkul("Matdis", 2, [])))  # Output: -1.0
print(SudahAmbilMK(MakeMatkul("Matdis", 2, []))) # Output: false
print(MengulangMK(MakeMatkul("Daspro", 3, [2.0, 3.0]))) # Output: True
print(LulusMK(MakeMatkul("Daspro", 3, [2.0, 3.0]))) # Output: True

print("="*50)
print("TES TIPE TRANSKRIP")
print("="*50)
print(GetMhs(MakeTranskrip(MakeMhs("A11.2020.01234", "Reno"), [MakeMatkul("Daspro", 3, [2.0, 3.0]),  MakeMatkul("Matdis", 2, [3.0, 4.0])])))
print(GetListMatkul(MakeTranskrip(MakeMhs("A11.2020.01234", "Reno"), [MakeMatkul("Daspro", 3, [2.0, 3.0]),  MakeMatkul("Matdis", 2, [3.0, 4.0])])))
print(CariMatkul(MakeTranskrip(MakeMhs("A11.2020.01234", "Reno"), [MakeMatkul("Daspro", 3, [2.0, 3.0]),  MakeMatkul("Matdis", 2, [3.0, 4.0])]),"Daspro"))
print(TotalSKSLulus(MakeTranskrip(MakeMhs("A11.2020.01234", "Reno"), [MakeMatkul("Daspro", 3, [2.0, 3.0]),  MakeMatkul("Matdis", 2, [3.0, 4.0])])))
print(JumlahMatkulMengulang(MakeTranskrip(MakeMhs("A11.2020.01234", "Reno"), [MakeMatkul("Daspro", 3, [2.0, 3.0]),  MakeMatkul("Matdis", 2, [3.0, 4.0])])))
print(IPKTranskrip(MakeTranskrip(MakeMhs("A11.2020.01234", "Reno"), [MakeMatkul("Daspro", 3, [2.0, 3.0]),  MakeMatkul("Matdis", 2, [3.0, 4.0])])))

print("="*50)
print("TES OPERATOR PALING BAWAH")
print("="*50)
S1 = MakeSetTranskrip([])
M1 =MakeMhs("A11.01","Reno")
MK1 =MakeMatkul("Daspro",3,[2.0])
MK2 =MakeMatkul("Matdis",2,[3.0])
T1 =MakeTranskrip(M1,[MK1,MK2])
S2 =AddTranskrip(S1,T1)
S3 =AddTranskrip(S2,T1)
M2 =MakeMhs("A11.02","Andi")
MK3 =MakeMatkul("Daspro",3,[3.0])
MK4 =MakeMatkul("Matdis",2,[4.0])
T2 =MakeTranskrip(M2,[MK3,MK4])
S4 =AddTranskrip(S3,T2)
M3 =MakeMhs("A11.03","Budi")
MK5 =MakeMatkul("Daspro",3,[1.0,2.0])
MK6 =MakeMatkul("Kalkulus",4, [3.0])
T3 =MakeTranskrip(M3,[MK5,MK6])
S5 =AddTranskrip(S4,T3)
S6 = AddNilaiMatkul(S5,"A11.01","Daspro", 3.0)
S7 = AddNilaiMatkul(S6,"A11.02","Daspro", 4.0)

print("="*50)
print('TESTCASE DENGAN VARIABLE')
print("="*50)
print(CariTranskripMhs(S7,"A11.01"))
print(CariTranskripMhs(S7,"A11.03"))
print(TopIPK(S7))
print(CountMhsPernahMengulang(S7))
print(CountMhsLulusSemuaMatkul(S7))
print(MatkulPalingSeringDiulang(S7))
print(CountMhsDenganIPKRentang(S7,2.0, 3.0))

print("="*50)
print('TESTCASE TANPA VARIABLE')
print("="*50)
print(CariTranskripMhs([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])], "24060122130077"))
print(TopIPK([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(CountMhsPernahMengulang([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(CountMhsLulusSemuaMatkul([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(MatkulPalingSeringDiulang([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Daspro", 3, [2.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(CountMhsDenganIPKRentang([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])], 3.0, 4.0))
