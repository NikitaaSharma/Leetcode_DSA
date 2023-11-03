class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def maxDepth(self, root):
        if not root:
            return 0
        
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        return max(maxLeft, maxRight) + 1
    

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

res = root.maxDepth(root)
print(res)