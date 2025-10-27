class employee:
    name = "ALone"
    lang = "Python"
    sal = 12000

    def __init__(self): # Dunder method which automatically called.
        print("Here,I'm creating an object")

    def getInfo(self):
        print(f"{self.name} ka salary {self.sal}₹ ha")

    def greet():
        print("Good Day!")


a = employee()
a.getInfo() # DUnder method is calling during ,jab class ko karenge tab tab 

b = employee() 