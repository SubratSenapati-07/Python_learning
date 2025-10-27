# Reduce Example: it is for list.
from functools import reduce
l = [1,3,2,5,3]
def sum(a,b):
    return a+b 
print(reduce(sum,l))

multiply = lambda a,b: a*b
print(reduce(multiply,l))