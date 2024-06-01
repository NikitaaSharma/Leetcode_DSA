class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        self.cap = capacity
        self.cache_map = {}
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, newnode):
        #have a temp node - pointed to wherever head was pointing
        temp =self.head.next

        #newnodes's next will point to temp
        newnode.next = temp

        #newnode's previous will point to head
        newnode.prev = self.head

        #make the head point to new node
        self.head.next = newnode

        #lastly, temps previous will point to newnode
        temp.prev = newnode

    def remove(self, delnode):
        #two pointers to keep track of left and right node
        left_node = delnode.prev
        right_node = delnode.next
        left_node.next = right_node
        right_node.prev = left_node

    def get(self, key):
        # Check first if the key exists in hashMap
        if key in self.cache_map:
            # get the node from the map
            node = self.cache_map[key]
            # answer would be the value of the node
            answer = node.value
            #delete it from the hashMap
            del self.cache_map[key]
            # we delete the node from wherever it is in the linked list
            self.remove(node)
            # and insert in right after the head
            self.insert(node)
            # update the cache with the new address which is self.head.next
            self.cache_map[key] = self.head.next
            return answer
        return -1

    def put(self, key, value):
        if key in self.cache_map:
            node = self.cache_map[key]
            # delete the node from hashMap and linkedlist
            del self.cache_map[key]
            self.remove(node)

        #len of hashMap becomes equal to capacity, we need to remove the lru element from hashMap and linkedlist
        if len(self.cache_map) == self.cap:
            lru = self.tail.prev.key
            del self.cache_map[lru]
            self.remove(self.tail.prev)

        new_node = self.Node(key, value)
        self.insert(new_node)
        self.cache_map[key] = self.head.next

    def printll(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print(" ")

lru_cache = LRUCache(3)
lru_cache.put(1,1)
lru_cache.printll()
lru_cache.put(2,2)
lru_cache.printll()
ans = lru_cache.get(1)
print(ans)
lru_cache.put(3,3)
lru_cache.printll()
ans = lru_cache.get(2)
print(ans)
lru_cache.put(4,4)
lru_cache.printll()
ans = lru_cache.get(1)
print(ans)
ans = lru_cache.get(3)
print(ans)
ans = lru_cache.get(4)
print(ans)
