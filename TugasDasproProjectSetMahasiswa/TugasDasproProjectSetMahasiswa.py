# Program   : TugasDasproProjectSetMahasiswa.py
# Deskripsi : Program yang berisi tentang implementasi dan penggunaan dari set of Mahasiswa
# Kelompok  : 24060124120010/Dhimas Reza Nafi Wahyudi, Anggota 2, Anggota 3, Anggota 4, Anggota 5
# Tanggal   : 10/11/2024

from listFunction import *

# Bagian 1
# Nomor 1 (Realisasi Selektor)
def getNIM(L): # Selektor untuk mengambil NIM dari mahasiswa
    return L[0]

def getNama(L):
    return L[1]

def getKelas(L):
    return L[2]

def getNilai(L):
    return L[3]

# Nomor 2
def IsEmpty(L):
    return L == []

def Konso(e, L):
    return [e] + L

def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]
    
# Fungsi antara untuk memrposes fungsi Nilai_Tertinggi
def MaxElmt(L):
    if IsEmpty(L):  # Basis: Jika list mahasiswa kosong, kembalikan nilai 0
        return 0
    elif getNilai(getFirstMhs(L)) == []:  # Jika mahasiswa pertama tidak punya nilai, lanjut ke Tail
        return MaxElmt(Tail(L))
    elif MaxElmt(Tail(L)) > FirstElmt(getNilai(getFirstMhs(L))):  # Bandingkan dengan nilai dari Tail
        return MaxElmt(Tail(L))
    else:  # Jika nilai mahasiswa pertama lebih besar atau sama, kembalikan nilai tersebut
        return FirstElmt(getNilai(getFirstMhs(L)))
    
# Bagian 2
# Nomor 1
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakeMhs(nim, nama, kelas, nilai): # Untuk membuat tipe bentukan mahasiswa
    return [nim, nama, kelas, nilai]

def makeNilai(nilai): # Untuk membuat set Nilai
    return nilai

# DEFINISI DAN SPESIFIKASI SELEKTOR
def getFirstMhs(set): # Selektor untuk mengambil list mahasiswa pertama dari set mahasiswa
    return set[0]

def getLastMhs(set): # Selektor untuk mengambil lst mahasiswa terakhir dari set mahasiswa
    return set[-1]


# Nomor 2
def MakeSpecialSetMhs(B, L): # Membuat set Mahasiswa dimana terdiri dari gabungan mahasiswa dengan NIM yang unik
    if IsEmpty(L):
        return Konso(B, L)
    elif getNIM(B) == getNIM(getFirstMhs(L)):
        return "Duplicate NIM " + "returning " + str(L)
    else:
        return Konso(MakeSpecialSetMhs(B, Tail(L)),getFirstMhs(L))
    
def TdkMngrjknKuis(L):
    if IsEmpty(L):  # Jika list mahasiswa kosong, kembalikan list kosong
        return []
    elif getNilai(getFirstMhs(L)) == []:  # Jika mahasiswa pertama tidak mengerjakan kuis (nilai == [])
        # Tambahkan seluruh data mahasiswa yang tidak mengerjakan kuis ke hasil
        return MakeSpecialSetMhs(getFirstMhs(L), TdkMngrjknKuis(Tail(L)))  # Tambahkan mahasiswa ke hasil dan lanjutkan
    else:
        return TdkMngrjknKuis(Tail(L))  # Jika mahasiswa mengerjakan kuis, lanjutkan ke elemen berikutnya tanpa menambahkannya ke hasil

print("Mahasiswa yang tidak mengerjakan kuis:", TdkMngrjknKuis(([MakeMhs('24060124120032', 'Dewangga Maulana Saputro', 'B', makeNilai([])), MakeMhs('24060124120033', 'Dhimas Rheza', 'B', makeNilai([90]))])))


# Fungsi untuk mendapatkan mahasiswa dengan nilai tertinggitanpa 
def NilaiTertinggi(L):
    if IsEmpty(L):
        return []
    elif getNilai(getFirstMhs(L)) == [MaxElmt(L)]:
        # Tambahkan mahasiswa dengan nilai tertinggi ke dalam list hasil
        return MakeSpecialSetMhs(getFirstMhs(L), NilaiTertinggi(Tail(L)))
    else:
        # Lanjutkan ke mahasiswa berikutnya jika nilai tidak sama dengan nilai tertinggi
        return NilaiTertinggi(Tail(L))
    
print("Mahasiswa dengan nilai tertinggi:", NilaiTertinggi(([MakeMhs('24060124120032', 'Dewangga Maulana Saputro', 'B', makeNilai([85])), MakeMhs('24060124120033', 'Dhimas Rheza', 'B', makeNilai([90]))])))






# Contoh Aplikasi SetMhs
print(
    MakeSpecialSetMhs(
        MakeMhs(24060124120011, "Rawr", "F", makeNilai([90, 100, 80])),
        [
            MakeMhs(24060124120014, "Mooo", "F", makeNilai([90, 100, 80])),
            MakeMhs(24060124120015, "Quack", "F", makeNilai([90, 100, 80])),
        ],
    )
)

