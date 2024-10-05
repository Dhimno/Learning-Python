def make_Customer(nama,jenis,jumlah,alpaca):
    return [nama,jenis,jumlah,alpaca]

def nama(C):
    return C[0]

def jenis(C):
    return C[1]

def jumlah(C):
    return C[2]

def bawa_alpaca(C):
    return C[3]

def handlerjenis(C):
    if jenis(C) == "Naga":
        return 0.8
    elif jenis(C) == "Mata Mata":
        return 0.5
    elif jenis(C) == "Hitman":
        return 2.3    
    else:
        return 1   
    
def lemonade(C):
    if bawa_alpaca(C) == True:
        return 0
    else:
        if jenis(C) == "Seniman" or jenis(C) == "Observer Planet" or jenis(C) == "Sejarawan":
            return 3 * handlerjenis(C) * jumlah(C)
        else:
            return 5 * handlerjenis(C) * jumlah(C)

 
print(lemonade(make_Customer("Alice", "Seniman", 10, False)))

