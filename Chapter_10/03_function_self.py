class employee:
    name = "Alone"
    lang = "Python"
    sal = 12000
    
    def getInfo(self): # Self parameter which passes name,lang,sal etc
        print(f"Name {self.name} having salary {self.sal} with {self.lang} language")

    @staticmethod # It is a method : means no any object passes through it.
    def greet():
        print("Good Day!")
# employee().getInfo()
# employee().greet()

z = employee()
# z.name = "Subrat"
z.getInfo("Subrat",12,"java")
z.greet()
