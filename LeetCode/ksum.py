from collections import defaultdict

def subarraySum(nums, k):
    dict = {0: -1}
    prefix_sum = 0
    ans = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if dict.__contains__(prefix_sum):
            ans = max(ans, i - dict.get(nums[i])) + 1
        else:
            dict[prefix_sum] = i
    print(ans)
nums = [1,1,1]
k = 2
subarraySum(nums, k)