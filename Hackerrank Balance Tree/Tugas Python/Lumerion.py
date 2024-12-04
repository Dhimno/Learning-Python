

def MakeList(a):
    return [a]

def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def concatList(L1, L2):
    return L1 + L2

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def FirstList(LoL):
    return LoL[0]

def LastList(LoL):
    return LoL[-1]

def HeadList(LoL):
    return LoL[:-1]

def TailList(LoL):
    return LoL[1:]

def IsEmpty(LoL):
    if LoL == []:
        return True
    else:
        return False

def IsAtom(LoL):
    if type(LoL) == list:
             return False
    else:
        return True

def IsList(LoL):
    if IsAtom(LoL) == False:
        return True
    else:
        return False
def Tail(L):
    return L[1:]

def operasi(S):
    return S[0]

def IsEmpty(L):
    return L == []

def EvaluateExpression(S):
    if IsEmpty(S):
        return []
    else:
        if operasi(S) == '+':
            return FirstElmt(Tail(S)) + FirstElmt(Tail(Tail(S)))
        elif operasi(S) == '-':
            return FirstElmt(Tail(S)) - FirstElmt(Tail(Tail(S)))
        elif operasi(S) == '*':
            return FirstElmt(Tail(S)) * FirstElmt(Tail(Tail(S)))
        elif operasi(S) == '/':
            return FirstElmt(Tail(S)) / FirstElmt(Tail(Tail(S)))
    


print(EvaluateExpression(['-', 10, 4]))