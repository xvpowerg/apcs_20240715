def gcd(m,n):
    print(f"({m},{n})")
    if n == 0:
        return m
    else:
        x = gcd(n,m%n)
        print(f"end ({m},{n})")
        return x
    
n1 = 20
n2 = 14
ans = gcd(n1,n2)
print(ans)
