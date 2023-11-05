class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):
    def validBST(root, min_val, max_val):
        if not root:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        return validBST(root.left, min_val, root.val) and validBST(root.right, root.val, max_val)
    
    return validBST(root, float("-inf"), float("inf"))

root = Node(5)
root.left = Node(1)
root.right = Node(4)

res = isValidBST(root)
print(res)