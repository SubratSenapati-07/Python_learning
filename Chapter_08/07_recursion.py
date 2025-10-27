def factorial(inp):
    if(inp==1 or inp==0):
        return 1
    else:
        return inp * factorial(inp-1)  #  a base condition ke basis pe chalta hai 
                                   #  or final result ko khudme i.e. function 
                                   #  me [ factorial(inp)]
                                   #  Store karega 
inp=int(input("Enter a number:"))
print("Factorial is:",factorial(inp))
