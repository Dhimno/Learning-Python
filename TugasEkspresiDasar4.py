# Nama file : TugasEkspresiDasar4.py
# Pembuat   : Dhimas Reza Nafi Wahyudi
# Tanggal   : 3 September 2024
# Deskripsi : Mengecek status cumlaude mahasiswa

# Definisi dan spesifikasi
# cumlaude : 2 real --> boolean
# cumlaude(bulan, IPK) 

# Realisasi
def cumlaude(bulan, IPK):
    if bulan <= 54.0 and 3.5 <= IPK <= 4.0:
        print("Mahasiswa dengan masa studi " + str(bulan) + " bulan dan dengan IPK " + str(IPK) + " dinyatakan lulus cumlaude.")
    else:
        print("Mahasiswa dengan masa studi " + str(bulan) + " bulan dan dengan IPK " + str(IPK) + " dinyatakan tidak lulus cumlaude.")

# Aplikasi
cumlaude(40.0, 2.5)
cumlaude(40.0, 3.6)
cumlaude(50.0, 4.0)
