# Program   : set_24060124120010.py
# Deskripsi : Program yang berisi implementasi operasi-operasi himpunan
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 6/11/2024

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah tipe bentukan yang berisi kumpulan elemen yang unik dan tidak terurut

from listFunction import * # list bisa diganti dengan file yang berisi operasi-operasi list

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x, L) menghapus sebuah elemen x dari list L
#   Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.
def IsSet2(L):
    return IsEmpty(L) or (not IsMember(FirstElmt(L), Tail(L))) and IsSet2(Tail(L))


def IsSet1(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet1(Tail(L))

def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1),H2):
            return IsSubset(Tail(H1),H2)
        else:
            return False

def MultiRember(x,L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return Konso(FirstElmt(L),MultiRember(x,Tail(L)))

def MakeSet(L):
    if IsEmpty(L):
        return L
    else:
        return Konso(FirstElmt(L),MakeSet(MultiRember(FirstElmt(L),Tail(L))))

def MakeSetIsMember(L):
    if IsEmpty(L):
        return L
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSetIsMember(Tail(L))
        else:
            return Konso(FirstElmt(L),MakeSetIsMember(Tail(L)))

def IsIntersect(H1,H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return False
    elif IsEmpty(H1) == False and IsEmpty(H2) == False:
        if IsMember(FirstElmt(H1),H2):
            return True
        else:
            return IsIntersect(Tail(H1),H2)

def KonsoSet(e, H):
    if IsEmpty(H):
        return Konso(e, H)
    else:
        if IsMember(e, H):
            return H
        else:
            return Konso(e,H)

print(IsSet1([1,2,3,4,5]))
print(IsSet1([1,1,3,4,5]))
print(IsSubset([1,2,3,4],[1,2,3,4,5]))
print(IsSubset([1,2,3,6],[1,2,3,4,5]))
print(MultiRember(2,[2,2,2,3]))
print(IsIntersect([1,2,3,4,5], [10,9,8,7,6,5]))
print(IsIntersect([1,2,3,4,5], [10,9,8,7,6]))
print(MakeSetIsMember([1,1,1,1,2]))
print(MakeSet([1,1,1,1,2]))
print(KonsoSet(1,[1,2,3,4,5]))
print(KonsoSet(6,[1,2,3,4,5]))