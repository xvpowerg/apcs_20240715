name = "小民"
age = 12
#小民今年12歲
msg = name+"今年"+str(age)+"歲"
#%d 輸出無小數點的
#%f 輸出有小數點的
#%s 輸出字串
msg2 = "%s今年%d歲"%(name,age)
msg3 = f"{name}今年{age}歲"
print(msg)
print(msg2)
print(msg3)

pi = 3.1415926
print(f"PI:{pi:.2f}")
