def func2(x):
    print("Start:",x)
    if x <= 4:
        print(x)
        v = func2(x + 1)
        print("v:",v)
    print("End:",x)
    return x

endV = func2(1)
print("endV:",endV)
