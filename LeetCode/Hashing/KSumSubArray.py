def subarraySum(nums):
    dict = {0: -1}
    prefix_sum = 0
    ans = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if dict.get(prefix_sum):
            ans = max(ans, abs(dict.get(prefix_sum) - i)) 
        else:
            dict[prefix_sum] = i
    print(ans)
    return ans
nums = [1, 3, -1, 4, -4]
subarraySum(nums)
