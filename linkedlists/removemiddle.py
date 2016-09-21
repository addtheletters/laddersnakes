# stipulation: 
# Given a reference to a node in the middle of a singly linked list, remove it from the list.
import singlylinkedlist as lists

def removeMid(node):
    if node.next == None:
        #node       = None # futile; this is local, so really has no effect
        #node.val   = None # doesn't actully remove this node unfortunately
        return None # can't actually accomplish our goal
    node.val  = node.next.val
    node.next = node.next.next

testarr = [1, 4, 6, 7, 1]
testlst = lists.buildLinks(testarr)

print(testlst)
removeMid(testlst.getAt(0))
print(testlst)

# postmortem:
# Easier than expected. Still, not really very satisfying of a solution, since this node isn't actually erased.
