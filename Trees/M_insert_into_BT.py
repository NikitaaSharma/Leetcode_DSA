"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node 
of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. 
You can return any of them.
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insertNode(root, val):
    if root is None:
        return TreeNode(val)
    
    if val > root.key:
        root.right = insertNode(root.right, val)
    else:
        root.left = insertNode(root.left, val)

    return root

def printTree(root):
    if not root:
        return
    
    print(root.key, end=" ")
    printTree(root.left)
    printTree(root.right)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

printTree(root)
res = insertNode(root, 5)
printTree(res)
