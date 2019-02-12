# Problem ID 325 Delete ith Node Recursively
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

def deleteRec(head, i):
    #  a linked list and a position i, delete the node of ith position from
    # Linked List recursively. If position i is greater than length of LL,
    # then:
    # you should return the same LL without any change.
    curr = head
    if head==None:
        return None
    if i==0:
        p = curr.next
        return p
    head.next=deleteRec(head.next,i-1)
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = deleteRec(l, i)
printll(l)
