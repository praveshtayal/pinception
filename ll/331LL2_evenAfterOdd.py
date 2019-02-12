# Problem ID 331 even after odd in a LL
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

def arrange_LinkedList(head):
    #  Even after Odd LinkedList: Arrange elements in a given Linked List such
    #  that, all even numbers are placed after odd numbers. Respective order of
    #  elements should remain same.
    if(head==None):
        return head
    even=None
    odd=None
    while(head):
        next = head.next
        if(head.data%2==0):
            # add node to evenList
            if(even==None):
                even = evenLast = head
            else:
                evenLast.next = head
                evenLast = head
        else:
            # add node to oddList
            if(odd==None):
                odd = oddLast = head
            else:
                oddLast.next = head
                oddLast = head
        head.next = None
        head = next
    if(odd==None):
        return even
    oddLast.next = even
    return odd

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)
