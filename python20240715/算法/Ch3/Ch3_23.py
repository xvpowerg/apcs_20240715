def square_root1(x):
    i = 1
    while i*i < x:
        i += 1
        if i * i == x:
            return i
    return i - 1

        
print(square_root1(9))
print(square_root1(2))
