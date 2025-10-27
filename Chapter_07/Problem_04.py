user = int(input("Enter number: "))

for i in range(2, user):
    if((user%i) == 0):
        print("Number is not Prime")
        break

    else:
        print("Number is Prime")