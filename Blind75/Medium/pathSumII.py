"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""

"""
Sol: Use DFS, recursion
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pathSum(root, targetSum):
    res = []

    def dfs(root, res, remainingSum, path):
        if not root:
            return
        
        path.append(root.val)
        
        if not root.left and not root.right and remainingSum == root.val:
            res.append(list(path))

        dfs(root.left, res, remainingSum - root.val, path)
        dfs(root.right, res, remainingSum - root.val, path)

        # backtracking
        path.pop()

    dfs(root, res, targetSum, [])
    return len(res)

root = Node(5)
root.left = Node(4)
root.right = Node(8)

root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)

root.right.left = Node(13)
root.right.right = Node(4)

root.right.right.left = Node(5)
root.right.right.right = Node(1)

targetSum = 22
res = pathSum(root, targetSum)
print(res)
