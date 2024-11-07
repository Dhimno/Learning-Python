# Program   : set_24060124120010.py
# Deskripsi : Program yang berisi implementasi operasi-operasi himpunan
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 6/11/2024

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah tipe bentukan yang berisi kumpulan elemen yang unik dan tidak terurut

from listFunction import * # list bisa diganti dengan file yang berisi operasi-operasi list

def Rember1(x,L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L),Rember1(x,Tail(L)))

# Kurang Rember1

def MultiRember(x,L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return Konso(FirstElmt(L),MultiRember(x,Tail(L)))

def MakeSet1(L):
    if IsEmpty(L):
        return L
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet1(Tail(L))
        else:
            return Konso(FirstElmt(L),MakeSet1(Tail(L)))

def MakeSet2(L):
    if IsEmpty(L):
        return L
    else:
        return Konso(FirstElmt(L),MakeSet2(MultiRember(FirstElmt(L),Tail(L))))

def KonsoSet(e, H):
    if IsEmpty(H):
        return Konso(e, H)
    elif IsMember(e, H):
        return H
    else:
        return Konso(e,H)

def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet(Tail(L))

def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1),H2):
            return IsSubset(Tail(H1),H2)
        else:
            return False

def IsEQSet(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)

def IsIntersect(H1,H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return False
    elif IsEmpty(H1) == False and IsEmpty(H2) == False:
        if IsMember(FirstElmt(H1),H2):
            return True
        else:
            return IsIntersect(Tail(H1),H2)

def MakeIntersect1(H1,H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1), MakeIntersect1(Tail(H1),H2))
        else:
            return MakeIntersect1(Tail(H1),H2)

def MakeIntersect2(H1, H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2), H1):
            return Konso(FirstElmt(H2), MakeIntersect2(H1, Tail(H2)))
        else:
            return MakeIntersect2(H1, Tail(H2))

def MakeUnion1(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    elif IsEmpty(H1) and not IsEmpty(H2):
        return H2
    else:
        if IsMember(FirstElmt(H1),H2):
            return MakeUnion1(Tail(H1),H2)
        else:
            return Konso(FirstElmt(H1),MakeUnion1(Tail(H1),H2))

def MakeUnion2(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1):
        return H2
    elif IsEmpty(H2):
        return H1
    else:
        if IsMember(FirstElmt(H2), H1):
            return MakeUnion2(H1, Tail(H2)) 
        else:
            return Konso(FirstElmt(H2), MakeUnion2(H1, Tail(H2)))

# Kurang NBintersect dan NBunion



print(IsSet([1,2,3,4,5]))
print(IsSet([1,1,3,4,5]))
print(IsSubset([1,2,3,4],[1,2,3,4,5]))
print(IsSubset([1,2,3,6],[1,2,3,4,5]))
print(MultiRember(2,[2,2,2,3]))
print(IsIntersect([1,2,3,4,5], [10,9,8,7,6,5]))
print(IsIntersect([1,2,3,4,5], [10,9,8,7,6]))
print(MakeSet1([1,1,1,1,2]))
print(MakeSet2([1,1,1,1,2]))
print(KonsoSet(1,[1,2,3,4,5]))
print(KonsoSet(6,[1,2,3,4,5]))