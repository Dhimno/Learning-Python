def logaritma(L):
    if L == 0:
        return []
    else:
        return [2**L] + logaritma(L-1)
    
print(logaritma(3))


# Belum selesai