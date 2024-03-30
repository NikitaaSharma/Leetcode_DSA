class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
        else:
            self.map.append([key, value])

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj)

obj.put(1,1)
print(obj)
param_2 = obj.get(1)
print(param_2)
# obj.remove(key)