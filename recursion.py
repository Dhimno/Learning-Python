def add(x,y):
    if y == 0 :
        return x
    else :
        return 1 + add(x,y-1)
    
print(add(1,2))
print(add(3,4))
print(add(6,7))

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
    if x < y:
        return 0
    return 1 + bagi(x-y,y)
print(bagi(11,2))


def akar(x,y):
    if y**2 < x and ((y+1)**2 >x):
        return y
    if y**2 == x:
        return y
    return akar(x,y+1)

print(akar(3,1))

def faktorial(x):
    if x == 0:
        return 1
    else:
        return x*(faktorial(x-1))
    
print(faktorial(6))
print(faktorial(7))

def faciter(a,b,c):
    if a == b:
        return c * b
    else:
        return faciter(a,b+1,c*b)

def fac(n):
    return faciter(n,1,1)

print(fac(6))
print(fac(7))

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))

