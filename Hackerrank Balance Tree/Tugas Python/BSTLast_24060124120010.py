# Program   : BSTLast_24060124120010.py
# Deskripsi : Program yang berisi implementasi binary search tree dalam python
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 3/12/2024
# ============================================================================================================================================

from BST_24060124120010 import *
from listFunction import *

# KONSTRUKTOR TREE DENGAN FORMAT PREFIX
def MakePB(A, L, R):
    return [A, L, R]

# PREDIKAT
# MakeBinSearchTree: integer, BST --> boolean
# BSearchX(x,P) adalah sebuah predikat untuk mengecek apakah integer dari parameter x ada dalam sebuah pohon
def BSearchX(x, P):
    if isTreeNEmpty(P):
        return False
    else:
        if Akar(P) == x:
            return True
        else:
            return BSearchX(x,Left(P)) or BSearchX(x,Right(P))

# SORTER
# Berfungsi untuk mengesort data dari list yang tidak urut
def FilterKurangDari(x, L):
    if IsEmpty(L):
        return []
    elif FirstElmt(L) < x:
        return Konso(FirstElmt(L), FilterKurangDari(x, Tail(L)))
    else:
        return FilterKurangDari(x, Tail(L))

def FilterLebihDari(x, L):
    if IsEmpty(L):
        return []
    elif FirstElmt(L) >= x:
        return Konso(FirstElmt(L), FilterLebihDari(x, Tail(L)))
    else:
        return FilterLebihDari(x, Tail(L))

def Konso(e, L):
    return [e] + L

def AddList(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1), AddList(Tail(L1), L2))

def sortList(L):
    if IsEmpty(L):  
        return []
    else:
        return AddList(sortList(FilterKurangDari(FirstElmt(L), Tail(L))), Konso(FirstElmt(L), sortList(FilterLebihDari(FirstElmt(L), Tail(L)))))  

# KONSTRUKTOR BINARY SEARCH TREE
# MakeBinSearchTree: List --> BST
# MakeBinSearchTree(List) adalah sebuah konstruktor untuk mengubah sebuah list menjadi Binary Search Tree
def MakeBinSearchTree(List):
    if NbElmt(sortList(List)) == 0:
        return []
    else:
        return MakePB(
            sortList(List)[NbElmt(sortList(List)) // 2],
            MakeBinSearchTree(sortList(List)[:NbElmt(sortList(List)) // 2]),
            MakeBinSearchTree(sortList(List)[(NbElmt(sortList(List)) // 2) + 1:])
        )

# ============================================================================================================================================
# APLIKASI
print(MakeBinSearchTree([3,2,1,4,5,6,7]))
print(BSearchX(50,AddX(AddX(AddX(AddX(AddX([],50),75),200),100),120)))