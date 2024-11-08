def logaritma(L):
    if L == 0:
        return []
    else:
        return [2**L] + logaritma(L-1)
    
def konso(e,L):
    return [e] + L

def logaritma2(N):
    if N == 0:
        return []
    return konso(2**N, logaritma(N-1))

print(logaritma2(3))

# Belum selesai