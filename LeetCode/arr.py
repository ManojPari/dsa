def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    lowerIndex = -1
    for index in range(len(nums) - 2, -1, -1):
        if nums[index] < nums[lowerIndex]:
            lowerIndex = index
            break
    if lowerIndex == -1:
        nums.reverse()
        return nums
    for index in range(len(nums) -1, lowerIndex, -1):
        if nums[lowerIndex] < nums[index]:
            nums[lowerIndex], nums[index] = nums[index], nums[lowerIndex]
            break
    nums[lowerIndex + 1:] = reversed(nums[lowerIndex+1:])
    return nums

nums = [2,3,1]
print(nextPermutation(nums))