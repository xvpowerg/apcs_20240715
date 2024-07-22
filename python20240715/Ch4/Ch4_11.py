a = 5
def func():
    global a#說a是外部變數
    a = a + 1
    print("func(): a=",a)
print("a:",a)
func()
print("a:",a)
