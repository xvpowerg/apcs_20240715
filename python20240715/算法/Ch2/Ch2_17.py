num = input("請輸入數值")
num =  map(int,num.split())
arr = list(num)

for k in range(len(arr) - 1):
    if arr[k] * arr[k + 1] >= 0:
        print("不是正負交錯")
        break
else:
    print("是正負交錯")
