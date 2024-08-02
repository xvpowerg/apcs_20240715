x = [5,15,25,35,45]
for data in x:
    print(data)


for data in x:
    print(data,end= ",")
print()
print("=================")
str1 = ""
for data in x:
    str1+=str(data)+","
print(str1[0:-1])
print("=================")
x.insert(2,100)
print(x)
x.append(200)
print(x)
x[2] = 20
print(x)
n = x.pop()
print(x)
print(n)
n = x.pop()
print(x)
print(n)
n = x.pop(2)
print(x)
print(n)
