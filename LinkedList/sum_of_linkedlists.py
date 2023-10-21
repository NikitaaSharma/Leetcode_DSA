class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sumOfLinkedList(self, LinkedList1, Linkedlist2):
        
        pass

    def add(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

    
llist1 = LinkedList()
llist2 = LinkedList()
llist1.add(1)
llist1.add(7)
llist1.add(4)
llist1.add(2)
print("Linked list1")
llist1.printllist()
llist2.add(5)
llist2.add(4)
llist2.add(9)
print("Linked list2")
llist2.printllist()

