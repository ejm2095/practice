__author__ = 'ejm2095'

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#designed for this problem ONLY!
def mod(max, v):
    d = 0
    for x in range(1,max+1):
        if v%x:
            d += 1
    return not bool(d)

def min(s, max):
    min = m = max
    b = True
    if mod(s,m):
        max = m
    cnt = 1
    while m>1:
        if mod(s,m):
            min = m
        m /= (2*cnt)
        cnt += 1

    print min

s = 20
i = (10*11*13*14*17*19*18*16)
min(s,i)






