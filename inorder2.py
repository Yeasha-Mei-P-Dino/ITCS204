class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = TreeNode('3')
nodeA = TreeNode('15')
nodeB = TreeNode('16')
nodeC = TreeNode('17')
nodeD = TreeNode('18')
nodeE = TreeNode('19')
nodeF = TreeNode('20')
nodeG = TreeNode('24')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
inOrderTraversal(root)