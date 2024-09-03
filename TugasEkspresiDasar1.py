# Nama file : TugasEkspresiDasar1.py
# Pembuat   : Dhimas Reza Nafi Wahyudi
# Tanggal   : 3 September 2024
# Deskripsi : Mengubah waktu menjadi detik

# Definisi dan spesifikasi
# total_detik : 3 integer --> integer
# total_detik(x,y,z) adalah total detik dari waktu yang ditentukan

# Definisi dan spesifikasi fungsi antara
# jam(x) : integer --> integer
# jam(x) adalah total detik dari satuan jam yang ditentukan

# menit(x) : integer --> integer
# menit(x) adalah total detik dari satuan menit yang ditentukan

# Realisasi
def jam(x):
    return x*3600

def menit(x):
    return x*60

def total_detik(x,y,z):
    if 0 <= x <= 24 and 0 <= y <= 59 and 0 <= z <= 59:
        print("Jadi total detik dalam waktu "+ str(x) + " jam " + str(y) + " menit " + str(z) + " detik adalah " + str(jam(x) + menit(y) + z))
    else:     
        print("Penulisan waktu salah!")

# Aplikasi
total_detik(25, 0, 0)
total_detik(25, 0, 0)
total_detik(24, 90, 0)