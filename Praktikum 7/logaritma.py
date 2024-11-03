def logaritma(L):
    if L < 0:
        return 
    elif L == 0:
        return [1]
    elif L == 1:
        return [2]
    else:
        return [2**L] + logaritma(L-1)
    
print(logaritma(4))


# Belum selesai