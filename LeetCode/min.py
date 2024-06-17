def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    maxiNum = 0
    secMax = 0
    secMin = 0
    minNum = a[0]
    for i in a:
        if i > maxiNum:
            secMax = maxiNum
            maxiNum = i
        elif (i < maxiNum and i > secMax):
            secMax = i
        if i < minNum:
            secMin = minNum
            minNum = i
        elif i > secMin and i > minNum:
            secMin = i
    return secMax, secMin
n = 5
a = [1,2,3,4,5]
print(getSecondOrderElements(n,a))