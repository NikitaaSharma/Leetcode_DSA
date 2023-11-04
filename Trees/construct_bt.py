# construct a binary tree from the given preorder and inorder traversal
# in preorder -- root --> left --> right (so the first element is alwyas the root)
# in inorder - left --> root --> right (so everything on the left side of root is left subtree and right side is right subtree.)
# we get the first element from the preorder array and find it in the inorder array, everything from 0 till that root index is 
# left subtree and eveyrthing after that root index till the end is right subtree.
# do this recursively for every node

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def constructBT(preorder, inorder):
    if inorder:
        #find the index of the first element of preorder in inorder
        INDEX = inorder.index(preorder.pop(0))
        #Now set that as root
        root = TreeNode(inorder[INDEX])
        #Everything at the lft side of inorder array from the roor index would be the left subtree
        root.left = constructBT(preorder, inorder[:INDEX])
        #Everything at the right side of inorder array fromt he root index would be the right subtree
        root.right = constructBT(preorder, inorder[INDEX+1:])
        return root

def print_tree(node) : 
    if (node == None):  
        return   
    print(node.val, end=" ")
    print_tree(node.left)  
    print_tree(node.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
bt = constructBT(preorder, inorder)
print_tree(bt)