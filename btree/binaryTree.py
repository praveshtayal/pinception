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

# Problem ID 351, Sum of all Nodes
def sumOfAllNodes(root):
    # Given a binary tree, find and return the sum of all nodes.
    if root==None:
        return 0
    result = root.data # root node
    result += sumOfAllNodes(root.left)
    result += sumOfAllNodes(root.right)
    return result

# Problem ID 1153, Max Data Node
def maxDataNode(root):
    # Given a Binary Tree, find and return the node with maximum data. Return
    # the complete node. Return null is binary tree is empty.
    if root==None:
        return None
    left = maxDataNode(root.left)
    right = maxDataNode(root.right)
    # We are using root as temporary pointer to hold the resultant node
    if left!=None and root.data < left.data:
        root = left
    if right!=None and root.data < right.data:
        root = right
    return root

# Problem ID 1154, Count Leaf Nodes
def countLeafNodes(root):
    # Given a Binary Tree, find and return the count of leaf nodes. Leaf nodes
    # are those, who don't have any children. Root is also leaf node if both its
    # child are null.
    if root==None:
        return 0
    if root.left == None and root.right == None:
        return 1 # root node
    return countLeafNodes(root.left) + countLeafNodes(root.right)

# Problem ID 1155, Count Nodes Greater than x
def countNodesGreaterThanX(root, x):
    # Given a Binary Tree and an integer x, find and return the count of nodes
    # which are having data greater than x.
    if root==None:
        return 0
    result = 0
    if root.data > x:
        result += 1
    result += countNodesGreaterThanX(root.left,x)
    result += countNodesGreaterThanX(root.right,x)
    return result

# Problem ID 1156, Find a node with value x
def isNodePresent(root, x):
    # Given a Binary Tree and an integer x, check if node with data x is present
    # in the input binary tree or not. Return True or False.
    if root==None:
        return False
    if root.data == x:
        return True
    if isNodePresent(root.left, x):
        return True
    if isNodePresent(root.right, x):
        return True
    return False

# Problem ID 580, mirror a binary tree
def mirrorBinaryTree(root):
    # Mirror the given binary tree. That is, right child of every nodes should
    # become left and left should become right.
    if root==None:
        return
    left = root.left
    root.left = root.right
    root.right = left
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)

def depth(root):
    # Used internally by diameter and other functions
    if root==None:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    return max(left,right)+1

def depthDiff(root):
    # Presently Unused. But may be used by isBalanced
    if root==None:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    diff = left-right
    if diff<0:
        diff *= -1
    max = left if left>right else right
    return max+1

def diameterNDepth(root):
    # First has diameter and second has depth
    dia, depth = 0, 0
    if root==None:
        return dia, depth
    leftDia, leftDepth = diameterNDepth(root.left)
    rightDia, rightDepth = diameterNDepth(root.right)
    depth.second = 1+max(leftDepth, rightDepth)    # Calculating depth
    diameterwithRoot = leftDepth + rightDepth + 1
    dia = max(leftDia, rightDia, diameterwithRoot)
    return dia, depth

def diameter2(root):
    dia, depth = diameterNDepth(root)
    return dia

# Problem ID 1157, Find Diameter option 1
def diameter(root):
    # Given a Binary Tree, find and return the diameter of input binary tree.
    # Diameter is - largest count of nodes between any two leaf nodes in the
    # binary tree (both the leaf nodes are inclusive). 
    # if there is only one node, diameter = 1 
    # if there are two nodes, diameter = 2
    if root==None:
        return 0
    leftDia = diameter(root.left)
    rightDia = diameter(root.right)
    d = depth(root.left) + depth(root.right) + 1
    return max(leftDia,rightDia,d)

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value
def minMax(root):
    # Given a binary tree, find and return the min and max data value of given
    # binary tree. Return the output as an object of PairAns class, which is
    # already created.
    minimum, maximum =  INT_MIN, INT_MAX
    if root==None:
        return minimum, maximum
    # Initialize answer as root node data
    leftMin, leftMax = minMax(root.left)
    rightMin, rightMax = minMax(root.right)
    minimum = min(root.data, leftMin, rightMin)
    maximum = max(root.data, leftMax, rightMax)
    return minimum, maximum

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

