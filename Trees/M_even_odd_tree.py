"""
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""
from collections import deque
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isEvenOdd(root):
    if not root:
        return True
    
    queue = deque()
    queue.append(root)
    level = 0

    while queue:
        prev_node = float("-inf") if level %2==0 else float("inf")
        for _ in range(len(queue)):
            node = queue.popleft()

            if level % 2 == 0 and (node.key % 2 == 0 or node.key <= prev_node) or (level % 2 != 0 and (node.key % 2 !=0 or node.key >= prev_node )):
                return False
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            prev_node = node.key

        level +=1

    return True


def printTree(root):
    if not root:
        return
    
    print(root.key, end=" ")
    printTree(root.left)
    printTree(root.right)

root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(4)

root.left.left = TreeNode(3)
root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)

root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(2)


# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(2)

# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)

# root.right.left = TreeNode(7)

res = isEvenOdd(root)
print(res)