def c2f(c):
    f = 9 / 5 * c + 32
    return f
inF = float(input("請輸入攝氏溫度:"))

ans = c2f(inF)
print(f"{ans:.2f}")
