# def trap(height):
#     left, right = 0 , len(height) - 1
#     maxLeft , maxRight = height[left] , height[right]
#     total = 0
#     while left < right:
#         if maxLeft > maxRight:
#             right -= 1
#             maxRight = max(maxLeft , height[right])
#             total += maxRight -height[right]
#         else:
#             left += 1
#             maxLeft = max(maxLeft, height[left])
#             total += maxLeft - height[left]
#     return total

# h = [4,2,0,3,2,5]
# print(trap(h))

from math import ceil


print((3//2))