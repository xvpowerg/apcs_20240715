#p1 來源
#p2 中繼
#p3 目標

def hanoi(n,p1,p2,p3):
    if n == 1:
        print(f"{n}套環從{p1}移到{p3}")
    else:
       hanoi(n-1,p1,p3,p2)#中繼目標交換(移動到中繼)
       print(f"{n}套環從{p1}移到{p3}")#剩下的大盤子往目標移動
       hanoi(n-1,p2,p1,p3)#中繼移動到目標

i = int(input("請輸入套環數:"))
hanoi(i,"A","B","C")
