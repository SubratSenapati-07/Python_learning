class programmer:
    company = "Microsoft"

    def __init__(self,name , position , salary , address):
        
        self.name = name
        self.position = position
        self.salary = salary
        self.address = address

a = programmer("Saroj kumar","SuperVS","55k","Mp")
print(a.name,a.position ,a.salary ,a.address)

a = programmer("Rishi kumar","SuperVS","90K","Up")
print(a.name,a.position ,a.salary ,a.address)