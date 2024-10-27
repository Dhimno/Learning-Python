# Program     : Garis.py
# Deskripsi   : Membuat tipe bentukan garis dan mengoperasikannya ke operator dan predikat yang ditentukan
# NIM/Nama    : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal     : (28/10/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# TYPE GARIS
# type Point: <x:real, y:real>
#       {<x,y> adalah titik x (absis) dan titik y (ordinat)}
# type Garis: <titik1: Point, titik2: Point>
#       {<titik1,titik2> adalah garis dimana titik1 adalah titik pangkal dan titik2 adalah titik ujung}
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makePoint: <x:real, y:real> --> Point
#       {makePoint(x,y) adalah sebuah konstruktor untuk mengubah x (absis) dan y (ordinat) menjadi sebuah titik (point)}
# makeGaris: 2 Point --> Garis
#       {makeGaris(titik1,titik2) adalah sebuah konstruktor untuk mengubah 2 point (menghubungkan) menjadi sebuah garis}
# DEFINISI DAN SPESIFIKASI SELEKTOR
# getAbsis: Point --> real
#       {getAbsis(x): sebuah selektor untuk mengambil nilai absis dari point}
# getOrdinat: Point --> real
#       {getOrdinat(y): sebuah selektor untuk mengambil nilai ordinat dari point}
# getTitikPangkal: Garis --> Point
#       {getTitikPangkal(x): sebuah selektor untuk mengambil nilai point (titik ujung) dari garis}
# getTitikUjung: Garis --> Point
#       {getTitikUjung(x): sebuah selektor untuk mengambil nilai point (titik pangkal) dari garis}
# DEFINISI DAN SPESIFIKASI OPERATOR
# panjangGaris: Garis --> real
#       {panjangGaris(G): adalah operator untuk menghitung panjang garis}
# Gradien: Garis --> real
#       {Gradien(G): adalah operator untuk menghitung gradien dari sebuah garis}
# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSejajar?: 2 Garis --> real
#       {IsSejajar?(G1,G2): adalah predikat untuk mengecek apakah garis 1 dan 2 sejajar (memiliki nilai gradien yang sama)}
# IsTegakLurus?: 2 Garis --> real
#       {IsSejajar?(G1,G2): adalah predikat untuk mengecek apakah garis 1 dan 2 tegak lurus (gradien garis1 * gradien garis2 = -1)}
# ===========================================================================
# REALISASI
# ===========================================================================
def makePoint(x,y):
    return [x,y]

def makeGaris(titik1, titik2):
    return [titik1, titik2]

def getAbsis(x):
    return x[0]

def getOrdinat(y):
    return y[1]

def getTitikPangkal(x):
    return x[0]

def getTitikUjung(x):
    return x[1]

def panjangGaris(G):
    return ((getAbsis(getTitikPangkal(G)) - getAbsis(getTitikUjung(G)))**2 + (getOrdinat(getTitikPangkal(G)) - getOrdinat(getTitikUjung(G)))**2)**0.5

def Gradien(G):
    return (getOrdinat(getTitikUjung(G)) - getOrdinat(getTitikPangkal(G))) / (getAbsis(getTitikUjung(G)) - getAbsis(getTitikPangkal(G)))

def IsSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus(G1,G2):
    return Gradien(G1) * Gradien(G2) == -1

# ===========================================================================
# APLIKASI
print(panjangGaris(makeGaris(makePoint(0,0), makePoint(0,8))))
print(Gradien(makeGaris(makePoint(0,0), makePoint(4,8))))
print(IsSejajar(makeGaris(makePoint(0,0), makePoint(4,8)), makeGaris(makePoint(2,4), makePoint(4,8))))
print(IsTegakLurus(makeGaris(makePoint(0,0), makePoint(1,1)), makeGaris(makePoint(1,-1), makePoint(0,0))))