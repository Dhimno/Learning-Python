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

def getNilai(x):
    return 

# Operator
def hitungRangeNilai(nilai):
    return max(nilai[0],nilai[1],nilai[2]) - min(nilai[0],nilai[1],nilai[2])

print(MakeHasil(getNama(MHS('20010', "Dhimas", NMatkul(100,99,98))),1,1,hitungRangeNilai(NMatkul(100,99,98))))