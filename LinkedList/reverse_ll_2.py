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

    def reverseAtNodes(self, left, right):
        dummy_node = Node(0)
        dummy_node.next = self.head
        leftPrev = dummy_node
        curr = self.head
        for _ in range(left -1):
            leftPrev = leftPrev.next
            curr = curr.next

        rev_head = curr
        prev = None

        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        leftPrev.next = prev
        rev_head.next = curr

        return dummy_node.next

llist = LinkedList()
llist.add(7)
llist.add(6)
llist.add(5)
llist.add(4)
llist.add(3)
llist.add(2)
llist.add(1)
print("Given list:\n")
llist.printll()
print(llist.reverseAtNodes(2,4))
llist.printll()