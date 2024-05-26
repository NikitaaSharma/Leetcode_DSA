from collections import deque
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def printTree(root):
    if not root:
        return
    
    print(root.key, end=" ")
    printTree(root.left)
    printTree(root.right)

def deepestLevelSum(root):
    if not root:
        return 0
    
    q = deque()
    q.append(root)
    while q:
        curr_level_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            curr_level_sum += node.key

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return curr_level_sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)
root.left.left.left = Node(7)
root.right.right.right = Node(8)

printTree(root)
res = deepestLevelSum(root)
print(f"Sum at the deepest level is: {res}")