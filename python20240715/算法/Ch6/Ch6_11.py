import random
nums = random.sample(range(1,100),10)
print(nums)
nSum3 = 0

for i in range(3):
    maxNum = 0
    for j in range(len(nums)):
        if nums[j] > maxNum:
            maxNum = nums[j]
    nSum3 += maxNum
    nums.remove(maxNum)
print(nSum3)
