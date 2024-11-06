def Konso(L, e):
    return [e] + L

def Konsi(e, L):
    return L + [e]

def Tail(L):
    return L[1:]

def Head(L):
    return L[:-1]

def FirstElement(L):
    return L[0]

def LastElement(L):
    return L[-1]

def IsEmpty(L):
    return L == []

def IsOneElement(L):
    return len(L) == 1

def NbElement(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElement(Tail(L))

def psum(L):
    if IsEmpty(L):
        return []
    if IsOneElement(L):
        return [FirstElement(L)]
    else:
        return [FirstElement(L) + psum(Tail(L))[0]] + psum(Tail(L))

print(psum([1000, -20000, 50000, 100000, -250000]))
