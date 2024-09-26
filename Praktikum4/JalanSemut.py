# Program     : JalanSemut.py
# Deskripsi   : Mencari jalan bagi semut dengan jarak terpendek yang memungkinkan antara 0,0,0 dan x,y,z
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

import math
def jalanSemut(x,y,z):
    return round(math.sqrt((min(x,y,z) + (x + y + z - min(x,y,z) - max(x,y,z)))**2 + max(x,y,z)**2),3)

print(jalanSemut(5,4,3))
print(jalanSemut(1,2,7))
print(jalanSemut(10,10,7))