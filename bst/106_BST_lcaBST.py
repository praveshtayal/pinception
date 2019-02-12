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

# Problem ID 1600, searchInBST
def searchInBST(root, k):
    # Given a BST and an integer k. Find if the integer k is present in given
    # BST or not. Return the node with data k if it is present, return null
    # otherwise. Assume that BST contains all unique elements.
    if root==None:
        return None
    if root.data==k:
        return root
    if k < root.data:
        return searchInBST(root.left, k)
    else:
        return searchInBST(root.right, k)

# Problem ID 106, lcaInBST
def lcaInBST(root, val1, val2):
    # Given a BST and two nodes, find LCA (Lowest Common Ancestor) of
    # the given two nodes in BST. Read about LCA if you are having
    # doubts about the definition. If out of 2 nodes only one node is present,
    # return that node. If both are not present, return -1.
    if root==None:
        return -1
    # Ensure val1 <= val2. If not swap them
    if val1>val2:
        val1, val2 = val2, val1
    node1 = searchInBST(root, val1)
    node2 = searchInBST(root, val2)
    if node1==None:
        if node2==None:
            return -1
        else:
            return node2.data
    # node1 is not null
    if node2==None:
        return node1.data
    # node2 is not null
    if node1 == node2:
        return node1.data
    # Here we are sure that we have two distinct nodes present in the tree. Now,
    # we can start from root and traverse the tree untill we get the LCA Node
    curr = root
    while curr != None:
        if val1 <= curr.data and curr.data <= val2:
            return curr.data
        # Both node1 and node 2 are in some subtree
        if val2 < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    # This code should never be executed if given tree is a BST
    return -1

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k1, k2 = (int(i) for i in input().strip().split())
print(lcaInBST(root, k1, k2))
