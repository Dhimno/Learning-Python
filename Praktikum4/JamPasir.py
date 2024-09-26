# Program     : JamPasir.py
# Deskripsi   : Menulis waktu yang di input jika valid dan memberikan output "Waktu tidak valid" apabila input tidak memenuhi kondisi
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

def jam(j,m,s):
    if j <= 24 and j >=0:
        if m <= 59 and m >= 0:
            if s <= 59 and s >= 0:
                return "Jam: " + str(j) + ", Menit: " + str(m) + ", Detik: " + str(s)
    return "Waktu tidak valid"

print(jam(12,30,45))
print(jam(12,45,60))
print(jam(12,45,59))