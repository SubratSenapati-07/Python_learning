# Problem 01

def greatest():
    a = int(input("Enter number here:"))
    b = int(input("Enter number here:"))
    c = int(input("Enter number here:"))
    if(a>b and b>c ):
        print(f"{a} is greatest")

    elif(b>a and b>c):
        print(f"{b} is greatest")

    else:
        print(f"{c} is greatest")

greatest()