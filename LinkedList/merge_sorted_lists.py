#Create a new list list3 with temp pointer and check the value of list1 and list2, insert the lesser value and move next

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
llist.add(10)
llist.add(20)
llist.add(30)
llist.add(40)
llist.add(50)
llist.add(60)
print("Given list1")
llist.printllist()
llist2 = LinkedList()
llist2.add(30)
llist2.add(60)
llist2.add(37)
llist2.add(43)
llist2.add(56)
llist2.add(62)
print("Given list2")
llist2.printllist()

llist3 = LinkedList()
llist3.mergeLinkedList(list1=llist, list2=llist2)
# print("\Merged list")
# llist3.printllist()