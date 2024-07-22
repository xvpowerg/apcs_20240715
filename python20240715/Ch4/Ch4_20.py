def testAge(age):
    if age < 0 or age > 200:
        #print("錯的年齡")
        raise Exception("錯的年齡")
    else:
        print(age) 

#0~200 小於0 或大於200顯示錯的年齡
#其他就正常顯示年齡    
testAge(900)
print(".......")
