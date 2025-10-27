class Animals:
    pass
    # def bark():
    #     print("This is Animal class i.e. Parent class")

class pets(Animals):
    pass
class Dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow")

a = Dog()
a.bark()
