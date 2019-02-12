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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(countLeafNodes(root))
