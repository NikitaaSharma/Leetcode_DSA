class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lca(node, p, q):
    if not node:
        return None

    if node.key == p or node.key == q:
        return node

    left = lca(node.left, p, q)
    right = lca(node.right, p, q)

    if left and right:
        return node

    return left or right


root = Node(3)
root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

root.right.left = Node(0)
root.right.right = Node(8)

res = lca(root, 5, 4)
print(f'lowest common ancestor is {res.key}')