# Problem ID 1145 Last nth Node for a LL
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

def nthFromLastIter(head, n):
    #  Given a linked list and an integer n you need to find and return the nth
    #  node from last without calculating length of input linked list. Return
    #  null if length of LL is smaller than n. Counting of nodes starts from 0 
    result=0
    curr=head
    while(curr and n!=result):
        result += 1
        curr = curr.next
    #  Here curr is n nodes ahead of head. Now we will move both head and curr
    #  simultaneously untill curr is None 
    if(curr==None):
        return None
    next = curr.next
    while(next):
        curr = next
        next = curr.next
        head = head.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
node = nthFromLastIter(l, i)
if node:
    print(node.data)
