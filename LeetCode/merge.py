def sortedArray(a, b):
    result = []
    left = 0
    right = 0
    leftLenght = len(a)
    rightLenght = len(b)
    while left < leftLenght and right < rightLenght:
        if a[left] < b[right]:
            if len(result) == 0 or result[-1] != a[left]:
                result.append(a[left])
            left += 1
        else:
            if len(result) == 0 or result[-1] != a[right]:
                result.append(b[right])
            right += 1
    while left < leftLenght:
        if len(result) == 0 or result[-1] != a[left]:
            result.append(a[left])
        left += 1
    while right < rightLenght:
        if len(result) == 0 or result[-1] != [right]:
            result.append(b[right])
        right += 1
    return result
a = [1,2,3,3]
b= [2,2,4]
print(sortedArray(a, b))
