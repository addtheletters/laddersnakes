class TreeNode:
    def __init__(self, val=None):
        self.val    = val
        self.left   = None
        self.right  = None

    def __str__(self):
        return "[" + str(self.val) + ": " + str(self.left) + "," + str(self.right) + "]"
    
    def __repr__(self):
        return self.__str__()
        
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

def buildBST(elements):
    root = TreeNode(elements[0])
    for elm in elements[1:]:
        root.bstAppend(elm)
    return root

def _test():
    lst = [9, 5, 7, 2, 10, 67, 3 ,24, 6, 99, 100, 98.5]
    print(lst)
    print(buildBST(lst))

if __name__ == "__main__":
    _test()
