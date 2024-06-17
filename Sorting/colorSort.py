nums = [1,0,2]

zero = 0
two = len(nums) - 1
for i in range(len(nums)):
    if nums[i] == 0:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1
    elif nums[i] == 2 and i < two:
        nums[i], nums[two] = nums[two], nums[i]
        two -= 1
print(nums)