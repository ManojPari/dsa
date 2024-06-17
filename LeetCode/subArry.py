def getLongestZeroSumSubarrayLength(arr):
    # Write your code here.
    d={}
    presum=0
    length=0
    for i in range(len(arr)):
        presum=presum+arr[i]
        if presum==0:
            length=max(length,i+1)
        rem=presum-0
        if rem in d:
            length=max(length,i-d[rem])
        if presum not in d:
            d[presum]=i 
    return length
# Sample Input 1:
arr1 = [0, 0, 1, -2, 0, 1]
print(getLongestZeroSumSubarrayLength(arr1))  # Output: 3

# Sample Input 2:
# Output: 0
