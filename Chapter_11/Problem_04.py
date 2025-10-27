class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self0,self1):
        return f"Complex Number: {Complex(self0.r + self1.r,self0.i + self1.i)}"
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
# a1 = int(input("Enter number:"))
# a2 = int(input("Enter number:"))
# b1 = int(input("Enter number:"))
# b2 = int(input("Enter number:"))
z = Complex(1, 2)
z1 = Complex(3, 2)
# q = Complex(1, 1)
print(z+z1)