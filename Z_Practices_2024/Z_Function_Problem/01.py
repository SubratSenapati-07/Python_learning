def greatest(a,b,c):
    if a>b and a>c :
        return a 
    if b>a and b>c :
        return b
    if c>a and c>b :
        return c
    

a = int(input("Number 1:"))
b = int(input("Number 2:"))
c = int(input("Number 3:"))
greatvalue = greatest(a,b,c)
print("Greatest value is:",greatvalue)
