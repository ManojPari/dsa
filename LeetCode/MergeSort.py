def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while (left <= mid and right <= high):
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    print(temp)
    for i in range(len(temp)):
        arr[low + i] = temp[i]

def mergesort(arr, low, high):
    if (low >= high): return
    mid = (low + high) // 2
    mergesort(arr, low, mid)
    mergesort(arr, mid+1, high)
    merge(arr, low, mid, high)

def mergeSort(arr):
    # Write Your Code Here
    mergesort(arr, 0, (len(arr) - 1))
arr = [9,3,6,2,0]
mergeSort(arr)
print(arr)