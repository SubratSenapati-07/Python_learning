class employee:
    name = "ALone"
    lang = "Python"
    sal = 12000

    def __init__(self,name,lang,sal): # Dunder method which automatically called.
        self.name = name
        self.lang = lang
        self.sal = sal
        print("Here,I'm creating an object")

    def getInfo(self):
        print(f"{self.name} ka salary {self.sal}₹ ha")

    def greet():
        print("Good Day!")


a = employee("Subrat Senapati","HTML",15000) # BY the help of __init__
# a.name = "Subrat Senapati"
print(a.name, a.lang , a.sal)




