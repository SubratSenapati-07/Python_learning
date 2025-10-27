# Filter EXample: It is for list.
l = [2,5,4,9,14]
def even(n):
    if n%2 == 0 :
        return True
    else:
        return False
    
onlyEven =  filter(even,l)
print(list(onlyEven))