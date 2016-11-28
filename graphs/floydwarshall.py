# Floyd-Warshall all-pairs shortest-paths (APSP) algorithm
# Finds the shortest distance needed to travel between any two graph nodes
# Assumes no negative-weight cycles, though some negative weights are okay
# O(vertices^3) complexity, as might be expected 

import testgraph as tg
from copy import deepcopy

def floydWarshall(graph):
    sp = deepcopy(graph)
    print(sp)
    for k in graph:
        for i in graph:
            for j in graph:
                if (k in sp[i]) and (j in sp[k]) \
                and ( (j not in sp[i]) or (sp[i][k] + sp[k][j] < sp[i][j]) ):
                    sp[i][j] = sp[i][k] + sp[k][j]
    return sp

print(tg.adjList())
print(floydWarshall(tg.adjList()))
print(floydWarshall(tg.adjNegative()))
