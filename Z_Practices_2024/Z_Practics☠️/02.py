# Sum of digits of number.

x = int(input("Enter a Number: "))
a = 0

while(x>0):
    y= x % 10
    a += y
    x = x // 10
print("Sum of digits:",a)