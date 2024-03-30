graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [0],
    4: [3, 5],
    5: [0]
}

from collections import deque
def findRoot(graph, start):
    queue = deque()
    visited = set()
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

    # check out of all the nodes, which node is not in visited set
    for node in graph.keys():
        if node not in visited:
            return node
        
    return None
    
ver = findRoot(graph, 0)
print(ver)