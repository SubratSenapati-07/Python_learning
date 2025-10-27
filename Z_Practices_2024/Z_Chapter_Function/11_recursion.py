# Find factorial of n number by using recursion.

def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

num = int(input("Enter number:"))
print("Fatorial:",factorial(num))




