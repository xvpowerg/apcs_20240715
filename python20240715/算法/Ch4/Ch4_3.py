minValue = int(input("輸入下限"))
maxValue = int(input("輸入上限")) + 1
for i in range(minValue,maxValue):
    for j in range(i,maxValue):
        for k in range(j,maxValue):
            if i**2 + j**2 == k **2:
                print(f"({i},{j},{k})")
                
