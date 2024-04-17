"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] 
represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place 
them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Sol: DFS, just find all connected components, subtract the "not connected" component.
"""

def makeConnected(connections, n):

    if len(connections) < n-1:
        return -1
    
    def dfs(node, adj, visited):
        visited.add(node)
        for neighbour_node in adj[node]:
            if neighbour_node not in visited:
                dfs(neighbour_node, adj, visited)

    adjList = {i:[] for i in range(n)}
    visited = set()
    connected_comp = 0

    for src, dest in connections:
        adjList[src].append(dest)
        adjList[dest].append(src)

    for i in range(n):
        if i not in visited:
            connected_comp +=1 
            dfs(i, adjList, visited)
    
    return connected_comp - 1

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
res = makeConnected(connections, n)
print(res)