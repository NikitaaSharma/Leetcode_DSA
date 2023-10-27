# Two methods:
# - Use set to keep track of visitedNodes, if curr in visitedNodes, return True else add curr to set
# - TWO pointers, initialise slow and fast pointer, if slow == fast: return True else continue

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def hasCycle(self):
        visitedNodes = set()
        curr = self.head

        while curr:
            next = curr.next
            if curr in visitedNodes:
                return True
            visitedNodes.add(curr)
            curr = next
        return False


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
print(llist.hasCycle())