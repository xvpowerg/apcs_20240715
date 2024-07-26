list1 = ["A","B","C"]
print(list1[0])
print(list1[-1])

empList = []
empList.append("A")
empList.append("B")
empList.append("C")
print(empList)
empList.insert(1,"HH")
print(empList)
empList.insert(-1,"KK")
print(empList)


list2 = ["Q","W","E"]
list3 = ["V","B","N"]
list2.extend(list3)#修改list2
print(list2)

list2 = ["Q","W","E"]
list3 = ["V","B","N"]
newList = list2 + list3#生成新的List
print(newList)

