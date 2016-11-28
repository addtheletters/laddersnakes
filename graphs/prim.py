# Prim's min-weight spanning tree algorithm

import testgraph as tg

# returns edge list
def prim(graph, src):

    dCut = list(graph.keys())
    dCut.remove(src)
    mwTreeEdges = []

    def findMinEdgeTo(cut):
        minEdge = None
        for v1 in graph:
            if v1 not in cut:
                for v2 in graph[v1]:
                    if v2 not in cut:
                        continue
                    if (minEdge is None) or (graph[v1][v2] < minEdge[1]):
                        minEdge = ((v1, v2), graph[v1][v2])
        #print(minEdge)
        return minEdge

    while len(dCut) > 0:
        leastEdge = findMinEdgeTo(dCut)
        dCut.remove(leastEdge[0][1])
        mwTreeEdges.append(leastEdge)

    return mwTreeEdges

# needs more testing
print(prim(tg.adjList(), "A"))
print(prim(tg.adjList(True), "G"))
