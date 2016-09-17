# Reversing a linked list. Runs with O(n) time, constant space. 
import singlylinkedlist as lists

testFilename = "linkedlists/listreverse.txt"

def run(intext):
    intext = lists.buildLinks(list(intext))
    print(str(intext) + " <=> " + str(reverse(intext)) )

def reverse(node):
    prev = node
    if not prev.next: # only one element
        return prev
    mid = prev.next
    aft = mid.next
    prev.next = None
    while aft != None:
        mid.next = prev
        prev = mid
        mid = aft
        aft = aft.next
    mid.next = prev
    return mid

def trial():
    llst = lists.buildLinks([0, 1, 5, 7, 9, 100])
    print(llst)
    print(reverse(llst))

    print( reverse(lists.buildLinks([4]) ) )

if __name__ == "__main__":
    trial()
