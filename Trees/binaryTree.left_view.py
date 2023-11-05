class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def leftSideView(root):
    res = []
    def sideView(node, level, res):
        if not node:
            return
        
        if level == len(res):
            res.append(node.val)

        sideView(node.left, level+1, res)
        sideView(node.right, level+1, res)

    sideView(root, 0, res)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

res = leftSideView(root)
print(res)