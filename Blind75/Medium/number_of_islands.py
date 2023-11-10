"""
Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
from collections import deque


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def numIslands(grid):
    if not grid:
        return -1

    m, n = len(grid), len(grid[0])

    queue = deque()
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                queue.append((i,j))
                grid[i][j] = "0"
                findIslands(queue, grid)
                count +=1

    return count

def findIslands(queue, grid):
    while queue:
        x, y = queue.popleft()

        row = [-1,0,0,1]
        col = [0,-1,1,0]

        for k in range(4):
            nr, nc = x + row[k], y + col[k]
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == "1":
                queue.append((nr, nc))
                grid[nr][nc] = "0"

res = numIslands(grid)
print(f'no. of islands is {res}')