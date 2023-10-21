class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def maxTwinSum(self):
        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        
        max_sum = 0
        while slow and prev:
            max_sum = max(max_sum, (slow.value + prev.value))
            slow = slow.next
            prev = prev.next

        print(f"\nMax Twin sum is {max_sum}")

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
llist.add(5)
llist.add(3)
llist.add(7)
llist.add(2)
llist.add(10)
llist.add(2)
print("Given list")
llist.printllist()
llist.maxTwinSum()