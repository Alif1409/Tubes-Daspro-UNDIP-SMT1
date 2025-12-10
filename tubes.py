#TYPE 
type Mhs = tuple[str, str]
type Matkul = tuple[str, int, list]
type Transkrip = tuple[Mhs, Matkul]

# Konstruktor
def MakeMhs(nim: str, nama: str) -> Mhs:
    return (nim, nama)

def MakeMatkul(nama: str, sks: int, listnilai: list) -> Matkul:
    return (nama, sks, listnilai)

def MakeTranskrip(M: Mhs, ListMK: Matkul) -> Transkrip:
    return (M, ListMK)

def MakeSetTranskrip(ListTranskrip: list) -> list:
    return ListTranskrip

 # Konso: elemen, List -> List
 #  {Konso(e, L) menghasilkan sebuah list dari e dan L 
#   dengan e sebagai elemen pertama dari L.}
 # Realisasi:
def Konso (E, L):
    return [E] + L
 # Aplikasi:
print(Konso(7, [2, 4, 6])) # -> [7, 2, 4, 6]

 # Konsi: elemen, List -> List
 #  {Konsi(e, L) menghasilkan sebuah list dari e dan L
 #   dengan e sebagai elemen terakhir dari L.}
# Realisasi:
def Konsi (L,E):
    return L + [E]
 # Aplikasi:
print(Konsi([6,7,8],9))# -> [6, 7, 8, 9]

# Fungsi konsLo (L, S)  membentuk list baru dengan list (L) sebagai elemen pertama list of list 
# konsLo: list, list of list -> list of list
def konsLo(L, S):
    return [L] + S

# Fungsi konsLi (S, L) membentuk list baru dengan list (L) sebagai elemen terakhir list of list
# konsLi: list of list, list -> list of list
def konsLi(S, L):
    return S + [L]


# Selektor
def GetNIM(M: Mhs) -> str:
    return M[0]

def GetNama(M: Mhs) -> str:
    return M[1]

def GetNamaMK(MK: Matkul) -> str:
    return MK[0]

def GetSKS(MK: Matkul) -> int:
    return MK[1]

def GetNilai(MK: Matkul) -> list:
    return MK[2]

def GetMhs(T: Transkrip) -> Mhs:
    return T[0]

def GetListMatkul(T: Transkrip) -> Matkul:
    return T[1]

# Fungsi firstList(S) yang mengembalikan elemen pertama dari list of list S (atom atau list)
# firstList: list of list tidak kosong -> list
def firstList(S):
    return S[0]

# Fungsi lastList(S) yang mengembalikan elemen terakhir dari list of list S (atom atau list)
# lastList: list of list tidak kosong -> list
def lastList(S):
    return S[-1]    

# Fungsi tailList(S) yang mengembalikan list of list S tanpa elemen pertamanya
# tailList: list of list tidak kosong -> list of list
def tailList(S):
    return S[1:]

# Fungsi headList(S) yang mengembalikan list of list S tanpa elemen terakhirnya
# headList: list of list tidak kosong -> list of list
def headList(S):
    return S[:-1]

# IsOneElmt(L): List -> boolean
#  {IsOneElmt(L) bernilai True jika List hanya memiliki
#   tepat satu elemen.}
# Realisasi:
def IsOneElmt(L):
 if isEmpty(L):
  return False
 else:
  return Tail(L)==[] and Head(L)==[]

#PENOLONG
def Head(List: list):
    return List[0]

def Tail(List: list):
    return List[1:]

def FirstElmt(List: list):
    return List[0]

def LastElmt(List: list):
    return List[-1]

def IsOneElmt(List: list) -> bool:
    return


 # DEFINISI DAN SPESIFIKASI SELEKTOR
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
 # Realisasi:
def Tail(L):
    return L[1:]
 # Aplikasi:



 # DEFINISI DAN SPESIFIKASI PREDIKAT
 # isEmpty(L): List -> boolean
 #  {isEmpty(L) bernilai True jika List merupakan list kosong.}
 # Realisasi:
def isEmpty(L):
    return L == []
 # Aplikasi:
print(isEmpty([]))# -> True
print(isEmpty([2,7]))# -> False
 # IsOneElmt(L): List -> boolean
 #  {IsOneElmt(L) bernilai True jika List hanya memiliki 
#   tepat satu elemen.}
 # Realisasi:
def IsOneElmt(L):
    if isEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []




