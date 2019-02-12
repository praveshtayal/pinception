# Problem ID 1140 Delete ith Node
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

def delete(head, i):
    # A linked list and a position i, delete the node of ith position from
    # Linked List iteratively. If position i is greater than length of LL, then
    # you should return the same LL without any change. Indexing starts from 0.
    # You don't need to print the elements, just delete the node and return the
    # head of updated LL.
    curr=head
    if(head==None):
        return None
    if(i==0):
        p = curr.next
        return p
    result=0
    while(curr and i-1!=result):
        result += 1
        curr = curr.next
    if(i-1==result):
        p = curr.next
        if(p==None):
            return head
        curr.next = p.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = delete(l, i)
printll(l)
