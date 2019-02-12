# Problem ID 1142 LL Length
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

# Main
# Read the link list elements including -1
#from sys import setrecursionlimit
#setrecursionlimit(11000)
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
printll(l)
len=length(l)
print(len)

def length(head):
    result=0
    while head:
        result += 1
        head = head.next
    return result

def ithNode(head, i):
    result=0
    while(head and i!=result):
        result += 1
        head = head.next
    if(i==result):
        return head
    else:
        return None

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

def lengthRecursive(head):
    # A linked list, find and return the length of input LL recursively.
    if head==None:
        return 0
    result=lengthRecursive(head.next)
    return result+1

def insertRec(head, i, data):
    #  a linked list, an integer n and a position i, Insert that node
    # n into Linked List at ith position recursively. If position i is greater
    # than length of LL, then you should return the same LL without any change.
    # And if position i is equal to length of input LL, insert the node at last
    # position.
    if(head==None and i!=0):
        return None
    if(i==0):
        # Insert data at i 0 
        p = Node(data)
        p.next = head
        return p
    head.next=insertRec(head.next,i-1,data)
    return head

def deleteRec(head, i):
    #  a linked list and a position i, delete the node of ith position from
    # Linked List recursively. If position i is greater than length of LL,
    # then:
    # you should return the same LL without any change.
    curr = head
    if head==None:
        return None
    if i==0:
        p = curr.next
        return p
    head.next=deleteRec(head.next,i-1)
    return head

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

def eliminate_duplicate(head):
    #  Given a sorted linked list (elements are sorted in ascending order).
    #  Eliminate duplicates from the given LL, such that output LL contains only
    #  unique elements.
    curr=head
    if(curr==None):
        return head
    next=curr.next
    while(next):
        if(curr.data == next.data):
            # Delete next node
            p=next
            curr.next = p.next
            next = curr.next
        else:
            curr=next
            next = curr.next
    return head

def check_palindrome(head) :
    #  Note: This check for None is redundant
    if(head==None):
        return True
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

