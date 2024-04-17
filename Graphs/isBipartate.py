graph = [[1,2,3],[0,2],[0,1,3],[0,2]]

def isBipartate(graph):
    def dfs(node):
        for neighbour in graph[node]:
            if color[neighbour] == 0:
                color[neighbour] = -(color[node])
                dfs(neighbour)
            elif color[neighbour] == color[node]:
                return False
        return True

    adjList = {i:[] for i in range(len(graph))}

    #0 -> no color, 1 -> red, -1 -> blue
    color = [0] * len(graph)

    for i in range(len(graph)):
        if color[i] !=0 : continue
        color[i] = 1
        return dfs(i)
            

res = isBipartate(graph)
print(res)