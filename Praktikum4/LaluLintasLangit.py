# Program     : LaluLintasLangit.py
# Deskripsi   : Menggambarkan kondisi pesawat berdasarkan ketinggian, kecepatan, dan banyak bahan bakar yang tersisa
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

def monitor_pesawat(x,y,z):
    if x > 12000:
        return "Terlalu Tinggi"
    elif y > 900 or y < 200:
        return "Kecepatan Berbahaya"
    elif z < 20:
        return "Bahan Bakar Rendah"
    elif x < 5000 and y > 200 and y < 900 and z > 50:
        return "Aman untuk Mendarat"
    else:
        return "Berjalan Normal"
    
print(monitor_pesawat(4000,850,55))
print(monitor_pesawat(5000,950,70))
print(monitor_pesawat(6000,900,50))