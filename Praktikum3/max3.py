def max3(a,b,c):
    if a > b:
        if a > c:
            return a
    elif b > a :
        if b > c:
            return b
    else :
        return c
    
# Aplikasi
print("Maksimum dari 10, 7, 5 adalah ", max3(10,7,5))
print("Maksimum dari 3, 5, 2 adalah ", max3(3,5,2))
print("Maksimum dari 20, 20, 20 adalah ", max3(20,20,20))
