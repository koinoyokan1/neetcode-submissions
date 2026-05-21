class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = self.tail = None
        self.cap = capacity
        self.curr = 0

    def removeNode(self, node):
        if node.left: node.left.right = node.right
        else: self.head = node.right

        if node.right: node.right.left = node.left
        else: self.tail = node.left

    def addNodeToEnd(self, node):
        node.left = node.right = None
        if self.tail == None: 
            self.tail = node
            self.head = node
            return
        
        node.left = self.tail
        node.right = None
        self.tail.right = node
        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.removeNode(node)
        self.addNodeToEnd(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if not key in self.cache:
            self.curr += 1
            node = Node(key, value)
            self.addNodeToEnd(node)

            if self.curr > self.cap: 
                del self.cache[self.head.key]
                self.removeNode(self.head)
                self.curr -= 1

            self.cache[key] = node
            return

        node = self.cache[key]
        node.val = value

        self.removeNode(node)
        self.addNodeToEnd(node)
        self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)