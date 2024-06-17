def minPatches(nums, n):
    miss = 1
    i = 0
    patches = 0
    
    while miss <= n:
        if i < len(nums) and nums[i] <= miss:
            miss += nums[i]
            i += 1
        else:
            miss += miss
            patches += 1
            
    return patches

# Example usage:
nums = [1, 3]
n = 6
print(minPatches(nums, n))  # Output: 1

nums = [1, 5, 10]
n = 20
print(minPatches(nums, n))  # Output: 2

nums = [1, 2, 2]
n = 5
print(minPatches(nums, n))  # Output: 0
