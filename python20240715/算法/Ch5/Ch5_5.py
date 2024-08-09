def showData(data_list):
    print('[', end='')
    for i in range(len(data_list)):
        print(data_list[i],end=' ')
    print(']')

def bin_search(data,score):
    low,high = 0,len(data) - 1
    mid = -1
    while not low > high:
        mid = (low + high) // 2
        if score > data[mid].gpa:
            print("往左找")
            high = mid - 1
        elif  score  <  data[mid].gpa:
            print("往右找")
            low = mid + 1
        else:
            return mid
    return -1    
#由高到低
class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __lt__(self,other):
        return self.gpa < other.gpa
    def __str__(self):
        return f"name:{self.name} age: {self.age} gpa:{self.gpa}"
data=[Student('Amy', 15, 4.2),
      Student('Bill', 16, 3.8),
      Student('Chris', 13, 4.0),
      Student('David', 19, 4.8),
      Student('Ed', 17, 2.6)]
data.sort(reverse= True)
showData(data)

while True:
    score = float(input("請輸入搜尋成績 輸入-1結束:"))
    if score == -1.0:
        break
    pos =  bin_search(data,score)
    if  pos == -1:
        print("找不到")
    else:
        print(f"位置是{pos}")

