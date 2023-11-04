class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


def isSubtree(tree, subtree):
    def isMatch(s,t):
        # AND condition needs to come first as if OR is put first, it will return true for leaf nodes.
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        if s.key == t.key:
            if isMatch(s.left, t.left) and isMatch(s.right, t.right):
                return True
            else:
                return False
            
    if isMatch(tree, subtree):
        return True
    if not tree:
        return False
    
    return isSubtree(tree.left, subtree) or isSubtree(tree.right, subtree)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root1 = TreeNode(2)
root1.left = TreeNode(4)
root1.right = TreeNode(5)

res = isSubtree(root, root1)
print(res)