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

# Problem ID 107, rootToLeafPathsSumToK
# The function does not modify the lst
def rootToLeafPathsSumToK(root, k, lst):
    if root==None:
        return
    if root.left==None and root.right==None:
        # Reached leaf node
        if root.data==k:
            print(*lst, k)
        return
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left, k-root.data, lst)
    rootToLeafPathsSumToK(root.right, k-root.data, lst)
    lst.pop()

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
rootToLeafPathsSumToK(root, k, [])
