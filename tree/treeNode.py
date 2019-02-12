class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def countNodes(tree):
    if not tree:
        return 0
    count = 1 # The root node of tree exist
    for child in tree.children:
        count += countNodes(child)
    return count

def sumofNodes(tree):
    if not tree:
        return 0
    sum = tree.data # The root node of tree exist
    for child in tree.children:
        sum += sumofNodes(child)
    return sum

def maxDataNode(tree):
    if not tree:
        return None
    maxNode = tree # Assume that the root node has max Data
    for child in tree.children:
        temp = maxDataNode(child)
        if temp.data > maxNode.data:
            maxNode = temp
    return maxNode

def printNodesAtDepthK(tree, k):
    if not tree:
        return
    if k==0:
        print(tree.data)
        return
    for child in tree.children:
        printNodesAtDepthK(child, k-1)

def nodesGreaterThanX(tree, x):
    if not tree:
        return 0
    count = 0
    if tree.data > x:
        count = 1
    for child in tree.children:
        count += nodesGreaterThanX(child, x)
    return count

def leafNodeCount(tree):
    if not tree:
        return 0
    if len(tree.children) == 0:
        return 1
    count = 0
    for child in tree.children:
        count += leafNodeCount(child)
    return count

def postOrder(tree):
    if not tree:
        return
    for child in tree.children:
        postOrder(child)
    print(tree.data, end=' ')

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print('No of Nodes in the tree are: ', countNodes(tree))
print('Sum of Nodes in the tree is: ', sumofNodes(tree))
print('Max Data Node in the tree is: ', maxDataNode(tree).data)
k=1
print('Nodes at depth ', k, ' in the tree are: ')
printNodesAtDepthK(tree, k)
x=5
print('Nodes greater than ', x, ' in the tree are: ', nodesGreaterThanX(tree, x))
print('Leaf Nodes in the tree are: ', leafNodeCount(tree))
postOrder(tree)
print()
