# Program   : listfunctions.py
# Deskripsi : Fungsi-fungsi untuk operasi list
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 30/10/2024
# ============================================================================================================================================
# DEFINISI DAN SPESIFIKASI SERTA REALISASI
# ============================================================================================================================================
# Head: List tidak kosong -> List
# Head(L) mengoutput elemen dari list kecuali elemen terakhirnya
def Head(L):
    if IsEmpty(L):
        return None
    else: 
        return L[:-1]

# Tail: List tidak kosong -> boolean
# Tail(L) mengoutput elemen dari list kecuali elemen pertamanya
def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

# REALISASI KONSTRUKTOR
# Konso: elemen, List -> List
# Konso(e,L) menyatukan sebuah elemen dengan sebuah list dan menaruhnya di depan
def Konso(e, L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(e,L) menyatukan sebuah elemen dengan sebuah list dan menaruhnya di belakang
def Konsi(L, e):
    return L + [e]

# print("Hasil Konso:", Konso(1, [2, 3, 4, 5]))
# print("Hasil Konsi:", Konsi([1, 2, 3, 4], 5))

# REALISASI PREDIKAT
# IsEmpty: List -> boolean
# IsEmpty(L) predikat yang mengoutput True apabila sebuah list adalah himpunan kosong dan False jika sebaliknya
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> boolean
# IsOneElmt(L) mengoutput True jika sebuah list hanya memiliki satu element dan False jika sebaliknya
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:   
        return Tail(L) == [] and Head(L) == []

# print("\nHasil IsEmpty:", IsEmpty([]))
# print("Hasil IsOneElmt:", IsOneElmt([1, 2, 3 ,4 ,5]))

# REALISASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) selektor untuk mengambil nilai elemen pertama dari list
def FirstElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[0]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L) selektor untuk mengambil nilai elemen terakhir dari list
def LastElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[-1]

# print("\nHasil FirstElmt:", FirstElmt([]))
# print("Hasil LastElmt:", LastElmt([1,2,3,4,5]))

# print("\nHasil Tail:", Tail([0]))
# print("Hasil Head:", Head([1,2,3,4,5]))

# REALISASI OPERATOR
# NbElmt: List -> integer
# NbElmt(L) menghitung jumlah elemen pada sebuah list
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else: 
        return 1 + NbElmt(Tail(L))

# print("\nHasil NbElmt:", NbElmt([]))
# print("Hasil NbElmt:", NbElmt([1, 2, 3, 4, 5]))

# TUGAS REALISASI OPERATOR
# ElmtkeN: integer >= 0, List -> elemen
# ElmtkeN(N, L) : Mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N>=0
def ElmtkeN(N,L):
    if N <= NbElmt(L) and N >= 0:
        if N == 0:
            return FirstElmt(L)
        else:
            return ElmtkeN(N-1, Tail(L))

# print(ElmtkeN(2, [3,4,5]))

# IsMember: elemen, List -> boolean
# IsMember(X,L) adalah benar jika X adalah elemen list L
def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        if LastElmt(L) == x:
            return True
        else:
            return (IsMember(x, Head(L)))

# print(IsMember(2, [3, 4, 6, 2]))

# Copy: List -> List
# Copy(L) : Menghasilkan list yang identik dengan list asal
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

# print(Copy([2, 3, 4, 5]))

# Inverse: List -> List
# Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya
#   adalah kebalikan dari list asal
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

# print(Inverse([3, 70, 40, 55]))

