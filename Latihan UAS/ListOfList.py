List = [1,2,3,4,5,6,7,8]

def FirstElmt(List):
    return List[0]

def LastElmt(List):
    return List[-1]

def IsEmpty(List):
    return List == []

def Konso(element,List):
    return [element] + List

def Tail(List):
    return List[1:]

def IsGenap(element):
    return element % 2 == 0

def IsGanjil(element):
    return element % 2 != 0

def FilterBilGenap(List):
    if IsEmpty(List):
        return []
    else:
        if IsGenap(FirstElmt(List)):
            return Konso(FirstElmt(List),FilterBilGenap(Tail(List)))
        else:
            return FilterBilGenap(Tail(List))
        
def FilterBilGanjil(List):
    if IsEmpty(List):
        return []
    else:
        if IsGanjil(FirstElmt(List)):
            return Konso(FirstElmt(List),FilterBilGanjil(Tail(List)))
        else:
            return FilterBilGanjil(Tail(List))

def NbElmt(List):
    if IsEmpty(List):
        return 0
    else:
        return 1 + NbElmt(Tail(List))

def AvgElmt(List):
    return SumElmt(List)/NbElmt(List)

def ElmtKeN(N,List):
    return List[N]

def SumElmt(List):
    if IsEmpty(List):
        return 0
    else:
        return FirstElmt(List) + SumElmt(Tail(List))
        
print("Ini adalah Bilangan Genap", FilterBilGenap(List))
print("Ini adalah Bilangan Ganjil", FilterBilGanjil(List))
print("Ini adalah Jumlah dari semua element list", SumElmt(List))
print("Ini adalah Jumlah dari element genap list", SumElmt(FilterBilGenap(List)))
print("Ini adalah rata rata dari list", AvgElmt(List))
print("Ini adalah elemenet ke N dari list", ElmtKeN(0,List))
