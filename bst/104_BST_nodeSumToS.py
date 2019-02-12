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

#def updateMap(root, unordered_map<int, int> &treemap):
def updateMap(root, treemap):
    if root==None:
        return
    treemap[root.data] = 1
    updateMap(root.left, treemap)
    updateMap(root.right, treemap)

# Problem ID 104, nodeSumToS
def nodesSumToS(root, S):
    # Given a binary tree and an integer S, print all the pair of nodes whose
    # sum equals S. Assume binary tree contains all unique elements. Note: In
    # a pair, print the smaller element first. Order of different pair doesn't
    # matter.
    if S<0:
        S *= -1
    treemap = {}
    updateMap(root, treemap)
    for num in treemap:
        if S-num in treemap and num<S-num:
            print(num, S-num)

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
nodesSumToS(root, k)
