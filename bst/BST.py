import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Problem ID 353, Level order traversal
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Problem ID 1568, print level wise tree
def printLevelWise(root):
    # Given a binary tree, print the tree in level wise order. For printing
    # a node with data N, you need to follow the exact format: 
    # N:L:x,R:y
    # wherer, N is data of any node present in the binary tree. x and y are the
    # values of left and right child of node N. Print -1. if any child is null.
    # There is no space in between. You need to print all nodes in the level
    # order form in different lines.
    if root==None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr = q.get()
        currData=curr.data
        left=-1
        right=-1
        if curr.left!=None:
            left = curr.left.data
            q.put(curr.left)
        
        if curr.right!=None:
            right = curr.right.data
            q.put(curr.right)
        
        print(currData, ":L:", left, ",R:", right, sep='')

# Problem ID 1600, searchInBST
def searchInBST(root, k):
    # Given a BST and an integer k. Find if the integer k is present in given
    # BST or not. Return the node with data k if it is present, return null
    # otherwise. Assume that BST contains all unique elements.
    if root==None:
        return None
    if root.data==k:
        return root
    if k < root.data:
        return searchInBST(root.left, k)
    else:
        return searchInBST(root.right, k)

# Problem ID 1158, elementsInRangeK1K2
def elementsInRangeK1K2(root, k1, k2):
    # Given a Binary Search Tree and two integers k1 and k2, find and print the
    # elements which are in range k1 and k2 (both inclusive). Print the elements
    # in increasing order.
    # Solution: Since the elemnts have to be printed in increasing oder we will
    # use in-order traversal and print the node only if it lies between range
    if root==None:
        return
    if k1<=root.data and root.data<=k2:
        elementsInRangeK1K2(root.left, k1, k2)
        print(root.data, end=' ')
        elementsInRangeK1K2(root.right, k1, k2)
        return
    if root.data>k2:
        return elementsInRangeK1K2(root.left, k1, k2)
    else:
        elementsInRangeK1K2(root.right, k1, k2)

# Problem ID 1600, areElementsInRangeK1K2
def areElementsInRangeK1K2(root, k1, k2):
    # Given a Binary Search Tree and two integers k1 and k2, find and print the
    # elements which are in range k1 and k2 (both inclusive). Print the elements
    # in increasing order.
    # Solution: Since the elemnts have to be printed in increasing oder we will
    # use in-order traversal and print the node only if it lies between range
    if root==None:
        return True
    if root.data<k1 or k2<root.data:
        return False
    if not areElementsInRangeK1K2(root.left, k1, k2):
        return False
    if not areElementsInRangeK1K2(root.right, k1, k2):
        return False
    return True

# Link List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Problem ID 1160, sortedLLFromBST
def sortedLLFromBST(root):
    # Given a BST, convert it into a sorted linked list. Return the head of
    # LL
    if root==None:
        return None
    lst = sortedLLFromBST(root.left)
    curr = Node(root.data)
    curr.next = sortedLLFromBST(root.right)
    if lst==None:
        return curr
    # Append curr at end of list and return list
    ptr = lst
    while ptr.next!=None:
        ptr = ptr.next
    ptr.next = curr
    return lst

# Problem ID 1565, preorder Recursive
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Problem ID 1159, constructBST
def constructBST(lst):
    # Given a sorted integer array A of size n which contains all unique
    # elements. You need to construct a balanced BST from this input array.
    # Return the root of constructed BST. If array size is even, take first mid
    # as root.
    n=len(lst)
    if lst==None or n<=0:
        return None
    rootIndex = (n-1)//2
    root = BinaryTreeNode(lst[rootIndex])
    root.left = constructBST(lst[:rootIndex])
    root.right = constructBST(lst[rootIndex+1:])
    return root

# Problem ID 861, isBSTandInRange
def isBSTandInRange(root, minimum, maximum):
    # Given a binary tree with N number of nodes, check if that input tree is
    # BST (Binary Search Tree) or not. If yes, return True, return False
    # otherwise. Duplicate elements should be in right subtree.
    if root==None:
        return True
    if minimum > root.data or root.data > maximum:
        return False
    if not isBSTandInRange(root.left, minimum, root.data-1):
        return False
    if not isBSTandInRange(root.right, root.data, maximum):
        return False
    return True

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 861, isBST2
def isBST2(root):
    return isBSTandInRange(root, INT_MIN, INT_MAX)

def isBST(root):
    # Given a binary tree with N number of nodes, check if that input tree is
    # BST (Binary Search Tree) or not. If yes, return True, return False
    # otherwise. Duplicate elements should be in right subtree.
    if root==None:
        return True
    if not isBST(root.left):
        return False
    if not isBST(root.right):
        return False
    if not areElementsInRangeK1K2(root.left, INT_MIN, root.data-1):
        return False
    if not areElementsInRangeK1K2(root.right, root.data, INT_MAX):
        return False
    return True

