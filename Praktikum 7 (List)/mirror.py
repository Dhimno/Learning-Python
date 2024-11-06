def Mirror(L):
    if L == []:
        return []
    else:
        return L + L[::-1]
    
print(Mirror([1,2,3]))