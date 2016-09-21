class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + ( (", " + str(self.next)) if self.next else "")

    def __repr__(self):
        return self.__str__()

    # follows the links 'index' times
    # returns a node further along in the list
    def getAt(self, index):
        place = self
        for i in range(index):
            place = place.next
            if place == None:
                return None
        return place

def buildLinks(arr):
    if len(arr) < 1:
        return None
    else:
        return ListNode(arr[0], buildLinks(arr[1:]))
