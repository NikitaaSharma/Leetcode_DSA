class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def removeKthNode(self, k):
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next

        if not fast:
            self.head.value = self.head.next.value
            self.head.next = self.head.next.next
            return
        
        while fast.next:
            slow = slow.next
            fast = fast.next

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
llist.add(7)
llist.add(6)
llist.add(5)
llist.add(4)
llist.add(3)
llist.add(2)
llist.add(1)
print("Given list")
llist.printllist()
llist.removeKthNode(7)
print("\nAfter removing kth node list")
llist.printllist()