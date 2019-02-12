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

def diameterNDepth(root):
    # First has diameter and second has depth
    dia, depth = 0, 0
    if root==None:
        return dia, depth
    leftDia, leftDepth = diameterNDepth(root.left)
    rightDia, rightDepth = diameterNDepth(root.right)
    depth = 1+max(leftDepth, rightDepth)    # Calculating depth
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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(diameter2(root))
