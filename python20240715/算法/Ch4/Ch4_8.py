def sqrt_binary(x,pre=2):
    min,max = 0,x
    while(max-min) > 10 **-pre:
        mid = (min + max)/ 2        
        if mid * mid > x:
            max = mid
        else:
            min = mid
        print(f"mid:{mid}")    
    return mid

num = int(input("輸入整數"))
ans = sqrt_binary(num)
print(f"{ans:.2f}")
