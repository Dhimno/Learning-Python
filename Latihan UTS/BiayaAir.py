# Total Biaya Air                               BiayaAir(kode, x)
# DEFINISI DAN SPESIFIKASI
# BiayaAir : character, real --> real
# {BiayaAir(kode, x) adalah sebuah fungsi untuk menghitung total biaya air dengan memperhitungkan berdasarkan kondisi dari input kode}

# Realisasi
# BiayaAir(kode, x) : 
# depend on kode, x
#       Kode = 'A' and x <= 10 : then 30000
#       Kode = 'A' and x > 10 : then 30000 + (x-10) * 2500
#       Kode = 'B' and x <= 10 : then 40000
#       Kode = 'B' and x > 10 : then 40000 + (x-10) * 2500
#       Kode = 'C' and x <= 10 : then 50000
#       Kode = 'C' and x > 10 : then 50000 + (x-10) * 2500

def BiayaAir(kode, x):
    if kode == 'A':
        if x <= 10:
            return 30000
        else:
            return 30000 + (x-10) * 2500
    if kode == 'B':
        if x <= 10:
            return 40000
        else:
            return 40000 + (x-10) * 2500
    if kode == 'A':
        if x <= 10:
            return 50000
        else:
            return 50000 + (x-10) * 2500    
        
print(BiayaAir('A',25))