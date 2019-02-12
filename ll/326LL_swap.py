# Problem ID 326 Swap Nodes in a Link List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def swap_nodes(head, i, j):
    curr=head
    prev = previ = curri = prevj = currj = None
    count = 0
    while curr != None:
        if(count==i):
            previ = prev
            curri = curr
        elif(count==j):
            prevj = prev
            currj = curr
        prev = curr
        curr = curr.next
        count += 1
    if(curri==None or currj==None):
        return

    if(previ==None):
        head = currj
    else:
        previ.next = currj

    if(prevj==None):
        head = curri
    else:
        prevj.next = curri

    curr = curri.next
    curri.next = currj.next
    currj.next = curr

    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
