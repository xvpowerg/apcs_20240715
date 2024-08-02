a1 = int(input("首項"))#1
d = int(input("公差"))#2
n = int(input("項數"))#3
#3
# 2

#1 3 5
for i in range(n):
    print(a1+i*d,end = " ")

def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n - 1) + d
print()    
print(getAn(n))
