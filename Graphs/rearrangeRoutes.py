"""
leetcode: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different 
cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""
def dfs(visited, adj, curr_city):
    visited.add(curr_city)
    route_changes = 0
    for neighbour in adj[curr_city]:
        # check if the curr city is not alreadt visited
        if neighbour[0] not in visited:
            # check if it has an outgoing route
            if neighbour[1] == 1:
                # route change is needed to make an incoming route
                route_changes +=1

            route_changes += dfs(visited, adj, neighbour[0])

    return route_changes


def minReorder(n: int, connections):
    # create an empty adjacency list
    adj_list = [[] for _ in range(n)]

    for connection in connections:
        # mark outgoing connections as 1
        adj_list[connection[0]].append((connection[1], 1))
        # mark incoming connections as -1
        adj_list[connection[1]].append((connection[0], -1))

    visited = set()
    return f"{dfs(visited, adj_list, curr_city = 0)} route changeses are needed for the fair"

n = 6
# connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
connections = [[1,0],[1,2],[3,2],[3,4]]

print(minReorder(n, connections))