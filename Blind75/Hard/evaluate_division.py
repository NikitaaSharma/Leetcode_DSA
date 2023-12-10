def calcEquation(equations, values, queries):
    def buildGraph(equations, values):
        graph = {}
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value
        print(graph)
        return graph

    def dfs()

    buildGraph(equations, values)

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

res = calcEquation(equations, values, queries)
print(res)