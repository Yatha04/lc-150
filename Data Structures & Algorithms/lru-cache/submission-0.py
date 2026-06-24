class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insertFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    

    def get(self, key: int) -> int:
        #if key not in dict = return -1
        #else: node = map[key]
        #remove node from it's position and add it to the start
        #return node.value
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insertFront(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        #if key already in dict:
        #node = map[key]
        #node.value = key
        #remov node from its pos and move it to the front

        #else:
        #create new node and insert it in the front
        #map[key] = node
        #if len(map) > capacity:
        #lru = tail.prev
        #remove lru: delete map[lru.key]
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._insertFront(node)

        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
        
        
