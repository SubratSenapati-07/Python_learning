a1 = int(input("Enter no. 1: "))
a2 = int(input("Enter no. 2: "))
if(a2 == 0):
    raise ZeroDivisionError("Hey!not be division Posible")
else:
    print(f"The Division: {a1/a2}")