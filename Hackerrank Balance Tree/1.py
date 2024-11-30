def IsEmpty(L):
    return L == []

def MakePB(A, L, R):
    return [A, L, R]

def NilaiTengah(awal, akhir):
    return (awal + akhir + 1) // 2  

def BuildBalanceTree(L, n):
    def build_tree(awal, akhir):
        if awal > akhir:
            return []
        return MakePB(
            L[NilaiTengah(awal, akhir)],
            build_tree(awal, NilaiTengah(awal, akhir) - 1),  
            build_tree(NilaiTengah(awal, akhir) + 1, akhir)  
        )
    return build_tree(0, n - 1)

print(eval(input()))
