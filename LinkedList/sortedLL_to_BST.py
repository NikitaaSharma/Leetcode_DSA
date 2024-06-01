class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printll(self):
        temp = self.head
        while temp:
            print(temp.key, end=" ")
            temp = temp.next
        print()
    
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def sortedListToBST(self):
        def find_middle(start):
            slow = start
            fast = start
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
        
        def sorted_list_to_bst(start):
            if not start:
                return None
            mid = find_middle(start)
            root = TreeNode(mid.key)
            if start == mid:
                return root
            root.left = sorted_list_to_bst(start)
            root.right = sorted_list_to_bst(mid.next)
            return root
        
        return sorted_list_to_bst(self.head)
    
    def printTree(self, root):
        if not root:
            return
        print(root.val, end=" ")
        self.printTree(root.left)
        self.printTree(root.right)

# Example usage for BST conversion
llist = LinkedList()
llist.add(9)
llist.add(5)
llist.add(0)
llist.add(-3)
llist.add(-10)
root = llist.sortedListToBST()
print("BST Preorder:")
llist.printTree(root)
print()

