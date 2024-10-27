def BarisAritmatika(awal,beda,n):
    if n == 1:
        return awal
    else:
        return beda*n + BarisAritmatika(awal,beda,n-1)
    
print(BarisAritmatika(3,3,4))

def BarisGeometri(awal,ratio,n):
    if n == 1:
        return awal
    else:
        return awal*(ratio**(n-1)) + BarisGeometri(awal,ratio,n-1)
    
print(BarisGeometri(1,3,1))