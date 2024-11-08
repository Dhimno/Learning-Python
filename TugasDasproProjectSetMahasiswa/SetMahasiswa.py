from listFunction import *


def makeNilai(nilai): # Untuk membuat set Nilai
    return nilai


def MakeMhs(nim, nama, kelas, nilai): # Untuk membuat tipe bentukan mahasiswa
    return [nim, nama, kelas, nilai]


def getNIM(Mhs): # Selektor untuk mengambik NIM dari mahasiswa
    return Mhs[0]


def FirstMhs(sMhs): # Selektor untuk mengambil list mahasiswa pertama dari set mahasiswa
    return sMhs[0]


def SetMhs(B, L): # Membuat set Mahasiswa dimana terdiri dari gabungan mahasiswa dengan NIM yang unik
    if IsEmpty(L):
        return Konso(B, L)
    elif getNIM(B) == getNIM(FirstMhs(L)):
        return "Duplicate NIM " + "returning " + str(L)
    else:
        return Konso(FirstMhs(L), SetMhs(B, Tail(L)))

# Contoh Aplikasi SetMhs
print(
    SetMhs(
        MakeMhs(24060124120011, "Rawr", "F", makeNilai([90, 100, 80])),
        [
            MakeMhs(24060124120014, "Mooo", "F", makeNilai([90, 100, 80])),
            MakeMhs(24060124120015, "Quack", "F", makeNilai([90, 100, 80])),
        ],
    )
)
