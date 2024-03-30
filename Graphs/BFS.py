from collections import deque

def bfs(graph, start):
    # a queue and a visited set
    queue = deque()
    visited = set()

    # add the start to queue
    queue.append(start)

    # mark is as visited
    visited.add(start)

    # while queue is not empty
    while queue:
        # pop the top one out
        vertex = queue.popleft()

        # for all the neighbours of the popped vertex
        for neighbour in graph[vertex]:
            # if the neighbour is not already visited
            if neighbour not in visited:
                # add the neighbour to queue to explore it
                queue.append(neighbour)
                # mark the neighbour as visited
                visited.add(neighbour)


    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}

start = 'A'
print(bfs(graph, start))

