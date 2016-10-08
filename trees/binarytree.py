class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right

    def __str__(self):
        return "[TreeNode " + str(self.val) + "]"
        
    def __repr__(self):
        return self.__str__()

    def str_inorder(self):
        return "[" + str(self.val) + ": " + str(self.left.str_inorder() if self.left else self.left)+ "," + str(self.right.str_inorder() if self.right else self.right) + "]"
    
    def bstAppend(self, value):
        if value > self.val:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.bstAppend(value)
        else:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.bstAppend(value)
    
    def str_bfs(self):
        out = ""
        nodequeue = [{"level":0,"node":self}]
        lastlevel = 0
        while len(nodequeue) > 0:
            working = nodequeue.pop(0)
            #print(working)
            #if working["node"] != None:# and isinstance(working, TreeNode):
            if working["level"] != lastlevel:
                lastlevel = working["level"]
                out += "\n" + lastlevel * " "
            out = out + str(working["node"].val if working["node"] else working["node"]) + (" , " if "left" in working else " | ")
            if working["node"] != None:
                nodequeue.append( {"level":working["level"] + 1, "node":working["node"].left, "left":True} )
                nodequeue.append( {"level":working["level"] + 1, "node":working["node"].right})
        return out

def buildBST(elements):
    s = set()
    duplicates = set(x for x in elements if x in s or s.add(x)) # find duplicate elements
    if len(duplicates) > 0:
        print("error: BST elements contained duplicates: " + str(duplicates))
        return
    root = TreeNode(elements[0])
    for elm in elements[1:]:
        root.bstAppend(elm)
    return root

def build_test(debug=False):
    lst = [9, 5, 7, 2, 10, 67, 3 ,24, 6, 99, 100, 98.5, 34, 11, 21]
    if debug:
        print(lst)
    tre = buildBST(lst)
    if debug:
        print(tre.str_inorder())
        print(tre.str_bfs())
    return tre

if __name__ == "__main__":
    build_test(True)
