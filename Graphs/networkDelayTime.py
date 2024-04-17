"""
Need to find the minimum time it will take to send info to all networks from a given start network

Sol: Dijkstra's minimum heap algo
"""

import heapq

def networkDelayTime(times, n: int, k: int) -> int:
    # Dijkstra's algorithm
    adjList = {i:[] for i in range(1, n+1)}

    for src, dest, time in times:
        adjList[src].append((dest, time))

    visited = set()
    # min heap so that popped element gives the min time element
    minHeap = [(0, k)]
    time = 0

    while minHeap:
        curr_time, curr_node = heapq.heappop(minHeap)
        if curr_node in visited:
            continue

        visited.add(curr_node)
        time = max(time, curr_time)

        for neighbour_node, neighbour_time in adjList[curr_node]:
            if neighbour_node not in visited:
                heapq.heappush(minHeap, (neighbour_time + curr_time, neighbour_node))  # Add total time from source node

    return time if len(visited) == n else -1



times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

res = networkDelayTime(times, n, k)
print(res)