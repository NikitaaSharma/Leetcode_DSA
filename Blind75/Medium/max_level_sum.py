"""
link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxLevelSum(root):
    if not root:
        return 0

    level = 1
    max_level = 1
    max_sum = float("-inf")
    queue = [root]

    while queue:
        level_sum = 0

        for _ in range(len(queue)):
            curr = queue.pop(0)

            level_sum += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

        level +=1
    return max_level


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
res = maxLevelSum(root)
print(res)