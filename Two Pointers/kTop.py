


# from collections import Counter
# nums = [1,1,1,2,2,3]
# k = 2

# result = Counter(nums)
# ans = [[] for i in range(len(nums) + 1)]
# for key, value in result.items():
#         ans[value].append(key)
# result = []
# for i in range(len(ans) - 1, 0, -1):
#     for j in ans[i]:
#         result.append(j)
#         if len(result) == k:
#
#              print(result)
# count  = 0
# n = 10
# for i in range(2, n):
#     flag = True
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False             
#     if flag:
#         count += 1
# print(count)

class FourDivisors:
    def __init__(self, arr):
        self.arr = arr
    def divisor(self, n):
        count = 0
        sums = 0
        # print(/)
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                count += 1
                sums += i
                if i != n // i:
                    sums += n // i
                    count += 1
                if count > 4:
                    return 0
        return sums if count == 4 else 0

    def solve(self):
        ans = 0
        for i in self.arr:
            ans = self.divisor(i)
        return ans
n = [21,4,7]
a = FourDivisors(n)
a.solve()

