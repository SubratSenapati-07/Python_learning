try:
    a = int(input("Enter Number a: "))
    b = int(input("Enter Number b: "))
    print(f"division : {a/b}")
except ZeroDivisionError as v:
    print("Infinite")