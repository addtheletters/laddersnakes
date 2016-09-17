# CtCI 6th ed problem 2.2
import singlylinkedlist as lists

def kthToLast(node, k):
    if k < 1:
        return None
    pkth = node
    pend = node
    for i in range(k-1):
        pend = pend.next
        if pend == None:
            return None # < k elements are present
    while pend.next != None:
        pkth = pkth.next
        pend = pend.next
    return pkth.val

testarr = [5, 6, 2, 76, 7, 75, 3, 4, 4 ]
testk = 0
testlist = lists.buildLinks(testarr)
print(testlist)
if testk < 1:
    print("Invalid k.")
else:
    print("kth is " + str(testarr[-testk]))
print("kth to last found " + str(kthToLast(testlist, testk)))

# Postmortem:
# Consider recursive options.