# Problem ID 1600, findPathBinaryTree
#def findPathBinaryTree(root, data, vector& v):
def findPathBinaryTree(root, data, v):
    # Given a Binary Tree and integer k. Find and return path from the node with
    # data k and root (if a node with data k is present in given BST). Return
    # null otherwise. Assume that BST contains all unique elements.
    if root==None:
        return False
    v.append(root.data)
    if root.data==data:
        return True
    left = findPathBinaryTree(root.left, data, v)
    if left == True:
        return True
    right = findPathBinaryTree(root.right, data, v)
    if right == True:
        return True
    v.pop_back()
    return False

# Problem ID 1600, findPath
#vector findPath(root, data):
def findPath(root, data):
    # Given a BST and an integer k. Find and return the path from the node with
    # data k and root (if a node with data k is present in given BST). Return
    # null otherwise. Assume that BST contains all unique elements.
    #vector path = vector
    path = []
    while root!=None:
        path.append(root.data)
        if root.data==data:
            #reverse(path.begin(),path.end())
            return path
        elif root.data<data:
            root = root.right
        else:
            root = root.left
    return None

# Problem ID 512, insertDuplicateNode
def insertDuplicateNode(root):
    # Given a BST with N number of nodes, for each node create a new duplicate
    # node, and insert that duplicate as left child of the original node.
    if root==None:
        return
    node = BinaryTreeNode(root.data)
    node.left = root.left
    root.left = node
    insertDuplicateNode(node.left)
    insertDuplicateNode(root.right)

def searchInBinaryTree(root, x):
    if root==None:
        return None
    if root.data == x:
        return root
    result = searchInBinaryTree(root.left, x)
    if result!=None:
        return result
    result = searchInBinaryTree(root.right, x)
    return result

# Problem ID 513, lcaBinaryTree
def lcaBinaryTree(root, val1, val2):
    # Given a Binart Tree and two nodes, find LCA (Lowest Common Ancestor) of
    # the given two nodes in Binart Tree. Read about LCA if you are having
    # doubts about the definition. If out of 2 nodes only one node is present,
    # return that node. If both are not present, return -1.
    if root==None:
        return -1
    node1 = searchInBinaryTree(root, val1)
    node2 = searchInBinaryTree(root, val2)
    if node1==None:
        if node2==None:
            return -1
        else:
            return node2.data
    # node1 is not null
    if node2==None:
        return node1.data
    # node2 is not null
    if node1 == node2:
        return node1.data
    # Here we are sure that we have two distinct nodes present in the tree. Now,
    # we can start from root and traverse the tree untill we get the LCA Node
    curr = root
    while curr != None:
        # If both nodes are present in left tree
        node1 = searchInBinaryTree(curr.left, val1)
        node2 = searchInBinaryTree(curr.left, val2)
        if node1!=None and node2!=None:
            curr = curr.left
            continue
        # If both nodes are present in right tree
        #node1 = searchInBinaryTree(curr.right, val1)
        #node2 = searchInBinaryTree(curr.right, val2)
        if node1==None and node2==None:
            curr = curr.right
            continue
        return curr.data
    # This code should never be executed
    return -1

# Problem ID 106, lcaInBST
def lcaInBST(root, val1, val2):
    # Given a BST and two nodes, find LCA (Lowest Common Ancestor) of
    # the given two nodes in BST. Read about LCA if you are having
    # doubts about the definition. If out of 2 nodes only one node is present,
    # return that node. If both are not present, return -1.
    if root==None:
        return -1
    # Ensure val1 <= val2. If not swap them
    if val1>val2:
        val1, val2 = val2, val1
    node1 = searchInBST(root, val1)
    node2 = searchInBST(root, val2)
    if node1==None:
        if node2==None:
            return -1
        else:
            return node2.data
    # node1 is not null
    if node2==None:
        return node1.data
    # node2 is not null
    if node1 == node2:
        return node1.data
    # Here we are sure that we have two distinct nodes present in the tree. Now,
    # we can start from root and traverse the tree untill we get the LCA Node
    curr = root
    while curr != None:
        if val1 <= curr.data and curr.data <= val2:
            return curr.data
        # Both node1 and node 2 are in some subtree
        if val2 < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    # This code should never be executed if given tree is a BST
    return -1

#def updateMap(root, unordered_map<int, int> &treemap):
def updateMap(root, treemap):
    if root==None:
        return
    treemap[root.data] = 1
    updateMap(root.left, treemap)
    updateMap(root.right, treemap)

# Problem ID 104, nodeSumToS
def nodesSumToS(root, S):
    # Given a binary tree and an integer S, print all the pair of nodes whose
    # sum equals S. Assume binary tree contains all unique elements. Note: In
    # a pair, print the smaller element first. Order of different pair doesn't
    # matter.
    if S<0:
        S *= -1
    treemap = {}
    updateMap(root, treemap)
    for num in treemap:
        if S-num in treemap and num<S-num:
            print(num, S-num)

# Problem ID 107, rootToLeafPathsSumToK
# The function does not modify the lst
def rootToLeafPathsSumToK(root, k, lst):
    if root==None:
        return
    if root.left==None and root.right==None:
        # Reached leaf node
        if root.data==k:
            print(*lst, k)
        return
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k-root.data, lst)
    rootToLeafPathsSumToK(root.right, k-root.data, lst)
    lst.pop()

