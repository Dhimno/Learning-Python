# Program     : denumerator.py
# Deskripsi   : Menentukan urutan angka x yang terulang sesuai dengan hasil pembagian 1 dengan sebuah bilangan bulat
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

def denumeratorSeq(x):
    if (10**len(x) - 1) > 0 and (10**len(x) - 1)%int(x) == 0:
            return "Ada: " + str((10**len(x) - 1)//int(x))
    return "Tidak ada"

print(denumeratorSeq('3'))
print(denumeratorSeq('166'))
print(denumeratorSeq('1'))