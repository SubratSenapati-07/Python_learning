class Employee: # Parent class
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:     # Parent class
    language = "Python"
    def prLan(self):
        print(f"Out of all language is your language {self.language}")

class Programmer(Employee, Coder):  # Child class 
    company = "ITC InfoTECH"      # Employee , Coder ki property Programmer me aa gyi ha
    def showLan(self):
        print(f"The name is  and the company is {self.company}")



c = Programmer()

c.show()
c.prLan()
c.showLan()
