m = 3
n = 2

def uniquePath(i, j):
    if i == 0 or j == 0:
        return 1
    elif i < 0 or j < 0 or i == m or j == n:
        return 0
    else:
        return uniquePath(i, j - 1) + uniquePath(i - 1, j)
print(uniquePath(m-1, n-1))