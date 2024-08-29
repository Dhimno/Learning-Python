# Nama file : Pangkat3.py
# Pembuat   : Dhimas Reza Nafi Wahyudi
# Tanggal   : 27 Agustus 2024
# Deskripsi : Menghitung pangkat 3 dari sebuah fungsi

# Definisi dan spesifikasi
# pangkat : integer --> integer
# pangkat(x) menghitung pangkat 3 dari sebuah angka

# Realisasi
def pangkat(x):
    return x ** 3

# Aplikasi
x = int(input('Masukkan angka yang ingin dipangkat 3: '))
print(pangkat(x))