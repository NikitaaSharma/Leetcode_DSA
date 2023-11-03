class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def invertTree(root):
    if not root:
        return root
    
    invertTree(root.left)
    invertTree(root.right)

    root.left, root.right = root.right, root.left
    return root

# print InOrder binary tree traversal.
def print_tree(node) : 
  
    if (node == None):  
        return   
    print_tree(node.left)  
    print(node.key, end=" "),
    print_tree(node.right)

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

# Print inorder traversal of the input tree
print("Inorder traversal of the constructed tree is")  
print_tree(root)  
      
# Convert tree to its mirror
invertTree(root)  
  
# Print inorder traversal of the mirror tree
print("\nInorder traversal of the mirror treeis ")  
print_tree(root) 