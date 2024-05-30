class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def printTree(root):
    if not root:
        return None
    
    print(root.key, end=" ")
    printTree(root.left)
    printTree(root.right)

def constructBSTFromArray(nums):
    n = len(nums)

    if not n:
        return None
    
    mid = (n-1)//2
    root = TreeNode(nums[mid])

    root.left = constructBSTFromArray(nums[:mid])
    root.right = constructBSTFromArray(nums[mid+1:])

    return root

nums = [-10,-3,0,5,9]
root = constructBSTFromArray(nums)
printTree(root)