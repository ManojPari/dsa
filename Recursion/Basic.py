def sequence(arr, i, s):
    if (i >= len(s)):
        print(arr)
        return
    arr.append(s[i])
    sequence(arr, i + 1, s)
    arr.pop()
    sequence(arr, i +1, s)

s = [1,2,3]
i = 0
arr = []
sequence(arr, i, s)