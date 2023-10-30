matrix= [[0,1,2,0],
         [2,3,4,5],
         [6,7,8,9]]

print(matrix)
#BRUTE Force

# create 2 new array, zeroes_row = [False], zeroes_col = [False], now start iterating the matrix, if there is a 0, mark the
# row and col as True. Iterate again, wherever there is True, insert a 0
# zeroes_row = [False] * len(matrix)
# zeroes_col = [False] * len(matrix[0])

# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         if matrix[row][col] == 0:
#             zeroes_row[row] = True
#             zeroes_col[col] = True

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if zeroes_row[i] or zeroes_col[j]:
#             matrix[i][j] = 0
# print(matrix)


#OPTIMAL Solution
# take matrix's 1st row and 1st column as an array to mark, now to not overlap matrix[0][0] twice, create another variable col0 to store 1
# start iterating the matrix, if a 0 is found in 0th column, update the new var to 0 else, update the matrix[0][col] as 0
# similarly, as soon as a 0 is encounered, update matrix[row][0] and matrix[0][col] as 0
# Now start updating 0's leaving the first row and col, so start from (1,1), if matrix[row][col] !=0 then only proceed
# Now update the horizontal row first after checking if matrix[0][0] is 0 or not
# lastly update the vertical column after checking if col0 is 0 or not

m = len(matrix)
n = len(matrix[0])

col0 = 1

for row in range(m):
    for col in range(n):
        if matrix[row][col] == 0:
            matrix[row][0] = 0
            if col != 0:
                matrix[0][col] = 0
            else:
                col0 = 0

#start from 1,1 so as to NOT touch 0th row and 0th col:
for row in range(1, m):
    for col in range(1, n):
        if matrix[row][col] != 0:
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

# Now check the horizontal row first
if matrix[0][0] == 0:
    for col in range(n):
        matrix[0][col] = 0


# lastly, check vertical col
if col0 == 0:
    for row in range(m):
        matrix[row][0] = 0

print(matrix)