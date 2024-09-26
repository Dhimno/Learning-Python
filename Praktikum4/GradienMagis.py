# Program     : GradienMagis.py
# Deskripsi   : Menghitung a dan b pada f(x) lalu mensubtitusi hasilnya pada rumus gradien
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

def f(x):
    return 3*x**2 + 2*x -5
    
def gradien(a,b):
    return ((f(a)-f(b))/(a-b))

print(eval(input()))