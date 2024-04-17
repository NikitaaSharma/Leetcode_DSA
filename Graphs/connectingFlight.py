n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

from collections import deque


def cheapFlight(flights, src, dst, k, n):
    adjList = [[] for _ in range(len(flights))]
    for flight in flights:
        adjList[flight[0]].append((flight[1], flight[2]))
    print(adjList)

    queue = deque()
    visited = set()

    queue.append((src, 0))
    visited.add((src, 0))
    k+=1

    while k>0 and queue:
        size = len(queue)
        while size>0:
            curr_node, curr_price = queue.popleft()
            
            for neighbour, price in adjList[curr_node]:
                new_price = price + curr_price
                if (neighbour, new_price) not in visited:
                    queue.append((neighbour, new_price))
                    visited.add((neighbour, new_price))
            size -=1
        k -=1 

    min_price = float("inf")
    for node, price in visited:
        if node == dst:
            min_price = min(min_price, price)

    return min_price if min_price != float('inf') else -1

res = cheapFlight(flights, src, dst, k, n)
print(res)

    
        
