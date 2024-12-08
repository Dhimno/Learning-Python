BST = [5,[2,[1,[],[]],[3,[],[]]],[7,[6,[],[]],[8,[],[]]]]

def akar(P):
    return P[0]

def kiri(P):
    return P[1]

def kanan(P):
    return P[2]

def isTreeNEmpty(P):
    return P == []

def BSearchX(x, P):
    if isTreeNEmpty(P):
        return False
    else:
        if akar(P) == x:
            return True
        else:
            return BSearchX(x,kiri(P)) or BSearchX(x,kanan(P))
        
def BSubtreeX(x, P):
    if isTreeNEmpty(P):
        return []
    else:
        if akar(P) == x:
            return P
        else:
            if BSubtreeX(x, kiri(P)):
                return BSubtreeX(x, kiri(P))
            return BSubtreeX(x, kanan(P))

print(BSubtreeX(2, BST))
