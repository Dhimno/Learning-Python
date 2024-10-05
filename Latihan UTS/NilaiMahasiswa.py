# Konstuktor
def MHS(NIM, Nama, Matkul):
    return [NIM, Nama, Matkul]

def NMatkul(Daspro,Dasis,Matematika1):
    return [Daspro,Dasis,Matematika1]

def MakeHasil(Nama, NilaiTertinggi, NilaiTerendah, RangeNilai):
    return [Nama, NilaiTertinggi, NilaiTerendah, RangeNilai]

# Selektor
def getNama(x):
    return x[1]

def getDaspro(x):
    return x[0]

def getDasis(x):
    return x[1]

def getMatematika(x):
    return x[2]

# Operator
def max2(a,b):
    return (a + b + abs(a-b)) // 2

def max3(a,b,c):
    return max2(max2(a,b),c)

def min2(a,b):
    return (a + b - abs(a-b)) // 2

def min3(a,b,c):
    return min2(min2(a,b),c)

def hitungRangeNilai(nilai):
    return max3(getDaspro(nilai), getDasis(nilai), getMatematika(nilai)) - min3(getDaspro(nilai), getDasis(nilai), getMatematika(nilai))

def nilaitertinggi(x):
    return max3(getDaspro(x), getDasis(x), getMatematika(x))

def nilaiterterendah(x):
    return min3(getDaspro(x), getDasis(x), getMatematika(x))

# Aplikasi
print(MakeHasil(getNama(MHS('20010', "Dhimas", NMatkul(100,99,98))),nilaitertinggi(NMatkul(100,99,98)),nilaiterterendah(NMatkul(100,99,98)),hitungRangeNilai(NMatkul(100,99,98))))