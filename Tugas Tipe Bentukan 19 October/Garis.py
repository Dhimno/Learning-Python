# Tipe Bentukan
# _type_ Point: <x:_real_, y:_real_>
#       {<x,y> adalah point dengan x adalah absis dan y adalah ordinat}
# _type_ Garis: <titik1: Point, titik2: Point>
#       {<titik1,titik2> adalah titik yang membentuk garis dimana titik 1 adalah titik pangkal dan titik 2 adalah titik ujung}
# _DEFINISI DAN SPESIFIKASI KONSTRUKTOR_
# makePoint: 2 _real_ --> Point
#       {makePoint(x,y) adalah fungsi untuk membuat point dengan 2 inputan real (x,y)}
# makeGaris: 2 Point --> Garis
#       {makeGaris(titik1,titik2) adalah fungsi untuk membuat sebuah garis dengan 2 inputan berupa 2 Point}
# _DEFINISI DAN SPESIFIKASI SELEKTOR_
# getAbsis: Point --> _real_
#       {getAbsis(x): mengambil nilai absis dalam sebuah point}
# getOrdinat: Point --> _real_
#       {getOrdinat(y): mengambil nilai ordinat dalam sebuah point}
# getTitikPangkal: Garis --> Point
#       {getTitikPangkal(x): mengambil nilai titik pangkal dalam sebuah garis}
# getTitikUjung: Garis --> Point
#       {getTitikUjung(x): mengambil nilai titik ujung dalam sebuah garis}
# _DEFINISI DAN SPESIFIKASI OPERATOR_
# panjangGaris: Garis --> _real_
#       {panjangGaris(x): menghitung panjang Garis dimana 2 nilai Point dimasukkan kedalam rumus yang sudah ditentukan}
# IsKuadran3?: Garis --> _boolean_
#       {IsKuadran3?(x): mengecek apakah titik ujung dan titik pangkal dari sebuah garis dalam kuadran 3, output true jika kedua titik berada pada kuadran 3, false jika sebaliknya}
# _DEFINISI DAN SPESIFIKASI FUNGSI ANTARA_
# FX2: _real_ --> _real_
#       {FX2(x): mengkuadratkan input dengan rumus x*x}
# _REALISASI_
# FX2(x): 
#   x * x
# panjangGaris(x): 
#   (FX2(getAbsis(getTitikPangkal(x)) - getAbsis(getTitikUjung(x))) + FX2(getOrdinat(getTitikPangkal(x)) - getOrdinat(getTitikUjung(x))))**0.5
# IsKuadran3?(X):
#   _if_ getAbsis(getTitikPangkal(x)) < 0 _and_ getOrdinat(getTitikPangkal(x)) < 0 _and_ getAbsis(getTitikUjung(x)) < 0 and getOrdinat(getTitikUjung(x)) < 0 _then_
#       _true_
#   _else_
#       _false_
# _APLIKASI_
# panjangGaris(makeGaris(makePoint(0,0), makePoint(0,8))) --> 8.0
# panjangGaris(makeGaris(makePoint(0,0), makePoint(0,9))) --> 9.0
# panjangGaris(makeGaris(makePoint(0,0), makePoint(0,10))) --> 10.0
# IsKuadran3(makeGaris(makePoint(-2,-8), makePoint(-7,-9))) --> _true_
# IsKuadran3(makeGaris(makePoint(2,-8), makePoint(-7,-9))) --> _false_
# IsKuadran3(makeGaris(makePoint(-2,-8), makePoint(7,-9))) --> _false_



# Konstruktor
def makePoint(x,y):
    return [x,y]

def makeGaris(titik1, titik2):
    return [titik1, titik2]

# Selektor
def getAbsis(x):
    return x[0]

def getOrdinat(y):
    return y[1]

def getTitikPangkal(x):
    return x[0]

def getTitikUjung(x):
    return x[1]

# Operator
def panjangGaris(x):
    return ((getAbsis(getTitikPangkal(x)) - getAbsis(getTitikUjung(x)))**2 + (getOrdinat(getTitikPangkal(x)) - getOrdinat(getTitikUjung(x)))**2)**0.5

def IsKuadran3(x):
    if getAbsis(getTitikPangkal(x)) < 0 and getOrdinat(getTitikPangkal(x)) < 0 and getAbsis(getTitikUjung(x)) < 0 and getOrdinat(getTitikUjung(x)) < 0:
        return True
    else:
        return False


print(panjangGaris(makeGaris(makePoint(0,0), makePoint(0,8))))
print(IsKuadran3(makeGaris(makePoint(-2,-8), makePoint(-7,-9))))
