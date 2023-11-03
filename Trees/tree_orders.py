class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right= None

def printInorder(root):
    if root:
        #Inorder traversal = left -> node -> right
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

def printPreorder(root):
    if root:
        #Preorder  = node ->left ->right
        print(root.val, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)  

def printPostorder(root):
    if root:
        #Preorder  = node ->left ->right
        printPostorder(root.left)
        printPostorder(root.right)  
        print(root.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printInorder(root)
print(" ")
printPreorder(root)
print(" ")
printPostorder(root)