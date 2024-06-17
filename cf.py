nums = [1, 2, 2]
count = 0
num = sorted(nums)
for i in range(1, len(num)):
    if num[i-1] >= num[i]:
        count += (num[i - 1] - num[i]) + 1
        num[i] = num[i - 1] + 1
print(count)