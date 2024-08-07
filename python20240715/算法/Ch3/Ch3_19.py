def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

n = int(input("輸入一個數字"))
if is_prime(n):
    print(f"{n}是質數")
else:
    print(f"{n}不是質數")
        
p=[]

for j in range(2,n+1):
    if is_prime(j):
        p.append(j)
print(f"小於{n}的質數",p)        
