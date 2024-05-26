class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
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

    def swapNodes(self):
        slow = self.head
        fast = self.head.next
        prev = slow
        self.head = fast

        while fast and fast.next:
            fast.next, slow.next = slow, fast.next
            if fast != self.head:
                prev.next, prev = fast, slow

            slow = slow.next
            if slow is None:
                return self.head
            fast = slow.next

        return self.head
    
llist = LinkedList()
for i in range(50, 0, -10):
    llist.add(i)

llist.printll()
llist.swapNodes()
print("\n")
llist.printll()