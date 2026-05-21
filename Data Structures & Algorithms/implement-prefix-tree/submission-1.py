class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        p = self.head

        for c in word:
            chr = ord(c) - ord('a')

            if not p.children[chr]: p.children[chr] = Node()
            p = p.children[chr]
        p.isEnd = True 

    def search(self, word: str) -> bool:
        p = self.head

        for c in word:
            chr = ord(c) - ord('a')
            if not p.children[chr]: return False
            p = p.children[chr]
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        p = self.head

        for c in prefix:
            chr = ord(c) - ord('a')
            if not p.children[chr]: return False
            p = p.children[chr]
        return True        
        