class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def levelOrder(self, root):
        #DO BFS
        queue = []
        res = []

        if root:
            queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.key)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(level)

        return res
    

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

res = root.levelOrder(root)
print(res)