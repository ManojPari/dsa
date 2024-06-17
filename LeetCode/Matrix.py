def numSpecial(left, right) -> int:
    pass
#         return sum(
#             sum(mat[i][col] for i in range(len(mat))) == 1
#             for col in [
#                 row.index(1)
#                 for row in mat
#                 if sum(row) == 1
#             ]
#         )
# mat = [[0,0,1,0],
#        [0,0,0,0],
#        [0,0,0,0],
#        [0,1,0,0]]
#         result = []
#         for i in range(left, right + 1):
#             status = True
#             num = i
#             while num:
#                 temp = num % 10
#                 if temp == 0:
#                     status = False
#                     break   
#                 if i % temp != 0 or temp == 0:
#                     status = False
#                 num //= 10
#             if status: result.append(i)
#         return result
# l = 1
# r = 22
# print(numSpecial(l, r))
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
prefix_sum = matrix.copy()
prefix_sum[0][0] = matrix[0][0]
        # first row value

for i in range(1, len(matrix[0])):
    prefix_sum[0][i] = matrix[0][i] + prefix_sum[0][i - 1]
# first col value


for i in range(1, len(matrix)):
    prefix_sum[i][0] = matrix[i][0] + prefix_sum[i-1][0]

# for all values 
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        prefix_sum[i][j] =  matrix[i][j] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]

# for j in range(3):
#     prefix_sum[0][j] = matrix[0][j] + (prefix_sum[0][j-1] if j > 0 else 0)

# # For j = 0 (leftmost column)
# for i in range(3):
#     prefix_sum[i][0] = matrix[i][0] +     (prefix_sum[i-1][0] if i > 0 else 0)

# # For the rest of the cells
# for i in range(1, len(matrix)):
#     for j in range(1, len(matrix[0])):
#         prefix_sum[i][j] = matrix[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

                                 

print(prefix_sum)