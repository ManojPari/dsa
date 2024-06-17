arr = [1, 3, 4, 5, 7, 10]

def binarySearch(arr, start, end, target):
    mid = (start + end) // 2
    if arr[mid] != target and start == end:
        return False
    elif arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binarySearch(arr, start, mid - 1, target)
    else:
        return binarySearch(arr, mid + 1, end, target)
target = 1
print(binarySearch(arr, 0, len(arr) - 1, target))