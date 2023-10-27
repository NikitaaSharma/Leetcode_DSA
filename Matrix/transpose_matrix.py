matrix = [[5,4,7],
          [1,3,8],
          [2,9,6]]

for i in matrix:
    for j in i:
        print(j, end=" ")

    print(" ")

    
def transposeMatrix(grid):
    rows = len(grid)
    cols = len(grid[0])

    res = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            res[j][i] = grid[i][j]

    return res

res = transposeMatrix(matrix)
for i in res:
    for j in i:
        print(j, end=" ")

    print(" ")