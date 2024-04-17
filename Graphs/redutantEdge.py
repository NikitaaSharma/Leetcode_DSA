"""
Need to find any 1 redundant edge in the graph.

Sol: The edge that is responsible for making a CYCLE, is the redundant edge.
"""

from collections import defaultdict


def findRedundantEdge(edges):
    
    def path_exists(start_node, end_node):
        if start_node == end_node:
            return True
        
        visited.add(start_node)

        for neighbour in graph_so_far[start_node]:
            if neighbour not in visited:
                if path_exists(neighbour, end_node):
                    return True
                
        return False

    # construct the graph edge by edge, initialise it empty
    graph_so_far = defaultdict(lambda: [])

    for start_node, end_node in edges:

        # a new visited set for every edge
        visited = set()

        if path_exists(start_node, end_node):
            return [start_node, end_node]
        else:
            graph_so_far[start_node].append(end_node)
            graph_so_far[end_node].append(start_node)

    return None





edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
res = findRedundantEdge(edges)
print(f"Redundant edge: {res}")