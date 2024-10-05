# Total Biaya Air                               BiayaAir(kode, x)
# DEFINISI DAN SPESIFIkASI
# BiayaAir : _character_['A', 'B', 'C'], _real_ > 0 --> _real_
# {BiayaAir(kode, x) adalah sebuah fungsi untuk menghitung total biaya air dengan memperhitungkan berdasarkan kondisi dari input kode}

# Realisasi
# BiayaAir(kode, x) : 
# _depend on_ kode, x
#       kode = 'A' _and_ x <= 10 : _then_ 
#           30000
#       kode = 'A' _and_ x > 10 : _then_ 
#           30000 + (x-10) * 2500
#       kode = 'B' _and_ x <= 10 : _then_ 
#           40000
#       kode = 'B' _and_ x > 10 : _then_ 
#           40000 + (x-10) * 2500
#       kode = 'C' _and_ x <= 10 : _then_ 
#           50000
#       kode = 'C' _and_ x > 10 : _then_ 
#           50000 + (x-10) * 2500

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

# Aplikasi
# BiayaAir('A',25)
# BiayaAir('B',25)
# BiayaAir('C',25)