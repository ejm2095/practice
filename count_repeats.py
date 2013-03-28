from datetime import datetime

def repeats(lst):
    awn = 0
    i =0
    while i < len(lst):
        p = lst.count(lst[i])
        if p > 1:
            awn += 1
        i += p
    return awn


l = [1,2,2,3,4,4,4,5,6]

print repeats(l)



