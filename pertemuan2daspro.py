angka = 1024
desimal = 3.14
karakter = 'a'
teks = "Solkhan's always"
bool = True
masukan = input("Masukkan teks: ")

def isorigin(x,y):
    return x == 0 and y == 0

def max2(a,b):
    return ((a+b)+abs(a-b))//2

def max3(a,b,c):
    return max2(max2(a,b), c)



print(angka)
print(desimal)
print(karakter)
print(teks, bool)
print(masukan)
print(isorigin(100,100))
print(isorigin(0,0))

print(max2(5,10))