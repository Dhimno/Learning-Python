
x = int(input("Masukkan nilai suhu (Bukan Galvin) dalam celcius: "))
y = (input("Konversi ke?\n1. Reamur\n2. Fahrenheit\n3. Kelvin\n-> "))
def konversi(x, y):
    if y == "1":
        return 4/5 * x
    elif y == "2":
        return 9/5 * x + 32
    elif y == "3":
        return x+273
    else :
        return "Galvin ganteng banget >.<"
    
print("Jadi suhunya adalah", konversi(x,y))
    



