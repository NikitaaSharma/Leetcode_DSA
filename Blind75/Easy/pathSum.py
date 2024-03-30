class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
def hasPathSum(root, targetSum) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        return targetSum == root.val
    
    leftSum = hasPathSum(root.left, targetSum - root.val)
    rightSum = hasPathSum(root.right, targetSum - root.val)

    return leftSum or rightSum
root = Node(10)
root.left = Node(1)
root.right = Node(5)

root.left.left = Node(10)
root.left.right = Node(8)

root.right.right = Node(3)

root.left.left.right = Node(6)
root.left.right.right = Node(7)

targetSum = 67

# root = [10,1,5,10,8,None, 3, None, 6, None, 7]
res = hasPathSum(root, targetSum)
print(res)