from typing import Optional


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def isSubtree(root: Optional[Node], subRoot: Optional[Node]):
    if not root:
        return False
    
    if isSameTree(root, subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSameTree(p, q):
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

root = Node(10)
root.left = Node(5)
root.right = Node(4)

root.left.left = Node(2)
root.left.right = Node(9)

subRoot = Node(5)
subRoot.left = Node(2)
subRoot.right = Node(9)

res = isSubtree(root, subRoot)
print(res)