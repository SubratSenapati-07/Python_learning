class Employee:
    a = 1 #Class Attribute
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

z = Employee()
z.a = 50  #intstance attribute
z.show() 
# Here, class atrribute ko show krne ke liye 
# @classmethod use krte hai taki instance
#  attribute print na ho.