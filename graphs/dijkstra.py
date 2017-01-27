# Dijkstra algorithm. 
# Find the shortest paths from a source to elsewhere in the graph, no negative-weight edges.
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import testgraph as tg
from heapdict import heapdict

def dijkstra_noPQ(graph, src): # not using a priority queue
    unvisited = list(graph.keys())
    dist = {}
    path = {}
    dist[src] = 0

    def findMinDist():
        found = unvisited[0]
        mindist = (dist[unvisited[0]]) if (unvisited[0] in dist) else None
        for i in range(1,len(unvisited)):
            if unvisited[i] in dist:
                if (mindist is None) or (dist[unvisited[i]] < mindist):
                     found = unvisited[i]
                     mindist = dist[unvisited[i]]
        return found

    def relax(vertex):
        unvisited.remove(vertex)
        for adj in graph[vertex]:
            if adj in unvisited:
                if (adj not in dist) or (dist[vertex] + graph[vertex][adj] < dist[adj]):
                    dist[adj] = (dist[vertex] + graph[vertex][adj])
                    path[adj] = vertex

    while len(unvisited) > 0:
        relax(findMinDist())
    
    return dist, path

def dijkstra_PQ(graph, src):
    unvisited = list(graph.keys())
    dist = {}
    path = {}
    dist[src] = 0

    pq = heapdict() # now using a priority queue
    pq[src] = 0

    def findMinDist():
        return pq.popitem()[0]

    def relax(vertex):
        unvisited.remove(vertex)
        for adj in graph[vertex]:
            if adj in unvisited:
                if (adj not in dist) or (dist[vertex] + graph[vertex][adj] < dist[adj]):
                    dist[adj] = (dist[vertex] + graph[vertex][adj])
                    path[adj] = vertex
                    pq[adj] = dist[adj]

    while len(unvisited) > 0:
        relax(findMinDist())
    
    return dist, path

print(dijkstra_noPQ(tg.adjList(), "A"))
print(dijkstra_PQ(tg.adjList(), "A"))
