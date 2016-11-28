# Bellman-Ford algorithm. 
# Find shortest paths from a source to elsewhere in a graph.
# Slower than Dijkstras, but works with negative edge weights.
# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

import testgraph as tg

def bellmanford(graph, src):
    edges = tg.edgeList(graph)
    dist = {}
    path = {}
    dist[src] = 0

    def relax(v, w):
        if (v in dist) and ((w not in dist) or (dist[v] + graph[v][w] < dist[w])):
            dist[w] = (dist[v] + graph[v][w])
            path[w] = v
    
    for i in range(len(graph.keys()) - 1):
        for edge in edges:
            relax(edge[0][0], edge[0][1])

    for edge in edges:
        if dist[edge[0][1]] > dist[edge[0][0]] + edge[1]:
            print("Negative weight cycle with edge " + str(edge[0]))

    return dist, path

print( bellmanford(tg.adjList(), "A") )
print( bellmanford(tg.adjNegative(), "O"))
print( bellmanford(tg.adjNegative(True), "O")) # with cycles