# Problem ID 1568, print level wise tree
def inOrderRecursive(root):
    if root==None:
        return
    inOrderRecursive(root.left)
    print(root.data, end=' ')
    inOrderRecursive(root.right)

# Problem ID 1565, preorder Recursive
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Problem ID 1566, postorder Recursive
def postOrder(root):
    # Given a binary tree, print the postorder traversal of given tree.
    # Post-order traversal is: LeftChild RightChild Root
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=' ')

# Problem ID 100, Construct Tree from Preorder and Inorder
def buildTreePreOrder(preorder, inorder):
    # Given Preorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 12 Nodes with following input:
    # preOrder: 1 2 3 4 15 5 6 7 8 10 9 12
    # inOrder: 4 15 3 2 5 1 6 10 8 7 9 12
    preLength = len(preorder)
    inLength = len(inorder)
    if preLength!=inLength or preorder==None or inorder==None or preLength==0:
        return None
    root = BinaryTreeNode(preorder[0])
    rootIndex = inorder.index(root.data)

    root.left = buildTreePreOrder(preorder[1:rootIndex+1],inorder[:rootIndex])
    root.right = buildTreePreOrder(preorder[rootIndex+1:],inorder[rootIndex+1:])
    return root

# Problem ID 355, Construct Tree from Postorder and Inorder
def buildTreePostOrder(postorder, inorder):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    postLength = len(postorder)
    inLength = len(inorder)
    if postLength!=inLength or postorder==None or inorder==None or postLength==0:
        return None
    root = BinaryTreeNode(postorder[-1])
    rootIndex = inorder.index(root.data)

    root.left = buildTreePostOrder(postorder[:rootIndex],inorder[:rootIndex])
    root.right = buildTreePostOrder(postorder[rootIndex:-1],inorder[rootIndex+1:])
    return root

# Problem ID 79, is tree balanced
def isBalanced(root):
    # Given a binary tree, check if its balanced i.e. depth of left and right
    # subtrees of every node differ by at max 1. Return True if given binary
    # tree is balanced, False otherwise.
    if root==None:
        return True
    left = depth(root.left)
    right = depth(root.right)
    diff = abs(left-right)
    if diff>1:
        return False
    if not isBalanced(root.left):
        return False
    if not isBalanced(root.right):
        return False
    return True

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

# Problem ID 352, Remove Leaf Nodes
def removeLeafNodes(root):
    # Remove all leaf nodes from a given Binary Tree. Leaf nodes are those
    # nodes, which don't have any children.
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    
    root.left = removeLeafNodes(root.left)
    root.right = removeLeafNodes(root.right)
    return root

# Link List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Problem ID 78, Level wise linked list
#vector<node<int>*> createLLForEachLevel(root):
def createLLForEachLevel(root):
    # Given a binary tree, write code to create a separate linked list for each
    # level. You need to return the array which contains head of each level
    # linked list.
    #vector<node<int>*> result
    result = []
    if root==None:
        return result
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    # Here we want to add a link list into result
    #node<int> ptr = new node<int>(root.data)
    ptr = Node(root.data)
    result.append(ptr)
    while not inputQ.empty():
        #nodelist<int> list = new nodelist<int>()
        l = []
        while not inputQ.empty():
            curr = inputQ.get()
            if curr.left!=None:
                outputQ.put(curr.left)
                ptr = Node(curr.left.data)
                l.pushnode(ptr)
            if curr.right!=None:
                outputQ.put(curr.right)
                ptr = Node(curr.right.data)
                l.pushnode(ptr)
        inputQ, outputQ = outputQ, inputQ
        result.append(l.start)
    return result

