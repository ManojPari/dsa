pairs = []
i = 0
k = 2
nums1 = [1,1,2]
nums2  = [1,2,3]
pairs = []
i = 0
j = 0
while (len(pairs) < k and i < len(nums1) and j < len(nums2)):
    pairs.append([nums1[i], nums2[j]])
    if i < len(nums1) and j < len(nums2) and nums1[i + 1] < nums2[j+1]:
        i += 1
    else:
        j += 1 
print(pairs)