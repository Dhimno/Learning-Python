# Program   : listfunctions.py
# Deskripsi : Fungsi-fungsi untuk operasi list
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 30/10/2024

#REALISASI SELEKTOR AGAR FUNGSI BISA BERJALAN
# Head: List -> List
def Head(L):
    if IsEmpty(L):
        return None
    else: 
        return L[:-1]

# Tail: List -> boolean
def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

# REALISASI KONSTRUKTOR
# Konso: elemen, List -> List
def Konso(e, L):
    return [e] + L

# Konsi: List, elemen -> List
def Konsi(L, e):
    return L + [e]

# print("Hasil Konso:", Konso(1, [2, 3, 4, 5]))
# print("Hasil Konsi:", Konsi([1, 2, 3, 4], 5))

# REALISASI PREDIKAT
# IsEmpty: List -> boolean
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> boolean
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:   
        return Tail(L) == [] and Head(L) == []

# print("\nHasil IsEmpty:", IsEmpty([]))
# print("Hasil IsEmpty:", IsEmpty([1,2,3,4,5]))
# print("Hasil IsOneElmt:", IsOneElmt([]))
# print("Hasil IsOneElmt:", IsOneElmt([1]))
# print("Hasil IsOneElmt:", IsOneElmt([1, 2, 3 ,4 ,5]))

# REALISASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
def FirstElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[0]

# LastElmt: List tidak kosong -> elemen
def LastElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[-1]

# Tail: List tidak kosong -> boolean
def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

# Head: List tidak kosong -> List
def Head(L):
    if IsEmpty(L):
        return None
    else: 
        return L[:-1]

# print("\nHasil FirstElmt:", FirstElmt([]))
# print("Hasil FirstElmt:", FirstElmt([1,2,3,4,5]))
# print("Hasil LastElmt:", LastElmt([]))
# print("Hasil LastElmt:", LastElmt([1,2,3,4,5]))

# print("\nHasil Tail:", Tail([0]))
# print("Hasil Tail:", Tail([1,2,3,4,5]))
# print("Hasil Head:", Head([0]))
# print("Hasil Head:", Head([1,2,3,4,5]))

# REALISASI OPERATOR
# NbElmt: List -> integer
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else: 
        return 1 + NbElmt(Tail(L))

# print("\nHasil NbElmt:", NbElmt([]))
# print("Hasil NbElmt:", NbElmt([0]))
# print("Hasil NbElmt:", NbElmt([1, 1, 1, 1, 1]))
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

# print(IsPalindrom(['K', 'A', 'T', 'A', 'K']))

