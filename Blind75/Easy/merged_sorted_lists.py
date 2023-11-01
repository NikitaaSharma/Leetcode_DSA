list1 = [1,2,4] 
list2 = [1,3,4]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

    def add(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def mergeSortedLists(self, list1, list2):
        list3 = LinkedList()
        temp = list3

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            temp.next = list1
            list1 = list1.next

        if list2:
            temp.next = list2
            list2 = list2.next

        return list3.next



list1 = LinkedList()
list1.add(4)
list1.add(2)
list1.add(1)


list2 = LinkedList()
list2.add(4)
list2.add(3)
list2.add(1)

