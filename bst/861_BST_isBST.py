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
# Problem ID 861, isBST
def isBST(root):
    return isBSTandInRange(root, INT_MIN, INT_MAX)

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print('true') if isBST(root) else print('false')
