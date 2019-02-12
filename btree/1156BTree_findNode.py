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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
x=int(input())
present=isNodePresent(root, x)
if present:
    print('true')
else:
    print('false')
