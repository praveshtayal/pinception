import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Problem ID 1565, preorder Recursive
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Problem ID 1159, constructBST
def constructBST(lst):
    # Given a sorted integer array A of size n which contains all unique
    # elements. You need to construct a balanced BST from this input array.
    # Return the root of constructed BST. If array size is even, take first mid
    # as root.
    n=len(lst)
    if lst==None or n<=0:
        return None
    rootIndex = (n-1)//2
    root = BinaryTreeNode(lst[rootIndex])
    root.left = constructBST(lst[:rootIndex])
    root.right = constructBST(lst[rootIndex+1:])
    return root

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)
