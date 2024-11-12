def makeTree(A,PN):
    return [A,PN]

def akar(Tree):
    return Tree[0]

def anak(Tree):
    return Tree[1]

def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(anak(PN)) == True)

