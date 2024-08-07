def sqrt_binary(x,min,max,pre=2):
    if (max - min) < 10 ** -pre:
        return (max + min) / 2
    mid = (min + max) / 2
    if mid*mid < x:
        return sqrt_binary(x,mid,max,pre)
    else:
        return sqrt_binary(x,min,mid,pre)
num = int(input("輸入整數"))
ans = sqrt_binary(num,0,num,2)
print(f"{ans:.2f}")
