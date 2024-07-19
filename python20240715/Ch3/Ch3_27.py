v = int(input("離開的數字"))
for i in range(1,6):
    print(i,end=" ")
    if i == v:
       print("找到離開的數字")
       break
else:
   print("沒找到離開的數字") 
#else 如果不是break 離開的時候運行

#由break離開迴圈 顯示
#找到離開的數字

