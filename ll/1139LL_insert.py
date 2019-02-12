# Problem ID 1139 Insert ith Node
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

def insert(head, pos, data):
    # Given a linked list, an integer n and a position i, insert that node
    # n into Linked List at ith position. If position i is greater than length
    # of LL, you should return the same LL without any change. Indexing starts
    # from 0. You don't need to print the elements, just insert and return the
    # head of updated LL.
    curr=head
    if(head==None and pos!=0):
        return None
    p = Node(data)
    if(pos==0):
       # Insert data at pos 0 
       p.next = head
       return p
    result=0
    while(curr and pos-1!=result):
        result += 1
        curr = curr.next
    if(pos-1==result):
        # Insert data at pos. curr points to pos-1 index.
        p.next = curr.next
        curr.next = p
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
data=int(input())
l = insert(l, i, data)
printll(l)
