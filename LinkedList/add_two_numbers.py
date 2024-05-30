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
        l1 = list1.head
        l2 = list2.head
        while l1 or l2 or carry!=0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            new_val = val1 + val2 + carry
            carry = new_val // 10
            digit = new_val % 10
            temp.next = Node(digit)
            temp = temp.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

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

res = llist.addTwoNumbers(list1=llist, list2=llist2)
res.printllist()