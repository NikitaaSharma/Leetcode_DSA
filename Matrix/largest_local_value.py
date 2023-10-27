grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]


def largestLocal(grid):
    n = len(grid)

    maxLocal = [[0] * (n-2) for _ in range(n-2)]

    for i in range(n-2):
        for j in range(n-2):
            maxLocal[i][j] = max(grid[x][y] for x in range(i,i+3) for y in range(j, j+3))

    return maxLocal

maxLocal = largestLocal(grid)

for i in maxLocal:
    for j in i:
        print(j, end=" ")

    print(" ")