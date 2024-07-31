temp = {0:0,1:1}
def fib(n):
    if n == 0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def fib2(n):
    if n in temp:
        return temp[n]
    else:
         key1 = n - 1
         key2 = n - 2
        
         if  key1 in temp:
            v1 = temp[key1]
         else:
            v1 = fib2(key1)
            temp[key1] = v1
            
         if  key2 in temp:
            v2 = temp[key2]
         else:
            v2 = fib2(key2)
            temp[key2] = v2
    return v1 + v2
    
ans = fib2(40)
print(ans)
