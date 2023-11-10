class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None


def printTopView(node, ver, level, res):
    if not node:
        return

    if ver not in res or level < res[ver][1]:
        res[ver] = (node.val, level)

    printTopView(node.left, ver -1, level + 1, res)
    printTopView(node.right, ver +1, level + 1, res)


def topView(root):
    dict_map = {}
    printTopView(root, 0, 0, dict_map)
    for i in sorted(dict_map.keys()):
        print(dict_map.get(i)[0], end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

topView(root)