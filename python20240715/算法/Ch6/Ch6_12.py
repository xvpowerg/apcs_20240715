coinType = (50,10,5,1)
def exhange(amt):
    global count
    result = {}
    for coin in coinType:
        num = amt // coin
        result[coin] = num
        count += num
        amt %= coin
    return result    


count = 0
amount = int(input("輸入金額"))
ans = exhange(amount)
print("count:",count)
print(ans)
