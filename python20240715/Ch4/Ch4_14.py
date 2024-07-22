strList = ["1","3","6","7"]
'''
intList = []
for v in strList:
    intList.append(int(v))
'''
mapObj = map(int,strList)   
intList = list(mapObj)
total = 0
for i in intList:
    total += i
print(total)
