#Create a new list list3 with temp pointer and check the value of list1 and l2, insert the lesser value and move next

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def mergeLinkedList(self, list1, list2):
        list3 = Node(0)
        temp = list3

        l1 = list1.head
        l2 = list2.head

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = l1
            l1 = l1.next

        if l2:
            temp.next = l2
            l2 = l2.next

        return list3.next

    def add(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

    
llist = LinkedList()
llist.add(4)
llist.add(2)
llist.add(1)
print("Given list1")
llist.printllist()
llist2 = LinkedList()
llist2.add(4)
llist2.add(3)
llist2.add(1)
print("Given list2")
llist2.printllist()
merged_list_head = llist.mergeLinkedList(list1=llist, list2=llist2)

llist3 = LinkedList()
llist3.head = merged_list_head
print("-_______")
llist3.printllist()