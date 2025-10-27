class Employee:
    salary = 5000
    increament = 500

    @property
    def salaryAfterIncreament(self):
        return (self.salary + self.salary * (self.increament/100))

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,salary):
        self.increament = ((salary/self.salary) -1)*100

z = Employee()
z.salaryAfterIncreament = 8000
print(z.increament)
