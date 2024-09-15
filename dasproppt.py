# Hitung rata rata nilai berbobot       RataRata(w,x,y,z,a,b,c,d)

# Definisi dan spesifikasi
# RataRata = 4 real 4 int --> int
# {RataRata(w,x,y,z,a,b,c,d) adalah rata-rata dari 4 nilai yang berbobot}

# Realisasi
def RataRata(w,x,y,z,a,b,c,d) : 
    return (((w*a) + (x*b) + (y*c) + (z*d))// (a+b+c+d))

# Aplikasi
print(RataRata(1,2,3,4,5,6,7,8))

# ===============================================================================

# Hitung nilai tengah dari 3 bilangan       median(a,b,c)

# Definisi dan spesifikasi
# median = 3 int --> int
# {median(a,b,c) adalah nilai tengah dari bilangan a, b, dan c}

# Realisasi
def max1(a,b):
    return max(a,b)
def max2(a,b):
    return max(a,b)
def min1(a,b):
    return min(a,b)
def min2(a,b):
    return min(a,b)
def median(a,b,c):
    return (a+b+c)-(max2(max1(a,b),c)-min2(min1(a,b),c)) 

#Aplikasi
print(median(1,4,5))


