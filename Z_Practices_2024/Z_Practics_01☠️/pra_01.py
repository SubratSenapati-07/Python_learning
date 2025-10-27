def fact():
    n = int(input("Enter here:"))
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial*i
    print("factorial:",factorial)

fact()