def countdown(n):
    if(n == 0):
        print("Countdown Over!")

        return 
    print(n)
    countdown(n - 1)

p = int(input("Enter number:"))
countdown(p)

p = int(input("Enter number:"))
countdown(p)

p = int(input("Enter number:"))
countdown(p)