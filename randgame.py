import random

def maingame():
    x = random.randint(0,100)
    print("============================================\nWelcome to a simple guess the number game!")
    y = int(input("Please input your number here\n--> "))
    while y != x:
        if y > x:
            print("Lower!!!")
            y = int(input("Please input your number here\n--> ")) 
        elif y < x:
            print("Higher!!!")
            y = int(input("Please input your number here\n--> "))
        else:
            print("Congratulations the number was indeed" + x)
    coba_lagi()



def coba_lagi():
    print("============================================")
    plagi = input("Mau lagi ngga? (Y/N)\n--> ")
    if plagi == "Y" or plagi == "y":
        maingame()
    elif plagi == "N" or plagi == "n":
        print("Terima kasih telah bermain game tolol ini!")
    else:
        print("Tolol anjing gw bilang aja Y/N")
        coba_lagi()

maingame()