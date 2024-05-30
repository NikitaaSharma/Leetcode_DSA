from collections import deque
"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Sol: BFS
"""
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.next = None

class Tree:
    def print_tree(self, node) : 
        if (node == None):  
            return   
        print(node.key, end=" ")
        self.print_tree(node.left)  
        self.print_tree(node.right)
        self.print_tree(node.next)
        

    def connect(self, root):
        if not root:
            return

        queue = deque()
        queue.append(root)

        while queue:
            prev = None
            size = len(queue)
            while (size > 0):
                node = queue.popleft()
                node.next = prev
                prev = node
                # append the right child first as that will be pointing to Null
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
                size -=1
        return root

root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(4)

print("Given tree")
res = Tree()
res.print_tree(root)
print("\n")
out = res.connect(root)

res.print_tree(out)