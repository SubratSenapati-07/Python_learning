class Employee: # Parent Class or Base Class  
    company = "ITC"
    def show(self):
        
        print(f"The name is {self.name} and the salary is {self.salary}")

 
class Programmer(Employee):  # Child Class or Derived Class
    company = "ITC InfoTech" 
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
a = Employee()
b = Programmer()
print(a.company ,b.company)