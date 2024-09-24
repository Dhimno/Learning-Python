import math
def jalanSemut(x,y,z):
    return round(math.sqrt((min(x,y,z) + (x + y + z - min(x,y,z) - max(x,y,z)))**2 + max(x,y,z)**2),3)

print(jalanSemut(5,4,3))
