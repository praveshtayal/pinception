# Problem ID 327 Eliminate Duplicates in LL
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

def eliminate_duplicate(head):
    #  Given a sorted linked list (elements are sorted in ascending order).
    #  Eliminate duplicates from the given LL, such that output LL contains only
    #  unique elements.
    curr=head
    if(curr==None):
        return head
    next=curr.next
    while(next):
        if(curr.data == next.data):
            # Delete next node
            p=next
            curr.next = p.next
            next = curr.next
        else:
            curr=next
            next = curr.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = eliminate_duplicate(l)
printll(l)
