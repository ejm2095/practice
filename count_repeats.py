
def repeatsNN(lst):
    awn = 0
    i =0
    while i < len(lst):
        p = lst.count(lst[i])
        if p > 1:
            awn += 1
        i += p
    return awn

def repeatsN(lst):
    awn = 0
    i =0
    d = {}
    while i < len(lst):
        x = lst[i]
        p = d.get(x)
        if not p:
            d[x] = 1
        if p == 1:
            awn += 1
            d[x] +=1
        i += 1
    return awn


l = [1,2,2,3,4,4,4,5,6]

print repeatsNN(l)
print repeatsN(l)



