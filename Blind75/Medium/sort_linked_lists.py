class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Split the list into two halves
        mid = slow
        prev.next = None
        # Recursively sort both halves
        l1 = self.sortList(head)
        l2 = self.sortList(mid)

        return self.merge(l1, l2)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
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
        if l2:
            temp.next = l2
        return dummy.next

    def add(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()  # for newline

# Example usage
llist = LinkedList()
llist.add(6)
llist.add(2)
llist.add(1)
llist.add(7)
llist.add(4)
llist.add(3)
llist.add(1)

print("Given list:")
llist.printllist()

res = llist.sortList(llist.head)

llist2 = LinkedList()
llist2.head = res

print("After sorting list:")
llist2.printllist()
