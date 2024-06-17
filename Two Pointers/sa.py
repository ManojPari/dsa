def merge(first, second, count):
    l = 0
    r = 0
    merged = []
    while l < len(first) and r < len(second):
        if first[l] > 2 * second[r]:
            count[0] += len(first) - l  # Increment count by the number of elements remaining in 'first'
            r += 1
        else:
            l += 1
    l = 0
    r = 0
    while l < len(first) and r < len(second):
        if first[l] < second[r]:
            merged.append(first[l])
            l += 1
        else:
            merged.append(second[r])
            r += 1
    merged.extend(first[l:])
    merged.extend(second[r:])
    return merged
def recursive(l, r, nums, count):
    if (l == r):
        return [nums[l]]
    mid = (l + r) // 2
    first = recursive(l, mid, nums, count)
    second = recursive(mid+1, r, nums, count)
    
    return merge(first, second, count)
def reversePairs(nums) -> int:
    count = [0]
    l = 0 
    r = len(nums) - 1
    recursive(l, r, nums, count)
    return count
    
nums = [1,3,2,3,1]
print(reversePairs(nums))
# print(count[0])

# def merge(first, second, count):
#     l = 0
#     r = 0
#     merged = []
#     while l < len(first) and r < len(second):
#         if first[l] > second[r]:
#             count[0] += len(second) - r
#             merged.append(first[l])
#             l += 1
#         else:
#             merged.append(second[r])
#             r += 1
#     merged.extend(first[l:])
#     merged.extend(second[r:])
#     return merged

# def recursive(l, r, nums, count):
#     if l == r:
#         return [nums[l]]
#     mid = (l + r) // 2
#     first = recursive(l, mid, nums, count)
#     second = recursive(mid + 1, r, nums, count)
#     return merge(first, second, count)

# def reversePairs(nums) -> int:
#     count = [0]  # Using a list to pass count by reference
#     l = 0 
#     r = len(nums) - 1
#     recursive(l, r, nums, count)
#     return count[0]

# nums = [1,3,2,3,1]
# print(reversePairs(nums))  # Output: 2
