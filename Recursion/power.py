# def isPowerOfThree(n: int) -> bool:
    # if n < 3:
    #     return 
    # while n > 1:
    #     if n % 3 != 0:
    #         return 
    #     n //= 3
    # return True
# def myPow(x: int, n) -> bool:
#     if n == 0:
#         return 1

#     if n == -1:
#         return 1/x
    
#     if n == 1:
#         return x
#     return myPow(x*x, n//2) * myPow(x, n % 2)
# x  = 2
# n = 6
# print(myPow(x, n))

nums = [10, 5, 2, 6]
k = 100
temp = 1
ans = 0
i = 0
j = 0
while i < len(nums) and j < len(nums):
    temp *= nums[j]
    if temp < k and j != 0:
        ans += 1
    if nums[j] < k:
        ans += 1
    while (temp >= k or j == len(nums) - 1) and i < j:
        temp //= nums[i]
        if temp < k and j - i > 1:
            ans += 1
        i += 1
    j += 1
print(ans)