class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def isSameTree(self, p, q):
        #if both trees are empty, they're identical
        if not p and not q:
            return True

        #if one of the tree is empty, not identical
        if not p or not q:
            return False
        
        #if node values are not same, return false
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(4)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)

root1.left.left = Node(3)
root1.left.right = Node(3)
root1.left.left.left = Node(4)
root1.left.left.right = Node(4)

res = root.isSameTree(root, root1)
print(res)