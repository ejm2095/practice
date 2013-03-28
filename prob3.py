__author__ = 'undergroundskier'

from utils import *

def prime(val):
    if val == 2:
        return True
    if val == 1:
        return False
    if not(val%2):
        return False
    for n in range(3, int(val**.5)+1, 2):
        if not(val%n):
            return False

    return True

def find(v):
    num = v
    facts = factors(num)
    awns = []
    for x in facts:
        if prime(x):
            awns.append(x)
    return awns
print largest(find(600851475143))

