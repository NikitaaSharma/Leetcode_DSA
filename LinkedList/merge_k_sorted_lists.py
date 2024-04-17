lists = [[1,3,5], [1,5,8], [2,6,9]]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, newnodeVal):
        newnode = Node(newnodeVal)
        newnode.next = self.head
        self.head.next = newnode
    
    def printll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

    def mergeKSortedLl(self, lists):
        if not lists:
            return None
        
        return self.merge(lists, 0, len(lists)-1)
        
    def merge(self, lists, start, end):
        if start == end:
            return lists[start]
    
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid+1, end)

        return self.mergeSort(left, right)
        
    def mergeSort(self, left, right):
        dummyNode = Node(-1,-1)
        curr = dummyNode

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        while left:
            curr.next = left
            left = left.next
            curr = curr.next

        while right:
            curr.next = right
            right = right.next
            curr = curr.next

        return dummyNode.next