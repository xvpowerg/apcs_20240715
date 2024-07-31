def func1(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
def func2(n):
    if n == 1:
        return 1
    else:
        return func2(n-1) * n
    
ans = func1(5)
print(ans)
ans = func2(5)
print(ans)
