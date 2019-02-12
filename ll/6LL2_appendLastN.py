# Problem ID 6 Append last N nodes to the Front of LL
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

def append_LinkedList(head,n) :
    #  Given a linked list and an integer n, append the last n elements of the LL
    #  to front. 
        if(head==None or n<0):
            return None
        result=0
        curr=head
        prev=head
        while(curr and n!=result):
                result += 1
                curr = curr.next
        #  Here curr is n nodes ahead of prev. Now we will move both prev and curr
        #  simultaneously untill curr is None 
        if(curr==None):
            return None
        next = curr.next
        while next:     
                curr = next
                next = curr.next
                prev = prev.next

        #  curr is last node and prev is prev node
        curr.next = head
        curr = prev.next
        prev.next = None
        return curr

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = append_LinkedList(l, i)
printll(l)
