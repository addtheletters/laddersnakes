# stipulation:
# You have 2 singly linked lists.
# Check if they intersect. Get the node where they do that.
# (It's in CtCI 6th ed somewhere)

import singlylinkedlist as lists

def intersect(lstA, lstB):
    posA, posB = lstA, lstB
    lenA, lenB = 0, 0
    while posA.next != None:
        lenA += 1
        posA = posA.next
    while posB.next != None:
        lenB += 1
        posB = posB.next
    
    lstBig, lstSml = None, None
    lenDiff = abs(lenA - lenB)
    if lenA < lenB:
        lstBig, lstSml = lstB, lstA
    else:
        lstBig, lstSml = lstA, lstB

    posBig, posSml = lstBig, lstSml
    for i in range(lenDiff):
        posBig = posBig.next
    while posBig.next != None and posSml.next != None:
        posBig = posBig.next
        posSml = posSml.next
        if posBig == posSml:
            return posBig
             
    return None

tst1 = lists.buildLinks([1, 4,6, 7, 8, 84, 7, 4,3])
tst2 = lists.buildLinks([8, 4, 5, 7, 2, 89, 13])
tst2.getAt(6).next = tst1.getAt(3)

print(tst1)
print(tst2)
print(intersect(tst1, tst2))

# postmortem:
# Don't be afraid to scan through multiple times. 
# A large part of this problem was just optimizing.
# Carefully consider spatial relations. What does data mean relative to other pieces of it?
