# Problem ID 1146 Linear Search in a LL
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

def linearSearch(head, n):
    #  Given a linked list and an integer n you need to find and return index
    #  where n is present in the LL. Do this iteratively. Return -1 if n is not
    #  present in the LL. Indexing of nodes starts from 0. 
    result=0
    curr=head
    while(curr and curr.data!=n):
        result += 1
        curr = curr.next
    if(curr==None):
        return -1
    return result

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
data=int(input())
index = linearSearch(l, data)
print(index)
