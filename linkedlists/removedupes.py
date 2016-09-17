# CtCI 6th ed problem 2.1
import singlylinkedlist as lists

def removeDuplicates(node):
    valset = [node.val]
    prev = node
    while prev.next != None:
        if prev.next.val not in valset:
            valset.append(prev.next.val)
            prev = prev.next
        else:
            prev.next = prev.next.next
    return


testlist = lists.buildLinks([0, 56, 3, 3, 5, 2, 4, 5, 6, 76, 2, 71, 4, 4, 1])
print(testlist)
removeDuplicates(testlist)
print(testlist)

# Postmortem: 
# Don't track things that aren't needed. Take it easy.
# To do without any buffer space, use two pointers. That's slow, n^2, eww.
