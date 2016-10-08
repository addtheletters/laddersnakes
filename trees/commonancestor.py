# CtCI 6th ed problem 4.8
import binarytree as trees

def findAncestor(tree, a, b):
    return _findAncestor(tree, [], a, b, [])

def _findAncestor(node, path, a, b, firstPath):
    #print("Finding at " + str(node))
    #print("Path is " + str(path))
    #print("Firstpath is " + str(firstPath))

    if node is None:
        return None
        
    foundFirst = False

    if (node.val is a) or (node.val is b):
        if (firstPath is not None) and (len(firstPath) > 0):
            path.append(node) # complete second path

            print(firstPath)
            print(path)

            # find last intersection of paths
            pIndex = 0
            for i in range(min(len(path), len(firstPath))):
                if path[i] is not firstPath[i]:
                    break
                pIndex = i

            #print("Found second.")
            return path[pIndex]
        else:
            #print("Found " + str(node.val))
            # save path to the first element we found
            for nde in path:
                firstPath.append(nde)
            firstPath.append(node)
            #return _findAncestor(node, path + [node], a, b, firstPath=path)

    lft = _findAncestor(node.left, path + [node], a, b, firstPath)
    if lft is not None:
        return lft
    rgt = _findAncestor(node.right, path + [node], a, b, firstPath)
    return rgt

testtree = trees.TreeNode(val=8,left=trees.build_test())
print(testtree.str_bfs())
res = findAncestor(testtree, 2, 3)
print(res)
