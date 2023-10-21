class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def removeMiddleNode(self):
        if not self.head or not self.head.next:
            return None

        slow = self.head
        fast = self.head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return self.head

    def add(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

    
llist = LinkedList()
llist.add(6)
llist.add(2)
llist.add(1)
llist.add(7)
llist.add(4)
llist.add(3)
llist.add(1)
print("Given list")
llist.printllist()
llist.removeMiddleNode()
print("\After removing duplicates list")
llist.printllist()