# Problem ID 107, rootToLeafPathsSumToKIterative
def rootToLeafPathsSumToKIterative(root, k):
    # Given a binary tree and a number k, print out all root to leaf paths where
    # the sum of all nodes value is same as the given number k.
    # Here we will traverse the tree is inorder using stack
    # if root==None) return This check is not required
    #vector<BinaryTreeNode *> s, path
    s = []
    path = []
    while not s.empty() or root!=None:
        while root!=None:
            s.append(root)
            path.append(root)
            root = root.left
        if not s.empty():
            root = s.back()
            s.pop_back()
            if root.right==None:
                # root is leaf node, calculate sum
                sum = 0
                for i in range(0, len(path)):
                    sum += path[i].data
                if sum==k:
                    for i in range(0, len(path)):
                        print(path[i].data, end=' ')
                    print()
                # pop from path untill path is s
                if not s.empty():
                    while path.back()!=s.back():
                        path.pop_back()
            root = root.right

# Problem ID 1600, largestBSTSubtree
#def largestBSTSubtree(BinaryTreeNoderoot, &minV, &maxV, & ht):
def largestBSTSubtree(BinaryTreeNoderoot):
    # If function return True, subtree is BST with ht, minV and maxV updated
    # If function returns False, subtree is not BST but ht has max height of BST
    if root==None:
        return True, INT_MAX, INT_MIN, 0
    if root.left==None and root.right==None:
        return True, root.data, root.data, 1
    leftIsBST, minLeft, maxLeft, htLeft = largestBSTSubtree(root.left) 
    rightIsBST, minRight, maxRight, htRight = largestBSTSubtree(root.right) 
    ht = max(htLeft,htRight)
    if leftIsBST and rightIsBST:
        if maxLeft < root.data and root.data <= minRight:
            # We have a BST
            return True, minLeft, maxRight, ht+1

    return False, 0, 0, ht

# Problem ID 1600, largestBSTSubtree
def largestBSTSubtree(root):
    # Given a Binary tree, find the largest BST subtree. That is, you need to
    # find the BST with maximum height in the given binary tree.
    isBST, minV, maxV, ht = largestBSTSubtree(root)
    return ht

# Problem ID 1600, replaceWithLargerNodesSum
def replaceWithLargerNodesSum(root, increment):
    if root==None:
        return 0
    sumRight = replaceWithLargerNodesSum(root.right, increment)
    rootData = root.data
    root.data += sumRight + increment
    sumLeft = replaceWithLargerNodesSum(root.left, root.data)
    return sumLeft + rootData + sumRight

# Problem ID 1600, replaceWithLargerNodesSum
def replaceWithLargerNodesSum(root):
    # Given a binary search tree, replace each nodes' data with the sum of all
    # nodes' which are greater or equal than it. You need to include the current
    # node's data also. 
    # That is, if in given BST there is a node with data 5, you need to replace
    # it with sum of its data (i.e. 5) and all nodes whose data is greater than
    # or equal to 5.
    replaceWithLargerNodesSum(root, 0)

# This is my understanding of problem
def replaceWithLargerNodesSumPravesh(root):
    # Given a binary search tree, replace each nodes' data with the sum of all
    # nodes' which are greater or equal than it. You need to include the current
    # node's data also. 
    # That is, if in given BST there is a node with data 5, you need to replace
    # it with sum of its data (i.e. 5) and all nodes whose data is greater than
    # or equal to 5.
    if root==None:
        return
    replaceWithLargerNodesSum(root.left)
    if root.right:
        replaceWithLargerNodesSum(root.right)
        root.data += root.right.data

def printNodesSumToS(root,node,s):
    pass

# Problem ID 1600, printNodesSumToS
def printNodesSumToS(root, s):
    # a binary search tree and a integer S, find pair of nodes in the BST
    # which sum to S. You can use extra space only O(log n).
    # Assume BST contains all unique elements.
    # Note: In a pair, print the smaller element first with utput format: Each
    # pair in different line (pair elements separated by space)
    if root==None:
        return
    pair = s - root.data
    if pair<root.data and searchInBST(root.left, pair)!=None:
        print(pair, root.data)
    if pair>=root.data and searchInBST(root.right, pair)!=None:
        print(root.data, pair)

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
#node=searchInBST(root, k)
#if node:
#    print(node.data)
#k1, k2 = (int(i) for i in input().strip().split())
#elementsInRangeK1K2(root, k1, k2)
#ll=sortedLLFromBST(root)
#printll(ll)
#lst=[int(i) for i in input().strip().split()]
#root=constructBST(lst)
#preOrder(root)
#print('true') if isBST(root) else print('false')
#insertDuplicateNode(root)
#printLevelATNewLine(root)
#print(lcaBinaryTree(root, k1, k2))
#print(lcaInBST(root, k1, k2))
#nodesSumToS(root, k)
rootToLeafPathsSumToK(root, k, [])
