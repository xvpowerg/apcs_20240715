def square_root2(x,pre=2):
    step =1
    r=step
    while step >= 10**-pre:
        while r*r<x:
            r+=step
            if r*r==x:
                return r
        r-=step
        step/=10
    return r
n=int(input(""))
print(f"{n}的平方根{square_root2(n):.2f}")
