class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
 
# Reverses alternate k nodes and 
#returns the pointer to the new head node 

def kAltReverse(head, k) : 
    current = head 
    prev = None
    count = 0
    #1) reverse first k nodes of the linked list 
    while (current != None and count < k) : 
        next = current.next
        current.next = prev 
        prev = current 
        current = next
        count = count + 1;
    
    # 2) Now head position to the kth node. So change next of head to (k+1)th node
    if(head != None): 
        head.next = current 
 
    # 3) We do not want to reverse next k 
    # nodes. So move the current pointer to skip next k nodes 
    count = 0
    while(count < k - 1 and current != None ): 
        current = current.next
        count = count + 1

    # 4) Recursively call for the list 
    # starting from current.next. And make rest of the list as next of first node 
    if(current != None): 
        current.next = kAltReverse(current.next, k) 
 
    # 5) prev is new head of the input list 
    return prev 

def push(head_ref, new_data): 
    # allocate node 
    new_node = Node(new_data)
    # put in the data 
    # new_node.data = new_data 
    # link the old list of the new node 
    new_node.next = head_ref 
    # move the head to po to the new node 
    head_ref = new_node
    return head_ref
 
# Function to print linked list 
def printList(node): 
    count = 0
    while(node != None): 
        print(node.data, end = " ") 
        node = node.next
        count = count + 1

# Driver code
if __name__=='__main__':
    # Start with the empty list 
    head = None
    # create a list 1.2.3.4.5...... .20
    for i in range(20, 0, -1):
        head = push(head, i) 

    print("Given linked list ") 
    printList(head) 
    head = kAltReverse(head, 3) 
 
    print("\nModified Linked list") 
    printList(head) 