i = 1
loop = 1
while loop <= 3:
     aktif = 1
     loop += 1
     if aktif == 1:
        while i <= 5:
                print(int(i) * "*")
                i += 1
                if i == 5:
                    aktif = 0
     if aktif == 0:
        while i >= 1:
                print(int(i) * "*")
                i -= 1

#def asterisk():
#    while i <= 5:
#        print(int(i) * "*")
#        i = i + 1
#if aktif == 1:
#    asterisk()
