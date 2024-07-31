def func1(x):
    print("Start:",x)
    if x <= 4:
        print(x)
        func1(x+1)
    print("End:",x)    
        
func1(1)

