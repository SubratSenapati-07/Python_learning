class Vector:
    def __init__(self,list):
        self.list = list

    def __len__(self):
        return len(self.list)
    

v = Vector([1,5,3])
print(len(v))