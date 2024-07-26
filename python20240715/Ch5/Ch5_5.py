class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print("name:",self.name,"age:",self.age)
p1 = Person("Lucy",10)
p2 = Person("Ken",15)
p1.printInfo()
p2.printInfo()
