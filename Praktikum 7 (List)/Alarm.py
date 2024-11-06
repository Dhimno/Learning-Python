def ring(L):
    if L <= 0:
        return []
    else:
        return [L] + ring(L-15)
    
print(ring(60))