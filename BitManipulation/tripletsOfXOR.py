
arr = [2,3,1,6,7]
n = len(arr)
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] ^ arr[i]

count = 0
for i in range(n):
    for k in range(i + 1, n):
        print(prefix[i], prefix[k + 1])
        if prefix[i] == prefix[k + 1]:
            count += (k - i)

print(count)