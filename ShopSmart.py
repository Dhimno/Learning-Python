def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    if kategori == "elektronik":
        if VIP == True:
            if hari == "Jumat" or hari == "Sabtu":
                if lokasi == "dalam negeri":
                    return harga * 70/100 * 95/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 70/100 * 95/100 * 120/100 
            elif hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 70/100 * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 70/100 * 105/100 * 120/100 
            else:
                if lokasi == "dalam negeri":
                    return harga * 70/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 70/100 * 120/100
        elif VIP == False:
            if hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 90/100 * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 90/100 * 105/100 * 120/100 
            else:
                if lokasi == "dalam negeri":
                    return harga * 90/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 90/100 * 120/100
                
    elif kategori == "pakaian":
        if VIP == True:
            if hari == "Jumat" or hari == "Sabtu":
                if lokasi == "dalam negeri":
                    return harga * 80/100 * 95/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 80/100 * 95/100 * 120/100 
            elif hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 80/100 * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 80/100 * 105/100 * 120/100 
            elif hari == "Rabu":
                if lokasi == "dalam negeri":
                    return harga * 80/100 * 95/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 80/100 * 95/100 * 120/100
            else:
                if lokasi == "dalam negeri":
                    return harga * 80/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 80/100 * 120/100
        elif VIP == False:
            if hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 95/100 * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 95/100 * 105/100 * 120/100 
            elif hari == "Rabu":
                if lokasi == "dalam negeri":
                    return harga * 95/100 * 95/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 95/100 * 95/100 * 120/100
            else:
                if lokasi == "dalam negeri":
                    return harga * 95/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 95/100 * 120/100   
    elif kategori == "makanan":
        if VIP == True:
            if hari == "Jumat" or hari == "Sabtu":
                if lokasi == "dalam negeri":
                    return harga * 85/100 * 95/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 85/100 * 95/100 * 120/100 
            elif hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 85/100 * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 85/100 * 105/100 * 120/100 
            else:
                if lokasi == "dalam negeri":
                    return harga * 85/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 85/100 * 120/100
        elif VIP == False:
            if hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 95/100 * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 95/100 * 105/100 * 120/100 
            else:
                if lokasi == "dalam negeri":
                    return harga * 95/100 * 110/100
                elif lokasi == "luar negeri":
                    return harga * 95/100 * 120/100
    else:
        if VIP == True:
            if hari == "Jumat" or hari == "Sabtu":
                if lokasi == "dalam negeri":
                    return harga * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 120/100 
            elif hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 105/100 * 120/100 
            else:
                if lokasi == "dalam negeri":
                    return harga * 110/100
                elif lokasi == "luar negeri":
                    return harga * 120/100
        elif VIP == False:
            if hari == "Minggu":
                if lokasi == "dalam negeri":
                    return harga * 105/100 * 110/100 
                elif lokasi == "luar negeri":
                    return harga * 105/100 * 120/100 
            else:
                if lokasi == "dalam negeri":
                    return harga * 110/100
                elif lokasi == "luar negeri":
                    return harga * 120/100