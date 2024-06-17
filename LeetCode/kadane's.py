
def maxSubArraySum(nums, size):
 
    maxiArr = -1
    tempSum = 0
    for index in range(0, len(nums)):
        tempSum = tempSum + nums[index]
        if (tempSum > maxiArr):
            maxiArr = tempSum

        if (tempSum < 0):
            tempSum = 0
    return tempSum
 
# Driver function to check the above function
 
 
a = [-2,1,-3,4,-1,2,1,-5,4]
result =  maxSubArraySum(a, len(a))
 
print("Maximum contiguous sum is", result)