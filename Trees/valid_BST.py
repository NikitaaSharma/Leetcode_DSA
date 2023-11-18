class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):
    def validBST(node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return validBST(node.left, min_val, node.val) and validBST(node.right, node.val, max_val)
    
    return validBST(root, float("-inf"), float("inf"))

root = Node(5)
root.left = Node(1)
root.right = Node(4)

res = isValidBST(root)
print(res)