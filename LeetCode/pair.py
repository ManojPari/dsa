
# def pairSum(arr, s):
#     result = {}
#     res = []
#     for i in range(len(arr)):
#         result[s - arr[i]] = i
#     for i in range(len(arr)):
#         if result.get(arr[i]):
#             res.append([arr[i], arr[result.get(arr[i])]])
#     return res
# s = 5
# arr = [1,2,3,4,5]
# print(pairSum(arr, s))


# def longestSuccessiveElements(a) -> int:
#     # Write your code here.
#     a.sort()
#     maxCount = 0
#     count = 1
#     for i in range(1, len(a)):
#         if  a[i] - a[i - 1] == 0: continue
#         if a[i] - a[i - 1] == 1:
#             count += 1
#             maxCount = max(maxCount, count)
#         else:
#             count = 1
#     return maxCount
# a = [15,6,2,1,16,4,2,29,9,12,8,5,14,21,8,12,17,16,6,26,3]
# print(longestSuccessiveElements(a))
from math import floor


result = floor(1/3)
print(result)