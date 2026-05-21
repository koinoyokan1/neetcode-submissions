"""
  /
 node[26]
"""
class Node:
    def __init__(self):
        self.mp = [None] * 26
        self.isEow = False 

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            c = ord(c) - ord('a')
            if not node.mp[c]:
                node.mp[c] = Node()
            node = node.mp[c]
        node.isEow = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            c = ord(c) - ord('a')
            if not node.mp[c]: return False
            node = node.mp[c]
        return node.isEow

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            c = ord(c) - ord('a')
            if not node.mp[c]: return False
            node = node.mp[c]
        return True      
        