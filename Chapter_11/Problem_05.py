class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,add):
        result = Vector(self.x + add.x, self.y + add.y, self.z + add.z) 
        return result
    
    def __mul__(self,mul):
        result = (self.x * mul.x + self.y * mul.y + self.z * mul.z)
        return f"Multiplication: {result}"
    
    def __str__(self):
        return f"Vector ({self.x}, {self.y},{self.z})"
    
v1 = Vector(2,1,3)
v2 = Vector(1,3,4)
v3 = Vector(1,1,1)

print(v1 + v2)
print(v1 * v2)