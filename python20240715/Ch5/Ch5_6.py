class Person:
    def __init__(self,name="empty",age = 10):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print("name:",self.name,"age:",self.age)
p1 = Person("Gigi",25)
p1.printInfo()
p2 = Person("Joy")
p2.printInfo()
p3 = Person()
p3.printInfo()#name:empy age: 10
