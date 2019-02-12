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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
ll=sortedLLFromBST(root)
printll(ll)
