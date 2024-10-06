# Tipe bentukan
# _DEFINISI DAN SPESIFIKASI_
# _type_ MHS: <NIM: _string_, Nama: _string_, Matkul: NMatkul>
#       {MHS adalah tipe bentukan yang mencakup input berupa NIM, Nama, dan Nilai Matkul}
# _type_ NMatkul: <Daspro: _real_, Dasis: _real_, Matematika1: _real_>
#       {NMatkul adalah tipe bentukan yang didalamnya berupa nilai matkul dari Daspro, Dasis, dan Matematika1}
# _type_ Hasil: 
#       {Hasil adalah tipe bentukan yang merupakan output terakhir yang diinginkan yang berupa Nama, NilaiTertinggi, NilaiTerendah, dan Rangenilai}
#
# _DEFINISI DAN SPESIFIKASI KONSTRUKTOR_
# MakeMHS: 2 _string_, NMatkul --> MHS
# MakeNMatkul: 3 _real_ --> NMatkul
# MakeHasil: 1 _string_, 3 _real_ --> Hasil
#
# _DEFINISI DAN SPESIFIKASI SELEKTOR_
# getNama: MHS --> _string_
# getDaspro: NMatkul --> _real_
# getDasis: NMatkul --> _real_
# getMatematika: NMatkul --> _real_
#
# _DEFINISI DAN SPESIFIKASI OPERATOR_
# Max2: 2 _real_ --> _real_
# Min2: 2 _real_ --> _real_
# Max3: 3 _real_ --> _real_
# Min3: 3 _real_ --> _real_
# hitungRangeNilai: MHS --> _real_
# nilaitertinggi: MHS --> _real_
# nilaiterendah: MHS --> _real_
#
# _REALISASI_
# max2(a,b): (a + b + _abs_(a-b)) _div_ 2
# min2(a,b): (a + b - _abs_(a-b)) _div_ 2
# max3(a,b,c): max2(max2(a,b),c)
# min3(a,b,c): min2(min2(a,b),c)
# hitungRangeNilai(nilai):
#      max3(getDaspro(nilai), getDasis(nilai), getMatematika(nilai)) - min3(getDaspro(nilai), getDasis(nilai), getMatematika(nilai))
# nilaitertinggi(x):
#      max3(getDaspro(x), getDasis(x), getMatematika(x))
# nilaiterendah(x):
#      min3(getDaspro(x), getDasis(x), getMatematika(x))
#
# _APLIKASI_
# MakeHasil(getNama(MakeMHS('20010', "Dhimas", MakeNMatkul(100,99,98))),nilaitertinggi(MakeNMatkul(100,99,98)),nilaiterterendah(MakeNMatkul(100,99,98)),hitungRangeNilai(MakeNMatkul(100,99,98)))) --> ['Dhimas', 100, 98, 2]
# MakeHasil(getNama(MakeMHS('20069', "Rawr", MakeNMatkul(70,80,90))),nilaitertinggi(MakeNMatkul(70,80,90)),nilaiterterendah(MakeNMatkul(70,80,90)),hitungRangeNilai(MakeNMatkul(70,80,90)))) --> ['Rawr', 90, 70, 20]   
# MakeHasil(getNama(MakeMHS('20042', "Indominus", MakeNMatkul(75,80,85))),nilaitertinggi(MakeNMatkul(75,80,85)),nilaiterterendah(MakeNMatkul(75,80,85)),hitungRangeNilai(MakeNMatkul(75,80,85)))) --> ['Indominus', 85, 75, 10]

# Konstuktor
def MakeMHS(NIM, Nama, Matkul):
    return [NIM, Nama, Matkul]

def MakeNMatkul(Daspro,Dasis,Matematika1):
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

def getMatkul(x):
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
print(MakeHasil(getNama(MakeMHS('20042', "Indominus", MakeNMatkul(75,80,85))),nilaitertinggi(getMatkul(MakeMHS('20042', "Indominus", MakeNMatkul(75,80,85)))),nilaiterterendah(getMatkul(MakeMHS('20042', "Indominus", MakeNMatkul(75,80,85)))),hitungRangeNilai(getMatkul(MakeMHS('20042', "Indominus", MakeNMatkul(75,80,85))))))
print(MakeHasil(getNama(MakeMHS('20069', "Rawr", MakeNMatkul(70,80,90))),nilaitertinggi(getMatkul(MakeMHS('20069', "Rawr", MakeNMatkul(70,80,90)))),nilaiterterendah(getMatkul(MakeMHS('20069', "Rawr", MakeNMatkul(70,80,90)))),hitungRangeNilai(getMatkul(MakeMHS('20069', "Rawr", MakeNMatkul(70,80,90))))))
print(MakeHasil(getNama(MakeMHS('20010', "Dhimno", MakeNMatkul(100,99,98))),nilaitertinggi(getMatkul(MakeMHS('20010', "Dhimno", MakeNMatkul(100,99,98)))),nilaiterterendah(getMatkul(MakeMHS('20010', "Dhimno", MakeNMatkul(100,99,98)))),hitungRangeNilai(getMatkul(MakeMHS('20010', "Dhimno", MakeNMatkul(100,99,98))))))