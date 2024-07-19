subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]

for i in range(0,len(subjs)):
    print(subjs[i],scores[i])
print("="*50)
#zip 打包
for n,s in zip(subjs,scores):
    print(n,s)

