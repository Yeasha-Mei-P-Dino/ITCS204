class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

root = TreeNode('3')
nodeA = TreeNode('7')
nodeB = TreeNode('8')
nodeC = TreeNode('9')
nodeD = TreeNode('10')
nodeE = TreeNode('11')
nodeF = TreeNode('12')
nodeG = TreeNode('15')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
preOrderTraversal(root)