bottleType = (30,18,5,1)
def exhange(amt):
    global count
    result = {}
    for bottle in bottleType:
        num = amt // bottle
        result[bottle] = num
        count += num
        amt %= bottle
    return result    


count = 0
amount = int(input("輸入水量"))
ans = exhange(amount)
#30公升容量2個
#18公升容量0個
for k in ans:
    print(f"{k}公升容量{ans[k]}個")
print("count:",count)
#print(ans)
