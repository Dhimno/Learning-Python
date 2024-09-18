def IsKabisat(x):
    if x % 4 == 0 and x % 100 != 0 or x // 400 == 0:
        return True
def HariKe(d,m,y):
    if m == 1:
        return 1 + d-1
    if m > 2 and IsKabisat(y) == True:
        if m == 3:
            return 60 + d-1 + 1
        elif m == 4:
            return 91 + d-1 + 1
        elif m == 5:
            return 121 + d-1 + 1
        elif m == 6:
            return 152 + d-1 + 1
        elif m == 7:
            return 182 + d-1 + 1
        elif m == 8:
            return 213 + d-1 + 1
        elif m == 9:
            return 244 + d-1 + 1
        elif m == 10:
            return 274 + d-1 + 1
        elif m == 11:
            return 305 + d-1 + 1
        elif m == 12:
            return 335 + d-1 + 1
    elif m == 2:
        return 32 + d-1 
    elif m == 3:
        return 60 + d-1 
    elif m == 4:
        return 91 + d-1 
    elif m == 5:
        return 121 + d-1
    elif m == 6:
        return 152 + d-1 
    elif m == 7:
        return 182 + d-1
    elif m == 8:
        return 213 + d-1
    elif m == 9:
        return 244 + d-1
    elif m == 10:
        return 274 + d-1 
    elif m == 11:
        return 305 + d-1 
    elif m == 12:
        return 335 + d-1
    else:
        return "Invalid month"
    
def IsLusaKamis(d,m,y):
    if HariKe(d+2,m,y) % 7 == 6:
        return True
    else:
        return False

print(IsLusaKamis(4,1,2020))
print(IsLusaKamis(24,5,1999))
print(IsLusaKamis(10,8,2000))

# 29 Februari = Kamis
# 28 Feruari = senin

