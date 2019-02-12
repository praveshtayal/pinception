# Problem ID 764 Rearrange LL
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

def rearrange(head):
    #  Given a singly linked list L: L0→L1→…→Ln-1→Ln . Rearrange the nodes in
    #  the list so that the new formed list is: L0→Ln→L1→Ln-1→L2→Ln-2→… 
    #  You are required do this in-place without altering the nodes' values.
    #  Input: 2 5 8 12
    #  Output: 2 12 5 8 
    if(head==None):
        return head
    second=head.next
    prev=second
    if(prev==None):
        return head
    last = prev.next
    if(last==None):
        return head
    # atleast 3 nodes are present
    while(last.next):
        prev = last
        last = last.next
    # here we have 4 pointers poing to head node, second node, last node and
    # 2nd last node(pointed to by prev). Note that second and prev may point to
    # same node
    head.next = last
    prev.next = None
    last.next = rearrange(second)
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = rearrange(l)
printll(l)
