# def res(n, a):
#     if n == 0:
#         return(False)
#     if n == 1:
#         return(True)
#     if a >= n:
#         return(a == n)
#     return res(n, a * 4)

# print(res(16, 4))

# def res(n):
#     left_to_right = True
#     remaining = n
#     step = 1
#     head = 1
    
#     while remaining > 1:
#         if left_to_right or remaining % 2 == 1:
#             head += step
        
#         remaining //= 2
#         step *= 2
#         left_to_right = not left_to_right
    
#     return head
# n = 10
# print(res(n))

# def unmarkedSumArray(nums, queries):
#         ans = []
#         s = sum(nums)
#         index = {}
#         p = nums.copy()
#         for i in queries:
#             if not index.get(i[0]):
#                 s -= nums[i[0]]
#                 index[i[0]] = 1
#                 p.pop(i[0])
                
#             loop = i[1]
#             while loop > 0:
#                 m = nums.index(min(p))
#                 if index.get(m):
#                     continue
#                 else:
#                     s -= nums[m]
#                     index[m] = i
#                     p.pop(m)
#                     loop -= 1
#             ans.append(s)
#         return ans
# nums = [1,2,2,1,2,3,1] 
# queries = [[1,2],[3,3],[4,2]]
# print(unmarkedSumArray(nums, queries))

def asteroidCollision(asteroids):
    ans = [] 
    for i in asteroids:  
        if not ans or i > 0 or ans[-1] < 0:
            ans.append(i)
        else:
            while ans and ans[-1] > 0 and ans[-1] < abs(i):
                ans.pop()  
            if not ans or ans[-1] < 0:
                ans.append(i) 
            elif ans[-1] == abs(i):
                ans.pop()  
    return ans


a = [10,2,-5]
print(asteroidCollision(a))
.


# ans = []
# for i in asteroids:
#     if i > 0 or not ans or ans[-1] < 0:
#         ans.append(i)
#     else:
#         while ans and ans[-1] > 0 and ans[-1] < abs(i):
#             ans.pop()
#         if not ans or ans[-1] < 0:
#             ans.append(i)
#         elif ans[-1] == abs(i):
#             ans.pop()
# return ans