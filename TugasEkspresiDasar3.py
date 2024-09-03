# Nama file : TugasEkspresiDasar3.py
# Pembuat   : Dhimas Reza Nafi Wahyudi
# Tanggal   : 3 September 2024
# Deskripsi : Mengecek tahun kabisat

# Definisi dan spesifikasi
# kabisat : 1 int --> boolean
# kabisat(x) adalah operasi yang menentukan apakah sebuah tahun kabisat atau tidak

# Realisasi
def kabisat(x):
    if x % 400 == 0:
        print("Tahun " + str(x) + " adalah tahun kabisat")
    elif x % 4 == 0 and x % 100 != 0:
        print("Tahun " + str(x) + " adalah tahun kabisat")
    else:
        print("Tahun " + str(x) + " bukan tahun kabisat")

# Aplikasi
kabisat(2000)
kabisat(1996)
kabisat(1900)