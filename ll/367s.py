class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    #  Given a linked list and two integers M and N. Traverse the linked list
    #  such that you retain M nodes then delete next N nodes, continue the same
    #  until end of the linked list. That is, in the given linked list you need
    #  to delete N nodes after every M nodes.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l) 
