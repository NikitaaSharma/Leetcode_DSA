"""
Given a linked list, rotate the linked list at kth position from the end
eg: input: [1,2,3,4,5], k=2
output = 
i)[5,1,2,3,4]
ii) [4,5,1,2,3] <- res
"""
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printll(self):
        temp = self.head
        while temp:
            print(temp.key, end=" ")
            temp = temp.next

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def rotateList(self, k):
        if not self.head:
            return None
        
        lastNode = self.head
        size = 1
        while lastNode.next is not None:
            lastNode = lastNode.next
            size +=1

        lastNode.next = self.head
        k = k % 2

        temp = self.head
        for _ in range(size - k -1):
            temp = temp.next

        self.head = temp.next
        temp.next = None
        
        return self.head

llist = LinkedList()
llist.add(5)
llist.add(4)
llist.add(3)
llist.add(2)
llist.add(1)

llist.printll()
print(llist.rotateList(2))