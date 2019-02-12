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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(maxDataNode(root).data)
