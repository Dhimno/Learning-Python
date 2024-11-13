# Program   : LOL.py
# Deskripsi : Fungsi-fungsi untuk operasi list
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 30/10/2024

from listFunction import *

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
print('\nIni adalah IsMemberS', IsMemberS(9,[4,5,6,[8,9,10],[12,0],8]),'\n')

# Kurang Rember

def Max(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return max2(max(FirstList(S)),Max(TailList(S)))
        else:
            return max2(FirstList(S),Max(TailList(S)))
print('Ini adalah fungsi Max', Max([4,5,6,[8,9,10],[12,0],8]),'\n')


def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return NBElmtAtom(TailList(S))
    else:
        return 1 + NBElmtAtom(TailList(S))
print('Ini adalah NB Element', NBElmtAtom([4,5,6,[8,9,10],[12,0],8]),'\n')

def NBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return NBElmtList(TailList(S))
    else:
        return 1 + NBElmtList(TailList(S))
print('Ini adalah NB List', NBElmtList([4,5,6,[8,9,10],[12,0],8]),'\n')

def SumLoL(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return SumElmt(FirstList(S)) + SumLoL(TailList(S))
    else:
        return FirstList(S) + SumLoL(TailList(S))
    
print('Ini adalah SumLOL', SumLoL([4,5,6,[2,3,1]]),'\n')

def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return max2(NbElmt(FirstList(S)),MaxNBElmtList(TailList(S)))
    else:
        return MaxNBElmtList(TailList(S))
    
print('Ini adalah MaxNBElmtList', MaxNBElmtList([4,5,6,[2,3,1]]),'\n')
print('Ini adalah MaxNBElmtList', MaxNBElmtList([4,5,6,[2,3,1],[2,3,1,4]]),'\n')

def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return max2(SumElmt(FirstList(S)),MaxSumElmt(TailList(S)))
        else:
            return max2(FirstList(S),MaxSumElmt(TailList(S)))
        
print('Ini adalah MaxSumElmt', MaxSumElmt([4,5,9,[2,3,1],[2,3,1,4]]),'\n')


