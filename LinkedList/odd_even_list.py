class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def oddEven(self):
        if not self.head or not self.head.next:
            return None

        odd = self.head
        even = evenHead = self.head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
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
llist.oddEven()
print("\nOdd even list")
llist.printllist()