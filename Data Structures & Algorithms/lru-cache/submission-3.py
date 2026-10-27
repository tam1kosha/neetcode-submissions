class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        # key (node key) : value (node)

        self.LRU, self.MRU = Node(0, 0), Node(0, 0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.MRU.prev, self.MRU
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]
        
