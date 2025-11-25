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
    listNilai = GetNilai(MK)
    if isEmpty(listNilai):
        return -1.0
    else:
        return LastElmt(listNilai)
    

    
def SudahAmbilMK(T: Transkrip, namaMK: str) -> bool:
    listMK = GetListMatkul(T)
    if isEmpty(listMK):
        return False
    elif GetNamaMK(FirstElmt(listMK)) == namaMK:
        return True
    else:
        return SudahAmbilMK(MakeTranskrip(GetMhs(T), Tail(listMK)), namaMK)
    
def MengulangMK(MK: Matkul) -> bool:
    listNilai = GetNilai(MK)
    if isEmpty(listNilai):
        return False
    else:
        if IsOneElmt(listNilai):
            return False
        else:
            return True
        
def LulusMK(MK: Matkul) -> bool:
    nilaiAkhir = NilaiSekarangMK(MK)
    if nilaiAkhir >= 2.0:
        return True
    else:
        return False
    
def CariMatkul(T:Transkrip, namaMK: str) -> Matkul:
    listMK = GetListMatkul(T)
    if isEmpty(listMK):
        return None
    else: 
        if GetNamaMK(FirstElmt(listMK)) == namaMK:
            return FirstElmt(listMK)
        else:
            return CariMatkul(MakeTranskrip(GetMhs(T), Tail(listMK)), namaMK)
#Apilkasi
m1 = MakeMhs("123", "Andi")
mk1 = MakeMatkul("Algoritma", 3, [2.0,3.0,4.0])

print(NilaiSekarangMK(mk1)) #Output: 4.0
print(MengulangMK(mk1)) #Output: 4.0
print(LulusMK(mk1)) #Output: True
print(CariMatkul(MakeTranskrip(m1, [mk1]), "Algoritma")) #Output: mk1


