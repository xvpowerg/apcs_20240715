a = [1,2,3]
b = [1,2,3]
c = a

print(a,id(a))
print(b,id(b))
print(c,id(c))
print(a is b)
print(a is c)

print(a is not c)
print(a is not b)
