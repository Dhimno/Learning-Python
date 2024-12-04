def IsEmpty(L):
    return L == []

def MakePB(A, L, R):
    return [A, L, R]

def NilaiTengah(awal, akhir):
    return (awal + akhir + 1) // 2  

def BuildBalanceTree(L, n):
    def MakeTree(awal, akhir):
        if awal > akhir:
            return []
        return MakePB(
            L[NilaiTengah(awal, akhir)],
            MakeTree(awal, NilaiTengah(awal, akhir) - 1),  
            MakeTree(NilaiTengah(awal, akhir) + 1, akhir)  
        )
    return MakeTree(0, n - 1)

print(eval(input()))
