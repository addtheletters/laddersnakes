# Reversing a linked list. Runs with O(n) time, constant space. 

testFilename = "listreverse.txt"

def run(intext):
    intext = buildLinks(list(intext))
    print(str(intext) + " <=> " + str(reverse(intext)) )

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + ( (", " + str(self.next)) if self.next else "")

    def __repr__(self):
        return self.__str__()

def buildLinks(arr):
    if len(arr) < 1:
        return None
    else:
        return ListNode(arr[0], buildLinks(arr[1:]))

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
    llst = buildLinks([0, 1, 5, 7, 9, 100])
    print(llst)
    print(reverse(llst))

    print( reverse(buildLinks([4]) ) )

if __name__ == "__main__":
    trial()
