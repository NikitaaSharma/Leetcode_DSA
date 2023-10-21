class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseLinkedList(self):
        curr = self.head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

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
llist.add(10)
llist.add(20)
llist.add(30)
llist.add(40)
llist.add(50)
llist.add(60)
print("Given list")
llist.printllist()
llist.reverseLinkedList()
print("\nreversed list")
llist.printllist()