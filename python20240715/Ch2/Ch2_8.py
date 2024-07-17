ch = int(input("國文"))
ma = int(input("數學"))
en = int(input("英文"))

total = ch + ma + en

print("總成績:",total)
print(f"平均成績:{total/3:.2f}")
print(round(total/3,2))

