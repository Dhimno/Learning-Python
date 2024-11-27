# Program   : BST_24060124120010.py
# Deskripsi : Implementasi binary search tree dengan representasi list of list
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 27/11/2024
# ============================================================================================================================================

from listFunction import *
from treeNaire_24060124120010 import *

# isEmpty(L): List of List --> boolean
# isEmpty(L) mengecek apakah List of List kosong
def IsEmpty(L):
    return L == []

# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A,L,R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
def MakePB(A,L,R):
    return [A,L,R]

# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
def Akar(P):
    return P[0]

# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
def Left(P):
    return P[1]

# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
def Right(P):
    return P[2]

# procedure PrintBinaryTreeHelp(input T: PohonBiner, input indent: character)
# Prosedur rekursif untuk PrintBinaryTree.
def PrintBinaryTreeHelp(T, indent):
    if T != []:
        print(indent + str(Akar(T)))
        PrintBinaryTreeHelp(Left(T), indent + '   ')   # Spasinya tiga.
        PrintBinaryTreeHelp(Right(T), indent + '   ')  # Yang ini juga.
    else:
        print(indent + "[]")

# procedure PrintBinaryTree(input T: PohonBiner)
# Mencetak PohonBiner dengan format indentasi.
def PrintBinaryTree(T):
    PrintBinaryTreeHelp(T, '')  # Yang di dalam petik kosong.

# AddX: BinSearchTree, integer --> BinSearchTree
# AddX(P, X) mengembalikan BinSearchTree P dengan tambahan simpul X.
# X adalah elemen baru yang belum ada di BinSearchTree P sebelumnya.
def AddX(P, X):
    if IsEmpty(P):
        return MakePB(X, [], [])
    else:
        if X >= Akar(P):
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))
        else:
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))
        
# DelBTree: BinSearchTree, integer --> BinSearchTree
# DelBTree(P, X) mengembalikan BinSearchTree P tanpa simpul yang bernilai X.
# X adalah elemen yang sudah ada di BinSearchTree sebelum dihapus.
def DelBTree(P, X):
    if IsEmpty(P):
        return []
    else:
        if Akar(P) == X:
            if IsEmpty(Left(P)) and IsEmpty(Right(P)):
                return []
            else:
                if IsEmpty(Left(P)):
                    return MakePB(Akar(Right(P)), Left(P), Right(P))
                else:
                    return MakePB(Akar(Left(P)), Left(P), Right(P))
        elif X >= Akar(P):
            return MakePB(Akar(P), Left(P), DelBTree(Right(P), X))
        else:
            return MakePB(Akar(P), DelBTree(Left(P), X), Right(P))
        
# Khusus kali ini saja diperbolehkan menyimpan variabel
T = AddX(AddX(AddX(AddX(AddX([],50),75),200),100),120)
PrintBinaryTree(T)
T = DelBTree(T,50)
PrintBinaryTree(T)

