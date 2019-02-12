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

def depth(root):
    # Used internally by diameter and other functions
    if root==None:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    return max(left,right)+1

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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
balanced=isBalanced(root)
if balanced:
    print('true')
else:
    print('false')
