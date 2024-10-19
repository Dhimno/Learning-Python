# Program     : PecahanCampuran.py
# Deskripsi   : Membuat pecahan campuran menggunakan tipe bentukan dan mengoperasikannya dengan operator yang ditentukan serta pengecekkan melalui predikat yang telah ditentukan
# NIM/Nama    : 24060124120010/Dhimas Reza Nafi Wahyudi
# Tanggal     : (19/10/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# type PecahanCampuran : <bil: integer, n:integer >= 0, d:integer > 0>
#   {<bil: integer, n:integer >= 0, d:integer > 0> adalah elemen dari pecahan campuran dimana bil adalah bilangan bulat disamping pecahan, n adalah pembilang dari pecahan, dan d adalah penyebut dari pecahan}
# type PecahanBiasa: <n:integer >= 0, d:integer > 0>
#   {<n:integer >= 0, d:integer > 0> adalah elemen dari pecahan biasa dimana n adalah sebuah pembilang dan d adalah penyebut}
# makePecahanC: <bil: integer, n:integer >= 0, d:integer > 0> -> PecahanCampuran
#   {makePecahanC(bil,n,d) adalah sebuah konstruktor untuk mengkonversi bil, n, d menjadi tipe bentukan pecahan campuran}
# makePecahanBiasa: <n:integer >= 0, d:integer > 0> -> PecahanBiasa
#   {makePecahanBiasa(n,d) adalah sebuah konstruktor untuk mengkonversi n, d menjadi tipe bentukan pecahan biasa}
# getBil: PecahanCampuran -> integer
#   {getBil(x) adalah selektor untuk mengambil data bilangan dari tipe bentukan pecahan campuran}
# getN: PecahanCampuran -> integer
#   {getN(x) adalah selektor untuk mengambil data pembilang dari tipe bentukan pecahan campuran}
# getD: PecahanCampuran -> integer
#   {getD(x) adalah selektor untuk mengambil data penyebut dari tipe bentukan pecahan campuran}
# getPembilang: PecahanBiasa -> integer
#   {getPembilang(x) adalah selektor untuk mengambil data penyebut dari tipe bentukan pecahan biasa}
# getPenyebut: PecahanBiasa -> integer
#   {getPenyebut(x) adalah selektor untuk mengambil data penyebut dari tipe bentukan pecahan biasa}
# KonversiPecahan: PecahanCampuran -> PecahanBiasa
#   {KonversiPecahan(P) adalah sebuah operator untuk mengkonversi tipe bentukan pecahan campuran menjadi pecahan biasa}
# KonversiReal: PecahanCampuran -> real
#   {KonversiReal(P) adalah sebuah operator untuk mengkonversi tipe bentukan pecahan campuran menjadi real}
# AddP: 2 PecahanCampuran -> PecahanBiasa
#   {AddP(P1,P2) adalah sebuah operator untuk menambahkan 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# SubP: 2 PecahanCampuran -> PecahanBiasa
#   {SubP(P1,P2) adalah sebuah operator untuk mengurangi 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# DivP: 2 PecahanCampuran -> PecahanBiasa
#   {DivP(P1,P2) adalah sebuah operator untuk membagi 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# MulP: 2 PecahanCampuran -> PecahanBiasa
#   {MulP(P1,P2) adalah sebuah operator untuk mengali 2 PecahanCampuran dan mengoutputkan sebagai PecahanBiasa}
# IsEqP?: 2 PecahanCampuran -> boolean
#   {IsEqP?(P1,P2) adalah sebuah predikat untuk mengoutput true jika kedua pecahan bernilai sama dan false jika sebaliknya}
# IsLtP?: 2 PecahanCampuran -> boolean
#   {IsLtP?(P1,P2) adalah sebuah predikat untuk mengoutput true jika pecahan pertama bernilai lebih kecil daripada pecahan kedua}
# IsGtP?: 2 PecahanCampuran -> boolean
#   {IsGtP?(P1,P2) adalah sebuah predikat untuk mengoutput true jika pecahan pertama bernilai lebih besar daripada pecahan kedua}
# ===========================================================================
# REALISASI
# ===========================================================================
def makePecahanC(bil, n, d):
    return [bil,n,d]

def makePecahanBiasa(n,d):
    return [n,d]

def getBil(x):
    return x[0]

def getN(x):
    return x[1]

def getD(x):
    return x[2]

def getPembilang(x):
    return x[0]

def getPenyebut(x):
    return x[1]

def KonversiPecahan(P):
    if getD(P) > 0 and getBil(P) < 0 and getN(P) >= 0:
        return makePecahanBiasa((getD(P) * getBil(P) + getN(P) * (-1)), getD(P))
    else:
        return makePecahanBiasa(getD(P) * getBil(P) + getN(P), getD(P))

def KonversiReal(P):
    return getPembilang(KonversiPecahan(P)) / getPenyebut(KonversiPecahan(P))

def AddP(P1,P2):
    return makePecahanBiasa(getPembilang(KonversiPecahan(P1)) * getPenyebut(KonversiPecahan(P2)) + getPembilang(KonversiPecahan(P2)) * getPenyebut(KonversiPecahan(P1)), getPenyebut(KonversiPecahan(P1)) * getPenyebut(KonversiPecahan(P2)))

def SubP(P1,P2):
    return makePecahanBiasa(getPembilang(KonversiPecahan(P1)) * getPenyebut(KonversiPecahan(P2)) - getPembilang(KonversiPecahan(P2)) * getPenyebut(KonversiPecahan(P1)), getPenyebut(KonversiPecahan(P1)) * getPenyebut(KonversiPecahan(P2)))

def DivP(P1,P2):
    return makePecahanBiasa(getPembilang(KonversiPecahan(P1)) * getPenyebut(KonversiPecahan(P2)), getPembilang(KonversiPecahan(P2)) * getPenyebut(KonversiPecahan(P1)))

def MulP(P1,P2):
    return makePecahanBiasa(getPembilang(KonversiPecahan(P1)) * getPembilang(KonversiPecahan(P2)) , getPenyebut(KonversiPecahan(P2)) * getPenyebut(KonversiPecahan(P1)))

def IsEqP(P1,P2):
    return KonversiReal(P1) == KonversiReal(P2)

def IsLtP(P1,P2):
    return KonversiReal(P1) < KonversiReal(P2)

def IsGtP(P1,P2):
    return KonversiReal(P1) > KonversiReal(P2)

# ===========================================================================
# APLIKASI
print(IsEqP(makePecahanC(1,1,2), makePecahanC(1,1,2)))
print(IsLtP(makePecahanC(1,1,2), makePecahanC(2,1,2)))
print(IsGtP(makePecahanC(2,1,2), makePecahanC(1,1,2)))
print(MulP(makePecahanC(1,1,2), makePecahanC(1,1,2)))
print(DivP(makePecahanC(1,1,2), makePecahanC(1,1,2)))
print(SubP(makePecahanC(1,1,2), makePecahanC(1,1,2)))
print(AddP(makePecahanC(1,1,2), makePecahanC(1,1,2)))
print(KonversiReal(makePecahanC(1,1,2)))
print(KonversiPecahan(makePecahanC(1,1,2)))
print(KonversiPecahan(makePecahanC(-1,1,2)))