import math

def Akar1(a,b,c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / 2

def Akar2(a,b,c):
    return (-b - math.sqrt(b**2 - 4*a*c)) / 2

def AkarKuadrat(a,b,c):
    return max(Akar1(a,b,c),Akar2(a,b,c)) / min(Akar1(a,b,c),Akar2(a,b,c))

print(AkarKuadrat(1,2,1))
print(AkarKuadrat(1,-5,6))
print(AkarKuadrat(1,6,8))