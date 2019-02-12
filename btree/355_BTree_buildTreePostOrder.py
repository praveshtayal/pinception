import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Problem ID 355, Construct Tree from Postorder and Inorder
def buildTreePostOrder(postorder, inorder):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    postLength = len(postorder)
    inLength = len(inorder)
    if postLength!=inLength or postorder==None or inorder==None or postLength==0:
        return None
    root = BinaryTreeNode(postorder[-1])
    rootIndex = inorder.index(root.data)

    root.left = buildTreePostOrder(postorder[:rootIndex],inorder[:rootIndex])
    root.right = buildTreePostOrder(postorder[rootIndex:-1],inorder[rootIndex+1:])
    return root

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

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
