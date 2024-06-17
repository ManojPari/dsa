
# from typing import *

# def nCr(n, r):
#     res = 1

#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)
#     return int(res)

# def pascalTriangle(n : int) -> List[List[int]]:
#     ans = []

#     #Store the entire pascal's triangle:
#     for row in range(1, n+1):
#         tempLst = [] # temporary list
#         for col in range(1, row+1):
#             tempLst.append(nCr(row - 1, col - 1))
#         ans.append(tempLst)
#     return ans

# if __name__ == '__main__':
#     n = 5
#     ans = pascalTriangle(n)
#     for it in ans:
#         for ele in it:
#             print(ele, end=" ")
#         print()



def generate(numRows: int):   
    ans = []
    for i in range(numRows):
        row = [1]*(1 + i)
        for j in range(1, i):
            row[j] = ans[i - 1][j - 1] + ans[i -1][j]
        ans.append(row)
    return ans  
            
if __name__ == '__main__':
    n = 5
    ans = generate(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()

