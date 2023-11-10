from collections import deque

def findShorttestPath(mat, src, dest):
    i, j = src
    x, y = dest

    if not mat or mat[i][j] == 0 or mat[x][y] == 0 or len(mat) == 0:
        return -1

    m, n = len(mat), len(mat[0])

    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = deque()

    visited[i][j] = True
    queue.append((i, j, 0))

    min_dist = float("inf")

    while queue:
        (ii, jj, dist) = queue.popleft()

        if ii == x and jj == y:
            min_dist = dist
            return min_dist

        row = [-1, 0, 0, 1]
        col = [0, -1, 1, 0]

        for k in range(4):
            nr, nc = ii + row[k], jj + col[k]
            if 0<=nr<m and 0<=nc<n and mat[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist+1))

    return min_dist

mat = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

src = (0, 0)
dest = (7, 5)

min_dist = findShorttestPath(mat, src, dest)
if min_dist != -1:
    print(min_dist)
else:
    print("No valid minimum distance found!")

