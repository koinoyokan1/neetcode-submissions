class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.eow = False

class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        p = self.trie
        for c in word:
            c = ord(c) - ord('a')
            if not p.children[c]: p.children[c] = TrieNode()
            p = p.children[c]
        p.eow = True

    def search(self, word: str) -> bool:
        p = self.trie
        for c in word:
            c = ord(c) - ord('a')
            if not p.children[c]: return False
            p = p.children[c]
        return p.eow

    def startsWith(self, prefix: str) -> bool:
        p = self.trie
        for c in prefix:
            c = ord(c) - ord('a')
            if not p.children[c]: return False
            p = p.children[c]
        return True        
        