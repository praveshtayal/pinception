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

# Main
levelOrder = [int(i) for i in input().strip().split()]
x=int(input())
root = buildLevelTree(levelOrder)
print(countNodesGreaterThanX(root, x))
