# Reverse a number.

input = int(input("Enter number for reversing: "))

rev =0
while(input>0):
    a1 = input%10
    rev = (rev*10) + a1
    input = input//10
print("Reverse value is:",rev)
