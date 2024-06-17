
# # def s(arr):
#     length = len(arr)
#     max_left = [0] * length
#     min_right = [float('inf')] * length

#     max_value = float('-inf')
#     for i in range(length):
#         max_value = max(arr[i], max_value)
#         max_left[i] = max_value
    
#     min_value = float('inf')
#     for i in range(length -1, -1, -1):
#         min_value = min(arr[i], min_value)
#         min_right[i] = min_value
#     print(min_right)

#     chunks = 1
#     for i in range(1, length):
#         if max_left[i] <= min_right[i]:
#             chunks += 1
#     return chunks

# arr = [5,4,3,2,1]
import random


print(random(3))