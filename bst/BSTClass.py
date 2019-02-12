import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BinaryTreeNode(value)
        if self.root==None:
            self.root = node
            return
        curr=self.root
        prev=self.root
        while curr!=None:
            prev = curr
            if value<curr.data:
                curr = curr.left
            else:
                curr = curr.right
        # prev will have node as child
        if value < prev.data:
            # prev.left is None
            prev.left = node
        else:
            # prev.right is None
            prev.right = node

    def deleteData(self, value):
        if self.root==None:
            return False
        curr=self.root
        prev=None
        while curr!=None and curr.data != value:
            prev = curr
            if value<curr.data:
                curr = curr.left
            else:
                curr = curr.right

        # value not found
        if curr==None:
            return False

        # we have to delete node curr
        if curr.left and curr.right:
            # Special case where both subtrees of node to deleted exist
            # We can delete either largest of left subtree or 
            # smallest of right subtree. And replace the contents of curr
            # with content of deleted node. Here, we are deleting smallest
            # of right subtree.
            temp = curr.right
            smallest = temp.data
            while temp!=None:
                smallest = temp.data
                temp = temp.left
            BST.deleteData(self, smallest)
            curr.data = smallest
            return True

        # At least One subtree is empty
        if curr.left:
            # Right subtree is empty
            temp = curr.left
            if prev==None:
                # We are deleting the root node
                self.root = temp
                return True
            if prev.left==curr:
                prev.left = temp
            else:
                prev.right = temp
            return True
        temp = curr.right
        if prev==None:
            # We are deleting the root node
            self.root = temp
            return True
        if prev.left==curr:
            prev.left = temp
        else:
            prev.right = temp
        return True

    def hasData(self, value):
        if self.root==None:
            return False
        curr=self.root
        prev=self.root
        while curr!=None and curr.data != value:
            prev = curr
            if value<curr.data:
                curr = curr.left
            else:
                curr = curr.right
        # prev will have node as child
        if curr==None:
            return False
        return True
    def printTree(self):
        BST.__printTree(self.root)

    @staticmethod
    def __printTree(root):
        if root==None:
            return
        print(root.data,':', sep='', end='')
        if root.left:
            print("L:", root.left.data, ",", sep='', end='')
        if root.right:
            print("R:", root.right.data, sep='', end='')
        print()    
        BST.__printTree(root.left)
        BST.__printTree(root.right)

# Main
tree = BST()
getInput = True
while getInput:
    choice = int(input())
    if choice==1:
        value = int(input())
        tree.insert(value)
    elif choice==2:
        value = int(input())
        tree.deleteData(value)
    elif choice==3:
        value = int(input())
        if tree.hasData(value):
            print("true")
        else:
            print("false")
    elif choice==4:
        tree.printTree()
    else:
        tree.printTree()
        getInput = False
