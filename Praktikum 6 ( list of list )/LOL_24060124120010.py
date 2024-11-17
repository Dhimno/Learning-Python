# Program   : LOL_24060124120010.py
# Deskripsi : Fungsi-fungsi untuk operasi list of list
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 17/11/2024

from listFunction import *
from set_24060124120010 import Rember1

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
    elif IsList(FirstList(S)):
        return KonsLo(Rember(x,FirstList(S)),Rember(x,TailList(S)))
    else:
        if FirstElmt(S) == x:
            return Rember1(x,TailList(S))
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
        
# ========================================================================================
# APLIKASI TEST
# ========================================================================================
print("\nIni adalah hasil dari fungsi KonsLo", KonsLo([1, 2, 3], [4, 5, 6]), "\n")  # [[1, 2, 3], 4, 5, 6]
print("Ini adalah hasil dari fungsi KonsLi", KonsLi([1, 2, 3], [4, 5, 6]), "\n")  # [1, 2, 3, [4, 5, 6]]
print("Ini adalah hasil dari fungsi FirstList", FirstList([[1, 2, 3], 4, 5, 6]), "\n")  # [1, 2, 3]
print("Ini adalah hasil dari fungsi LastList", LastList([[1, 2, 3], 4, 5, 6]), "\n")  # 6
print("Ini adalah hasil dari fungsi TailList", TailList([[1, 2, 3], 4, 5, 6]), "\n")  # [4, 5, 6]
print("Ini adalah hasil dari fungsi HeadList", HeadList([[1, 2, 3], 4, 5, 6]), "\n")  # [[1, 2, 3], 4, 5]
print("Ini adalah hasil dari fungsi IsEmpty", IsEmpty([]), "\n")  # True
print("Ini adalah hasil dari fungsi IsEmpty", IsEmpty([[]]), "\n")  # False
print("Ini adalah hasil dari fungsi IsAtom", IsAtom(1), "\n")  # True
print("Ini adalah hasil dari fungsi IsAtom", IsAtom([1, 2, 3]), "\n")  # False
print("Ini adalah hasil dari fungsi IsList", IsList([1, 2, 3]), "\n")  # True
print("Ini adalah hasil dari fungsi IsList", IsList(1), "\n")  # False
print("================================================")
# ========================================================================================
# APLIKASI TUGAS
# ========================================================================================
print('\nIni adalah hasil dari IsMemberS', IsMemberS(9,[4,5,6,[8,9,10],[12,0],8]),'\n') # True
print('Ini adalah hasil dari Rember', Rember(9,[4,5,6,9,[8,9,10],[12,0],8]),'\n') # [4, 5, 6, [8, 9, 10], [12, 0], 8]
print('Ini adalah hasil dari fungsi Max', Max([4,5,6,[8,9,10],[12,0],8]),'\n') # 12
print('Ini adalah hasil dari NB Element', NBElmtAtom([4,5,6,[8,9,10],[12,0],8]),'\n') # 4
print('Ini adalah hasil dari NB List', NBElmtList([4,5,6,[8,9,10],[12,0],8]),'\n') # 2
print('Ini adalah hasil dari SumLOL', SumLoL([4,5,6,[2,3,1]]),'\n') # 21
print('Ini adalah hasil dari MaxNBElmtList', MaxNBElmtList([4,5,6,[2,3,1]]),'\n') # 3
print('Ini adalah hasil dari MaxNBElmtList', MaxNBElmtList([4,5,6,[2,3,1],[2,3,1,4]]),'\n') # 4
print('Ini adalah hasil dari MaxSumElmt', MaxSumElmt([4,5,9,[2,3,1],[2,3,1,4]]),'\n') # 10
