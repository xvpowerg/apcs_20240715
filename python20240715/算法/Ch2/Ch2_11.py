#myMax
#myMin
def myMax(scores):
    maxValue =  0
    for s in scores:
        if maxValue < s:
            maxValue = s
    return maxValue

def myMin(scores):
    minValue = 100
    for s in scores:
        if minValue > s:
            minValue = s
    return minValue
n = 3
scores = []
for i in range(n):
    s = int(input(f"請輸入第{i+1}筆成績"))
    scores.append(s) 
print(scores)
print(myMax(scores))
print(myMin(scores))
