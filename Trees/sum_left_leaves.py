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

def sumOfLeftLeaves(root):
    sum = 0

    if not root:
        return

    if root.left:
        if not root.left.left and not root.left.right:
            sum += root.left.key
        else:
            sum += sumOfLeftLeaves(root.left)

    if root.right:
        sum += sumOfLeftLeaves(root.right)
    return sum
    

root = Node(3)
root.left = Node(9)
root.right = Node(20)

root.right.left = Node(15)
root.right.right = Node(7)

printTree(root)
res = sumOfLeftLeaves(root)
print(f'Sum of left leaves: {res}')
