from listFunction import *


def makeNilai(nilai): # Untuk membuat set Nilai
    return nilai


def MakeMhs(nim, nama, kelas, nilai): # Untuk membuat tipe bentukan mahasiswa
    return [nim, nama, kelas, nilai]


def getNIM(L): # Selektor untuk mengambik NIM dari mahasiswa
    return L[0]

def getNama(L):
    return L[1]

def getKelas(L):
    return L[2]

def getNilai(L):
    return L[3]

def getFirstMhs(set): # Selektor untuk mengambil list mahasiswa pertama dari set mahasiswa
    return set[0]

def getLastMhs(set): # Selektor untuk mengambil list mahasiswa terakhir dari set mahasiswa
    return set[-1]

def MakeSetMhs(B, L): # Membuat set Mahasiswa dimana terdiri dari gabungan mahasiswa dengan NIM yang unik
    if IsEmpty(L):
        return Konso(B, L)
    elif getNIM(B) == getNIM(getFirstMhs(L)):
        return "Duplicate NIM " + "returning " + str(L)
    else:
        return Konso(MakeSetMhs(B, Tail(L)),getFirstMhs(L))

# Contoh Aplikasi SetMhs
print(
    MakeSetMhs(
        MakeMhs(24060124120011, "Rawr", "F", makeNilai([90, 100, 80])),
        [
            MakeMhs(24060124120014, "Mooo", "F", makeNilai([90, 100, 80])),
            MakeMhs(24060124120015, "Quack", "F", makeNilai([90, 100, 80])),
        ],
    )
)
