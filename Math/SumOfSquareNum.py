import math
c = 5
length = c // 2
for i in range(1, length + 1):
    temp = (c - (i ** 2)) ** .5
    if temp > c:
        print(False)
    if type(temp) == 'int':
        if (i ** 2 + temp ** 2) == c:
            print(True)
            break
print(False)