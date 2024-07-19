import random
answer = random.randint(1,100)#產生亂數1~100的數字
myMin,myMax = 1,100
guess = int(input(f"猜數字({myMin}~{myMax}):"))
while True:
    if guess == answer:
        print("答對!")
        break
    elif guess > answer:
        myMax = guess
    elif  guess <  answer:
       myMin =  guess
    guess = int(input(f"再猜一次:({myMin}~{myMax}):"))
print("完成遊戲")    
