# Program     : PerpustakaanAgung.py
# Deskripsi   : Menghitung perkiraan pengunjung
# NIM/Nama    : 24060124120010
# Tanggal     : (26/09/2024)

def PengunjungDay(day):
    if day == "senin":
        return (5000 + 6000 + 4000) / 3
    elif day == "selasa":
        return (7000 + 5000 + 2000) / 3
    elif day == "rabu":
        return (4500 + 3500 + 3000) / 3
    elif day == "kamis":
        return (2900 + 2100 + 2000) / 3
    elif day == "jumat":
        return (3000 + 3000 + 3000) / 3
    elif day == "sabtu":
        return (2000 + 2500 + 2300) / 3
    elif day == "minggu":
        return (1100 + 900 + 1000) / 3

def Estimation(D, X, Y, AS, AM, AIP):
    return (abs(Y-X)*(max(AS, AM, AIP)-min(AS, AM, AIP)))/PengunjungDay(D)

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    if X < SR and Y > SS:
           return round((Estimation(D, X, SR, AS, AM, AIP)*(R/100)+Estimation(D, SS, SR, AS, AM, AIP)+Estimation(D, SS, Y, AS, AM, AIP)*(R/100))/3, 5)
    elif X < SR and Y > SR:  
        return round((Estimation(D, X, SR, AS, AM, AIP)*(R / 100)+Estimation(D, SR, Y, AS, AM, AIP))/2, 5)
    elif  Y > SS and X < SS: 
        return round((Estimation(D, X, SS, AS, AM, AIP) + Estimation(D, SS, Y, AS, AM, AIP)*(R/100))/2, 5)
    elif (X < SR) or ((X > SS) and (Y < SR)) or (Y > SS):
        return round(Estimation(D, X, Y, AS, AM, AIP) * (R/100), 5)
    else:
        return round(Estimation(D,X,Y, AS, AM, AIP), 5)

print(EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3))
print(EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50))
print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75))