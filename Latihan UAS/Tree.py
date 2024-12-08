from ListOfList import *

print("============================================")

def IsList(element):
    return type(element) == list

def IsAtom(element):
    return type(element) != list

Kontol1 = 1
Kontol2 = [1]
Kontol3 = [1,2,[3,4]]

print("Ini adalah IsList", IsList(Kontol1))
print("Ini adalah IsAtom", IsAtom(Kontol2))

def IsContainList(List): 
    if IsEmpty(List):
        return False
    else:
        if IsList(FirstElmt(List)):
            return True
        else:
            return IsContainList(Tail(List))

print("Ini adalah IsContainList", IsContainList(Kontol3))
        
