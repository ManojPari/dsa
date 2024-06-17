def nextGreaterElement(arr, n):
    # Write your code here.
    res = [-1] * n
    stack = []
    for i in range(len(arr)):

        while len(stack) != 0 and arr[stack[-1]] < arr[i]:
            res[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    for num in arr:
        while stack and arr[stack[-1]] < num:
            res[stack.pop()] = num
    return res

n = 5
arr = [1, 5, 3, 4, 2]
print(nextGreaterElement(arr, n))