def midpoint_linkedlist2(head):
    #  Given a linked list, find and return the midpoint.
    curr=head, curr2=head
    if(curr==None):
        return None; # 0 
    if(curr.next==None or curr.next.next==None):
        return curr; # 1 or 2 
    result=0
    while(curr):
        result += 1
        curr = curr.next
    curr=head
    for i in range(1, (result+1)//2):
        curr = curr.next
    return curr

def print_linkedlist_spl(head):
    #  Print a given linked list in reverse order. You need to print the tail
    #  first and head last. You can’t change any pointer in the linked list, just
    #  print it in reverse order.
    #  GOOD PROBLEM for RECURSION
    if(head==None):
        return
    print_linkedlist_spl(head.next)
    print(head.data, end=' ')

def reverse(head):
    #  Given a linked list, reverse it iteratively.
    if head==None:
        return None
    elif head.next==None:
        return head
    prev=head
    curr=prev.next
    next=curr.next
    #  Create Reversed List
    prev.next =None
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
    curr.next = prev
    return curr

def reverseRecursive(head):
    #  Given a linked list, reverse it recursively.
    if head==None:
        return None
    elif head.next==None:
        return head
    result=reverseRecursive(head.next)
    head.next.next=head
    head.next=None
    return result

def swap_nodes(head, i, j):
    curr=head
    prev = previ = curri = prevj = currj = None
    count = 0
    while curr != None:
        if(count==i):
            previ = prev
            curri = curr
        elif(count==j):
            prevj = prev
            currj = curr
        prev = curr
        curr = curr.next
        count += 1
    if(curri==None or currj==None):
        return

    if(previ==None):
        head = currj
    else:
        previ.next = currj

    if(prevj==None):
        head = curri
    else:
        prevj.next = curri

    curr = curri.next
    curri.next = currj.next
    currj.next = curr

    return head

def swap_nodes2(*head,i,j) :
    #  Given a linked list, i & j, swap the nodes that are present at
    #  i & j position in the LL. You need to swap the entire nodes, not just the
    #  data. 
    if(i==j) return head; 
    if(i>j):
        temp=i
        i=j
        j=temp
    # Here i<j
    curr=head, *prevI, *prevJ, *I, *J, *nextI, *nextJ
    result=0
    if(i==0):
        prevI = None
        I = head
        nextI = I.next
    else :
        while(curr and i-1!=result):
            result += 1
            curr = curr.next
        prevI = curr
        I = curr.next
        nextI = I.next
    if(j==i+1):
        #  Special Case: i and j are consecutive
        J = nextI
        nextJ = J.next

        #  Swap
        if(prevI) prevI.next = J
        J.next = I
        I.next = nextJ
        if(i==0) return J
        return head
    do:
        result += 1
        curr = curr.next
    while(curr and j-1!=result)
    prevJ = curr
    J = curr.next
    nextJ = J.next

    #  Swap I & J
    if(prevI) prevI.next = J
    J.next = nextI
    prevJ.next = I
    I.next = nextJ

    #cout<< "i " << I.data << endl; 
    #cout<< "j " << J.data << endl; 
    if(i==0)
        return J
    return head

def nthFromLastIter(head, n):
    #  Given a linked list and an integer n you need to find and return the nth
    #  node from last without calculating length of input linked list. Return
    #  null if length of LL is smaller than n. Counting of nodes starts from 0 
    result=0
    curr=head
    while(curr and n!=result):
        result += 1
        curr = curr.next
    #  Here curr is n nodes ahead of head. Now we will move both head and curr
    #  simultaneously untill curr is None 
    if(curr==None):
        return None
    next = curr.next
    while(next):
        curr = next
        next = curr.next
        head = head.next
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

def linearSearchRecursive(head, n):
    #  Given a linked list and an integer n you need to find and return index
    #  where n is present in the LL. Do this iteratively. Return -1 if n is not
    #  present in the LL. Indexing of nodes starts from 0. 
    if(head==None):
        return -1
    if(head.data==n):
        return 0
    result=linearSearchRecursive(head.next,n)
    if(result==-1):
        return -1
    return 1+result

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

def bubbleSortLL(head) :
    #  Sort a given linked list using Bubble Sort (iteratively). While sorting,
    #  you need to swap the entire nodes, not just the data.
    if(head==None or head.next==None):
        return head
    #  We have atleast 2 nodes.
    len=length(head)
    for i in range(0,len):
        prev = None
        curr = head
        next = curr.next
        while next:
            if curr.data > next.data:
                if prev:
                    prev.next = next
                else:
                    head = next
                curr.next = next.next
                next.next = curr
                prev = next
            else:
                prev = curr
            curr = prev.next
            next = curr.next
    return head

def append_LinkedList(head,n) :
    #  Given a linked list and an integer n, append the last n elements of the LL
    #  to front. 
        if(head==None or n<0):
            return None
        result=0
        curr=head
        prev=head
        while(curr!=None and n!=result):
                result += 1
                curr = curr.next
        #  Here curr is n nodes ahead of prev. Now we will move both prev and curr
        #  simultaneously untill curr is None 
        if(curr==None):
            return None
        next = curr.next
        while(next!=None):     
                curr = next
                next = curr.next
                prev = prev.next

        #  curr is last node and prev is prev node
        curr.next = head
        curr = prev.next
        prev.next = None
        return curr

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
                evenLast = evenLast.next = head
        else:
            # add node to oddList
            if(odd==None):
                odd = oddLast = head
            else:
                oddLast = oddLast.next = head
        head.next = None
        head = next
    if(odd==None):
        return even
    oddLast.next = even
    return odd

def skipMdeleteN(head, M, N):
    #  Given a linked list and two integers M and N. Traverse the linked list
    #  such that you retain M nodes then delete next N nodes, continue the same
    #  until end of the linked list. That is, in the given linked list you need
    #  to delete N nodes after every M nodes.
    if(head==None or N<=0 or M<0):
        return head
    curr=head
    while curr:
        # skip M-1 nodes
        for i in range(0, M-1):
            if curr==None:
                return head
            curr = curr.next
        prev = curr
        curr = curr.next
        # delete N nodes
        for i in range(0, N):
            if curr==None:
                break
            next = curr.next
            curr = next
        prev.next = curr
    return head

def rearrange(head):
    #  Given a singly linked list L: L0→L1→…→Ln-1→Ln . Rearrange the nodes in
    #  the list so that the new formed list is: L0→Ln→L1→Ln-1→L2→Ln-2→… 
    #  You are required do this in-place without altering the nodes' values.
    #  Input: 2 5 8 12
    #  Output: 2 12 5 8 
    if(head==None):
        return head
    second=head.next
    prev=second
    if(prev==None):
        return head
    last = prev.next
    if(last==None):
        return head
    # atleast 3 nodes are present
    while(last.next):
        prev = last
        last = last.next
    # here we have 4 pointers poing to head node, second node, last node and
    # 2nd last node(pointed to by prev). Note that second and prev may point to
    # same node
    head.next = last
    last.next = second
    prev.next = None
    last.next = rearrange(last.next)
    return head
