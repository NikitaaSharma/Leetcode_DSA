class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def sortList(self, head):
        if not self.head or not self.head.next:
            return head

        # Find the middle of the linked list
        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Recursively sort both halves
        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        list3 = ListNode(0)
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
        new_data = ListNode(data)
        new_data.next = self.head
        self.head = new_data


    def printllist(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next


llist = LinkedList()
llist.add(6)
llist.add(2)
llist.add(1)
llist.add(7)
llist.add(4)
llist.add(3)
llist.add(1)
print("Given list")
llist.printllist()
llist.sortList(llist)
print("\nAfter sorting list")
llist.printllist()
