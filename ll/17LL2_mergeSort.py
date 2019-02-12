# Problem ID 17 MergeSort Linked List  
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

def merge(head1,head2):
    #  two linked lists sorted in increasing order. Merge them in such
    # a way that the result list is also sorted (in increasing order). Try
    # solving with O(1) auxiliary space (in-place). You just need to return the
    # head of new linked list, don't print the elements.
    #head = None
    if(head1==None):
        return head2
    if(head2==None):
        return head1
    if(head1.data<=head2.data):
        head=head1
        head1=head1.next
    else:
        head=head2
        head2=head2.next
    curr=head
    while(head1 and head2):
        if(head1.data<=head2.data):
            curr.next=head1
            head1=head1.next
        else:
            curr.next=head2
            head2=head2.next
        curr=curr.next
    if(head1==None):
        curr.next=head2
    else:
        curr.next=head1
    return head

def midpoint_linkedlist(head):
    #  Given a linked list, find and return the midpoint.
    curr=head
    result=0
    while curr:
        result += 1
        curr = curr.next
    curr=head
    for i in range(1, (result+1)//2):
        curr = curr.next
    return curr

def mergeSort(head):
    #  Sort a given linked list using Merge Sort.
    if(head==None):
        return None
    if(head.next==None):
        return head
    #  We have atleast 2 s. Split the list into two parts equally
    mid = midpoint_linkedlist(head)
    head2 = mid.next
    mid.next = None

    #  MegreSort the two lists
    head = mergeSort(head)
    head2 = mergeSort(head2)
    head = merge(head, head2)
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)
