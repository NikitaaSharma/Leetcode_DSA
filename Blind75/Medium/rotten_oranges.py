"""
link: https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

"""

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

from collections import deque
def rottenMinutes(grid):
    m, n = len(grid), len(grid[0])

    rotten_oranges = deque()
    minutes_passed = 0
    fresh_oranges = 0

    for row in range(m):
        for col in range(n):
            # add all the rotten oranges in the queue to check
            if grid[row][col] == 2:
                rotten_oranges.append((row, col))
            elif grid[row][col] == 1:
                fresh_oranges +=1

    row = [-1,0,0,1]
    col = [0,-1,1,0]

    # we need to keep going till all rotten oranges are done and there are no fresh oranges left
    while rotten_oranges and fresh_oranges:
        minutes_passed += 1

        for _ in range(len(rotten_oranges)):
            i, j = rotten_oranges.popleft()
            for k in range(4):
                nr, nc = i + row[k], j + col[k]
                if 0 <= nr < m and 0 <= nc < n  and grid[nr][nc] != 0 and grid[nr][nc] != 2:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append((nr, nc))


    return minutes_passed if fresh_oranges == 0 else -1


mins = rottenMinutes(grid)
print(f'All oranges will turn rotten in {mins} minutes')