weight = input("Masukkan berat badan anda (KG): ")
tinggi = input("Masukkan tinggi anda (cm): ")
tinggi_meter = int(tinggi) / 100
IMT = float(weight) / (float(tinggi_meter) * float(tinggi_meter))
float(IMT)
if IMT < 18.5:
    print("You are underweight!")
elif IMT < 24.9:
    print("You're Normal! Keep it up!")
elif IMT < 30:
    print("You are overweight!")
elif IMT >= 30:
    print("You're obese!!") 
print("BMI-mu adalah " + str(int(IMT)))