class Employee: # Base Class / Parent Class
    company = "ITC"
    def show(self):
        
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC InfoTech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
 
class Programmer(Employee):   # Derived Class/ Child Class/ Inherited Class 
    company = "ITC InfoTech"  # EK baar derive class banakr parent class ko dal dene se parent class ke saree method,attributes derive class me aa jayenge / agr uska alawa or kuch attribute ya method use krna ha toh iss line me add kr dena hai
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
a = Employee()
b = Programmer()
print(a.company ,b.company)