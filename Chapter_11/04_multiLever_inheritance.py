# MultiLevel Ineritance
class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

print(Manager.a,Manager.b,Manager.c)  
# tenno class ke attributes print ho 
# jayenge kyuki Manager ke ander 
# programmer and Programmer ke ander Employee