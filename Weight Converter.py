weight = input("Masukkan berat badan anda (KG): ")
satuan = input("(K)g or (P)ounds: ")
if satuan == "K":
    s_kg = print(int(weight) * 0.453592)
elif satuan == "k":
    s_kg = print(int(weight) * 0.453592)
elif satuan == "P":
    s_pound = print(int(weight) * 2.20462)
elif satuan == "p":
    s_pound = print(int(weight) * 2.20462)
else:
    print("Invalid")