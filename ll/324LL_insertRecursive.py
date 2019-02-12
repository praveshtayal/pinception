# Problem ID 324 Insert ith Node Recursively
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

def insertRec(head, i, data):
    #  a linked list, an integer n and a position i, Insert that node
    # n into Linked List at ith position recursively. If position i is greater
    # than length of LL, then you should return the same LL without any change.
    # And if position i is equal to length of input LL, insert the node at last
    # position.
    if(head==None and i!=0):
        return None
    if(i==0):
        # Insert data at i 0 
        p = Node(data)
        p.next = head
        return p
    head.next=insertRec(head.next,i-1,data)
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(10000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
data=int(input())
l = insertRec(l, i, data)
printll(l)
