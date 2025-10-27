# Directly using Function to Solve Problem 01.
def greatest(a,b,c):
    if a>b and b>c :
        return a
    elif b>a and b>c :
        return b
    else :
        return c
a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))
print("Greater:", greatest(a,b,c))
