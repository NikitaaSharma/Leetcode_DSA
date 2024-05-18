#Create a new list list3 with temp pointer and check the value of list1 and list2, insert the lesser value and move next

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, list1, list2):
        list3 = Node(0)
        temp = list3
        carry = 0
        while list1 or list2 or carry!=0:
            val1 = list1.val if list1 is not None else 0
            val2 = list2.val if list2 is not None else 0
            new_val = val1 + val2 + carry
            carry = new_val // 10
            digit = new_val % 10
            temp.next = Node(digit)
            temp = temp.next

            list1 = list1.next if list1 is not None else None
            list2 = list2.next if list2 is not None else None

        res = temp.next
        temp.next = None
        return res

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
llist.add(30)
llist.add(40)
llist.add(20)
print("Given list1")
llist.printllist()
llist2 = LinkedList()
llist2.add(4)
llist2.add(6)
llist2.add(3)
print("Given list2")
llist2.printllist()

llist3 = LinkedList()
llist3.mergeLinkedList(list1=llist, list2=llist2)
# print("\Merged list")
# llist3.printllist()