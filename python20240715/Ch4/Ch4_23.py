try:
    for i in range(1,5):
        for x in range(1,4):
            print(i,"_",x,end = " ")
            if i == 2:
                raise Exception()
        print()
except:
    pass
