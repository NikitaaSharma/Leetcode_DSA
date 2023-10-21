class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def removeDuplicates(self):
        curr = self.head
        while curr.next is not None:
            if curr.value == curr.next.value:
                curr.next = curr.next.next
            curr = curr.next
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
llist.add(10)
llist.add(20)
llist.add(20)
llist.add(40)
llist.add(40)
llist.add(60)
print("Given list")
llist.printllist()
llist.removeDuplicates()
print("\After removing duplicates list")
llist.printllist()