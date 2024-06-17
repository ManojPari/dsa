def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    ans = n
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x:
            ans =  mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

arr = [1,4,7,8,10]
x = 10
n = 5
print(upperBound(arr, x, n))