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

def searchInBinaryTree(root, x):
    if root==None:
        return None
    if root.data == x:
        return root
    result = searchInBinaryTree(root.left, x)
    if result!=None:
        return result
    result = searchInBinaryTree(root.right, x)
    return result

# Problem ID 513, lcaBinaryTree
def lcaBinaryTree(root, val1, val2):
    # Given a Binart Tree and two nodes, find LCA (Lowest Common Ancestor) of
    # the given two nodes in Binart Tree. Read about LCA if you are having
    # doubts about the definition. If out of 2 nodes only one node is present,
    # return that node. If both are not present, return -1.
    if root==None:
        return -1
    node1 = searchInBinaryTree(root, val1)
    node2 = searchInBinaryTree(root, val2)
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
        # If both nodes are present in left tree
        node1 = searchInBinaryTree(curr.left, val1)
        node2 = searchInBinaryTree(curr.left, val2)
        if node1!=None and node2!=None:
            curr = curr.left
            continue
        # If both nodes are present in right tree
        #node1 = searchInBinaryTree(curr.right, val1)
        #node2 = searchInBinaryTree(curr.right, val2)
        if node1==None and node2==None:
            curr = curr.right
            continue
        return curr.data
    # This code should never be executed
    return -1

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k1, k2 = (int(i) for i in input().strip().split())
print(lcaBinaryTree(root, k1, k2))
