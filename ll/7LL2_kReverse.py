# Problem ID 7 kReverse in LL
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

def kReverse(head, n) :
    #  Implement kReverse( k ) in a linked list i.e. you need to reverse
    #  first K elements then reverse next k elements and join the linked list and
    #  so on. Indexing starts from 0. If less than k elements left in the last,
    #  you need to reverse them as well. If k is greater than length of LL,
    #  reverse the complete LL. If n is 4 and LL is:
    #  Input: 1 2 3 4 5 6 7 8 9 10
    #  Output: 4 3 2 1 8 7 6 5 10 9 
    if(head==None or n<=1):
        return head
    elif(head.next==None):
        return head
    # n is atleast 2 and we have atleast 2 nodes
    prev=head
    curr=prev.next
    #  Create Reversed List
    i=1
    prev.next =None
    while(curr and i<n):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1
    head.next = kReverse(curr, n)
    return prev

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = kReverse(l, i)
printll(l)
