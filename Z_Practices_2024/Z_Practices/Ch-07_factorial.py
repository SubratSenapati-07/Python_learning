input = int(input("Enter number: "))
product = 1
for i in range(1, input+1):
    product *=i

print(f"Factorial of {input} is {product}")