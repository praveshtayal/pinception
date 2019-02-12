# Problem ID 330 Palindrome
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

def check_palindrome(head) :
    #  Note: This check for None is redundant
    if(head==None):
        return true
    # We will use stack s with operation append acting as push
    s = []
    while(head):
        s.append(head.data)
        head = head.next
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left += 1
        right -= 1
    return True

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
