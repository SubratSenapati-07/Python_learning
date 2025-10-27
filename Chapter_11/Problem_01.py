class Vector2D:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D Vector : {self.i}i + {self.j}j")

class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The 3D Vector: {self.i}i + {self.j}j + {self.k}k ")

a = Vector2D(4,8)
a.show()
b = Vector3D(1,2,3)
b.show()