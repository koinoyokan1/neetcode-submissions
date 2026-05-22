class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.eow = False

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        p = self.trie
        for c in word:
            c = ord(c) - ord('a')
            if not p.children[c]: p.children[c] = Trie()
            p = p.children[c]
        p.eow = True
        
    def search(self, word: str) -> bool:
        def _search(start, p):
            if start == len(word): return p.eow
            for i in range(start, len(word)):
                c = word[i]
                if c == '.': 
                    for x in range(26):
                        if p.children[x]:
                            if _search(i+1, p.children[x]): return True
                    return False

                c = ord(c) - ord('a')
                if not p.children[c]: return False
                p = p.children[c]
            return p.eow  

        p = self.trie
        return _search(0, self.trie)

               
