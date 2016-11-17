# sample graphs in various forms for testing algorithms

_TGRAPH = {
    "A":{"B":3, "C":2},
    "B":{"D":1, "F":5},
    "C":{"B":1, "E":7},
    "D":{"A":9, "E":14},
    "E":{"F":2, "C":6},
    "F":{"A":3, "B":1}
}

_TGRAPH_AUX = {
    "G":{"H":4, "L":19},
    "H":{"J":18, "K":10},
    "I":{"N":9, "M":7, "K":21},
    "J":{"K":22, "H":18},
    "K":{"L":14, "G":8, "J":7},
    "L":{"H":31, "I":5},
    "M":{"I":36, "N":13},
    "N":{"L":10, "M":11}
}

def adjList(aux=False):
    if aux:
        return _TGRAPH_AUX
    return _TGRAPH

def fromAdjMat(amat, ind=None):
    alst = {}
    if ind is None:
        print("no index record provided for adjacency matrix")
        print("apparent # of vertices:", len(amat))
        ind = [n for n in range(len(amat))] # default to vertices being numbered
    for i in range(len(amat)):
        for j in range(len(amat[i])):
            if amat[i][j] == None:
                continue
            if ind[i] not in alst:
                alst[ind[i]] = {}
            alst[ind[i]][ind[j]] = amat[i][j]
    return alst

def fromEdgeList(elst):
    alst = {}
    for edge in elst:
        if edge[0][0] not in alst:
            alst[edge[0][0]] = {}
        alst[edge[0][0]][edge[0][1]] = edge[1]
    return alst

# convert an adjacency list into an adjacency matrix
def adjMat(alist=_TGRAPH):
    mat = [None] * len(alist.keys())
    for i in range(len(mat)):
        mat[i] = [None] * len(alist.keys())
    ind = list(alist.keys())

    for vert in ind:
        for neighbor in alist[vert].keys():
            mat[ind.index(vert)][ind.index(neighbor)] = alist[vert][neighbor]
    return mat, ind

# convert an adjacency list into an edge list
def edgeList(alist=_TGRAPH):
    edges = []
    for key in alist:
        for subkey in alist[key]:
            edges.append( ( (key, subkey) , alist[key][subkey]) )
    return edges

def testConvert(alst):
    print(alst)
    tmat, tind = adjMat(alst)
    telst = edgeList(alst)
    print(fromAdjMat(tmat, tind))
    print(fromEdgeList(telst))
    return (tmat, tind), telst

if __name__ == "__main__":
    testConvert(adjList(True))
