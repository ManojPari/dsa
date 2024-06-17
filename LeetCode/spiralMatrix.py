
# def setZeroes(matrix):
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         cal0 = 1
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     # first row
#                     if j != 0: 
#                         matrix[0][j] = 0
#                     else:
#                         cal0 = 0
#                     # first col
#                     matrix[i][0] = 0
#         for i in range(1, len(matrix)):

#             for j in range(1, len(matrix[i])):
#                 if matrix[0][j] == 0 or matrix[i][0] == 0:
#                     matrix[i][j] = 0

#         if cal0 == 0:
#             for i in range(len(matrix[0])):
#                 matrix[0][i] = 0

#         if matrix[0][0] == 0:
#             for i in range(len(matrix)):
#                 matrix[i][0] = 0
#         return matrix
# matrix = [[0,0,3]]
# print(setZeroes(matrix))


def generateMatrix(n):
        spiralMatrix = []
        for i in range(n):
            spiralMatrix.append([1] * n)
        left, right = 0, n-1
        top, bottom = 0, n-1
        num = 1
        while left <= right and top <= bottom:
            # top row
            for i in range(left, right +1):
                spiralMatrix[top][i] = num
                num += 1
            top += 1

            # top to bottom
            for i in range(top, bottom+1):
                spiralMatrix[i][right] = num 
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                spiralMatrix[bottom][i] = num 
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                spiralMatrix[i][left] = num 
                num += 1
            left += 1
        return spiralMatrix

print(generateMatrix(3))