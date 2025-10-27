class calclator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"Square: {self.n*self.n}")

    def cube(self):
        print(f"Cube: {self.n*self.n*self.n}")

    def sqRoot(self):
        print(f"Square Root: {round(self.n**0.5,2 )}")

inputing = int(input("Enter number:"))
a = calclator(inputing)
a.square()
a.cube()
a.sqRoot()