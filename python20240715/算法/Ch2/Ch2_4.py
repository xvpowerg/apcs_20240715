a1 = int(input("首項"))#3
r = int(input("公比"))#2
n = int(input("項數"))#5

for i in range(n):
    print(a1*r**i,end=" ")

def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) * r
print()
print(getAn(n))