# Konkat: 2 List -> List
# Konkat(L1,L2) : Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
def Konkat(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(L1 + [FirstElmt(L2)], Tail(L2))

# print(Konkat([10, 14, 60, 100], [35, 66, 90]))

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# print(SumElmt([1, 2, 3, 4, 5]))

# AvgElmt: List of integer -> integer
# AvgElmt(L) menghasilkan nilai rata-rata
def AvgElmt(L):
    return int(SumElmt(L)/NbElmt(L))

# print(AvgElmt([1, 2, 3, 4, 5]))

# MaxElmt: List of integer -> integer
# MaxElmt(L) mengembalikan elemen maksimun dari list L
def max2(x,y):
    return int((x+y+(abs(x-y)))/2)

def MaxElmt(L):
    if IsOneElmt(L):
        return LastElmt(L)
    else:
        return max2(FirstElmt(L), MaxElmt(Tail(L)))

# print(MaxElmt([1, 2, 10, 2, 3]))

# MaxNB: List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max,countMax>
#   dengan max adalah elemen maksimun list L
#   dan countMax adalah banyaknya kemunculan max di list L
def maxlist(x):
    if IsOneElmt(x):
        return LastElmt(x)
    else:
        return max2(LastElmt(x), maxlist(Head(x)))

def NbOcc(x, L):
    if IsOneElmt(L):
        if x == FirstElmt(L):
            return 1
        else:
            return 0
    else:
        if x == FirstElmt(L):
            return 1 + NbOcc(x, Tail(L))
        else:
            return NbOcc(x, Tail(L))

def MaxNb(L):
    return [maxlist(L), NbOcc(maxlist(L), L)]

# print(MaxNb([100, 100000, 3000000, 30000000, 30000000, 1000000000]))

# AddList: 2 List of integer -> List of integer
# AddList(L1,L2) menghasilkan list baru yang setiap elemennya
#   adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
def AddList(L1, L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return []
    else:
        return Konso((FirstElmt(L1) + FirstElmt(L2)), AddList(Tail(L1), Tail(L2)))

# print(AddList([1, 6, 10], [3, 9, 6]))

# IsPalindrom: List of character -> boolean
# IsPalindrom(L) benar jika L merupakan kata palindrom
#   yaitu kata yang sama jika dibaca dari kiri atau kanan
#   contoh: RUSAK, KASUR RUSAK, NABABAN
def IsPalindrom(L):
    if IsEmpty(L):
        return True
    elif IsOneElmt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Head(Tail(L)))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo : list, list of list --> list of list
# KonsLo(L,S) menambahkan list L sebagai elemen pertama dalam list of list S
def KonsLo(L,S):
    return [L] + S

# KonsLi : list of list, list --> list of list
# KonsLi(S,L) menambahkan list L sebagai elemen terakhir dalam list of list S
def KonsLi(S,L):
    return S + [L]

# DEIFINISI DAN SPESIFIKASI TYPE PREDIKAT KHUSUS LIST
# IsEmpty : list of list -> boolean
# IsEmpty(L) true jika list of list L kosong, false jika tidak
def IsEmpty(L):
    return L == []

# IsAtom : elemen -> boolean
# IsAtom(L) true jika list of list L adalah sebuah Atom, false jika tidak
def IsAtom(L):
    return type(L) != list

# IsList : elemen -> boolean
# IsList(L) true jika list of list L adalah sebuah List, false jika tidak
def IsList(L):
    return type(L) == list

# DEIFINISI DAN SPESIFIKASI SELECTOR
# FirstList : list of list tidak kosong -> list
# FirstList(S) mengembalikan elemen pertama dari list of list S (mungkin sebuah atom atau list).
def FirstList(S):
    if IsEmpty(S):
        return None
    else:
        return S[0]

# LastList : list of list tidak kosong -> list
# LastList(S) mengembalikan elemen terakhir dari list of list S (mungkin sebuah atom atau list).
def LastList(S):
    if IsEmpty(S):
        return None
    else:
        return S[-1]

# TailList : list of list tidak kosong -> list of list
# TailList(S) mengembalikan list of list yang elemen pertamanya dihapus.
def TailList(S):
    if IsEmpty(S):
        return None
    else:
        return S[1:]

# HeadList : list of list tidak kosong -> list of list
# HeadList(S) mengembalikan list of list yang elemen terakhirnya dihapus.
def HeadList(S):
    if IsEmpty(S):
        return None
    else:
        return S[:-1]

# IsMemberS: elemen, list of list-> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
def IsMemberS(x,S):
    if IsEmpty(S):
        return False
    elif IsList(FirstList(S)):
        if IsMember(x,FirstList(S)):
            return True
        else:
            return IsMemberS(x,TailList(S))
    else:
        if FirstList(S) == x:
            return True
        else:
            return IsMemberS(x, TailList(S))

# Rember: elemen, list of list > list of list
# Rember(x,S) menghapus semua elemen x yang ada di list of list S
def Rember(x,S):
    if IsEmpty(S):
        return []
    elif IsList(FirstElmt(S)):
        return KonsLo(Rember(x,FirstList(S)),Rember(x,TailList(S)))
    else:
        if FirstElmt(S) == x:
            return Rember(x,TailList(S))
        else:
            return KonsLo(FirstElmt(S),Rember(x,TailList(S)))

# Max: list of list > elemen
# Max(S) mengembalikan elemen maksimum di dalam list of list S
def Max(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return max2(max(FirstList(S)),Max(TailList(S)))
        else:
            return max2(FirstList(S),Max(TailList(S)))

# NBElmtAtom: list of list -> integer
# NBElmtAtom (S) mengembalikan banyaknya elemen list of list S yang berupa atom
def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return NBElmtAtom(TailList(S))
    else:
        return 1 + NBElmtAtom(TailList(S))

# NBElmtList: list of list -> integer 
# NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
def NBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return NBElmtList(TailList(S))
    else:
        return 1 + NBElmtList(TailList(S))

# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
def SumLoL(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return SumElmt(FirstList(S)) + SumLoL(TailList(S))
    else:
        return FirstList(S) + SumLoL(TailList(S))
    
# MaxNBElmtList: list of list --> integer
# MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S
def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return max2(NbElmt(FirstList(S)),MaxNBElmtList(TailList(S)))
    else:
        return MaxNBElmtList(TailList(S))
    
# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return max2(SumElmt(FirstList(S)),MaxSumElmt(TailList(S)))
        else:
            return max2(FirstList(S),MaxSumElmt(TailList(S)))
# print(IsPalindrom(['K', 'A', 'T', 'A', 'K']))


