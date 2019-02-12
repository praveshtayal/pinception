# Problem ID 329 Print LL in reverse order
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

def print_linkedlist_spl(head):
    #  Print a given linked list in reverse order. You need to print the tail
    #  first and head last. You can’t change any pointer in the linked list, just
    #  print it in reverse order.
    #  GOOD PROBLEM for RECURSION
    if(head==None):
        return
    print_linkedlist_spl(head.next)
    print(head.data, end=' ')

# Main
# Read the link list elements including -1
from sys import setrecursionlimit
setrecursionlimit(10000)
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
print_linkedlist_spl(l)
