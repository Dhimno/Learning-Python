from math import sqrt

#print(sqrt(16))


def add(x,y):
    if y == 0 :
        return x
    else :
        return 1 + add(x,y-1)
    
#print(add(90,90))

def kurang(x,y):
    if y == 0 :
        return x
    else :
        return kurang(x,y-1) - 1
#print(kurang(10,4))

def kali(x,y):
    if y == 1:
        return x
    return x + kali(x,y-1)
#print(kali(3,2))

def pangkat(x,y):
    if y == 1:
        return x
    return x * pangkat(x,y-1)
#print(pangkat(9,8))

def bagi(x,y):
    if x == 0:
        return 0
    return 1 + bagi(x-y,y)
#print(bagi(10,2))


def akar(x,y):
    if y**2 < x and ((y+1)**2 >x):
        return y
    if y**2 == x:
        return y
    return akar(x,y+1)

print(akar(3,1))


