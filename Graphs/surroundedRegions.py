"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Sol: BFS/DFS to get all the "O" that are touching the boundaries, then all "O"s which can be reached from these Os, flip them to something else.
"""
from collections import deque
def solve(board):
    m, n = len(board), len(board[0])
    queue = deque()

    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                if board[i][j] == "O":
                    board[i][j] = "N"
                    queue.append((i, j))


    while queue:
        x, y = queue.popleft()

        row, col = [-1,0,0,1], [0,-1,1,0]
        for k in range(4):
            nr, nc = x + row[k], y + col[k]

            if 0<=nr<m and 0<=nc<n and board[nr][nc] == "O":
                board[nr][nc] = "N"
                queue.append((nr, nc))

    for i in range(m):
        for j in range(n):
            if board[i][j] == "N":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"

    return board


board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
    ]
res = solve(board)
print(res)