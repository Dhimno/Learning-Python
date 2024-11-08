def Tail(L):
    return L[1:]

def Tail2(L):
    return L[2:]

def FirstElement(L):
    return L[0]

def SecondElement(L):
    return L[1]

def NBelement(L):
    if L == []:
        return 0
    else:
        return 1 + NBelement(Tail(L))

def psum(L):
    if NBelement(L) == 0:
        return []
    elif NBelement(L) == 1:
        return [FirstElement(L)]
    else:
        return [FirstElement(L)] + psum([FirstElement(L)+SecondElement(L)]+L[2:])

print(psum([1000, -20000, 50000, 100000, -250000]))