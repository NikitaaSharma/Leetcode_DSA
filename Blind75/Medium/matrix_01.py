"""
Return a new matrix with the blocks updated to represent the distance from the nearest 0

input = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

output = [
    [0,0,0],
    [0,1,0],
    [1,2,1]
]
"""
from collections import deque
mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1],
    [1,1,1]
]


def mat_01(mat):
    if not mat:
        return []

    m, n = len(mat), len(mat[0])

    distances = [[float("inf") for _ in range(n)] for _ in range(m)]

    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                distances[i][j] = 0
                queue.append((i,j))

    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    while queue:
        i, j = queue.popleft()

        for k in range(4):
            nr = i + row[k]
            nc = j + col[k]

            if 0 <= nr < m and 0 <= nc < n and distances[nr][nc] > distances[i][j]+1:
                distances[nr][nc] = distances[i][j] + 1
                queue.append((nr, nc))

    return distances


res = mat_01(mat)
for i in res:
    for j in i:
        print(j, end=" ")
    print(" ")



