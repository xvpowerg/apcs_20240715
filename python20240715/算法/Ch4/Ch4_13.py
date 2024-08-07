def showdata(data_list):
    print('[', end='')
    for i in range(len(data_list)):
        print(data_list[i],end=' ')
    print(']')

class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __lt__(self,other):
        return self.age < other.age
    def __str__(self):
        return f"{self.name}:{self.age}:{self.gpa}"
    
st1 = Student("Amy",15,4.2)
st2 = Student("Bill",16,3.8)
st3 = Student("Iris",13,4.8)
st4 = Student("Ken",19,4.0)
st5 = Student("Lucy",17,2.6)
stList = [st1,st2,st3,st4,st5]
showdata(stList) 
n = len(stList)
for i in range(n - 1):
    minId = i
    for j in range(i + 1,n):
        if stList[j] <  stList[minId]:
            minId = j
    stList[i],stList[minId] = stList[minId], stList[i]
showdata(stList)  
#print(st1 < st2)
#print(st1)
#print(st2)
