nums=[[[33,45,67],[23,71,66],[55,38,66]],
      [[21,9,15],[38,69,18],[90,101,89]],
      [[50,32,72],[68,8,29],[88,24,9]],]    # 宣告三維陣列
max_value = nums[0][0][0]                   # 最大值設定為num陣列的第一個元素
min_value = nums[0][0][0]                   # 最小值設定為num陣列的第一個元素
for i in range(len(nums)):
    for j in range(len(nums[i])):
        for k in range(len(nums[i][j])):
            if(max_value<nums[i][j][k]):
                max_value=nums[i][j][k]      # 利用三層迴圈找出最大值
            if(min_value>nums[i][j][k]):
                min_value=nums[i][j][k]      # 利用三層迴圈找出最小值

print("最大值= %d" %max_value)
print("最小值= %d" %min_value)
