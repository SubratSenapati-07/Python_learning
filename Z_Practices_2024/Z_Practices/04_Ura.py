a = int(input("Put Your mark: "))
b = int(input("Put Your mark: "))
c = int(input("Put Your mark: "))
d = int(input("Put Your mark: "))
e = int(input("Put Your mark: "))
t = (a+b+c+d+e) /5

if(t>=90):
    Print("A+")

elif(t>=80):
    print("A")

elif(t>=70):
    print("B")

elif(t>=60):
    print("C")

elif(t<60 and t>=0):
    print("Fail")


else:
    Print("Invalid value")
