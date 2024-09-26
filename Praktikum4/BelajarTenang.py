# Program     : BelajarTenang.py
# Deskripsi   : Menghitung jarak minimal yang harus mereka tempuh agar suara dari sound system tidak melebihi 40 dB dan menghitung apakah bensin masih memungkinkan
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

def Jarak(x,y):
    return round(15 * 10**((x-40)/20),3)
def BelajarTenang(x,y):
    if Jarak(x,y) <= y:
        return str(Jarak(x,y)) + " meter"
    else:
        return "Isi bensin dulu, bang"

print(BelajarTenang(102, 20000))
print(BelajarTenang(100, 1300))
print(BelajarTenang(50, 30000))
