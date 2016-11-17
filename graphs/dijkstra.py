# Dijkstra. Shortest paths, no negative-weight edges.
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
        unvisited.remove(v)
        for adj in graph[vertex]:
            if adj in unvisited:
                if (adj not in dist) or (dist[vertex] + graph[vertex][adj] < dist[adj]):
                    dist[adj] = (dist[vertex] + graph[vertex][adj])
                    path[adj] = v

    while len(unvisited) > 0:
        v = findMinDist()
        relax(v)
    
    return dist, path

def dijkstra_PQ(graph, src):
    unvisited = list(graph.keys())
    dist = {}
    path = {}
    dist[src] = 0

    pq = heapdict()
    pq[src] = 0

    def findMinDist():
        return pq.popitem()[0]

    def relax(vertex):
        unvisited.remove(v)

        for adj in graph[vertex]:
            if adj in unvisited:
                if (adj not in dist) or (dist[vertex] + graph[vertex][adj] < dist[adj]):
                    dist[adj] = (dist[vertex] + graph[vertex][adj])
                    path[adj] = v
                    pq[adj] = dist[adj]

    while len(unvisited) > 0:
        v = findMinDist()
        relax(v)
    
    return dist, path


print(tg.adjList())
print(dijkstra_noPQ(tg.adjList(), "A"))
print(dijkstra_PQ(tg.adjList(), "A"))

