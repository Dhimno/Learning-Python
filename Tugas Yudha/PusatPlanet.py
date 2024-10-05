# import sys
# exec(''.join(sys.stdin.readlines()))

# Konstruktor
def make_Titik(x,y):
    return [x,y]

def make_sirkel(T,r):
    return [T,r]

# Selektor
def titik_pusat(P):
    return P[0]

def jari_jari(P):
    return P[1]

# Predikat
def is_bersinggungan(S1,S2):
    if (((titik_pusat(S1)[0] - titik_pusat(S2)[0])**2 + (titik_pusat(S1)[1]-titik_pusat(S2)[2])**2) ** 2) <= (jari_jari(S1)+jari_jari(S2)) and (((titik_pusat(S1)[0] - titik_pusat(S2)[0])**2 + (titik_pusat(S1)[1]-titik_pusat(S2)[2])**2) ** 2) >= abs(jari_jari(S1) - jari_jari(S2)):
        return True
    else:
        return False
# Operator
# def titik_potong_sumbu_x(S):
#     if 




print(is_bersinggungan(make_sirkel(make_Titik(6, 1), 5), make_sirkel(make_Titik(6, 5), 1)))
# print(titik_potong_sumbu_x(make_sirkel(make_Titik(1, 1), 5)))
#                            <<1,1>,5>      (<1,1>,5)

