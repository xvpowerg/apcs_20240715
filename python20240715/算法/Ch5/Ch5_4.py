import random

def bin_search(data,val):
    low,high = 0,len(data) - 1
    mid = -1
    while not low > high:
                mid = (low + high) // 2
                if val < data[mid]:
                    print("在往左找")
                    high = mid - 1
                elif val > data[mid]:    
                    print("在往右找")
                    low = mid + 1
                else:
                    return mid
    return -1

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
data.sort()

while True:
    val =int( input("請輸入(1-100) -1離開"))
    if val == -1:
        break
    pos = bin_search(data,val)
    if pos == -1:
       print("找不到")
    else:
       print(f"找到了位置是{pos + 1}")
print('資料內容：')
showData(data)        
