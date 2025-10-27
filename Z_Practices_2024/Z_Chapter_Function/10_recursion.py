# Sum of Nth Natural number

def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)

num = int(input("Enter number here:"))
print("Sum:",sum(num))


'''
# Explaination:
num = 3
1+2+3 = 6
'''