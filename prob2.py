__author__ = 'ejm2095'
#By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.
x=1
y=2
c=0
MAX = 4000000
cont = True
while cont:
    if not(x%2):
        c+=x
    if not(y%2):
        c+=y
    if (x+y)<MAX:
        x+=y
    if (x+y)<MAX:
        y+=x
    else:
        cont = False

print c