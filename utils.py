__author__ = 'undergroundskier'
def factors(n):
    fact=[1,n]
    check=2
    rootn=n**.5
    while check<rootn:
        if n%check==0:
            fact.append(check)
            fact.append(n/check)
        check+=1
    if rootn==check:
        fact.append(check)
        fact.sort()
    return fact

def largest(lst):
    v = lst[0]
    for x in lst:
        if x>v:
            v=x
    return v