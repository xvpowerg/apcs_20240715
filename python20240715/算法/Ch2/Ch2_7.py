n = int(input("輸入n"))
sum1 = 0
for i in range(2,n+1):
    ai = (i - 1) * i
    sum1 += ai
    print(f"{i-1}*{i}",end=" ")
print("=",sum1)    
    
def getSum(n):
    if n == 1 or n == 0:
        return 0
    else:
        return getSum(n - 1) + (n-1) * n
ans = getSum(n)
print(ans)
