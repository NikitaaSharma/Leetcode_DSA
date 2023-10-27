class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reorderedList(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        curr = middle
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        first = self.head
        second = prev

        while second.next:
            next_jump = first.next
            first.next = second
            first = next_jump

            next_jump = second.next
            second.next = first
            second = next_jump

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
llist.add(30)
llist.add(40)
llist.add(50)
llist.add(60)
print("Given list")
llist.printllist()
llist.reorderedList()
print("\Reordered list")
llist.printllist()