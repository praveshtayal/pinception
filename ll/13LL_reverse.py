# Problem ID 13 Reverse LL
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

def reverse(head):
    #  Given a linked list, reverse it iteratively.
    if head==None:
        return None
    elif head.next==None:
        return head
    prev=head
    curr=prev.next
    next=curr.next
    #  Create Reversed List
    prev.next =None
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
    curr.next = prev
    return curr
# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverse(l)
printll(l)
