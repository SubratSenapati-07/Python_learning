class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def display_balance(self):
        print(f"Name: {self.name}\nCurrent Balance:{self.balance}")

    def deposite(self,amount):
        self.balance = self.balance + amount
        print(f"Deposited :{amount}")

    def withdrawn(self,amount):
        if(self.balance < amount):
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawn: {amount}")
a = input("ENter name:")
b = int(input("Enter balance:"))
c = int(input("Enter deposite balance:"))
d = int(input("Enter Withdrawn balance:"))

call = BankAccount(a,b)
call.display_balance()
call.deposite(c)
call.withdrawn(d)
call.display_balance()
