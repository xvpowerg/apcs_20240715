a1 = int(input("首項"))#1
d = int(input("公差"))#2
n = int(input("項數"))#3

sum1 = 0
for i in range(n):
    ai = a1 + i * d
    sum1 += ai
    print(ai,end = " ")
print("=",end="")    
print(sum1)    


def getAn(n):
    if n ==1:
        return a1
    else:
        return getAn(n-1) + d
    
def getSn(n):
    if n == 1:
        return a1
    else:
       an = getAn(n)
       return getSn(n-1) + an
print("=================")    
print(getSn(n))    
