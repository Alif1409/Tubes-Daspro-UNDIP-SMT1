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
    if isEmpty(GetListMatkul(T)):
        return 0.0
    else:
        return 0.0
# APLIKASI TESTING
print("="*50)
print("TESTING FUNGSI-FUNGSI TRANSKRIP")
print("="*50)
M = MakeMhs("24060122130077", "Budi Santoso")
print(GetNIM(M))  # Output: "24060122130077"
print(GetNama(M)) # Output: "Budi Santoso"
MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0])
MK2 = MakeMatkul("Matdis", 2, [])
print(GetNamaMK(MK1))  # Output: "Daspro"
print(GetSKS(MK1))     # Output: 3
print(GetNilai(MK1))   # Output: [2.0, 3.0]
print(NilaiSekarangMK(MK1))  # Output: 3.0
print(NilaiSekarangMK(MK2))  # Output: -1.0
print(SudahAmbilMK(MK2))
print(MengulangMK(MK1))  # Output: True
print(LulusMK(MK1))

MK3 = MakeMatkul("Daspro", 3, [2.0, 3.0])
MK4 = MakeMatkul("Matdis", 2, [3.0, 4.0])
T = MakeTranskrip(M, [MK3, MK4])
print(GetMhs(T))  # Output: Mhs
print(GetListMatkul(T))  # Output: [MK1, MK2]
print(CariMatkul(T, "Daspro"))  # Output: MK1
print(TotalSKSLulus(T))  # Output: 5
print(JumlahMatkulMengulang(T))  # Output: 2

print("="*50)
print("TESTING FUNGSI-FUNGSI TRANSKRIP")
print("="*50)


