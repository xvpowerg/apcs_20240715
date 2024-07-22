class Employee:
    def __init__(self,name,salary = 28000):
        self.name = name
        self.salary = salary
    
emp = Employee("Vivin",35000)
print(emp.name)
print(emp.salary)
emp2 = Employee("Ken")
print(emp2.name)
print(emp2.salary)
