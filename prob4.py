__author__ = 'undergroundskier'

from utils import largest
def pal():
    v = []
    for x in range(999, 99, -1):
        for y in range(999, x, -1):
            v1 = x*y
            v1_s = str(v1)
            v2_s = v1_s[::-1]
            if v1_s == v2_s:
                v.append(v1)
    return v

p = pal()
print largest(p)


