# WAP a recursive function to calculate
# the sum of first n natural number.

def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
n = int(input("Enter natural number:"))
print(f"Sum of Natural number {n} is : {sum(n)}")
