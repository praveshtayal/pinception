import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Problem ID 353, Level order traversal
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

def buildTreePreOrder(preorder, inorder):
    # Given Preorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 12 Nodes with following input:
    # preOrder: 1 2 3 4 15 5 6 7 8 10 9 12
    # inOrder: 4 15 3 2 5 1 6 10 8 7 9 12
    preLength = len(preorder)
    inLength = len(inorder)
    if preLength!=inLength or preorder==None or inorder==None or preLength==0:
        return None
    root = BinaryTreeNode(preorder[0])
    rootIndex = inorder.index(root.data)

    root.left = buildTreePreOrder(preorder[1:rootIndex+1],inorder[:rootIndex])
    root.right = buildTreePreOrder(preorder[rootIndex+1:],inorder[rootIndex+1:])
    return root

# Main
n=int(input())
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)
