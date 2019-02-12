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

def midpoint_linkedlist(head):
    # Given a linked list, find and return the midpoint.
    curr=head
    result=0
    while curr:
        result += 1
        curr = curr.next
    curr=head
    for i in range(1, (result+1)//2):
        curr = curr.next
    return curr

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
node = midpoint_linkedlist(l)
if node:
    print(node.data)
