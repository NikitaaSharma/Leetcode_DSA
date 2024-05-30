class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def printll(self):
        temp = self.head
        while temp:
            random_val = temp.random.val if temp.random else "None"
            print(f"Value: {temp.val}, Random: {random_val}")
            temp = temp.next
        print()

    def copyRandomPointer(self):
        if not self.head:
            return 
        
        hashMap = {}

        curr = self.head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        curr = self.head
        while curr:
            hashMap[curr].next = hashMap.get(curr.next)
            hashMap[curr].random = hashMap.get(curr.random)
            curr = curr.next

        return hashMap[self.head]

llist = LinkedList()
node1 = llist.add(3)
node2 = llist.add(4)
node3 = llist.add(5)

node1.random = node3  # Node with value 3 points randomly to node with value 5
node2.random = node1  # Node with value 4 points randomly to node with value 3
node3.random = node2 

print("Original list:")
llist.printll()

# Copy the list
copied_list_head = llist.copyRandomPointer()

# Print the copied list
print("Copied list:")
copied_list = LinkedList()
copied_list.head = copied_list_head
copied_list.printll()