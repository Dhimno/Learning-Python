def stabilize(L):
    if L == []:
        return []
    elif L[0] > 100:
        return [100] + stabilize(L[1:])
    elif L[0] < -100:
        return [-100] + stabilize(L[1:])
    else:
        return [L[0]] + stabilize(L[1:])
    
print(stabilize([-150, -50, 0, 50, 150]))

