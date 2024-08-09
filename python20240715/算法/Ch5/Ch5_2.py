H = int(input('輸入樹高: '))
D = int(input('白天上升公尺數: '))
N = int(input('晚上下降公尺數: '))

height = D
days = 1
while height < H:
    height -= N
    height += D
    days += 1

print('蝸牛第%d天可爬到樹頂' % days)
