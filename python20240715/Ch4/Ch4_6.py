def f1(x,y,*z):
    print(x,y,z)
def f2(x,y,**z):
    print(x,y,z)
f1(1,2,3,4,5,6,7,8,9,10,11,12)
f2(1,2,k1 = 3,k2 = 4)
