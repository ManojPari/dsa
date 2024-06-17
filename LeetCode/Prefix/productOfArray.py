def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products and store them in the result array
    prefix_product = 1
    for i in range(n):
        result[i] *= prefix_product
        prefix_product *= nums[i]
    
    # Calculate suffix products and accumulate them in the result array
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]
    
    return result

# Example usage:
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
