# Problem ID 1144 Merge two sorted Linked List 
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

# Main
# Read the link list elements including -1
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)
