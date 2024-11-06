def firstelement(L):
    return L[0]

def tail(L):
    return L[1:]

def nbelement(L):
    if L == []:
        return 0
    else:
        return 1 + nbelement(tail(L))

def messup(L):
    if L == []:
        return []
    if nbelement(L) % 2 == 0:
        return [-1*firstelement(L)] + messup(tail(L))
    else:
        return [firstelement(L)] + messup(tail(L))