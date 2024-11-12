# Program   : set_24060124120010.py
# Deskripsi : Program yang berisi implementasi operasi-operasi himpunan
# NIM/Nama  : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal   : 6/11/2024
# ============================================================================================================================================
# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah tipe bentukan yang berisi kumpulan elemen yang unik dan tidak terurut

from listFunction import * # list bisa diganti dengan file yang berisi operasi-operasi list

# Rember: elemen, list -> list
# Rember(x, L) menghapus sebuah elemen x dari list L.
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.
def Rember(x,L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L),Rember(x,Tail(L)))

# MultiRember: elemen, list -> list
# MultiRember(x, L) menghapus semua kemunculan elemen x dari list L.
# List baru yang dihasilkan tidak lagi memiliki elemen x.
# List kosong tetap menjadi list kosong.
def MultiRember(x,L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return Konso(FirstElmt(L),MultiRember(x,Tail(L)))

# MakeSet: list -> set
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali.
# List kosong tetap menjadi himpunan kosong.
def MakeSet1(L): # Rekursif terhadap H1
    if IsEmpty(L):
        return L
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet1(Tail(L))
        else:
            return Konso(FirstElmt(L),MakeSet1(Tail(L)))

def MakeSet2(L): # Rekursif terhadap H2
    if IsEmpty(L):
        return L
    else:
        return Konso(FirstElmt(L),MakeSet2(MultiRember(FirstElmt(L),Tail(L))))

# KonsoSet: elemen, set -> set
# KonsoSet(e, H) menambahkan sebuah elemen e sebagai elemen pertama set H
# dengan syarat e belum ada di dalam himpunan H.
def KonsoSet(e, H):
    if IsEmpty(H):
        return Konso(e, H)
    elif IsMember(e, H):
        return H
    else:
        return Konso(e,H)

# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set.
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet(Tail(L))

# IsSubset: 2 set -> boolean
# IsSubset(H1, H2) mengembalikan true jika H1 merupakan subset dari H2.
def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1),H2):
            return IsSubset(Tail(H1),H2)
        else:
            return False

# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1, H2) benar jika H1 adalah set yang sama dengan H2.
def IsEqualSet(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)


def IsIntersect(H1,H2): 
    if IsEmpty(H1) or IsEmpty(H2):
        return False
    elif IsEmpty(H1) == False and IsEmpty(H2) == False:
        if IsMember(FirstElmt(H1),H2):
            return True
        else:
            return IsIntersect(Tail(H1),H2)

# MakeIntersect: 2 set -> set
# MakeIntersect(H1, H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2.
def MakeIntersect1(H1,H2): # Rekursif terhadap H1
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1), MakeIntersect1(Tail(H1),H2))
        else:
            return MakeIntersect1(Tail(H1),H2)

def MakeIntersect2(H1, H2): # Rekursif terhadap H2
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2), H1):
            return Konso(FirstElmt(H2), MakeIntersect2(H1, Tail(H2)))
        else:
            return MakeIntersect2(H1, Tail(H2))

# MakeUnion: 2 set -> set
# MakeUnion(H1, H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2.
def MakeUnion1(H1,H2): # Rekursif terhadap H1
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

def MakeUnion2(H1, H2): # Rekursif terhadap H2
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

# NBIntersect: 2 set -> integer
# NBIntersect(H1, H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
def NBIntersect(H1, H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return 0
    else:
        if IsMember(FirstElmt(H1), H2):
            return 1 + NBIntersect(Tail(H1), H2)
        else:
            return NBIntersect(Tail(H1), H2)

# NBUnion: 2 set -> integer
# NBUnion(H1, H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
def NBUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return 0
    elif IsEmpty(H1):
        return 1 + NBUnion(H1, Tail(H2))
    elif IsEmpty(H2):
        return 1 + NBUnion(Tail(H1), H2)
    else:
        if IsMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1 + NBUnion(Tail(H1), H2)

# ============================================================================================================================================
# APLIKASI
# ============================================================================================================================================
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