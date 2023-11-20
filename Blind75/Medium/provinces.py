"""
link:https://leetcode.com/problems/number-of-provinces/description/
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and
city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
"""

isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

def findProvinces(isConnected):

    def dfs(node):
        for neighbor in range(len(isConnected[node])):
            # Check if neighbor is unvisited and IS CONNECTED, isConnected[node][neighbor] =1
            if neighbor not in visited and isConnected[node][neighbor]:
                visited.add(neighbor)
                dfs(neighbor)

    connected_components = 0
    visited = set()

    n = len(isConnected)


    for i in range(n):
        if i not in visited:
            connected_components += 1
            visited.add(i)
            dfs(i)

    return connected_components

ans = findProvinces(isConnected)
print(f'There are {ans} provinces')
