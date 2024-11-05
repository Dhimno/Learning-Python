def psum(L):
    if L == []:
        return []
    else:
        return [L[0]] + [L[1]+L[0]] + psum(L[2:])
    
print(psum([1000, -20000, 50000, 100000, -250000]))