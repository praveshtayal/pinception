class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

import queue
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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(sumOfAllNodes(root))
