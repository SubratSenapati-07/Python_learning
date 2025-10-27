# Print a star Pattern ( n = 3)

n = int(input("Enter number to print star pattern: "))
i=1
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print(" ")