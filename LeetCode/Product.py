
nums = [2,-5,-2,-4,3]
maxiNum = nums[0]
tempNum = 1
for index in nums:
    if maxiNum <= index:
        maxiNum = index
    tempNum = tempNum * index
    if maxiNum < tempNum:
        maxiNum = tempNum
    
print(maxiNum)