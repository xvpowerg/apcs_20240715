def myLog(a,b,pre=6):
    step = 1
    ans = step
    while step >= 10**-pre:
        while b ** ans < a:
            ans += step
            if b ** ans == a:
                return ans
        ans -= step
        step /= 10
    return ans    

a = int(input("輸入數值"))#9
b = int(input("輸入基數"))#2
ans = myLog(a,b,2)
print(f"{a}以{b}為底的對數:{ans:.6f}")
