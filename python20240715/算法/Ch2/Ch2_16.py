num = input("請輸入數值")
num =  map(int,num.split())
arr = list(num)
for j in range(len(arr) - 1):
    if arr[j] >= arr[j+1]:
        print("不是遞增陣列")
        break
else:
    print("是遞增陣列")
