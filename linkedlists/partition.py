# CtCI problem 2.4, Partition
# given value x, make everything < x come before everything >= x

import singlylinkedlist as lists

def partition(lst, x):
    lastLess, lastMore = None, None
    firstLess, firstMore = None, None
    here = lst
    while here is not None:
        herenext = here.next # don't want overriding of this
        if here.val < x:
            if firstLess is None:
                firstLess = here
            if lastLess is not None:
                lastLess.next = here
            lastLess = here
            #print("lastLess", lastLess)
        else:
            if firstMore is None:
                firstMore = here
            if lastMore is not None:
                lastMore.next = here
            lastMore = here
            #print("lastMore", lastMore)
            #print("firstMore", firstMore)
        here = herenext
    if firstLess is None:
        return firstMore
    lastLess.next = firstMore
    lastMore.next = None
    return firstLess

testlist = lists.buildLinks([0, 56, 3, 3, 5, 2, 4, 5, 6, 76, 2, 71, 4, 4, 1])
print(testlist)
print(partition(testlist, 6))

# Postmortem:
# Pay attention to what you need to return. 
# Alternate solution is to build up from head and from tail rather than assembling 2 lists from the start
