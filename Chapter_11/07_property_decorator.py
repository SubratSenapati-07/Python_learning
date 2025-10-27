class Employee:
    a = 1 
    @classmethod # It is a decorator.
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property  # It is a decorator
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


z = Employee()
z.a = 50  

z.name = "Subrat Senapati"
print(z.fname,z.lname)
z.show() 
 
# The Total Process is called Abstraction or encapsulation.☠️  