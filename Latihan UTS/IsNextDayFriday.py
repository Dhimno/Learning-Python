# Mengecek apakah hari esok adalah hari Jum'at                              IsNextDayFriday?(h, b, t)
# DEFINISI DAN SPESIFIKASI
# IsNextDayFriday? : 3 _integer_ --> _boolean_
#       {IsNextDayFriday?(h, b, t) merupakan sebuah predikat untuk mengecek apakah hari esok adalah hari jum'at}
# IsKabisat? : _integer_ --> _boolean_
#       {IsKabisat?(t) merupakan sebuah predikat untuk mengecek apakah tahun yang disediakan adalah tahun kabisat}
# dpm : _integer_ --> _integer_
#       {dpm(b) merupakan sebuah fungsi untuk mengkonversi sebuah hari pertama bulan menjadi hari ke-x dalam tahun tersebut}
#
# Realisasi
# IsKabisat?(t) : 
#   _if_ t _mod_ 4 _and_ t _mod_ 100 != 0 _or_ t _mod_ 400 = 0 _then_
#       _true_
#   _else_
#       _false_
#
# dpm(B):
#   _depend on_ B
#       B = 1 : 1
#       B = 2 : 32
#       B = 3 : 60
#       B = 4 : 91
#       B = 5 : 121
#       B = 6 : 152
#       B = 7 : 182
#       B = 8 : 213
#       B = 9 : 244
#       B = 10 : 274
#       B = 11 : 305
#       B = 12 : 335
#
# IsNextDayFriday?(h,b,t) :
#   _if_ b > 2 _and_ IsKabisat(t) _then_
#       (dpm(b) + (h-1) + 1) _mod_ 7 = 4
#   _else_
#       (dpm(b) + (h-1)) _mod_ 7 = 4

def IsKabisat(t):
    if t % 4 == 0 and t % 100 != 0 or t % 400 == 0:
        return True
    else:
        return False

def dpm(B):
    if B == 1:
        return 1
    elif B == 2:
        return 32
    elif B == 3:
        return 60
    elif B == 4:
        return 91
    elif B == 5:
        return 121        
    elif B == 6:
        return 152
    elif B == 7:
        return 182
    elif B == 8:
        return 213
    elif B == 9:
        return 244  
    elif B == 10:
        return 274
    elif B == 11:
        return 305
    elif B == 12:
        return 335
    
def IsNextDayFriday(h,b,t):
    if b > 2 and IsKabisat(t) == True:
        if (dpm(b) + (h-1) + 1) % 7 == 4:
            return True
        else:
            return False
    else:
        if (dpm(b) + (h-1)) % 7 == 4:
            return True
        else:
            return False
    
# Aplikasi
# IsNextDayFriday?(4, 1, 2020) --> _true_
# IsNextDayFriday?(29, 2, 2020) --> _true_
# IsNextDayFriday?(7, 3, 2020) --> _true_

print(IsNextDayFriday(4, 1, 2020))
print(IsNextDayFriday(29, 2, 2020))
print(IsNextDayFriday(7, 3, 2020))



