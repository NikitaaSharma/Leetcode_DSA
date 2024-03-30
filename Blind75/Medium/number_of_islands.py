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
    ["1", "1", "0", "1", "1"]
]


def numIslands(grid):
    if not grid:
        return -1

    m, n = len(grid), len(grid[0])

    count = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and (i,j) not in visited:
                findIslandsBFS(i,j, grid, visited)
                count +=1

    return count

def findIslandsBFS(i,j, grid, visited):
    queue = deque()
    queue.append((i,j))
    visited.add((i,j))
    while queue:
        x, y = queue.popleft()

        row = [-1,0,0,1]
        col = [0,-1,1,0]

        for k in range(4):
            nr, nc = x + row[k], y + col[k]
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))

res = numIslands(grid)
print(f'no. of islands is {res}')