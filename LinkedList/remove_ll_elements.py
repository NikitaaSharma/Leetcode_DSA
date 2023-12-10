"""
Given a linked list and a value, remove that value from the linked list

"""

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
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next

    def removeElement(self, key):
        if not self.head:
            return self.head

        curr = self.head

        while curr and curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return self.head if self.head and self.head.val == key else self.head

list1 = LinkedList()
list1.add(1)
list1.add(2)
list1.add(3)
list1.add(4)
list1.add(2)
list1.add(6)
list1.add(2)

list1.printll()
key = 2
print(f'\nAfter removing {key} from the list')
list1.removeElement(key)
list1.printll()
