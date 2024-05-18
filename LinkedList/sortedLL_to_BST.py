"""
Given a linked list, rotate the linked list at kth position from the end
eg: input: [1,2,3,4,5], k=2
output = 
i)[5,1,2,3,4]
ii) [4,5,1,2,3] <- res
"""
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printll(self):
        temp = self.head
        while temp:
            print(temp.key, end=" ")
            temp = temp.next

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def sortedListToBST(self, head):
        if not self.head:
            return None
        if not self.head.next:
            return Tree(self.head.val)
        
        #find the middle of the LL
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev:
            prev.next = None

        root = Tree(slow.key)
        root.right = self.sortedListToBST(slow.next)
        root.left = self.sortedListToBST(self.head)
        return root

llist = LinkedList()
llist.add(9)
llist.add(5)
llist.add(0)
llist.add(-3)
llist.add(-5)
llist.sortedListToBST(llist)