class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name:{self.name} age:{self.age}"
    def __lt__(self,other):
        return self.age < other.age
#定義一個函數稱為foreachList 可以輸出所List的Person
def  foreachList(personList):
    for v in personList:
        print(v)
    print("======================")    
p1 = Person("Ken",15)
p2 = Person("Iris",17)
p3 = Person("Joy",11)
p4 = Person("Vivin",18)
p5 = Person("Gigi",12)
print(p1)#name: Ken age: 15
print(p3 < p1)#True
print(p4 < p5)#False

personList = []
personList.append(p1)
personList.append(p2)
personList.append(p3)
personList.append(p4)
personList.append(p5)

foreachList(personList)
newList = sorted(personList,reverse=True)
foreachList(newList)

personList.sort(reverse=True)
foreachList(personList)