# ElmtKeN : integer >=0, List -> elemen
# {ElmtKeN(N,L) mengembalikan elemen ke-N dari L}
def elmtKeN(N, L):
    if N == 1:
        return FirstElmt(L)
    else:
        return elmtKeN(N-1, Tail(L))



#IsMember: elemen, List -> boolean
# {IsMember(e,L) mengembalikan true jika e adalah anggota dari L}
def IsMember (X, L):
    if isEmpty (L):
        return False
    elif FirstElmt (L) == X:
        return True
    else:
        return IsMember (X, Tail (L))



# FUNGSI OPERATOR
def NilaiSekarangMK(MK: Matkul) -> float:
    if isEmpty(GetNilai(MK)):
        return -1.0
    else:
        if IsOneElmt(GetNilai(MK)):
            return FirstElmt(GetNilai(MK))
        else:
            return NilaiSekarangMK(MakeMatkul(GetNamaMK(MK), GetSKS(MK), Tail(GetNilai(MK))))

def SudahAmbilMK(MK: Matkul) -> bool:
    if isEmpty(GetNilai(MK)):
        return False
    else:
        return True
    
def MengulangMK(MK: Matkul) -> bool:
    if isEmpty(GetNilai(MK)):
        return False
    else:
        if IsOneElmt(GetNilai(MK)):
            return False
        else:
            return True

def LulusMK(MK: Matkul) -> bool:
    if NilaiSekarangMK(MK) >= 2.0:
        return True
    else:
        return False


#CariMatkul: <Transkrip, string> → Matkul
# {CariMatkul(T, namaMK) mencari dan mengambil Matkul dari
#  transkrip T berdasarkan nama mata kuliah namaMK}

def CariMatkul(T: Transkrip, namaMK: str) -> Matkul:
    if isEmpty(GetListMatkul(T)):
        return GetListMatkul(T)
    else:
        if GetNamaMK(FirstElmt(GetListMatkul(T))) == namaMK:
            return FirstElmt(GetListMatkul(T))
        else:
            return CariMatkul(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))), namaMK)

# TotalSKSLulus: Transkrip → integer
#  {TotalSKSLulus(T) menjumlahkan seluruh SKS dari mata kuliah yang lulus
#  (nilai ≥ 2.0) pada transkrip T}

