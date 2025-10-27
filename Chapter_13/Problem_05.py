from functools import reduce
lst =[5,8,9,2,1,75,85,2,55515,4]
def max(a,b):
    if a>b:
        return a
    return b 
    
print(reduce(max,lst))
