matrix = [[1,2,3,54],
          [4,5,6,56],
          [7,8,9,23],
          [10,11,12,76]]

def spiralMatrix(grid):
    res = []
    m = len(grid)
    n = len(grid[0])

    #define boundaries
    row_start = 0
    row_end = m-1
    col_start = 0
    col_end = n-1

    while row_start<=row_end and col_start<=col_end:
        for i in range(col_start, col_end + 1):
            res.append(grid[row_start][i])
        row_start+=1

        for i in range(row_start, row_end+1):
            res.append(grid[i][col_end])
        col_end -=1

        if col_start<=col_end:
            for i in range(col_end, col_start-1, -1):
                res.append(grid[row_end][i])
        row_end-=1

        if row_start<=row_end:
            for i in range(row_end, row_start-1, -1):
                res.append(grid[i][col_start])
        col_start+=1

    return res


res = spiralMatrix(matrix)
print(res)