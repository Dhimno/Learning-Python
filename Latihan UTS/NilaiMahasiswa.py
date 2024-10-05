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
def hitungRangeNilai(nilai):
    return max(nilai[0],nilai[1],nilai[2]) - min(nilai[0],nilai[1],nilai[2])

def nilaitertinggi(x):
    return max(getDaspro(x), getDasis(x), getMatematika(x))

def nilaiterterendah(x):
    return min(getDaspro(x), getDasis(x), getMatematika(x))

# Aplikasi
print(MakeHasil(getNama(MHS('20010', "Dhimas", NMatkul(100,99,98))),nilaitertinggi(NMatkul(100,99,98)),nilaiterterendah(NMatkul(100,99,98)),hitungRangeNilai(NMatkul(100,99,98))))