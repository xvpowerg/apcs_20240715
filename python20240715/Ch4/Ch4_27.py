class Employee:
    def __init__(self,name,salary = 28000):
        self.name = name
        self.salary = salary
    def printInfo(self):
        print("name:",self.name," salary:",self.salary)
    
emp = Employee("Vivin",35000)
emp2 = Employee("Ken")

emp.printInfo()
emp2.printInfo()
