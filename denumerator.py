def denumeratorSeq(x):
    if (10**len(x) - 1) > 0 and (10**len(x) - 1)%int(x) == 0:
            return "Ada: " + x
    return "Tidak ada"

print(denumeratorSeq("-3"))