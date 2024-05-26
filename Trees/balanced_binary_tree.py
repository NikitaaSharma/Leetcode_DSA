# A binary tree is balances if:
#1. the height difference between it's left and right subtree is < 1
#2. the left subtree is balances and 3. the right subtree is balances

# in an AVL tree the difference between left subtree and right subtree height is at most one.

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


    def height(self, root):
        if root is None:
            return True
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if left_height == -1 or right_height == -1:
            return -1
        elif abs(left_height - right_height) > 1:
            return -1
        
        return 1+max(left_height, right_height)

    def isBalanced(self, root):
        return self.height(root) != -1
    
    # Print preorder
def printTree(root):
    print(root.key, end=" ")
    printTree(root.left)
    printTree(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(4)

res = root.isBalanced(root)
print(res)

printTree(root)

