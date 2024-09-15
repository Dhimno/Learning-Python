def JenisSegitiga(a,b,c):
    if a+b > c:
        if a == b and a == c and b == c:
            return "sama sisi"
        elif a == b or b == c or c == a:
            return "sama kaki"
        else:
            return "sembarang"
    else:
        return "tidak terbentuk"

min ()
print(JenisSegitiga(1,4,5))
print(JenisSegitiga(6,3,6))