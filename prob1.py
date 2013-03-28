__author__ = 'undergroundskier'

c = 0
for x in range(0,1000):
    if(not(x % 3) or not(x % 5)):
        c+=x

print c
