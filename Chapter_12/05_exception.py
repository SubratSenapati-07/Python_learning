try:
    a = int(input("Hey! Enter a number:"))
    print(a)

except ValueError as v:
    print(v)
    print("Hello")
    
    
except Exception as prnt: # it is use to reduce the documentation
    print(prnt)  # Solve the program_Crash Problem.
print("Thank You")