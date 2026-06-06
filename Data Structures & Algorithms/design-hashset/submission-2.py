class MyHashSet:

    def __init__(self):
        self.b = [[] for i in range(1000)]

    def add(self, key: int) -> None:
        h = key%1000
        if key in self.b[h]: return
        self.b[h].append(key)

    def remove(self, key: int) -> None:
        h = key%1000
        if key in self.b[h]:
            self.b[h].remove(key)       

    def contains(self, key: int) -> bool:
        h = key%1000
        return key in self.b[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)