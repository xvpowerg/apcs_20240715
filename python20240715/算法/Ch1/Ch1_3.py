def func2(x):
    print("Start:",x)
    if x <= 3:
        print(x)
        v = func2(x + 1) + func2(x + 2)
        print("v:",v)
    print("End:",x)
    return x

func2(1)
