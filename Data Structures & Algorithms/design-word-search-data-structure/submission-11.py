class Node:
    def __init__(self):
        self.ch = [None] * 26
        self.end = False

class WordDictionary:
    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        p = self.head

        for c in word:
            ch = ord(c) - ord('a')
            if not p.ch[ch]: p.ch[ch] = Node()
            p = p.ch[ch]
        p.end = True

    def _search(self, word, wordi, p):
        if wordi == len(word): return p.end

        c = word[wordi]

        if c == '.':
            for q in p.ch:
                if not q: continue
                if self._search(word, wordi+1, q): return True
            return False
            
        ch = ord(c) - ord('a')
        if not p.ch[ch]: return False

        return self._search(word, wordi+1, p.ch[ch])

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.head)






