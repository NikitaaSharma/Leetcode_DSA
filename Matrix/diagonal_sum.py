# Odd matrix
matrix = [[5,4,7],
          [1,3,8],
          [2,9,6]]

# Even matrix

# matrix_2 = [[1,1,1,1],
#             [1,1,1,1],
#             [1,1,1,1],
#             [1,1,1,1]]

# Find the sum of all diagonal elemets both primary and secondary

def diagonalSum(mat):
    n = len(mat)
    sum = 0
    for i in range(n):
        sum +=mat[i][i] + mat[i][n-i-1]

    if n%2!=0:
        sum -= mat[n//2][n//2]
    return sum

sum = diagonalSum(matrix)
for i in matrix:
    for j in i:
        print(j, end=" ")

    print(" ")
print(sum)