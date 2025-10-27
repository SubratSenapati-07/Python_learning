def divisible5(n):
    if(n%5 == 0):
        return True 
    return False 
lst = [5,68,45,95,90,40,50,30]
new = filter(divisible5,lst)
print(list(new))