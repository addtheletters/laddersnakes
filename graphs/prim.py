# Prim's min-weight spanning tree algorithm

def prim(graph):
    uncut = list(graph.keys())

    def findEdges(cut):
        for edge in graph:
            if edge in cut:
                print("hi")
                
    while len(uncut) > 0:
        nslice = uncut.pop()
        findEdges(uncut)