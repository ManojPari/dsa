# def isPalindrome(x: int) -> bool:
#         if x < 0:
#             return False

#         reversed_num = 0
#         temp = x

#         while temp != 0:
#             digit = temp % 10
#             reversed_num = reversed_num * 10 + digit
#             temp //= 10

#         return reversed_num == x
# x = 3456
# result= isPalindrome(x)
# print(result)

def search(nums, target) -> int:
        length = len(nums)
        firstIndex = nums[0]
        array = nums[firstIndex:] + nums[:firstIndex] 
        first = 0
        end = length
        if length == 1:
            if nums[0] == target:
                return 0
            else:
                 return -1
        for i in range(length // 2):
            mid = (end + first) // 2
            if array[mid] == target:
                return (mid + firstIndex) % length
            elif array[mid] > target:
                end = mid - 1
            else:
                first = mid + 1
        return -1
nums = [1,3]
target = 3
res = search(nums, target)
print(res)