# Problem ID 82, Zig Zag Order
def zigZagOrder(root):
    # Given a binary tree, print the zig zag order i.e print level 1 from left
    # to right, level 2 from right to left and so on. This means odd levels
    # should get printed from left to right and even level right to left.
    #vector<node<int>*> v = createLLForEachLevel(root)
    v = createLLForEachLevel(root)
    size= len(v)
    for i in range(0,size):
        #node<int> list = v[i]
        list = v[i]
        if i%2==0:
            # Print the list in forward order
            while list!=None:
                print(list.data, end=' ')
                list = list.next
            print()
        else:
            #vector<int> stack
            stack = []
            # Print the list in backward order
            while(list!=None):
                stack.push_back(list.data)
                list = list.next
            
            #for(j=stack.size()-1 j>=0 j--)
            for num in reversed(stack):
                print(num, end=' ')
            print()
        
# Problem ID 77, print nodes without sibling
def nodesWithoutSibling(root):
    # Given a binary tree, print all nodes that don’t have a sibling. Print the
    # elements in different lines. And order of elements doesn't matter.
    if root==None:
        return
    if root.left==None and root.right!=None:
        # right node has no sibling. Print right node and call recursion
        print(root.right.data, end=' ')
        nodesWithoutSibling(root.right)
        return
    
    if root.left!=None and root.right==None:
        # left node has no sibling. Print left node and call recursion
        print(root.left.data, end=' ')
        nodesWithoutSibling(root.left)
        return
    
    nodesWithoutSibling(root.right)
    nodesWithoutSibling(root.left)

#def updateMap(root, level, unordered_map<int, queue<int> > &m):
def updateMap(root, level, m):
    if root==None:
        return
    if level in m:
        m[level].append(root.data)
    else:
        m[level] = [root.data]
    updateMap(root.left, level-1, m)
    updateMap(root.right, level+1, m)

def printBinaryTreeVerticalOrder(root):
    # Print the binary tree in vertical order
    m = {}
    updateMap(root, 0, m)
    for l in m:
        for num in l:
            print(num, end=' ')
        print()

#def find(root, x, vector<>& v):
def find(root, x, v):
    # Given a Binary Tree and an integer x, check if node with data x is present
    # in the input binary tree or not. Return True or False.
    if root==None:
        return False
    v.push_back(root)
    if root.data == x:
        return True
    if find(root.left, x, v):
        return True
    if find(root.right, x, v):
        return True
    v.pop_back()
    return False

def printNodesatDistanceK(root, k):
    if root==None or k<0:
        return
    if k==0:
        print(root.data)
        return
    
    printNodesatDistanceK(root.left, k-1)
    printNodesatDistanceK(root.right, k-1)

def nodesAtDistanceKH(root, node, k):
    if root==None or k<0:
        return -1
    if root.data==node:
        printNodesatDistanceK(root, k)
        return 0
    
    distance = nodesAtDistanceKH(root.left, node, k)
    if distance != -1:
        # node found in left subtree
        if distance+1==k:
            print(root.data)
        printNodesatDistanceK(root.right, k-distance-2)
        return distance+1
    
    distance = nodesAtDistanceKH(root.right, node, k)
    if distance != -1:
        # node found in right subtree
        if distance+1==k:
            print(root.data)
        printNodesatDistanceK(root.left, k-distance-2)
        return distance+1
    
    return -1

def nodesAtDistanceK(root, node, k):
    nodesAtDistanceKH(root, node, k)

def nodesAtDistanceKOld(root, k):
    # Given a binary tree, a node and an integer K, print nodes which are at
    # K distance from the the given node.
    if root==None or k<0:
        return
    v = [] # v is empty vector
    #if find(root, node, v)==False) return    # Node doesn't exist
    curr = v.back()
    parent=None
    nodesAtDistanceKOld(curr,k)
    distance = 0
    while(not v.empty() and distance<k):
        curr = v.back()
        v.pop_back()
        if v.empty():
            break
        parent = v.back()
        sibling = None
        if parent.left==curr:
            sibling = parent.right
        else: 
            sibling = parent.left
        distance += 2
        nodesAtDistanceKOld(sibling,k-distance)
    
    if parent:
        print(parent.data)


def printNodesSumToS(root, s):
    # Given a binary search tree and a integer S, find pair of nodes in the BST
    # which sum to S. You can use extra space only O(log n).
    pass

# Main
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
balanced=isBalanced(root)
if balanced:
    print('true')
else:
    print('false')
