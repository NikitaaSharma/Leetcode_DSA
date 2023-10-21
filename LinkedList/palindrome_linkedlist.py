class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def printll(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next

    def isPalindrome(self):
        if not self.head:
            return True
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev :
            if prev.val != self.head.val:
                return False
            
            self.head = self.head.next
            prev = prev.next
        return True

llist = LinkedList()
llist.add(1)
llist.add(2)
llist.add(1)
llist.add(2)
llist.add(1)
print("Given list:\n")
llist.printll()
print(llist.isPalindrome())