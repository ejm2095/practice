__author__ = 'ejm2095'

#Find the difference between:
# the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def sum_sqr(n):
    return ((n*(n+1))/2)**2

def sqr_sum(n):
    return (n*(n+1)*(2*n+1))/6

n = 100
print sum_sqr(n)-sqr_sum(n)