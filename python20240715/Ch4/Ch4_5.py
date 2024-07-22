def  w_sum(c,e=80,m=60):
    return c + e*2+m*3

x1 = w_sum(100,20,30)
print(x1)
x2 = w_sum(100,10)
print(x2)
x3 = w_sum(100,m = 20)
print(x3)
x4 = w_sum(e = 5,c = 3,m = 2)
print(x4)
#x5 = w_sum(e=5,3)#因為使用了具名指定所以其他參數也必須具名
#print(x5)
