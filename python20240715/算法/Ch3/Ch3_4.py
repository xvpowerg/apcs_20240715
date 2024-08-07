poly2 = [3, 2, 2, -3, 1, 1, 0]
x = 2
fx = 0
for j in range(poly2[0]):
    fx += poly2[2 * j + 1] * x ** poly2[2 * (j + 1)]
print(f"fx({x}):{fx}")