def TotalSKSLulus(T: Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        if LulusMK(FirstElmt(GetListMatkul(T))):
            return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKSLulus(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))
        else:
            return TotalSKSLulus(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

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


#  IPKTranskrip: Transkrip → real
#  {IPKTranskrip(T) menghitung IPK dari transkrip T dengan rumus:
#  Σ(NilaiAkhir * SKS)/ ΣSKS}
def IPKTranskrip(T: Transkrip) -> float:
    if TotalSKS(T) == 0:
        return 0.0
    else:
        return TotalNilaiSKS(T) / TotalSKS(T)
# TotalNilaiSKS: Transkrip → real
# {TotalNilaiSKS(T) menghitung total dari NilaiAkhir * SKS untuk setiap matkul di T}
def TotalNilaiSKS(T: Transkrip) -> float:
    if isEmpty(GetListMatkul(T)):
        return 0.0
    else:
        return (NilaiSekarangMK(FirstElmt(GetListMatkul(T))) * GetSKS(FirstElmt(GetListMatkul(T)))) + TotalNilaiSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

# TotalSKS: Transkrip → integer
# {TotalSKS(T) menghitung total SKS dari semua matkul di T}
def TotalSKS(T: Transkrip) -> int:
    if isEmpty(GetListMatkul(T)):
        return 0
    else:
        return GetSKS(FirstElmt(GetListMatkul(T))) + TotalSKS(MakeTranskrip(GetMhs(T), Tail(GetListMatkul(T))))

# AddTranskrip: <SetTranskrip, Transkrip> → SetTranskrip
# {AddTranskrip(S, T) menambahkan transkrip T ke akhir SetTranskrip S
# jika NIM mahasiswa pada T belum ada di S.
# Jika sudah ada, tidak ditambahkan}
def AddTranskrip(S: list, T: Transkrip) -> list:
    if isEmpty(S):
        return Konso(T, S)
    else:
        if GetNIM(GetMhs(FirstElmt(S))) == GetNIM(GetMhs(T)):
            return S
        else:
            return Konso(FirstElmt(S), AddTranskrip(Tail(S), T))
        
def UpdateListMatkul(ListMK: list, namaMK: str, nilai: float) -> list:
    if isEmpty(ListMK):
        return ListMK
    else:
        if GetNamaMK(FirstElmt(ListMK)) == namaMK:
            return Konso(MakeMatkul(GetNamaMK(FirstElmt(ListMK)), GetSKS(FirstElmt(ListMK)), Konsi(GetNilai(FirstElmt(ListMK)), nilai)), Tail(ListMK))
        else:
            return Konso(FirstElmt(ListMK), UpdateListMatkul(Tail(ListMK), namaMK, nilai))
        
# AddNilaiMatkul: <SetTranskrip, string, string, real> →
# SetTranskrip
# {AddNilaiMatkul(S, nim, namaMK, nilai) menambahkan nilai baru nilai ke
# mata kuliah namaMK pada transkrip mahasiswa dengan NIM nim di
# SetTranskrip S}

def AddNilaiMatkul(S: list, nim: str, namaMK: str, nilai: float) -> list:
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
    
    return MaxFrekuensiMatkul(S, GetAllNamaMatkul(S))

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

        
        

# APLIKASI TESTING
print("="*50)
print("TESTING FUNGSI-FUNGSI TRANSKRIP")
print("="*50)

print(MakeMhs("24060122130077", "Budi Santoso"))
print(MakeMhs("24060122130078", "Siti Aminah"))
print(MakeMatkul("Daspro", 3, [2.0, 3.0]))
print(MakeMatkul("Matdis", 2, [4.0]))
print(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]))
print(GetNIM(MakeMhs("24060122130077", "Budi Santoso")))
print(GetNama(MakeMhs("24060122130077", "Budi Santoso")))
print(GetSKS(MakeMatkul("Daspro", 3, [2.0, 3.0])))
print(GetNilai(MakeMatkul("Daspro", 3, [2.0, 3.0])))
print(GetMhs(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])))
print(GetListMatkul(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])))
print(CariMatkul(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), "Daspro"))
print(TotalSKSLulus(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])))
print(JumlahMatkulMengulang(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])))
print(IPKTranskrip(MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])))
print(AddTranskrip([], MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])))
print(AddNilaiMatkul([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])], "24060122130077", "Daspro", 4.0))
print(CariTranskripMhs([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])])], "24060122130077"))
print(TopIPK([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(CountMhsPernahMengulang([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(CountMhsLulusSemuaMatkul([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(MatkulPalingSeringDiulang([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Daspro", 3, [2.0]), MakeMatkul("Pancasila", 2, [4.0])])]))
print(CountMhsDenganIPKRentang([MakeTranskrip(MakeMhs("24060122130077", "Budi Santoso"), [MakeMatkul("Daspro", 3, [2.0, 3.0]), MakeMatkul("Matdis", 2, [4.0])]), MakeTranskrip(MakeMhs("24060122130078", "Siti Aminah"), [MakeMatkul("Aljabar Linear", 3, [4.0]), MakeMatkul("Pancasila", 2, [4.0])])], 3.0, 4.0))

# print(GetSKS(MK1))     # Output: 3
# print(GetNilai(MK1))   # Output: [2.0, 3.0]
# print(NilaiSekarangMK(MK1))  # Output: 3.0
# print(NilaiSekarangMK(MK2))  # Output: -1.0
# print(SudahAmbilMK(MK2))
# print(MengulangMK(MK1))  # Output: True
# print(LulusMK(MK1))

# MK3 = MakeMatkul("Aljabar Linear", 3, [2.0, 3.0])
# MK4 = MakeMatkul("Pancasila", 2, [3.0, 4.0])

# T = MakeTranskrip(M, [MK3, MK4])
# T1 = MakeTranskrip(M2, [MK2, MK4])
# print(GetMhs(T))  # Output: Mhs
# print(GetListMatkul(T))  # Output: [MK1, MK2]
# print(CariMatkul(T, "Daspro"))  # Output: MK1
# print(TotalSKSLulus(T))  # Output: 5
# print(JumlahMatkulMengulang(T))  # Output: 2

# print("="*50)
# print("TESTING FUNGSI-FUNGSI TRANSKRIP")
# print("="*50)
# S = [T]
# print(AddNilaiMatkul(S, "24060122130077", "Daspro", 4.0))
# print(CariTranskripMhs(S, "24060122130077"))
# print(TopIPK(S)) 

